"""Tests for configurable TL-XH TOU controls."""

from datetime import time
from types import SimpleNamespace
from unittest.mock import AsyncMock

from custom_components.growatt_local.select import GrowattTouPrioritySelect
from custom_components.growatt_local.time import GrowattTouEndTime, GrowattTouStartTime
from custom_components.growatt_local.tou import (
    TOU_SLOTS,
    GrowattTouEnabledSwitch,
    pack_start,
)
import pytest


def _entry() -> SimpleNamespace:
    return SimpleNamespace(
        data={
            "serial_number": "SNL0CGV020",
            "model": "MIN 6000TL-XH",
            "firmware": "fixture",
        },
        options={"name": "Growatt"},
    )


def _coordinator() -> SimpleNamespace:
    slot = TOU_SLOTS[1]
    return SimpleNamespace(
        data={
            slot.start_key: pack_start(time(19, 28), "battery_first", True),
            slot.end_key: (19 << 8) | 58,
        },
        write_xh_schedule=AsyncMock(),
    )


def test_tou_slots_match_portal_register_pairs() -> None:
    """The nine controls cover the portal's H3038-H3059 pairs."""

    assert [slot.start_register for slot in TOU_SLOTS] == [
        3038,
        3040,
        3042,
        3044,
        3050,
        3052,
        3054,
        3056,
        3058,
    ]
    assert pack_start(time(19, 28), "battery_first", True) == 0xB31C


@pytest.mark.asyncio
async def test_tou_priority_writes_complete_pair() -> None:
    """Changing priority preserves time and enable bits in one FC10 request."""

    coordinator = _coordinator()
    entity = GrowattTouPrioritySelect(coordinator, _entry(), TOU_SLOTS[1])

    await entity.async_select_option("grid_first")

    coordinator.write_xh_schedule.assert_awaited_once_with(
        3040,
        "xh_schedule_2_start",
        "xh_schedule_2_end",
        0xD31C,
        0x133A,
    )


@pytest.mark.asyncio
async def test_tou_time_and_enable_controls_preserve_other_fields() -> None:
    """Time and enable changes preserve the other packed-word fields."""

    coordinator = _coordinator()
    slot = TOU_SLOTS[1]
    start = GrowattTouStartTime(coordinator, _entry(), slot)
    end = GrowattTouEndTime(coordinator, _entry(), slot)
    enabled = GrowattTouEnabledSwitch(coordinator, _entry(), slot)

    await start.async_set_value(time(20, 5))
    assert coordinator.write_xh_schedule.await_args_list[0].args[-2:] == (
        0xB405,
        0x133A,
    )
    await end.async_set_value(time(21, 10))
    assert coordinator.write_xh_schedule.await_args_list[1].args[-2:] == (
        0xB31C,
        0x150A,
    )
    await enabled.async_turn_off()
    assert coordinator.write_xh_schedule.await_args_list[2].args[-2:] == (
        0x331C,
        0x133A,
    )
