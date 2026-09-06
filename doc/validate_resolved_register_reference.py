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
        "semantic_model",
        "capability_validation",
        "read_plans",
        "runtime_audit",
    }
    missing = required - set(reference)
    if missing:
        fail(f"missing top-level fields: {sorted(missing)}")
    metadata = reference["meta"]
    if metadata.get("canonical") is not False or metadata.get("generated_compatibility_view") is not True:
        fail("compatibility reference has ambiguous canonical identity")
    if metadata.get("canonical_reference") != "doc/register-spec/growatt-register-spec.json":
        fail("compatibility reference points to the wrong canonical artifact")
    records = record_map(reference)
    record_ids = {record["id"] for record in records.values()}
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
        if record.get("semantic_key") is None:
            if record.get("semantic_role") != "unknown":
                fail(f"unkeyed record has semantic role {record['id']}")
        elif record.get("semantic_role") == "unknown":
            fail(f"semantic record has unknown role {record['id']}")
        for relationship in record.get("relationships", []):
            if relationship.get("target") not in record_ids:
                fail(f"relationship target missing from {record['id']}")

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
    legacy_soc = min_records.get(("input", 1014))
    preferred_soc = min_records.get(("input", 3171))
    if (
        not legacy_soc
        or not preferred_soc
        or legacy_soc["semantic_key"] != "battery_soc"
        or preferred_soc["semantic_key"] != "battery_soc"
        or legacy_soc["semantic_role"] != "legacy"
        or preferred_soc["semantic_role"] != "preferred"
    ):
        fail("MIN battery SOC legacy/preferred semantic relationship is missing")
    if min_records.get(("input", 3036), {}).get("length_registers") != 2:
        fail("MIN input 3036 must remain a two-register value")

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

    capabilities = reference["capability_validation"]
    if capabilities.get("family") != "min_tl_xh":
        fail("MIN capability validation family is missing")
    for capability in capabilities.get("capabilities", []):
        if capability.get("write_verified"):
            fail(
                f"capability write evidence was incorrectly promoted: {capability['key']}"
            )
        for register_id in capability.get("supporting_registers", []):
            if register_id not in record_ids:
                fail(f"capability register is missing: {register_id}")

    runtime_audit = reference["runtime_audit"]
    findings = runtime_audit.get("findings", [])
    if runtime_audit.get("finding_count") != len(findings):
        fail("runtime consistency audit finding count is stale")
    expected_audit_status = "consistent" if not findings else "issues_found"
    if runtime_audit.get("status") != expected_audit_status:
        fail("runtime consistency audit status is stale")
    if not any(
        finding.get("family") == "min_tl_xh"
        and finding.get("table") == "input"
        and finding.get("address") == 3170
        and any(
            issue.get("kind") == "signedness_mismatch"
            for issue in finding.get("issues", [])
        )
        for finding in findings
    ):
        fail("MIN input 3170 runtime mismatch was not preserved as a derived audit finding")
    if any(
        finding.get("family") == "min_tl_xh"
        and finding.get("table") == "input"
        and finding.get("address") == 3036
        and any(
            issue.get("kind") == "length_mismatch"
            for issue in finding.get("issues", [])
        )
        for finding in findings
    ):
        fail("MIN input 3036 still has a runtime length mismatch")

    read_plans = reference["read_plans"]
    transport = read_plans.get("vendor_transport", {})
    if {
        transport.get("minimum_cmd_period_ms"),
        transport.get("recommended_cmd_period_ms"),
        transport.get("maximum_read_words"),
        transport.get("maximum_write_words"),
    } != {850, 1000, 125}:
        fail("V1.24 vendor transport constraints are missing or incorrect")
    for profile in [
        *read_plans.get("profiles", []),
        *read_plans.get("source_derived_profiles", []),
    ]:
        blocks = profile.get("blocks", [])
        if profile.get("transaction_count") != len(blocks):
            fail(f"read-plan transaction count mismatch for {profile.get('id')}")
        for block in blocks:
            if block.get("end") != block.get("start", 0) + block.get("count", 0) - 1:
                fail(f"read-plan block end mismatch for {profile.get('id')}")
            expected_function = 3 if block.get("table") == "holding" else 4
            if block.get("function_code") != expected_function:
                fail(f"read-plan function code mismatch for {profile.get('id')}")
            if block.get("count", 0) > profile.get("max_register_words", 0):
                fail(f"read-plan block exceeds family limit for {profile.get('id')}")
            if block.get("gap_words") != block.get("additional_words_fetched"):
                fail(f"read-plan gap accounting mismatch for {profile.get('id')}")
    dynamic = next(
        (
            profile
            for profile in read_plans.get("profiles", [])
            if profile.get("id") == "min_dynamic_tariff"
        ),
        None,
    )
    if dynamic is None or dynamic.get("transaction_count") != 3:
        fail("MIN dynamic-tariff read plan must contain three native transactions")
    if dynamic and any(
        not block.get("hardware_block_read_validated")
        or not block.get("safe_range_id")
        or block.get("count") != 125
        for block in dynamic.get("blocks", [])
    ):
        fail("MIN dynamic-tariff plan is not backed by validated native blocks")
    bms = next(
        (
            profile
            for profile in read_plans.get("profiles", [])
            if profile.get("id") == "min_bms_diagnostics"
        ),
        None,
    )
    if bms is None or bms.get("transaction_count") != 1:
        fail("MIN BMS diagnostic read plan must contain one transaction")
    if bms and (
        len(bms.get("blocks", [])) != 1
        or bms["blocks"][0].get("start") != 3125
        or bms["blocks"][0].get("count") != 125
        or not bms["blocks"][0].get("hardware_block_read_validated")
    ):
        fail("MIN BMS diagnostic plan is not the validated input 3125 native block")

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
