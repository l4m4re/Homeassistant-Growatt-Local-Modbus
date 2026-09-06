#!/usr/bin/env python3
"""Validate the project-independent Growatt Register Specification."""

# ruff: noqa: C901, D103, T201

import json
from pathlib import Path
import re

import jsonschema

SPEC_DIR = Path(__file__).resolve().parent
DOC_DIR = SPEC_DIR.parent
SPEC_PATH = SPEC_DIR / "growatt-register-spec.json"
SCHEMA_PATH = SPEC_DIR / "growatt-register-spec.schema.json"
EXPECTED_HUMAN_FILES = {
    "README.md",
    "PROTOCOLS.md",
    "SEMANTIC_INDEX.md",
    "families/LEGACY_315.md",
    "families/MIN_TL_XH.md",
    "families/MIX.md",
    "families/MOD_TL3_XH.md",
    "families/SPA.md",
    "families/SPF.md",
    "families/SPH.md",
    "families/TL3_MAX_MID_MAC.md",
}


def fail(message: str) -> None:
    raise SystemExit(f"validation failed: {message}")


def validate(spec: dict) -> None:
    schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
    jsonschema.Draft202012Validator(schema).validate(spec)
    records = spec["registers"]
    if spec["specification"].get("canonical_truth") is not True:
        fail("canonical specification does not advertise canonical truth")
    if spec["specification"].get("artifact_role") != "canonical_machine_and_human_product":
        fail("canonical artifact role is ambiguous")
    if any(
        key in spec["specification"]
        for key in ("primary_public_reference", "generated_compatibility_view")
    ):
        fail("canonical artifact contains compatibility identity flags")
    compatibility_path = DOC_DIR / "growatt_register_reference.json"
    if compatibility_path.is_file():
        compatibility = json.loads(compatibility_path.read_text(encoding="utf-8"))
        metadata = compatibility.get("meta", {})
        if (
            metadata.get("canonical") is not False
            or metadata.get("generated_compatibility_view") is not True
            or metadata.get("canonical_reference") != "doc/register-spec/growatt-register-spec.json"
        ):
            fail("compatibility artifact advertises a second canonical truth")
    ids = {record["physical_id"] for record in records}
    record_by_id = {record["physical_id"]: record for record in records}
    fields_by_id = {field["id"]: field for field in spec["logical_fields"]}
    relationship_ids = ids | set(fields_by_id)
    physical_words = {
        (record["family"], record["table"], record["address"]): record["physical_id"]
        for record in records
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
        if record["semantic_identity"]["quantity"] is None and record["normalization"]["status"] != "unresolved":
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
        if record.get("component_of") and record["relationships"]:
            fail(f"logical component has semantic relationships: {record['physical_id']}")
        for relationship in record["relationships"]:
            if relationship["target"] not in relationship_ids:
                fail(f"missing relationship target from {record['physical_id']}")
            target = record_by_id.get(relationship["target"]) or fields_by_id[relationship["target"]]
            target_family = target["family"] if "family" in target else target["physical_registers"][0]["family"]
            target_subsystem = target["semantic_identity"]["subsystem"] if "semantic_identity" in target else target["subsystem"]
            if (
                target_family != record["family"]
                or target_subsystem != semantic["subsystem"]
            ):
                fail(
                    f"relationship crosses family/subsystem boundary: {record['physical_id']}"
                )
            if target.get("component_of") == record.get("component_of") and record.get("component_of"):
                fail(f"logical components are related as alternates: {record['physical_id']}")
    if len(fields_by_id) != len(spec["logical_fields"]):
        fail("logical field identity is not unique")
    for record in records:
        component_of = record.get("component_of")
        if component_of and component_of not in fields_by_id:
            fail(f"missing logical field for component {record['physical_id']}")
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
            if physical_words[physical_word] not in {
                record["physical_id"]
                for record in records
                if record.get("component_of") == field["id"]
            }:
                fail(f"logical field component is not linked back: {field['id']}")
        if field["word_order_status"] == "source_explicit" and field["word_order"] == "unknown":
            fail(f"source-explicit logical field has unknown ordering: {field['id']}")
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
    if audit["unique_family_table_address_mappings"] != audit["unique_physical_mappings_checked"]:
        fail("legacy runtime uniqueness alias is stale")
    if audit["unique_family_table_address_issue_findings"] != audit["unique_findings"]:
        fail("family-aware runtime finding uniqueness is stale")
    if not all((SPEC_DIR / name).is_file() for name in EXPECTED_HUMAN_FILES):
        fail("generated human documentation is not persistent")
    if spec["coverage"]["reversible_candidate_records"]:
        fail("source-poor writable registers still default to reversible_candidate")
    for record in records:
        for relationship in record["relationships"]:
            target = record_by_id.get(relationship["target"]) or fields_by_id[relationship["target"]]
            if record.get("component_of") == target.get("component_of") and record.get("component_of"):
                fail("component-as-alternate relationship remains")
    print(
        json.dumps(
            {
                "ok": True,
                "records": len(records),
                "unique_semantics": spec["coverage"]["semantic_concepts"],
                "runtime_unique_findings": audit["unique_findings"],
                "human_docs": len(EXPECTED_HUMAN_FILES),
            },
            indent=2,
        )
    )


def main() -> None:
    validate(json.loads(SPEC_PATH.read_text(encoding="utf-8")))


if __name__ == "__main__":
    main()
