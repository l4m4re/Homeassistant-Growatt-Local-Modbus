"""Regression checks for the GII-backed MIN/TL-XH register map."""

from custom_components.growatt_local.API.const import DeviceTypes
from custom_components.growatt_local.API.device_type.base import (
    ATTR_INPUT_4_ENERGY_TODAY,
    ATTR_INPUT_4_ENERGY_TOTAL,
    ATTR_XH_UPS_EPS_FREQUENCY_SELECTION,
    ATTR_XH_UPS_EPS_FUNCTION_ENABLE,
    ATTR_XH_UPS_EPS_VOLTAGE_SELECTION,
)
from custom_components.growatt_local.API.growatt import get_register_information


def test_min_tlxh_map_excludes_reserved_words_and_keeps_gii_energy_rows() -> None:
    """The runtime map excludes GII-reserved words and includes reviewed PV4 energy."""

    registers = get_register_information(DeviceTypes.HYBRID_120_TL_XH)

    assert 3046 not in registers.holding
    assert not set(registers.holding) & set(range(3115, 3125))
    assert not set(registers.input) & set(range(3281, 3375))
    assert registers.input[3079].name == ATTR_INPUT_4_ENERGY_TODAY
    assert registers.input[3079].length == 2
    assert registers.input[3081].name == ATTR_INPUT_4_ENERGY_TOTAL
    assert registers.input[3081].length == 2
    assert registers.holding[3079].name == ATTR_XH_UPS_EPS_FUNCTION_ENABLE
    assert registers.holding[3080].name == ATTR_XH_UPS_EPS_VOLTAGE_SELECTION
    assert registers.holding[3081].name == ATTR_XH_UPS_EPS_FREQUENCY_SELECTION
