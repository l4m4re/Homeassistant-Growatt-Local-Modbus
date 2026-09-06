#!/usr/bin/env python3
# ruff: noqa: D103, T201
"""Build the public, resolved Growatt register reference.

The graph-derived consolidated export remains an audit/intermediate artefact.
This builder adds explicit family applicability, model-specific MIN evidence,
live-read evidence and honest resolution states without treating generated
derivatives as independent corroboration.
"""

import argparse
from collections import Counter, defaultdict
from datetime import UTC, datetime
import hashlib
import json
from pathlib import Path
import re
from typing import Any

DOC_DIR = Path(__file__).resolve().parent
CANONICAL_PATH = DOC_DIR / "consolidated_register_ref.json"
MIN_MAP_PATH = DOC_DIR / "min_6000tl_xh_register_map.json"
MIN_LIVE_PATH = DOC_DIR / "min_6000tl_xh_live_validation.json"
OPENINVERTER_PATH = DOC_DIR / "openinverter_gateway_registers.json"
OUTPUT_PATH = DOC_DIR / "growatt_register_reference.json"
MARKDOWN_PATH = DOC_DIR / "GROWATT_REGISTER_REFERENCE.md"

STATUS_VALUES = (
    "RESOLVED",
    "RESOLVED_WITH_NOTES",
    "CONFLICTED",
    "SOURCE_ONLY",
    "UNKNOWN_RESERVED",
)

SOURCE_DEFINITIONS: dict[str, dict[str, Any]] = {
    "vendor_v124": {
        "label": "Growatt protocol v1.24 tables",
        "kind": "primary_source_claim",
        "path": "Growatt-Inverter-Modbus-RTU-Protocol_II-V1_24-English-tables.json",
        "independent": True,
    },
    "curated_best_guess": {
        "label": "curated best-guess/spec interpretation",
        "kind": "curated_interpretation",
        "path": "growatt_registers_best_guess.json",
        "independent": False,
    },
    "ha_runtime": {
        "label": "Home Assistant runtime register snapshot",
        "kind": "runtime_implementation",
        "path": "HA_local_registers.json",
        "independent": True,
    },
    "openinverter_gateway": {
        "label": "OpenInverterGateway mapping",
        "kind": "external_implementation",
        "path": "openinverter_gateway_registers.json",
        "independent": True,
    },
    "inverter_to_mqtt": {
        "label": "inverter-to-MQTT mapping",
        "kind": "external_implementation",
        "path": "inverter_to_mqtt_registers.json",
        "independent": True,
    },
    "grott": {
        "label": "Grott decoded layout",
        "kind": "external_implementation",
        "path": "grott_register_layouts.json",
        "independent": True,
    },
    "manual": {
        "label": "curated/manual datatype annotation",
        "kind": "curated_interpretation",
        "path": "build_register_data_types.py",
        "independent": False,
    },
    "min_resolved_map": {
        "label": "MIN 6000TL-XH resolved model map",
        "kind": "model_specific_resolved_overlay",
        "path": "min_6000tl_xh_register_map.json",
        "independent": False,
    },
    "min_live_validation": {
        "label": "MIN 6000TL-XH live read validation",
        "kind": "live_hardware_evidence",
        "path": "min_6000tl_xh_live_validation.json",
        "independent": True,
    },
    "ha5_regression_tests": {
        "label": "HA-5 regression tests",
        "kind": "deterministic_validation",
        "path": "../tests/test_ha5_regressions.py",
        "independent": False,
    },
    "graph_export": {
        "label": "graph-derived consolidated export",
        "kind": "generated_derivative",
        "path": "consolidated_register_ref.json",
        "independent": False,
        "derived": True,
    },
}

FAMILY_DEFINITIONS: list[dict[str, Any]] = [
    {
        "id": "min_tl_xh",
        "name": "MIN / TL-XH",
        "aliases": ["min", "tlx", "tlxh", "hybrid_120_TL_XH"],
        "protocol_group": "120",
        "models": ["MIN 6000TL-XH"],
        "source_family_ids": ["device_family:vendor:tlx_family"],
        "openinverter_devices": ["GrowattTLXH"],
        "notes": "Best-supported model family; MIN 6000TL-XH is live read validated.",
    },
    {
        "id": "tl3_max_mid_mac",
        "name": "TL3-X / MAX / MID / MAC",
        "aliases": ["tl3", "max", "mid", "mac", "inverter_120"],
        "protocol_group": "120",
        "models": [],
        "source_family_ids": [
            "device_family:vendor:tl3_x_family",
            "device_family:vendor:max_family",
        ],
        "openinverter_devices": ["Growatt120", "Growatt124"],
        "notes": "The repository groups these 120-family inverter layouts; model-specific differences remain possible.",
    },
    {
        "id": "mod_tl3_xh",
        "name": "MOD TL3-XH",
        "aliases": ["mod", "mod_tl3_xh"],
        "protocol_group": "120",
        "models": [],
        "source_family_ids": ["device_family:vendor:mod_tl3_xh"],
        "openinverter_devices": [],
        "notes": "Vendor/catalogue family; no model-specific live validation is claimed here.",
    },
    {
        "id": "storage_mix",
        "name": "MIX storage",
        "aliases": ["mix", "storage"],
        "protocol_group": "120",
        "models": [],
        "source_family_ids": ["device_family:vendor:storage_mix"],
        "openinverter_devices": [],
        "notes": "Storage family applicability comes from the graph/catalogue ranges.",
    },
    {
        "id": "storage_spa",
        "name": "SPA storage",
        "aliases": ["spa"],
        "protocol_group": "120",
        "models": [],
        "source_family_ids": ["device_family:vendor:storage_spa"],
        "openinverter_devices": [],
        "notes": "Storage family applicability comes from the graph/catalogue ranges.",
    },
    {
        "id": "storage_sph",
        "name": "SPH storage",
        "aliases": ["sph"],
        "protocol_group": "120",
        "models": [],
        "source_family_ids": ["device_family:vendor:storage_sph"],
        "openinverter_devices": [],
        "notes": "Storage family applicability comes from the graph/catalogue ranges.",
    },
    {
        "id": "legacy_inverter_315",
        "name": "Older inverter / 3.15 family",
        "aliases": ["inverter_315", "legacy"],
        "protocol_group": "3.15",
        "models": [],
        "source_family_ids": [],
        "openinverter_devices": ["Growatt305"],
        "notes": "Source-only external layout coverage; no live hardware resolution is claimed.",
    },
    {
        "id": "spf_offgrid",
        "name": "SPF off-grid / hybrid",
        "aliases": ["spf", "offgrid_SPF"],
        "protocol_group": "SPF",
        "models": [],
        "source_family_ids": [],
        "openinverter_devices": ["GrowattSPF"],
        "notes": "Source-only external layout coverage; no live hardware resolution is claimed.",
    },
]

CANONICAL_FAMILY_ALIASES = {
    "tlx": "device_family:vendor:tlx_family",
    "tl3": "device_family:vendor:tl3_x_family",
    "storage": "device_family:vendor:storage_mix",
    "max": "device_family:vendor:max_family",
}

SOURCE_KEY_MAP = {
    "vendor": "vendor_v124",
    "spec": "curated_best_guess",
    "home_assistant": "ha_runtime",
    "openinverter_gateway": "openinverter_gateway",
    "grott": "grott",
    "manual": "manual",
    "inverter_to_mqtt": "inverter_to_mqtt",
}

UNIT_MAP = {
    "PERCENTAGE": "%",
    "POWER_W": "W",
    "POWER_KWH": "kWh",
    "VOLTAGE": "V",
    "CURRENT": "A",
    "CURRENT_M": "A",
    "FREQUENCY": "Hz",
    "TEMPERATURE": "°C",
    "SECONDS": "s",
    "RESISTANCE_K": "kΩ",
    "NONE": None,
}

MIN_BMS_INPUT_REGISTERS = set(range(3212, 3223))


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(65536), b""):
            digest.update(chunk)
    return digest.hexdigest()


def compact(value: Any) -> Any:
    if isinstance(value, dict):
        return {k: compact(v) for k, v in value.items() if v not in (None, "", [], {})}
    if isinstance(value, list):
        return [compact(v) for v in value if v not in (None, "", [], {})]
    return value


def parse_range(reference: str) -> tuple[str, int, int] | None:
    match = re.fullmatch(r"register_range:(holding|input):(\d+)-(\d+)", reference)
    if not match:
        return None
    return match.group(1), int(match.group(2)), int(match.group(3))


def graph_ranges(canonical: dict[str, Any]) -> dict[str, list[tuple[str, int, int]]]:
    result: dict[str, list[tuple[str, int, int]]] = {}
    for family in canonical.get("families", []):
        result[family["id"]] = [
            parsed for raw in family.get("ranges", []) if (parsed := parse_range(raw))
        ]
    return result


def in_ranges(
    ranges: dict[str, list[tuple[str, int, int]]],
    family_ids: list[str],
    table: str,
    address: int,
) -> bool:
    return any(
        range_table == table and start <= address <= end
        for family_id in family_ids
        for range_table, start, end in ranges.get(family_id, [])
    )


def normalise_unit(unit: Any) -> str | None:
    if not unit:
        return None
    return UNIT_MAP.get(str(unit), str(unit))


def parse_data_type(data_type: str | None) -> dict[str, Any]:
    result: dict[str, Any] = {}
    if not data_type:
        return result
    for key, value in re.findall(r"(?:^|\|)([a-z_]+):([^|]+)", data_type):
        if value in {"?", "conflict"}:
            continue
        if key in {"length_bytes", "divide", "scale", "multiplier"}:
            try:
                result[key] = float(value) if "." in value else int(value)
            except ValueError:
                continue
        elif key == "signed":
            result[key] = value == "true"
        elif key == "unit":
            result[key] = normalise_unit(value)
        else:
            result[key] = value
    return result


def parse_min_encoding(encoding: str) -> dict[str, Any]:
    result: dict[str, Any] = {"encoding": encoding}
    match = re.match(r"([us])(\d+)", encoding.lower())
    if match:
        result["signed"] = match.group(1) == "s"
        result["length_registers"] = int(match.group(2)) // 16
    if match := re.search(r"/\s*(\d+(?:\.\d+)?)", encoding):
        divisor = float(match.group(1))
        result["divisor"] = int(divisor) if divisor.is_integer() else divisor
        result["scale"] = 1 / divisor
    if "percentage" in encoding.lower():
        result["unit"] = "%"
    elif (
        "enum" in encoding.lower()
        or "flag" in encoding.lower()
        or "bitfield" in encoding.lower()
    ):
        result["value_encoding"] = "enum_or_bitfield"
    return result


def access_from_payload(payload: dict[str, Any]) -> str:
    values: set[str] = set()

    def visit(value: Any) -> None:
        if isinstance(value, dict):
            for key, nested in value.items():
                key_lower = key.lower()
                if key_lower in {"access", "write_or_not"} and nested:
                    token = str(nested).upper().replace(" ", "")
                    if "R/W" in token or "RW" in token:
                        values.update({"R", "W"})
                    elif token == "W" or token.startswith("W"):
                        values.add("W")
                    elif token == "R" or token.startswith("R"):
                        values.add("R")
                elif key_lower in {"read_write", "writable"} and nested is not None:
                    values.add("W" if nested else "R")
                else:
                    visit(nested)
        elif isinstance(value, list):
            for nested in value:
                visit(nested)

    visit(payload)
    if values == {"R", "W"}:
        return "R/W"
    if values == {"W"}:
        return "W"
    if values == {"R"}:
        return "R"
    return "UNKNOWN"


def aliases_from_sources(sources: dict[str, Any]) -> dict[str, list[str]]:
    aliases: dict[str, set[str]] = defaultdict(set)
    for source_name, payload in sources.items():
        rows = payload if isinstance(payload, list) else [payload]
        for row in rows:
            if not isinstance(row, dict):
                continue
            for key in ("variable", "name", "label", "mqtt_key", "field", "enum"):
                if row.get(key):
                    aliases[source_name].add(str(row[key]))
    return {key: sorted(values) for key, values in sorted(aliases.items()) if values}


def enum_definitions(payload: dict[str, Any]) -> list[dict[str, Any]]:
    text = " ".join(
        str(value)
        for key in ("description", "tooltip", "help", "encoding", "range")
        if (value := payload.get(key))
    )
    result = []
    for raw_value, label in re.findall(r"(\d+)\s*[=:]\s*([A-Za-z][\w -]*)", text):
        result.append({"value": int(raw_value), "label": label.strip()})
    return sorted(
        {json.dumps(item, sort_keys=True): item for item in result}.values(),
        key=lambda item: item["value"],
    )


def semantic_category(name: str, access: str, aliases: dict[str, list[str]]) -> str:
    lowered = name.lower()
    if access in {"W", "R/W"} or any(
        token in lowered
        for token in ("enable", "setpoint", "schedule", "rate", "stop soc")
    ):
        return "control"
    if any(
        token in lowered
        for token in ("fault", "warn", "status", "derating", "temperature")
    ):
        return "diagnostic"
    if any(token in lowered for token in ("battery", "bms", "soc", "soh", "cell")):
        return "battery"
    if any(
        token in lowered
        for token in ("energy", "power", "voltage", "current", "frequency")
    ):
        return "telemetry"
    if aliases:
        return "register_data"
    return "unknown"


def source_ids_for(raw_sources: dict[str, Any]) -> list[str]:
    ids = {SOURCE_KEY_MAP[key] for key in raw_sources if key in SOURCE_KEY_MAP}
    return sorted(ids)


def independent_source_count(source_ids: list[str]) -> int:
    return sum(
        1
        for source_id in source_ids
        if SOURCE_DEFINITIONS.get(source_id, {}).get("independent")
    )


def base_record(
    raw: dict[str, Any], family: dict[str, Any], table: str, address: int
) -> dict[str, Any]:
    raw_sources = raw.get("sources", {})
    parsed_type = parse_data_type(raw.get("data_type"))
    source_ids = source_ids_for(raw_sources)
    spec_rows = raw_sources.get("spec", [])
    spec_name = next(
        (
            row.get("name")
            for row in spec_rows
            if isinstance(row, dict) and row.get("name")
        ),
        None,
    )
    canonical_name = (
        spec_name
        or raw.get("description")
        or raw.get("tooltip")
        or f"Register {address}"
    )
    access = access_from_payload(raw)
    aliases = aliases_from_sources(raw_sources)
    record: dict[str, Any] = {
        "id": f"register:{family['id']}:{table}:{address}",
        "family": family["id"],
        "family_name": family["name"],
        "table": table,
        "address": address,
        "model_applicability": [],
        "canonical_name": canonical_name,
        "description": raw.get("help")
        or raw.get("tooltip")
        or raw.get("description")
        or "",
        "length_registers": raw.get("data_width_words")
        or int(parsed_type.get("length_bytes", 2) / 2),
        "encoding": parsed_type.get("text_category") or "register value",
        "signed": parsed_type.get("signed"),
        "divisor": parsed_type.get("divide") or parsed_type.get("scale"),
        "scale": None,
        "multiplier": parsed_type.get("multiplier"),
        "unit": normalise_unit(raw.get("unit") or parsed_type.get("unit")),
        "access": access,
        "enum_definitions": enum_definitions(raw),
        "bitfields": [],
        "semantic_category": semantic_category(canonical_name, access, aliases),
        "resolution_status": "SOURCE_ONLY",
        "confidence": "medium" if independent_source_count(source_ids) > 1 else "low",
        "provenance": source_ids or ["graph_export"],
        "evidence_levels": ["source_claim"] if source_ids else [],
        "conflicts": [],
        "alternatives": raw.get("alternate_data_types", []),
        "source_aliases": aliases,
        "validation_evidence": [],
        "source_family_ids": sorted(
            {
                CANONICAL_FAMILY_ALIASES.get(value, value)
                for value in raw.get("families", [])
            }
        ),
    }
    if independent_source_count(source_ids) >= 2:
        record["evidence_levels"].append("semantic_correlated")
    if "conflict" in str(raw.get("data_type", "")):
        record["conflicts"].append(
            {
                "kind": "datatype_catalogue",
                "detail": "Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.",
            }
        )
    return record


def apply_openinverter(record: dict[str, Any], entry: dict[str, Any]) -> None:
    aliases = record.setdefault("source_aliases", {}).setdefault(
        "openinverter_gateway", []
    )
    for value in (entry.get("label"), entry.get("mqtt_key"), entry.get("enum")):
        if value and value not in aliases:
            aliases.append(value)
    aliases.sort()
    if record.get("canonical_name", "").startswith("Register ") and entry.get("label"):
        record["canonical_name"] = entry["label"]
        record["description"] = entry.get("comment", "") or entry["label"]
    size = str(entry.get("size", ""))
    if size.startswith("SIZE_"):
        width = size.removeprefix("SIZE_").removesuffix("_S")
        if width.isdigit():
            record["length_registers"] = int(width) // 16
    if "multiplier" in entry:
        record["multiplier"] = entry["multiplier"]
    if entry.get("unit"):
        record["unit"] = normalise_unit(entry["unit"])
    if size.endswith("_S"):
        record["signed"] = True
    record["provenance"] = sorted(
        set(record.get("provenance", [])) | {"openinverter_gateway"}
    )
    if "source_claim" not in record["evidence_levels"]:
        record["evidence_levels"].append("source_claim")


def live_ranges(live: dict[str, Any]) -> dict[str, list[tuple[int, int, str]]]:
    result: dict[str, list[tuple[int, int, str]]] = defaultdict(list)
    pattern = re.compile(r"fc(03|04)_(\d+)_count(\d+)_")

    def visit(value: Any, locator: str) -> None:
        if isinstance(value, dict):
            for key, nested in value.items():
                visit(nested, f"{locator}.{key}")
        elif isinstance(value, list):
            for index, nested in enumerate(value):
                visit(nested, f"{locator}[{index}]")
        elif isinstance(value, (str, int, float)):
            match = pattern.search(locator)
            if match:
                table = "holding" if match.group(1) == "03" else "input"
                start = int(match.group(2))
                count = int(match.group(3))
                result[table].append((start, start + count - 1, locator))

    visit(live, "live")
    return result


def live_match(
    live_index: dict[str, list[tuple[int, int, str]]], table: str, address: int
) -> list[str]:
    return [
        locator
        for start, end, locator in live_index.get(table, [])
        if start <= address <= end
    ]


def min_overlay_rows(
    min_map: dict[str, Any],
) -> list[tuple[str, dict[str, Any], str | None]]:
    result = []
    for original_table in ("holding", "input"):
        for row in min_map.get(original_table, []):
            address = int(row["register"])
            table = original_table
            relocation_note = None
            if original_table == "holding" and address in MIN_BMS_INPUT_REGISTERS:
                table = "input"
                relocation_note = "The older model-map section labels this BMS row as holding; runtime mapping, Grott layout and FC04 live evidence identify it as input-table telemetry."
            result.append((table, row, relocation_note))
    return result


def apply_min_overlay(
    record: dict[str, Any],
    row: dict[str, Any],
    relocation_note: str | None,
    live_index: dict[str, list[tuple[int, int, str]]],
) -> None:
    parsed = parse_min_encoding(row.get("encoding", ""))
    record.update(
        {
            "model_applicability": sorted(
                set(record.get("model_applicability", []))
                | {row.get("applicability", "MIN 6000TL-XH")}
            ),
            "canonical_name": row["name"],
            "description": row["name"],
            "length_registers": int(row["length"]),
            "encoding": row["encoding"],
            "access": row.get("access", record.get("access", "UNKNOWN")),
            "unit": row.get("unit") or parsed.get("unit") or record.get("unit"),
            "signed": parsed.get("signed"),
            "divisor": parsed.get("divisor"),
            "scale": parsed.get("scale"),
            "value_encoding": parsed.get("value_encoding", "numeric"),
            "confidence": row.get("confidence", "medium"),
            "provenance": sorted(
                set(record.get("provenance", [])) | {"min_resolved_map"}
            ),
        }
    )
    if relocation_note:
        record["conflicts"].append(
            {"kind": "table_reconciliation", "detail": relocation_note}
        )
    for token in row.get("provenance", []):
        mapped = {
            "vendor": "vendor_v124",
            "best_guess": "curated_best_guess",
            "OpenInverter": "openinverter_gateway",
            "HA": "ha_runtime",
            "live": "min_live_validation",
        }.get(token)
        if mapped:
            record["provenance"].append(mapped)
    record["provenance"] = sorted(set(record["provenance"]))
    for conflict in row.get("conflicts", []):
        record["conflicts"].append({"kind": "model_map_note", "detail": conflict})
    locators = live_match(live_index, record["table"], record["address"])
    if locators:
        record["evidence_levels"].append("read_verified")
        record["validation_evidence"].append(
            {"source": "min_live_validation", "locations": sorted(set(locators))}
        )
    if record["table"] == "input" and record["address"] == 3217:
        record["provenance"].append("ha5_regression_tests")
        record["provenance"] = sorted(set(record["provenance"]))
        record["validation_evidence"].append(
            {
                "source": "ha5_regression_tests",
                "locations": ["test_signed_bms_current_processing"],
                "detail": "0xFEB6 decodes to -3.30 A at 0.01 A resolution.",
            }
        )


def classify(record: dict[str, Any], has_min_overlay: bool) -> None:
    name = f"{record.get('canonical_name', '')} {record.get('description', '')}".lower()
    if any(token in name for token in ("reserved", "unknown")) and not record.get(
        "validation_evidence"
    ):
        record["resolution_status"] = "UNKNOWN_RESERVED"
        record["confidence"] = "low"
        return
    if has_min_overlay:
        record["resolution_status"] = (
            "RESOLVED_WITH_NOTES" if record.get("conflicts") else "RESOLVED"
        )
        record["confidence"] = "high"
        return
    independent = independent_source_count(record.get("provenance", []))
    if not record.get("canonical_name") or record["canonical_name"].startswith(
        "Register "
    ):
        record["resolution_status"] = "UNKNOWN_RESERVED"
        record["confidence"] = "low"
    elif independent >= 2:
        record["resolution_status"] = (
            "RESOLVED_WITH_NOTES" if record.get("conflicts") else "RESOLVED"
        )
        record["confidence"] = "high" if not record.get("conflicts") else "medium"
    elif independent == 1:
        record["resolution_status"] = "SOURCE_ONLY"
        record["confidence"] = "medium"
    else:
        record["resolution_status"] = "SOURCE_ONLY"
        record["confidence"] = "low"
    if record.get("conflicts") and record["resolution_status"] == "SOURCE_ONLY":
        record["resolution_status"] = "CONFLICTED"


def build_reference() -> dict[str, Any]:
    canonical = load_json(CANONICAL_PATH)
    min_map = load_json(MIN_MAP_PATH)
    live = load_json(MIN_LIVE_PATH)
    openinverter = load_json(OPENINVERTER_PATH)
    ranges = graph_ranges(canonical)
    family_by_id = {family["id"]: family for family in FAMILY_DEFINITIONS}
    records: dict[tuple[str, str, int], dict[str, Any]] = {}

    for _raw_key, raw in sorted(canonical.get("canonical_registers", {}).items()):
        table = raw.get("table")
        address = int(raw.get("register"))
        if table not in {"holding", "input"}:
            continue
        raw_family_ids = {
            CANONICAL_FAMILY_ALIASES.get(value, value)
            for value in raw.get("families", [])
        }
        for family in FAMILY_DEFINITIONS:
            applicable = bool(raw_family_ids & set(family["source_family_ids"]))
            applicable = applicable or in_ranges(
                ranges, family["source_family_ids"], table, address
            )
            if not applicable:
                continue
            key = (family["id"], table, address)
            record = base_record(raw, family, table, address)
            records[key] = record

    for family in FAMILY_DEFINITIONS:
        for device in family["openinverter_devices"]:
            payload = openinverter.get("devices", {}).get(device, {})
            for table_key, table in (
                ("holding_registers", "holding"),
                ("input_registers", "input"),
            ):
                for entry in payload.get(table_key, []):
                    if "address" not in entry:
                        continue
                    address = int(entry["address"])
                    key = (family["id"], table, address)
                    if key not in records:
                        records[key] = base_record(
                            {
                                "register": address,
                                "table": table,
                                "description": entry.get("label")
                                or f"Register {address}",
                                "sources": {"openinverter_gateway": [entry]},
                            },
                            family,
                            table,
                            address,
                        )
                    apply_openinverter(records[key], entry)

    live_index = live_ranges(live)
    min_overlays: set[tuple[str, str, int]] = set()
    min_family = family_by_id["min_tl_xh"]
    for table, row, relocation_note in min_overlay_rows(min_map):
        address = int(row["register"])
        key = ("min_tl_xh", table, address)
        if key not in records:
            records[key] = base_record(
                {
                    "register": address,
                    "table": table,
                    "description": row["name"],
                    "sources": {},
                },
                min_family,
                table,
                address,
            )
        apply_min_overlay(records[key], row, relocation_note, live_index)
        min_overlays.add(key)

    for address in (3047, 3048):
        key = ("min_tl_xh", "input", address)
        if key in records:
            records[key]["canonical_name"] = "Inverter runtime"
            records[key]["model_applicability"] = sorted(
                set(records[key].get("model_applicability", [])) | {"MIN 6000TL-XH"}
            )

    for key, record in records.items():
        classify(record, key in min_overlays)
        record["evidence_levels"] = sorted(set(record.get("evidence_levels", [])))
        record["conflicts"] = [
            dict(item)
            for item in {
                json.dumps(item, sort_keys=True): item
                for item in record.get("conflicts", [])
            }.values()
        ]
        record["source_aliases"] = {
            source: sorted(set(values))
            for source, values in sorted(record.get("source_aliases", {}).items())
        }
        record["validation_evidence"] = sorted(
            record.get("validation_evidence", []),
            key=lambda item: (item.get("source", ""), str(item.get("locations", ""))),
        )

    ordered_records = sorted(
        records.values(),
        key=lambda item: (item["family"], item["table"], item["address"]),
    )
    family_output = []
    for family in FAMILY_DEFINITIONS:
        family_records = [
            record for record in ordered_records if record["family"] == family["id"]
        ]
        status_counts = Counter(
            record["resolution_status"] for record in family_records
        )
        family_output.append(
            {
                key: value
                for key, value in {
                    **family,
                    "coverage": {
                        "total": len(family_records),
                        "holding": sum(
                            record["table"] == "holding" for record in family_records
                        ),
                        "input": sum(
                            record["table"] == "input" for record in family_records
                        ),
                        "by_resolution_status": {
                            status: status_counts.get(status, 0)
                            for status in STATUS_VALUES
                        },
                        "live_read_verified": sum(
                            "read_verified" in record["evidence_levels"]
                            for record in family_records
                        ),
                        "write_verified": 0,
                    },
                }.items()
                if key not in {"source_family_ids", "openinverter_devices"}
            }
        )

    status_counts = Counter(record["resolution_status"] for record in ordered_records)
    meta_sources = {}
    source_paths = {
        "vendor_v124": DOC_DIR / SOURCE_DEFINITIONS["vendor_v124"]["path"],
        "curated_best_guess": DOC_DIR
        / SOURCE_DEFINITIONS["curated_best_guess"]["path"],
        "ha_runtime": DOC_DIR / SOURCE_DEFINITIONS["ha_runtime"]["path"],
        "openinverter_gateway": DOC_DIR
        / SOURCE_DEFINITIONS["openinverter_gateway"]["path"],
        "inverter_to_mqtt": DOC_DIR / SOURCE_DEFINITIONS["inverter_to_mqtt"]["path"],
        "grott": DOC_DIR / SOURCE_DEFINITIONS["grott"]["path"],
        "min_resolved_map": MIN_MAP_PATH,
        "min_live_validation": MIN_LIVE_PATH,
        "graph_export": CANONICAL_PATH,
    }
    for source_id, source in SOURCE_DEFINITIONS.items():
        path = source_paths.get(source_id)
        entry = dict(source)
        if path and path.exists():
            entry["sha256"] = sha256(path)
        meta_sources[source_id] = entry

    return {
        "meta": {
            "schema_version": "1.0.0",
            "reference_version": "2026.09-resolved",
            "generated_at": datetime.now(UTC).isoformat(),
            "generator": "build_resolved_register_reference.py",
            "primary_public_reference": True,
            "identity": "(family, table, address)",
            "source_files": meta_sources,
            "lineage_policy": "Generated graph and overlay derivatives do not count as independent corroboration.",
        },
        "families": family_output,
        "records": ordered_records,
        "unresolved_or_conflicted_records": [
            record["id"]
            for record in ordered_records
            if record["resolution_status"]
            in {"CONFLICTED", "SOURCE_ONLY", "UNKNOWN_RESERVED"}
        ],
        "summary": {
            "total_records": len(ordered_records),
            "holding_records": sum(
                record["table"] == "holding" for record in ordered_records
            ),
            "input_records": sum(
                record["table"] == "input" for record in ordered_records
            ),
            "by_resolution_status": {
                status: status_counts.get(status, 0) for status in STATUS_VALUES
            },
            "live_read_verified": sum(
                "read_verified" in record["evidence_levels"]
                for record in ordered_records
            ),
            "write_verified": 0,
            "write_evidence_policy": "No current corpus entry is marked write_verified; HA-5 hardware validation was read-only.",
            "families_with_records": sum(
                bool(family["coverage"]["total"]) for family in family_output
            ),
        },
        "resolution_model": {
            "RESOLVED": "Evidence is sufficiently consistent for one primary interpretation.",
            "RESOLVED_WITH_NOTES": "Primary interpretation is strong, but alternatives or relevant notes remain.",
            "CONFLICTED": "Material disagreement remains without a defensible family-specific resolution.",
            "SOURCE_ONLY": "A semantic claim exists but lacks sufficient independent corroboration.",
            "UNKNOWN_RESERVED": "No useful semantic interpretation is available, or the register is reserved/unknown.",
        },
        "evidence_legend": {
            "source_claim": "A retained source explicitly describes the register.",
            "semantic_correlated": "At least two independent source classes support the semantic interpretation.",
            "read_verified": "A live hardware read matched the published interpretation; this is not a write claim.",
            "write_accepted": "The device accepted a write in a controlled test (none in this release).",
            "write_reversible": "A write was tested and safely reversed (none in this release).",
            "behavior_verified": "Observed device behavior confirmed the interpretation (none in this release).",
        },
    }


def markdown_escape(value: Any) -> str:
    return str(value).replace("|", "\\|").replace("\n", " ")


def render_markdown(reference: dict[str, Any]) -> str:
    lines = [
        "# Growatt resolved register reference",
        "",
        "> This file is generated from `doc/growatt_register_reference.json`. The JSON file is the primary machine-readable public reference; the original vendor, runtime, external and live-evidence files remain the provenance corpus.",
        "",
        f"Reference version: `{reference['meta']['reference_version']}`  ",
        f"Records: **{reference['summary']['total_records']}** ({reference['summary']['holding_records']} holding, {reference['summary']['input_records']} input)  ",
        f"Live read verified: **{reference['summary']['live_read_verified']}**  ",
        "Write verified: **0** (the current hardware evidence is read-only)",
        "",
        "## Family overview",
        "",
        "| Family | Holding coverage | Input coverage | Resolution quality | Live validation |",
        "|---|---:|---:|---|---:|",
    ]
    for family in reference["families"]:
        coverage = family["coverage"]
        counts = coverage["by_resolution_status"]
        quality = (
            ", ".join(
                f"{status}={counts[status]}"
                for status in STATUS_VALUES
                if counts[status]
            )
            or "none"
        )
        lines.append(
            f"| {markdown_escape(family['name'])} | {coverage['holding']} | {coverage['input']} | {quality} | {coverage['live_read_verified']} |"
        )
    lines.extend(
        [
            "",
            "## How to read the reference",
            "",
            "Identity is always **family + table + address**. Holding register 3047 and input register 3047 are therefore separate records and are not merged. `RESOLVED_WITH_NOTES` is deliberately publishable but retains source differences; `SOURCE_ONLY`, `CONFLICTED` and `UNKNOWN_RESERVED` are not hidden.",
            "",
            "### Evidence legend",
            "",
            "- `source_claim`: a retained source explicitly describes the register.",
            "- `semantic_correlated`: at least two independent source classes support the interpretation.",
            "- `read_verified`: a live read matched the interpretation; it does not mean writable.",
            "- `write_accepted`, `write_reversible`, `behavior_verified`: no entries have these in this release.",
            "",
            "### Provenance and lineage",
            "",
            "The graph export, datatype catalogues and overlays are generated or curated derivatives. They are retained for audit but do not count as independent corroboration of their own upstream claims. The MIN 6000TL-XH model overlay is reconciled against the runtime mapping and the read-only live validation. In particular, BMS register 3217 is published as input-table signed int16 / 100 A; the older model-map placement under holding is retained as a table-reconciliation note.",
            "",
            "## Register tables by family",
            "",
        ]
    )
    for family in reference["families"]:
        lines.extend([f"### {family['name']}", "", family.get("notes", ""), ""])
        family_records = [
            record
            for record in reference["records"]
            if record["family"] == family["id"]
        ]
        lines.extend(
            [
                "| Table | Address | Name | Description | Encoding / scale | Unit | Access | Status | Evidence | Notes |",
                "|---|---:|---|---|---|---|---|---|---|---|",
            ]
        )
        for record in family_records:
            scale = record.get("encoding", "")
            if record.get("divisor") is not None:
                scale += f"; /{record['divisor']}"
            evidence = ", ".join(record.get("evidence_levels", [])) or "—"
            notes = "; ".join(conflict["detail"] for conflict in record.get("conflicts", [])) or "—"
            lines.append(
                "| "
                + " | ".join(
                    [
                        record["table"],
                        str(record["address"]),
                        markdown_escape(record["canonical_name"]),
                        markdown_escape(record.get("description") or "—"),
                        markdown_escape(scale),
                        markdown_escape(record.get("unit") or "—"),
                        record["access"],
                        record["resolution_status"],
                        markdown_escape(evidence),
                        markdown_escape(notes),
                    ]
                )
                + " |"
            )
        lines.append("")
    lines.extend(
        [
            "## Remaining gaps",
            "",
            "- MIN/TL-XH is materially stronger than the other families because it has model-specific live reads; the other families are primarily source/correlation based.",
            "- No register has genuine write-accepted, write-reversible or behavior-verified evidence in this release.",
            "- Some vendor, Grott and external layouts use different width/signedness conventions; alternatives and conflicts remain attached to the JSON records.",
            "- Shine/proprietary protocol traffic and broker transport behavior are intentionally outside this register-reference release.",
            "",
            "Original evidence files are retained in `doc/` and the local research checkouts; this generated reference is the recommended normal lookup.",
            "",
        ]
    )
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=OUTPUT_PATH)
    parser.add_argument("--markdown", type=Path, default=MARKDOWN_PATH)
    args = parser.parse_args()
    reference = build_reference()
    args.output.write_text(
        json.dumps(reference, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )
    args.markdown.write_text(render_markdown(reference), encoding="utf-8")
    print(json.dumps(reference["summary"], indent=2, sort_keys=True))
    print(f"wrote {args.output}")
    print(f"wrote {args.markdown}")


if __name__ == "__main__":
    main()
