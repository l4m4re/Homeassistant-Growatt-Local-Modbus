"""Tests for the MIN/TL-XH vendor-native block planner."""

from custom_components.growatt_local.API.const import DeviceTypes
from custom_components.growatt_local.API.device_type.base import (
    ATTR_BATTERY_CURRENT,
    ATTR_BMS_BATTERY_CURRENT,
    ATTR_INPUT_POWER,
    ATTR_INVERTER_ENABLED,
    GrowattDeviceRegisters,
)
from custom_components.growatt_local.API.growatt import get_register_information
from custom_components.growatt_local.API.utils import (
    DeviceRegisters,
    RegisterKeys,
    min_tlxh_read_plan,
    process_registers,
    register_sequences,
)
import pytest


def tl_xh_registers() -> DeviceRegisters:
    """Return the runtime register set used by the MIN/TL-XH device."""

    return get_register_information(DeviceTypes.HYBRID_120_TL_XH)


def test_min_fast_plan_uses_two_complete_input_pages() -> None:
    """All current fast power and battery values fit in the two fast pages."""

    keys = RegisterKeys(input={3001, 3023, 3041, 3043, 3045, 3171, 3178, 3180})

    sequences = register_sequences(keys, tl_xh_registers())

    assert sequences.holding == set()
    assert sequences.input == {(3000, 125), (3125, 125)}


def test_min_full_plan_keeps_control_and_static_pages_separate() -> None:
    """The full entity set adds native control/static pages without changing fast pages."""

    keys = RegisterKeys(
        holding={0, 3049},
        input={3001, 3023, 3171, 3178, 3125, 3217},
    )

    sequences = register_sequences(keys, tl_xh_registers())

    assert sequences.holding == {(0, 125), (3000, 125)}
    assert sequences.input == {(3000, 125), (3125, 125)}


def test_min_all_current_registers_fit_in_required_native_pages() -> None:
    """Every currently mapped MIN register is covered without a cross-page read."""

    registers = tl_xh_registers()
    sequences = register_sequences(
        RegisterKeys(holding=set(registers.holding), input=set(registers.input)),
        registers,
    )

    assert sequences.holding == {(0, 125), (3000, 125)}
    assert sequences.input == {(3000, 125), (3125, 125)}


@pytest.mark.parametrize(
    ("register", "expected"),
    [
        (3123, {(3000, 125)}),
        (3124, {(3000, 125)}),
        (3248, {(3125, 125)}),
        (3249, {(3125, 125)}),
        (3250, {(3250, 125)}),
        (3251, {(3250, 125)}),
    ],
)
def test_min_page_boundaries_select_complete_native_pages(
    register: int, expected: set[tuple[int, int]]
) -> None:
    """Boundary addresses are resolved to a complete vendor page."""

    registers = tl_xh_registers()
    registers.input[register] = GrowattDeviceRegisters(
        name=f"test_{register}", register=register, value_type=int
    )

    assert register_sequences(
        RegisterKeys(input={register}), registers
    ).input == expected


def test_min_multiregister_boundary_does_not_cross_pages() -> None:
    """A two-word value at a page edge causes both complete pages to be read."""

    registers = tl_xh_registers()
    registers.input[3124] = GrowattDeviceRegisters(
        name="cross_page", register=3124, value_type=float, length=2
    )

    assert register_sequences(
        RegisterKeys(input={3124}), registers
    ).input == {(3000, 125), (3125, 125)}


def test_min_block_buffer_preserves_decoding_semantics() -> None:
    """Absolute addresses decoded from a page retain the HA-5 meanings."""

    registers = tl_xh_registers()
    values = {
        0: 1,
        3001: 0,
        3002: 2,
        3170: 330,
        3217: 0xFEB6,
    }

    decoded = process_registers(registers.input, values)
    decoded.update(process_registers(registers.holding, values))

    assert decoded[ATTR_INPUT_POWER] == 0.2
    assert decoded[ATTR_BATTERY_CURRENT] == 33.0
    assert decoded[ATTR_BMS_BATTERY_CURRENT] == -3.30
    assert process_registers(
        registers.holding, {0: 1}
    )[ATTR_INVERTER_ENABLED] == 1


def test_min_read_plan_is_inspectable() -> None:
    """The runtime plan is data, not only a comment or implicit test fixture."""

    assert min_tlxh_read_plan() == {
        "fast": (("input", 3000, 125), ("input", 3125, 125)),
        "control": (("holding", 3000, 125),),
        "static": (("holding", 0, 125),),
        "diagnostic": (("input", 3250, 125),),
    }


def test_legacy_family_keeps_45_word_limit() -> None:
    """The native 125-word plan is isolated from the legacy v3.15 family."""

    sequences = register_sequences(
        RegisterKeys(input={1, 46}),
        get_register_information(DeviceTypes.INVERTER_315),
    )

    assert sequences.input
    assert all(length <= 45 for _, length in sequences.input)
    assert all(length != 125 for _, length in sequences.input)
