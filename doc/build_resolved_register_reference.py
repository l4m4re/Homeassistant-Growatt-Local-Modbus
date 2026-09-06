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
HA_RUNTIME_PATH = DOC_DIR / "HA_local_registers.json"
MIN_BLOCK_VALIDATION_PATH = DOC_DIR / "min_6000tl_xh_block_validation.json"
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
    "min_block_validation": {
        "label": "MIN 6000TL-XH bounded block-read validation",
        "kind": "live_hardware_evidence",
        "path": "min_6000tl_xh_block_validation.json",
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

SEMANTIC_DEFINITIONS: dict[str, dict[str, Any]] = {
    "inverter_status": {
        "name": "Inverter operating status",
        "category": "status",
        "aliases": ["status_code", "Inverter status", "operating state"],
    },
    "battery_soc": {
        "name": "Battery state of charge",
        "category": "battery",
        "aliases": ["battery_soc", "batSoc", "Battery SOC", "BMS SOC", "SOC"],
    },
    "battery_voltage": {
        "name": "Battery voltage",
        "category": "battery",
        "aliases": ["battery_voltage", "Battery voltage", "BMS battery voltage"],
    },
    "battery_current": {
        "name": "Battery current",
        "category": "battery",
        "aliases": ["battery_current", "Battery current", "BMS battery current"],
    },
    "battery_discharge_power": {
        "name": "Battery discharge power",
        "category": "battery",
        "aliases": ["discharge_power", "Battery discharge power", "Pdischarge"],
    },
    "battery_charge_power": {
        "name": "Battery charge power",
        "category": "battery",
        "aliases": ["charge_power", "Battery charge power", "Pcharge"],
    },
    "pv_total_power": {
        "name": "PV total power",
        "category": "telemetry",
        "aliases": ["input_power", "Total PV/input power", "PV total power"],
    },
    "grid_import_power": {
        "name": "Grid import power",
        "category": "telemetry",
        "aliases": ["power_to_user", "Power to user/grid import", "grid import"],
    },
    "grid_export_power": {
        "name": "Grid export power",
        "category": "telemetry",
        "aliases": ["power_to_grid", "Power to grid/export", "grid export"],
    },
    "house_load_power": {
        "name": "House load power",
        "category": "telemetry",
        "aliases": ["power_user_load", "User load power", "house load"],
    },
    "grid_frequency": {
        "name": "Grid frequency",
        "category": "telemetry",
        "aliases": ["grid_frequency", "Grid frequency"],
    },
    "ac_charge_enabled": {
        "name": "AC charging enabled",
        "category": "control",
        "aliases": ["ac_charge_enabled", "AC charge enabled"],
    },
    "battery_first_charge_rate": {
        "name": "Battery-first charge power rate",
        "category": "control",
        "aliases": ["Battery-first charge power rate"],
    },
    "battery_first_stop_soc": {
        "name": "Battery-first stop SOC",
        "category": "control",
        "aliases": ["Battery-first stop SOC"],
    },
    "grid_first_discharge_rate": {
        "name": "Grid-first discharge power rate",
        "category": "control",
        "aliases": ["Grid-first discharge power rate"],
    },
    "grid_first_stop_soc": {
        "name": "Grid-first stop SOC",
        "category": "control",
        "aliases": ["Grid-first stop SOC"],
    },
    "load_first_stop_soc": {
        "name": "Load-first stop SOC",
        "category": "control",
        "aliases": ["Load-first stop SOC"],
    },
    "ac_phase_l3_power": {
        "name": "AC phase L3 power",
        "category": "telemetry",
        "aliases": ["output_3_power", "AC phase L3 power", "Pac3H", "Pac3L"],
    },
    "inverter_runtime": {
        "name": "Inverter runtime",
        "category": "telemetry",
        "aliases": ["operation_hours", "Inverter runtime", "runtime"],
    },
    "pv4_energy_total": {
        "name": "PV4 energy total",
        "category": "energy",
        "aliases": ["PV4 energy total", "input_4_energy_total"],
    },
}

SEMANTIC_RULES: tuple[tuple[str, re.Pattern[str]], ...] = tuple(
    (key, re.compile(pattern, re.IGNORECASE))
    for key, pattern in (
        ("battery_first_charge_rate", r"battery[- ]first.*charge.*rate"),
        ("battery_first_stop_soc", r"battery[- ]first.*stop.*soc"),
        ("grid_first_discharge_rate", r"grid[- ]first.*discharge.*rate"),
        ("grid_first_stop_soc", r"grid[- ]first.*stop.*soc"),
        ("load_first_stop_soc", r"load[- ]first.*stop.*soc"),
        ("ac_charge_enabled", r"(?:ac|grid).*charge.*enabled|ac_charge_enabled"),
        ("grid_import_power", r"power_to_user|user/grid import|grid import"),
        ("grid_export_power", r"power_to_grid|grid/export|grid export"),
        ("house_load_power", r"power_user_load|user load power|house load"),
        ("battery_discharge_power", r"discharge_power|battery discharge power"),
        ("battery_charge_power", r"charge_power|battery charge power"),
        ("battery_voltage", r"battery voltage|bms battery voltage"),
        ("battery_current", r"battery current|bms battery current"),
        ("battery_soc", r"battery soc|bms soc|state.?of.?charge|(?:^|\W)soc(?:$|\W)"),
        ("pv_total_power", r"total pv/input power|input_power|pv total power"),
        ("inverter_status", r"inverter status|status_code|operating state"),
        ("grid_frequency", r"grid_frequency|grid frequency"),
        ("ac_phase_l3_power", r"output_3_power|ac phase l3 power|pac3[hl]"),
        ("inverter_runtime", r"operation_hours|inverter runtime|runtime"),
        ("pv4_energy_total", r"pv4 energy total|input_4_energy_total"),
    )
)

PROTOCOL_TRANSPORT_MODEL = {
    "120": {
        "name": "Modern 120-family / V1.24",
        "minimum_cmd_period_ms": 850,
        "recommended_cmd_period_ms": 1000,
        "maximum_read_words": 125,
        "maximum_write_words": 125,
        "vendor_defined_read_blocks": [
            {"table": "holding", "start": 0, "count": 125, "end": 124},
            {"table": "holding", "start": 3000, "count": 125, "end": 3124},
            {
                "table": "holding",
                "start": 3125,
                "count": 125,
                "end": 3249,
                "applicability": "TL-XH US where applicable",
            },
            {"table": "input", "start": 3000, "count": 125, "end": 3124},
            {"table": "input", "start": 3125, "count": 125, "end": 3249},
            {"table": "input", "start": 3250, "count": 125, "end": 3374},
        ],
        "source": "Growatt-Inverter-Modbus-RTU-Protocol_II-V1_24-English.txt lines 45-62, 211-216",
    },
    "3.15": {
        "name": "Older V3.14 / 3.15-family",
        "minimum_cmd_period_ms": 850,
        "recommended_cmd_period_ms": 1000,
        "maximum_read_words": 45,
        "maximum_write_words": 45,
        "vendor_defined_read_blocks": [
            {
                "description": "Vendor-defined 45-word grouping boundaries; crossing restrictions apply."
            }
        ],
        "source": "Growatt PV Inverter Modbus RS485 RTU Protocol V3.14; family-specific validation not performed here",
    },
    "SPF": {
        "name": "SPF family",
        "minimum_cmd_period_ms": None,
        "recommended_cmd_period_ms": None,
        "maximum_read_words": None,
        "maximum_write_words": None,
        "vendor_defined_read_blocks": [],
        "source": "Not resolved in this release; do not inherit V1.24/V3.14 limits",
    },
}

MIN_LEGACY_BRIDGES = (("input", 1014),)

SEMANTIC_ROLE_OVERRIDES = {
    ("min_tl_xh", "input", 1014): "legacy",
    ("min_tl_xh", "input", 3171): "preferred",
    ("min_tl_xh", "input", 3215): "alternate",
    ("min_tl_xh", "input", 3169): "preferred",
    ("min_tl_xh", "input", 3216): "alternate",
    ("min_tl_xh", "input", 3170): "preferred",
    ("min_tl_xh", "input", 3217): "alternate",
}

MIN_CAPABILITY_DEFINITIONS = (
    {
        "key": "pv_generation",
        "name": "PV generation telemetry",
        "semantic_keys": ["pv_total_power"],
    },
    {
        "key": "grid_exchange",
        "name": "Grid import/export telemetry",
        "semantic_keys": ["grid_import_power", "grid_export_power"],
    },
    {
        "key": "house_load",
        "name": "House load telemetry",
        "semantic_keys": ["house_load_power"],
    },
    {
        "key": "battery_telemetry",
        "name": "Battery voltage/current/SOC telemetry",
        "semantic_keys": [
            "battery_voltage",
            "battery_current",
            "battery_soc",
            "battery_discharge_power",
            "battery_charge_power",
        ],
    },
    {
        "key": "bms_telemetry",
        "name": "BMS telemetry",
        "semantic_keys": ["battery_soc", "battery_voltage", "battery_current"],
        "preferred_addresses": [3215, 3216, 3217],
    },
    {
        "key": "dynamic_tariff_controls",
        "name": "Dynamic-tariff charge/discharge controls",
        "semantic_keys": [
            "ac_charge_enabled",
            "battery_first_charge_rate",
            "battery_first_stop_soc",
            "grid_first_discharge_rate",
            "grid_first_stop_soc",
            "load_first_stop_soc",
        ],
    },
)

READ_PLAN_PROFILES = (
    {
        "id": "min_dynamic_tariff",
        "name": "MIN/TL-XH dynamic-tariff control and telemetry",
        "semantic_keys": [
            "inverter_status",
            "pv_total_power",
            "grid_import_power",
            "grid_export_power",
            "house_load_power",
            "battery_voltage",
            "battery_current",
            "battery_soc",
            "battery_discharge_power",
            "battery_charge_power",
            "ac_charge_enabled",
            "battery_first_charge_rate",
            "battery_first_stop_soc",
            "grid_first_discharge_rate",
            "grid_first_stop_soc",
            "load_first_stop_soc",
        ],
        "max_register_words": 125,
    },
    {
        "id": "min_bms_diagnostics",
        "name": "MIN/TL-XH BMS diagnostics",
        "semantic_keys": ["battery_soc", "battery_voltage", "battery_current"],
        "preferred_addresses": [3215, 3216, 3217],
        "max_register_words": 125,
    },
)


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


def semantic_match(text: str) -> str | None:
    for key, pattern in SEMANTIC_RULES:
        if pattern.search(text):
            return key
    return None


def semantic_for_record(
    canonical_name: str, description: str, aliases: dict[str, list[str]]
) -> tuple[str | None, dict[str, Any]]:
    alias_text = " ".join(value for values in aliases.values() for value in values)
    semantic_key = semantic_match(f"{canonical_name} {description} {alias_text}")
    if semantic_key is None:
        return None, {}
    definition = SEMANTIC_DEFINITIONS[semantic_key]
    return semantic_key, {
        "semantic_key": semantic_key,
        "semantic_name": definition["name"],
        "semantic_aliases": definition["aliases"],
    }


def record_length(raw: dict[str, Any], parsed_type: dict[str, Any]) -> int:
    candidates = [
        int(raw.get("data_width_words", 0) or 0),
        int(parsed_type.get("length_bytes", 0) / 2),
    ]
    for source_rows in raw.get("sources", {}).values():
        rows = source_rows if isinstance(source_rows, list) else [source_rows]
        for row in rows:
            if not isinstance(row, dict):
                continue
            if row.get("length"):
                candidates.append(int(row["length"]))
            if row.get("register_start") == raw.get("register") and row.get(
                "register_end"
            ):
                candidates.append(
                    int(row["register_end"]) - int(row["register_start"]) + 1
                )
    return max([candidate for candidate in candidates if candidate > 0] or [1])


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
    semantic_key, semantic_fields = semantic_for_record(
        canonical_name, raw.get("help") or raw.get("tooltip") or "", aliases
    )
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
        "length_registers": record_length(raw, parsed_type),
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
        "semantic_key": semantic_key,
        "semantic_name": semantic_fields.get("semantic_name"),
        "semantic_aliases": semantic_fields.get("semantic_aliases", []),
        "semantic_role": "unknown" if semantic_key is None else "supported",
        "alternate_registers": [],
        "relationships": [],
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
        "applicability": {
            "status": "family_source_range",
            "models": [],
        },
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


def refresh_semantic(record: dict[str, Any]) -> None:
    semantic_key, semantic_fields = semantic_for_record(
        record.get("canonical_name", ""),
        record.get("description", ""),
        record.get("source_aliases", {}),
    )
    record["semantic_key"] = semantic_key
    record["semantic_name"] = semantic_fields.get("semantic_name")
    record["semantic_aliases"] = semantic_fields.get("semantic_aliases", [])
    record["semantic_role"] = "unknown" if semantic_key is None else "supported"


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
            "applicability": {
                "status": "live_read_verified"
                if live_match(live_index, record["table"], record["address"])
                else "model_overlay",
                "models": [row.get("applicability", "MIN 6000TL-XH")],
            },
        }
    )
    refresh_semantic(record)
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


def add_min_legacy_bridges(
    records: dict[tuple[str, str, int], dict[str, Any]],
    canonical: dict[str, Any],
    family: dict[str, Any],
) -> None:
    for table, address in MIN_LEGACY_BRIDGES:
        source = canonical.get("canonical_registers", {}).get(
            f"register:{table}:{address}"
        )
        if source is None:
            continue
        key = (family["id"], table, address)
        record = base_record(source, family, table, address)
        record["model_applicability"] = ["MIN/TL-XH legacy/base map"]
        record["applicability"] = {
            "status": "legacy_source_supported",
            "models": ["MIN 6000TL-XH"],
        }
        record["notes"] = (
            "Legacy/base register retained because newer TL-XH families may expose "
            "the older storage block; no MIN live read was issued for this address."
        )
        records[key] = record


def add_semantic_relationships(
    records: list[dict[str, Any]],
) -> None:
    grouped: dict[tuple[str, str], list[dict[str, Any]]] = defaultdict(list)
    for record in records:
        if record.get("semantic_key"):
            grouped[(record["family"], record["semantic_key"])].append(record)
    for group in grouped.values():
        group.sort(key=lambda item: (item["table"], item["address"]))
        preferred = next(
            (
                item
                for item in group
                if SEMANTIC_ROLE_OVERRIDES.get(
                    (item["family"], item["table"], item["address"])
                )
                == "preferred"
            ),
            None,
        )
        if preferred is None and len(group) > 1:
            preferred = next(
                (item for item in group if "read_verified" in item["evidence_levels"]),
                group[0],
            )
        for record in group:
            override = SEMANTIC_ROLE_OVERRIDES.get(
                (record["family"], record["table"], record["address"])
            )
            record["semantic_role"] = override or (
                "supported" if len(group) == 1 else "alternate"
            )
            alternate_records = [item for item in group if item is not record]
            record["alternate_registers"] = [item["id"] for item in alternate_records]
            record["relationships"] = [
                {
                    "type": "alternate_registers",
                    "target": item["id"],
                }
                for item in alternate_records
            ]
            if preferred is not None and preferred is not record:
                record["relationships"].append(
                    {
                        "type": "preferred_register",
                        "target": preferred["id"],
                    }
                )
                if record["semantic_role"] == "legacy":
                    record["relationships"].append(
                        {"type": "superseded_by", "target": preferred["id"]}
                    )
            if preferred is record:
                for item in alternate_records:
                    if item["semantic_role"] == "legacy":
                        record["relationships"].append(
                            {"type": "supersedes", "target": item["id"]}
                        )
            record["relationships"] = sorted(
                record["relationships"],
                key=lambda item: (item["type"], item["target"]),
            )


def build_capability_validation(
    records: list[dict[str, Any]],
) -> dict[str, Any]:
    family_records = [record for record in records if record["family"] == "min_tl_xh"]
    by_semantic: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for record in family_records:
        if record.get("semantic_key"):
            by_semantic[record["semantic_key"]].append(record)
    capabilities = []
    for definition in MIN_CAPABILITY_DEFINITIONS:
        selected = []
        for semantic_key in definition["semantic_keys"]:
            candidates = by_semantic.get(semantic_key, [])
            preferred_addresses = definition.get("preferred_addresses", [])
            if preferred_addresses:
                candidates = [
                    candidate
                    for candidate in candidates
                    if candidate["address"] in preferred_addresses
                ]
            candidate = next(
                (item for item in candidates if item["semantic_role"] == "preferred"),
                next(
                    (
                        item
                        for item in candidates
                        if "read_verified" in item["evidence_levels"]
                    ),
                    candidates[0] if candidates else None,
                ),
            )
            if candidate is not None:
                selected.append(candidate)
        complete = len(selected) == len(definition["semantic_keys"])
        read_verified = complete and all(
            "read_verified" in record["evidence_levels"] for record in selected
        )
        capabilities.append(
            {
                "key": definition["key"],
                "name": definition["name"],
                "semantic_keys": definition["semantic_keys"],
                "status": (
                    "read_verified"
                    if read_verified
                    else "source_supported"
                    if complete
                    else "missing_registers"
                ),
                "supporting_registers": [record["id"] for record in selected],
                "write_verified": False,
                "write_policy": "Read-only evidence; no writes were issued.",
            }
        )
    return {
        "family": "min_tl_xh",
        "model": "MIN 6000TL-XH",
        "evidence_source": "min_live_validation",
        "capabilities": capabilities,
    }


def choose_read_records(
    records: list[dict[str, Any]], profile: dict[str, Any]
) -> list[dict[str, Any]]:
    candidates = [
        record
        for record in records
        if record["family"] == profile.get("family", "min_tl_xh")
    ]
    selected = []
    for semantic_key in profile["semantic_keys"]:
        matching = [
            record
            for record in candidates
            if record.get("semantic_key") == semantic_key
        ]
        preferred_addresses = profile.get("preferred_addresses", [])
        if preferred_addresses:
            matching = [
                record
                for record in matching
                if record["address"] in preferred_addresses
            ]
        record = next(
            (item for item in matching if item["semantic_role"] == "preferred"),
            next(
                (
                    item
                    for item in matching
                    if "read_verified" in item["evidence_levels"]
                ),
                matching[0] if matching else None,
            ),
        )
        if record is not None and record not in selected:
            selected.append(record)
    return sorted(selected, key=lambda item: (item["table"], item["address"]))


def plan_contiguous_blocks(
    records: list[dict[str, Any]],
    max_register_words: int,
    safe_ranges: list[dict[str, Any]] | None = None,
) -> list[dict[str, Any]]:
    if safe_ranges:
        blocks = []
        assigned: set[str] = set()
        for safe_range in sorted(
            safe_ranges, key=lambda item: (item["table"], item["start"])
        ):
            covered = [
                record
                for record in records
                if record["id"] not in assigned
                and record["table"] == safe_range["table"]
                and record["address"] >= safe_range["start"]
                and record["address"] + record["length_registers"] - 1
                <= safe_range["end"]
            ]
            if not covered:
                continue
            assigned.update(record["id"] for record in covered)
            blocks.append(
                {
                    "table": safe_range["table"],
                    "function_code": 3 if safe_range["table"] == "holding" else 4,
                    "start": safe_range["start"],
                    "count": safe_range["count"],
                    "end": safe_range["end"],
                    "registers": [record["id"] for record in covered],
                    "required_semantic_keys": sorted(
                        {
                            record["semantic_key"]
                            for record in covered
                            if record.get("semantic_key")
                        }
                    ),
                    "additional_words_fetched": safe_range["count"]
                    - sum(record["length_registers"] for record in covered),
                    "gap_words": safe_range["count"]
                    - sum(record["length_registers"] for record in covered),
                    "hardware_block_read_validated": safe_range.get(
                        "hardware_block_read_validated", False
                    ),
                    "safe_range_id": safe_range.get("id"),
                    "source_basis": safe_range.get("source_basis", []),
                    "validation": {
                        "maximum_tested_block_length": safe_range.get(
                            "maximum_tested_block_length"
                        ),
                        "all_words_respond_safely": safe_range.get(
                            "all_words_respond_safely"
                        ),
                        "repeatability": safe_range.get("repeatability"),
                        "observed_response_seconds": safe_range.get(
                            "observed_response_seconds", []
                        ),
                    },
                }
            )
        records = [record for record in records if record["id"] not in assigned]

    blocks = blocks if safe_ranges else []
    for table in ("holding", "input"):
        table_records = [record for record in records if record["table"] == table]
        current: list[dict[str, Any]] = []
        current_start = current_end = None
        for record in table_records:
            start = record["address"]
            end = start + record["length_registers"] - 1
            proposed_end = end if current_end is None else max(current_end, end)
            if current and proposed_end - current_start + 1 > max_register_words:
                blocks.append(
                    {
                        "table": table,
                        "function_code": 3 if table == "holding" else 4,
                        "start": current_start,
                        "count": current_end - current_start + 1,
                        "end": current_end,
                        "registers": [record["id"] for record in current],
                        "required_semantic_keys": sorted(
                            {
                                record["semantic_key"]
                                for record in current
                                if record.get("semantic_key")
                            }
                        ),
                        "additional_words_fetched": current_end
                        - current_start
                        + 1
                        - sum(item["length_registers"] for item in current),
                        "gap_words": (
                            current_end
                            - current_start
                            + 1
                            - sum(item["length_registers"] for item in current)
                        ),
                        "hardware_block_read_validated": False,
                        "source_basis": ["resolved_reference_contiguous_fallback"],
                    }
                )
                current = []
                current_start = current_end = None
            if not current:
                current_start = start
            current.append(record)
            current_end = end if current_end is None else max(current_end, end)
        if current:
            blocks.append(
                {
                    "table": table,
                    "function_code": 3 if table == "holding" else 4,
                    "start": current_start,
                    "count": current_end - current_start + 1,
                    "end": current_end,
                    "registers": [record["id"] for record in current],
                    "required_semantic_keys": sorted(
                        {
                            record["semantic_key"]
                            for record in current
                            if record.get("semantic_key")
                        }
                    ),
                    "additional_words_fetched": current_end
                    - current_start
                    + 1
                    - sum(item["length_registers"] for item in current),
                    "gap_words": (
                        current_end
                        - current_start
                        + 1
                        - sum(item["length_registers"] for item in current)
                    ),
                    "hardware_block_read_validated": False,
                    "source_basis": ["resolved_reference_contiguous_fallback"],
                }
            )
    return blocks


def build_read_plans(
    records: list[dict[str, Any]], block_validation: dict[str, Any]
) -> dict[str, Any]:
    safe_ranges = block_validation.get("validated_ranges", [])
    profiles = []
    for profile in READ_PLAN_PROFILES:
        selected = choose_read_records(records, profile)
        blocks = plan_contiguous_blocks(
            selected, profile["max_register_words"], safe_ranges
        )
        profiles.append(
            {
                "id": profile["id"],
                "name": profile["name"],
                "selection_semantic_keys": profile["semantic_keys"],
                "selected_registers": [record["id"] for record in selected],
                "max_register_words": profile["max_register_words"],
                "transaction_count": len(blocks),
                "blocks": blocks,
            }
        )
    source_derived_profiles = []
    core_profile = {
        "semantic_keys": [
            "inverter_status",
            "pv_total_power",
            "grid_frequency",
            "grid_import_power",
            "grid_export_power",
            "house_load_power",
            "battery_voltage",
            "battery_current",
            "battery_soc",
        ]
    }
    for family in FAMILY_DEFINITIONS:
        if family["id"] == "min_tl_xh":
            continue
        transport = PROTOCOL_TRANSPORT_MODEL[family["protocol_group"]]
        if transport["maximum_read_words"] is None:
            continue
        family_profile = {**core_profile, "family": family["id"]}
        selected = choose_read_records(records, family_profile)
        blocks = plan_contiguous_blocks(selected, transport["maximum_read_words"])
        source_derived_profiles.append(
            {
                "id": f"{family['id']}_core_source_derived",
                "family": family["id"],
                "name": f"{family['name']} core telemetry (source-derived)",
                "polling_class": "CORE_TELEMETRY",
                "selection_semantic_keys": core_profile["semantic_keys"],
                "selected_registers": [record["id"] for record in selected],
                "max_register_words": transport["maximum_read_words"],
                "transaction_count": len(blocks),
                "hardware_validated": False,
                "blocks": blocks,
            }
        )
    return {
        "planning_policy": "Use vendor-declared native blocks first; optimize transaction count, not returned-word count. Decode selected semantic values locally and do not expose fetched gaps as entities.",
        "transaction_rate_assumption": "Vendor V1.24 minimum command period is 850 ms; vendor recommendation and current broker period are 1000 ms.",
        "vendor_transport": PROTOCOL_TRANSPORT_MODEL["120"],
        "vendor_declared_blocks": block_validation.get("vendor_declared_blocks", []),
        "hardware_validated_ranges": [
            item["id"] for item in block_validation.get("validated_ranges", [])
        ],
        "hardware_validated_pages": [
            {
                "id": item["id"],
                "table": item["table"],
                "function_code": item["function_code"],
                "start": item["start"],
                "count": item["count"],
                "end": item["end"],
                "polling_class": item["polling_class"],
                "applicability": item["applicability"],
                "required_semantic_keys": item["required_semantic_keys"],
                "additional_words_fetched": item["additional_words_fetched"],
                "hardware_block_read_validated": item["hardware_block_read_validated"],
                "repeatability": item["repeatability"],
                "observed_response_seconds": item["observed_response_seconds"],
            }
            for item in block_validation.get("validated_ranges", [])
        ],
        "profiles": profiles,
        "source_derived_profiles": source_derived_profiles,
    }


def build_runtime_audit(
    records: list[dict[str, Any]], runtime: dict[str, Any]
) -> dict[str, Any]:
    family_by_group = {
        ("tlx", "holding_common"): "min_tl_xh",
        ("tlx", "input_tl_xh"): "min_tl_xh",
        ("storage", "holding_tl_xh"): "min_tl_xh",
        ("storage", "input_tl_xh"): "min_tl_xh",
        ("storage", "input_common"): "storage_mix",
    }
    by_identity = {
        (record["family"], record["table"], record["address"]): record
        for record in records
    }
    findings = []
    checked = 0
    for device, payload in runtime.get("devices", {}).items():
        for group_name, rows in payload.items():
            family = family_by_group.get((device, group_name))
            if family is None or not isinstance(rows, list):
                continue
            table = "holding" if "holding" in group_name else "input"
            for row in rows:
                if not isinstance(row, dict) or "register" not in row:
                    continue
                checked += 1
                address = int(row["register"])
                record = by_identity.get((family, table, address))
                runtime_name = str(row.get("name", ""))
                runtime_semantic = semantic_match(runtime_name)
                base = {
                    "device": device,
                    "group": group_name,
                    "family": family,
                    "table": table,
                    "address": address,
                    "runtime_name": runtime_name,
                    "runtime_semantic_key": runtime_semantic,
                }
                if record is None:
                    findings.append({**base, "kind": "missing_reference_record"})
                    continue
                issues = []
                if int(row.get("length", 1)) != record["length_registers"]:
                    issues.append(
                        {
                            "kind": "length_mismatch",
                            "reference": record["length_registers"],
                            "runtime": row.get("length", 1),
                        }
                    )
                runtime_signed = bool(row.get("signed", False))
                # process_registers decodes all two-word float values as signed
                # int32, even when the dataclass flag is absent.
                effective_runtime_signed = runtime_signed or (
                    row.get("value_type") == "float" and row.get("length", 1) == 2
                )
                if (
                    record["signed"] is not None
                    and effective_runtime_signed != record["signed"]
                ):
                    issues.append(
                        {
                            "kind": "signedness_mismatch",
                            "reference": record["signed"],
                            "runtime": effective_runtime_signed,
                            "declared": runtime_signed,
                        }
                    )
                if row.get("value_type") == "float" and record["divisor"] is not None:
                    runtime_scale = row.get("scale", 10)
                    if float(runtime_scale) != float(record["divisor"]):
                        issues.append(
                            {
                                "kind": "scale_mismatch",
                                "reference": record["divisor"],
                                "runtime": runtime_scale,
                            }
                        )
                if (
                    runtime_semantic is not None
                    and record.get("semantic_key") is not None
                    and runtime_semantic != record["semantic_key"]
                ):
                    issues.append(
                        {
                            "kind": "semantic_mismatch",
                            "reference": record["semantic_key"],
                            "runtime": runtime_semantic,
                        }
                    )
                if issues:
                    findings.append(
                        {**base, "reference_id": record["id"], "issues": issues}
                    )
    return {
        "source": "HA_local_registers",
        "checked_mappings": checked,
        "finding_count": len(findings),
        "status": "consistent" if not findings else "issues_found",
        "findings": findings,
    }


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
    runtime = load_json(HA_RUNTIME_PATH)
    block_validation = load_json(MIN_BLOCK_VALIDATION_PATH)
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

    add_min_legacy_bridges(records, canonical, min_family)

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
    add_semantic_relationships(ordered_records)
    capability_validation = build_capability_validation(ordered_records)
    read_plans = build_read_plans(ordered_records, block_validation)
    runtime_audit = build_runtime_audit(ordered_records, runtime)
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
                    "transport": PROTOCOL_TRANSPORT_MODEL[family["protocol_group"]],
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
        "min_block_validation": MIN_BLOCK_VALIDATION_PATH,
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
        "semantic_model": SEMANTIC_DEFINITIONS,
        "protocol_transport_model": PROTOCOL_TRANSPORT_MODEL,
        "capability_validation": capability_validation,
        "read_plans": read_plans,
        "runtime_audit": runtime_audit,
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
        f"Reference version: `{reference['meta']['reference_version']}`",
        f"Records: **{reference['summary']['total_records']}** ({reference['summary']['holding_records']} holding, {reference['summary']['input_records']} input)",
        f"Live read verified: **{reference['summary']['live_read_verified']}**",
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
            "## Semantic concepts and MIN capabilities",
            "",
            "Physical identity remains family + table + address. `semantic_key` is the stable implementation-neutral concept identity, so multiple physical registers can intentionally represent one concept. The MIN/TL-XH legacy/base `input 1014` SOC register is retained alongside preferred `input 3171`; it is not merged with it.",
            "",
            "| Capability | Status | Supporting registers | Write verified |",
            "|---|---|---|---:|",
        ]
    )
    lines.extend(
        [
            f"| {markdown_escape(capability['name'])} | {capability['status']} | "
            f"{markdown_escape(', '.join(capability['supporting_registers'])) or '—'} | "
            f"{'yes' if capability['write_verified'] else 'no'} |"
            for capability in reference["capability_validation"]["capabilities"]
        ]
    )
    lines.extend(
        [
            "",
            "### Family-specific block-read plans",
            "",
            "The vendor V1.24 transport model declares an 850 ms minimum command period, recommends 1 second, and permits up to 125 words per read. The current MIN hardware evidence validates the complete native pages below twice each; the observed response durations are device evidence, not a replacement for the vendor timing rule.",
            "",
            f"Vendor transport: **{reference['read_plans']['vendor_transport']['minimum_cmd_period_ms']} ms minimum**, **{reference['read_plans']['vendor_transport']['recommended_cmd_period_ms']} ms recommended**, **{reference['read_plans']['vendor_transport']['maximum_read_words']} words maximum**.",
            "",
            "Semantic selection and physical read planning are separate. These plans optimize Modbus transaction count first; local decoding extracts the selected registers from each returned block. Holding and input spaces always remain separate FC03/FC04 transactions.",
            "",
            "| Profile | Transactions | Blocks |",
            "|---|---:|---|",
        ]
    )
    for profile in reference["read_plans"]["profiles"]:
        block_text = "; ".join(
            f"FC{block['function_code']} {block['start']}+{block['count']}"
            for block in profile["blocks"]
        )
        lines.append(
            f"| {markdown_escape(profile['name'])} | {profile['transaction_count']} | "
            f"{markdown_escape(block_text)} |"
        )
    lines.extend(
        [
            "",
            "#### Hardware-validated native pages",
            "",
            "These are the bounded live MIN 6000TL-XH page probes used by the planner. `additional_words_fetched` are decoded locally only; they do not become Home Assistant entities.",
            "",
            "| Page | Class | Function | Range | Required semantics | Extra words | Repeatability |",
            "|---|---|---:|---|---|---:|---|",
        ]
    )
    lines.extend(
        [
            f"| {page['id']} | {page['polling_class']} | FC{page['function_code']} | "
            f"{page['start']}–{page['end']} ({page['count']} words) | "
            f"{markdown_escape(', '.join(page['required_semantic_keys']) or 'none listed')} | "
            f"{page['additional_words_fetched']} | {markdown_escape(page['repeatability'])} |"
            for page in reference["read_plans"].get("hardware_validated_pages", [])
        ]
    )
    lines.extend(
        [
            "",
            "#### Source-derived family plans",
            "",
            "Non-MIN plans are derived from the family/protocol source corpus and are not hardware validated by the live MIN probe.",
            "",
            "| Family plan | Transactions | Maximum words | Hardware validated |",
            "|---|---:|---:|---:|",
        ]
    )
    lines.extend(
        [
            f"| {markdown_escape(profile['name'])} | {profile['transaction_count']} | "
            f"{profile['max_register_words']} | {'yes' if profile.get('hardware_validated') else 'no'} |"
            for profile in reference["read_plans"].get("source_derived_profiles", [])
        ]
    )
    lines.extend(
        [
            "",
            "## Runtime consistency audit",
            "",
            f"HA runtime mappings checked: **{reference['runtime_audit']['checked_mappings']}**; findings: **{reference['runtime_audit']['finding_count']}**; status: **{reference['runtime_audit']['status']}**.",
            "",
        ]
    )
    if reference["runtime_audit"]["findings"]:
        lines.extend(
            [
                "| Family | Table | Address | Runtime name | Finding |",
                "|---|---|---:|---|---|",
            ]
        )
        for finding in reference["runtime_audit"]["findings"]:
            detail = finding.get("kind") or "; ".join(
                issue["kind"] for issue in finding.get("issues", [])
            )
            lines.append(
                f"| {finding['family']} | {finding['table']} | {finding['address']} | "
                f"{markdown_escape(finding['runtime_name'])} | {markdown_escape(detail)} |"
            )
        lines.append("")
    lines.extend(
        [
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
                "| Table | Address | Semantic | Role | Name | Description | Encoding / scale | Unit | Access | Status | Evidence | Notes |",
                "|---|---:|---|---|---|---|---|---|---|---|---|---|",
            ]
        )
        for record in family_records:
            scale = record.get("encoding", "")
            if record.get("divisor") is not None:
                scale += f"; /{record['divisor']}"
            evidence = ", ".join(record.get("evidence_levels", [])) or "—"
            notes = (
                "; ".join(
                    [
                        *(
                            conflict["detail"]
                            for conflict in record.get("conflicts", [])
                        ),
                        record.get("notes", ""),
                        (
                            "alternates: "
                            + ", ".join(record.get("alternate_registers", []))
                            if record.get("alternate_registers")
                            else ""
                        ),
                    ]
                )
                or "—"
            )
            lines.append(
                "| "
                + " | ".join(
                    [
                        record["table"],
                        str(record["address"]),
                        markdown_escape(record.get("semantic_key") or "—"),
                        record.get("semantic_role", "unknown"),
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
