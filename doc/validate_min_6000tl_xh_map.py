#!/usr/bin/env python3
"""Validate the focused MIN 6000TL-XH map and its captured read-only evidence."""

from __future__ import annotations

import json
from pathlib import Path


DOC_DIR = Path(__file__).resolve().parent
MAP_PATH = DOC_DIR / "min_6000tl_xh_register_map.json"
VALIDATION_PATH = DOC_DIR / "min_6000tl_xh_live_validation.json"


def main() -> None:
    register_map = json.loads(MAP_PATH.read_text(encoding="utf-8"))
    validation = json.loads(VALIDATION_PATH.read_text(encoding="utf-8"))

    holding = {entry["register"]: entry for entry in register_map["holding"]}
    input_registers = {entry["register"]: entry for entry in register_map["input"]}

    assert {0, 23, 43, 44, 88, 3036, 3037, 3047, 3048, 3049, 3081, 3082} <= holding.keys()
    assert {3000, 3001, 3041, 3043, 3045, 3047, 3049, 3081, 3169, 3171, 3178, 3180, 3215} <= input_registers.keys()
    assert holding[3081]["name"] == "UPS/EPS frequency selection"
    assert input_registers[3081]["name"] == "PV4 energy total"
    assert validation["meta"]["access"] == "FC03/FC04 only; no writes issued"
    assert validation["identity"]["fc03_43_count2_registers"] == [5100, 513]
    assert validation["holding_ems"]["fc03_3081_count2_registers"] == [0, 0]

    print(
        f"validated {len(holding)} holding and {len(input_registers)} input entries; "
        "table-specific 3081 conflict is resolved"
    )


if __name__ == "__main__":
    main()
