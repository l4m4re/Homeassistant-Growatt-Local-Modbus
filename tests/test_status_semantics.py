"""Tests for vendor-defined MIN/TL-XH status word decoding."""

from custom_components.growatt_local.API.device_type.base import (
    ATTR_BATT_REQUEST_FLAGS,
    ATTR_BDC_FLAG_WORD,
    ATTR_BDC_SYSTEM_MODE_STATUS,
    ATTR_BMS_STATUS,
    ATTR_STATUS,
    ATTR_STATUS_CODE,
    ATTR_STANDBY_FLAGS,
    diagnostic_attributes,
    inverter_status,
)


def test_modern_inverter_status_keeps_packed_mode_and_status_separate() -> None:
    """I3000 low-byte status remains compatible with the public status state."""
    values = {ATTR_STATUS_CODE: 0x0001}

    assert inverter_status(values) == "Normal"
    assert diagnostic_attributes(values, ATTR_STATUS) == {
        "status_code_raw": 1,
        "status_code_mode": 0,
        "status_code_mode_name": "waiting_module",
        "status_code_state": 1,
        "status_code_state_name": "Normal",
    }


def test_status_diagnostics_decode_vendor_bdc_and_bms_words() -> None:
    """Packed BDC, BMS and request words expose only documented fields."""
    values = {
        ATTR_BDC_SYSTEM_MODE_STATUS: 0x0201,
        ATTR_BDC_FLAG_WORD: 0xA503,
        ATTR_BMS_STATUS: 2,
        ATTR_BATT_REQUEST_FLAGS: 0x0207,
        ATTR_STANDBY_FLAGS: 0x0005,
    }

    attributes = diagnostic_attributes(values, ATTR_STATUS)

    assert attributes["bdc_system_mode_name"] == "discharge"
    assert attributes["bdc_system_status_name"] == "normal"
    assert attributes["bdc_charge_enabled"] is True
    assert attributes["bdc_discharge_enabled"] is True
    assert attributes["bdc_warning_subcode"] == 5
    assert attributes["bdc_fault_subcode"] == 10
    assert attributes["bms_status_name"] == "discharge"
    assert attributes["charging_prohibited"] is True
    assert attributes["strong_charge_enabled"] is True
    assert attributes["strong_charge_2_enabled"] is True
    assert attributes["discharge_prohibited"] is False
    assert attributes["power_reduction_enabled"] is True
    assert attributes["standby_turn_off_order"] is True
    assert attributes["standby_pv_low"] is False
    assert attributes["standby_ac_voltage_or_frequency_out_of_scope"] is True


def test_unknown_status_values_remain_observable() -> None:
    """Undocumented values are not silently converted to a known enum."""
    values = {ATTR_STATUS_CODE: 0x070E}

    assert inverter_status(values) == "Unknown - code: 14"
    assert (
        diagnostic_attributes(values, ATTR_STATUS_CODE)["status_code_state_name"]
        == "unknown_14"
    )
