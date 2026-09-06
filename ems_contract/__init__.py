"""Project-independent read-only contracts for the future Home Energy Manager."""

from .growatt import (
    PriorityMode,
    PriorityWord,
    XhScheduleSlot,
    decode_priority_word,
    decode_xh_schedule,
)
from .live_snapshot import load_snapshot, snapshot_from_inventory
from .providers import (
    EvAvailability,
    EvProvider,
    EvProviderState,
    FixtureEvProvider,
    FixturePriceProvider,
    PriceInterval,
    PriceProvider,
    PriceProviderState,
)
from .snapshot import EmsSnapshot, GrowattState

__all__ = [
    "EmsSnapshot",
    "EvAvailability",
    "EvProvider",
    "EvProviderState",
    "FixtureEvProvider",
    "FixturePriceProvider",
    "GrowattState",
    "PriceInterval",
    "PriceProvider",
    "PriceProviderState",
    "PriorityMode",
    "PriorityWord",
    "XhScheduleSlot",
    "decode_priority_word",
    "decode_xh_schedule",
    "load_snapshot",
    "snapshot_from_inventory",
]
