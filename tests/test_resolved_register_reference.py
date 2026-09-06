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
