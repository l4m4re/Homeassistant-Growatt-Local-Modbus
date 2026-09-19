"""Growatt TL-XH TOU priority controls."""

from homeassistant.components.select import SelectEntity
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback

from .API.const import DeviceTypes
from .API.device_type.storage_120 import XH_SCHEDULE_REGISTER_KEYS
from .const import CONF_SERIAL_NUMBER, DOMAIN
from .tou import (
    PRIORITY_OPTIONS,
    TOU_SLOTS,
    GrowattTouEntity,
    pack_start,
    slot_values,
    unpack_slot,
)


async def async_setup_entry(
    hass: HomeAssistant,
    config_entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    """Set up the nine TOU priority selectors."""

    coordinator = hass.data[DOMAIN][config_entry.data[CONF_SERIAL_NUMBER]]
    if coordinator.growatt_api.device is not DeviceTypes.HYBRID_120_TL_XH:
        async_add_entities([])
        return
    coordinator.get_keys_by_name(set(XH_SCHEDULE_REGISTER_KEYS), True)
    async_add_entities(
        [
            GrowattTouPrioritySelect(coordinator, config_entry, slot)
            for slot in TOU_SLOTS
        ],
        True,
    )


class GrowattTouPrioritySelect(GrowattTouEntity, SelectEntity):
    """Select Load First, Battery First, or Grid First for one period."""

    _attr_options = list(PRIORITY_OPTIONS)

    def __init__(self, coordinator, entry: ConfigEntry, slot) -> None:
        super().__init__(coordinator, entry, slot, "priority")

    @property
    def current_option(self) -> str | None:
        try:
            return unpack_slot(self.coordinator.data, self.slot).priority.state
        except (KeyError, ValueError):
            return None

    async def async_select_option(self, option: str) -> None:
        if option not in PRIORITY_OPTIONS:
            raise ValueError(f"Unsupported TOU priority: {option}")
        _, end_word = slot_values(self.coordinator.data, self.slot)
        decoded = unpack_slot(self.coordinator.data, self.slot)
        if decoded.start is None:
            raise ValueError(f"TOU period {self.slot.number} has an invalid start")
        await self._write_words(
            pack_start(decoded.start, option, decoded.enabled),
            end_word,
        )
