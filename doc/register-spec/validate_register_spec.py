#!/usr/bin/env python3
"""Validate the project-independent Growatt Register Specification."""

# ruff: noqa: C901, D103, T201

import json
from pathlib import Path
import re

import jsonschema

SPEC_DIR = Path(__file__).resolve().parent
SPEC_PATH = SPEC_DIR / "growatt-register-spec.json"
SCHEMA_PATH = SPEC_DIR / "growatt-register-spec.schema.json"


def fail(message: str) -> None:
    raise SystemExit(f"validation failed: {message}")


def validate(spec: dict) -> None:
    schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
    jsonschema.Draft202012Validator(schema).validate(spec)
    records = spec["registers"]
    ids = {record["physical_id"] for record in records}
    physical_words = {
        (record["family"], record["table"], address)
        for record in records
        for address in range(
            record["address"], record["address"] + record["length_words"]
        )
    }
    if len(ids) != len(records):
        fail("physical register identity is not unique")
    families = {family["id"] for family in spec["families"]}
    source_ids = set(spec["source_catalog"])
    valid_subsystems = {
        "bms",
        "storage_device",
        "pv",
        "grid",
        "load",
        "ac",
        "control",
        "inverter",
        "unknown",
    }
    for record in records:
        if record["family"] not in families:
            fail(f"unknown family in {record['physical_id']}")
        if record["table"] not in {"holding", "input"}:
            fail(f"invalid table in {record['physical_id']}")
        if not re.fullmatch(r"[^:]+:(holding|input):\d+", record["physical_id"]):
            fail(f"invalid physical id {record['physical_id']}")
        semantic = record["semantic_identity"]
        if semantic["subsystem"] not in valid_subsystems:
            fail(f"invalid subsystem in {record['physical_id']}")
        if semantic["instance_kind"] == "bms" and semantic["instance"] is not None:
            fail(f"unproven BMS instance index in {record['physical_id']}")
        if (
            record["semantic_identity"]["quantity"] is None
            and record["normalization"]["status"] != "unresolved"
        ):
            fail(f"unkeyed record is not marked unresolved: {record['physical_id']}")
        if any(source not in source_ids for source in record["source_provenance"]):
            fail(f"unknown provenance source in {record['physical_id']}")
        if any(item["level"] == "semantic_verified" for item in record["evidence"]):
            fail(
                f"semantic_verified was asserted without a controlled semantic evidence contract: {record['physical_id']}"
            )
        enum_values = [item["value"] for item in record["enums"]]
        if len(enum_values) != len(set(enum_values)):
            fail(f"duplicate normalized enum value in {record['physical_id']}")
        occupied: set[int] = set()
        for field in record["bitfields"]:
            bits = field["bits"]
            if len(bits) == 2:
                current = set(range(bits[0], bits[1] + 1))
            else:
                current = set(bits)
            if occupied & current:
                fail(f"overlapping bitfields in {record['physical_id']}")
            occupied |= current
        if (
            record["semantic_identity"]["instance_kind"] == "bms"
            and record["relationships"]
        ):
            fail(
                f"BMS instance fields must not be flattened into alternates: {record['physical_id']}"
            )
        for relationship in record["relationships"]:
            if relationship["target"] not in ids:
                fail(f"missing relationship target from {record['physical_id']}")
            target = next(
                item
                for item in records
                if item["physical_id"] == relationship["target"]
            )
            if (
                target["family"] != record["family"]
                or target["semantic_identity"]["subsystem"] != semantic["subsystem"]
            ):
                fail(
                    f"relationship crosses family/subsystem boundary: {record['physical_id']}"
                )
    for field in spec["logical_fields"]:
        components = field["physical_registers"]
        component_ids = {
            (item.get("family"), item.get("table"), item.get("address"))
            for item in components
        }
        if len(component_ids) != len(components):
            fail(f"logical field overlaps itself: {field['id']}")
        for component in components:
            physical_word = (
                component["family"],
                component["table"],
                component["address"],
            )
            if physical_word not in physical_words:
                fail(f"logical field component missing: {field['id']}")
    for protocol in spec["protocols"].values():
        maximum = protocol.get("maximum_read_words")
        for block in protocol.get("native_read_blocks", []):
            if (
                "start" in block
                and "count" in block
                and maximum is not None
                and block["count"] > maximum
            ):
                fail("native block exceeds protocol maximum")
    for page in spec["native_read_evidence"]["pages"]:
        if page["end"] != page["start"] + page["count"] - 1:
            fail(f"native page range is inconsistent: {page['id']}")
        validation = page["hardware_validation"]
        if validation["repetitions"] != 2 or validation["response_word_counts"] != [
            125,
            125,
        ]:
            fail(f"MIN native page evidence is not 2/2 complete: {page['id']}")
        if any(
            validation[key] for key in ("exceptions", "timeouts", "retries", "crc_bad")
        ):
            fail(f"MIN native page evidence contains errors: {page['id']}")
    audit = spec["derived_views"]["ha_runtime_audit"]
    if audit["finding_occurrences"] != len(audit["findings"]):
        fail("runtime finding occurrence count is stale")
    if audit["unique_findings"] > audit["finding_occurrences"]:
        fail("runtime unique finding count exceeds occurrences")
    print(
        json.dumps(
            {
                "ok": True,
                "records": len(records),
                "unique_semantics": spec["coverage"]["semantic_concepts"],
                "runtime_unique_findings": audit["unique_findings"],
            },
            indent=2,
        )
    )


def main() -> None:
    validate(json.loads(SPEC_PATH.read_text(encoding="utf-8")))


if __name__ == "__main__":
    main()
