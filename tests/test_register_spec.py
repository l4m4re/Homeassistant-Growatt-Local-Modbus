"""Tests for the project-independent Growatt Register Specification."""

import importlib.util
import json
from pathlib import Path

REPO = Path(__file__).parents[1]
SPEC_DIR = REPO / "doc" / "register-spec"
VALIDATOR_SPEC = importlib.util.spec_from_file_location(
    "growatt_register_spec_validator", SPEC_DIR / "validate_register_spec.py"
)
assert VALIDATOR_SPEC and VALIDATOR_SPEC.loader
VALIDATOR = importlib.util.module_from_spec(VALIDATOR_SPEC)
VALIDATOR_SPEC.loader.exec_module(VALIDATOR)


def load_spec() -> dict:
    """Load the generated canonical specification."""
    return json.loads((SPEC_DIR / "growatt-register-spec.json").read_text())


def test_canonical_spec_validates_and_preserves_table_identity() -> None:
    """Canonical physical identity remains family/table/address based."""
    spec = load_spec()
    VALIDATOR.validate(spec)
    records = {record["physical_id"]: record for record in spec["registers"]}

    assert (
        records["min_tl_xh:holding:3081"]["normalized"]["name"]
        == "UPS/EPS frequency selection"
    )
    assert records["min_tl_xh:input:3081"]["normalized"]["name"] == "PV4 energy total"
    assert (
        records["min_tl_xh:holding:3081"]["table"]
        != records["min_tl_xh:input:3081"]["table"]
    )


def test_bms_and_storage_current_are_distinct_measurement_points() -> None:
    """I3170 and I3217 retain different subsystem meanings."""
    records = {record["physical_id"]: record for record in load_spec()["registers"]}
    storage = records["min_tl_xh:input:3170"]
    bms = records["min_tl_xh:input:3217"]

    assert (
        storage["semantic_identity"]["quantity"]
        == bms["semantic_identity"]["quantity"]
        == "battery.current"
    )
    assert storage["semantic_identity"]["subsystem"] == "storage_device"
    assert bms["semantic_identity"]["subsystem"] == "bms"
    assert (
        storage["normalized"]["signedness_status"]
        == "implementation_correlated_not_live_sign_validated"
    )
    assert (
        bms["normalized"]["signedness_status"] == "regression_and_live_value_validated"
    )
    assert storage["relationships"] == []
    assert bms["relationships"] == []
    assert bms["normalized"]["divisor"] == 100


def test_native_pages_are_read_observed_not_semantically_promoted() -> None:
    """Native page evidence is separate from semantic verification."""
    spec = load_spec()
    pages = spec["native_read_evidence"]["pages"]

    assert [
        (page["function_code"], page["start"], page["count"]) for page in pages
    ] == [
        (3, 0, 125),
        (3, 3000, 125),
        (4, 3000, 125),
        (4, 3125, 125),
        (4, 3250, 125),
    ]
    assert all(page["hardware_validation"]["repetitions"] == 2 for page in pages)
    assert all(
        evidence["level"] != "semantic_verified"
        for record in spec["registers"]
        for evidence in record["evidence"]
    )


def test_canonical_coverage_exposes_structures_and_enums() -> None:
    """Coverage reports the remaining normalization work explicitly."""
    coverage = load_spec()["coverage"]

    assert coverage["normalized_percentage"] > 80
    assert coverage["logical_multi_register_fields"] > 0
    assert coverage["indexed_structures"] > 0
    assert coverage["enum_bearing_records"] > 0
    assert coverage["bitfield_bearing_records"] > 0


def test_runtime_audit_reports_occurrences_and_unique_findings() -> None:
    """The derived HA audit keeps repeated runtime mappings distinguishable."""
    audit = load_spec()["derived_views"]["ha_runtime_audit"]

    assert audit["mapping_occurrences_checked"] == 274
    assert audit["unique_physical_mappings_checked"] == 198
    assert audit["finding_occurrences"] == 34
    assert audit["unique_findings"] == 27
    assert set(audit["finding_kinds"]) == {"scale_mismatch", "signedness_mismatch"}
