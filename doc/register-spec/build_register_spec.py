#!/usr/bin/env python3
"""Build the project-independent Growatt Register Specification.

The resolved HA-era reference is used as a compatibility input during this
migration.  The output deliberately removes HA-specific semantics from the
public model and adds subsystem, instance, evidence, protocol and logical-field
metadata.  The old reference remains a generated compatibility view; this
directory is the canonical consumer-facing product.
"""

# ruff: noqa: D103, T201

from collections import defaultdict
import json
from pathlib import Path
import re
from typing import Any

SPEC_DIR = Path(__file__).resolve().parent
DOC_DIR = SPEC_DIR.parent
SOURCE_PATH = DOC_DIR / "growatt_register_reference.json"
BLOCK_PATH = DOC_DIR / "min_6000tl_xh_block_validation.json"
OUTPUT_PATH = SPEC_DIR / "growatt-register-spec.json"

FAMILY_SLUGS = {
    "min_tl_xh": "MIN_TL_XH",
    "tl3_max_mid_mac": "TL3_MAX_MID_MAC",
    "mod_tl3_xh": "MOD_TL3_XH",
    "storage_mix": "MIX",
    "storage_spa": "SPA",
    "storage_sph": "SPH",
    "legacy_inverter_315": "LEGACY_315",
    "spf_offgrid": "SPF",
}

SEMANTIC_RENAMES = {
    "battery_current": "battery.current",
    "battery_voltage": "battery.voltage",
    "battery_soc": "battery.soc",
    "battery_charge_power": "battery.charge_power",
    "battery_discharge_power": "battery.discharge_power",
    "pv_total_power": "pv.total_power",
    "grid_import_power": "grid.import_power",
    "grid_export_power": "grid.export_power",
    "house_load_power": "load.house_power",
    "inverter_status": "inverter.status",
    "grid_frequency": "grid.frequency",
    "ac_phase_l3_power": "ac.phase.l3_power",
    "inverter_runtime": "inverter.runtime",
    "pv4_energy_total": "pv.mppt4.energy_total",
}

EXTERNAL_IMPLEMENTATIONS = {
    "grott",
    "openinverter_gateway",
    "inverter_to_mqtt",
}

EVIDENCE_LEVELS = (
    "source_documented",
    "implementation_correlated",
    "read_observed",
    "value_plausible",
    "semantic_verified",
    "write_accepted",
    "write_reversible",
    "behavior_verified",
)

EVIDENCE_DESCRIPTIONS = {
    "source_documented": "A retained vendor or source document explicitly describes the physical field.",
    "implementation_correlated": "Independent implementation families agree with the interpretation; generated derivatives are not counted independently.",
    "read_observed": "The physical address or native block returned successfully from real hardware; this does not establish semantics.",
    "value_plausible": "A retained raw value decodes compatibly with the claimed datatype, scale, unit and expected range.",
    "semantic_verified": "A decoded value or behavior was meaningfully compared with independently trusted device state; none is asserted without that evidence.",
    "write_accepted": "A controlled write was accepted and read back; none is asserted in this release.",
    "write_reversible": "The exact original raw value was restored and verified; none is asserted in this release.",
    "behavior_verified": "Observed device behavior matched the claimed control semantics; none is asserted in this release.",
}


def load(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def slug(value: str) -> str:
    value = re.sub(r"[^A-Za-z0-9]+", " ", value).strip().lower()
    return re.sub(r"\s+", "_", value) or "unknown"


def numeric_or_none(value: Any) -> int | float | None:
    return (
        value
        if isinstance(value, (int, float)) and not isinstance(value, bool)
        else None
    )


def quantity(record: dict[str, Any]) -> str | None:
    key = record.get("semantic_key")
    if key in SEMANTIC_RENAMES:
        return SEMANTIC_RENAMES[key]
    if key:
        return key.replace("_", ".")
    name = str(record.get("canonical_name", "")).strip()
    if name and not name.lower().startswith(("register ", "reserved", "unknown")):
        category = {
            "battery": "battery",
            "control": "control",
            "diagnostic": "diagnostic",
            "energy": "energy",
            "telemetry": "telemetry",
        }.get(record.get("semantic_category"), "field")
        return f"{category}.{slug(name)}"
    return None


def subsystem(record: dict[str, Any]) -> tuple[str, str]:
    text = " ".join(
        [
            str(record.get("canonical_name", "")),
            str(record.get("description", "")),
            " ".join(record.get("source_aliases", {}).get("vendor", [])),
        ]
    ).lower()
    address = record["address"]
    if "bms" in text or address in range(3212, 3232):
        return "bms", "bms"
    if (record.get("semantic_key") or "").startswith("battery") or "battery" in text:
        return "storage_device", "bdc_or_storage_device"
    if "mppt" in text or "pv" in text or "input" in text:
        return "pv", "pv_or_mppt"
    if "grid" in text or "frequency" in text:
        return "grid", "grid_meter_or_inverter"
    if "load" in text:
        return "load", "load_meter_or_inverter"
    if "ac phase" in text or "phase" in text:
        return "ac", "ac_phase"
    if record.get("semantic_category") == "control":
        return "control", "inverter_control"
    if "inverter" in text:
        return "inverter", "inverter"
    return "unknown", "unknown"


def instance_metadata(record: dict[str, Any], sub: str) -> dict[str, Any]:
    text = " ".join(
        [
            str(record.get("canonical_name", "")),
            *record.get("source_aliases", {}).get("vendor", []),
        ]
    )
    mppt = re.search(r"(?:PV|MPPT)\s*([1-9][0-9]*)", text, re.IGNORECASE)
    phase = re.search(r"phase\s*(L[1-3])", text, re.IGNORECASE)
    if mppt:
        return {
            "instance_kind": "mppt",
            "instance": int(mppt.group(1)),
            "instance_status": "vendor_indexed",
            "index_kind": "mppt",
            "index": int(mppt.group(1)),
        }
    if phase:
        return {
            "instance_kind": "ac_phase",
            "instance": None,
            "instance_status": "vendor_indexed",
            "index_kind": "phase",
            "index": phase.group(1).upper(),
        }
    if sub != "bms":
        return {
            "instance_kind": None,
            "instance": None,
            "instance_status": "not_applicable",
            "index_kind": None,
            "index": None,
        }
    return {
        "instance_kind": "bms",
        "instance": None,
        "instance_status": "unknown",
        "index_kind": None,
        "index": None,
        "structure_id": "bms_status_and_telemetry_block",
        "structure_note": "Repeated BMS fields are retained structurally; numeric suffixes on diagnostics do not prove separate BMS instances.",
    }


def evidence(record: dict[str, Any]) -> list[dict[str, Any]]:
    provenance = set(record.get("provenance", []))
    levels: set[str] = set()
    if "vendor_v124" in provenance or "vendor_v314" in provenance:
        levels.add("source_documented")
    if provenance & EXTERNAL_IMPLEMENTATIONS:
        levels.add("implementation_correlated")
    if any(
        item.get("source") == "min_live_validation"
        for item in record.get("validation_evidence", [])
    ):
        levels.add("read_observed")
    if (
        record["family"] == "min_tl_xh"
        and record["table"] == "input"
        and record["address"] == 3217
    ):
        levels.add("value_plausible")
    result = []
    source_ids = sorted({"vendor_v124"} & provenance)
    implementation_ids = sorted(EXTERNAL_IMPLEMENTATIONS & provenance)
    read_ids = ["min_live_validation"] if "min_live_validation" in provenance else []
    for level in EVIDENCE_LEVELS:
        if level in levels:
            sources = {
                "source_documented": source_ids,
                "implementation_correlated": implementation_ids,
                "read_observed": read_ids,
                "value_plausible": ["ha5_regression_tests", "min_live_validation"],
            }.get(level, [])
            result.append({"level": level, "sources": sources})
    return result


def write_policy(record: dict[str, Any]) -> str:
    if record.get("access") not in {"W", "R/W"}:
        return "read_only"
    text = f"{record.get('canonical_name', '')} {record.get('description', '')}".lower()
    dangerous = (
        "reset",
        "factory",
        "firmware",
        "bootloader",
        "baud",
        "modbus address",
        "country",
        "grid code",
        "safety",
        "on/off",
        "shutdown",
        "reboot",
    )
    if any(token in text for token in dangerous):
        return "never_test"
    if any(
        token in text
        for token in ("schedule", "mode", "enable", "frequency", "voltage")
    ):
        return "conditional"
    return "reversible_candidate"


def resolution_from_evidence(
    record: dict[str, Any], evidence_items: list[dict[str, Any]]
) -> dict[str, Any]:
    name = str(record.get("canonical_name", ""))
    if name.lower().startswith(("register ", "reserved", "unknown")):
        return {"status": "unknown_reserved", "confidence": "low"}
    levels = {item["level"] for item in evidence_items}
    has_vendor = "source_documented" in levels
    has_implementation = "implementation_correlated" in levels
    if has_vendor and has_implementation:
        status = "resolved_with_notes" if record.get("conflicts") else "resolved"
        confidence = "medium" if record.get("conflicts") else "high"
    elif has_vendor:
        status, confidence = "source_only", "medium"
    elif has_implementation:
        status, confidence = "source_only", "low"
    else:
        status, confidence = "unknown_reserved", "low"
    result = {"status": status, "confidence": confidence}
    if record.get("conflicts"):
        result["note"] = "; ".join(
            item.get("detail", "") for item in record["conflicts"]
        )
    return result


def normalized_enums(record: dict[str, Any]) -> list[dict[str, Any]]:
    grouped: dict[int, set[str]] = defaultdict(set)
    for item in record.get("enum_definitions", []):
        label = str(item.get("label", "")).strip()
        grouped[item["value"]].add(label)
    return [
        {
            "value": value,
            "canonical_name": slug("_".join(sorted(labels))),
            "vendor_label": " / ".join(sorted(labels)),
            "ambiguous": len(labels) > 1,
        }
        for value, labels in sorted(grouped.items())
    ]


def bitfields(record: dict[str, Any]) -> list[dict[str, Any]]:
    address = record["address"]
    if (
        record["family"] == "min_tl_xh"
        and record["table"] == "input"
        and address == 3187
    ):
        return [
            {"bits": [0], "name": "charge_enabled", "vendor_label": "ChargeEn"},
            {"bits": [1], "name": "discharge_enabled", "vendor_label": "DischargeEn"},
            {"bits": [2, 7], "name": "reserved", "vendor_label": "Resvd"},
            {"bits": [8, 11], "name": "warning_subcode", "vendor_label": "WarnSubCode"},
            {"bits": [12, 15], "name": "fault_subcode", "vendor_label": "FaultSubCode"},
        ]
    text = f"{record.get('canonical_name', '')} {record.get('encoding', '')}".lower()
    if "bitfield" in text or "flags" in text or " flag" in text:
        return [
            {
                "bits": [0, 15],
                "name": "undocumented_flags",
                "status": "undocumented",
                "description": "The source identifies a packed flag word but does not define safe individual meanings.",
            }
        ]
    return []


def logical_fields(records: list[dict[str, Any]]) -> list[dict[str, Any]]:
    fields = []
    for record in records:
        length = record["length_words"]
        if length < 2:
            continue
        fields.append(
            {
                "id": f"logical:{record['physical_id']}",
                "semantic_key": record["semantic_identity"]["quantity"],
                "physical_registers": [
                    {
                        "family": record["family"],
                        "table": record["table"],
                        "address": record["address"] + offset,
                        "role": f"word_{offset + 1}",
                    }
                    for offset in range(length)
                ],
                "encoding": record["normalized"]["raw_type"],
                "word_order": "not_specified_by_canonical_source",
                "scale": record["normalized"]["scale"],
                "unit": record["normalized"]["unit"],
                "status": "structured; word order requires source evidence",
            }
        )
    return fields


def native_blocks(block_validation: dict[str, Any]) -> list[dict[str, Any]]:
    return [
        {
            "id": item["id"],
            "table": item["table"],
            "function_code": item["function_code"],
            "start": item["start"],
            "end": item["end"],
            "count": item["count"],
            "polling_policy": item["polling_class"],
            "applicability": item["applicability"],
            "hardware_validation": {
                "model": block_validation["meta"]["model"],
                "repetitions": len(item["response_word_counts"]),
                "response_word_counts": item["response_word_counts"],
                "exceptions": item["exceptions"],
                "timeouts": item["timeouts"],
                "retries": item["retries"],
                "crc_bad": item["crc_bad"],
                "observed_response_seconds": item["observed_response_seconds"],
                "evidence_level": "read_observed",
            },
        }
        for item in block_validation["validated_ranges"]
    ]


def runtime_audit_projection(source: dict[str, Any]) -> dict[str, Any]:
    runtime = source["runtime_audit"]
    ha_mapping = load(DOC_DIR / "HA_local_registers.json")
    occurrences = 0
    identities: set[tuple[str, int]] = set()
    for payload in ha_mapping.get("devices", {}).values():
        for group, rows in payload.items():
            if not isinstance(rows, list):
                continue
            table = "holding" if "holding" in group else "input"
            for row in rows:
                if isinstance(row, dict) and "register" in row:
                    occurrences += 1
                    identities.add((table, int(row["register"])))
    finding_occurrences = sum(
        len(item.get("issues", [])) for item in runtime["findings"]
    )
    unique_findings = {
        (item["family"], item["table"], item["address"], issue["kind"])
        for item in runtime["findings"]
        for issue in item.get("issues", [])
    }
    return {
        "mapping_occurrences_checked": occurrences,
        "unique_physical_mappings_checked": len(identities),
        "finding_occurrences": finding_occurrences,
        "unique_findings": len(unique_findings),
        "finding_kinds": sorted({kind for *_, kind in unique_findings}),
        "classification_policy": "Derived consumer audit; aliases, legitimate legacy maps, repeated instances and missing HA entity exposure are not register-map errors.",
        "findings": runtime["findings"],
    }


def build() -> dict[str, Any]:
    source = load(SOURCE_PATH)
    block = load(BLOCK_PATH)
    source_records = source["records"]
    records = []
    for old in source_records:
        sub, point = subsystem(old)
        identity = instance_metadata(old, sub)
        semantic = {
            "quantity": quantity(old),
            "canonical_name": old.get("semantic_name") or old.get("canonical_name"),
            "subsystem": sub,
            "measurement_point": point,
            **identity,
        }
        vendor_aliases = old.get("source_aliases", {}).get("vendor", [])
        physical_id = f"{old['family']}:{old['table']}:{old['address']}"
        evidence_items = evidence(old)
        normalized = {
            "name": old.get("canonical_name"),
            "description": old.get("description"),
            "raw_type": old.get("encoding"),
            "signed": old.get("signed"),
            "divisor": numeric_or_none(old.get("divisor")),
            "multiplier": old.get("multiplier"),
            "scale": numeric_or_none(old.get("scale"))
            or numeric_or_none(old.get("multiplier")),
            "unit": old.get("unit"),
            "access": old.get("access"),
        }
        if (
            old["family"] == "min_tl_xh"
            and old["table"] == "input"
            and old["address"] == 3170
        ):
            normalized["signedness_status"] = (
                "implementation_correlated_not_live_sign_validated"
            )
            normalized["signedness_note"] = (
                "Retained live samples show plausible positive Ibat values but no negative raw I3170 sample; vendor/implementation evidence supports signed int16 without making the HA consumer authoritative."
            )
        elif (
            old["family"] == "min_tl_xh"
            and old["table"] == "input"
            and old["address"] == 3217
        ):
            normalized["signedness_status"] = "regression_and_live_value_validated"
            normalized["signedness_note"] = (
                "HA-5 regression 0xFEB6 decodes to -3.30 A at 0.01 A resolution; retained live BMS sample is also negative."
            )
        records.append(
            {
                "physical_id": physical_id,
                "family": old["family"],
                "family_name": old["family_name"],
                "table": old["table"],
                "address": old["address"],
                "length_words": old["length_registers"],
                "vendor": {
                    "variable_names": vendor_aliases,
                    "description": old.get("description"),
                    "datatype_notation": old.get("encoding"),
                    "unit_notation": old.get("unit"),
                    "access": old.get("access"),
                    "applicability": old.get("model_applicability", []),
                },
                "normalized": normalized,
                "semantic_identity": semantic,
                "instance": identity,
                "enums": normalized_enums(old),
                "bitfields": bitfields(old),
                "packed_fields": (
                    {
                        "status": "incomplete",
                        "source_description": old.get("encoding"),
                        "components": [
                            item
                            for item in ("hour", "minute", "priority", "enable")
                            if item in str(old.get("encoding", "")).lower()
                        ],
                    }
                    if "packed" in str(old.get("encoding", "")).lower()
                    else None
                ),
                "relationships": [],
                "resolution": resolution_from_evidence(old, evidence_items),
                "normalization": {
                    "status": "normalized" if semantic["quantity"] else "unresolved",
                    "reason": None
                    if semantic["quantity"]
                    else "No stable non-placeholder semantic identity was supportable from the retained corpus.",
                },
                "evidence": evidence_items,
                "source_provenance": old.get("provenance", []),
                "source_aliases": old.get("source_aliases", {}),
                "validation_evidence": old.get("validation_evidence", []),
                "write_policy": write_policy(old),
                "native_read_blocks": [],
            }
        )

    by_relation: defaultdict[tuple[Any, ...], list[dict[str, Any]]] = defaultdict(list)
    for record in records:
        identity = record["semantic_identity"]
        if identity["quantity"] and identity["instance_kind"] != "bms":
            by_relation[
                (
                    record["family"],
                    identity["quantity"],
                    identity["subsystem"],
                    identity["instance_kind"],
                    identity["instance"],
                )
            ].append(record)
    for group in by_relation.values():
        preferred = next(
            (r for r in group if r["resolution"]["status"] == "resolved"), group[0]
        )
        for record in group:
            if len(group) == 1:
                continue
            if record is preferred:
                role = "preferred"
            elif record["resolution"]["status"] == "source_only":
                role = "legacy_or_supported"
            else:
                role = "alternate"
            record["semantic_identity"]["relationship_role"] = role
            record["relationships"] = [
                {"type": "alternate", "target": other["physical_id"]}
                for other in group
                if other is not record
            ]
    for record in records:
        record["native_read_blocks"] = [
            page["id"]
            for page in block["validated_ranges"]
            if page["family"] == record["family"]
            and page["table"] == record["table"]
            and page["start"] <= record["address"] <= page["end"]
            and record["address"] + record["length_words"] - 1 <= page["end"]
        ]
        if record["family"] == "min_tl_xh" and record["address"] == 3170:
            record["resolution"] = {
                "status": "resolved_with_notes",
                "confidence": "medium",
                "note": "Signed int16 is implementation-correlated and physically read, but the retained live samples do not contain a negative I3170 raw value; do not treat HA signed=True as proof.",
            }
            record["evidence"] = [
                item
                for item in record["evidence"]
                if item["level"] != "semantic_verified"
            ]
        if (
            record["family"] == "min_tl_xh"
            and record["table"] == "input"
            and record["address"] == 3217
        ):
            record["semantic_identity"]["subsystem"] = "bms"
            record["semantic_identity"]["measurement_point"] = "bms"
            record["semantic_identity"]["relationship_role"] = "supported"
            record["relationships"] = []

    records.sort(key=lambda item: (item["family"], item["table"], item["address"]))
    families = []
    for family in source["families"]:
        family_records = [r for r in records if r["family"] == family["id"]]
        families.append(
            {
                "id": family["id"],
                "name": family["name"],
                "slug": FAMILY_SLUGS.get(family["id"], slug(family["id"]).upper()),
                "protocol_group": family["protocol_group"],
                "aliases": family.get("aliases", []),
                "models": family.get("models", []),
                "notes": family.get("notes", ""),
                "record_count": len(family_records),
                "live_hardware_observed": family["id"] == "min_tl_xh",
            }
        )
    semantic_index: dict[str, list[str]] = defaultdict(list)
    for record in records:
        if record["semantic_identity"]["quantity"]:
            semantic_index[record["semantic_identity"]["quantity"]].append(
                record["physical_id"]
            )
    return {
        "specification": {
            "name": "Growatt Register Specification",
            "version": "1.0",
            "identity": "family + table + address",
            "canonical_truth": True,
            "compatibility_input": "doc/growatt_register_reference.json",
            "scope": "Project-independent Growatt register and protocol knowledge product.",
        },
        "evidence_vocabulary": {
            level: {"description": EVIDENCE_DESCRIPTIONS[level]}
            for level in EVIDENCE_LEVELS
        },
        "source_catalog": {
            **source["meta"]["source_files"],
            "protocol_v314": {
                "label": "Growatt V3.14/3.15 protocol constraints",
                "kind": "primary_source_claim",
                "path": "Growatt-PV-Inverter-Modbus-RS485-RTU-Protocol-V3-14.pdf",
                "independent": True,
            },
        },
        "families": families,
        "protocols": {
            "120_v124": {
                "minimum_cmd_period_ms": 850,
                "recommended_cmd_period_ms": 1000,
                "maximum_read_words": 125,
                "maximum_write_words": 125,
                "native_read_blocks": source["read_plans"]["vendor_declared_blocks"],
                "source": "vendor_v124",
            },
            "legacy_315": {
                "minimum_cmd_period_ms": 850,
                "recommended_cmd_period_ms": 1000,
                "maximum_read_words": 45,
                "maximum_write_words": 45,
                "boundary_rules": "Vendor V3.14/3.15 grouping restrictions apply.",
                "source": "protocol_v314",
            },
        },
        "registers": records,
        "logical_fields": logical_fields(records),
        "semantic_index": dict(sorted(semantic_index.items())),
        "native_read_evidence": {
            "source": "min_block_validation",
            "capture": {
                key: block["meta"].get(key)
                for key in (
                    "model",
                    "endpoint",
                    "unit",
                    "captured_at",
                    "capture_artifact",
                    "capture_sha256",
                    "analysis",
                )
                if key in block["meta"]
            },
            "pages": native_blocks(block),
            "semantic_claim_policy": "Native-page readability contributes read_observed only; it does not promote every contained register to semantic_verified.",
        },
        "derived_views": {
            "ha_runtime_audit": runtime_audit_projection(source),
            "ha_read_plans": source["read_plans"]["profiles"],
        },
        "coverage": {
            "physical_registers": len(records),
            "holding_registers": sum(r["table"] == "holding" for r in records),
            "input_registers": sum(r["table"] == "input" for r in records),
            "meaningful_vendor_defined": sum(
                bool(r["vendor"]["variable_names"] or r["vendor"]["description"])
                for r in records
            ),
            "unknown_or_reserved": sum(
                r["resolution"]["status"] == "unknown_reserved" for r in records
            ),
            "semantic_concepts": len(semantic_index),
            "normalized_records": sum(
                bool(r["semantic_identity"]["quantity"]) for r in records
            ),
            "normalized_percentage": round(
                100
                * sum(bool(r["semantic_identity"]["quantity"]) for r in records)
                / len(records),
                2,
            ),
            "logical_multi_register_fields": len(logical_fields(records)),
            "indexed_structures": sum(
                bool(r["semantic_identity"].get("index_kind")) for r in records
            ),
            "enum_bearing_records": sum(bool(r["enums"]) for r in records),
            "bitfield_bearing_records": sum(bool(r["bitfields"]) for r in records),
            "defined_bitfield_ranges": sum(len(r["bitfields"]) for r in records),
        },
    }


def markdown_record(record: dict[str, Any]) -> str:
    normalized = record["normalized"]
    status = record["resolution"]["status"]
    return (
        f"| {record['table'][0].upper()} | {record['address']} | "
        f"{record['vendor']['description'] or normalized['name']} | {normalized['raw_type']} | "
        f"{normalized['unit'] or '—'} | {normalized['access']} | {status} |"
    )


def render_family(spec: dict[str, Any], family: dict[str, Any]) -> str:
    records = [r for r in spec["registers"] if r["family"] == family["id"]]
    lines = [
        f"# {family['name']}",
        "",
        family["notes"],
        "",
        "| T | Addr | Name | Type | Unit | Access | Status |",
        "|---|---:|---|---|---|---|---|",
    ]
    lines.extend(markdown_record(record) for record in records)
    interesting = [
        r
        for r in records
        if r["enums"]
        or r["bitfields"]
        or r["relationships"]
        or r["write_policy"] != "read_only"
        or r["length_words"] > 1
    ]
    if interesting:
        lines.extend(["", "## Details", ""])
        for record in interesting:
            identity = record["semantic_identity"]
            lines.extend(
                [
                    f"### {record['table']} {record['address']} — {record['normalized']['name']}",
                    "",
                    f"Semantic: `{identity['quantity'] or 'unknown'}`; subsystem: `{identity['subsystem']}`; measurement point: `{identity['measurement_point']}`.",
                    f"Vendor names: {', '.join(record['vendor']['variable_names']) or '—'}; evidence: {', '.join(item['level'] for item in record['evidence']) or 'none'}.",
                    f"Write policy: `{record['write_policy']}`; native blocks: {', '.join(record['native_read_blocks']) or 'none'}.",
                    "",
                ]
            )
            if record["enums"]:
                lines.append(
                    "Enums: "
                    + "; ".join(
                        f"{item['value']}={item['canonical_name']} ({item['vendor_label']})"
                        for item in record["enums"]
                    )
                )
            if record["bitfields"]:
                lines.append(
                    "Bitfields: "
                    + "; ".join(
                        f"{item['bits']}={item['name']}" for item in record["bitfields"]
                    )
                )
            lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def render_semantic_index(spec: dict[str, Any]) -> str:
    lines = [
        "# Semantic index",
        "",
        "This index preserves subsystem and instance distinctions; entries are not automatically interchangeable.",
        "",
    ]
    for key, ids in spec["semantic_index"].items():
        lines.extend([f"## `{key}`", ""])
        for physical_id in ids:
            record = next(
                item for item in spec["registers"] if item["physical_id"] == physical_id
            )
            identity = record["semantic_identity"]
            role = identity.get("relationship_role", "supported")
            lines.append(
                f"- `{record['family']}` {record['table']} {record['address']} — {identity['subsystem']} / {identity['measurement_point']} — `{role}`"
            )
        lines.append("")
    return "\n".join(lines)


def render_readme(spec: dict[str, Any]) -> str:
    coverage = spec["coverage"]
    return f"""# Growatt Register Specification v1

This is the project-independent canonical Growatt register/protocol knowledge
product. It is intended for Home Assistant, Grott-like tools, gateways,
ESP/MQTT projects and diagnostic software. Home Assistant is one consumer and
one corroborating implementation, not the source of truth.

The machine-readable canonical artifact is [`growatt-register-spec.json`](growatt-register-spec.json), validated by [`growatt-register-spec.schema.json`](growatt-register-spec.schema.json). It is generated by `build_register_spec.py` from the retained resolved/source corpus. The former `doc/growatt_register_reference.json` is a compatibility input/view during migration, not a second maintained semantic truth.

## Model

Physical identity is always `family + table + address`; holding and input
registers never merge. Records retain vendor wording and aliases alongside
normalized decoding, semantic quantity, subsystem, measurement point,
instance status, relationships, provenance, evidence and write policy.

Repeated BMS fields are represented as a structural BMS group with unknown
instance unless evidence proves an index. Diagnostic suffixes do not create
false BMS instances. Native page reads establish `read_observed`, not
`semantic_verified`.

Coverage: **{coverage["physical_registers"]}** physical records, **{coverage["holding_registers"]}** holding, **{coverage["input_registers"]}** input, **{coverage["normalized_percentage"]}%** normalized semantic coverage, **{coverage["logical_multi_register_fields"]}** logical multi-word fields, **{coverage["enum_bearing_records"]}** enum-bearing records and **{coverage["bitfield_bearing_records"]}** structured bitfield records.

See [`SEMANTIC_INDEX.md`](SEMANTIC_INDEX.md), [`PROTOCOLS.md`](PROTOCOLS.md),
the generated family pages, and [`CLEANUP_MANIFEST.md`](CLEANUP_MANIFEST.md).
"""


def render_protocols(spec: dict[str, Any]) -> str:
    return """# Protocol and native read blocks

## V1.24 / modern 120-family

- minimum command period: 850 ms
- recommended period: 1000 ms
- maximum read/write: 125 words
- native pages and family applicability are in the machine-readable `protocols.120_v124` object.

## V3.14 / 3.15 family

- minimum command period: 850 ms
- recommended period: 1000 ms
- maximum read/write: 45 words
- vendor grouping/boundary restrictions remain family-specific.

The five MIN/TL-XH pages in `native_read_evidence` are bounded live hardware
readability evidence. They are not a Home Assistant polling prescription and
do not promote every returned register to a verified semantic interpretation.
"""


def main() -> None:
    spec = build()
    OUTPUT_PATH.write_text(
        json.dumps(spec, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )
    (SPEC_DIR / "README.md").write_text(render_readme(spec), encoding="utf-8")
    (SPEC_DIR / "SEMANTIC_INDEX.md").write_text(
        render_semantic_index(spec), encoding="utf-8"
    )
    (SPEC_DIR / "PROTOCOLS.md").write_text(render_protocols(spec), encoding="utf-8")
    for family in spec["families"]:
        (SPEC_DIR / "families" / f"{family['slug']}.md").write_text(
            render_family(spec, family), encoding="utf-8"
        )
    print(f"wrote {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
