"""Configurable Growatt TL-XH time-of-use schedule controls."""

from collections.abc import Mapping
from dataclasses import dataclass
from datetime import time as dt_time
from typing import Any

from homeassistant.components.switch import SwitchEntity
from homeassistant.config_entries import ConfigEntry
from homeassistant.const import CONF_MODEL, CONF_NAME
from homeassistant.core import callback
from homeassistant.helpers.entity import DeviceInfo
from homeassistant.helpers.update_coordinator import CoordinatorEntity

from .API.device_type.base import (
    ATTR_XH_SCHEDULE_1_END,
    ATTR_XH_SCHEDULE_1_START,
    ATTR_XH_SCHEDULE_2_END,
    ATTR_XH_SCHEDULE_2_START,
    ATTR_XH_SCHEDULE_3_END,
    ATTR_XH_SCHEDULE_3_START,
    ATTR_XH_SCHEDULE_4_END,
    ATTR_XH_SCHEDULE_4_START,
    ATTR_XH_SCHEDULE_5_END,
    ATTR_XH_SCHEDULE_5_START,
    ATTR_XH_SCHEDULE_6_END,
    ATTR_XH_SCHEDULE_6_START,
    ATTR_XH_SCHEDULE_7_END,
    ATTR_XH_SCHEDULE_7_START,
    ATTR_XH_SCHEDULE_8_END,
    ATTR_XH_SCHEDULE_8_START,
    ATTR_XH_SCHEDULE_9_END,
    ATTR_XH_SCHEDULE_9_START,
)
from .const import CONF_SERIAL_NUMBER
from .ems_types import PriorityMode, PriorityWord, XhScheduleSlot

PRIORITY_OPTIONS = tuple(mode.state for mode in PriorityMode)


@dataclass(frozen=True)
class TouSlot:
    """Register and key mapping for one portal TOU period."""

    number: int
    start_register: int
    start_key: str
    end_key: str


TOU_SLOTS = (
    TouSlot(1, 3038, ATTR_XH_SCHEDULE_1_START, ATTR_XH_SCHEDULE_1_END),
    TouSlot(2, 3040, ATTR_XH_SCHEDULE_2_START, ATTR_XH_SCHEDULE_2_END),
    TouSlot(3, 3042, ATTR_XH_SCHEDULE_3_START, ATTR_XH_SCHEDULE_3_END),
    TouSlot(4, 3044, ATTR_XH_SCHEDULE_4_START, ATTR_XH_SCHEDULE_4_END),
    TouSlot(5, 3050, ATTR_XH_SCHEDULE_5_START, ATTR_XH_SCHEDULE_5_END),
    TouSlot(6, 3052, ATTR_XH_SCHEDULE_6_START, ATTR_XH_SCHEDULE_6_END),
    TouSlot(7, 3054, ATTR_XH_SCHEDULE_7_START, ATTR_XH_SCHEDULE_7_END),
    TouSlot(8, 3056, ATTR_XH_SCHEDULE_8_START, ATTR_XH_SCHEDULE_8_END),
    TouSlot(9, 3058, ATTR_XH_SCHEDULE_9_START, ATTR_XH_SCHEDULE_9_END),
)


def slot_values(data: Mapping[str, Any], slot: TouSlot) -> tuple[int, int]:
    """Return the current packed words for a slot."""

    start_word = data.get(slot.start_key)
    end_word = data.get(slot.end_key)
    if start_word is None or end_word is None:
        raise ValueError(f"TOU period {slot.number} has no current register data")
    return int(start_word), int(end_word)


def pack_time(value: dt_time) -> int:
    """Pack a portal hour/minute field."""

    return (value.hour << 8) | value.minute


def pack_start(value: dt_time, priority: str, enabled: bool) -> int:
    """Pack a portal start/control word."""

    priority_value = PriorityMode[priority.upper()].value
    return pack_time(value) | (priority_value << 13) | (int(enabled) << 15)


def unpack_slot(data: Mapping[str, Any], slot: TouSlot) -> XhScheduleSlot:
    """Decode one slot from coordinator register data."""

    start_word, end_word = slot_values(data, slot)
    start_hour = (start_word >> 8) & 0x1F
    start_minute = start_word & 0xFF
    end_hour = (end_word >> 8) & 0x1F
    end_minute = end_word & 0xFF
    start = (
        dt_time(start_hour, start_minute)
        if start_hour <= 23 and start_minute <= 59
        else None
    )
    end = (
        dt_time(end_hour, end_minute)
        if end_hour <= 23 and end_minute <= 59
        else None
    )
    priority_raw = (start_word >> 13) & 0x03
    return XhScheduleSlot(
        slot=slot.number,
        start=start,
        end=end,
        priority=PriorityWord(
            raw=priority_raw,
            mode=PriorityMode._value2member_map_.get(priority_raw),
        ),
        enabled=bool(start_word & 0x8000),
        raw_start_word=start_word,
        raw_end_word=end_word,
    )


class GrowattTouEntity(CoordinatorEntity):
    """Base entity for one configurable TOU period."""

    def __init__(self, coordinator, entry: ConfigEntry, slot: TouSlot, suffix: str):
        super().__init__(coordinator, slot.start_key)
        self.slot = slot
        self._config_entry = entry
        self._attr_device_info = DeviceInfo(
            identifiers={("growatt_local", entry.data[CONF_SERIAL_NUMBER])},
            manufacturer="Growatt",
            model=entry.data[CONF_MODEL],
            sw_version=entry.data.get("firmware"),
            name=entry.options[CONF_NAME],
        )
        self._attr_unique_id = (
            f"growatt_local_{entry.data[CONF_SERIAL_NUMBER]}_tou_"
            f"{slot.number}_{suffix}"
        )
        self._tou_name = f"TOU {slot.number} {suffix}"

    @property
    def name(self) -> str:
        """Return a stable portal-style entity name."""

        return f"{self._config_entry.options[CONF_NAME]} {self._tou_name}"

    @callback
    def _handle_coordinator_update(self) -> None:
        self.async_write_ha_state()

    async def _write_words(self, start_word: int, end_word: int) -> None:
        await self.coordinator.write_xh_schedule(
            self.slot.start_register,
            self.slot.start_key,
            self.slot.end_key,
            start_word,
            end_word,
        )


class GrowattTouEnabledSwitch(GrowattTouEntity, SwitchEntity):
    """Enable or disable one TOU period."""

    def __init__(self, coordinator, entry: ConfigEntry, slot: TouSlot) -> None:
        super().__init__(coordinator, entry, slot, "enabled")

    @property
    def is_on(self) -> bool | None:
        try:
            return unpack_slot(self.coordinator.data, self.slot).enabled
        except (KeyError, ValueError):
            return None

    async def async_turn_on(self, **kwargs: Any) -> None:
        start_word, end_word = slot_values(self.coordinator.data, self.slot)
        await self._write_words(start_word | 0x8000, end_word)

    async def async_turn_off(self, **kwargs: Any) -> None:
        start_word, end_word = slot_values(self.coordinator.data, self.slot)
        await self._write_words(start_word & 0x7FFF, end_word)
