#!/usr/bin/env python3
"""Convert growatt_registers_best_guess.json into the canonical register data schema."""

from __future__ import annotations

import argparse
import hashlib
import json
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
import re
from typing import Any, Dict, List, Optional, Tuple

DOC_DIR = Path(__file__).resolve().parent
SPEC_PATH = DOC_DIR / "growatt_registers_best_guess.json"
OUTPUT_PATH = DOC_DIR / "growatt_registers_best_guess.v2.json"
CATALOG_PATH = DOC_DIR / "register_catalog.json"


@dataclass
class SpecEntry:
    table: str
    section: str
    register: int
    register_end: int
    payload: Dict[str, Any]

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


def build_register_value(entry: SpecEntry, block_id: str) -> Tuple[str, Dict[str, Any]]:
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
            "block": block_id,
        },
        "tooltip": payload.get("note"),
        "help": None,
        "annotations": annotations,
        "siblings": [],
    }

    return canonical_id, register_value


def find_block_for_entry(entry: SpecEntry, catalog_blocks: Dict[str, Dict[str, Any]]) -> Optional[str]:
    for block_id, block in catalog_blocks.items():
        if block.get("reg_type") != entry.table:
            continue
        start = block["register"]
        end = start + block["length"] - 1
        if start <= entry.register and entry.register_end <= end:
            return block_id
    return None


def normalize_label(label: Optional[str]) -> str:
    text = (label or "").strip().lower()
    text = re.sub(r"\s*\(.*?\)\s*$", "", text)
    return text


def compare_sections(
    block_id: str,
    catalog_block: Dict[str, Any],
    discovered_sections: Dict[str, Dict[str, int]],
) -> None:
    catalog_sections = catalog_block.get("sections", [])

    catalog_by_label: Dict[str, List[Tuple[str, int, int]]] = {}
    for sec in catalog_sections:
        label = sec.get("label")
        start = sec.get("register")
        length = sec.get("length")
        if start is None or length is None:
            continue
        catalog_by_label.setdefault(normalize_label(label), []).append((label, start, start + length - 1))

    discovered_by_label: Dict[str, List[Tuple[str, int, int]]] = {}
    for label, info in discovered_sections.items():
        start = info["start"]
        end = info["end"]
        discovered_by_label.setdefault(normalize_label(label), []).append((label, start, end))

    matched_catalog: Dict[Tuple[str, int, int], bool] = {}

    for norm_label, entries in discovered_by_label.items():
        catalog_entries = catalog_by_label.get(norm_label)
        if not catalog_entries:
            for label, start, end in entries:
                print(
                    f"[WARN] Block {block_id}: section not in catalog -> {label} ({start}-{end})"
                )
            continue

        # attempt to match each discovered entry to a catalog entry
        remaining_catalog = [item for item in catalog_entries if not matched_catalog.get(item)]
        for label, start, end in entries:
            match = None
            for candidate in remaining_catalog:
                cat_label, cat_start, cat_end = candidate
                if cat_start <= start <= cat_end:
                    match = candidate
                    break
            if match is None:
                print(
                    f"[WARN] Block {block_id}: no catalog match for {label} ({start}-{end})"
                )
                continue

            remaining_catalog.remove(match)
            matched_catalog[match] = True
            cat_label, cat_start, cat_end = match
            if start < cat_start or end > cat_end:
                print(
                    f"[WARN] Block {block_id}: discovered range {label} ({start}-{end}) extends beyond catalog {cat_label} ({cat_start}-{cat_end})"
                )
            elif start > cat_start or end < cat_end:
                print(
                    f"[INFO] Block {block_id}: partial coverage for {cat_label} -> best guess {start}-{end} within {cat_start}-{cat_end}"
                )

    for norm_label, catalog_entries in catalog_by_label.items():
        for entry in catalog_entries:
            if not matched_catalog.get(entry):
                label, start, end = entry
                print(
                    f"[WARN] Block {block_id}: catalog section without best-guess coverage -> {label} ({start}-{end})"
                )


def build_document(raw: Dict[str, Any], catalog: Dict[str, Any]) -> Dict[str, Any]:
    catalog_blocks: Dict[str, Dict[str, Any]] = catalog.get("blocks", {})
    tables = collect_entries(raw)

    register_values: Dict[str, Dict[str, Any]] = {}
    canonical_ids: List[str] = []
    block_usage: Dict[str, Dict[str, Any]] = {}

    unmatched_entries: List[SpecEntry] = []

    for table, entries in tables.items():
        for entry in entries:
            block_id = find_block_for_entry(entry, catalog_blocks)
            if not block_id:
                unmatched_entries.append(entry)
                continue

            usage = block_usage.setdefault(block_id, {"sections": {}, "entries": []})
            usage["entries"].append(entry)
            section_label = entry.section.strip() if entry.section else "Unnamed section"
            section_info = usage["sections"].setdefault(
                section_label, {"start": entry.register, "end": entry.register_end}
            )
            section_info["start"] = min(section_info["start"], entry.register)
            section_info["end"] = max(section_info["end"], entry.register_end)

            cid, value = build_register_value(entry, block_id)
            if cid not in register_values:
                register_values[cid] = value
                canonical_ids.append(cid)

    if unmatched_entries:
        print("[WARN] Entries without matching catalog block:")
        for entry in unmatched_entries[:20]:
            print(
                f"  - {entry.table} register {entry.register}-{entry.register_end} section '{entry.section}'"
            )
        if len(unmatched_entries) > 20:
            print(f"  ... and {len(unmatched_entries) - 20} more")

    blocks: Dict[str, Dict[str, Any]] = {}
    for block_id in sorted(block_usage.keys()):
        catalog_block = catalog_blocks.get(block_id)
        if not catalog_block:
            print(f"[WARN] Block id {block_id} referenced by best guess but missing in catalog")
            continue

        compare_sections(block_id, catalog_block, block_usage[block_id]["sections"])

        block_entry = {
            "label": catalog_block.get("label"),
            "reg_type": catalog_block.get("reg_type"),
            "register": catalog_block.get("register"),
            "length": catalog_block.get("length"),
            "description": catalog_block.get("description"),
            "sections": catalog_block.get("sections", []),
            "metadata": {"source": "register_catalog"},
        }
        blocks[block_id] = block_entry

    holding_blocks = [bid for bid, block in blocks.items() if block.get("reg_type") == "holding"]
    input_blocks = [bid for bid, block in blocks.items() if block.get("reg_type") == "input"]

    catalog_meta = catalog.get("meta", {})

    document: Dict[str, Any] = {
        "meta": {
            "version": "0.1.0",
            "generated_at": datetime.now(timezone.utc).isoformat(),
            "generator": Path(__file__).name,
            "source_files": {
                "growatt_registers_best_guess": {
                    "path": str(SPEC_PATH.relative_to(DOC_DIR)),
                    "sha256": sha256sum(SPEC_PATH),
                },
                "register_catalog": {
                    "path": str(CATALOG_PATH.relative_to(DOC_DIR)),
                    "sha256": sha256sum(CATALOG_PATH),
                },
            },
        },
        "catalog": {
            "version": catalog_meta.get("version"),
            "path": str(CATALOG_PATH.relative_to(DOC_DIR)),
            "sha256": sha256sum(CATALOG_PATH),
        },
        "inverter_families": {
            "vendor_best_guess": {
                "label": "Vendor best guess",
                "description": "Curated interpretation derived from growatt_registers_best_guess.json",
                "aliases": ["vendor"],
                "holding_blocks": sorted(holding_blocks),
                "input_blocks": sorted(input_blocks),
                "notes": "Sections and ranges aligned with register_catalog.json",
            }
        },
        "blocks": blocks,
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
    catalog = json.loads(CATALOG_PATH.read_text(encoding="utf-8"))
    document = build_document(raw, catalog)

    output_path = args.output
    if not output_path.is_absolute():
        output_path = DOC_DIR / output_path
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(json.dumps(document, indent=2), encoding="utf-8")
    print(f"Wrote {output_path.relative_to(DOC_DIR)}")


if __name__ == "__main__":
    main()
