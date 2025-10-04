#!/usr/bin/env python3
"""Convert growatt_registers_best_guess.json into the canonical register data schema."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional, Tuple

DOC_DIR = Path(__file__).resolve().parent
SPEC_PATH = DOC_DIR / "growatt_registers_best_guess.json"
OUTPUT_PATH = DOC_DIR / "growatt_registers_best_guess.v2.json"


@dataclass
class SpecEntry:
    table: str
    section: str
    register: int
    register_end: int
    payload: Dict[str, Any]


def slugify(value: str, default: str = "section") -> str:
    value = re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")
    return value or default


def sha256sum(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(65536), b""):
            digest.update(chunk)
    return digest.hexdigest()


def parse_range(value: Optional[str]) -> Optional[Dict[str, Any]]:
    if not value:
        return None
    text = value.strip()
    match = re.fullmatch(r"(-?\d+(?:\.\d+)?)\s*-\s*(-?\d+(?:\.\d+)?)", text)
    if not match:
        return None
    def convert(token: str) -> Any:
        return float(token) if "." in token else int(token)
    return {"min": convert(match.group(1)), "max": convert(match.group(2))}


def detect_encoding(description: Optional[str], unit: Optional[str]) -> str:
    text = (description or "").lower()
    if any(token in text for token in ("ascii", "string", "serial")):
        return "ascii"
    if "bitfield" in text or "bit field" in text or "bit mask" in text:
        return "bitfield"
    if unit and unit.lower() in {"text", "string"}:
        return "ascii"
    return "numeric"


def build_canonical_id(table: str, start: int, end: int) -> str:
    if start == end:
        return f"canonical:{table}:{start}"
    return f"canonical:{table}:{start}-{end}"


def collect_entries(raw: Dict[str, Any]) -> Dict[str, List[SpecEntry]]:
    tables: Dict[str, List[SpecEntry]] = {}
    for table in ("holding", "input"):
        entries: List[SpecEntry] = []
        current_sections: Dict[str, Dict[str, Any]] = {}
        for item in raw.get(table, []):
            if item.get("type") == "section":
                title = item.get("title") or "Unnamed section"
                current_sections[title] = item
                continue
            if item.get("type") != "entry":
                continue
            section = item.get("section") or "Unnamed section"
            entry = SpecEntry(
                table=table,
                section=section,
                register=int(item.get("register_start", item.get("register", 0))),
                register_end=int(item.get("register_end", item.get("register", 0))),
                payload=item,
            )
            entries.append(entry)
        entries.sort(key=lambda e: (e.register, e.register_end))
        tables[table] = entries
    return tables


def group_by_section(entries: Iterable[SpecEntry]) -> Dict[str, List[SpecEntry]]:
    sections: Dict[str, List[SpecEntry]] = {}
    for entry in entries:
        sections.setdefault(entry.section, []).append(entry)
    for bucket in sections.values():
        bucket.sort(key=lambda e: (e.register, e.register_end))
    return sections


def build_register_value(entry: SpecEntry) -> Tuple[str, Dict[str, Any]]:
    payload = entry.payload
    start = entry.register
    end = entry.register_end
    length = end - start + 1
    canonical_id = build_canonical_id(entry.table, start, end)

    description = payload.get("description")
    unit = payload.get("unit")
    encoding = detect_encoding(description, unit)
    value_range = parse_range(payload.get("range"))

    annotations = []
    attributes = payload.get("attributes")
    if isinstance(attributes, list):
        annotations = [str(item) for item in attributes]

    register_value: Dict[str, Any] = {
        "id": canonical_id,
        "label": payload.get("name") or canonical_id,
        "description": description,
        "register": start,
        "length": length,
        "reg_type": entry.table,
        "unit": unit,
        "writable": bool(payload.get("access") and "W" in str(payload["access"]).upper()),
        "scale": None,
        "value_encoding": encoding,
        "enum_values": [],
        "bitfields": [],
        "decoder": None,
        "value_range": value_range,
        "metadata": {
            "source": "growatt_registers_best_guess",
            "access": payload.get("access"),
            "initial": payload.get("initial"),
            "range": payload.get("range"),
            "note": payload.get("note"),
            "section": entry.section,
        },
        "tooltip": payload.get("note"),
        "help": None,
        "annotations": annotations,
        "siblings": [],
    }

    return canonical_id, register_value


def build_sections(
    table: str,
    entries: List[SpecEntry],
    register_values: Dict[str, Dict[str, Any]],
    canonical_ids: List[str],
) -> Tuple[List[Dict[str, Any]], Dict[str, Dict[str, Any]]]:
    sections: List[Dict[str, Any]] = []
    section_index: Dict[str, Dict[str, Any]] = {}

    for title, bucket in group_by_section(entries).items():
        start = min(item.register for item in bucket)
        end = max(item.register_end for item in bucket)
        section_id = f"section:{table}:{start}-{end}:{slugify(title)}"
        canonical_mappings = []
        value_ids: List[str] = []
        for entry in bucket:
            cid, value = build_register_value(entry)
            if cid not in register_values:
                register_values[cid] = value
                canonical_ids.append(cid)
            value_ids.append(cid)
            canonical_mappings.append(
                {
                    "canonical_register": cid,
                    "instance_register": entry.register,
                    "offset": entry.register - start,
                }
            )
        section = {
            "id": section_id,
            "block": None,  # to be filled by caller
            "label": title,
            "description": None,
            "kind": "vendor",
            "index": None,
            "register": start,
            "length": end - start + 1,
            "canonical_mappings": canonical_mappings,
            "register_values": value_ids,
            "children": [],
            "metadata": {
                "source": "growatt_registers_best_guess",
            },
        }
        sections.append(section)
        section_index[section_id] = section

    sections.sort(key=lambda item: (item["register"], item["length"]))
    return sections, section_index


def build_blocks(
    tables: Dict[str, List[SpecEntry]],
    register_values: Dict[str, Dict[str, Any]],
    canonical_ids: List[str],
    sections_store: Dict[str, Dict[str, Any]],
) -> Dict[str, Dict[str, Any]]:
    blocks: Dict[str, Dict[str, Any]] = {}
    for table, entries in tables.items():
        if not entries:
            continue
        start = min(item.register for item in entries)
        end = max(item.register_end for item in entries)
        block_id = f"block:{table}:{start}-{end}"

        block_sections, section_index = build_sections(table, entries, register_values, canonical_ids)
        for section in block_sections:
            section["block"] = block_id
            sections_store[section["id"]] = section

        block = {
            "reg_type": table,
            "register": start,
            "length": end - start + 1,
            "description": f"Vendor {table} registers {start}-{end}",
            "supported_families": ["vendor_best_guess"],
            "sections": block_sections,
            "metadata": {"source": "growatt_registers_best_guess"},
        }
        blocks[block_id] = block

    return blocks


def build_document(raw: Dict[str, Any]) -> Dict[str, Any]:
    tables = collect_entries(raw)
    register_values: Dict[str, Dict[str, Any]] = {}
    sections_store: Dict[str, Dict[str, Any]] = {}
    canonical_ids: List[str] = []

    blocks = build_blocks(tables, register_values, canonical_ids, sections_store)

    document: Dict[str, Any] = {
        "meta": {
            "version": "0.1.0",
            "generated_at": datetime.now(timezone.utc).isoformat(),
            "generator": Path(__file__).name,
            "source_files": {
                "growatt_registers_best_guess": {
                    "path": str(SPEC_PATH.relative_to(DOC_DIR)),
                    "sha256": sha256sum(SPEC_PATH),
                }
            },
        },
        "inverter_families": {
            "vendor_best_guess": {
                "description": "Vendor RTU protocol v1.24",
                "aliases": ["vendor"],
                "blocks": sorted(blocks.keys()),
                "metadata": {
                    "source": "growatt_registers_best_guess",
                },
            }
        },
        "blocks": blocks,
        "sections": sections_store,
        "register_values": register_values,
        "canonical_register_values": sorted(canonical_ids),
    }

    return document


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--output",
        type=Path,
        default=OUTPUT_PATH,
        help=f"Destination file (default: {OUTPUT_PATH.name})",
    )
    args = parser.parse_args()

    raw = json.loads(SPEC_PATH.read_text(encoding="utf-8"))
    document = build_document(raw)

    output_path = args.output
    if not output_path.is_absolute():
        output_path = DOC_DIR / output_path
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(json.dumps(document, indent=2), encoding="utf-8")
    print(f"Wrote {output_path.relative_to(DOC_DIR)}")


if __name__ == "__main__":
    main()
