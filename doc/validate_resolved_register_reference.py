#!/usr/bin/env python3
"""Validate the public resolved Growatt register reference."""

# ruff: noqa: D103, T201

import argparse
from collections import Counter, defaultdict
import json

try:
    from .build_resolved_register_reference import (
        MARKDOWN_PATH,
        OUTPUT_PATH,
        STATUS_VALUES,
        build_reference,
        render_markdown,
    )
except ImportError:  # pragma: no cover - supports direct CLI execution
    from build_resolved_register_reference import (
        MARKDOWN_PATH,
        OUTPUT_PATH,
        STATUS_VALUES,
        build_reference,
        render_markdown,
    )


def fail(message: str) -> None:
    raise SystemExit(f"validation failed: {message}")


def strip_generation_time(reference: dict) -> dict:
    copy = json.loads(json.dumps(reference))
    copy["meta"].pop("generated_at", None)
    return copy


def record_map(reference: dict) -> dict[tuple[str, str, int], dict]:
    records = {}
    for record in reference.get("records", []):
        identity = (record.get("family"), record.get("table"), record.get("address"))
        if identity in records:
            fail(f"duplicate identity {identity}")
        records[identity] = record
    return records


def validate_contract(reference: dict) -> None:  # noqa: C901
    required = {
        "meta",
        "families",
        "records",
        "unresolved_or_conflicted_records",
        "summary",
        "resolution_model",
        "evidence_legend",
    }
    missing = required - set(reference)
    if missing:
        fail(f"missing top-level fields: {sorted(missing)}")
    records = record_map(reference)
    if not records:
        fail("reference contains no records")
    if not any(record["address"] == 0 for record in records.values()):
        fail("register 0 was filtered from every family/table")
    valid_access = {"R", "W", "R/W", "UNKNOWN"}
    for record in records.values():
        if record["table"] not in {"holding", "input"}:
            fail(f"invalid table in {record['id']}")
        if not isinstance(record["address"], int) or record["address"] < 0:
            fail(f"invalid address in {record['id']}")
        if record["resolution_status"] not in STATUS_VALUES:
            fail(f"invalid resolution status in {record['id']}")
        if record["access"] not in valid_access:
            fail(f"invalid access in {record['id']}")
        if (
            record["resolution_status"] != "UNKNOWN_RESERVED"
            and not record["provenance"]
        ):
            fail(f"missing provenance in {record['id']}")

    min_records = {
        (record["table"], record["address"]): record
        for record in records.values()
        if record["family"] == "min_tl_xh"
    }
    expected_holding = {
        3036: "Grid-first discharge power rate",
        3037: "Grid-first stop SOC",
        3047: "Battery-first charge power rate",
        3048: "Battery-first stop SOC",
        3049: "AC charge enabled",
        3081: "UPS/EPS frequency selection",
        3082: "Load-first stop SOC",
    }
    for address, name in expected_holding.items():
        record = min_records.get(("holding", address))
        if not record or record["canonical_name"] != name:
            fail(f"MIN holding {address} lost resolved meaning {name!r}")
    expected_input = {
        3036: "AC phase L3 power",
        3037: "AC phase L3 power",
        3081: "PV4 energy total",
        3082: "PV4 energy total",
    }
    for address, name in expected_input.items():
        record = min_records.get(("input", address))
        if not record or record["canonical_name"] != name:
            fail(f"MIN input {address} lost table-specific meaning {name!r}")
    for address in (3047, 3048):
        record = min_records.get(("input", address))
        if not record or record["canonical_name"] != "Inverter runtime":
            fail(f"MIN input {address} lost runtime meaning")
    bms = min_records.get(("input", 3217))
    if (
        not bms
        or bms["signed"] is not True
        or bms["divisor"] != 100
        or bms["unit"] != "A"
    ):
        fail("MIN input 3217 is not signed int16 / 100 A")
    if ("holding", 3217) not in min_records:
        fail(
            "MIN holding 3217 was removed instead of retaining the independent holding namespace"
        )

    summary = reference["summary"]
    actual_status = Counter(record["resolution_status"] for record in records.values())
    if summary["total_records"] != len(records):
        fail("summary total_records does not match records")
    for status in STATUS_VALUES:
        if summary["by_resolution_status"].get(status, 0) != actual_status.get(
            status, 0
        ):
            fail(f"summary status count mismatch for {status}")
    if summary["write_verified"] != 0:
        fail("write evidence was incorrectly promoted")

    family_counts = defaultdict(Counter)
    for record in records.values():
        family_counts[record["family"]][record["table"]] += 1
        family_counts[record["family"]][record["resolution_status"]] += 1
    for family in reference["families"]:
        actual = family_counts[family["id"]]
        coverage = family["coverage"]
        if coverage["total"] != sum(actual[table] for table in ("holding", "input")):
            fail(f"coverage total mismatch for {family['id']}")
        if (
            coverage["holding"] != actual["holding"]
            or coverage["input"] != actual["input"]
        ):
            fail(f"coverage table count mismatch for {family['id']}")
        for status in STATUS_VALUES:
            if coverage["by_resolution_status"].get(status, 0) != actual[status]:
                fail(f"coverage status mismatch for {family['id']} / {status}")


def validate_generated_files() -> None:
    if not OUTPUT_PATH.exists() or not MARKDOWN_PATH.exists():
        fail("generated JSON or Markdown output is missing")
    actual = json.loads(OUTPUT_PATH.read_text(encoding="utf-8"))
    expected = build_reference()
    if strip_generation_time(actual) != strip_generation_time(expected):
        fail("JSON output is stale or not reproducible")
    if MARKDOWN_PATH.read_text(encoding="utf-8") != render_markdown(expected):
        fail("Markdown output is stale or was not generated from the JSON dataset")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--no-regeneration-check", action="store_true")
    args = parser.parse_args()
    reference = json.loads(OUTPUT_PATH.read_text(encoding="utf-8"))
    validate_contract(reference)
    if not args.no_regeneration_check:
        validate_generated_files()
    print(
        json.dumps(
            {
                "ok": True,
                "records": reference["summary"]["total_records"],
                "by_resolution_status": reference["summary"]["by_resolution_status"],
                "live_read_verified": reference["summary"]["live_read_verified"],
                "write_verified": reference["summary"]["write_verified"],
            },
            indent=2,
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
