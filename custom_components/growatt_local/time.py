"""Growatt TL-XH TOU start and end time controls."""

from datetime import time as dt_time

from homeassistant.components.time import TimeEntity
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback

from .API.const import DeviceTypes
from .API.device_type.storage_120 import XH_SCHEDULE_REGISTER_KEYS
from .const import CONF_SERIAL_NUMBER, DOMAIN
from .tou import (
    TOU_SLOTS,
    GrowattTouEntity,
    pack_start,
    pack_time,
    slot_values,
    unpack_slot,
)


async def async_setup_entry(
    hass: HomeAssistant,
    config_entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    """Set up the eighteen TOU time controls."""

    coordinator = hass.data[DOMAIN][config_entry.data[CONF_SERIAL_NUMBER]]
    if coordinator.growatt_api.device is not DeviceTypes.HYBRID_120_TL_XH:
        async_add_entities([])
        return
    coordinator.get_keys_by_name(set(XH_SCHEDULE_REGISTER_KEYS), True)
    async_add_entities(
        [
            entity_class(coordinator, config_entry, slot)
            for slot in TOU_SLOTS
            for entity_class in (GrowattTouStartTime, GrowattTouEndTime)
        ],
        True,
    )


class _GrowattTouTime(GrowattTouEntity, TimeEntity):
    """Base time entity for one period."""

    start = True

    @property
    def native_value(self) -> dt_time | None:
        try:
            decoded = unpack_slot(self.coordinator.data, self.slot)
        except (KeyError, ValueError):
            return None
        return decoded.start if self.start else decoded.end

    async def async_set_value(self, value: dt_time) -> None:
        start_word, end_word = slot_values(self.coordinator.data, self.slot)
        decoded = unpack_slot(self.coordinator.data, self.slot)
        if decoded.start is None:
            raise ValueError(f"TOU period {self.slot.number} has an invalid start")
        await self._write_words(
            pack_start(value, decoded.priority.state, decoded.enabled)
            if self.start
            else start_word,
            pack_time(value) if not self.start else end_word,
        )


class GrowattTouStartTime(_GrowattTouTime):
    """Start time of one TOU period."""

    def __init__(self, coordinator, entry: ConfigEntry, slot) -> None:
        super().__init__(coordinator, entry, slot, "start")


class GrowattTouEndTime(_GrowattTouTime):
    """End time of one TOU period."""

    start = False

    def __init__(self, coordinator, entry: ConfigEntry, slot) -> None:
        super().__init__(coordinator, entry, slot, "end")
