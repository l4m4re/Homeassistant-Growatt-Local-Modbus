from datetime import timedelta
import logging
import re
from typing import Optional

from homeassistant.components.sensor import SensorEntity
from homeassistant.config_entries import ConfigEntry
from homeassistant.const import (
    CONF_MODEL,
    CONF_NAME,
    CONF_TYPE,
    STATE_UNAVAILABLE,
    STATE_UNKNOWN,
)
from homeassistant.core import HomeAssistant, callback
from homeassistant.helpers.entity import DeviceInfo
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.restore_state import RestoreEntity
from homeassistant.helpers.update_coordinator import CoordinatorEntity

from .API.const import DeviceTypes
from .API.device_type.base import (
    ATTR_ACTIVE_POWER,
    ATTR_CHARGE_POWER,
    ATTR_CURRENT_PRIORITY,
    ATTR_DISCHARGE_POWER,
    ATTR_INPUT_POWER,
    ATTR_LOAD_PERCENTAGE,
    ATTR_OUTPUT_POWER,
    ATTR_PAC_TO_GRID_TOTAL,
    ATTR_PAC_TO_USER_TOTAL,
    ATTR_POWER_TO_GRID,
    ATTR_POWER_TO_USER,
    ATTR_POWER_USER_LOAD,
    ATTR_SOC_PERCENTAGE,
)
from .API.device_type.storage_120 import XH_SCHEDULE_REGISTER_KEYS
from .const import (
    CONF_AC_PHASES,
    CONF_DC_STRING,
    CONF_FIRMWARE,
    CONF_POWER_SCAN_ENABLED,
    CONF_SERIAL_NUMBER,
    DOMAIN,
    SENSOR_CONTRACT_VERSION,
)
from .ems_types import PriorityWord, decode_priority_word, decode_xh_schedule
from .sensor_types.inverter import INVERTER_SENSOR_TYPES
from .sensor_types.offgrid import OFFGRID_SENSOR_TYPES
from .sensor_types.sensor_entity_description import GrowattSensorEntityDescription
from .sensor_types.storage import STORAGE_SENSOR_TYPES

_LOGGER = logging.getLogger(__name__)

SCAN_INTERVAL = timedelta(minutes=1)


async def async_setup_entry(
    hass: HomeAssistant,
    config_entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    coordinator = hass.data[DOMAIN][config_entry.data[CONF_SERIAL_NUMBER]]
    entities = []
    sensor_descriptions: list[GrowattSensorEntityDescription] = []
    supported_key_names = coordinator.growatt_api.get_register_names()

    device_type = DeviceTypes(config_entry.data[CONF_TYPE])

    if device_type in (DeviceTypes.INVERTER, DeviceTypes.INVERTER_315, DeviceTypes.INVERTER_120,
                       DeviceTypes.HYBRID_120, DeviceTypes.HYBRID_120_TL_XH):
        for sensor in INVERTER_SENSOR_TYPES:
            if sensor.key not in supported_key_names:
                continue

            if re.match(r"input_\d+", sensor.key) and not re.match(
                f"input_[1-{config_entry.data[CONF_DC_STRING]}]", sensor.key
            ):
                continue
            elif re.match(r"output_\d+", sensor.key) and not re.match(
                f"output_[1-{config_entry.data[CONF_AC_PHASES]}]", sensor.key
            ):
                continue

            sensor_descriptions.append(sensor)
    elif device_type == DeviceTypes.OFFGRID_SPF:
        for sensor in OFFGRID_SENSOR_TYPES:
            if sensor.key not in supported_key_names:
                continue

            if re.match(r"input_\d+", sensor.key) and not re.match(
                f"input_[1-{config_entry.data[CONF_DC_STRING]}]", sensor.key
            ):
                continue

            sensor_descriptions.append(sensor)

    if device_type in (DeviceTypes.HYBRID_120, DeviceTypes.HYBRID_120_TL_XH, DeviceTypes.STORAGE_120):
        for sensor in STORAGE_SENSOR_TYPES:
            if sensor.key not in supported_key_names:
                continue

            sensor_descriptions.append(sensor)

    if device_type in (DeviceTypes.INVERTER, DeviceTypes.INVERTER_315, DeviceTypes.INVERTER_120):
        power_sensor = (ATTR_INPUT_POWER, ATTR_OUTPUT_POWER)
    elif device_type in (DeviceTypes.HYBRID_120, DeviceTypes.HYBRID_120_TL_XH):
        power_sensor = (ATTR_INPUT_POWER, ATTR_OUTPUT_POWER,
                        ATTR_SOC_PERCENTAGE, ATTR_DISCHARGE_POWER, ATTR_CHARGE_POWER,
                        ATTR_PAC_TO_USER_TOTAL, ATTR_PAC_TO_GRID_TOTAL, ATTR_POWER_TO_USER,
                        ATTR_POWER_USER_LOAD, ATTR_POWER_TO_GRID)
    elif device_type in (DeviceTypes.STORAGE_120, ):
        power_sensor = (ATTR_SOC_PERCENTAGE, ATTR_DISCHARGE_POWER, ATTR_CHARGE_POWER)
    elif device_type == DeviceTypes.OFFGRID_SPF:
        power_sensor = (ATTR_ACTIVE_POWER, ATTR_LOAD_PERCENTAGE, ATTR_DISCHARGE_POWER, ATTR_CHARGE_POWER)
    else:
        power_sensor = tuple()
        _LOGGER.debug(
            "Device type %s was found but is not supported right now",
            config_entry.data[CONF_TYPE],
        )

    coordinator.get_keys_by_name({sensor.key for sensor in sensor_descriptions}, True)

    if config_entry.options[CONF_POWER_SCAN_ENABLED]:
        power_keys = coordinator.get_keys_by_name(power_sensor)
        coordinator.p_keys.update(power_keys)

    entities.extend(
        [
            GrowattDeviceEntity(
                coordinator, description=description, entry=config_entry
            )
            for description in sensor_descriptions
        ]
    )

    if device_type == DeviceTypes.HYBRID_120_TL_XH:
        coordinator.get_keys_by_name(
            {ATTR_CURRENT_PRIORITY, *XH_SCHEDULE_REGISTER_KEYS}, True
        )
        entities.extend(
            (
                GrowattPriorityEntity(coordinator, entry=config_entry),
                GrowattScheduleEntity(coordinator, entry=config_entry),
            )
        )

    async_add_entities(entities, True)


class GrowattDeviceEntity(CoordinatorEntity, RestoreEntity, SensorEntity):
    """An entity using CoordinatorEntity."""

    def __init__(self, coordinator, description, entry):
        """Pass coordinator to CoordinatorEntity."""
        super().__init__(coordinator, description.key)
        self.entity_description = description
        self._config_entry = entry

        self._attr_device_info = DeviceInfo(
            identifiers={(DOMAIN, entry.data[CONF_SERIAL_NUMBER])},
            manufacturer="Growatt",
            model=entry.data[CONF_MODEL],
            sw_version=entry.data[CONF_FIRMWARE],
            name=entry.options[CONF_NAME],
        )

    @property
    def name(self):
        return f"{self._config_entry.options[CONF_NAME]} {self.entity_description.name}"

    @property
    def unique_id(self) -> Optional[str]:
        return f"{DOMAIN}_{self._config_entry.data[CONF_SERIAL_NUMBER]}_{self.entity_description.key}"

    async def async_added_to_hass(self) -> None:
        """Call when entity is about to be added to Home Assistant."""
        await super().async_added_to_hass()

        if self.entity_description.midnight_reset:
            self.async_on_remove(
                self.coordinator.async_add_midnight_listener(
                    self._handle_midnight_update, self.coordinator_context
                )
            )

        if (state := await self.async_get_last_state()) is None:
            return

        if self._numeric_state_expected and state.state in (STATE_UNAVAILABLE, STATE_UNKNOWN):
            return

        self._attr_native_value = state.state

    @callback
    def _handle_coordinator_update(self) -> None:
        """Handle updated data from the coordinator."""
        if (state := self.coordinator.data.get(self.entity_description.key)) is None:
            return
        self._attr_native_value = state
        self.async_write_ha_state()

    @callback
    def _handle_midnight_update(self) -> None:
        """Handle updated data from the coordinator."""
        if (state := self.coordinator.data.get(self.entity_description.key)) is None:
            return
        self._attr_native_value = state
        self.async_write_ha_state()


class _GrowattFeedbackEntity(CoordinatorEntity, SensorEntity):
    """Base for bounded, read-only EMS feedback entities."""

    def __init__(self, coordinator, entry, key: str, name: str) -> None:
        """Initialize a feedback entity."""

        super().__init__(coordinator, key)
        self._config_entry = entry
        self._key = key
        self._name = name
        self._attr_device_info = DeviceInfo(
            identifiers={(DOMAIN, entry.data[CONF_SERIAL_NUMBER])},
            manufacturer="Growatt",
            model=entry.data[CONF_MODEL],
            sw_version=entry.data[CONF_FIRMWARE],
            name=entry.options[CONF_NAME],
        )

    @property
    def name(self) -> str:
        """Return a stable entity name."""

        return f"{self._config_entry.options[CONF_NAME]} {self._name}"

    @property
    def unique_id(self) -> str:
        """Return a stable non-energy-continuity unique ID."""

        return f"{DOMAIN}_{self._config_entry.data[CONF_SERIAL_NUMBER]}_{self._key}"


class GrowattPriorityEntity(_GrowattFeedbackEntity):
    """Expose I3144 as a typed read-only priority state."""

    def __init__(self, coordinator, entry) -> None:
        """Initialize the current-priority sensor."""

        super().__init__(coordinator, entry, ATTR_CURRENT_PRIORITY, "Current priority")

    @callback
    def _handle_coordinator_update(self) -> None:
        value = self.coordinator.data.get(ATTR_CURRENT_PRIORITY)
        if value is None:
            self._attr_native_value = STATE_UNAVAILABLE
            self._attr_extra_state_attributes = {
                "sensor_contract_version": SENSOR_CONTRACT_VERSION,
            }
        else:
            if not isinstance(value, PriorityWord):
                value = decode_priority_word(int(value))
            self._attr_native_value = value.state
            self._attr_extra_state_attributes = {
                **value.as_dict(),
                "observed_at": _observed_at(self.coordinator),
                "sensor_contract_version": SENSOR_CONTRACT_VERSION,
            }
        self.async_write_ha_state()


class GrowattScheduleEntity(_GrowattFeedbackEntity):
    """Expose the nine XH schedule slots as bounded structured attributes."""

    def __init__(self, coordinator, entry) -> None:
        """Initialize the schedule-state sensor."""

        super().__init__(coordinator, entry, "xh_schedule", "XH schedule")

    @callback
    def _handle_coordinator_update(self) -> None:
        registers = {}
        for key in XH_SCHEDULE_REGISTER_KEYS:
            value = self.coordinator.data.get(key)
            register = self.coordinator.get_holding_register_by_name(key)
            if value is None or register is None:
                self._attr_native_value = STATE_UNAVAILABLE
                self._attr_extra_state_attributes = {
                    "sensor_contract_version": SENSOR_CONTRACT_VERSION,
                }
                self.async_write_ha_state()
                return
            registers[register.register] = int(value)

        schedule = decode_xh_schedule(registers)
        self._attr_native_value = "valid" if all(slot.valid for slot in schedule) else "invalid"
        self._attr_extra_state_attributes = {
            "slots": [slot.as_dict() for slot in schedule],
            "decode_valid": all(slot.valid for slot in schedule),
            "observed_at": _observed_at(self.coordinator),
            "sensor_contract_version": SENSOR_CONTRACT_VERSION,
        }
        self.async_write_ha_state()


def _observed_at(coordinator) -> str | None:
    """Return the last successful read timestamp for diagnostics."""

    timestamp = getattr(coordinator, "data_timestamp", None)
    return timestamp.isoformat() if timestamp is not None else None
