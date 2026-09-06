# HA-7A MIN/TL-XH runtime mapping audit

This report records the evidence-gated review of the `MIN 6000TL-XH` runtime
against research commit `a3a75e2068a14026f1fd558035c47f2c6deb75da`. It is a
runtime handoff document, not a copy of the canonical register specification.

The MIN projection checked 253 runtime mapping occurrences and 185 unique
family/table/address mappings. It contains 22 finding occurrences and 15
unique findings keyed by `(family, table, address, issue kind)`. Duplicate
`tlx` and `storage` consumer occurrences are counted once in the decision
table below.

## Decision summary

| Decision | Unique findings | Addresses |
|---|---:|---|
| `FIX_NOW` | 0 | — |
| `KEEP_RUNTIME_FOR_NOW` | 1 | I3170 |
| `NEEDS_TARGETED_VALIDATION` | 4 | I3191, I3194, I3195, I3224 |
| `CANONICAL_OR_AUDIT_ISSUE` | 10 | I3001, I3005, I3009, I3023, I3028, I3047, I3049, I3101, I3230, I3231 |

No runtime mapping is changed by HA-7A. The existing mapping is already
consistent with the strongest retained evidence for the EMS-critical fields;
the remaining uncertainty is explicitly carried forward.

## Unique MIN findings

| Address | Runtime name | Issue | Runtime interpretation | Canonical interpretation | Vendor evidence | Implementation evidence | Live evidence | Semantic status | Decision / reason |
|---:|---|---|---|---|---|---|---|---|---|
| I3001 | `input_power` | signedness | 32-bit `/10`, current decoder uses signed int32 | unsigned 32-bit `/10 W` | `PpvH`, `0.1W`; PV power is non-negative | Grott/OpenInverter agree | observed positive PV values, 571/703 W | reconciled; resolved with notes | `CANONICAL_OR_AUDIT_ISSUE`: generic two-word decoder behavior is being compared with unsigned physical metadata; no reachable MIN 6 kW high-bit case is evidenced |
| I3005 | `input_1_power` | signedness | 32-bit `/10`, current decoder uses signed int32 | unsigned 32-bit `/10 W` | `Ppv1H`, `0.1W` | Grott/OpenInverter agree | observed positive PV1 values, 199/313 W | syntactic-only; resolved with notes | `CANONICAL_OR_AUDIT_ISSUE`: same bounded physical-power issue as I3001 |
| I3009 | `input_2_power` | signedness | 32-bit `/10`, current decoder uses signed int32 | unsigned 32-bit `/10 W` | `Ppv2H`, `0.1W` | Grott/OpenInverter agree | observed positive PV2 values, 372/390 W | syntactic-only; resolved with notes | `CANONICAL_OR_AUDIT_ISSUE`: same bounded physical-power issue as I3001 |
| I3023 | `output_power` | signedness | 32-bit `/10`, current decoder uses signed int32 | unsigned 32-bit `/10 W` | `PacH`, `0.1W` | Grott/OpenInverter agree | observed positive AC output, 528.6 W | syntactic-only; resolved with notes | `CANONICAL_OR_AUDIT_ISSUE`: same bounded physical-power issue as I3001 |
| I3028 | `output_1_power` | signedness | 32-bit `/10`, current decoder uses signed int32 | unsigned 32-bit `/10 VA` | `Pac1H`, `0.1VA` | Grott/OpenInverter agree | no contradictory raw value | syntactic-only; resolved with notes | `CANONICAL_OR_AUDIT_ISSUE`: phase output is non-negative and the generic decoder projection is too coarse |
| I3047 | `operation_hours` | signedness | 32-bit `/7200`, current decoder uses signed int32 | unsigned 32-bit runtime counter `/7200 h` | `TimetotalH`, `0.5s` | Grott/OpenInverter agree | no high-bit counter sample | reconciled; resolved with notes | `CANONICAL_OR_AUDIT_ISSUE`: runtime counter is non-negative; no production-scale high-bit case is evidenced |
| I3049 | `output_energy_today` | signedness | 32-bit `/10`, current decoder uses signed int32 | unsigned 32-bit `/10 kWh` | `EactodayH`, `0.1kWh` | Grott/OpenInverter agree | no contradictory raw value | syntactic-only; resolved with notes | `CANONICAL_OR_AUDIT_ISSUE`: energy counter is non-negative; no production-scale high-bit case is evidenced |
| I3101 | `real_output_power_percent` | signedness | unsigned 16-bit integer | signed in canonical projection | `RealOPPercent`, `1%`, range `1–100` | Grott/OpenInverter agree | no contradictory raw value | syntactic-only; resolved with notes | `CANONICAL_OR_AUDIT_ISSUE`: vendor range proves a non-negative percentage; runtime is the safer interpretation |
| I3170 | `battery_current` | signedness | unsigned 16-bit `/10 A` | signed `/10 A` | `Ibat`, `0.1A`; direction is not stated | Grott/OpenInverter list the field but do not prove polarity | live raw values `22` and `115` only; both positive | reconciled; resolved with notes | `KEEP_RUNTIME_FOR_NOW`: a negative I3170 sample is not retained. Do not infer it from I3217 |
| I3191 | `bms_avg_temp_a` | scale | `/10 °C` | `/1` | vendor row is malformed and omits a unit at 3191; neighbouring rows use `0.1°C` | Grott names the field but no decisive scale | retained raw value `0`; insufficient to distinguish | syntactic-only; resolved with notes | `NEEDS_TARGETED_VALIDATION`: exact BMS temperature encoding remains ambiguous |
| I3194 | `bms_max_cell_temp_b` | scale | `/10 °C` | `/1` | vendor row omits a unit at 3194; same BMS temperature block uses `0.1°C` | Grott names the field but no decisive scale | retained raw value `2`; insufficient alone | syntactic-only; resolved with notes | `NEEDS_TARGETED_VALIDATION`: exact BMS temperature encoding remains ambiguous |
| I3195 | `bms_avg_temp_c` | scale | `/10 °C` | `/1` | vendor row omits a unit at 3195; same BMS temperature block uses `0.1°C` | Grott names the field but no decisive scale | retained raw value `14`; insufficient alone | syntactic-only; resolved with notes | `NEEDS_TARGETED_VALIDATION`: exact BMS temperature encoding remains ambiguous |
| I3224 | `bms_discharge_volt_limit` | scale | `/100 V` | `/1` | row omits scale; adjacent charge limit I3223 explicitly says `0.01V` | Grott names the field but no decisive scale | retained raw value `18880`, which is plausible as `188.80 V` with `/100` | syntactic-only; resolved with notes | `NEEDS_TARGETED_VALIDATION`: vendor row needs a direct confirming read/reference; do not replace a plausible runtime value with `/1` |
| I3230 | `bms_cell_volt_max` | scale | `/1000 V` | `/1` | explicit `0.001V` | Grott and vendor agree | raw `3314` decodes to `3.314 V` | syntactic-only; resolved with notes | `CANONICAL_OR_AUDIT_ISSUE`: canonical scale is contradicted directly by vendor and live evidence; runtime must remain `/1000` |
| I3231 | `bms_cell_volt_min` | scale | `/1000 V` | `/1` | explicit `0.001V` | Grott and vendor agree | raw `3311` decodes to `3.311 V` | syntactic-only; resolved with notes | `CANONICAL_OR_AUDIT_ISSUE`: canonical scale is contradicted directly by vendor and live evidence; runtime must remain `/1000` |

## I3170 versus I3217

These registers remain distinct:

- I3170 is the storage-device/BDC-side battery current. The retained MIN
  samples are raw `22` and `115`, or `2.2 A` and `11.5 A` using the runtime
  `/10` scale. They do not prove signedness.
- I3217 is the BMS-reported battery current. Its retained regression evidence
  uses raw `0xFEB6`, which decodes as `-3.30 A` with signed int16 and `/100`.

The HA-5 regression for I3217 is preserved. No aliasing or mapping collapse is
introduced.

## Required follow-up validation

The smallest useful follow-up is read-only and bounded to the four ambiguous
BMS fields: capture repeated I3191/I3194/I3195/I3224 values while the battery
operating point changes, retaining raw words and an independent temperature or
voltage reference. A negative I3170 sample would separately settle its
signedness. No broad scan or write is justified by this audit.

## Scope

HA-7A changes no polling ranges, no transport logic, no entity names, no
dynamic-tariff code and no inverter settings. No writes were issued. The
canonical research tree and its commit remain unchanged.
