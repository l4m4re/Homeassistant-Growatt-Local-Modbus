#!/usr/bin/env python3
"""Generate a Home Assistant overlay for the Growatt register baseline.

This script inspects the `HA_local_registers.json` snapshot that already powers
`extract_HA_local_registers.py` and emits a lightweight overlay mapping canonical
register ids to the identifiers Home Assistant uses (entity ids, keys, friendly
names, enum metadata, etc.). The overlay format mirrors the incremental
enrichment plan documented in README:

```
{
  "meta": { ... provenance ... },
  "overlays": {
     "canonical:<table>:<register>[-<end>]": {
        "sources": {
            "ha": {
                "entity_id": "sensor.growatt_xxx",
                "key": "pv1_voltage",
                ...
            }
        },
        "notes": {
            "ha": "Original HA name or description"
        },
        "enum_candidates": {
            "ha": [ {"value": 0, "label": "Off"}, ... ]
        }
     },
     ...
  }
}
```

The script warns when a Home Assistant register cannot be mapped to a catalog
block so we can extend `register_catalog.json` before promotion.
"""

from __future__ import annotations

import argparse
import json
from collections import defaultdict
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional

DOC_DIR = Path(__file__).resolve().parent
HA_SNAPSHOT_PATH = DOC_DIR / "HA_local_registers.json"
CATALOG_PATH = DOC_DIR / "register_catalog.json"
DEFAULT_OUTPUT = DOC_DIR / "overlays" / "ha_overlay.json"


@dataclass
class HARegister:
    reg_type: str
    register: int
    length: int
    key: str
    name: Optional[str]
    writable: bool
    enum_map: Optional[Dict[str, Any]]
    device_class: Optional[str]
    state_class: Optional[str]
    unit: Optional[str]


def load_catalog_blocks() -> Dict[str, Dict[str, Any]]:
    catalog = json.loads(CATALOG_PATH.read_text(encoding="utf-8"))
    return catalog.get("blocks", {})


def find_block_id(
    reg_type: str, register: int, length: int, blocks: Dict[str, Dict[str, Any]]
) -> Optional[str]:
    for block_id, block in blocks.items():
        if block.get("reg_type") != reg_type:
            continue
        start = block.get("register")
        if start is None:
            continue
        end = start + block.get("length", 0) - 1
        if start <= register and register + length - 1 <= end:
            return block_id
    return None


def canonical_id(reg_type: str, register: int, length: int) -> str:
    if length <= 1:
        return f"canonical:{reg_type}:{register}"
    return f"canonical:{reg_type}:{register}-{register + length - 1}"


def build_sensor_metadata(snapshot: Dict[str, Any]) -> Dict[str, Dict[str, Any]]:
    metadata = snapshot.get("metadata", {})
    result: Dict[str, Dict[str, Any]] = {}

    translations = (
        metadata.get("sensor_translations", {})
        .get("entity", {})
        .get("sensor", {})
    )
    for key, value in translations.items():
        result.setdefault(key, {}).update(value)

    sensor_types = metadata.get("sensor_types", {})
    for entries in sensor_types.values():
        if not isinstance(entries, list):
            continue
        for item in entries:
            key = item.get("key")
            if not key:
                continue
            slot = result.setdefault(key, {})
            for field in ("name", "device_class", "state_class"):
                if item.get(field):
                    slot.setdefault(field, item.get(field))
            native_unit = item.get("native_unit_of_measurement") or item.get("unit_of_measurement")
            if native_unit:
                slot.setdefault("unit", native_unit)
    return result


def extract_ha_registers(snapshot: Dict[str, Any], sensor_meta: Dict[str, Dict[str, Any]]) -> Iterable[HARegister]:
    devices = snapshot.get("devices", {})
    for device_name, groups in devices.items():
        if not isinstance(groups, dict):
            continue
        for group_name, registers in groups.items():
            if not isinstance(registers, list):
                continue
            reg_type = group_name.split("_", 1)[0].lower()
            if reg_type not in {"holding", "input"}:
                continue
            for item in registers:
                try:
                    register = int(item["register"])
                except (KeyError, TypeError, ValueError):
                    continue
                length = int(item.get("length", 1) or 1)
                key = str(item.get("name") or item.get("key") or f"register_{register}")
                writable = bool(item.get("read_write", False))
                enum_map = item.get("enum") or item.get("enum_map") or item.get("options")
                meta = sensor_meta.get(key, {})
                yield HARegister(
                    reg_type=reg_type,
                    register=register,
                    length=length,
                    key=key,
                    name=meta.get("name") or item.get("meta_name") or item.get("friendly_name"),
                    writable=writable,
                    enum_map=enum_map if isinstance(enum_map, dict) else None,
                    device_class=meta.get("device_class") or item.get("device_class"),
                    state_class=meta.get("state_class") or item.get("state_class"),
                    unit=meta.get("unit"),
                )


def build_overlay(
    ha_registers: Iterable[HARegister], blocks: Dict[str, Dict[str, Any]]
) -> Dict[str, Any]:
    overlays: Dict[str, Dict[str, Any]] = defaultdict(
        lambda: {"notes": {}, "enum_candidates": {}}
    )
    warnings: List[str] = []

    for entry in ha_registers:
        block_id = find_block_id(entry.reg_type, entry.register, entry.length, blocks)
        if block_id is None:
            warnings.append(
                f"[WARN] unmatched register {entry.reg_type}:{entry.register}-{entry.register + entry.length - 1} (key={entry.key})"
            )
            continue

        cid = canonical_id(entry.reg_type, entry.register, entry.length)
        overlay_entry = overlays[cid]

        notes = overlay_entry["notes"]
        notes.setdefault("ha_key", entry.key)
        if entry.name:
            notes.setdefault("ha_name", entry.name)
        if entry.device_class:
            notes.setdefault("ha_device_class", entry.device_class)
        if entry.state_class:
            notes.setdefault("ha_state_class", entry.state_class)
        if entry.unit:
            notes.setdefault("ha_unit", entry.unit)

        if entry.writable:
            notes.setdefault("ha_writable", True)

        if entry.enum_map:
            enum_list = [
                {"value": int(value) if str(value).isdigit() else value, "label": label}
                for value, label in entry.enum_map.items()
            ]
            overlay_entry["enum_candidates"].setdefault("ha", enum_list)

    return overlays, warnings


def build_document(overlays: Dict[str, Any]) -> Dict[str, Any]:
    return {
        "meta": {
            "generated_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
            "generator": Path(__file__).name,
            "source_files": {
                "HA_local_registers.json": str(HA_SNAPSHOT_PATH.relative_to(DOC_DIR)),
                "register_catalog.json": str(CATALOG_PATH.relative_to(DOC_DIR)),
            },
        },
        "overlays": overlays,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--output", type=Path, default=DEFAULT_OUTPUT, help="Destination overlay path"
    )
    args = parser.parse_args()

    snapshot = json.loads(HA_SNAPSHOT_PATH.read_text(encoding="utf-8"))
    catalog_blocks = load_catalog_blocks()

    sensor_meta = build_sensor_metadata(snapshot)
    overlays, warnings = build_overlay(
        extract_ha_registers(snapshot, sensor_meta), catalog_blocks
    )
    if warnings:
        for line in warnings:
            print(line)

    document = build_document(overlays)
    output_path = args.output if args.output.is_absolute() else DOC_DIR / args.output
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(json.dumps(document, indent=2), encoding="utf-8")
    print(f"Wrote {output_path.relative_to(DOC_DIR)}")


if __name__ == "__main__":
    main()
