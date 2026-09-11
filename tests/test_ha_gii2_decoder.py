"""Regression tests for the bounded HA-GII-2 decoder correction."""

import ctypes
from types import SimpleNamespace

from custom_components.growatt_local.API.const import DeviceTypes
from custom_components.growatt_local.API.device_type.base import (
    ATTR_BATTERY_CURRENT,
    ATTR_OUTPUT_ENERGY_TODAY,
    ATTR_OUTPUT_REACTIVE_POWER,
    ATTR_PRESENT_FFT_A,
    ATTR_WARNING_CODE,
    GrowattDeviceRegisters,
)
from custom_components.growatt_local.API.growatt import get_register_information
from custom_components.growatt_local.API.utils import process_registers
from custom_components.growatt_local.const import CONF_FIRMWARE, CONF_SERIAL_NUMBER
from custom_components.growatt_local.sensor import GrowattDeviceEntity
from custom_components.growatt_local.sensor_types.inverter import INVERTER_SENSOR_TYPES

from homeassistant.const import CONF_MODEL


def test_one_word_signed_and_unsigned_decoding() -> None:
    """One-word float mappings retain their explicit signedness."""
    unsigned = GrowattDeviceRegisters(
        name="unsigned", register=1, value_type=float, scale=10
    )
    signed = GrowattDeviceRegisters(
        name="signed", register=2, value_type=float, scale=10, signed=True
    )

    assert process_registers({1: unsigned, 2: signed}, {1: 0xFF9C, 2: 0xFF9C}) == {
        "unsigned": 6543.6,
        "signed": -10.0,
    }


def test_two_word_signedness_and_scale_are_mapping_driven() -> None:
    """Two-word decoding uses unsigned or signed 32-bit interpretation as declared."""
    unsigned = GrowattDeviceRegisters(
        name="unsigned", register=1, value_type=float, length=2, scale=100
    )
    signed = GrowattDeviceRegisters(
        name="signed", register=3, value_type=float, length=2, scale=100, signed=True
    )

    assert process_registers(
        {1: unsigned, 3: signed},
        {1: 0x0000, 2: 0x2710, 3: 0xFFFF, 4: 0xD8F0},
    ) == {"unsigned": 100.0, "signed": -100.0}


def test_positive_energy_counter_values_are_unchanged() -> None:
    """The unsigned correction preserves ordinary positive counter values."""
    register = GrowattDeviceRegisters(
        name=ATTR_OUTPUT_ENERGY_TODAY,
        register=3049,
        value_type=float,
        length=2,
        scale=10,
    )
    raw_value = (0x0001 << 16) | 0x86A0
    legacy_value = round(float(ctypes.c_int32(raw_value).value) / register.scale, 3)

    decoded = process_registers({3049: register}, {3049: 0x0001, 3050: 0x86A0})

    assert legacy_value == 10000.0
    assert decoded == {
        ATTR_OUTPUT_ENERGY_TODAY: 10000.0
    }
    assert decoded[ATTR_OUTPUT_ENERGY_TODAY] == legacy_value


def test_high_bit_unsigned_value_is_not_negative() -> None:
    """Unsigned high-bit values no longer become negative signed int32 values."""
    register = GrowattDeviceRegisters(
        name="unsigned", register=1, value_type=float, length=2, scale=10
    )

    assert process_registers({1: register}, {1: 0x8000, 2: 0}) == {
        "unsigned": 214748364.8
    }


def test_min_warning_words_are_separate_and_contract_keys_are_stable() -> None:
    """I3110 is one word, I3111 remains separate, and warning identity is stable."""
    registers = get_register_information(DeviceTypes.HYBRID_120_TL_XH)

    assert registers.input[3110].name == ATTR_WARNING_CODE
    assert registers.input[3110].length == 1
    assert registers.input[3111].name == ATTR_PRESENT_FFT_A
    assert registers.input[3111].length == 1
    assert registers.input[3170].name == ATTR_BATTERY_CURRENT
    assert registers.input[3170].signed is False
    assert registers.input[3021].name == ATTR_OUTPUT_REACTIVE_POWER
    assert registers.input[3021].signed is True

    warning_description = next(
        description for description in INVERTER_SENSOR_TYPES
        if description.key == ATTR_WARNING_CODE
    )
    entry = SimpleNamespace(
        data={
            CONF_SERIAL_NUMBER: "fixture-serial",
            CONF_MODEL: "MIN 6000TL-XH",
            CONF_FIRMWARE: "fixture",
        },
        options={"name": "Growatt"},
    )
    entity = GrowattDeviceEntity(SimpleNamespace(data={}), warning_description, entry)

    assert warning_description.key == "warning_code"
    assert entity.unique_id == "growatt_local_fixture-serial_warning_code"
