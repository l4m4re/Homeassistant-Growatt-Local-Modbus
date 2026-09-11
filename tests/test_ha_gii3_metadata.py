"""Regression tests for the HA-GII-3 metadata reconciliation."""

from types import SimpleNamespace

from custom_components.growatt_local.API.const import DeviceTypes
from custom_components.growatt_local.API.device_type.base import (
    ATTR_BMS_CELL_VOLT_MAX,
    ATTR_BMS_CELL_VOLT_MIN,
    ATTR_OUTPUT_PERCENTAGE,
    ATTR_OUTPUT_REACTIVE_POWER,
)
from custom_components.growatt_local.API.device_type.storage_120 import (
    STORAGE_INPUT_REGISTERS_120_TL_XH,
)
from custom_components.growatt_local.API.growatt import get_register_information
from custom_components.growatt_local.API.utils import process_registers
from custom_components.growatt_local.const import CONF_FIRMWARE, CONF_SERIAL_NUMBER
from custom_components.growatt_local.sensor import GrowattDeviceEntity
from custom_components.growatt_local.sensor_types.inverter import INVERTER_SENSOR_TYPES
from custom_components.growatt_local.sensor_types.sensor_entity_description import (
    GrowattSensorEntityDescription,
)
from custom_components.growatt_local.sensor_types.storage import STORAGE_SENSOR_TYPES

from homeassistant.components.sensor import SensorDeviceClass
from homeassistant.const import (
    CONF_MODEL,
    PERCENTAGE,
    UnitOfElectricPotential,
    UnitOfReactivePower,
)


def _description(
    descriptions: tuple[GrowattSensorEntityDescription, ...], key: str
) -> GrowattSensorEntityDescription:
    return next(description for description in descriptions if description.key == key)


def _entry():
    return SimpleNamespace(
        data={
            CONF_SERIAL_NUMBER: "fixture-serial",
            CONF_MODEL: "MIN 6000TL-XH",
            CONF_FIRMWARE: "fixture",
        },
        options={"name": "Growatt"},
    )


def test_reactive_power_metadata_preserves_read_and_entity_contract() -> None:
    """I3021 stays signed, scaled, and keyed while its unit becomes var."""
    register = get_register_information(DeviceTypes.HYBRID_120_TL_XH).input[3021]
    description = _description(INVERTER_SENSOR_TYPES, ATTR_OUTPUT_REACTIVE_POWER)
    entity = GrowattDeviceEntity(SimpleNamespace(data={}), description, _entry())

    assert (register.register, register.length, register.scale, register.signed) == (
        3021,
        2,
        10,
        True,
    )
    assert description.key == ATTR_OUTPUT_REACTIVE_POWER
    assert description.native_unit_of_measurement == (
        UnitOfReactivePower.VOLT_AMPERE_REACTIVE
    )
    assert description.device_class == SensorDeviceClass.REACTIVE_POWER
    assert description.state_class.value == "measurement"
    assert entity.unique_id == "growatt_local_fixture-serial_output_reactive_power"
    assert process_registers(
        {3021: register}, {3021: 0xFFFF, 3022: 0xD8F0}
    ) == {ATTR_OUTPUT_REACTIVE_POWER: -1000.0}


def test_cell_voltage_precision_is_presentation_only() -> None:
    """I3230/I3231 remain unsigned millivolt-scaled voltage readings."""
    registers = {
        register.register: register
        for register in STORAGE_INPUT_REGISTERS_120_TL_XH
        if register.register in (3230, 3231)
    }
    decoded = process_registers(registers, {3230: 3314, 3231: 3311})

    assert decoded == {
        ATTR_BMS_CELL_VOLT_MAX: 3.314,
        ATTR_BMS_CELL_VOLT_MIN: 3.311,
    }
    for key, register_number in (
        (ATTR_BMS_CELL_VOLT_MAX, 3230),
        (ATTR_BMS_CELL_VOLT_MIN, 3231),
    ):
        register = registers[register_number]
        description = _description(STORAGE_SENSOR_TYPES, key)
        entity = GrowattDeviceEntity(SimpleNamespace(data={}), description, _entry())

        assert (register.register, register.length, register.scale, register.signed) == (
            register_number,
            1,
            1000,
            False,
        )
        assert description.native_unit_of_measurement == UnitOfElectricPotential.VOLT
        assert description.device_class == SensorDeviceClass.VOLTAGE
        assert description.suggested_display_precision == 3
        assert entity.unique_id == f"growatt_local_fixture-serial_{key}"


def test_output_percentage_is_not_power_factor() -> None:
    """I3101 remains a percentage without the unrelated power-factor class."""
    register = get_register_information(DeviceTypes.HYBRID_120_TL_XH).input[3101]
    description = _description(INVERTER_SENSOR_TYPES, ATTR_OUTPUT_PERCENTAGE)
    entity = GrowattDeviceEntity(SimpleNamespace(data={}), description, _entry())

    assert (register.register, register.length, register.scale, register.signed) == (
        3101,
        1,
        10,
        False,
    )
    assert description.key == ATTR_OUTPUT_PERCENTAGE
    assert description.native_unit_of_measurement == PERCENTAGE
    assert description.device_class is None
    assert entity.unique_id == "growatt_local_fixture-serial_real_output_power_percent"
    assert process_registers({3101: register}, {3101: 73}) == {
        ATTR_OUTPUT_PERCENTAGE: 73
    }
