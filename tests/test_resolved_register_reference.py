"""Regression tests for the public resolved register reference."""

import json
from pathlib import Path

from doc.validate_resolved_register_reference import (
    validate_contract,
    validate_generated_files,
)

REPO = Path(__file__).parents[1]


def test_resolved_reference_is_valid_and_reproducible() -> None:
    """The checked-in public reference matches its deterministic generator."""
    reference = json.loads((REPO / "doc/growatt_register_reference.json").read_text())

    validate_contract(reference)
    validate_generated_files()


def test_min_table_identity_and_signed_bms_current() -> None:
    """MIN table identity and HA-5 signed BMS current remain explicit."""
    reference = json.loads((REPO / "doc/growatt_register_reference.json").read_text())
    records = {record["id"]: record for record in reference["records"]}

    holding_3081 = records["register:min_tl_xh:holding:3081"]
    input_3081 = records["register:min_tl_xh:input:3081"]
    bms_current = records["register:min_tl_xh:input:3217"]

    assert holding_3081["canonical_name"] == "UPS/EPS frequency selection"
    assert input_3081["canonical_name"] == "PV4 energy total"
    assert bms_current["signed"] is True
    assert bms_current["divisor"] == 100
    assert bms_current["unit"] == "A"
    assert "read_verified" in bms_current["evidence_levels"]
    assert reference["summary"]["write_verified"] == 0


def test_semantic_aliases_and_min_preferred_registers() -> None:
    """Equivalent MIN physical registers retain one semantic identity."""
    reference = json.loads((REPO / "doc/growatt_register_reference.json").read_text())
    records = {record["id"]: record for record in reference["records"]}

    legacy = records["register:min_tl_xh:input:1014"]
    preferred = records["register:min_tl_xh:input:3171"]

    assert legacy["semantic_key"] == preferred["semantic_key"] == "battery_soc"
    assert legacy["semantic_role"] == "legacy"
    assert preferred["semantic_role"] == "preferred"
    assert "register:min_tl_xh:input:3171" in legacy["alternate_registers"]
    assert "register:min_tl_xh:input:1014" in preferred["alternate_registers"]


def test_min_transport_and_native_read_plans() -> None:
    """MIN plans use validated vendor pages and the V1.24 timing model."""
    reference = json.loads((REPO / "doc/growatt_register_reference.json").read_text())
    plans = reference["read_plans"]
    transport = plans["vendor_transport"]

    assert transport["minimum_cmd_period_ms"] == 850
    assert transport["recommended_cmd_period_ms"] == 1000
    assert transport["maximum_read_words"] == 125

    dynamic = next(
        item for item in plans["profiles"] if item["id"] == "min_dynamic_tariff"
    )
    assert dynamic["transaction_count"] == 3
    assert [
        (block["function_code"], block["start"], block["count"])
        for block in dynamic["blocks"]
    ] == [
        (3, 3000, 125),
        (4, 3000, 125),
        (4, 3125, 125),
    ]
    assert all(block["hardware_block_read_validated"] for block in dynamic["blocks"])

    bms = next(
        item for item in plans["profiles"] if item["id"] == "min_bms_diagnostics"
    )
    assert bms["transaction_count"] == 1
    assert bms["blocks"][0]["start"] == 3125
    assert bms["blocks"][0]["count"] == 125


def test_runtime_audit_preserves_findings_without_hiding_fixed_defects() -> None:
    """Known source/runtime disagreements remain visible to later consumers."""
    reference = json.loads((REPO / "doc/growatt_register_reference.json").read_text())
    audit = reference["runtime_audit"]

    assert audit["status"] == "issues_found"
    assert audit["finding_count"] == len(audit["findings"])
    assert any(
        finding["family"] == "min_tl_xh"
        and finding["table"] == "input"
        and finding["address"] == 3170
        and any(issue["kind"] == "signedness_mismatch" for issue in finding["issues"])
        for finding in audit["findings"]
    )
