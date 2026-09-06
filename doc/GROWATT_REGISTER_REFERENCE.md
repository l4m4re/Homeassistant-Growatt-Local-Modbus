# Growatt resolved register reference

> This file is a generated compatibility view. The canonical machine-readable and human reference is `doc/register-spec/growatt-register-spec.json` plus its Markdown views; the original vendor, runtime, external and live-evidence files remain the provenance corpus.

Reference version: `2026.09-resolved`
Records: **4048** (1805 holding, 2243 input)
Live read verified: **60**
Write verified: **0** (the current hardware evidence is read-only)

## Family overview

| Family | Holding coverage | Input coverage | Resolution quality | Live validation |
|---|---:|---:|---|---:|
| MIN / TL-XH | 415 | 480 | RESOLVED=82, RESOLVED_WITH_NOTES=288, SOURCE_ONLY=377, UNKNOWN_RESERVED=148 | 60 |
| TL3-X / MAX / MID / MAC | 250 | 399 | RESOLVED=24, RESOLVED_WITH_NOTES=92, SOURCE_ONLY=473, UNKNOWN_RESERVED=60 | 0 |
| MOD TL3-XH | 290 | 250 | RESOLVED=45, RESOLVED_WITH_NOTES=199, SOURCE_ONLY=242, UNKNOWN_RESERVED=54 | 0 |
| MIX storage | 350 | 325 | RESOLVED=61, RESOLVED_WITH_NOTES=183, SOURCE_ONLY=358, UNKNOWN_RESERVED=73 | 0 |
| SPA storage | 250 | 375 | RESOLVED=41, RESOLVED_WITH_NOTES=24, SOURCE_ONLY=380, UNKNOWN_RESERVED=180 | 0 |
| SPH storage | 250 | 375 | RESOLVED=64, RESOLVED_WITH_NOTES=106, SOURCE_ONLY=353, UNKNOWN_RESERVED=102 | 0 |
| Older inverter / 3.15 family | 0 | 12 | SOURCE_ONLY=12 | 0 |
| SPF off-grid / hybrid | 0 | 27 | SOURCE_ONLY=27 | 0 |

## How to read the reference

Identity is always **family + table + address**. Holding register 3047 and input register 3047 are therefore separate records and are not merged. `RESOLVED_WITH_NOTES` is deliberately publishable but retains source differences; `SOURCE_ONLY`, `CONFLICTED` and `UNKNOWN_RESERVED` are not hidden.

### Evidence legend

- `source_claim`: a retained source explicitly describes the register.
- `semantic_correlated`: at least two independent source classes support the interpretation.
- `read_verified`: a live read matched the interpretation; it does not mean writable.
- `write_accepted`, `write_reversible`, `behavior_verified`: no entries have these in this release.

### Provenance and lineage

The graph export, datatype catalogues and overlays are generated or curated derivatives. They are retained for audit but do not count as independent corroboration of their own upstream claims. The MIN 6000TL-XH model overlay is reconciled against the runtime mapping and the read-only live validation. In particular, BMS register 3217 is published as input-table signed int16 / 100 A; the older model-map placement under holding is retained as a table-reconciliation note.

## Semantic concepts and MIN capabilities

Physical identity remains family + table + address. `semantic_key` is the stable implementation-neutral concept identity, so multiple physical registers can intentionally represent one concept. The MIN/TL-XH legacy/base `input 1014` SOC register is retained alongside preferred `input 3171`; it is not merged with it.

| Capability | Status | Supporting registers | Write verified |
|---|---|---|---:|
| PV generation telemetry | read_verified | register:min_tl_xh:input:3001 | no |
| Grid import/export telemetry | read_verified | register:min_tl_xh:input:3041, register:min_tl_xh:input:3043 | no |
| House load telemetry | read_verified | register:min_tl_xh:input:3045 | no |
| Battery voltage/current/SOC telemetry | read_verified | register:min_tl_xh:input:3169, register:min_tl_xh:input:3170, register:min_tl_xh:input:3171, register:min_tl_xh:input:3178, register:min_tl_xh:input:3180 | no |
| BMS telemetry | read_verified | register:min_tl_xh:input:3215, register:min_tl_xh:input:3216, register:min_tl_xh:input:3217 | no |
| Dynamic-tariff charge/discharge controls | read_verified | register:min_tl_xh:holding:3049, register:min_tl_xh:holding:3047, register:min_tl_xh:holding:3048, register:min_tl_xh:holding:3036, register:min_tl_xh:holding:3037, register:min_tl_xh:holding:3082 | no |

### Family-specific block-read plans

The vendor V1.24 transport model declares an 850 ms minimum command period, recommends 1 second, and permits up to 125 words per read. The current MIN hardware evidence validates the complete native pages below twice each; the observed response durations are device evidence, not a replacement for the vendor timing rule.

Vendor transport: **850 ms minimum**, **1000 ms recommended**, **125 words maximum**.

Semantic selection and physical read planning are separate. These plans optimize Modbus transaction count first; local decoding extracts the selected registers from each returned block. Holding and input spaces always remain separate FC03/FC04 transactions.

| Profile | Transactions | Blocks |
|---|---:|---|
| MIN/TL-XH dynamic-tariff control and telemetry | 3 | FC3 3000+125; FC4 3000+125; FC4 3125+125 |
| MIN/TL-XH BMS diagnostics | 1 | FC4 3125+125 |

#### Hardware-validated native pages

These are the bounded live MIN 6000TL-XH page probes used by the planner. `additional_words_fetched` are decoded locally only; they do not become Home Assistant entities.

| Page | Class | Function | Range | Required semantics | Extra words | Repeatability |
|---|---|---:|---|---|---:|---|
| min_fc03_holding_0_124 | SLOW_IDENTITY | FC3 | 0–124 (125 words) | none listed | 125 | 2/2 complete responses |
| min_fc03_holding_3000_3124 | FAST_CONTROL | FC3 | 3000–3124 (125 words) | grid_first_discharge_rate, grid_first_stop_soc, battery_first_charge_rate, battery_first_stop_soc, ac_charge_enabled, load_first_stop_soc | 119 | 2/2 complete responses |
| min_fc04_input_3000_3124 | FAST_TELEMETRY | FC4 | 3000–3124 (125 words) | inverter_status, pv_total_power, grid_import_power, grid_export_power, house_load_power | 116 | 2/2 complete responses |
| min_fc04_input_3125_3249 | NORMAL_BATTERY_BMS | FC4 | 3125–3249 (125 words) | battery_voltage, battery_current, battery_soc, battery_discharge_power, battery_charge_power | 118 | 2/2 complete responses |
| min_fc04_input_3250_3374 | SLOW_DIAGNOSTIC | FC4 | 3250–3374 (125 words) | none listed | 125 | 2/2 complete responses |

#### Source-derived family plans

Non-MIN plans are derived from the family/protocol source corpus and are not hardware validated by the live MIN probe.

| Family plan | Transactions | Maximum words | Hardware validated |
|---|---:|---:|---:|
| TL3-X / MAX / MID / MAC core telemetry (source-derived) | 3 | 125 | no |
| MOD TL3-XH core telemetry (source-derived) | 4 | 125 | no |
| MIX storage core telemetry (source-derived) | 5 | 125 | no |
| SPA storage core telemetry (source-derived) | 2 | 125 | no |
| SPH storage core telemetry (source-derived) | 3 | 125 | no |
| Older inverter / 3.15 family core telemetry (source-derived) | 0 | 45 | no |

## Runtime consistency audit

HA runtime mappings checked: **198**; findings: **34**; status: **issues_found**.

| Family | Table | Address | Runtime name | Finding |
|---|---|---:|---|---|
| min_tl_xh | input | 3001 | input_power | signedness_mismatch |
| min_tl_xh | input | 3005 | input_1_power | signedness_mismatch |
| min_tl_xh | input | 3009 | input_2_power | signedness_mismatch |
| min_tl_xh | input | 3023 | output_power | signedness_mismatch |
| min_tl_xh | input | 3028 | output_1_power | signedness_mismatch |
| min_tl_xh | input | 3047 | operation_hours | signedness_mismatch |
| min_tl_xh | input | 3049 | output_energy_today | signedness_mismatch |
| min_tl_xh | input | 3101 | real_output_power_percent | signedness_mismatch |
| min_tl_xh | input | 3170 | battery_current | signedness_mismatch |
| min_tl_xh | input | 3191 | bms_avg_temp_a | scale_mismatch |
| min_tl_xh | input | 3194 | bms_max_cell_temp_b | scale_mismatch |
| min_tl_xh | input | 3195 | bms_avg_temp_c | scale_mismatch |
| min_tl_xh | input | 3224 | bms_discharge_volt_limit | scale_mismatch |
| min_tl_xh | input | 3230 | bms_cell_volt_max | scale_mismatch |
| min_tl_xh | input | 3231 | bms_cell_volt_min | scale_mismatch |
| storage_mix | input | 1009 | discharge_power | signedness_mismatch |
| storage_mix | input | 1011 | charge_power | signedness_mismatch |
| storage_mix | input | 1021 | pac_to_user_total | signedness_mismatch |
| storage_mix | input | 1029 | pac_to_grid_total | signedness_mismatch |
| storage_mix | input | 1044 | energy_to_user_today | signedness_mismatch |
| storage_mix | input | 1046 | energy_to_user_total | signedness_mismatch |
| storage_mix | input | 1048 | energy_to_grid_today | signedness_mismatch |
| storage_mix | input | 1050 | energy_to_grid_total | signedness_mismatch |
| storage_mix | input | 1052 | discharge_energy_today | signedness_mismatch |
| storage_mix | input | 1054 | discharge_energy_total | signedness_mismatch |
| storage_mix | input | 1056 | charge_energy_today | signedness_mismatch |
| storage_mix | input | 1058 | charge_energy_total | signedness_mismatch |
| min_tl_xh | input | 3170 | battery_current | signedness_mismatch |
| min_tl_xh | input | 3191 | bms_avg_temp_a | scale_mismatch |
| min_tl_xh | input | 3194 | bms_max_cell_temp_b | scale_mismatch |
| min_tl_xh | input | 3195 | bms_avg_temp_c | scale_mismatch |
| min_tl_xh | input | 3224 | bms_discharge_volt_limit | scale_mismatch |
| min_tl_xh | input | 3230 | bms_cell_volt_max | scale_mismatch |
| min_tl_xh | input | 3231 | bms_cell_volt_min | scale_mismatch |

## Register tables by family

### MIN / TL-XH

Best-supported model family; MIN 6000TL-XH is live read validated.

| Table | Address | Semantic | Role | Name | Description | Encoding / scale | Unit | Access | Status | Evidence | Notes |
|---|---:|---|---|---|---|---|---|---|---|---|---|
| holding | 0 | — | unknown | Inverter enable flags | Inverter enable flags | u16 bitfield | — | R/W | RESOLVED_WITH_NOTES | read_verified, semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| holding | 1 | — | unknown | Safety function enable flags | SPI: system protection interface Bit0~3:forCEI0-21 Bit4~6:forSAA | register value | — | W | SOURCE_ONLY | source_claim | ;  |
| holding | 2 | — | unknown | Persist power-factor commands | Means these settings will be acting or not when next poweron | register value | — | W | RESOLVED | semantic_correlated, source_claim | ;  |
| holding | 3 | — | unknown | Active power limit setpoint | 255:powerisnotbelimited | register value; /1 | % | W | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| holding | 4 | — | unknown | Reactive power limit setpoint | 255:powerisnotbelimited | register value; /1 | % | W | SOURCE_ONLY | source_claim | ;  |
| holding | 5 | — | unknown | Power factor target | Inverter output power factor’s10000times | register value; /10000 | pf | W | SOURCE_ONLY | source_claim | ;  |
| holding | 6 | — | unknown | Rated apparent power | Normal power(high) | register value; /10 | 0.1VA | R | SOURCE_ONLY | source_claim | ;  |
| holding | 7 | — | unknown | Rated apparent power | Normal power(low) | register value; /10 | 0.1VA | R | SOURCE_ONLY | source_claim | ;  |
| holding | 8 | — | unknown | Nominal PV voltage | NormalworkPV voltage | register value; /10 | 0.1V | R | SOURCE_ONLY | source_claim | ;  |
| holding | 9 | — | unknown | Firmware | Firmwareversion (high) | firmware_version; /10 | ASCII | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| holding | 10 | — | unknown | Firmware | Firmwareversion (middle) | register value | ASCII | R | SOURCE_ONLY | source_claim | ;  |
| holding | 11 | — | unknown | Firmware | Firmwareversion(low) | register value | ASCII | R | SOURCE_ONLY | source_claim | ;  |
| holding | 12 | — | unknown | Firmware | ControlFirmware version(high) | register value | ASCII | R | SOURCE_ONLY | source_claim | ;  |
| holding | 13 | — | unknown | Firmware | ControlFirmware version(middle) | register value | ASCII | R | SOURCE_ONLY | source_claim | ;  |
| holding | 14 | — | unknown | Firmware | ControlFirmware version(low) | register value | ASCII | R | SOURCE_ONLY | source_claim | ;  |
| holding | 15 | — | unknown | LCD language selection | 0:Italian; 1:English; 2:German; 3:Spanish; 4:French; 5:Chinese; 6：Polish 7：Portugues 8：Hungary | register value | — | W | SOURCE_ONLY | source_claim | ;  |
| holding | 16 | — | unknown | Country profile configured | CountrySelectedor not | register value | — | W | SOURCE_ONLY | source_claim | ;  |
| holding | 17 | — | unknown | PV start voltage threshold | Inputstartvoltage | register value; /10 | 0.1V | W | SOURCE_ONLY | source_claim | ;  |
| holding | 18 | — | unknown | Start-up delay | Starttime | register value; /1 | 1s | W | SOURCE_ONLY | source_claim | ;  |
| holding | 19 | — | unknown | Restart delay | RestartDelayTime afterfaultback; | register value; /1 | 1s | W | SOURCE_ONLY | source_claim | ;  |
| holding | 20 | — | unknown | Active power ramp rate (startup) | Powerstartslope | register value; /10 | 0.1% | W | SOURCE_ONLY | source_claim | ;  |
| holding | 21 | — | unknown | Active power ramp rate (restart) | Powerrestartslope | register value; /10 | 0.1% | W | SOURCE_ONLY | source_claim | ;  |
| holding | 22 | — | unknown | Modbus RTU baud rate | Select communicationbaudrat e 0:9600bps 1:38400bps | register value | — | W | SOURCE_ONLY | source_claim | ;  |
| holding | 23 | — | unknown | Inverter serial number | Inverter serial number | ASCII, 10 characters | ASCII | R | RESOLVED_WITH_NOTES | read_verified, semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| holding | 24 | — | unknown | Serial Number | The Home Assistant integration exposes this as the device serial number and reuses it as the unique identifier. | register value | ASCII | R | SOURCE_ONLY | source_claim | ;  |
| holding | 25 | — | unknown | Serial Number | The Home Assistant integration exposes this as the device serial number and reuses it as the unique identifier. | register value | ASCII | R | SOURCE_ONLY | source_claim | ;  |
| holding | 26 | — | unknown | Serial Number | The Home Assistant integration exposes this as the device serial number and reuses it as the unique identifier. | register value | ASCII | R | SOURCE_ONLY | source_claim | ;  |
| holding | 27 | — | unknown | Serial Number | The Home Assistant integration exposes this as the device serial number and reuses it as the unique identifier. | register value | ASCII | R | SOURCE_ONLY | source_claim | ;  |
| holding | 28 | — | unknown | Inverter Model | Home Assistant renders this value as the string A# B# D# T# P# U# M# S# via the integration's model() helper. Vendor spec lists value pattern `&*5`; digits appear to be stored without the leading letter codes, so treat as encoded tokens until verified on hardware. | register value; /10 | — | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| holding | 29 | — | unknown | Inverter Model | Home Assistant renders this value as the string A# B# D# T# P# U# M# S# via the integration's model() helper. Vendor spec lists value pattern `&*5`; digits appear to be stored without the leading letter codes, so treat as encoded tokens until verified on hardware. | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| holding | 30 | — | unknown | Modbus slave address | Communicate address | register value | — | W | SOURCE_ONLY | source_claim | ;  |
| holding | 31 | — | unknown | Firmware update trigger | Updatefirmware | register value | — | W | SOURCE_ONLY | source_claim | ;  |
| holding | 32 | — | unknown | Reset user configuration | Use with caution; the inverter immediately reboots and loses provisioning data. | register value | — | W | SOURCE_ONLY | source_claim | ;  |
| holding | 33 | — | unknown | Factory reset | Equivalent to the front-panel factory reset. Requires re-commissioning afterwards. | register value | — | W | SOURCE_ONLY | source_claim | ;  |
| holding | 34 | — | unknown | Manufacturer information string | The original table lists these words as Manufacturer Info 8-1 (high/middle/low); combine them to read the full string. | register value | ASCII | R | SOURCE_ONLY | source_claim | ;  |
| holding | 35 | — | unknown | Manufacturer information string | The original table lists these words as Manufacturer Info 8-1 (high/middle/low); combine them to read the full string. | register value | ASCII | R | SOURCE_ONLY | source_claim | ;  |
| holding | 36 | — | unknown | Manufacturer information string | The original table lists these words as Manufacturer Info 8-1 (high/middle/low); combine them to read the full string. | register value | ASCII | R | SOURCE_ONLY | source_claim | ;  |
| holding | 37 | — | unknown | Manufacturer information string | The original table lists these words as Manufacturer Info 8-1 (high/middle/low); combine them to read the full string. | register value | ASCII | R | SOURCE_ONLY | source_claim | ;  |
| holding | 38 | — | unknown | Manufacturer information string | The original table lists these words as Manufacturer Info 8-1 (high/middle/low); combine them to read the full string. | register value | ASCII | R | SOURCE_ONLY | source_claim | ;  |
| holding | 39 | — | unknown | Manufacturer information string | The original table lists these words as Manufacturer Info 8-1 (high/middle/low); combine them to read the full string. | register value | ASCII | R | SOURCE_ONLY | source_claim | ;  |
| holding | 40 | — | unknown | Manufacturer information string | The original table lists these words as Manufacturer Info 8-1 (high/middle/low); combine them to read the full string. | register value | ASCII | R | SOURCE_ONLY | source_claim | ;  |
| holding | 41 | — | unknown | Manufacturer information string | The original table lists these words as Manufacturer Info 8-1 (high/middle/low); combine them to read the full string. | register value | ASCII | R | SOURCE_ONLY | source_claim | ;  |
| holding | 42 | — | unknown | G100 failsafe enable | EnglishG100failsafeset | register value | — | W | SOURCE_ONLY | source_claim | ;  |
| holding | 43 | — | unknown | Device type code | Device type code | vendor encoded | — | R | RESOLVED_WITH_NOTES | read_verified, semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| holding | 44 | — | unknown | Trackers and phases | Trackers and phases | high byte trackers, low byte phases | — | R | RESOLVED_WITH_NOTES | read_verified, semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| holding | 45 | — | unknown | System clock year | Localtime | register value | — | W | SOURCE_ONLY | source_claim | ;  |
| holding | 46 | — | unknown | System clock month | Systemtime-Month | register value | — | W | SOURCE_ONLY | source_claim | ;  |
| holding | 47 | — | unknown | System clock day | Systemtime-Day | register value | — | W | SOURCE_ONLY | source_claim | ;  |
| holding | 48 | — | unknown | System clock hour | Systemtime-Hour | register value | — | W | SOURCE_ONLY | source_claim | ;  |
| holding | 49 | — | unknown | System clock minute | Systemtime-Min | register value | — | W | SOURCE_ONLY | source_claim | ;  |
| holding | 50 | — | unknown | System clock second | Systemtime-Second | register value | — | W | SOURCE_ONLY | source_claim | ;  |
| holding | 51 | — | unknown | System clock weekday | SystemWeekly | register value | — | W | SOURCE_ONLY | source_claim | ;  |
| holding | 52 | — | unknown | Stage 1 undervoltage limit | Gridvoltagelowlimit protect | register value | 0.1V | W | SOURCE_ONLY | source_claim | ;  |
| holding | 53 | — | unknown | Stage 1 overvoltage limit | Gridvoltagehighlimit protect | register value | 0.1V | W | SOURCE_ONLY | source_claim | ;  |
| holding | 54 | — | unknown | Stage 1 underfrequency limit | Gridfrequencylow limitprotect | register value | 0.01 Hz | W | SOURCE_ONLY | source_claim | ;  |
| holding | 55 | — | unknown | Stage 1 overfrequency limit | Gridhigh frequencylimitprotect | register value | 0.01 Hz | W | SOURCE_ONLY | source_claim | ;  |
| holding | 56 | — | unknown | Stage 2 undervoltage limit | Gridvoltagelowlimit protect2 | register value | 0.1V | W | SOURCE_ONLY | source_claim | ;  |
| holding | 57 | — | unknown | Stage 2 overvoltage limit | Gridvoltagehighlimit protect2 | register value | 0.1V | W | SOURCE_ONLY | source_claim | ;  |
| holding | 58 | — | unknown | Stage 2 underfrequency limit | Gridfrequencylow limitprotect2 | register value | 0.01 Hz | W | SOURCE_ONLY | source_claim | ;  |
| holding | 59 | — | unknown | Stage 2 overfrequency limit | Gridhighfrequency limitprotect2 | register value | 0.01 Hz | W | SOURCE_ONLY | source_claim | ;  |
| holding | 60 | — | unknown | Stage 3 undervoltage limit | Grid voltage low limit protect3 | register value | 0.1V | W | SOURCE_ONLY | source_claim | ;  |
| holding | 61 | — | unknown | Stage 3 overvoltage limit | Grid voltage high limit protect3 | register value | 0.1V | W | SOURCE_ONLY | source_claim | ;  |
| holding | 62 | grid_frequency | alternate | Stage 3 underfrequency limit | Grid frequency low limitprotect3 | register value | 0.01Hz | W | SOURCE_ONLY | source_claim | ; alternates: register:min_tl_xh:holding:63, register:min_tl_xh:holding:72, register:min_tl_xh:holding:73, register:min_tl_xh:holding:74, register:min_tl_xh:holding:75, register:min_tl_xh:holding:78, register:min_tl_xh:holding:79, register:min_tl_xh:input:37, register:min_tl_xh:input:3025 |
| holding | 63 | grid_frequency | alternate | Stage 3 overfrequency limit | Grid frequency high limitprotect3 | register value | 0.01Hz | W | SOURCE_ONLY | source_claim | ; alternates: register:min_tl_xh:holding:62, register:min_tl_xh:holding:72, register:min_tl_xh:holding:73, register:min_tl_xh:holding:74, register:min_tl_xh:holding:75, register:min_tl_xh:holding:78, register:min_tl_xh:holding:79, register:min_tl_xh:input:37, register:min_tl_xh:input:3025 |
| holding | 64 | — | unknown | Reconnect undervoltage limit | Gridlowvoltagelimit connecttoGrid | register value | 0.1V | W | SOURCE_ONLY | source_claim | ;  |
| holding | 65 | — | unknown | Reconnect overvoltage limit | Gridhighvoltagelimit connecttoGrid | register value | 0.1V | W | SOURCE_ONLY | source_claim | ;  |
| holding | 66 | — | unknown | Reconnect underfrequency limit | Gridlowfrequency | register value | 0.01 | W | SOURCE_ONLY | source_claim | ;  |
| holding | 67 | — | unknown | Reconnect overfrequency limit | Gridhighfrequency limitconnecttoGrid | register value | 0.01 Hz | W | SOURCE_ONLY | source_claim | ;  |
| holding | 68 | — | unknown | Stage 1 undervoltage trip delay | Grid voltage low limit protecttime 1 | register value | Cycle | W | SOURCE_ONLY | source_claim | ;  |
| holding | 69 | — | unknown | Stage 1 overvoltage trip delay | Grid voltage high limit protecttime 1 | register value | Cycle | W | SOURCE_ONLY | source_claim | ;  |
| holding | 70 | — | unknown | Stage 2 undervoltage trip delay | Grid voltage low limit protecttime 2 | register value | Cycle | W | SOURCE_ONLY | source_claim | ;  |
| holding | 71 | — | unknown | Stage 2 overvoltage trip delay | Grid voltage high limit protecttime 2 | register value | Cycle | W | SOURCE_ONLY | source_claim | ;  |
| holding | 72 | grid_frequency | alternate | Stage 1 underfrequency trip delay | Grid frequency low limitprotecttime 1 | register value | Cycle | W | SOURCE_ONLY | source_claim | ; alternates: register:min_tl_xh:holding:62, register:min_tl_xh:holding:63, register:min_tl_xh:holding:73, register:min_tl_xh:holding:74, register:min_tl_xh:holding:75, register:min_tl_xh:holding:78, register:min_tl_xh:holding:79, register:min_tl_xh:input:37, register:min_tl_xh:input:3025 |
| holding | 73 | grid_frequency | alternate | Modbus Version | Grid frequency high limitprotecttime 1 | register value | Cycle | W | SOURCE_ONLY | source_claim | ; alternates: register:min_tl_xh:holding:62, register:min_tl_xh:holding:63, register:min_tl_xh:holding:72, register:min_tl_xh:holding:74, register:min_tl_xh:holding:75, register:min_tl_xh:holding:78, register:min_tl_xh:holding:79, register:min_tl_xh:input:37, register:min_tl_xh:input:3025 |
| holding | 74 | grid_frequency | alternate | Stage 2 underfrequency trip delay | Grid frequency low limitprotecttime 2 | register value | Cycle | W | SOURCE_ONLY | source_claim | ; alternates: register:min_tl_xh:holding:62, register:min_tl_xh:holding:63, register:min_tl_xh:holding:72, register:min_tl_xh:holding:73, register:min_tl_xh:holding:75, register:min_tl_xh:holding:78, register:min_tl_xh:holding:79, register:min_tl_xh:input:37, register:min_tl_xh:input:3025 |
| holding | 75 | grid_frequency | alternate | Stage 2 overfrequency trip delay | Grid frequency high limitprotecttime 2 | register value | Cycle | W | SOURCE_ONLY | source_claim | ; alternates: register:min_tl_xh:holding:62, register:min_tl_xh:holding:63, register:min_tl_xh:holding:72, register:min_tl_xh:holding:73, register:min_tl_xh:holding:74, register:min_tl_xh:holding:78, register:min_tl_xh:holding:79, register:min_tl_xh:input:37, register:min_tl_xh:input:3025 |
| holding | 76 | — | unknown | Stage 3 undervoltage trip delay | Grid voltage low limit protecttime 3 | register value | Cycle | W | SOURCE_ONLY | source_claim | ;  |
| holding | 77 | — | unknown | Stage 3 overvoltage trip delay | Grid voltage high limit protecttime 3 | register value | Cycle | W | SOURCE_ONLY | source_claim | ;  |
| holding | 78 | grid_frequency | alternate | Stage 3 underfrequency trip delay | Grid frequency low limitprotecttime 3 | register value | Cycle | W | SOURCE_ONLY | source_claim | ; alternates: register:min_tl_xh:holding:62, register:min_tl_xh:holding:63, register:min_tl_xh:holding:72, register:min_tl_xh:holding:73, register:min_tl_xh:holding:74, register:min_tl_xh:holding:75, register:min_tl_xh:holding:79, register:min_tl_xh:input:37, register:min_tl_xh:input:3025 |
| holding | 79 | grid_frequency | alternate | Stage 3 overfrequency trip delay | Grid frequency high limitprotecttime 3 | register value | Cycle | W | SOURCE_ONLY | source_claim | ; alternates: register:min_tl_xh:holding:62, register:min_tl_xh:holding:63, register:min_tl_xh:holding:72, register:min_tl_xh:holding:73, register:min_tl_xh:holding:74, register:min_tl_xh:holding:75, register:min_tl_xh:holding:78, register:min_tl_xh:input:37, register:min_tl_xh:input:3025 |
| holding | 80 | — | unknown | Ten-minute overvoltage limit | Voltprotectionfor10 min | register value | 0.1V | W | SOURCE_ONLY | source_claim | ;  |
| holding | 81 | — | unknown | PV input high-voltage fault | PVVoltageHigh Fault | register value | 0.1V | W | SOURCE_ONLY | source_claim | ;  |
| holding | 82 | — | unknown | Controller firmware build string | Positions: 0-1 model letters, 2-3 model variant, 4-5 DSP1 build, 6-7 DSP2/M0 build, 8-9 CPLD/AFCI build, 10-11 M3 build. | register value | ASCII | R | SOURCE_ONLY | source_claim | ;  |
| holding | 83 | — | unknown | Controller firmware build string | Positions: 0-1 model letters, 2-3 model variant, 4-5 DSP1 build, 6-7 DSP2/M0 build, 8-9 CPLD/AFCI build, 10-11 M3 build. | register value | ASCII | R | SOURCE_ONLY | source_claim | ;  |
| holding | 84 | — | unknown | Controller firmware build string | Positions: 0-1 model letters, 2-3 model variant, 4-5 DSP1 build, 6-7 DSP2/M0 build, 8-9 CPLD/AFCI build, 10-11 M3 build. | register value | ASCII | R | SOURCE_ONLY | source_claim | ;  |
| holding | 85 | — | unknown | Controller firmware build string | Positions: 0-1 model letters, 2-3 model variant, 4-5 DSP1 build, 6-7 DSP2/M0 build, 8-9 CPLD/AFCI build, 10-11 M3 build. | register value | ASCII | R | SOURCE_ONLY | source_claim | ;  |
| holding | 86 | — | unknown | Controller firmware build string | Positions: 0-1 model letters, 2-3 model variant, 4-5 DSP1 build, 6-7 DSP2/M0 build, 8-9 CPLD/AFCI build, 10-11 M3 build. | register value | ASCII | R | SOURCE_ONLY | source_claim | ;  |
| holding | 87 | — | unknown | Controller firmware build string | Positions: 0-1 model letters, 2-3 model variant, 4-5 DSP1 build, 6-7 DSP2/M0 build, 8-9 CPLD/AFCI build, 10-11 M3 build. | register value | ASCII | R | SOURCE_ONLY | source_claim | ;  |
| holding | 88 | — | unknown | Modbus version | Modbus version | u16 / 100; /100 | version | R | RESOLVED_WITH_NOTES | read_verified, semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| holding | 89 | — | unknown | Power-factor control mode | 0=Unity PF, 1=Fixed PF setpoint, 2=Default PF line, 3=User-defined PF line, 4=Under-excited reactive power, 5=Over-excited reactive power, 6=Q(V) curve, 7=Direct control, 8=Static capacitive QV, 9=Static inductive QV. | register value | — | W | SOURCE_ONLY | source_claim | ;  |
| holding | 90 | — | unknown | GPRS modem IP/status flags | Bit 0-3: 0=idle, 1=IP read requested, 2=set IP succeeded; Bit 4-7: 0=unknown, 1=modem OK, 2=no SIM, 3=no network, 4=TCP connect fail, 5=TCP connected, etc. | register value | — | W | UNKNOWN_RESERVED | source_claim | ;  |
| holding | 91 | — | unknown | Frequency derating start | Frequencyderating startpoint | register value | 0.01H Z | W | SOURCE_ONLY | source_claim | ;  |
| holding | 92 | — | unknown | Frequency derating slope | Frequency–loadlimit rate | register value | 10tim es | W | SOURCE_ONLY | source_claim | ;  |
| holding | 93 | — | unknown | CEI 0-21 Q(V) point V1S | CEI021V1SQ(v) | register value | 0.1V | W | SOURCE_ONLY | source_claim | ;  |
| holding | 94 | — | unknown | CEI 0-21 Q(V) point V2S | CEI021V2SQ(v) | register value | 0.1V | W | SOURCE_ONLY | source_claim | ;  |
| holding | 95 | — | unknown | CEI 0-21 Q(V) point V1L | CEI021V1LQ(v) | register value | 0.1V | W | SOURCE_ONLY | source_claim | ;  |
| holding | 96 | — | unknown | CEI 0-21 Q(V) point V2L | CEI021V2LQ(v) | register value | 0.1V | W | SOURCE_ONLY | source_claim | ;  |
| holding | 97 | — | unknown | Q(V) lock-in active power | Q(v)lockinactive powerofCEI021 | register value | Percen t | W | SOURCE_ONLY | source_claim | ;  |
| holding | 98 | — | unknown | Q(V) lock-out active power | Q(v)lockOutactive powerofCEI021 | register value | Percen t | W | SOURCE_ONLY | source_claim | ;  |
| holding | 99 | — | unknown | Power-factor curve lock-in voltage | Lockingirdvoltof CEI021PFline | register value | 0.1V | W | SOURCE_ONLY | source_claim | ;  |
| holding | 100 | — | unknown | Power-factor curve lock-out voltage | Lockoutgirdvoltof CEI021PFline | register value | 0.1V | W | SOURCE_ONLY | source_claim | ;  |
| holding | 101 | — | unknown | Power-factor adjust value 1 | PFadjustvalue1 | register value | — | W | SOURCE_ONLY | source_claim | ;  |
| holding | 102 | — | unknown | Power-factor adjust value 2 | PFadjustvalue2 | register value | — | W | SOURCE_ONLY | source_claim | ;  |
| holding | 103 | — | unknown | Power-factor adjust value 3 | PFadjustvalue3 | register value | — | W | SOURCE_ONLY | source_claim | ;  |
| holding | 104 | — | unknown | Power-factor adjust value 4 | PFadjustvalue4 | register value | — | W | SOURCE_ONLY | source_claim | ;  |
| holding | 105 | — | unknown | Power-factor adjust value 5 | PFadjustvalue5 | register value | — | W | SOURCE_ONLY | source_claim | ;  |
| holding | 106 | — | unknown | Power-factor adjust value 6 | PFadjustvalue6 | register value | — | W | SOURCE_ONLY | source_claim | ;  |
| holding | 107 | — | unknown | Q(V) response delay | QV Reactive Power delaytime | register value | 1S | W | SOURCE_ONLY | source_claim | ;  |
| holding | 108 | — | unknown | Over-frequency derating delay | Overfrequency derati ngdelaytime | register value | 50ms | W | SOURCE_ONLY | source_claim | ;  |
| holding | 109 | — | unknown | Maximum reactive power magnitude | QmaxforQ(V)curve | register value | 0.1% | W | SOURCE_ONLY | source_claim | ;  |
| holding | 110 | — | unknown | PF curve point 1 load | 255meansnothispoint | register value | percen t | W | SOURCE_ONLY | source_claim | ;  |
| holding | 111 | — | unknown | PF curve point 1 target | PFlimitlinepoint1 powerfactor | register value | — | W | SOURCE_ONLY | source_claim | ;  |
| holding | 112 | — | unknown | PF curve point 2 load | 255meansnothispoint | register value | percen t | W | SOURCE_ONLY | source_claim | ;  |
| holding | 113 | — | unknown | PF curve point 2 target | PFlimitlinepoint 2powerfactor | register value | — | W | SOURCE_ONLY | source_claim | ;  |
| holding | 114 | — | unknown | PF curve point 3 load | 255meansnothispoint | register value | percen t | W | SOURCE_ONLY | source_claim | ;  |
| holding | 115 | — | unknown | PF curve point 3 target | PFlimitlinepoint3 powerfactor | register value | — | W | SOURCE_ONLY | source_claim | ;  |
| holding | 116 | — | unknown | PF curve point 4 load | 255meansnothispoint | register value | percen t | W | SOURCE_ONLY | source_claim | ;  |
| holding | 117 | — | unknown | PF curve point 4 target | PFlimitlinepoint4 powerfactor | register value | — | W | SOURCE_ONLY | source_claim | ;  |
| holding | 118 | — | unknown | Module code segments | SxxBxx | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| holding | 119 | — | unknown | Module code segments | DxxTxx | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| holding | 120 | — | unknown | Module code segments | PxxUxx | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| holding | 121 | — | unknown | Module code segments | Mxxxx Power | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| holding | 122 | — | unknown | Export limit enable mode | ExportLimitenable, 0:DisableexportLimit; 1:Enable485exportLimit; 2:Enable232exportLimit; 3:EnableCTexportLimit; | register value | — | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 123 | — | unknown | Export limit power setpoint | ExportLimitPowerRate | register value | 0.1% | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 124 | — | unknown | Tracker coupling mode | 0:Independent 1:DCSource 2:Parallel | register value | — | W | SOURCE_ONLY | source_claim | ;  |
| holding | 3000 | — | unknown | Export-limit fallback cap | Thepowerrate whenexportLimit failed | register value; /10 | 0.1% | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 3001 | — | unknown | Serial Number | Thenewmodel usesthefollowing registerstorecord theserialnumber; The representationis thesameasthe original:one registerholdstwo charactersandthe newserialnumber is30characters. | serial_number; /10 | ASCII | R/W | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| holding | 3002 | — | unknown | Serial Number | Serialnumber3-4 | register value | ASCII | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 3003 | — | unknown | Serial Number | Serialnumber5-6 | register value | ASCII | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 3004 | — | unknown | Serial Number | Serialnumber7-8 | register value | ASCII | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 3005 | — | unknown | Serial Number | Serialnumber9-10 | register value | ASCII | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 3006 | — | unknown | Serial Number | Serialnumber11-12 | register value | ASCII | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 3007 | — | unknown | Serial Number | Serialnumber13-14 | register value | ASCII | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 3008 | — | unknown | Serial Number | Serialnumber15-16 | register value | ASCII | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 3009 | — | unknown | Serial Number | Serialnumber17-18 | register value | ASCII | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 3010 | — | unknown | Serial Number | Serialnumber19-20 | register value | ASCII | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 3011 | — | unknown | Serial Number | Serialnumber21-22 | register value | ASCII | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 3012 | — | unknown | Serial Number | Serialnumber23-24 | register value | ASCII | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 3013 | — | unknown | Serial Number | Serialnumber25-26 | register value | ASCII | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 3014 | — | unknown | Serial Number | Serialnumber27-28 | register value | ASCII | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 3015 | — | unknown | Serial Number | Serialnumber29-30 | register value | ASCII | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 3016 | — | unknown | Dry-contact enable | DryContact functionenable | register value | — | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 3017 | — | unknown | Dry-contact close threshold | The power rate of drycontactturnon | register value | 0.1% | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 3018 | — | unknown | Hybrid work mode | MIN2.5~6KTL-XH/ XADoubleCT special | register value | — | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 3019 | — | unknown | Dry-contact release threshold | Drycontact closurepowerpe rcentage | register value | 0~100 0 | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 3020 | — | unknown | Off-grid box control | Leave at factory value unless instructed by Growatt support. | register value | — | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 3021 | — | unknown | External off-grid enable | 0x00: Disable; （default） 0x01:Enable; | register value | — | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 3022 | — | unknown | BDC stop-work bus voltage | BdcStopWorkOfBusVolt | register value | V | R | SOURCE_ONLY | source_claim | ;  |
| holding | 3023 | — | unknown | Grid topology selection | MIN2.5~6KTL-XH/ XADoubleCT special | register value | — | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 3024 | — | unknown | Float-charge current limit | CCcurrent | register value; /10 | 0.1A | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 3025 | — | unknown | Battery-low warning setpoint | Leadacidbattery LVvoltage | register value | 0.1V | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 3026 | — | unknown | Battery-low warning clear | Clearbatterylow voltageerror voltagepoint LoadPercent(only lead-Acid): 45.5V(Load< 20%); 48.0V(20%<=Load <=50%); 49.0V(Load> 50%); | register value | 0.1V | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 3027 | — | unknown | Battery discharge cutoff | Shouldstop dischargewhen lowerthanthis voltage(only lead-Acid): 46.0V(Load< 20%); 44.8V(20%<=Load <=50%); 44.2V(Load> 50%); | register value | 0.1V | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 3028 | — | unknown | Battery charge stop voltage | Shouldstop chargewhen higherthanthis voltage | register value; /100 | 0.01V | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 3029 | — | unknown | Battery discharge start voltage | Shouldnot dischargewhen lowerthanthis voltage | register value; /100 | 0.01V | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 3030 | — | unknown | Battery constant-charge voltage | CVvoltage（acid） canchargewhen lowerthanthis voltage | register value; /100 | 0.01V | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 3031 | — | unknown | Discharge low temperature limit | 0-200:0-20℃ 1000-1400： -40-0℃ | register value; /10 | 0.1℃ | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 3032 | — | unknown | Discharge high temperature limit | Batterytemperatureupper limitfordischarge | register value; /10 | 0.1℃ | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 3033 | — | unknown | Charge low temperature limit | Battery temperaturelower limit 0-200:0-20℃ 1000-1400： -40-0℃ | register value; /10 | 0.1℃ | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 3034 | — | unknown | Charge high temperature limit | Battery temperature upperlimit | register value; /10 | 0.1℃ | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 3035 | — | unknown | Under-frequency discharge delay | UnderFreDelay Time | register value | 50ms | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 3036 | grid_first_discharge_rate | supported | Grid-first discharge power rate | Grid-first discharge power rate | u16 percentage; 255 disables limit | % | R/W | RESOLVED | read_verified, semantic_correlated, source_claim | ;  |
| holding | 3037 | grid_first_stop_soc | supported | Grid-first stop SOC | Grid-first stop SOC | u16 | % | R/W | RESOLVED | read_verified, semantic_correlated, source_claim | ;  |
| holding | 3038 | — | unknown | Grid-first schedule 1 start/control | Grid-first schedule 1 start/control | packed minute/hour/priority/enable | — | R/W | RESOLVED | read_verified, source_claim | ;  |
| holding | 3039 | — | unknown | Grid-first schedule 1 end | Grid-first schedule 1 end | packed minute/hour | — | R/W | RESOLVED | read_verified, source_claim | ;  |
| holding | 3040 | — | unknown | Grid-first schedule 2 start/control | Grid-first schedule 2 start/control | packed minute/hour/priority/enable | — | R/W | RESOLVED | read_verified, source_claim | ;  |
| holding | 3041 | — | unknown | Grid-first schedule 2 end | Grid-first schedule 2 end | packed minute/hour | W | R/W | RESOLVED | read_verified, source_claim | ;  |
| holding | 3042 | — | unknown | Grid-first schedule 3 start/control | Grid-first schedule 3 start/control | packed minute/hour/priority/enable | W | R/W | RESOLVED | read_verified, source_claim | ;  |
| holding | 3043 | — | unknown | Grid-first schedule 3 end | Grid-first schedule 3 end | packed minute/hour | W | R/W | RESOLVED | read_verified, source_claim | ;  |
| holding | 3044 | — | unknown | Grid-first schedule 4 start/control | Grid-first schedule 4 start/control | packed minute/hour/priority/enable | W | R/W | RESOLVED | read_verified, source_claim | ;  |
| holding | 3045 | — | unknown | Grid-first schedule 4 end | Grid-first schedule 4 end | packed minute/hour | W | R/W | RESOLVED | read_verified, source_claim | ;  |
| holding | 3046 | — | unknown | Reserved | Reserved | u16 raw | W | R | RESOLVED | read_verified, source_claim | ;  |
| holding | 3047 | battery_first_charge_rate | supported | Battery-first charge power rate | Battery-first charge power rate | u16 percentage | % | R/W | RESOLVED_WITH_NOTES | read_verified, semantic_correlated, source_claim | Legacy data-type catalogue incorrectly labels this as a two-word runtime counter.; ;  |
| holding | 3048 | battery_first_stop_soc | supported | Battery-first stop SOC | Battery-first stop SOC | u16 | % | R/W | RESOLVED_WITH_NOTES | read_verified, semantic_correlated, source_claim | Legacy data-type catalogue incorrectly labels this as the low word of runtime.; ;  |
| holding | 3049 | ac_charge_enabled | supported | AC charge enabled | AC charge enabled | u16 enum 0=disabled, 1=enabled | — | R/W | RESOLVED_WITH_NOTES | read_verified, semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| holding | 3050 | — | unknown | Battery-first schedule 1 start/control | Battery-first schedule 1 start/control | packed minute/hour/priority/enable | — | R/W | RESOLVED | read_verified, source_claim | ;  |
| holding | 3051 | — | unknown | Battery-first schedule 1 end | Battery-first schedule 1 end | packed minute/hour | kWh | R/W | RESOLVED | read_verified, source_claim | ;  |
| holding | 3052 | — | unknown | Battery-first schedule 2 start/control | Battery-first schedule 2 start/control | packed minute/hour/priority/enable | kWh | R/W | RESOLVED | read_verified, source_claim | ;  |
| holding | 3053 | — | unknown | Battery-first schedule 2 end | Battery-first schedule 2 end | packed minute/hour | kWh | R/W | RESOLVED | read_verified, source_claim | ;  |
| holding | 3054 | — | unknown | Battery-first schedule 3 start/control | Battery-first schedule 3 start/control | packed minute/hour/priority/enable | kWh | R/W | RESOLVED | read_verified, source_claim | ;  |
| holding | 3055 | — | unknown | Battery-first schedule 3 end | Battery-first schedule 3 end | packed minute/hour | kWh | R/W | RESOLVED | read_verified, source_claim | ;  |
| holding | 3056 | — | unknown | Battery-first schedule 4 start/control | Battery-first schedule 4 start/control | packed minute/hour/priority/enable | kWh | R/W | RESOLVED | read_verified, source_claim | ;  |
| holding | 3057 | — | unknown | Battery-first schedule 4 end | Battery-first schedule 4 end | packed minute/hour | kWh | R/W | RESOLVED | read_verified, source_claim | ;  |
| holding | 3058 | — | unknown | Battery-first schedule 5 start/control | Battery-first schedule 5 start/control | packed minute/hour/priority/enable | kWh | R/W | RESOLVED | read_verified, source_claim | ;  |
| holding | 3059 | — | unknown | Battery-first schedule 5 end | Battery-first schedule 5 end | packed minute/hour | kWh | R/W | RESOLVED | read_verified, source_claim | ;  |
| holding | 3060 | — | unknown | Reserved | Reserved | register value; /10 | kWh | R | UNKNOWN_RESERVED | source_claim | ;  |
| holding | 3061 | — | unknown | Reserved | Reserved | register value; /10 | kWh | R | UNKNOWN_RESERVED | source_claim | ;  |
| holding | 3062 | — | unknown | Reserved | Reserved | register value; /10 | kWh | R | UNKNOWN_RESERVED | source_claim | ;  |
| holding | 3063 | — | unknown | Reserved | Reserved | register value; /10 | kWh | R | UNKNOWN_RESERVED | source_claim | ;  |
| holding | 3064 | — | unknown | Reserved | Reserved | register value; /10 | kWh | R | UNKNOWN_RESERVED | source_claim | ;  |
| holding | 3065 | — | unknown | Reserved | Reserved | register value; /10 | kWh | R | UNKNOWN_RESERVED | source_claim | ;  |
| holding | 3066 | — | unknown | Reserved | Reserved | register value; /10 | kWh | R | UNKNOWN_RESERVED | source_claim | ;  |
| holding | 3067 | — | unknown | Reserved | Reserved | register value; /10 | kWh | R | UNKNOWN_RESERVED | source_claim | ;  |
| holding | 3068 | — | unknown | Reserved | Reserved | register value; /10 | kWh | R | UNKNOWN_RESERVED | source_claim | ;  |
| holding | 3069 | — | unknown | Reserved | Reserved | register value; /10 | kWh | R | UNKNOWN_RESERVED | source_claim | ;  |
| holding | 3070 | — | unknown | BatteryType | Batterytype 0:Lithium 1:Lead-acid 2:other | register value; /10 | kWh | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 3071 | — | unknown | BatMdlSeria/ ParalNum | BatMdlSeria/Paral Num; SPH4-11Kused Theupper8bits indicatethe numberofseries segments； Thelower8bits indicatethe numberofparallel sections; | register value; /10 | kWh | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 3072 | — | unknown | Reserved | Reserved | register value; /10 | kWh | R | UNKNOWN_RESERVED | source_claim | ;  |
| holding | 3073 | — | unknown | Reserved | Reserved | register value; /10 | kWh | R | UNKNOWN_RESERVED | source_claim | ;  |
| holding | 3074 | — | unknown | Reserved | Reserved | register value; /10 | kWh | R | UNKNOWN_RESERVED | source_claim | ;  |
| holding | 3075 | — | unknown | Reserved | Reserved | register value; /10 | kWh | R | UNKNOWN_RESERVED | source_claim | ;  |
| holding | 3076 | — | unknown | Reserved | Reserved | register value; /10 | kWh | R | UNKNOWN_RESERVED | source_claim | ;  |
| holding | 3077 | — | unknown | Reserved | Reserved | register value; /10 | kWh | R | UNKNOWN_RESERVED | source_claim | ;  |
| holding | 3078 | — | unknown | Reserved | Reserved | register value; /10 | kWh | R | UNKNOWN_RESERVED | source_claim | ;  |
| holding | 3079 | — | unknown | UPS/EPS function enable | UPS/EPS function enable | u16 enum 0=disabled, 1=enabled | bool | R/W | RESOLVED | read_verified, source_claim | ;  |
| holding | 3080 | — | unknown | UPS/EPS voltage selection | UPS/EPS voltage selection | u16 enum 0=230 V, 1=208 V, 2=240 V | V | R/W | RESOLVED | read_verified, source_claim | ;  |
| holding | 3081 | — | unknown | UPS/EPS frequency selection | UPS/EPS frequency selection | u16 enum 0=50 Hz, 1=60 Hz | Hz | R/W | RESOLVED_WITH_NOTES | read_verified, source_claim | FC04 3081 is PV4 lifetime-energy high word; FC03 3081 is UPSFreqSet.; ;  |
| holding | 3082 | load_first_stop_soc | supported | Load-first stop SOC | Load-first stop SOC | u16 percentage | % | R/W | RESOLVED | read_verified, source_claim | ;  |
| holding | 3083 | — | unknown | Reserved | Reserved | register value; /10 | kWh | R | UNKNOWN_RESERVED | source_claim | ;  |
| holding | 3084 | — | unknown | Reserved | Reserved | register value; /10 | kWh | R | UNKNOWN_RESERVED | source_claim | ;  |
| holding | 3085 | — | unknown | Modbus slave address | 1:Communication addr=1 1~254: Communication addr=1~254 | register value | — | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 3086 | — | unknown | RS-485 baud rate | 0:9600bps 1:38400bps | register value | — | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 3087 | — | unknown | Battery rack serial | Forbattery | register value | ASCII | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 3088 | — | unknown | Battery rack serial | SerialNumber3-4 | register value | ASCII | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 3089 | — | unknown | Battery rack serial | SerialNumber5-6 | register value | ASCII | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 3090 | — | unknown | Battery rack serial | SerialNumber7-8 | register value | ASCII | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 3091 | — | unknown | Battery rack serial | SerialNumber9-10 | register value | ASCII | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 3092 | — | unknown | Battery rack serial | SerialNumber11-12 | register value | ASCII | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 3093 | — | unknown | Battery rack serial | SerialNumber13-14 | register value | ASCII | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 3094 | — | unknown | Battery rack serial | SerialNumber15-16 | register value | ASCII | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 3095 | — | unknown | BDC reset command | 0：Invaliddata 1：Resetsetting parameters 2：Resetcorrection parameter 3：Clearhistorical power | register value | — | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 3096 | — | unknown | BDC monitoring code | ZEBA | register value | ASCII | R | SOURCE_ONLY | source_claim | ;  |
| holding | 3097 | — | unknown | BDC monitoring code | Four-character identifier for the BDC monitoring firmware (e.g. ZEBA). | register value | ASCII | R | SOURCE_ONLY | source_claim | ;  |
| holding | 3098 | — | unknown | BDC DTC code | DTC | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| holding | 3099 | — | unknown | DSP firmware code | DSPsoftwarecode | register value | ASCII | R | SOURCE_ONLY | source_claim | ;  |
| holding | 3100 | — | unknown | DSP firmware code | Identifier for the inverter DSP firmware build. | register value | ASCII | R | SOURCE_ONLY | source_claim | ;  |
| holding | 3101 | — | unknown | DSP firmware version | DSPSoftwareVersion | register value | ASCII | R | SOURCE_ONLY | source_claim | ;  |
| holding | 3102 | — | unknown | Bus voltage reference | MinimumBUSvoltagefor charginganddischarging batteries | register value | V | R | SOURCE_ONLY | source_claim | ;  |
| holding | 3103 | — | unknown | BDC monitor firmware | BDCmonitoringsoftware version | register value | ASCII | R | SOURCE_ONLY | source_claim | ;  |
| holding | 3104 | — | unknown | BMS MCU hardware version | BMS hardware version information | register value | ASCII | R | SOURCE_ONLY | source_claim | ;  |
| holding | 3105 | — | unknown | BMS firmware version | BMSsoftwareversion information | register value | ASCII | R | SOURCE_ONLY | source_claim | ;  |
| holding | 3106 | — | unknown | BMS manufacturer | BMSManufacturerName | register value | ASCII | R | SOURCE_ONLY | source_claim | ;  |
| holding | 3107 | — | unknown | BMS communication interface | BMSCommunicati oninterfacetype： 0:RS485; 1:CAN; | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| holding | 3108 | — | unknown | BDC module identifier 4 | SxxBxx | register value | ASCII | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 3109 | — | unknown | BDC module identifier 3 | DxxTxx | register value | ASCII | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 3110 | — | unknown | BDC module identifier 2 | PxxUxx | register value | ASCII | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 3111 | — | unknown | BDC module identifier 1 | Mxxxx | register value | ASCII | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 3112 | — | unknown | Reserved | Reserved; reported as zero on known firmware. | register value | — | R | UNKNOWN_RESERVED | source_claim | ;  |
| holding | 3113 | — | unknown | BDC protocol version | Bit8-bit15The majorversion numberranges from0-256.In principle,itcannot bechanged Bit0-bit7Minor versionnumber [0-256].Ifthe protocolis changed,youneed toupdatethis version No. | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| holding | 3114 | — | unknown | BDC certification version | BDCCertificationVer | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| holding | 3115 | — | unknown | Reserved | Reserved for future use. | register value | — | R | UNKNOWN_RESERVED | source_claim | ;  |
| holding | 3116 | — | unknown | Reserved | Reserved for future use. | register value | — | R | UNKNOWN_RESERVED | source_claim | ;  |
| holding | 3117 | — | unknown | Reserved | Reserved for future use. | register value | — | R | UNKNOWN_RESERVED | source_claim | ;  |
| holding | 3118 | — | unknown | BDC on/off state | Indicates whether the battery DC converter is currently running (1) or idle (0). | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| holding | 3119 | — | unknown | Dry contact state | Current state of the dry-contact output (0 = open, 1 = closed). | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| holding | 3120 | — | unknown | Reserved | Reserved; reported as zero on TL-XH firmware. | register value | — | R | UNKNOWN_RESERVED | source_claim | ;  |
| holding | 3121 | — | unknown | Self-use power | Not yet surfaced by the Home Assistant integration. | register value; /10 | W | R | SOURCE_ONLY | source_claim | ;  |
| holding | 3122 | — | unknown | Self-use power | Not yet surfaced by the Home Assistant integration. | register value; /10 | W | R | SOURCE_ONLY | source_claim | ;  |
| holding | 3123 | — | unknown | System energy today | Available in firmware but not yet exposed as an integration attribute. | register value; /10 | kWh | R | SOURCE_ONLY | source_claim | ;  |
| holding | 3124 | — | unknown | System energy today | Available in firmware but not yet exposed as an integration attribute. | register value; /10 | kWh | R | SOURCE_ONLY | source_claim | ;  |
| holding | 3125 | — | unknown | Us Tou Month Groups | bit0~3:month_L； bit4~7:month_H bit8, 0:disable1：enable Bit9~15:reserve | register value | — | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 3126 | — | unknown | Us Tou Month Groups | WithTimeMonth1 | register value | — | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 3127 | — | unknown | Us Tou Month Groups | WithTimeMonth1 | register value | — | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 3128 | — | unknown | Us Tou Month Groups | WithTimeMonth1 | register value | — | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 3129 | — | unknown | Us Tou Slot Table | bit0~6:min； bit7~11:hour； bit12~14, 0:loadfirst; | register value | — | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 3130 | — | unknown | Us Tou Slot Table | bit0~6:min； bit7~11:hour； bit12-13, 0:Weekday 1:Weekend 2:WeeK bit14~15：reserve | register value | — | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 3131 | — | unknown | Us Tou Slot Table | SameasTime1 （us） | register value | — | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 3132 | — | unknown | Us Tou Slot Table | SameasTime1 （us） | register value | — | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 3133 | — | unknown | Us Tou Slot Table | SameasTime1 （us） | register value | — | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 3134 | — | unknown | Us Tou Slot Table | SameasTime1 （us） | register value | — | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 3135 | — | unknown | Us Tou Slot Table | SameasTime1 （us） | register value | — | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 3136 | — | unknown | Us Tou Slot Table | SameasTime1 （us） | register value | — | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 3137 | — | unknown | Us Tou Slot Table | SameasTime1 （us） | register value | — | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 3138 | — | unknown | Us Tou Slot Table | SameasTime1 （us） | register value | — | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 3139 | — | unknown | Us Tou Slot Table | SameasTime1 （us） | register value | — | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 3140 | — | unknown | Us Tou Slot Table | SameasTime1 （us） | register value | — | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 3141 | — | unknown | Us Tou Slot Table | SameasTime1 （us） | register value | — | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 3142 | — | unknown | Us Tou Slot Table | SameasTime1 （us） | register value | — | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 3143 | — | unknown | Us Tou Slot Table | SameasTime1 （us） | register value | — | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 3144 | — | unknown | Us Tou Slot Table | SameasTime1 （us） | register value | — | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 3145 | — | unknown | Us Tou Slot Table | SameasTime1 （us） | register value | — | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 3146 | — | unknown | Us Tou Slot Table | SameasTime1 （us） | register value | — | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 3147 | — | unknown | Us Tou Slot Table | SameasTime1 （us） | register value | — | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 3148 | — | unknown | Us Tou Slot Table | SameasTime1 （us） | register value | — | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 3149 | — | unknown | Us Tou Slot Table | SameasTime1 （us） | register value | — | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 3150 | — | unknown | Us Tou Slot Table | SameasTime1 （us） | register value | — | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 3151 | — | unknown | Us Tou Slot Table | SameasTime1 （us） | register value | — | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 3152 | — | unknown | Us Tou Slot Table | SameasTime1 （us） | register value | — | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 3153 | — | unknown | Us Tou Slot Table | SameasTime1 （us） | register value | — | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 3154 | — | unknown | Us Tou Slot Table | SameasTime1 （us） | register value | — | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 3155 | — | unknown | Us Tou Slot Table | SameasTime1 （us） | register value | — | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 3156 | — | unknown | Us Tou Slot Table | SameasTime1 （us） | register value | — | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 3157 | — | unknown | Us Tou Slot Table | SameasTime1 （us） | register value | — | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 3158 | — | unknown | Us Tou Slot Table | SameasTime1 （us） | register value | — | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 3159 | — | unknown | Us Tou Slot Table | SameasTime1 （us） | register value | — | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 3160 | — | unknown | Us Tou Slot Table | SameasTime1 （us） | register value | — | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 3161 | — | unknown | Us Tou Slot Table | SameasTime1 （us） | register value | — | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 3162 | — | unknown | Us Tou Slot Table | SameasTime1 （us） | register value | — | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 3163 | — | unknown | Us Tou Slot Table | SameasTime1 （us） | register value | — | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 3164 | — | unknown | Us Tou Slot Table | SameasTime1 （us） | register value | — | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 3165 | — | unknown | Us Tou Slot Table | SameasTime1 （us） | register value | — | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 3166 | — | unknown | Us Tou Slot Table | SameasTime1 （us） | register value | — | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 3167 | — | unknown | Us Tou Slot Table | SameasTime1 （us） | register value | — | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 3168 | — | unknown | Us Tou Slot Table | SameasTime1 （us） | register value | — | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 3169 | — | unknown | Us Tou Slot Table | SameasTime1 （us） | register value | — | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 3170 | — | unknown | Us Tou Slot Table | SameasTime1 （us） | register value | — | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 3171 | — | unknown | Us Tou Slot Table | SameasTime1 （us） | register value | — | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 3172 | — | unknown | Us Tou Slot Table | SameasTime1 （us） | register value | — | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 3173 | — | unknown | Us Tou Slot Table | SameasTime1 （us） | register value | — | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 3174 | — | unknown | Us Tou Slot Table | SameasTime1 （us） | register value | — | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 3175 | — | unknown | Us Tou Slot Table | SameasTime1 （us） | register value | — | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 3176 | — | unknown | Us Tou Slot Table | SameasTime1 （us） | register value | — | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 3177 | — | unknown | Us Tou Slot Table | SameasTime1 （us） | register value | — | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 3178 | — | unknown | Us Tou Slot Table | SameasTime1 （us） | register value | — | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 3179 | — | unknown | Us Tou Slot Table | SameasTime1 （us） | register value | — | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 3180 | — | unknown | Us Tou Slot Table | SameasTime1 （us） | register value | — | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 3181 | — | unknown | Us Tou Slot Table | SameasTime1 （us） | register value | — | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 3182 | — | unknown | Us Tou Slot Table | SameasTime1 （us） | register value | — | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 3183 | — | unknown | Us Tou Slot Table | SameasTime1 （us） | register value | — | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 3184 | — | unknown | Us Tou Slot Table | SameasTime1 （us） | register value | — | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 3185 | — | unknown | Us Tou Slot Table | SameasTime1 （us） | register value | — | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 3186 | — | unknown | Us Tou Slot Table | SameasTime1 （us） | register value | — | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 3187 | — | unknown | Us Tou Slot Table | SameasTime1 （us） | register value | — | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 3188 | — | unknown | Us Tou Slot Table | SameasTime1 （us） | register value | — | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 3189 | — | unknown | Us Tou Slot Table | SameasTime1 （us） | register value | — | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 3190 | — | unknown | Us Tou Slot Table | SameasTime1 （us） | register value | — | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 3191 | — | unknown | Us Tou Slot Table | SameasTime1 （us） | register value | — | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 3192 | — | unknown | Us Tou Slot Table | SameasTime1 （us） | register value | — | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 3193 | — | unknown | Us Tou Slot Table | SameasTime1 （us） | register value | — | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 3194 | — | unknown | Us Tou Slot Table | SameasTime1 （us） | register value | — | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 3195 | — | unknown | Us Tou Slot Table | SameasTime1 （us） | register value | — | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 3196 | — | unknown | Us Tou Slot Table | SameasTime1 （us） | register value | — | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 3197 | — | unknown | Us Tou Slot Table | SameasTime1 （us） | register value | — | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 3198 | — | unknown | Us Tou Slot Table | SameasTime1 （us） | register value | — | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 3199 | — | unknown | Us Tou Slot Table | SameasTime1 （us） | register value | — | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 3200 | — | unknown | Us Tou Slot Table | SameasTime1 （us） | register value | — | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 3201 | — | unknown | Us Tou Special Day 1 | bit0~7:day； bit8~14:month bit15， 0：disable1： enable | register value | — | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 3202 | — | unknown | Us Tou Special Day 1 | bit0~6:min； bit7~11:hour； bit12~14, 0:loadfirst; 1:batfirst； 2:gridfirst； 3:anti-reflux bit15, 0:disable; 1:enable; | register value | — | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 3203 | — | unknown | Us Tou Special Day 1 | bit0~6:min； bit7~11:hour； bit12~15：reserve | register value | — | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 3204 | — | unknown | Us Tou Special Day 1 | Sameas SpecialDay1_Time 1 | register value | — | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 3205 | — | unknown | Us Tou Special Day 1 | Sameas SpecialDay1_Time 1 | register value | — | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 3206 | — | unknown | Us Tou Special Day 1 | Sameas SpecialDay1_Time 1 | register value | — | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 3207 | — | unknown | Us Tou Special Day 1 | Sameas SpecialDay1_Time 1 | register value | — | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 3208 | — | unknown | Us Tou Special Day 1 | Sameas SpecialDay1_Time 1 | register value | — | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 3209 | — | unknown | Us Tou Special Day 1 | Sameas SpecialDay1_Time 1 | register value | — | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 3210 | — | unknown | Us Tou Special Day 1 | Sameas SpecialDay1_Time 1 | register value | — | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 3211 | — | unknown | Us Tou Special Day 1 | Sameas SpecialDay1_Time 1 | register value | — | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 3212 | — | unknown | Us Tou Special Day 1 | Sameas SpecialDay1_Time 1 | register value | — | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 3213 | — | unknown | Us Tou Special Day 1 | Sameas SpecialDay1_Time 1 | register value | — | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 3214 | — | unknown | Us Tou Special Day 1 | Sameas SpecialDay1_Time 1 | register value | — | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 3215 | — | unknown | Us Tou Special Day 1 | Sameas SpecialDay1_Time 1 | register value | — | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 3216 | — | unknown | Us Tou Special Day 1 | Sameas SpecialDay1_Time 1 | register value | — | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 3217 | — | unknown | Us Tou Special Day 1 | Sameas SpecialDay1_Time 1 | register value | — | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 3218 | — | unknown | Us Tou Special Day 1 | Sameas SpecialDay1_Time 1 | register value | — | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 3219 | — | unknown | Us Tou Special Day 1 | Sameas SpecialDay1_Time 1 | register value | — | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 3220 | — | unknown | Us Tou Special Day 2 | bit0~7:day； bit8~14:month bit15， 0：disable 1：enable | register value | — | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 3221 | — | unknown | Us Tou Special Day 2 | bit0~6:min； bit7~11:hour； bit12~14, 0:loadfirst; 1:batfirst； 2:gridfirst； 3:anti-reflux bit15, 0:disable; 1:enable; | register value | — | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 3222 | — | unknown | Us Tou Special Day 2 | bit0~6:min； bit7~11:hour； bit12~15：reserve | register value | — | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 3223 | — | unknown | Us Tou Special Day 2 | Sameas SpecialDay2_Time 1 | register value | — | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 3224 | — | unknown | Us Tou Special Day 2 | Sameas SpecialDay2_Time 1 | register value | — | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 3225 | — | unknown | Us Tou Special Day 2 | Sameas SpecialDay2_Time 1 | register value | — | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 3226 | — | unknown | Us Tou Special Day 2 | Sameas SpecialDay2_Time 1 | register value | — | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 3227 | — | unknown | Us Tou Special Day 2 | Sameas SpecialDay2_Time 1 | register value | — | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 3228 | — | unknown | Us Tou Special Day 2 | Sameas SpecialDay2_Time 1 | register value | — | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 3229 | — | unknown | Us Tou Special Day 2 | Sameas SpecialDay2_Time 1 | register value | — | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 3230 | — | unknown | Us Tou Special Day 2 | Sameas SpecialDay2_Time 1 | register value | — | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 3231 | — | unknown | Us Tou Special Day 2 | Sameas SpecialDay2_Time 1 | register value | — | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 3232 | — | unknown | Us Tou Special Day 2 | Sameas SpecialDay2_Time 1 | register value | — | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 3233 | — | unknown | Us Tou Special Day 2 | Sameas SpecialDay2_Time 1 | register value | — | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 3234 | — | unknown | Us Tou Special Day 2 | Sameas SpecialDay2_Time 1 | register value | — | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 3235 | — | unknown | Us Tou Special Day 2 | Sameas SpecialDay2_Time 1 | register value | — | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 3236 | — | unknown | Us Tou Special Day 2 | Sameas SpecialDay2_Time 1 | register value | — | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 3237 | — | unknown | Us Tou Special Day 2 | Sameas SpecialDay2_Time 1 | register value | — | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 3238 | — | unknown | Us Tou Special Day 2 | Sameas SpecialDay2_Time 1 | register value | — | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 3239 | — | unknown | Us Tou Reserved Block | Vendor documentation marks these addresses as reserved; observed values remain zero on known firmware. | register value | — | R/W | UNKNOWN_RESERVED | source_claim | ;  |
| holding | 3240 | — | unknown | Us Tou Reserved Block | Vendor documentation marks these addresses as reserved; observed values remain zero on known firmware. | register value | — | R/W | UNKNOWN_RESERVED | source_claim | ;  |
| holding | 3241 | — | unknown | Us Tou Reserved Block | Vendor documentation marks these addresses as reserved; observed values remain zero on known firmware. | register value | — | R/W | UNKNOWN_RESERVED | source_claim | ;  |
| holding | 3242 | — | unknown | Us Tou Reserved Block | Vendor documentation marks these addresses as reserved; observed values remain zero on known firmware. | register value | — | R/W | UNKNOWN_RESERVED | source_claim | ;  |
| holding | 3243 | — | unknown | Us Tou Reserved Block | Vendor documentation marks these addresses as reserved; observed values remain zero on known firmware. | register value | — | R/W | UNKNOWN_RESERVED | source_claim | ;  |
| holding | 3244 | — | unknown | Us Tou Reserved Block | Vendor documentation marks these addresses as reserved; observed values remain zero on known firmware. | register value | — | R/W | UNKNOWN_RESERVED | source_claim | ;  |
| holding | 3245 | — | unknown | Us Tou Reserved Block | Vendor documentation marks these addresses as reserved; observed values remain zero on known firmware. | register value | — | R/W | UNKNOWN_RESERVED | source_claim | ;  |
| holding | 3246 | — | unknown | Us Tou Reserved Block | Vendor documentation marks these addresses as reserved; observed values remain zero on known firmware. | register value | — | R/W | UNKNOWN_RESERVED | source_claim | ;  |
| holding | 3247 | — | unknown | Us Tou Reserved Block | Vendor documentation marks these addresses as reserved; observed values remain zero on known firmware. | register value | — | R/W | UNKNOWN_RESERVED | source_claim | ;  |
| holding | 3248 | — | unknown | Us Tou Reserved Block | Vendor documentation marks these addresses as reserved; observed values remain zero on known firmware. | register value | — | R/W | UNKNOWN_RESERVED | source_claim | ;  |
| holding | 3249 | — | unknown | Us Tou Reserved Block | Vendor documentation marks these addresses as reserved; observed values remain zero on known firmware. | register value | — | R/W | UNKNOWN_RESERVED | source_claim | ;  |
| holding | 5000 | — | unknown | Bdc Slot 1 Metadata | Repeat for additional BDCs at 40-register strides (5040-5079, 5080-5119, ). Stored as `bdc_metadata_block`. | register value | — | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 5001 | — | unknown | Bdc Slot 1 Metadata | Repeat for additional BDCs at 40-register strides (5040-5079, 5080-5119, ). Stored as `bdc_metadata_block`. | register value | — | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 5002 | — | unknown | Bdc Slot 1 Metadata | Repeat for additional BDCs at 40-register strides (5040-5079, 5080-5119, ). Stored as `bdc_metadata_block`. | register value | — | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 5003 | — | unknown | Bdc Slot 1 Metadata | Repeat for additional BDCs at 40-register strides (5040-5079, 5080-5119, ). Stored as `bdc_metadata_block`. | register value | — | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 5004 | — | unknown | Bdc Slot 1 Metadata | Repeat for additional BDCs at 40-register strides (5040-5079, 5080-5119, ). Stored as `bdc_metadata_block`. | register value | — | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 5005 | — | unknown | Bdc Slot 1 Metadata | Repeat for additional BDCs at 40-register strides (5040-5079, 5080-5119, ). Stored as `bdc_metadata_block`. | register value | — | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 5006 | — | unknown | Bdc Slot 1 Metadata | Repeat for additional BDCs at 40-register strides (5040-5079, 5080-5119, ). Stored as `bdc_metadata_block`. | register value | — | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 5007 | — | unknown | Bdc Slot 1 Metadata | Repeat for additional BDCs at 40-register strides (5040-5079, 5080-5119, ). Stored as `bdc_metadata_block`. | register value | — | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 5008 | — | unknown | Bdc Slot 1 Metadata | Repeat for additional BDCs at 40-register strides (5040-5079, 5080-5119, ). Stored as `bdc_metadata_block`. | register value | — | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 5009 | — | unknown | Bdc Slot 1 Metadata | Repeat for additional BDCs at 40-register strides (5040-5079, 5080-5119, ). Stored as `bdc_metadata_block`. | register value | — | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 5010 | — | unknown | Bdc Slot 1 Metadata | Repeat for additional BDCs at 40-register strides (5040-5079, 5080-5119, ). Stored as `bdc_metadata_block`. | register value | — | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 5011 | — | unknown | Bdc Slot 1 Metadata | Repeat for additional BDCs at 40-register strides (5040-5079, 5080-5119, ). Stored as `bdc_metadata_block`. | register value | — | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 5012 | — | unknown | Bdc Slot 1 Metadata | Repeat for additional BDCs at 40-register strides (5040-5079, 5080-5119, ). Stored as `bdc_metadata_block`. | register value | — | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 5013 | — | unknown | Bdc Slot 1 Metadata | Repeat for additional BDCs at 40-register strides (5040-5079, 5080-5119, ). Stored as `bdc_metadata_block`. | register value | — | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 5014 | — | unknown | Bdc Slot 1 Metadata | Repeat for additional BDCs at 40-register strides (5040-5079, 5080-5119, ). Stored as `bdc_metadata_block`. | register value | — | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 5015 | — | unknown | Bdc Slot 1 Metadata | Repeat for additional BDCs at 40-register strides (5040-5079, 5080-5119, ). Stored as `bdc_metadata_block`. | register value | — | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 5016 | — | unknown | Bdc Slot 1 Metadata | Repeat for additional BDCs at 40-register strides (5040-5079, 5080-5119, ). Stored as `bdc_metadata_block`. | register value | — | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 5017 | — | unknown | Bdc Slot 1 Metadata | Repeat for additional BDCs at 40-register strides (5040-5079, 5080-5119, ). Stored as `bdc_metadata_block`. | register value | — | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 5018 | — | unknown | Bdc Slot 1 Metadata | Repeat for additional BDCs at 40-register strides (5040-5079, 5080-5119, ). Stored as `bdc_metadata_block`. | register value | — | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 5019 | — | unknown | Bdc Slot 1 Metadata | Repeat for additional BDCs at 40-register strides (5040-5079, 5080-5119, ). Stored as `bdc_metadata_block`. | register value | — | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 5020 | — | unknown | Bdc Slot 1 Metadata | Repeat for additional BDCs at 40-register strides (5040-5079, 5080-5119, ). Stored as `bdc_metadata_block`. | register value | — | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 5021 | — | unknown | Bdc Slot 1 Metadata | Repeat for additional BDCs at 40-register strides (5040-5079, 5080-5119, ). Stored as `bdc_metadata_block`. | register value | — | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 5022 | — | unknown | Bdc Slot 1 Metadata | Repeat for additional BDCs at 40-register strides (5040-5079, 5080-5119, ). Stored as `bdc_metadata_block`. | register value | — | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 5023 | — | unknown | Bdc Slot 1 Metadata | Repeat for additional BDCs at 40-register strides (5040-5079, 5080-5119, ). Stored as `bdc_metadata_block`. | register value | — | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 5024 | — | unknown | Bdc Slot 1 Metadata | Repeat for additional BDCs at 40-register strides (5040-5079, 5080-5119, ). Stored as `bdc_metadata_block`. | register value | — | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 5025 | — | unknown | Bdc Slot 1 Metadata | Repeat for additional BDCs at 40-register strides (5040-5079, 5080-5119, ). Stored as `bdc_metadata_block`. | register value | — | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 5026 | — | unknown | Bdc Slot 1 Metadata | Repeat for additional BDCs at 40-register strides (5040-5079, 5080-5119, ). Stored as `bdc_metadata_block`. | register value | — | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 5027 | — | unknown | Bdc Slot 1 Metadata | Repeat for additional BDCs at 40-register strides (5040-5079, 5080-5119, ). Stored as `bdc_metadata_block`. | register value | — | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 5028 | — | unknown | Bdc Slot 1 Metadata | Repeat for additional BDCs at 40-register strides (5040-5079, 5080-5119, ). Stored as `bdc_metadata_block`. | register value | — | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 5029 | — | unknown | Bdc Slot 1 Metadata | Repeat for additional BDCs at 40-register strides (5040-5079, 5080-5119, ). Stored as `bdc_metadata_block`. | register value | — | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 5030 | — | unknown | Bdc Slot 1 Metadata | Repeat for additional BDCs at 40-register strides (5040-5079, 5080-5119, ). Stored as `bdc_metadata_block`. | register value | — | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 5031 | — | unknown | Bdc Slot 1 Metadata | Repeat for additional BDCs at 40-register strides (5040-5079, 5080-5119, ). Stored as `bdc_metadata_block`. | register value | — | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 5032 | — | unknown | Bdc Slot 1 Metadata | Repeat for additional BDCs at 40-register strides (5040-5079, 5080-5119, ). Stored as `bdc_metadata_block`. | register value | — | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 5033 | — | unknown | Bdc Slot 1 Metadata | Repeat for additional BDCs at 40-register strides (5040-5079, 5080-5119, ). Stored as `bdc_metadata_block`. | register value | — | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 5034 | — | unknown | Bdc Slot 1 Metadata | Repeat for additional BDCs at 40-register strides (5040-5079, 5080-5119, ). Stored as `bdc_metadata_block`. | register value | — | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 5035 | — | unknown | Bdc Slot 1 Metadata | Repeat for additional BDCs at 40-register strides (5040-5079, 5080-5119, ). Stored as `bdc_metadata_block`. | register value | — | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 5036 | — | unknown | Bdc Slot 1 Metadata | Repeat for additional BDCs at 40-register strides (5040-5079, 5080-5119, ). Stored as `bdc_metadata_block`. | register value | — | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 5037 | — | unknown | Bdc Slot 1 Metadata | Repeat for additional BDCs at 40-register strides (5040-5079, 5080-5119, ). Stored as `bdc_metadata_block`. | register value | — | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 5038 | — | unknown | Bdc Slot 1 Metadata | Repeat for additional BDCs at 40-register strides (5040-5079, 5080-5119, ). Stored as `bdc_metadata_block`. | register value | — | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 5039 | — | unknown | Bdc Slot 1 Metadata | Repeat for additional BDCs at 40-register strides (5040-5079, 5080-5119, ). Stored as `bdc_metadata_block`. | register value | — | R/W | SOURCE_ONLY | source_claim | ;  |
| input | 0 | inverter_status | alternate | Inverter status | InverterStatus | register value; /10 | — | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ; alternates: register:min_tl_xh:input:3000 |
| input | 1 | pv_total_power | alternate | PV input power | PpvH | register value; /10 | 0.1W | R/W | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ; alternates: register:min_tl_xh:input:2, register:min_tl_xh:input:5, register:min_tl_xh:input:6, register:min_tl_xh:input:9, register:min_tl_xh:input:10, register:min_tl_xh:input:13, register:min_tl_xh:input:14, register:min_tl_xh:input:17, register:min_tl_xh:input:18, register:min_tl_xh:input:21, register:min_tl_xh:input:22, register:min_tl_xh:input:25, register:min_tl_xh:input:26, register:min_tl_xh:input:29, register:min_tl_xh:input:30, register:min_tl_xh:input:33, register:min_tl_xh:input:34, register:min_tl_xh:input:3001 |
| input | 2 | pv_total_power | alternate | PV input power | PpvL | register value; /10 | 0.1W | R/W | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ; alternates: register:min_tl_xh:input:1, register:min_tl_xh:input:5, register:min_tl_xh:input:6, register:min_tl_xh:input:9, register:min_tl_xh:input:10, register:min_tl_xh:input:13, register:min_tl_xh:input:14, register:min_tl_xh:input:17, register:min_tl_xh:input:18, register:min_tl_xh:input:21, register:min_tl_xh:input:22, register:min_tl_xh:input:25, register:min_tl_xh:input:26, register:min_tl_xh:input:29, register:min_tl_xh:input:30, register:min_tl_xh:input:33, register:min_tl_xh:input:34, register:min_tl_xh:input:3001 |
| input | 3 | — | unknown | PV1 DC voltage | Vpv1 | register value; /10 | 0.1V | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 4 | — | unknown | PV1 DC current | PV1Curr | register value; /10 | 0.1A | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 5 | pv_total_power | alternate | PV1 DC power | Ppv1H | register value; /10 | 0.1W | R/W | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ; alternates: register:min_tl_xh:input:1, register:min_tl_xh:input:2, register:min_tl_xh:input:6, register:min_tl_xh:input:9, register:min_tl_xh:input:10, register:min_tl_xh:input:13, register:min_tl_xh:input:14, register:min_tl_xh:input:17, register:min_tl_xh:input:18, register:min_tl_xh:input:21, register:min_tl_xh:input:22, register:min_tl_xh:input:25, register:min_tl_xh:input:26, register:min_tl_xh:input:29, register:min_tl_xh:input:30, register:min_tl_xh:input:33, register:min_tl_xh:input:34, register:min_tl_xh:input:3001 |
| input | 6 | pv_total_power | alternate | PV1 DC power | Ppv1L | register value; /10 | 0.1W | R/W | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ; alternates: register:min_tl_xh:input:1, register:min_tl_xh:input:2, register:min_tl_xh:input:5, register:min_tl_xh:input:9, register:min_tl_xh:input:10, register:min_tl_xh:input:13, register:min_tl_xh:input:14, register:min_tl_xh:input:17, register:min_tl_xh:input:18, register:min_tl_xh:input:21, register:min_tl_xh:input:22, register:min_tl_xh:input:25, register:min_tl_xh:input:26, register:min_tl_xh:input:29, register:min_tl_xh:input:30, register:min_tl_xh:input:33, register:min_tl_xh:input:34, register:min_tl_xh:input:3001 |
| input | 7 | — | unknown | PV2 DC voltage | Vpv2 | register value; /10 | 0.1V | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 8 | — | unknown | PV2 DC current | PV2Curr | register value; /10 | 0.1A | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 9 | pv_total_power | alternate | PV2 DC power | Ppv2H | register value; /10 | 0.1W | R/W | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ; alternates: register:min_tl_xh:input:1, register:min_tl_xh:input:2, register:min_tl_xh:input:5, register:min_tl_xh:input:6, register:min_tl_xh:input:10, register:min_tl_xh:input:13, register:min_tl_xh:input:14, register:min_tl_xh:input:17, register:min_tl_xh:input:18, register:min_tl_xh:input:21, register:min_tl_xh:input:22, register:min_tl_xh:input:25, register:min_tl_xh:input:26, register:min_tl_xh:input:29, register:min_tl_xh:input:30, register:min_tl_xh:input:33, register:min_tl_xh:input:34, register:min_tl_xh:input:3001 |
| input | 10 | pv_total_power | alternate | PV2 DC power | Ppv2L | register value; /10 | 0.1W | R/W | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ; alternates: register:min_tl_xh:input:1, register:min_tl_xh:input:2, register:min_tl_xh:input:5, register:min_tl_xh:input:6, register:min_tl_xh:input:9, register:min_tl_xh:input:13, register:min_tl_xh:input:14, register:min_tl_xh:input:17, register:min_tl_xh:input:18, register:min_tl_xh:input:21, register:min_tl_xh:input:22, register:min_tl_xh:input:25, register:min_tl_xh:input:26, register:min_tl_xh:input:29, register:min_tl_xh:input:30, register:min_tl_xh:input:33, register:min_tl_xh:input:34, register:min_tl_xh:input:3001 |
| input | 11 | — | unknown | PV3 DC voltage | Vpv3 | register value; /10 | 0.1V | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 12 | — | unknown | PV3 DC current | PV3Curr | register value; /10 | 0.1A | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 13 | pv_total_power | alternate | PV3 DC power | Ppv3H | register value; /10 | 0.1W | R/W | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ; alternates: register:min_tl_xh:input:1, register:min_tl_xh:input:2, register:min_tl_xh:input:5, register:min_tl_xh:input:6, register:min_tl_xh:input:9, register:min_tl_xh:input:10, register:min_tl_xh:input:14, register:min_tl_xh:input:17, register:min_tl_xh:input:18, register:min_tl_xh:input:21, register:min_tl_xh:input:22, register:min_tl_xh:input:25, register:min_tl_xh:input:26, register:min_tl_xh:input:29, register:min_tl_xh:input:30, register:min_tl_xh:input:33, register:min_tl_xh:input:34, register:min_tl_xh:input:3001 |
| input | 14 | pv_total_power | alternate | PV3 DC power | Ppv3L | register value; /10 | 0.1W | R/W | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ; alternates: register:min_tl_xh:input:1, register:min_tl_xh:input:2, register:min_tl_xh:input:5, register:min_tl_xh:input:6, register:min_tl_xh:input:9, register:min_tl_xh:input:10, register:min_tl_xh:input:13, register:min_tl_xh:input:17, register:min_tl_xh:input:18, register:min_tl_xh:input:21, register:min_tl_xh:input:22, register:min_tl_xh:input:25, register:min_tl_xh:input:26, register:min_tl_xh:input:29, register:min_tl_xh:input:30, register:min_tl_xh:input:33, register:min_tl_xh:input:34, register:min_tl_xh:input:3001 |
| input | 15 | — | unknown | PV4 DC voltage | Vpv4 | register value; /10 | 0.1V | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 16 | — | unknown | PV4 DC current | PV4Curr | register value; /10 | 0.1A | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 17 | pv_total_power | alternate | PV4 DC power | Ppv4H | register value; /10 | 0.1W | R/W | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ; alternates: register:min_tl_xh:input:1, register:min_tl_xh:input:2, register:min_tl_xh:input:5, register:min_tl_xh:input:6, register:min_tl_xh:input:9, register:min_tl_xh:input:10, register:min_tl_xh:input:13, register:min_tl_xh:input:14, register:min_tl_xh:input:18, register:min_tl_xh:input:21, register:min_tl_xh:input:22, register:min_tl_xh:input:25, register:min_tl_xh:input:26, register:min_tl_xh:input:29, register:min_tl_xh:input:30, register:min_tl_xh:input:33, register:min_tl_xh:input:34, register:min_tl_xh:input:3001 |
| input | 18 | pv_total_power | alternate | PV4 DC power | Ppv4L | register value; /10 | 0.1W | R/W | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ; alternates: register:min_tl_xh:input:1, register:min_tl_xh:input:2, register:min_tl_xh:input:5, register:min_tl_xh:input:6, register:min_tl_xh:input:9, register:min_tl_xh:input:10, register:min_tl_xh:input:13, register:min_tl_xh:input:14, register:min_tl_xh:input:17, register:min_tl_xh:input:21, register:min_tl_xh:input:22, register:min_tl_xh:input:25, register:min_tl_xh:input:26, register:min_tl_xh:input:29, register:min_tl_xh:input:30, register:min_tl_xh:input:33, register:min_tl_xh:input:34, register:min_tl_xh:input:3001 |
| input | 19 | — | unknown | PV5 DC voltage | Vpv5 | register value; /10 | 0.1V | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 20 | — | unknown | PV5 DC current | PV5Curr | register value; /10 | 0.1A | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 21 | pv_total_power | alternate | PV5 DC power | Ppv5H | register value; /10 | 0.1W | R/W | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ; alternates: register:min_tl_xh:input:1, register:min_tl_xh:input:2, register:min_tl_xh:input:5, register:min_tl_xh:input:6, register:min_tl_xh:input:9, register:min_tl_xh:input:10, register:min_tl_xh:input:13, register:min_tl_xh:input:14, register:min_tl_xh:input:17, register:min_tl_xh:input:18, register:min_tl_xh:input:22, register:min_tl_xh:input:25, register:min_tl_xh:input:26, register:min_tl_xh:input:29, register:min_tl_xh:input:30, register:min_tl_xh:input:33, register:min_tl_xh:input:34, register:min_tl_xh:input:3001 |
| input | 22 | pv_total_power | alternate | PV5 DC power | Ppv5L | register value; /10 | 0.1W | R/W | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ; alternates: register:min_tl_xh:input:1, register:min_tl_xh:input:2, register:min_tl_xh:input:5, register:min_tl_xh:input:6, register:min_tl_xh:input:9, register:min_tl_xh:input:10, register:min_tl_xh:input:13, register:min_tl_xh:input:14, register:min_tl_xh:input:17, register:min_tl_xh:input:18, register:min_tl_xh:input:21, register:min_tl_xh:input:25, register:min_tl_xh:input:26, register:min_tl_xh:input:29, register:min_tl_xh:input:30, register:min_tl_xh:input:33, register:min_tl_xh:input:34, register:min_tl_xh:input:3001 |
| input | 23 | — | unknown | PV6 DC voltage | Vpv6 | register value; /10 | 0.1V | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 24 | — | unknown | PV6 DC current | PV6Curr | register value; /10 | 0.1A | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 25 | pv_total_power | alternate | PV6 DC power | PV6inputpower(high) | register value; /10 | W | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ; alternates: register:min_tl_xh:input:1, register:min_tl_xh:input:2, register:min_tl_xh:input:5, register:min_tl_xh:input:6, register:min_tl_xh:input:9, register:min_tl_xh:input:10, register:min_tl_xh:input:13, register:min_tl_xh:input:14, register:min_tl_xh:input:17, register:min_tl_xh:input:18, register:min_tl_xh:input:21, register:min_tl_xh:input:22, register:min_tl_xh:input:26, register:min_tl_xh:input:29, register:min_tl_xh:input:30, register:min_tl_xh:input:33, register:min_tl_xh:input:34, register:min_tl_xh:input:3001 |
| input | 26 | pv_total_power | alternate | PV6 DC power | PV6inputpower(low) | register value; /10 | W | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ; alternates: register:min_tl_xh:input:1, register:min_tl_xh:input:2, register:min_tl_xh:input:5, register:min_tl_xh:input:6, register:min_tl_xh:input:9, register:min_tl_xh:input:10, register:min_tl_xh:input:13, register:min_tl_xh:input:14, register:min_tl_xh:input:17, register:min_tl_xh:input:18, register:min_tl_xh:input:21, register:min_tl_xh:input:22, register:min_tl_xh:input:25, register:min_tl_xh:input:29, register:min_tl_xh:input:30, register:min_tl_xh:input:33, register:min_tl_xh:input:34, register:min_tl_xh:input:3001 |
| input | 27 | — | unknown | PV7 DC voltage | PV7voltage | register value; /10 | V | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 28 | — | unknown | PV7 DC current | PV7inputcurrent | register value; /10 | A | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 29 | pv_total_power | alternate | PV7 DC power | PV7inputpower(high) | register value; /10 | W | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ; alternates: register:min_tl_xh:input:1, register:min_tl_xh:input:2, register:min_tl_xh:input:5, register:min_tl_xh:input:6, register:min_tl_xh:input:9, register:min_tl_xh:input:10, register:min_tl_xh:input:13, register:min_tl_xh:input:14, register:min_tl_xh:input:17, register:min_tl_xh:input:18, register:min_tl_xh:input:21, register:min_tl_xh:input:22, register:min_tl_xh:input:25, register:min_tl_xh:input:26, register:min_tl_xh:input:30, register:min_tl_xh:input:33, register:min_tl_xh:input:34, register:min_tl_xh:input:3001 |
| input | 30 | pv_total_power | alternate | PV7 DC power | PV7inputpower(low) | register value; /10 | W | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ; alternates: register:min_tl_xh:input:1, register:min_tl_xh:input:2, register:min_tl_xh:input:5, register:min_tl_xh:input:6, register:min_tl_xh:input:9, register:min_tl_xh:input:10, register:min_tl_xh:input:13, register:min_tl_xh:input:14, register:min_tl_xh:input:17, register:min_tl_xh:input:18, register:min_tl_xh:input:21, register:min_tl_xh:input:22, register:min_tl_xh:input:25, register:min_tl_xh:input:26, register:min_tl_xh:input:29, register:min_tl_xh:input:33, register:min_tl_xh:input:34, register:min_tl_xh:input:3001 |
| input | 31 | — | unknown | PV8 DC voltage | PV8voltage | register value; /10 | V | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 32 | — | unknown | PV8 DC current | PV8inputcurrent | register value; /10 | A | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 33 | pv_total_power | alternate | PV8 DC power | PV8inputpower(high) | register value; /10 | W | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ; alternates: register:min_tl_xh:input:1, register:min_tl_xh:input:2, register:min_tl_xh:input:5, register:min_tl_xh:input:6, register:min_tl_xh:input:9, register:min_tl_xh:input:10, register:min_tl_xh:input:13, register:min_tl_xh:input:14, register:min_tl_xh:input:17, register:min_tl_xh:input:18, register:min_tl_xh:input:21, register:min_tl_xh:input:22, register:min_tl_xh:input:25, register:min_tl_xh:input:26, register:min_tl_xh:input:29, register:min_tl_xh:input:30, register:min_tl_xh:input:34, register:min_tl_xh:input:3001 |
| input | 34 | pv_total_power | alternate | PV8 DC power | PV8inputpower(low) | register value; /10 | W | R | RESOLVED | semantic_correlated, source_claim | ; alternates: register:min_tl_xh:input:1, register:min_tl_xh:input:2, register:min_tl_xh:input:5, register:min_tl_xh:input:6, register:min_tl_xh:input:9, register:min_tl_xh:input:10, register:min_tl_xh:input:13, register:min_tl_xh:input:14, register:min_tl_xh:input:17, register:min_tl_xh:input:18, register:min_tl_xh:input:21, register:min_tl_xh:input:22, register:min_tl_xh:input:25, register:min_tl_xh:input:26, register:min_tl_xh:input:29, register:min_tl_xh:input:30, register:min_tl_xh:input:33, register:min_tl_xh:input:3001 |
| input | 35 | — | unknown | AC output power | Outputpower(high) | register value; /10 | W | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 36 | — | unknown | AC output power | Outputpower(low) | register value; /10 | W | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 37 | grid_frequency | alternate | Grid frequency | Gridfrequency | register value; /100 | Hz | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ; alternates: register:min_tl_xh:holding:62, register:min_tl_xh:holding:63, register:min_tl_xh:holding:72, register:min_tl_xh:holding:73, register:min_tl_xh:holding:74, register:min_tl_xh:holding:75, register:min_tl_xh:holding:78, register:min_tl_xh:holding:79, register:min_tl_xh:input:3025 |
| input | 38 | — | unknown | AC phase L1 voltage | Three/singlephasegridvoltage | register value; /10 | V | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 39 | — | unknown | AC phase L1 current | Three/singlephasegridoutputcurrent | register value; /10 | A | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 40 | — | unknown | AC phase L1 power | Three/single phase grid output watt VA(high) | register value; /10 | W | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 41 | — | unknown | AC phase L1 power | Three/single phase grid output watt VA(low) | register value; /10 | W | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 42 | — | unknown | AC phase L2 voltage | Threephasegridvoltage | register value; /10 | V | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 43 | — | unknown | AC phase L2 current | Threephasegridoutputcurrent | register value; /10 | A | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 44 | — | unknown | AC phase L2 power | Threephasegridoutputpower(high) | register value; /10 | W | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 45 | — | unknown | AC phase L2 power | Threephasegridoutputpower(low) | register value; /10 | W | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 46 | — | unknown | AC phase L3 voltage | Threephasegridvoltage | register value; /10 | V | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 47 | — | unknown | AC phase L3 current | Threephasegridoutputcurrent | register value; /10 | A | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 48 | ac_phase_l3_power | alternate | AC phase L3 power | Threephasegridoutputpower(high) | register value; /10 | W | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ; alternates: register:min_tl_xh:input:49, register:min_tl_xh:input:3036, register:min_tl_xh:input:3037, register:min_tl_xh:input:3156, register:min_tl_xh:input:3157 |
| input | 49 | ac_phase_l3_power | alternate | AC phase L3 power | Threephasegridoutputpower(low) | register value; /10 | W | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ; alternates: register:min_tl_xh:input:48, register:min_tl_xh:input:3036, register:min_tl_xh:input:3037, register:min_tl_xh:input:3156, register:min_tl_xh:input:3157 |
| input | 53 | — | unknown | Output energy today | Todaygenerateenergy(high) | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 54 | — | unknown | Output energy today | Todaygenerateenergy(low) | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 55 | — | unknown | Output energy total | Totalgenerateenergy(high) | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 56 | — | unknown | Output energy total | Totalgenerateenergy(low) | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 57 | inverter_runtime | alternate | Run time | Raw counter counts seconds; divide by 7200 to obtain hours. | register value; /7200 | h | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ; alternates: register:min_tl_xh:input:3047 |
| input | 58 | — | unknown | Run time | Raw counter counts seconds; divide by 7200 to obtain hours. | register value; /7200 | h | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 59 | — | unknown | PV1 energy today | PV1Energytoday(high) | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 60 | — | unknown | PV1 energy today | PV1Energytoday(low) | register value; /10 | kWh | R | RESOLVED | semantic_correlated, source_claim | ;  |
| input | 61 | — | unknown | PV1 energy total | PV1Energytotal(high) | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 62 | — | unknown | PV1 energy total | PV1Energytotal(low) | register value; /10 | kWh | R | RESOLVED | semantic_correlated, source_claim | ;  |
| input | 63 | — | unknown | PV2 energy today | PV2Energytoday(high) | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 64 | — | unknown | PV2 energy today | PV2Energytoday(low) | register value; /10 | kWh | R | RESOLVED | semantic_correlated, source_claim | ;  |
| input | 65 | — | unknown | PV2 energy total | PV2Energytotal(high) | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 66 | — | unknown | PV2 energy total | PV2Energytotal(low) | register value; /10 | kWh | R | RESOLVED | semantic_correlated, source_claim | ;  |
| input | 67 | — | unknown | PV3 energy today | PV3Energytoday(high) | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 68 | — | unknown | PV3 energy today | PV3Energytoday(low) | register value; /10 | kWh | R | RESOLVED | semantic_correlated, source_claim | ;  |
| input | 69 | — | unknown | PV3 energy total | PV3Energytotal(high) | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 70 | — | unknown | PV3 energy total | PV3Energytotal(low) | register value; /10 | kWh | R | RESOLVED | semantic_correlated, source_claim | ;  |
| input | 71 | — | unknown | PV4 energy today | PV4Energytoday(high) | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 72 | — | unknown | PV4 energy today | PV4Energytoday(low) | register value; /10 | kWh | R | RESOLVED | semantic_correlated, source_claim | ;  |
| input | 73 | pv4_energy_total | alternate | PV4 energy total | PV4Energytotal(high) | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ; alternates: register:min_tl_xh:input:74, register:min_tl_xh:input:3081, register:min_tl_xh:input:3082 |
| input | 74 | pv4_energy_total | alternate | PV4 energy total | PV4Energytotal(low) | register value; /10 | kWh | R | RESOLVED | semantic_correlated, source_claim | ; alternates: register:min_tl_xh:input:73, register:min_tl_xh:input:3081, register:min_tl_xh:input:3082 |
| input | 75 | — | unknown | PV5 energy today | PV5Energytoday(high) | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 76 | — | unknown | PV5 energy today | PV5Energytoday(low) | register value; /10 | kWh | R | RESOLVED | semantic_correlated, source_claim | ;  |
| input | 77 | — | unknown | PV5 energy total | PV5Energytotal(high) | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 78 | — | unknown | PV5 energy total | PV5Energytotal(low) | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 79 | — | unknown | PV6 energy today | PV6Energytoday(high) | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 80 | — | unknown | PV6 energy today | PV6Energytoday(low) | register value; /10 | kWh | R | RESOLVED | semantic_correlated, source_claim | ;  |
| input | 81 | — | unknown | PV6 energy total | PV6Energytotal(high) | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 82 | — | unknown | PV6 energy total | PV6Energytotal(low) | register value; /10 | kWh | R | RESOLVED | semantic_correlated, source_claim | ;  |
| input | 83 | — | unknown | PV7 energy today | PV7Energytoday(high) | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 84 | — | unknown | PV7 energy today | PV7Energytoday(low) | register value; /10 | kWh | R | RESOLVED | semantic_correlated, source_claim | ;  |
| input | 85 | — | unknown | PV7 energy total | PV7Energytotal(high) | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 86 | — | unknown | PV7 energy total | PV7Energytotal(low) | register value; /10 | kWh | R | RESOLVED | semantic_correlated, source_claim | ;  |
| input | 87 | — | unknown | PV8 energy today | PV8Energytoday(high) | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 88 | — | unknown | PV8 energy today | PV8Energytoday(low) | register value; /10 | kWh | R | RESOLVED | semantic_correlated, source_claim | ;  |
| input | 89 | — | unknown | PV8 energy total | PV8Energytotal(high) | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 90 | — | unknown | PV8 energy total | PV8Energytotal(low) | register value; /10 | kWh | R | RESOLVED | semantic_correlated, source_claim | ;  |
| input | 91 | — | unknown | PV energy total | PVEnergytotal(high) | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 92 | — | unknown | PV energy total | PVEnergytotal(low) | register value; /10 | kWh | R | RESOLVED | semantic_correlated, source_claim | ;  |
| input | 93 | — | unknown | Inverter temperature | Invertertemperature | register value; /10 | °C | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 94 | — | unknown | IPM temperature | TheinsideIPMininverterTemperature | register value; /10 | °C | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 95 | — | unknown | Boost temperature | Boosttemperature | register value; /10 | °C | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 98 | — | unknown | P-bus voltage | PBusinsideVoltage | register value; /10 | V | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 99 | — | unknown | N-bus voltage | NBusinsideVoltage | register value; /10 | V | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 101 | — | unknown | Output power percentage | RealOutputpowerPercent | register value; /10 | % | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 104 | — | unknown | Derating mode | DeratingMode | register value; /10 | — | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 105 | — | unknown | Fault code | Inverterfaultmaincode | register value; /10 | — | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 110 | — | unknown | Warning code | WarningbitH | register value; /10 | — | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 111 | — | unknown | Warning code | Inverterwarnsubcode | register value; /10 | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 234 | — | unknown | Output reactive power | NominalOutputReactivePowerH | register value; /10 | var | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 235 | — | unknown | Output reactive power | NominalOutputReactivePowerL | register value; /10 | var | R | SOURCE_ONLY | source_claim | ;  |
| input | 236 | — | unknown | Reactive energy total | Reactivepowergeneration | register value; /10 | kvarh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 237 | — | unknown | Reactive energy total | Reactivepowergeneration | register value; /10 | kvarh | R | SOURCE_ONLY | source_claim | ;  |
| input | 1014 | battery_soc | legacy | SOC | StateofchargeCapacity | register value; /10 | lith/leadacid | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; Legacy/base register retained because newer TL-XH families may expose the older storage block; no MIN live read was issued for this address.; alternates: register:min_tl_xh:input:3171, register:min_tl_xh:input:3196, register:min_tl_xh:input:3197, register:min_tl_xh:input:3215 |
| input | 3000 | inverter_status | alternate | Inverter status | Inverter status | u16 enum; 1=normal | — | R | RESOLVED_WITH_NOTES | read_verified, semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ; alternates: register:min_tl_xh:input:0 |
| input | 3001 | pv_total_power | alternate | Total PV/input power | Total PV/input power | u32 / 10; /10 | W | R | RESOLVED_WITH_NOTES | read_verified, semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ; alternates: register:min_tl_xh:input:1, register:min_tl_xh:input:2, register:min_tl_xh:input:5, register:min_tl_xh:input:6, register:min_tl_xh:input:9, register:min_tl_xh:input:10, register:min_tl_xh:input:13, register:min_tl_xh:input:14, register:min_tl_xh:input:17, register:min_tl_xh:input:18, register:min_tl_xh:input:21, register:min_tl_xh:input:22, register:min_tl_xh:input:25, register:min_tl_xh:input:26, register:min_tl_xh:input:29, register:min_tl_xh:input:30, register:min_tl_xh:input:33, register:min_tl_xh:input:34 |
| input | 3002 | — | unknown | PV input power | Total PV input power summed across all strings (0.1 W resolution). | register value; /10 | W | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3003 | — | unknown | PV1 voltage | PV1 voltage | u16 / 10; /10 | V | R | RESOLVED_WITH_NOTES | read_verified, semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3004 | — | unknown | PV1 current | PV1 current | u16 / 10; /10 | A | R | RESOLVED_WITH_NOTES | read_verified, semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3005 | — | unknown | PV1 power | PV1 power | u32 / 10; /10 | W | R | RESOLVED_WITH_NOTES | read_verified, semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3006 | — | unknown | PV1 DC power | Real-time DC power from PV1 computed from voltage and current readings. | register value; /10 | W | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3007 | — | unknown | PV2 voltage | PV2 voltage | u16 / 10; /10 | V | R | RESOLVED_WITH_NOTES | read_verified, semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3008 | — | unknown | PV2 current | PV2 current | u16 / 10; /10 | A | R | RESOLVED_WITH_NOTES | read_verified, semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3009 | — | unknown | PV2 power | PV2 power | u32 / 10; /10 | W | R | RESOLVED_WITH_NOTES | read_verified, semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3010 | — | unknown | PV2 DC power | Real-time DC power from PV2 computed from voltage and current readings. | register value; /10 | W | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3011 | — | unknown | PV3 DC voltage | PV3voltage | register value; /10 | V | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3012 | — | unknown | PV3 DC current | PV3inputcurrent | register value; /10 | A | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3013 | — | unknown | PV3 DC power | PV3power | register value; /10 | W | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3014 | — | unknown | PV3 DC power | Real-time DC power from PV3 computed from voltage and current readings. | register value; /10 | W | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3015 | — | unknown | PV4 DC voltage | PV4voltage | register value; /10 | V | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3016 | — | unknown | PV4 DC current | PV4inputcurrent | register value; /10 | A | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3017 | — | unknown | PV4 DC power | PV4power | register value; /10 | W | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3018 | — | unknown | PV4 DC power | Real-time DC power from PV4 computed from voltage and current readings. | register value; /10 | W | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3019 | — | unknown | System output power | Systemoutputpower | register value; /10 | W | R | RESOLVED | semantic_correlated, source_claim | ;  |
| input | 3020 | — | unknown | System output power | AC output power reported by the TL-XH mirror block (0.1 W resolution). Mirrors the value at register 35. | register value; /10 | W | R | RESOLVED | semantic_correlated, source_claim | ;  |
| input | 3021 | — | unknown | Output reactive power | reactivepower | register value; /10 | POWER_REACTIVE | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3022 | — | unknown | Output reactive power | Instantaneous reactive power on the AC output (positive = inductive, negative = capacitive). | register value; /10 | var | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3023 | — | unknown | AC output power | AC output power | u32 / 10; /10 | W | R | RESOLVED_WITH_NOTES | read_verified, semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3024 | — | unknown | AC output power | Active AC output power delivered by the inverter (0.1 W resolution). | register value; /10 | W | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3025 | grid_frequency | alternate | Grid frequency | Grid frequency | u16 / 100; /100 | Hz | R | RESOLVED_WITH_NOTES | read_verified, semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ; alternates: register:min_tl_xh:holding:62, register:min_tl_xh:holding:63, register:min_tl_xh:holding:72, register:min_tl_xh:holding:73, register:min_tl_xh:holding:74, register:min_tl_xh:holding:75, register:min_tl_xh:holding:78, register:min_tl_xh:holding:79, register:min_tl_xh:input:37 |
| input | 3026 | — | unknown | AC phase L1 voltage | AC phase L1 voltage | u16 / 10; /10 | V | R | RESOLVED_WITH_NOTES | read_verified, semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3027 | — | unknown | AC phase L1 current | AC phase L1 current | u16 / 10; /10 | A | R | RESOLVED_WITH_NOTES | read_verified, semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3028 | — | unknown | AC phase L1 power | AC phase L1 power | u32 / 10; /10 | W | R | RESOLVED_WITH_NOTES | read_verified, semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3029 | — | unknown | AC phase L1 power | Active power exported on phase L1. | register value; /10 | W | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3030 | — | unknown | AC phase L2 voltage | Threephasegridvoltage | register value; /10 | V | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3031 | — | unknown | AC phase L2 current | Threephasegridoutputcurrent | register value; /10 | A | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3032 | — | unknown | AC phase L2 power | Threephasegridoutputpower | register value; /10 | VA | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3033 | — | unknown | AC phase L2 power | Active power exported on phase L2. | register value; /10 | W | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3034 | — | unknown | AC phase L3 voltage | Threephasegridvoltage | register value; /10 | V | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3035 | — | unknown | AC phase L3 current | Threephasegridoutputcurrent | register value; /10 | A | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3036 | ac_phase_l3_power | alternate | AC phase L3 power | Threephasegridoutputpower | register value; /10 | VA | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ; alternates: register:min_tl_xh:input:48, register:min_tl_xh:input:49, register:min_tl_xh:input:3037, register:min_tl_xh:input:3156, register:min_tl_xh:input:3157 |
| input | 3037 | ac_phase_l3_power | alternate | AC phase L3 power | Active power exported on phase L3. | register value; /10 | W | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ; alternates: register:min_tl_xh:input:48, register:min_tl_xh:input:49, register:min_tl_xh:input:3036, register:min_tl_xh:input:3156, register:min_tl_xh:input:3157 |
| input | 3038 | — | unknown | RS line voltage | Threephasegridvoltage | register value; /10 | V | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3039 | — | unknown | ST line voltage | Threephasegridvoltage | register value; /10 | V | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3040 | — | unknown | TR line voltage | Threephasegridvoltage | register value; /10 | V | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3041 | grid_import_power | supported | Power to user/grid import | Power to user/grid import | s32 / 10; /10 | W | R | RESOLVED_WITH_NOTES | read_verified, semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3042 | — | unknown | Load supply power | Real-time active power delivered to on-site (self-consumption) loads. | register value; /10 | W | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3043 | grid_export_power | alternate | Power to grid/export | Power to grid/export | s32 / 10; /10 | W | R | RESOLVED_WITH_NOTES | read_verified, semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ; alternates: register:min_tl_xh:input:3044, register:min_tl_xh:input:3071, register:min_tl_xh:input:3072, register:min_tl_xh:input:3073, register:min_tl_xh:input:3074 |
| input | 3044 | grid_export_power | alternate | Grid export power | Active power exported to the utility grid. | register value; /10 | W | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ; alternates: register:min_tl_xh:input:3043, register:min_tl_xh:input:3071, register:min_tl_xh:input:3072, register:min_tl_xh:input:3073, register:min_tl_xh:input:3074 |
| input | 3045 | house_load_power | supported | User load power | User load power | s32 / 10; /10 | W | R | RESOLVED_WITH_NOTES | read_verified, semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3046 | — | unknown | Home load power | Aggregate instantaneous demand from on-site loads. | register value; /10 | W | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3047 | inverter_runtime | alternate | Inverter runtime | Inverter runtime | u32 / 7200; /7200 | h | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ; alternates: register:min_tl_xh:input:57 |
| input | 3048 | — | unknown | Inverter runtime | Raw counter counts seconds; divide by 7200 to obtain hours. | register value; /7200 | h | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3049 | — | unknown | AC energy today | AC energy today | u32 / 10; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3050 | — | unknown | Output energy today | Energy exported to the AC output today (0.1 kWh resolution). | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3051 | — | unknown | Output energy total | Totalgenerateenergy | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3052 | — | unknown | Output energy total | Lifetime AC output energy (0.1 kWh resolution). | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3053 | — | unknown | PV energy total | PVenergytotal | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3054 | — | unknown | PV energy total | Total PV energy generated across all strings (0.1 kWh resolution). | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3055 | — | unknown | PV1 energy today | PV1energytoday | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3056 | — | unknown | PV1 energy today | Energy harvested by PV1 today. Values use 0.1 kWh resolution. | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3057 | — | unknown | PV1 energy total | PV1energytotal | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3058 | — | unknown | PV1 energy total | Lifetime energy harvested by PV1. Values use 0.1 kWh resolution. | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3059 | — | unknown | PV2 energy today | PV2energytoday | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3060 | — | unknown | PV2 energy today | Energy harvested by PV2 today. Values use 0.1 kWh resolution. | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3061 | — | unknown | PV2 energy total | PV2energytotal | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3062 | — | unknown | PV2 energy total | Lifetime energy harvested by PV2. Values use 0.1 kWh resolution. | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3063 | — | unknown | PV3 energy today | PV3energytoday | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3064 | — | unknown | PV3 energy today | Energy harvested by PV3 today. Values use 0.1 kWh resolution. | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3065 | — | unknown | PV3 energy total | PV3energytotal | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3066 | — | unknown | PV3 energy total | Lifetime energy harvested by PV3. Values use 0.1 kWh resolution. | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3067 | — | unknown | Load energy today | Todayenergytouser | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3068 | — | unknown | Load energy today | Energy delivered to on-site loads today (0.1 kWh resolution). | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3069 | — | unknown | Load energy total | Totalenergytouser | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3070 | — | unknown | Load energy total | Lifetime energy delivered to on-site loads (0.1 kWh resolution). | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3071 | grid_export_power | alternate | Export energy today | Todayenergytogrid | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ; alternates: register:min_tl_xh:input:3043, register:min_tl_xh:input:3044, register:min_tl_xh:input:3072, register:min_tl_xh:input:3073, register:min_tl_xh:input:3074 |
| input | 3072 | grid_export_power | alternate | Export energy today | Energy exported to the grid today (0.1 kWh resolution). | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ; alternates: register:min_tl_xh:input:3043, register:min_tl_xh:input:3044, register:min_tl_xh:input:3071, register:min_tl_xh:input:3073, register:min_tl_xh:input:3074 |
| input | 3073 | grid_export_power | alternate | Export energy total | Totalenergytogrid | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ; alternates: register:min_tl_xh:input:3043, register:min_tl_xh:input:3044, register:min_tl_xh:input:3071, register:min_tl_xh:input:3072, register:min_tl_xh:input:3074 |
| input | 3074 | grid_export_power | alternate | Export energy total | Lifetime energy exported to the grid (0.1 kWh resolution). | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ; alternates: register:min_tl_xh:input:3043, register:min_tl_xh:input:3044, register:min_tl_xh:input:3071, register:min_tl_xh:input:3072, register:min_tl_xh:input:3073 |
| input | 3075 | — | unknown | User load energy today | Todayenergyofuserload | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3076 | — | unknown | User load energy today | Energy delivered to on-site loads today (0.1 kWh resolution). | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3077 | — | unknown | User load energy total | Totalenergyofuserload | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3078 | — | unknown | User load energy total | Lifetime energy delivered to on-site loads (0.1 kWh resolution). | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3079 | — | unknown | PV4 energy today | PV4 energy today | u32 / 10; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3080 | — | unknown | PV4 energy today | Energy harvested by PV string 4 today (0.1 kWh resolution). | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3081 | pv4_energy_total | alternate | PV4 energy total | PV4 energy total | u32 / 10; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; FC03 3081 is UPSFreqSet; this input-space meaning is independent.; ; alternates: register:min_tl_xh:input:73, register:min_tl_xh:input:74, register:min_tl_xh:input:3082 |
| input | 3082 | pv4_energy_total | alternate | PV4 energy total | Lifetime energy harvested by PV string 4 (0.1 kWh resolution). | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ; alternates: register:min_tl_xh:input:73, register:min_tl_xh:input:74, register:min_tl_xh:input:3081 |
| input | 3083 | — | unknown | PV energy today | PVenergytoday | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3084 | — | unknown | PV energy today | Total PV energy harvested across all strings today (0.1 kWh resolution). | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3085 | — | unknown | Reserved | Reserved | register value; /1 | — | R | UNKNOWN_RESERVED | semantic_correlated, source_claim | ;  |
| input | 3086 | — | unknown | Derating mode | DeratingMode | register value; /1 | — | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3087 | — | unknown | PV insulation resistance | PVISOvalue | register value; /1 | kΩ | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3088 | — | unknown | Residual current R | RDCICurr | register value; /10 | A | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3089 | — | unknown | Residual current S | SDCICurr | register value; /10 | A | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3090 | — | unknown | Residual current T | TDCICurr | register value; /10 | A | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3091 | — | unknown | GFCI current | GFCICurr | register value; /1 | A | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3092 | — | unknown | Total bus voltage | totalbusvoltage | register value; /10 | V | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3093 | — | unknown | Inverter temperature | Invertertemperature | register value; /10 | °C | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3094 | — | unknown | IPM temperature | TheinsideIPMininvertertemperature | register value; /10 | °C | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3095 | — | unknown | Boost temperature | Boosttemperature | register value; /10 | °C | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3096 | — | unknown | Temp4 | Reserved | register value; /10 | — | R | UNKNOWN_RESERVED | semantic_correlated, source_claim | ;  |
| input | 3097 | — | unknown | Communication board temperature | Commmunicationbroadtemperature | register value; /10 | °C | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3098 | — | unknown | P-bus voltage | PBusinsideVoltage | register value; /10 | V | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3099 | — | unknown | N-bus voltage | NBusinsideVoltage | register value; /10 | V | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3100 | — | unknown | Inverter output power factor | InverteroutputPFnow | register value; /1 | — | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3101 | — | unknown | Output power percentage | RealOutputpowerPercent | register value; /1 | % | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3102 | — | unknown | Output max power limit | OutputMaxpowerLimited | register value; /10 | W | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3103 | — | unknown | Output max power limit | Current active output power limit enforced by the inverter (0.1 W resolution). | register value; /10 | W | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3104 | — | unknown | Standby flags | Inverterstandbyflag | register value; /1 | bit0:turn off Order； bit1:PVLow； bit2:AC Volt/Freq outofscope； bit3~bit7 ： Reserved | R | RESOLVED | semantic_correlated, source_claim | ;  |
| input | 3105 | — | unknown | Fault code | Inverterfaultmaincode | register value; /1 | — | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3106 | — | unknown | Warning main code | InverterWarningmaincode | register value; /1 | — | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3107 | — | unknown | Fault subcode | Inverterfaultsubcode | register value; /1 | — | R | RESOLVED | semantic_correlated, source_claim | ;  |
| input | 3108 | — | unknown | Warning subcode | InverterWarningsubcode | register value; /1 | — | R | RESOLVED | semantic_correlated, source_claim | ;  |
| input | 3109 | — | unknown | Register 3109 | — | register value; /1 | — | R | UNKNOWN_RESERVED | semantic_correlated, source_claim | ;  |
| input | 3110 | — | unknown | Warning code | Current inverter warning code (vendor-defined bitmask). | register value; /1 | — | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3111 | — | unknown | Warning code | PresentFFTValue[CHANNEL_A] | register value; /1 | — | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3112 | — | unknown | AFCI status | AFCIStatus | register value; /1 | — | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3113 | — | unknown | AFCI strength (channel A) | AFCIStrength[CHANNEL_A] | register value; /1 | — | R | RESOLVED | semantic_correlated, source_claim | ;  |
| input | 3114 | — | unknown | AFCI self-check (channel A) | AFCISelfCheck[CHANNEL_A] | register value; /1 | — | R | RESOLVED | semantic_correlated, source_claim | ;  |
| input | 3115 | — | unknown | Inverter start delay | invstartdelaytime | register value; /1 | s | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3116 | — | unknown | Reserved | Reserved | register value; /1 | — | R | UNKNOWN_RESERVED | semantic_correlated, source_claim | ;  |
| input | 3117 | — | unknown | Reserved | Reserved | register value; /1 | — | R | UNKNOWN_RESERVED | semantic_correlated, source_claim | ;  |
| input | 3118 | — | unknown | BDC connect state | BDCconnectstate | register value; /1 | — | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3119 | — | unknown | Dry contact state | CurrentstatusofDryContact | register value; /1 | — | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3120 | — | unknown | Reserved | Reserved | register value; /1 | — | R | UNKNOWN_RESERVED | semantic_correlated, source_claim | ;  |
| input | 3121 | — | unknown | Self-use power | self-usepower | register value; /10 | W | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3122 | — | unknown | Self-use power | Real-time power consumed by on-site loads (0.1 W resolution). | register value; /10 | W | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3123 | — | unknown | System energy today | Systemenergytoday | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3124 | — | unknown | System energy today | Total energy processed by the hybrid system today (0.1 kWh resolution). | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3125 | — | unknown | Battery discharge today | Todaydischargeenergy | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3126 | — | unknown | Battery discharge today | Energy discharged from the battery into the AC system today (0.1 kWh resolution). | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3127 | — | unknown | Battery discharge total | Totaldischargeenergy | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3128 | — | unknown | Battery discharge total | Total energy discharged from the battery (0.1 kWh resolution). | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3129 | — | unknown | Battery charge today | Chargeenergytoday | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3130 | — | unknown | Battery charge today | Energy charged into the battery today (0.1 kWh resolution). | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3131 | — | unknown | Battery charge total | Chargeenergytotal | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3132 | — | unknown | Battery charge total | Total energy charged into the battery (0.1 kWh resolution). | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3133 | — | unknown | AC charge energy today | TodayenergyofACcharge | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3134 | — | unknown | AC charge energy today | Energy charged into the battery from AC today (0.1 kWh resolution). | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3135 | — | unknown | AC charge energy total | TotalenergyofACcharge | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3136 | — | unknown | AC charge energy total | Lifetime energy charged into the battery from AC (0.1 kWh resolution). | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3137 | — | unknown | System energy total | Lifetime hybrid system energy throughput (0.1 kWh resolution). | register value; /1 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3138 | — | unknown | System energy total | Totalenergyofsystemoutput\ | register value; /1 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3139 | — | unknown | Self-use energy today | TodayenergyofSelfoutput | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3140 | — | unknown | Self-use energy today | Energy supplied to on-site loads today (0.1 kWh resolution). | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3141 | — | unknown | Self-use energy total | TotalenergyofSelfoutput | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3142 | — | unknown | Self-use energy total | Lifetime energy supplied to on-site loads (0.1 kWh resolution). | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3143 | — | unknown | Reserved | Reserved | register value; /1 | — | R | UNKNOWN_RESERVED | semantic_correlated, source_claim | ;  |
| input | 3144 | — | unknown | Priority mode | WordMode | register value | — | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3145 | — | unknown | EPS frequency | UPSfrequency | register value | Hz | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3146 | — | unknown | EPS phase R voltage | UPSphaseRoutputvoltage | register value; /10 | V | R | RESOLVED | semantic_correlated, source_claim | ;  |
| input | 3147 | — | unknown | EPS phase R current | UPSphaseRoutputcurrent | register value; /10 | A | R | RESOLVED | semantic_correlated, source_claim | ;  |
| input | 3148 | — | unknown | EPS phase R apparent power | UPSphaseRoutputpower | register value | VA | R | SOURCE_ONLY | source_claim | ;  |
| input | 3149 | — | unknown | EPS phase R apparent power | Phase R apparent power on the EPS output (0.1 VA resolution). | register value | VA | R | SOURCE_ONLY | source_claim | ;  |
| input | 3150 | — | unknown | EPS phase S voltage | UPSphaseSoutputvoltage | register value; /10 | V | R | RESOLVED | semantic_correlated, source_claim | ;  |
| input | 3151 | — | unknown | EPS phase S current | UPSphaseSoutputcurrent | register value; /10 | A | R | RESOLVED | semantic_correlated, source_claim | ;  |
| input | 3152 | — | unknown | EPS phase S apparent power | UPSphaseSoutputpower | register value; /10 | VA | R | RESOLVED | semantic_correlated, source_claim | ;  |
| input | 3153 | — | unknown | EPS phase S apparent power | Phase S apparent power on the EPS output (0.1 VA resolution). | register value; /10 | VA | R | RESOLVED | semantic_correlated, source_claim | ;  |
| input | 3154 | — | unknown | EPS phase T voltage | UPSphaseToutputvoltage | register value; /10 | V | R | RESOLVED | semantic_correlated, source_claim | ;  |
| input | 3155 | — | unknown | EPS phase T current | UPSphaseToutputcurrent | register value; /10 | A | R | RESOLVED | semantic_correlated, source_claim | ;  |
| input | 3156 | ac_phase_l3_power | alternate | EPS phase T apparent power | UPSphaseToutputpower | register value; /10 | VA | R | RESOLVED | semantic_correlated, source_claim | ; alternates: register:min_tl_xh:input:48, register:min_tl_xh:input:49, register:min_tl_xh:input:3036, register:min_tl_xh:input:3037, register:min_tl_xh:input:3157 |
| input | 3157 | ac_phase_l3_power | alternate | EPS phase T apparent power | Phase T apparent power on the EPS output (0.1 VA resolution). | register value; /10 | VA | R | RESOLVED | semantic_correlated, source_claim | ; alternates: register:min_tl_xh:input:48, register:min_tl_xh:input:49, register:min_tl_xh:input:3036, register:min_tl_xh:input:3037, register:min_tl_xh:input:3156 |
| input | 3158 | — | unknown | EPS total apparent power | UPSoutputpower | register value; /10 | VA | R | RESOLVED | semantic_correlated, source_claim | ;  |
| input | 3159 | — | unknown | EPS total apparent power | Total apparent power delivered by the EPS output (0.1 VA resolution). | register value; /10 | VA | R | RESOLVED | semantic_correlated, source_claim | ;  |
| input | 3160 | — | unknown | EPS load percentage | LoadpercentofUPSouput | register value; /10 | % | R | RESOLVED | semantic_correlated, source_claim | ;  |
| input | 3161 | — | unknown | BDC power factor | Powerfactor | register value; /10 | pf | R | RESOLVED | semantic_correlated, source_claim | ;  |
| input | 3162 | — | unknown | BDC DC voltage | DCvoltage | register value; /1 | V | R | RESOLVED | semantic_correlated, source_claim | ;  |
| input | 3163 | — | unknown | Reserved | Reserved | register value; /1 | — | R | UNKNOWN_RESERVED | semantic_correlated, source_claim | ;  |
| input | 3164 | — | unknown | BDC presence flag | BDC presence flag | u16 flag | 0:Don'tneed 1：need | R | RESOLVED_WITH_NOTES | read_verified, semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3165 | — | unknown | BDC derating mode | BDCDeratingMode： 0:Normal,unrestricted 1：Standbyorfault 2：Maximumbatterycurrentlimit (discharge) 3：BatterydischargeEnable(Discharge) 4：Highbusdischargederating | register value; /1 | — | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3166 | — | unknown | BDC system mode | SystemworkStateandmodeThe upper8bitsindicatethemode; 0：Nochargeanddischarge； 1：charge； 2：Discharge； Thelower8bitsrepresentthestatus; 0:StandbyStatus; 1:NormalStatus; 2:FaultStatus 3：FlashStatus; | register value; /1 | — | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3167 | — | unknown | BDC fault code | Storgedevicefaultcode | register value; /1 | — | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3168 | — | unknown | BDC warning code | Storgedevicewarningcode | register value; /1 | — | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3169 | battery_voltage | preferred | Battery voltage | Battery voltage | u16 / 100; /100 | V | R | RESOLVED_WITH_NOTES | read_verified, semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; OpenInverter lists /10; live raw 21146 is plausible as 211.46 V and not 2114.6 V.; ; alternates: register:min_tl_xh:input:3216 |
| input | 3170 | battery_current | preferred | Battery current | Battery current | s16 / 10; /10 | A | R | RESOLVED_WITH_NOTES | read_verified, semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ; alternates: register:min_tl_xh:input:3217 |
| input | 3171 | battery_soc | preferred | Battery SOC | Battery SOC | u16 percentage | % | R | RESOLVED_WITH_NOTES | read_verified, semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ; alternates: register:min_tl_xh:input:1014, register:min_tl_xh:input:3196, register:min_tl_xh:input:3197, register:min_tl_xh:input:3215 |
| input | 3172 | — | unknown | VBUS1 voltage | TotalBUSvoltage | register value; /10 | A | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3173 | — | unknown | VBUS2 voltage | OntheBUSvoltage | register value; /10 | A | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3174 | — | unknown | Buck/boost current | BUCK-BOOSTCurrent | register value; /10 | A | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3175 | — | unknown | LLC stage current | LLCCurrent | register value; /10 | A | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3176 | — | unknown | Battery temperature A | TempertureA | register value; /10 | °C | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3177 | — | unknown | Battery temperature B | TempertureB | register value; /10 | °C | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3178 | battery_discharge_power | alternate | Battery discharge power | Battery discharge power | s32 / 10; /10 | W | R | RESOLVED_WITH_NOTES | read_verified, semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ; alternates: register:min_tl_xh:input:3179 |
| input | 3179 | battery_discharge_power | alternate | Battery discharge power | Real-time discharge power flowing from the battery (0.1 W resolution). | register value; /10 | W | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ; alternates: register:min_tl_xh:input:3178 |
| input | 3180 | battery_charge_power | alternate | Battery charge power | Battery charge power | s32 / 10; /10 | W | R | RESOLVED_WITH_NOTES | read_verified, semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ; alternates: register:min_tl_xh:input:3181 |
| input | 3181 | battery_charge_power | alternate | Battery charge power | Real-time charge power flowing into the battery (0.1 W resolution). | register value; /10 | W | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ; alternates: register:min_tl_xh:input:3180 |
| input | 3182 | — | unknown | BDC discharge energy total | Dischargetotalenergyofstorgedevice | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3183 | — | unknown | BDC discharge energy total | Lifetime energy discharged by the battery DC converter (0.1 kWh resolution). | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3184 | — | unknown | BDC charge energy total | Chargetotalenergyofstorgedevice | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3185 | — | unknown | BDC charge energy total | Lifetime energy charged into the battery via the BDC (0.1 kWh resolution). | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3186 | — | unknown | Reserved | Reserved | register value; /1 | — | R | UNKNOWN_RESERVED | semantic_correlated, source_claim | ;  |
| input | 3187 | — | unknown | BDC flag word | BDCmark(chargeanddischarge, faultalarmcode) Bit0:ChargeEn;BDCallowscharging Bit1:DischargeEn;BDCallows discharge Bit2~7:Resvd;reserved Bit8~11:WarnSubCode;BDC sub-warningcode Bit12~15:FaultSubCode;BDC sub-errorcode | register value; /1 | — | R | UNKNOWN_RESERVED | semantic_correlated, source_claim | ;  |
| input | 3188 | — | unknown | VBUS2 low voltage | LowerBUSvoltage | register value; /10 | V | R | RESOLVED | semantic_correlated, source_claim | ;  |
| input | 3189 | — | unknown | BMS max cell index | BmsMaxVoltCellNo | register value; /1 | — | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3190 | — | unknown | BMS min cell index | BmsMinVoltCellNo | register value; /1 | — | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3191 | — | unknown | BMS average temperature A | BmsBatteryAvgTemp | register value; /1 | °C | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3192 | — | unknown | BMS max cell temperature A | BmsMaxCellTemp | register value; /10 | °C | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3193 | — | unknown | BMS average temperature B | BmsBatteryAvgTemp | register value; /10 | °C | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3194 | — | unknown | BMS max cell temperature B | BmsMaxCellTemp | register value; /1 | °C | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3195 | — | unknown | BMS average temperature C | BmsBatteryAvgTemp | register value; /1 | °C | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3196 | battery_soc | alternate | BMS max SOC | BmsMaxSOC | register value; /1 | % | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ; alternates: register:min_tl_xh:input:1014, register:min_tl_xh:input:3171, register:min_tl_xh:input:3197, register:min_tl_xh:input:3215 |
| input | 3197 | battery_soc | alternate | BMS min SOC | BmsMinSOC | register value; /1 | % | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ; alternates: register:min_tl_xh:input:1014, register:min_tl_xh:input:3171, register:min_tl_xh:input:3196, register:min_tl_xh:input:3215 |
| input | 3198 | — | unknown | Parallel battery count | ParallelBatteryNum | register value; /1 | — | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3199 | — | unknown | BMS derate reason | BmsDerateReason | register value; /1 | — | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3200 | — | unknown | BMS full charge capacity | BmsGaugeFCC（Ah） | register value; /1 | Ah | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3201 | — | unknown | BMS remaining capacity | BmsGaugeRM（Ah） | register value; /1 | Ah | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3202 | — | unknown | BMS protect flags 1 | BMSProtect1 | register value; /1 | — | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3203 | — | unknown | BMS warning flags 1 | BMSWarn1 | register value; /1 | — | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3204 | — | unknown | BMS fault flags 1 | BMSFault1 | register value; /1 | — | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3205 | — | unknown | BMS fault flags 2 | BMSFault2 | register value; /1 | — | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3206 | — | unknown | Reserved | Reserved | register value; /1 | — | R | UNKNOWN_RESERVED | semantic_correlated, source_claim | ;  |
| input | 3207 | — | unknown | Reserved | Reserved | register value; /1 | — | R | UNKNOWN_RESERVED | semantic_correlated, source_claim | ;  |
| input | 3208 | — | unknown | Reserved | Reserved | register value; /1 | — | R | UNKNOWN_RESERVED | semantic_correlated, source_claim | ;  |
| input | 3209 | — | unknown | Reserved | Reserved | register value; /1 | — | R | UNKNOWN_RESERVED | semantic_correlated, source_claim | ;  |
| input | 3210 | — | unknown | Battery insulation status | BatteryISOdetectionstatus | register value; /1 | 0：Not detected 1：Detection completed | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3211 | — | unknown | Battery request flags | batteryworkrequest | register value; /1 | — | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3212 | — | unknown | BMS status | BMS status | u16 enum | 0:dormancy 1:Charge 2:Discharge 3:free 4:standby 5:Softstart 6:fault 7:update | R | RESOLVED_WITH_NOTES | read_verified, semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3213 | — | unknown | BMS protect flags 2 | BMSProtect2 | register value; /1 | — | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3214 | — | unknown | BMS warning flags 2 | BMSWarn2 | register value; /1 | — | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3215 | battery_soc | alternate | BMS SOC | BMS SOC | u16 percentage | % | R | RESOLVED_WITH_NOTES | read_verified, semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ; alternates: register:min_tl_xh:input:1014, register:min_tl_xh:input:3171, register:min_tl_xh:input:3196, register:min_tl_xh:input:3197 |
| input | 3216 | battery_voltage | alternate | BMS battery voltage | BMS battery voltage | u16 / 100; /100 | V | R | RESOLVED_WITH_NOTES | read_verified, semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ; alternates: register:min_tl_xh:input:3169 |
| input | 3217 | battery_current | alternate | BMS battery current | BMS battery current | s16 / 100; /100 | A | R | RESOLVED_WITH_NOTES | read_verified, semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ; alternates: register:min_tl_xh:input:3170 |
| input | 3218 | — | unknown | BMS max cell temperature | batterycellmaximumtemperature | register value; /10 | °C | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3219 | — | unknown | BMS max charge current | Maximumchargingcurrent | register value; /100 | A | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3220 | — | unknown | BMS max discharge current | Maximumdischargecurrent | register value; /100 | A | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3221 | — | unknown | BMS cycle count | BMSCycleCnt | register value; /1 | — | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3222 | — | unknown | BMS SOH | BMS SOH | u16 percentage | % | R | RESOLVED_WITH_NOTES | read_verified, semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3223 | — | unknown | BMS charge voltage limit | Batterychargingvoltagelimitvalue | register value; /100 | V | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3224 | — | unknown | BMS discharge voltage limit | Batterydischargevoltagelimitvalue | register value; /1 | V | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3225 | — | unknown | BMS warning flags 3 | BMSWarn3 | register value; /1 | — | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3226 | — | unknown | BMS protect flags 3 | BMSProtect3 | register value; /1 | — | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3227 | — | unknown | Reserved | Reserved | register value; /1 | — | R | UNKNOWN_RESERVED | semantic_correlated, source_claim | ;  |
| input | 3228 | — | unknown | Reserved | Reserved | register value; /1 | — | R | UNKNOWN_RESERVED | semantic_correlated, source_claim | ;  |
| input | 3229 | — | unknown | Reserved | Reserved | register value; /1 | — | R | UNKNOWN_RESERVED | semantic_correlated, source_claim | ;  |
| input | 3230 | — | unknown | BMS max cell voltage | BMSBatterySingleVoltMax | register value; /1 | V | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3231 | — | unknown | BMS min cell voltage | BMSBatterySingleVoltMin | register value; /1 | V | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3232 | — | unknown | Battery load voltage | BatteryLoadVolt | register value; /100 | [0，650.00] | R | RESOLVED | semantic_correlated, source_claim | ;  |
| input | 3233 | — | unknown | Register 3233 | — | register value; /1 | — | R | UNKNOWN_RESERVED | semantic_correlated, source_claim | ;  |
| input | 3234 | — | unknown | Debug data 1 | Debugdata1 | register value; /1 | — | R | RESOLVED | semantic_correlated, source_claim | ;  |
| input | 3235 | — | unknown | Debug data 2 | Debugdata2 | register value; /1 | — | R | RESOLVED | semantic_correlated, source_claim | ;  |
| input | 3236 | — | unknown | Debug data 3 | Debugdata3 | register value; /1 | — | R | RESOLVED | semantic_correlated, source_claim | ;  |
| input | 3237 | — | unknown | Debug data 4 | Debugdata4 | register value; /1 | — | R | RESOLVED | semantic_correlated, source_claim | ;  |
| input | 3238 | — | unknown | Debug data 5 | Debugdata5 | register value; /1 | — | R | RESOLVED | semantic_correlated, source_claim | ;  |
| input | 3239 | — | unknown | Debug data 6 | Debugdata6 | register value; /1 | — | R | RESOLVED | semantic_correlated, source_claim | ;  |
| input | 3240 | — | unknown | Debug data 7 | Debugdata7 | register value; /1 | — | R | RESOLVED | semantic_correlated, source_claim | ;  |
| input | 3241 | — | unknown | Debug data 8 | Debugdata8 | register value; /1 | — | R | RESOLVED | semantic_correlated, source_claim | ;  |
| input | 3242 | — | unknown | Debug data 9 | Debugdata9 | register value; /1 | — | R | RESOLVED | semantic_correlated, source_claim | ;  |
| input | 3243 | — | unknown | Debug data 10 | Debugdata10 | register value; /1 | — | R | RESOLVED | semantic_correlated, source_claim | ;  |
| input | 3244 | — | unknown | Debug data 11 | Debugdata10 | register value; /1 | — | R | RESOLVED | semantic_correlated, source_claim | ;  |
| input | 3245 | — | unknown | Debug data 12 | Debugdata12 | register value; /1 | — | R | RESOLVED | semantic_correlated, source_claim | ;  |
| input | 3246 | — | unknown | Debug data 13 | Debugdata13 | register value; /1 | — | R | RESOLVED | semantic_correlated, source_claim | ;  |
| input | 3247 | — | unknown | Debug data 14 | Debugdata14 | register value; /1 | — | R | RESOLVED | semantic_correlated, source_claim | ;  |
| input | 3248 | — | unknown | Debug data 15 | Debugdata15 | register value; /1 | — | R | RESOLVED | semantic_correlated, source_claim | ;  |
| input | 3249 | — | unknown | Debug data 16 | Debugdata16 | register value; /1 | — | R | RESOLVED | semantic_correlated, source_claim | ;  |
| input | 3250 | — | unknown | Pex1H | PVinverter1outputpowerH | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 3251 | — | unknown | Pex1L | PVinverter1outputpowerL | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 3252 | — | unknown | Pex2H | PVinverter2outputpowerH | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 3253 | — | unknown | Pex2L | PVinverter2outputpowerL | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 3254 | — | unknown | Eex1TodayH | PVinverter1energyTodayH | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 3255 | — | unknown | Eex1TodayL | PVinverter1energyTodayL | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 3256 | — | unknown | Eex2TodayH | PVinverter2energyTodayH | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 3257 | — | unknown | Eex2TodayL | PVinverter2energyTodayL | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 3258 | — | unknown | Eex1TotalH | PVinverter1energyTotalH | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 3259 | — | unknown | Eex1TotalL | PVinverter1energyTotalL | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 3260 | — | unknown | Eex2TotalH | PVinverter2energyTotalH | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 3261 | — | unknown | Eex2TotalL | PVinverter2energyTotalL | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 3262 | — | unknown | uwBatNo | batterypacknumber | register value | BDC reports are updated every 15 minutes | R | SOURCE_ONLY | source_claim | ;  |
| input | 3263 | — | unknown | BatSerialNum1 | BatterypackserialnumberSN[0]SN[1] | register value | BDC reports are updated every 15 minutes | R | SOURCE_ONLY | source_claim | ;  |
| input | 3264 | — | unknown | BatSerialNum2 | BatterypackserialnumberSN[2]SN[3] | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 3265 | — | unknown | BatSerialNum3 | BatterypackserialnumberSN[4]SN[5] | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 3266 | — | unknown | BatSerialNum4 | BatterypackserialnumberSN[6]SN[7] | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 3267 | — | unknown | BatSerialNum5 | BatterypackserialnumberSN[8]SN[9] | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 3268 | — | unknown | BatSerialNum6 | Batterypackserial numberSN[10]SN[11] | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 3269 | — | unknown | BatSerialNum7 | Batterypackserial numberSN[12]SN[13] | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 3270 | — | unknown | BatSerialNum8 | Batterypackserial numberSN[14]SN[15] | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 3271 | — | unknown | Reserve | Reserve | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 3272 | — | unknown | Reserve | Reserve | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 3273 | — | unknown | Reserve | Reserve | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 3274 | — | unknown | Reserve | Reserve | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 3275 | — | unknown | Reserve | Reserve | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 3276 | — | unknown | Reserve | Reserve | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 3277 | — | unknown | Reserve | Reserve | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 3278 | — | unknown | Reserve | Reserve | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 3279 | — | unknown | Reserve | Reserve | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 3280 | — | unknown | bClrTodayDataFl ag | Cleardaydataflag | register value | Data of the current day that the server | R | SOURCE_ONLY | source_claim | ;  |
| input | 3281 | — | unknown | Register 3281 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| input | 3282 | — | unknown | Register 3282 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| input | 3283 | — | unknown | Register 3283 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| input | 3284 | — | unknown | Register 3284 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| input | 3285 | — | unknown | Register 3285 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| input | 3286 | — | unknown | Register 3286 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| input | 3287 | — | unknown | Register 3287 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| input | 3288 | — | unknown | Register 3288 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| input | 3289 | — | unknown | Register 3289 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| input | 3290 | — | unknown | Register 3290 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| input | 3291 | — | unknown | Register 3291 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| input | 3292 | — | unknown | Register 3292 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| input | 3293 | — | unknown | Register 3293 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| input | 3294 | — | unknown | Register 3294 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| input | 3295 | — | unknown | Register 3295 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| input | 3296 | — | unknown | Register 3296 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| input | 3297 | — | unknown | Register 3297 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| input | 3298 | — | unknown | Register 3298 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| input | 3299 | — | unknown | Register 3299 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| input | 3300 | — | unknown | Register 3300 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| input | 3301 | — | unknown | Register 3301 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| input | 3302 | — | unknown | Register 3302 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| input | 3303 | — | unknown | Register 3303 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| input | 3304 | — | unknown | Register 3304 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| input | 3305 | — | unknown | Register 3305 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| input | 3306 | — | unknown | Register 3306 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| input | 3307 | — | unknown | Register 3307 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| input | 3308 | — | unknown | Register 3308 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| input | 3309 | — | unknown | Register 3309 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| input | 3310 | — | unknown | Register 3310 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| input | 3311 | — | unknown | Register 3311 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| input | 3312 | — | unknown | Register 3312 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| input | 3313 | — | unknown | Register 3313 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| input | 3314 | — | unknown | Register 3314 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| input | 3315 | — | unknown | Register 3315 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| input | 3316 | — | unknown | Register 3316 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| input | 3317 | — | unknown | Register 3317 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| input | 3318 | — | unknown | Register 3318 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| input | 3319 | — | unknown | Register 3319 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| input | 3320 | — | unknown | Register 3320 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| input | 3321 | — | unknown | Register 3321 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| input | 3322 | — | unknown | Register 3322 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| input | 3323 | — | unknown | Register 3323 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| input | 3324 | — | unknown | Register 3324 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| input | 3325 | — | unknown | Register 3325 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| input | 3326 | — | unknown | Register 3326 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| input | 3327 | — | unknown | Register 3327 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| input | 3328 | — | unknown | Register 3328 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| input | 3329 | — | unknown | Register 3329 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| input | 3330 | — | unknown | Register 3330 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| input | 3331 | — | unknown | Register 3331 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| input | 3332 | — | unknown | Register 3332 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| input | 3333 | — | unknown | Register 3333 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| input | 3334 | — | unknown | Register 3334 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| input | 3335 | — | unknown | Register 3335 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| input | 3336 | — | unknown | Register 3336 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| input | 3337 | — | unknown | Register 3337 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| input | 3338 | — | unknown | Register 3338 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| input | 3339 | — | unknown | Register 3339 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| input | 3340 | — | unknown | Register 3340 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| input | 3341 | — | unknown | Register 3341 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| input | 3342 | — | unknown | Register 3342 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| input | 3343 | — | unknown | Register 3343 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| input | 3344 | — | unknown | Register 3344 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| input | 3345 | — | unknown | Register 3345 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| input | 3346 | — | unknown | Register 3346 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| input | 3347 | — | unknown | Register 3347 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| input | 3348 | — | unknown | Register 3348 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| input | 3349 | — | unknown | Register 3349 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| input | 3350 | — | unknown | Register 3350 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| input | 3351 | — | unknown | Register 3351 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| input | 3352 | — | unknown | Register 3352 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| input | 3353 | — | unknown | Register 3353 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| input | 3354 | — | unknown | Register 3354 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| input | 3355 | — | unknown | Register 3355 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| input | 3356 | — | unknown | Register 3356 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| input | 3357 | — | unknown | Register 3357 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| input | 3358 | — | unknown | Register 3358 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| input | 3359 | — | unknown | Register 3359 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| input | 3360 | — | unknown | Register 3360 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| input | 3361 | — | unknown | Register 3361 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| input | 3362 | — | unknown | Register 3362 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| input | 3363 | — | unknown | Register 3363 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| input | 3364 | — | unknown | Register 3364 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| input | 3365 | — | unknown | Register 3365 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| input | 3366 | — | unknown | Register 3366 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| input | 3367 | — | unknown | Register 3367 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| input | 3368 | — | unknown | Register 3368 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| input | 3369 | — | unknown | Register 3369 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| input | 3370 | — | unknown | Register 3370 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| input | 3371 | — | unknown | Register 3371 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| input | 3372 | — | unknown | Register 3372 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| input | 3373 | — | unknown | Register 3373 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| input | 3374 | — | unknown | Register 3374 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |

### TL3-X / MAX / MID / MAC

The repository groups these 120-family inverter layouts; model-specific differences remain possible.

| Table | Address | Semantic | Role | Name | Description | Encoding / scale | Unit | Access | Status | Evidence | Notes |
|---|---:|---|---|---|---|---|---|---|---|---|---|
| holding | 0 | — | unknown | Inverter Enabled | Theinvertercanbeswitched onandoff,andtheBDCcanbe switchedonandoffforthe battreadyfunction. | register value; /10 | — | R/W | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| holding | 1 | — | unknown | Safety function enable flags | SPI: system protection interface Bit0~3:forCEI0-21 Bit4~6:forSAA | register value | — | W | SOURCE_ONLY | source_claim | ;  |
| holding | 2 | — | unknown | Persist power-factor commands | Means these settings will be acting or not when next poweron | register value | — | W | RESOLVED | semantic_correlated, source_claim | ;  |
| holding | 3 | — | unknown | Active power limit setpoint | 255:powerisnotbelimited | register value; /1 | % | W | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| holding | 4 | — | unknown | Reactive power limit setpoint | 255:powerisnotbelimited | register value; /1 | % | W | SOURCE_ONLY | source_claim | ;  |
| holding | 5 | — | unknown | Power factor target | Inverter output power factor’s10000times | register value; /10000 | pf | W | SOURCE_ONLY | source_claim | ;  |
| holding | 6 | — | unknown | Rated apparent power | Normal power(high) | register value; /10 | 0.1VA | R | SOURCE_ONLY | source_claim | ;  |
| holding | 7 | — | unknown | Rated apparent power | Normal power(low) | register value; /10 | 0.1VA | R | SOURCE_ONLY | source_claim | ;  |
| holding | 8 | — | unknown | Nominal PV voltage | NormalworkPV voltage | register value; /10 | 0.1V | R | SOURCE_ONLY | source_claim | ;  |
| holding | 9 | — | unknown | Firmware | Firmwareversion (high) | firmware_version; /10 | ASCII | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| holding | 10 | — | unknown | Firmware | Firmwareversion (middle) | register value | ASCII | R | SOURCE_ONLY | source_claim | ;  |
| holding | 11 | — | unknown | Firmware | Firmwareversion(low) | register value | ASCII | R | SOURCE_ONLY | source_claim | ;  |
| holding | 12 | — | unknown | Firmware | ControlFirmware version(high) | register value | ASCII | R | SOURCE_ONLY | source_claim | ;  |
| holding | 13 | — | unknown | Firmware | ControlFirmware version(middle) | register value | ASCII | R | SOURCE_ONLY | source_claim | ;  |
| holding | 14 | — | unknown | Firmware | ControlFirmware version(low) | register value | ASCII | R | SOURCE_ONLY | source_claim | ;  |
| holding | 15 | — | unknown | LCD language selection | 0:Italian; 1:English; 2:German; 3:Spanish; 4:French; 5:Chinese; 6：Polish 7：Portugues 8：Hungary | register value | — | W | SOURCE_ONLY | source_claim | ;  |
| holding | 16 | — | unknown | Country profile configured | CountrySelectedor not | register value | — | W | SOURCE_ONLY | source_claim | ;  |
| holding | 17 | — | unknown | PV start voltage threshold | Inputstartvoltage | register value; /10 | 0.1V | W | SOURCE_ONLY | source_claim | ;  |
| holding | 18 | — | unknown | Start-up delay | Starttime | register value; /1 | 1s | W | SOURCE_ONLY | source_claim | ;  |
| holding | 19 | — | unknown | Restart delay | RestartDelayTime afterfaultback; | register value; /1 | 1s | W | SOURCE_ONLY | source_claim | ;  |
| holding | 20 | — | unknown | Active power ramp rate (startup) | Powerstartslope | register value; /10 | 0.1% | W | SOURCE_ONLY | source_claim | ;  |
| holding | 21 | — | unknown | Active power ramp rate (restart) | Powerrestartslope | register value; /10 | 0.1% | W | SOURCE_ONLY | source_claim | ;  |
| holding | 22 | — | unknown | Modbus RTU baud rate | Select communicationbaudrat e 0:9600bps 1:38400bps | register value | — | W | SOURCE_ONLY | source_claim | ;  |
| holding | 23 | — | unknown | Serial Number | The Home Assistant integration exposes this as the device serial number and reuses it as the unique identifier. | serial_number; /10 | ASCII | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| holding | 24 | — | unknown | Serial Number | The Home Assistant integration exposes this as the device serial number and reuses it as the unique identifier. | register value | ASCII | R | SOURCE_ONLY | source_claim | ;  |
| holding | 25 | — | unknown | Serial Number | The Home Assistant integration exposes this as the device serial number and reuses it as the unique identifier. | register value | ASCII | R | SOURCE_ONLY | source_claim | ;  |
| holding | 26 | — | unknown | Serial Number | The Home Assistant integration exposes this as the device serial number and reuses it as the unique identifier. | register value | ASCII | R | SOURCE_ONLY | source_claim | ;  |
| holding | 27 | — | unknown | Serial Number | The Home Assistant integration exposes this as the device serial number and reuses it as the unique identifier. | register value | ASCII | R | SOURCE_ONLY | source_claim | ;  |
| holding | 28 | — | unknown | Inverter Model | Home Assistant renders this value as the string A# B# D# T# P# U# M# S# via the integration's model() helper. Vendor spec lists value pattern `&*5`; digits appear to be stored without the leading letter codes, so treat as encoded tokens until verified on hardware. | register value; /10 | — | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| holding | 29 | — | unknown | Inverter Model | Home Assistant renders this value as the string A# B# D# T# P# U# M# S# via the integration's model() helper. Vendor spec lists value pattern `&*5`; digits appear to be stored without the leading letter codes, so treat as encoded tokens until verified on hardware. | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| holding | 30 | — | unknown | Modbus slave address | Communicate address | register value | — | W | SOURCE_ONLY | source_claim | ;  |
| holding | 31 | — | unknown | Firmware update trigger | Updatefirmware | register value | — | W | SOURCE_ONLY | source_claim | ;  |
| holding | 32 | — | unknown | Reset user configuration | Use with caution; the inverter immediately reboots and loses provisioning data. | register value | — | W | SOURCE_ONLY | source_claim | ;  |
| holding | 33 | — | unknown | Factory reset | Equivalent to the front-panel factory reset. Requires re-commissioning afterwards. | register value | — | W | SOURCE_ONLY | source_claim | ;  |
| holding | 34 | — | unknown | Manufacturer information string | The original table lists these words as Manufacturer Info 8-1 (high/middle/low); combine them to read the full string. | register value | ASCII | R | SOURCE_ONLY | source_claim | ;  |
| holding | 35 | — | unknown | Manufacturer information string | The original table lists these words as Manufacturer Info 8-1 (high/middle/low); combine them to read the full string. | register value | ASCII | R | SOURCE_ONLY | source_claim | ;  |
| holding | 36 | — | unknown | Manufacturer information string | The original table lists these words as Manufacturer Info 8-1 (high/middle/low); combine them to read the full string. | register value | ASCII | R | SOURCE_ONLY | source_claim | ;  |
| holding | 37 | — | unknown | Manufacturer information string | The original table lists these words as Manufacturer Info 8-1 (high/middle/low); combine them to read the full string. | register value | ASCII | R | SOURCE_ONLY | source_claim | ;  |
| holding | 38 | — | unknown | Manufacturer information string | The original table lists these words as Manufacturer Info 8-1 (high/middle/low); combine them to read the full string. | register value | ASCII | R | SOURCE_ONLY | source_claim | ;  |
| holding | 39 | — | unknown | Manufacturer information string | The original table lists these words as Manufacturer Info 8-1 (high/middle/low); combine them to read the full string. | register value | ASCII | R | SOURCE_ONLY | source_claim | ;  |
| holding | 40 | — | unknown | Manufacturer information string | The original table lists these words as Manufacturer Info 8-1 (high/middle/low); combine them to read the full string. | register value | ASCII | R | SOURCE_ONLY | source_claim | ;  |
| holding | 41 | — | unknown | Manufacturer information string | The original table lists these words as Manufacturer Info 8-1 (high/middle/low); combine them to read the full string. | register value | ASCII | R | SOURCE_ONLY | source_claim | ;  |
| holding | 42 | — | unknown | G100 failsafe enable | EnglishG100failsafeset | register value | — | W | SOURCE_ONLY | source_claim | ;  |
| holding | 43 | — | unknown | Device Type Code | Vendor spec provides value pattern `&*6`; handle as encoded type/family digits with implied prefixes pending confirmation. | register value; /10 | — | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| holding | 44 | — | unknown | Number Of Trackers And Phases | Inputtrackernumand outputphasenum | register value; /10 | — | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| holding | 45 | — | unknown | System clock year | Localtime | register value | — | W | SOURCE_ONLY | source_claim | ;  |
| holding | 46 | — | unknown | System clock month | Systemtime-Month | register value | — | W | SOURCE_ONLY | source_claim | ;  |
| holding | 47 | — | unknown | System clock day | Systemtime-Day | register value | — | W | SOURCE_ONLY | source_claim | ;  |
| holding | 48 | — | unknown | System clock hour | Systemtime-Hour | register value | — | W | SOURCE_ONLY | source_claim | ;  |
| holding | 49 | — | unknown | System clock minute | Systemtime-Min | register value | — | W | SOURCE_ONLY | source_claim | ;  |
| holding | 50 | — | unknown | System clock second | Systemtime-Second | register value | — | W | SOURCE_ONLY | source_claim | ;  |
| holding | 51 | — | unknown | System clock weekday | SystemWeekly | register value | — | W | SOURCE_ONLY | source_claim | ;  |
| holding | 52 | — | unknown | Stage 1 undervoltage limit | Gridvoltagelowlimit protect | register value | 0.1V | W | SOURCE_ONLY | source_claim | ;  |
| holding | 53 | — | unknown | Stage 1 overvoltage limit | Gridvoltagehighlimit protect | register value | 0.1V | W | SOURCE_ONLY | source_claim | ;  |
| holding | 54 | — | unknown | Stage 1 underfrequency limit | Gridfrequencylow limitprotect | register value | 0.01 Hz | W | SOURCE_ONLY | source_claim | ;  |
| holding | 55 | — | unknown | Stage 1 overfrequency limit | Gridhigh frequencylimitprotect | register value | 0.01 Hz | W | SOURCE_ONLY | source_claim | ;  |
| holding | 56 | — | unknown | Stage 2 undervoltage limit | Gridvoltagelowlimit protect2 | register value | 0.1V | W | SOURCE_ONLY | source_claim | ;  |
| holding | 57 | — | unknown | Stage 2 overvoltage limit | Gridvoltagehighlimit protect2 | register value | 0.1V | W | SOURCE_ONLY | source_claim | ;  |
| holding | 58 | — | unknown | Stage 2 underfrequency limit | Gridfrequencylow limitprotect2 | register value | 0.01 Hz | W | SOURCE_ONLY | source_claim | ;  |
| holding | 59 | — | unknown | Stage 2 overfrequency limit | Gridhighfrequency limitprotect2 | register value | 0.01 Hz | W | SOURCE_ONLY | source_claim | ;  |
| holding | 60 | — | unknown | Stage 3 undervoltage limit | Grid voltage low limit protect3 | register value | 0.1V | W | SOURCE_ONLY | source_claim | ;  |
| holding | 61 | — | unknown | Stage 3 overvoltage limit | Grid voltage high limit protect3 | register value | 0.1V | W | SOURCE_ONLY | source_claim | ;  |
| holding | 62 | grid_frequency | alternate | Stage 3 underfrequency limit | Grid frequency low limitprotect3 | register value | 0.01Hz | W | SOURCE_ONLY | source_claim | ; alternates: register:tl3_max_mid_mac:holding:63, register:tl3_max_mid_mac:holding:72, register:tl3_max_mid_mac:holding:73, register:tl3_max_mid_mac:holding:74, register:tl3_max_mid_mac:holding:75, register:tl3_max_mid_mac:holding:78, register:tl3_max_mid_mac:holding:79, register:tl3_max_mid_mac:input:37 |
| holding | 63 | grid_frequency | alternate | Stage 3 overfrequency limit | Grid frequency high limitprotect3 | register value | 0.01Hz | W | SOURCE_ONLY | source_claim | ; alternates: register:tl3_max_mid_mac:holding:62, register:tl3_max_mid_mac:holding:72, register:tl3_max_mid_mac:holding:73, register:tl3_max_mid_mac:holding:74, register:tl3_max_mid_mac:holding:75, register:tl3_max_mid_mac:holding:78, register:tl3_max_mid_mac:holding:79, register:tl3_max_mid_mac:input:37 |
| holding | 64 | — | unknown | Reconnect undervoltage limit | Gridlowvoltagelimit connecttoGrid | register value | 0.1V | W | SOURCE_ONLY | source_claim | ;  |
| holding | 65 | — | unknown | Reconnect overvoltage limit | Gridhighvoltagelimit connecttoGrid | register value | 0.1V | W | SOURCE_ONLY | source_claim | ;  |
| holding | 66 | — | unknown | Reconnect underfrequency limit | Gridlowfrequency | register value | 0.01 | W | SOURCE_ONLY | source_claim | ;  |
| holding | 67 | — | unknown | Reconnect overfrequency limit | Gridhighfrequency limitconnecttoGrid | register value | 0.01 Hz | W | SOURCE_ONLY | source_claim | ;  |
| holding | 68 | — | unknown | Stage 1 undervoltage trip delay | Grid voltage low limit protecttime 1 | register value | Cycle | W | SOURCE_ONLY | source_claim | ;  |
| holding | 69 | — | unknown | Stage 1 overvoltage trip delay | Grid voltage high limit protecttime 1 | register value | Cycle | W | SOURCE_ONLY | source_claim | ;  |
| holding | 70 | — | unknown | Stage 2 undervoltage trip delay | Grid voltage low limit protecttime 2 | register value | Cycle | W | SOURCE_ONLY | source_claim | ;  |
| holding | 71 | — | unknown | Stage 2 overvoltage trip delay | Grid voltage high limit protecttime 2 | register value | Cycle | W | SOURCE_ONLY | source_claim | ;  |
| holding | 72 | grid_frequency | alternate | Stage 1 underfrequency trip delay | Grid frequency low limitprotecttime 1 | register value | Cycle | W | SOURCE_ONLY | source_claim | ; alternates: register:tl3_max_mid_mac:holding:62, register:tl3_max_mid_mac:holding:63, register:tl3_max_mid_mac:holding:73, register:tl3_max_mid_mac:holding:74, register:tl3_max_mid_mac:holding:75, register:tl3_max_mid_mac:holding:78, register:tl3_max_mid_mac:holding:79, register:tl3_max_mid_mac:input:37 |
| holding | 73 | grid_frequency | alternate | Modbus Version | Grid frequency high limitprotecttime 1 | register value | Cycle | W | SOURCE_ONLY | source_claim | ; alternates: register:tl3_max_mid_mac:holding:62, register:tl3_max_mid_mac:holding:63, register:tl3_max_mid_mac:holding:72, register:tl3_max_mid_mac:holding:74, register:tl3_max_mid_mac:holding:75, register:tl3_max_mid_mac:holding:78, register:tl3_max_mid_mac:holding:79, register:tl3_max_mid_mac:input:37 |
| holding | 74 | grid_frequency | alternate | Stage 2 underfrequency trip delay | Grid frequency low limitprotecttime 2 | register value | Cycle | W | SOURCE_ONLY | source_claim | ; alternates: register:tl3_max_mid_mac:holding:62, register:tl3_max_mid_mac:holding:63, register:tl3_max_mid_mac:holding:72, register:tl3_max_mid_mac:holding:73, register:tl3_max_mid_mac:holding:75, register:tl3_max_mid_mac:holding:78, register:tl3_max_mid_mac:holding:79, register:tl3_max_mid_mac:input:37 |
| holding | 75 | grid_frequency | alternate | Stage 2 overfrequency trip delay | Grid frequency high limitprotecttime 2 | register value | Cycle | W | SOURCE_ONLY | source_claim | ; alternates: register:tl3_max_mid_mac:holding:62, register:tl3_max_mid_mac:holding:63, register:tl3_max_mid_mac:holding:72, register:tl3_max_mid_mac:holding:73, register:tl3_max_mid_mac:holding:74, register:tl3_max_mid_mac:holding:78, register:tl3_max_mid_mac:holding:79, register:tl3_max_mid_mac:input:37 |
| holding | 76 | — | unknown | Stage 3 undervoltage trip delay | Grid voltage low limit protecttime 3 | register value | Cycle | W | SOURCE_ONLY | source_claim | ;  |
| holding | 77 | — | unknown | Stage 3 overvoltage trip delay | Grid voltage high limit protecttime 3 | register value | Cycle | W | SOURCE_ONLY | source_claim | ;  |
| holding | 78 | grid_frequency | alternate | Stage 3 underfrequency trip delay | Grid frequency low limitprotecttime 3 | register value | Cycle | W | SOURCE_ONLY | source_claim | ; alternates: register:tl3_max_mid_mac:holding:62, register:tl3_max_mid_mac:holding:63, register:tl3_max_mid_mac:holding:72, register:tl3_max_mid_mac:holding:73, register:tl3_max_mid_mac:holding:74, register:tl3_max_mid_mac:holding:75, register:tl3_max_mid_mac:holding:79, register:tl3_max_mid_mac:input:37 |
| holding | 79 | grid_frequency | alternate | Stage 3 overfrequency trip delay | Grid frequency high limitprotecttime 3 | register value | Cycle | W | SOURCE_ONLY | source_claim | ; alternates: register:tl3_max_mid_mac:holding:62, register:tl3_max_mid_mac:holding:63, register:tl3_max_mid_mac:holding:72, register:tl3_max_mid_mac:holding:73, register:tl3_max_mid_mac:holding:74, register:tl3_max_mid_mac:holding:75, register:tl3_max_mid_mac:holding:78, register:tl3_max_mid_mac:input:37 |
| holding | 80 | — | unknown | Ten-minute overvoltage limit | Voltprotectionfor10 min | register value | 0.1V | W | SOURCE_ONLY | source_claim | ;  |
| holding | 81 | — | unknown | PV input high-voltage fault | PVVoltageHigh Fault | register value | 0.1V | W | SOURCE_ONLY | source_claim | ;  |
| holding | 82 | — | unknown | Controller firmware build string | Positions: 0-1 model letters, 2-3 model variant, 4-5 DSP1 build, 6-7 DSP2/M0 build, 8-9 CPLD/AFCI build, 10-11 M3 build. | register value | ASCII | R | SOURCE_ONLY | source_claim | ;  |
| holding | 83 | — | unknown | Controller firmware build string | Positions: 0-1 model letters, 2-3 model variant, 4-5 DSP1 build, 6-7 DSP2/M0 build, 8-9 CPLD/AFCI build, 10-11 M3 build. | register value | ASCII | R | SOURCE_ONLY | source_claim | ;  |
| holding | 84 | — | unknown | Controller firmware build string | Positions: 0-1 model letters, 2-3 model variant, 4-5 DSP1 build, 6-7 DSP2/M0 build, 8-9 CPLD/AFCI build, 10-11 M3 build. | register value | ASCII | R | SOURCE_ONLY | source_claim | ;  |
| holding | 85 | — | unknown | Controller firmware build string | Positions: 0-1 model letters, 2-3 model variant, 4-5 DSP1 build, 6-7 DSP2/M0 build, 8-9 CPLD/AFCI build, 10-11 M3 build. | register value | ASCII | R | SOURCE_ONLY | source_claim | ;  |
| holding | 86 | — | unknown | Controller firmware build string | Positions: 0-1 model letters, 2-3 model variant, 4-5 DSP1 build, 6-7 DSP2/M0 build, 8-9 CPLD/AFCI build, 10-11 M3 build. | register value | ASCII | R | SOURCE_ONLY | source_claim | ;  |
| holding | 87 | — | unknown | Controller firmware build string | Positions: 0-1 model letters, 2-3 model variant, 4-5 DSP1 build, 6-7 DSP2/M0 build, 8-9 CPLD/AFCI build, 10-11 M3 build. | register value | ASCII | R | SOURCE_ONLY | source_claim | ;  |
| holding | 88 | — | unknown | Modbus Version | ModbusVersion | register value; /100 | Int(16 bits) | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| holding | 89 | — | unknown | Power-factor control mode | 0=Unity PF, 1=Fixed PF setpoint, 2=Default PF line, 3=User-defined PF line, 4=Under-excited reactive power, 5=Over-excited reactive power, 6=Q(V) curve, 7=Direct control, 8=Static capacitive QV, 9=Static inductive QV. | register value | — | W | SOURCE_ONLY | source_claim | ;  |
| holding | 90 | — | unknown | GPRS modem IP/status flags | Bit 0-3: 0=idle, 1=IP read requested, 2=set IP succeeded; Bit 4-7: 0=unknown, 1=modem OK, 2=no SIM, 3=no network, 4=TCP connect fail, 5=TCP connected, etc. | register value | — | W | UNKNOWN_RESERVED | source_claim | ;  |
| holding | 91 | — | unknown | Frequency derating start | Frequencyderating startpoint | register value | 0.01H Z | W | SOURCE_ONLY | source_claim | ;  |
| holding | 92 | — | unknown | Frequency derating slope | Frequency–loadlimit rate | register value | 10tim es | W | SOURCE_ONLY | source_claim | ;  |
| holding | 93 | — | unknown | CEI 0-21 Q(V) point V1S | CEI021V1SQ(v) | register value | 0.1V | W | SOURCE_ONLY | source_claim | ;  |
| holding | 94 | — | unknown | CEI 0-21 Q(V) point V2S | CEI021V2SQ(v) | register value | 0.1V | W | SOURCE_ONLY | source_claim | ;  |
| holding | 95 | — | unknown | CEI 0-21 Q(V) point V1L | CEI021V1LQ(v) | register value | 0.1V | W | SOURCE_ONLY | source_claim | ;  |
| holding | 96 | — | unknown | CEI 0-21 Q(V) point V2L | CEI021V2LQ(v) | register value | 0.1V | W | SOURCE_ONLY | source_claim | ;  |
| holding | 97 | — | unknown | Q(V) lock-in active power | Q(v)lockinactive powerofCEI021 | register value | Percen t | W | SOURCE_ONLY | source_claim | ;  |
| holding | 98 | — | unknown | Q(V) lock-out active power | Q(v)lockOutactive powerofCEI021 | register value | Percen t | W | SOURCE_ONLY | source_claim | ;  |
| holding | 99 | — | unknown | Power-factor curve lock-in voltage | Lockingirdvoltof CEI021PFline | register value | 0.1V | W | SOURCE_ONLY | source_claim | ;  |
| holding | 100 | — | unknown | Power-factor curve lock-out voltage | Lockoutgirdvoltof CEI021PFline | register value | 0.1V | W | SOURCE_ONLY | source_claim | ;  |
| holding | 101 | — | unknown | Power-factor adjust value 1 | PFadjustvalue1 | register value | — | W | SOURCE_ONLY | source_claim | ;  |
| holding | 102 | — | unknown | Power-factor adjust value 2 | PFadjustvalue2 | register value | — | W | SOURCE_ONLY | source_claim | ;  |
| holding | 103 | — | unknown | Power-factor adjust value 3 | PFadjustvalue3 | register value | — | W | SOURCE_ONLY | source_claim | ;  |
| holding | 104 | — | unknown | Power-factor adjust value 4 | PFadjustvalue4 | register value | — | W | SOURCE_ONLY | source_claim | ;  |
| holding | 105 | — | unknown | Power-factor adjust value 5 | PFadjustvalue5 | register value | — | W | SOURCE_ONLY | source_claim | ;  |
| holding | 106 | — | unknown | Power-factor adjust value 6 | PFadjustvalue6 | register value | — | W | SOURCE_ONLY | source_claim | ;  |
| holding | 107 | — | unknown | Q(V) response delay | QV Reactive Power delaytime | register value | 1S | W | SOURCE_ONLY | source_claim | ;  |
| holding | 108 | — | unknown | Over-frequency derating delay | Overfrequency derati ngdelaytime | register value | 50ms | W | SOURCE_ONLY | source_claim | ;  |
| holding | 109 | — | unknown | Maximum reactive power magnitude | QmaxforQ(V)curve | register value | 0.1% | W | SOURCE_ONLY | source_claim | ;  |
| holding | 110 | — | unknown | PF curve point 1 load | 255meansnothispoint | register value | percen t | W | SOURCE_ONLY | source_claim | ;  |
| holding | 111 | — | unknown | PF curve point 1 target | PFlimitlinepoint1 powerfactor | register value | — | W | SOURCE_ONLY | source_claim | ;  |
| holding | 112 | — | unknown | PF curve point 2 load | 255meansnothispoint | register value | percen t | W | SOURCE_ONLY | source_claim | ;  |
| holding | 113 | — | unknown | PF curve point 2 target | PFlimitlinepoint 2powerfactor | register value | — | W | SOURCE_ONLY | source_claim | ;  |
| holding | 114 | — | unknown | PF curve point 3 load | 255meansnothispoint | register value | percen t | W | SOURCE_ONLY | source_claim | ;  |
| holding | 115 | — | unknown | PF curve point 3 target | PFlimitlinepoint3 powerfactor | register value | — | W | SOURCE_ONLY | source_claim | ;  |
| holding | 116 | — | unknown | PF curve point 4 load | 255meansnothispoint | register value | percen t | W | SOURCE_ONLY | source_claim | ;  |
| holding | 117 | — | unknown | PF curve point 4 target | PFlimitlinepoint4 powerfactor | register value | — | W | SOURCE_ONLY | source_claim | ;  |
| holding | 118 | — | unknown | Module code segments | SxxBxx | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| holding | 119 | — | unknown | Module code segments | DxxTxx | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| holding | 120 | — | unknown | Module code segments | PxxUxx | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| holding | 121 | — | unknown | Module code segments | Mxxxx Power | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| holding | 122 | — | unknown | Export limit enable mode | ExportLimitenable, 0:DisableexportLimit; 1:Enable485exportLimit; 2:Enable232exportLimit; 3:EnableCTexportLimit; | register value | — | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 123 | — | unknown | Export limit power setpoint | ExportLimitPowerRate | register value | 0.1% | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 124 | — | unknown | Tracker coupling mode | 0:Independent 1:DCSource 2:Parallel | register value | — | W | SOURCE_ONLY | source_claim | ;  |
| holding | 125 | — | unknown | Inverter type identifier | Reserved | register value | ASCII | R | UNKNOWN_RESERVED | source_claim | ;  |
| holding | 126 | — | unknown | Inverter type identifier | Reserved for factory diagnostics; not currently surfaced by the Home Assistant integration. | register value | ASCII | R | UNKNOWN_RESERVED | source_claim | ;  |
| holding | 127 | — | unknown | Inverter type identifier | Reserved for factory diagnostics; not currently surfaced by the Home Assistant integration. | register value | ASCII | R | UNKNOWN_RESERVED | source_claim | ;  |
| holding | 128 | — | unknown | Inverter type identifier | Reserved for factory diagnostics; not currently surfaced by the Home Assistant integration. | register value | ASCII | R | UNKNOWN_RESERVED | source_claim | ;  |
| holding | 129 | — | unknown | Inverter type identifier | Reserved for factory diagnostics; not currently surfaced by the Home Assistant integration. | register value | ASCII | R | UNKNOWN_RESERVED | source_claim | ;  |
| holding | 130 | — | unknown | Inverter type identifier | Reserved for factory diagnostics; not currently surfaced by the Home Assistant integration. | register value | ASCII | R | UNKNOWN_RESERVED | source_claim | ;  |
| holding | 131 | — | unknown | Inverter type identifier | Reserved for factory diagnostics; not currently surfaced by the Home Assistant integration. | register value | ASCII | R | UNKNOWN_RESERVED | source_claim | ;  |
| holding | 132 | — | unknown | Inverter type identifier | Reserved for factory diagnostics; not currently surfaced by the Home Assistant integration. | register value | ASCII | R | UNKNOWN_RESERVED | source_claim | ;  |
| holding | 133 | — | unknown | Bootloader identifier string | Reserved | register value | ASCII | R | UNKNOWN_RESERVED | source_claim | ;  |
| holding | 134 | — | unknown | Bootloader identifier string | Reserved | register value | ASCII | R | UNKNOWN_RESERVED | source_claim | ;  |
| holding | 135 | — | unknown | Bootloader identifier string | Reserved | register value | ASCII | R | UNKNOWN_RESERVED | source_claim | ;  |
| holding | 136 | — | unknown | Bootloader identifier string | Reserved | register value | ASCII | R | UNKNOWN_RESERVED | source_claim | ;  |
| holding | 137 | — | unknown | Reactive power direct-control setpoint | Positive values command inductive (lagging) vars; negative values request capacitive (leading) vars. | register value | 0.1var | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 138 | — | unknown | Reactive power direct-control setpoint | Positive values command inductive (lagging) vars; negative values request capacitive (leading) vars. | register value | 0.1var | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 139 | — | unknown | Reactive priority enable | 0：disable 1：enable | register value | 0/1 | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 140 | — | unknown | Reactive priority ratio | Tune together with the direct-control setpoint to limit how much active power is sacrificed for reactive support. | register value | 0.1 | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 141 | — | unknown | Night reactive support (SVG) | 0：disable 1：enable | register value | 0/1 | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 142 | — | unknown | Frequency-watt boost start | Pair with registers 151, 175, and 176 to set the under-frequency support profile. | register value | 0.01H Z | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 143 | — | unknown | Over-frequency recovery point | Works with registers 154-155 and the recovery delay in register 144. | register value | 0.01H Z | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 144 | — | unknown | Over-frequency recovery delay | OFDerate RecoverDelayTime | register value | 50ms | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 145 | — | unknown | Zero-current detection enable | Disable only when local interconnection rules explicitly forbid the zero-current method. | register value | — | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 146 | — | unknown | Zero-current low voltage | ZeroCurrent StaticlowVolt | register value | 0.1V | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 147 | — | unknown | Zero-current high voltage | ZeroCurrent StaticHighVolt | register value | 0.1V | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 148 | — | unknown | High-voltage derate start | HVoltDerateHighPoint | register value | 0.1V | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 149 | — | unknown | High-voltage derate end | Configure together with register 148 to define the slope of the derating curve. | register value | 0.1V | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 150 | — | unknown | Q(V) stabilisation time | QVPowerStableTime | register value | 0.1S | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 151 | — | unknown | Frequency-watt boost stop | Defines the end point of the frequency-watt boost region together with register 142. | register value | 0.01H Z | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 152 | — | unknown | CEI under-frequency ramp start | CEI | register value | 0.01Hz | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 153 | — | unknown | CEI under-frequency ramp end | CEI | register value | 0.01Hz | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 154 | — | unknown | CEI over-frequency ramp start | CEI | register value | 0.01Hz | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 155 | — | unknown | CEI over-frequency ramp end | CEI | register value | 0.01Hz | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 156 | — | unknown | CEI undervoltage ramp start | CEI | register value | 0.1V | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 157 | — | unknown | CEI undervoltage ramp end | CEI | register value | 0.1V | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 158 | — | unknown | CEI overvoltage ramp start | CEI | register value | 0.1V | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 159 | — | unknown | CEI overvoltage ramp end | CEI | register value | 0.1V | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 160 | — | unknown | Nominal grid voltage selection | UL | register value | — | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 161 | — | unknown | Grid watt restoration delay | UL | register value | 20ms | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 162 | — | unknown | Reconnect ramp slope | UL | register value | 0.1 | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 163 | — | unknown | LFRT stage 1 frequency | UL | register value | 0.01Hz | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 164 | — | unknown | LFRT stage 1 duration | UL | register value | 20ms | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 165 | — | unknown | LFRT stage 2 frequency | UL | register value | 0.01Hz | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 166 | — | unknown | LFRT stage 2 duration | UL | register value | 20ms | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 167 | — | unknown | HFRT stage 1 frequency | UL | register value | 0.01Hz | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 168 | — | unknown | HFRT stage 1 duration | UL | register value | 20ms | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 169 | — | unknown | HFRT stage 2 frequency | UL | register value | 0.01Hz | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 170 | — | unknown | HFRT stage 2 duration | UL | register value | 20ms | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 171 | — | unknown | HVRT stage 1 voltage | UL | register value | 0.001 Un | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 172 | — | unknown | HVRT stage 1 duration | UL | register value | 20ms | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 173 | — | unknown | HVRT stage 2 voltage | UL | register value | 0.001 Un | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 174 | — | unknown | HVRT stage 2 duration | UL | register value | 0.001 Un | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 175 | — | unknown | Under-frequency boost delay | 50549 | register value | 50ms | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 176 | — | unknown | Under-frequency boost rate | 50549 | register value | — | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 177 | — | unknown | Grid restart high-frequency limit | 50549 | register value | 0.01Hz | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 178 | — | unknown | Over-frequency derate response time | Growatt documentation implies steps of roughly 0.1 s; confirm on-site before changing. | register value | — | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 179 | — | unknown | Under-frequency boost response time | Steps are vendor-defined; treat as a tuning knob for the frequency-watt boost ramp rate. | register value | — | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 180 | — | unknown | Meter link status | 0:Missed,1:Received | register value | — | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 181 | — | unknown | Optimizer count | Thetotalnumberofoptimizers connectedtotheinverter | register value | — | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 182 | — | unknown | Optimizer configuration flag | 0x00:Notconfiguredsuccess 0x01:Configurationiscomplete | register value | — | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 183 | — | unknown | PV string scan mode | 0：Notsupport Other：PvStringNum | register value | — | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 184 | — | unknown | BDC parallel count | ThenumberofBDCs | register value | — | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 185 | — | unknown | Battery pack count | Totalnumberofbattery | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| holding | 186 | — | unknown | Reserved | No documented function. | register value | — | R | UNKNOWN_RESERVED | source_claim | ;  |
| holding | 187 | — | unknown | VPP function enable status | 0：Disable | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| holding | 188 | — | unknown | Datalogger server status | 0：connectionsucceeded | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| holding | 189 | — | unknown | Register 189 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| holding | 190 | — | unknown | Register 190 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| holding | 191 | — | unknown | Register 191 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| holding | 192 | — | unknown | Register 192 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| holding | 193 | — | unknown | Register 193 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| holding | 194 | — | unknown | Register 194 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| holding | 195 | — | unknown | Register 195 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| holding | 196 | — | unknown | Register 196 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| holding | 197 | — | unknown | Register 197 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| holding | 198 | — | unknown | Register 198 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| holding | 199 | — | unknown | Register 199 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| holding | 200 | — | unknown | PID control reserved | Reserved | register value | — | R | UNKNOWN_RESERVED | source_claim | ;  |
| holding | 201 | — | unknown | PID operating mode | 0=Automatic on demand, 1=Continuous, 2=All-night forced run. | register value | — | W | SOURCE_ONLY | source_claim | ;  |
| holding | 202 | — | unknown | PID breaker control | Leave enabled unless servicing the PID circuit. | register value | — | W | SOURCE_ONLY | source_claim | ;  |
| holding | 203 | — | unknown | PID output voltage setpoint | PID Output voltage option | register value | V | W | SOURCE_ONLY | source_claim | ;  |
| holding | 204 | — | unknown | Register 204 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| holding | 205 | — | unknown | Register 205 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| holding | 206 | — | unknown | Register 206 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| holding | 207 | — | unknown | Register 207 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| holding | 208 | — | unknown | Register 208 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| holding | 209 | — | unknown | Alternate serial number | Used by newer dataloggers; apply via commissioning tools when required. | register value | ASCII | R | SOURCE_ONLY | source_claim | ;  |
| holding | 210 | — | unknown | Alternate serial number | Used by newer dataloggers; apply via commissioning tools when required. | register value | ASCII | R | SOURCE_ONLY | source_claim | ;  |
| holding | 211 | — | unknown | Alternate serial number | Used by newer dataloggers; apply via commissioning tools when required. | register value | ASCII | R | SOURCE_ONLY | source_claim | ;  |
| holding | 212 | — | unknown | Alternate serial number | Used by newer dataloggers; apply via commissioning tools when required. | register value | ASCII | R | SOURCE_ONLY | source_claim | ;  |
| holding | 213 | — | unknown | Alternate serial number | Used by newer dataloggers; apply via commissioning tools when required. | register value | ASCII | R | SOURCE_ONLY | source_claim | ;  |
| holding | 214 | — | unknown | Alternate serial number | Used by newer dataloggers; apply via commissioning tools when required. | register value | ASCII | R | SOURCE_ONLY | source_claim | ;  |
| holding | 215 | — | unknown | Alternate serial number | Used by newer dataloggers; apply via commissioning tools when required. | register value | ASCII | R | SOURCE_ONLY | source_claim | ;  |
| holding | 216 | — | unknown | Alternate serial number | Used by newer dataloggers; apply via commissioning tools when required. | register value | ASCII | R | SOURCE_ONLY | source_claim | ;  |
| holding | 217 | — | unknown | Alternate serial number | Used by newer dataloggers; apply via commissioning tools when required. | register value | ASCII | R | SOURCE_ONLY | source_claim | ;  |
| holding | 218 | — | unknown | Alternate serial number | Used by newer dataloggers; apply via commissioning tools when required. | register value | ASCII | R | SOURCE_ONLY | source_claim | ;  |
| holding | 219 | — | unknown | Alternate serial number | Used by newer dataloggers; apply via commissioning tools when required. | register value | ASCII | R | SOURCE_ONLY | source_claim | ;  |
| holding | 220 | — | unknown | Alternate serial number | Used by newer dataloggers; apply via commissioning tools when required. | register value | ASCII | R | SOURCE_ONLY | source_claim | ;  |
| holding | 221 | — | unknown | Alternate serial number | Used by newer dataloggers; apply via commissioning tools when required. | register value | ASCII | R | SOURCE_ONLY | source_claim | ;  |
| holding | 222 | — | unknown | Alternate serial number | Used by newer dataloggers; apply via commissioning tools when required. | register value | ASCII | R | SOURCE_ONLY | source_claim | ;  |
| holding | 223 | — | unknown | Alternate serial number | Used by newer dataloggers; apply via commissioning tools when required. | register value | ASCII | R | SOURCE_ONLY | source_claim | ;  |
| holding | 224 | — | unknown | Register 224 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| holding | 225 | — | unknown | Register 225 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| holding | 226 | — | unknown | Register 226 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| holding | 227 | — | unknown | Register 227 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| holding | 228 | — | unknown | Register 228 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| holding | 229 | — | unknown | Energy calibration factor | 1-1000,(Percentratio) | register value | 0.1% | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 230 | — | unknown | Anti-islanding override | Never disable anti-islanding on a grid-connected installation unless explicitly authorised. | register value | — | W | SOURCE_ONLY | source_claim | ;  |
| holding | 231 | — | unknown | Fan self-test trigger | The inverter clears the flag automatically once the test completes. | register value | — | W | SOURCE_ONLY | source_claim | ;  |
| holding | 232 | — | unknown | Neutral line monitoring enable | EnableNLineofgrid | register value | — | W | SOURCE_ONLY | source_claim | ;  |
| holding | 233 | — | unknown | Hardware warning flags | wCheckHardware Bit0:GFCIBreak; Bit1:SPSDamage Bit8:EepromReadWarni ng Bit9:EEWriteWarning …… | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| holding | 234 | — | unknown | Hardware warning flags (reserved word) | Monitor for future firmware updates. | register value | — | R | UNKNOWN_RESERVED | source_claim | ;  |
| holding | 235 | — | unknown | Neutral-to-ground detection | Should remain enabled for safety compliance. | register value | — | W | SOURCE_ONLY | source_claim | ;  |
| holding | 236 | — | unknown | Non-standard voltage range | 0=Standard range, 1=Voltage grade 1, 2=Voltage grade 2. | register value | — | W | SOURCE_ONLY | source_claim | ;  |
| holding | 237 | — | unknown | Appointed spec override | Bit 0: Hungary | register value | Binary | W | SOURCE_ONLY | source_claim | ;  |
| holding | 238 | — | unknown | Fast MPPT mode | Reserved | register value | — | W | UNKNOWN_RESERVED | source_claim | ;  |
| holding | 239 | — | unknown | Reserved | Reserved | register value | — | R | UNKNOWN_RESERVED | source_claim | ;  |
| holding | 240 | — | unknown | Commissioning step index | Internal step counter used during factory self-check sequences. Installers should leave this value unchanged. | register value | — | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 241 | — | unknown | Installer longitude word | Longitude | register value | — | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 242 | — | unknown | Installer latitude word | Latitude | register value | — | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 243 | — | unknown | Register 243 | — | register value | — | R | UNKNOWN_RESERVED | source_claim | ;  |
| holding | 244 | — | unknown | Register 244 | — | register value | — | R | UNKNOWN_RESERVED | source_claim | ;  |
| holding | 245 | — | unknown | Register 245 | — | register value | — | R | UNKNOWN_RESERVED | source_claim | ;  |
| holding | 246 | — | unknown | Register 246 | — | register value | — | R | UNKNOWN_RESERVED | source_claim | ;  |
| holding | 247 | — | unknown | Register 247 | — | register value | — | R | UNKNOWN_RESERVED | source_claim | ;  |
| holding | 248 | — | unknown | Register 248 | — | register value | — | R | UNKNOWN_RESERVED | source_claim | ;  |
| holding | 249 | — | unknown | Register 249 | — | register value | — | R | UNKNOWN_RESERVED | source_claim | ;  |
| input | 0 | inverter_status | supported | Inverter status | InverterStatus | register value; /10 | — | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 1 | pv_total_power | alternate | PV input power | PpvH | register value; /10 | W | R/W | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ; alternates: register:tl3_max_mid_mac:input:2, register:tl3_max_mid_mac:input:5, register:tl3_max_mid_mac:input:6, register:tl3_max_mid_mac:input:9, register:tl3_max_mid_mac:input:10, register:tl3_max_mid_mac:input:13, register:tl3_max_mid_mac:input:14, register:tl3_max_mid_mac:input:17, register:tl3_max_mid_mac:input:18, register:tl3_max_mid_mac:input:21, register:tl3_max_mid_mac:input:22, register:tl3_max_mid_mac:input:25, register:tl3_max_mid_mac:input:26, register:tl3_max_mid_mac:input:29, register:tl3_max_mid_mac:input:30, register:tl3_max_mid_mac:input:33, register:tl3_max_mid_mac:input:34 |
| input | 2 | pv_total_power | alternate | PV input power | PpvL | register value; /10 | 0.1W | R/W | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ; alternates: register:tl3_max_mid_mac:input:1, register:tl3_max_mid_mac:input:5, register:tl3_max_mid_mac:input:6, register:tl3_max_mid_mac:input:9, register:tl3_max_mid_mac:input:10, register:tl3_max_mid_mac:input:13, register:tl3_max_mid_mac:input:14, register:tl3_max_mid_mac:input:17, register:tl3_max_mid_mac:input:18, register:tl3_max_mid_mac:input:21, register:tl3_max_mid_mac:input:22, register:tl3_max_mid_mac:input:25, register:tl3_max_mid_mac:input:26, register:tl3_max_mid_mac:input:29, register:tl3_max_mid_mac:input:30, register:tl3_max_mid_mac:input:33, register:tl3_max_mid_mac:input:34 |
| input | 3 | — | unknown | PV1 DC voltage | Vpv1 | register value; /10 | V | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 4 | — | unknown | PV1 DC current | PV1Curr | register value; /10 | A | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 5 | pv_total_power | alternate | PV1 DC power | Ppv1H | register value; /10 | W | R/W | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ; alternates: register:tl3_max_mid_mac:input:1, register:tl3_max_mid_mac:input:2, register:tl3_max_mid_mac:input:6, register:tl3_max_mid_mac:input:9, register:tl3_max_mid_mac:input:10, register:tl3_max_mid_mac:input:13, register:tl3_max_mid_mac:input:14, register:tl3_max_mid_mac:input:17, register:tl3_max_mid_mac:input:18, register:tl3_max_mid_mac:input:21, register:tl3_max_mid_mac:input:22, register:tl3_max_mid_mac:input:25, register:tl3_max_mid_mac:input:26, register:tl3_max_mid_mac:input:29, register:tl3_max_mid_mac:input:30, register:tl3_max_mid_mac:input:33, register:tl3_max_mid_mac:input:34 |
| input | 6 | pv_total_power | alternate | PV1 DC power | Ppv1L | register value; /10 | 0.1W | R/W | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ; alternates: register:tl3_max_mid_mac:input:1, register:tl3_max_mid_mac:input:2, register:tl3_max_mid_mac:input:5, register:tl3_max_mid_mac:input:9, register:tl3_max_mid_mac:input:10, register:tl3_max_mid_mac:input:13, register:tl3_max_mid_mac:input:14, register:tl3_max_mid_mac:input:17, register:tl3_max_mid_mac:input:18, register:tl3_max_mid_mac:input:21, register:tl3_max_mid_mac:input:22, register:tl3_max_mid_mac:input:25, register:tl3_max_mid_mac:input:26, register:tl3_max_mid_mac:input:29, register:tl3_max_mid_mac:input:30, register:tl3_max_mid_mac:input:33, register:tl3_max_mid_mac:input:34 |
| input | 7 | — | unknown | PV2 DC voltage | Vpv2 | register value; /10 | V | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 8 | — | unknown | PV2 DC current | PV2Curr | register value; /10 | A | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 9 | pv_total_power | alternate | PV2 DC power | Ppv2H | register value; /10 | W | R/W | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ; alternates: register:tl3_max_mid_mac:input:1, register:tl3_max_mid_mac:input:2, register:tl3_max_mid_mac:input:5, register:tl3_max_mid_mac:input:6, register:tl3_max_mid_mac:input:10, register:tl3_max_mid_mac:input:13, register:tl3_max_mid_mac:input:14, register:tl3_max_mid_mac:input:17, register:tl3_max_mid_mac:input:18, register:tl3_max_mid_mac:input:21, register:tl3_max_mid_mac:input:22, register:tl3_max_mid_mac:input:25, register:tl3_max_mid_mac:input:26, register:tl3_max_mid_mac:input:29, register:tl3_max_mid_mac:input:30, register:tl3_max_mid_mac:input:33, register:tl3_max_mid_mac:input:34 |
| input | 10 | pv_total_power | alternate | PV2 DC power | Ppv2L | register value; /10 | 0.1W | R/W | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ; alternates: register:tl3_max_mid_mac:input:1, register:tl3_max_mid_mac:input:2, register:tl3_max_mid_mac:input:5, register:tl3_max_mid_mac:input:6, register:tl3_max_mid_mac:input:9, register:tl3_max_mid_mac:input:13, register:tl3_max_mid_mac:input:14, register:tl3_max_mid_mac:input:17, register:tl3_max_mid_mac:input:18, register:tl3_max_mid_mac:input:21, register:tl3_max_mid_mac:input:22, register:tl3_max_mid_mac:input:25, register:tl3_max_mid_mac:input:26, register:tl3_max_mid_mac:input:29, register:tl3_max_mid_mac:input:30, register:tl3_max_mid_mac:input:33, register:tl3_max_mid_mac:input:34 |
| input | 11 | — | unknown | PV3 DC voltage | Vpv3 | register value; /10 | V | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 12 | — | unknown | PV3 DC current | PV3Curr | register value; /10 | A | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 13 | pv_total_power | alternate | PV3 DC power | Ppv3H | register value; /10 | W | R/W | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ; alternates: register:tl3_max_mid_mac:input:1, register:tl3_max_mid_mac:input:2, register:tl3_max_mid_mac:input:5, register:tl3_max_mid_mac:input:6, register:tl3_max_mid_mac:input:9, register:tl3_max_mid_mac:input:10, register:tl3_max_mid_mac:input:14, register:tl3_max_mid_mac:input:17, register:tl3_max_mid_mac:input:18, register:tl3_max_mid_mac:input:21, register:tl3_max_mid_mac:input:22, register:tl3_max_mid_mac:input:25, register:tl3_max_mid_mac:input:26, register:tl3_max_mid_mac:input:29, register:tl3_max_mid_mac:input:30, register:tl3_max_mid_mac:input:33, register:tl3_max_mid_mac:input:34 |
| input | 14 | pv_total_power | alternate | PV3 DC power | Ppv3L | register value; /10 | 0.1W | R/W | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ; alternates: register:tl3_max_mid_mac:input:1, register:tl3_max_mid_mac:input:2, register:tl3_max_mid_mac:input:5, register:tl3_max_mid_mac:input:6, register:tl3_max_mid_mac:input:9, register:tl3_max_mid_mac:input:10, register:tl3_max_mid_mac:input:13, register:tl3_max_mid_mac:input:17, register:tl3_max_mid_mac:input:18, register:tl3_max_mid_mac:input:21, register:tl3_max_mid_mac:input:22, register:tl3_max_mid_mac:input:25, register:tl3_max_mid_mac:input:26, register:tl3_max_mid_mac:input:29, register:tl3_max_mid_mac:input:30, register:tl3_max_mid_mac:input:33, register:tl3_max_mid_mac:input:34 |
| input | 15 | — | unknown | PV4 DC voltage | Vpv4 | register value; /10 | V | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 16 | — | unknown | PV4 DC current | PV4Curr | register value; /10 | A | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 17 | pv_total_power | alternate | PV4 DC power | Ppv4H | register value; /10 | W | R/W | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ; alternates: register:tl3_max_mid_mac:input:1, register:tl3_max_mid_mac:input:2, register:tl3_max_mid_mac:input:5, register:tl3_max_mid_mac:input:6, register:tl3_max_mid_mac:input:9, register:tl3_max_mid_mac:input:10, register:tl3_max_mid_mac:input:13, register:tl3_max_mid_mac:input:14, register:tl3_max_mid_mac:input:18, register:tl3_max_mid_mac:input:21, register:tl3_max_mid_mac:input:22, register:tl3_max_mid_mac:input:25, register:tl3_max_mid_mac:input:26, register:tl3_max_mid_mac:input:29, register:tl3_max_mid_mac:input:30, register:tl3_max_mid_mac:input:33, register:tl3_max_mid_mac:input:34 |
| input | 18 | pv_total_power | alternate | PV4 DC power | Ppv4L | register value; /10 | 0.1W | R/W | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ; alternates: register:tl3_max_mid_mac:input:1, register:tl3_max_mid_mac:input:2, register:tl3_max_mid_mac:input:5, register:tl3_max_mid_mac:input:6, register:tl3_max_mid_mac:input:9, register:tl3_max_mid_mac:input:10, register:tl3_max_mid_mac:input:13, register:tl3_max_mid_mac:input:14, register:tl3_max_mid_mac:input:17, register:tl3_max_mid_mac:input:21, register:tl3_max_mid_mac:input:22, register:tl3_max_mid_mac:input:25, register:tl3_max_mid_mac:input:26, register:tl3_max_mid_mac:input:29, register:tl3_max_mid_mac:input:30, register:tl3_max_mid_mac:input:33, register:tl3_max_mid_mac:input:34 |
| input | 19 | — | unknown | PV5 DC voltage | Vpv5 | register value; /10 | V | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 20 | — | unknown | PV5 DC current | PV5Curr | register value; /10 | A | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 21 | pv_total_power | alternate | PV5 DC power | Ppv5H | register value; /10 | W | R/W | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ; alternates: register:tl3_max_mid_mac:input:1, register:tl3_max_mid_mac:input:2, register:tl3_max_mid_mac:input:5, register:tl3_max_mid_mac:input:6, register:tl3_max_mid_mac:input:9, register:tl3_max_mid_mac:input:10, register:tl3_max_mid_mac:input:13, register:tl3_max_mid_mac:input:14, register:tl3_max_mid_mac:input:17, register:tl3_max_mid_mac:input:18, register:tl3_max_mid_mac:input:22, register:tl3_max_mid_mac:input:25, register:tl3_max_mid_mac:input:26, register:tl3_max_mid_mac:input:29, register:tl3_max_mid_mac:input:30, register:tl3_max_mid_mac:input:33, register:tl3_max_mid_mac:input:34 |
| input | 22 | pv_total_power | alternate | PV5 DC power | Ppv5L | register value; /10 | 0.1W | R/W | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ; alternates: register:tl3_max_mid_mac:input:1, register:tl3_max_mid_mac:input:2, register:tl3_max_mid_mac:input:5, register:tl3_max_mid_mac:input:6, register:tl3_max_mid_mac:input:9, register:tl3_max_mid_mac:input:10, register:tl3_max_mid_mac:input:13, register:tl3_max_mid_mac:input:14, register:tl3_max_mid_mac:input:17, register:tl3_max_mid_mac:input:18, register:tl3_max_mid_mac:input:21, register:tl3_max_mid_mac:input:25, register:tl3_max_mid_mac:input:26, register:tl3_max_mid_mac:input:29, register:tl3_max_mid_mac:input:30, register:tl3_max_mid_mac:input:33, register:tl3_max_mid_mac:input:34 |
| input | 23 | — | unknown | PV6 DC voltage | Vpv6 | register value; /10 | V | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 24 | — | unknown | PV6 DC current | PV6Curr | register value; /10 | A | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 25 | pv_total_power | alternate | PV6 DC power | PV6inputpower(high) | register value; /10 | W | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ; alternates: register:tl3_max_mid_mac:input:1, register:tl3_max_mid_mac:input:2, register:tl3_max_mid_mac:input:5, register:tl3_max_mid_mac:input:6, register:tl3_max_mid_mac:input:9, register:tl3_max_mid_mac:input:10, register:tl3_max_mid_mac:input:13, register:tl3_max_mid_mac:input:14, register:tl3_max_mid_mac:input:17, register:tl3_max_mid_mac:input:18, register:tl3_max_mid_mac:input:21, register:tl3_max_mid_mac:input:22, register:tl3_max_mid_mac:input:26, register:tl3_max_mid_mac:input:29, register:tl3_max_mid_mac:input:30, register:tl3_max_mid_mac:input:33, register:tl3_max_mid_mac:input:34 |
| input | 26 | pv_total_power | alternate | PV6 DC power | PV6inputpower(low) | register value; /10 | W | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ; alternates: register:tl3_max_mid_mac:input:1, register:tl3_max_mid_mac:input:2, register:tl3_max_mid_mac:input:5, register:tl3_max_mid_mac:input:6, register:tl3_max_mid_mac:input:9, register:tl3_max_mid_mac:input:10, register:tl3_max_mid_mac:input:13, register:tl3_max_mid_mac:input:14, register:tl3_max_mid_mac:input:17, register:tl3_max_mid_mac:input:18, register:tl3_max_mid_mac:input:21, register:tl3_max_mid_mac:input:22, register:tl3_max_mid_mac:input:25, register:tl3_max_mid_mac:input:29, register:tl3_max_mid_mac:input:30, register:tl3_max_mid_mac:input:33, register:tl3_max_mid_mac:input:34 |
| input | 27 | — | unknown | PV7 DC voltage | PV7voltage | register value; /10 | V | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 28 | — | unknown | PV7 DC current | PV7inputcurrent | register value; /10 | A | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 29 | pv_total_power | alternate | PV7 DC power | PV7inputpower(high) | register value; /10 | W | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ; alternates: register:tl3_max_mid_mac:input:1, register:tl3_max_mid_mac:input:2, register:tl3_max_mid_mac:input:5, register:tl3_max_mid_mac:input:6, register:tl3_max_mid_mac:input:9, register:tl3_max_mid_mac:input:10, register:tl3_max_mid_mac:input:13, register:tl3_max_mid_mac:input:14, register:tl3_max_mid_mac:input:17, register:tl3_max_mid_mac:input:18, register:tl3_max_mid_mac:input:21, register:tl3_max_mid_mac:input:22, register:tl3_max_mid_mac:input:25, register:tl3_max_mid_mac:input:26, register:tl3_max_mid_mac:input:30, register:tl3_max_mid_mac:input:33, register:tl3_max_mid_mac:input:34 |
| input | 30 | pv_total_power | alternate | PV7 DC power | PV7inputpower(low) | register value; /10 | W | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ; alternates: register:tl3_max_mid_mac:input:1, register:tl3_max_mid_mac:input:2, register:tl3_max_mid_mac:input:5, register:tl3_max_mid_mac:input:6, register:tl3_max_mid_mac:input:9, register:tl3_max_mid_mac:input:10, register:tl3_max_mid_mac:input:13, register:tl3_max_mid_mac:input:14, register:tl3_max_mid_mac:input:17, register:tl3_max_mid_mac:input:18, register:tl3_max_mid_mac:input:21, register:tl3_max_mid_mac:input:22, register:tl3_max_mid_mac:input:25, register:tl3_max_mid_mac:input:26, register:tl3_max_mid_mac:input:29, register:tl3_max_mid_mac:input:33, register:tl3_max_mid_mac:input:34 |
| input | 31 | — | unknown | PV8 DC voltage | PV8voltage | register value; /10 | V | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 32 | — | unknown | PV8 DC current | PV8inputcurrent | register value; /10 | A | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 33 | pv_total_power | alternate | PV8 DC power | PV8inputpower(high) | register value; /10 | W | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ; alternates: register:tl3_max_mid_mac:input:1, register:tl3_max_mid_mac:input:2, register:tl3_max_mid_mac:input:5, register:tl3_max_mid_mac:input:6, register:tl3_max_mid_mac:input:9, register:tl3_max_mid_mac:input:10, register:tl3_max_mid_mac:input:13, register:tl3_max_mid_mac:input:14, register:tl3_max_mid_mac:input:17, register:tl3_max_mid_mac:input:18, register:tl3_max_mid_mac:input:21, register:tl3_max_mid_mac:input:22, register:tl3_max_mid_mac:input:25, register:tl3_max_mid_mac:input:26, register:tl3_max_mid_mac:input:29, register:tl3_max_mid_mac:input:30, register:tl3_max_mid_mac:input:34 |
| input | 34 | pv_total_power | alternate | PV8 DC power | PV8inputpower(low) | register value; /10 | W | R | RESOLVED | semantic_correlated, source_claim | ; alternates: register:tl3_max_mid_mac:input:1, register:tl3_max_mid_mac:input:2, register:tl3_max_mid_mac:input:5, register:tl3_max_mid_mac:input:6, register:tl3_max_mid_mac:input:9, register:tl3_max_mid_mac:input:10, register:tl3_max_mid_mac:input:13, register:tl3_max_mid_mac:input:14, register:tl3_max_mid_mac:input:17, register:tl3_max_mid_mac:input:18, register:tl3_max_mid_mac:input:21, register:tl3_max_mid_mac:input:22, register:tl3_max_mid_mac:input:25, register:tl3_max_mid_mac:input:26, register:tl3_max_mid_mac:input:29, register:tl3_max_mid_mac:input:30, register:tl3_max_mid_mac:input:33 |
| input | 35 | — | unknown | AC output power | Outputpower(high) | register value; /10 | W | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 36 | — | unknown | AC output power | Outputpower(low) | register value; /10 | W | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 37 | grid_frequency | alternate | Grid frequency | Gridfrequency | register value; /100 | Hz | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ; alternates: register:tl3_max_mid_mac:holding:62, register:tl3_max_mid_mac:holding:63, register:tl3_max_mid_mac:holding:72, register:tl3_max_mid_mac:holding:73, register:tl3_max_mid_mac:holding:74, register:tl3_max_mid_mac:holding:75, register:tl3_max_mid_mac:holding:78, register:tl3_max_mid_mac:holding:79 |
| input | 38 | — | unknown | AC phase L1 voltage | Three/singlephasegridvoltage | register value; /10 | V | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 39 | — | unknown | AC phase L1 current | Three/singlephasegridoutputcurrent | register value; /10 | A | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 40 | — | unknown | AC phase L1 power | Three/single phase grid output watt VA(high) | register value; /10 | VA | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 41 | — | unknown | AC phase L1 power | Three/single phase grid output watt VA(low) | register value; /10 | W | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 42 | — | unknown | AC phase L2 voltage | Threephasegridvoltage | register value; /10 | V | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 43 | — | unknown | AC phase L2 current | Threephasegridoutputcurrent | register value; /10 | A | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 44 | — | unknown | AC phase L2 power | Threephasegridoutputpower(high) | register value; /10 | VA | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 45 | — | unknown | AC phase L2 power | Threephasegridoutputpower(low) | register value; /10 | W | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 46 | — | unknown | AC phase L3 voltage | Threephasegridvoltage | register value; /10 | V | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 47 | — | unknown | AC phase L3 current | Threephasegridoutputcurrent | register value; /10 | A | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 48 | ac_phase_l3_power | alternate | AC phase L3 power | Threephasegridoutputpower(high) | register value; /10 | VA | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ; alternates: register:tl3_max_mid_mac:input:49 |
| input | 49 | ac_phase_l3_power | alternate | AC phase L3 power | Threephasegridoutputpower(low) | register value; /10 | W | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ; alternates: register:tl3_max_mid_mac:input:48 |
| input | 50 | — | unknown | Vac_RS | Threephasegridvoltage | register value | V | R | RESOLVED | semantic_correlated, source_claim | ;  |
| input | 51 | — | unknown | Vac_ST | Threephasegridvoltage | register value | V | R | RESOLVED | semantic_correlated, source_claim | ;  |
| input | 52 | — | unknown | Vac_TR | Threephasegridvoltage | register value | V | R | RESOLVED | semantic_correlated, source_claim | ;  |
| input | 53 | — | unknown | Output energy today | Todaygenerateenergy(high) | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 54 | — | unknown | Output energy today | Todaygenerateenergy(low) | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 55 | — | unknown | Output energy total | Totalgenerateenergy(high) | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 56 | — | unknown | Output energy total | Totalgenerateenergy(low) | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 57 | inverter_runtime | supported | Run time | Raw counter counts seconds; divide by 7200 to obtain hours. | register value; /7200 | s | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 58 | — | unknown | Run time | Raw counter counts seconds; divide by 7200 to obtain hours. | register value; /7200 | h | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 59 | — | unknown | PV1 energy today | PV1Energytoday(high) | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 60 | — | unknown | PV1 energy today | PV1Energytoday(low) | register value; /10 | kWh | R | RESOLVED | semantic_correlated, source_claim | ;  |
| input | 61 | — | unknown | PV1 energy total | PV1Energytotal(high) | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 62 | — | unknown | PV1 energy total | PV1Energytotal(low) | register value; /10 | kWh | R | RESOLVED | semantic_correlated, source_claim | ;  |
| input | 63 | — | unknown | PV2 energy today | PV2Energytoday(high) | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 64 | — | unknown | PV2 energy today | PV2Energytoday(low) | register value; /10 | kWh | R | RESOLVED | semantic_correlated, source_claim | ;  |
| input | 65 | — | unknown | PV2 energy total | PV2Energytotal(high) | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 66 | — | unknown | PV2 energy total | PV2Energytotal(low) | register value; /10 | kWh | R | RESOLVED | semantic_correlated, source_claim | ;  |
| input | 67 | — | unknown | PV3 energy today | PV3Energytoday(high) | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 68 | — | unknown | PV3 energy today | PV3Energytoday(low) | register value; /10 | kWh | R | RESOLVED | semantic_correlated, source_claim | ;  |
| input | 69 | — | unknown | PV3 energy total | PV3Energytotal(high) | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 70 | — | unknown | PV3 energy total | PV3Energytotal(low) | register value; /10 | kWh | R | RESOLVED | semantic_correlated, source_claim | ;  |
| input | 71 | — | unknown | PV4 energy today | PV4Energytoday(high) | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 72 | — | unknown | PV4 energy today | PV4Energytoday(low) | register value; /10 | kWh | R | RESOLVED | semantic_correlated, source_claim | ;  |
| input | 73 | pv4_energy_total | alternate | PV4 energy total | PV4Energytotal(high) | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ; alternates: register:tl3_max_mid_mac:input:74 |
| input | 74 | pv4_energy_total | alternate | PV4 energy total | PV4Energytotal(low) | register value; /10 | kWh | R | RESOLVED | semantic_correlated, source_claim | ; alternates: register:tl3_max_mid_mac:input:73 |
| input | 75 | — | unknown | PV5 energy today | PV5Energytoday(high) | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 76 | — | unknown | PV5 energy today | PV5Energytoday(low) | register value; /10 | kWh | R | RESOLVED | semantic_correlated, source_claim | ;  |
| input | 77 | — | unknown | PV5 energy total | PV5Energytotal(high) | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 78 | — | unknown | PV5 energy total | PV5Energytotal(low) | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 79 | — | unknown | PV6 energy today | PV6Energytoday(high) | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 80 | — | unknown | PV6 energy today | PV6Energytoday(low) | register value; /10 | kWh | R | RESOLVED | semantic_correlated, source_claim | ;  |
| input | 81 | — | unknown | PV6 energy total | PV6Energytotal(high) | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 82 | — | unknown | PV6 energy total | PV6Energytotal(low) | register value; /10 | kWh | R | RESOLVED | semantic_correlated, source_claim | ;  |
| input | 83 | — | unknown | PV7 energy today | PV7Energytoday(high) | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 84 | — | unknown | PV7 energy today | PV7Energytoday(low) | register value; /10 | kWh | R | RESOLVED | semantic_correlated, source_claim | ;  |
| input | 85 | — | unknown | PV7 energy total | PV7Energytotal(high) | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 86 | — | unknown | PV7 energy total | PV7Energytotal(low) | register value; /10 | kWh | R | RESOLVED | semantic_correlated, source_claim | ;  |
| input | 87 | — | unknown | PV8 energy today | PV8Energytoday(high) | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 88 | — | unknown | PV8 energy today | PV8Energytoday(low) | register value; /10 | kWh | R | RESOLVED | semantic_correlated, source_claim | ;  |
| input | 89 | — | unknown | PV8 energy total | PV8Energytotal(high) | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 90 | — | unknown | PV8 energy total | PV8Energytotal(low) | register value; /10 | kWh | R | RESOLVED | semantic_correlated, source_claim | ;  |
| input | 91 | — | unknown | PV energy total | PVEnergytotal(high) | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 92 | — | unknown | PV energy total | PVEnergytotal(low) | register value; /10 | kWh | R | RESOLVED | semantic_correlated, source_claim | ;  |
| input | 93 | — | unknown | Inverter temperature | Invertertemperature | register value; /10 | °C | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 94 | — | unknown | IPM temperature | TheinsideIPMininverterTemperature | register value; /10 | °C | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 95 | — | unknown | Boost temperature | Boosttemperature | register value; /10 | °C | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 96 | — | unknown | Temp4 | Temp4 | register value | reserved | R | SOURCE_ONLY | source_claim | ;  |
| input | 97 | — | unknown | uwBatVolt_DSP | BatVolt_DSP | register value | BatVolt(DSP) | R | SOURCE_ONLY | source_claim | ;  |
| input | 98 | — | unknown | P-bus voltage | PBusinsideVoltage | register value; /10 | V | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 99 | — | unknown | N-bus voltage | NBusinsideVoltage | register value; /10 | V | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 100 | — | unknown | IPF | InverteroutputPFnow | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 101 | — | unknown | Output power percentage | RealOutputpowerPercent | register value; /10 | % | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 102 | — | unknown | OPFullwattH | OutputMaxpowerLimitedhigh | register value | W | R | RESOLVED | semantic_correlated, source_claim | ;  |
| input | 103 | — | unknown | OPFullwattL | OutputMaxpowerLimitedlow | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 104 | — | unknown | Derating mode | DeratingMode | register value; /10 | — | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 105 | — | unknown | Fault code | Inverterfaultmaincode | register value; /10 | — | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 106 | — | unknown | Register 106 | — | register value | — | R | UNKNOWN_RESERVED | source_claim | ;  |
| input | 107 | — | unknown | FaultSubcode | Inverterfaultsubcode | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 108 | — | unknown | RemoteCtrlEn | / | register value | StoragePow er(SPA) | R | SOURCE_ONLY | source_claim | ;  |
| input | 109 | — | unknown | RemoteCtrlPow er | / | register value | StoragePow er(SPA) | R | SOURCE_ONLY | source_claim | ;  |
| input | 110 | — | unknown | Warning code | WarningbitH | register value; /10 | — | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 111 | — | unknown | Warning code | Inverterwarnsubcode | register value; /10 | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 112 | — | unknown | WarnMaincode | Inverterwarnmaincode | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 113 | — | unknown | real Power Percent | realPowerPercent | register value | MAX | R | SOURCE_ONLY | source_claim | ;  |
| input | 114 | — | unknown | inv start delay time | invstartdelaytime | register value | MAX | R | SOURCE_ONLY | source_claim | ;  |
| input | 115 | — | unknown | bINVAllFaultCod e | bINVAllFaultCode | register value | MAX | R | SOURCE_ONLY | source_claim | ;  |
| input | 116 | — | unknown | AC charge Power_H | Gridpowertolocalload | register value | Storage Power | R | SOURCE_ONLY | source_claim | ;  |
| input | 117 | — | unknown | AC charge Power_L | Gridpowertolocalload | register value | Storage Power | R | SOURCE_ONLY | source_claim | ;  |
| input | 118 | — | unknown | Priority | 0:LoadFirst | register value | Storage | R | RESOLVED | semantic_correlated, source_claim | ;  |
| input | 119 | — | unknown | BatteryType | 0：Lead-acid 1：Lithiumbattery | register value | — | R | RESOLVED | semantic_correlated, source_claim | ;  |
| input | 120 | — | unknown | AutoProofreadC MD | Aging mode Auto-calibration command | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 121 | — | unknown | Register 121 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| input | 122 | — | unknown | Register 122 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| input | 123 | — | unknown | Register 123 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| input | 124 | — | unknown | reserved | reserved | register value | — | R | UNKNOWN_RESERVED | source_claim | ;  |
| input | 125 | — | unknown | PIDPV1+Voltage | PIDPV1+Voltage | register value | 0.1V | R | SOURCE_ONLY | source_claim | ;  |
| input | 126 | — | unknown | PIDPV1+Current | PIDPV1+Current | register value | 0.1mA | R | SOURCE_ONLY | source_claim | ;  |
| input | 127 | — | unknown | PIDPV2+Voltage | PIDPV2+Voltage | register value | 0.1V | R | SOURCE_ONLY | source_claim | ;  |
| input | 128 | — | unknown | PIDPV2+Current | PIDPV2+Current | register value | 0.1mA | R | SOURCE_ONLY | source_claim | ;  |
| input | 129 | — | unknown | PIDPV3+Voltage | PIDPV3+Voltage | register value | 0.1V | R | SOURCE_ONLY | source_claim | ;  |
| input | 130 | — | unknown | PIDPV3+Current | PIDPV3+Current | register value | 0.1mA | R | SOURCE_ONLY | source_claim | ;  |
| input | 131 | — | unknown | PIDPV4+Voltage | PIDPV4+Voltage | register value | 0.1V | R | SOURCE_ONLY | source_claim | ;  |
| input | 132 | — | unknown | PIDPV4+Current | PIDPV4+Current | register value | 0.1mA | R | SOURCE_ONLY | source_claim | ;  |
| input | 133 | — | unknown | PIDPV5+Voltage | PIDPV5+Voltage | register value | 0.1V | R | SOURCE_ONLY | source_claim | ;  |
| input | 134 | — | unknown | PIDPV5+Current | PIDPV5+Current | register value | 0.1mA | R | SOURCE_ONLY | source_claim | ;  |
| input | 135 | — | unknown | PIDPV6+Voltage | PIDPV6+Voltage | register value | 0.1V | R | SOURCE_ONLY | source_claim | ;  |
| input | 136 | — | unknown | PIDPV6+Current | PIDPV6+Current | register value | 0.1mA | R | SOURCE_ONLY | source_claim | ;  |
| input | 137 | — | unknown | PIDPV7+Voltage | PIDPV7+Voltage | register value | 0.1V | R | SOURCE_ONLY | source_claim | ;  |
| input | 138 | — | unknown | PIDPV7+Current | PIDPV7+Current | register value | 0.1mA | R | SOURCE_ONLY | source_claim | ;  |
| input | 139 | — | unknown | PIDPV8+Voltage | PIDPV8+Voltage | register value | 0.1V | R | SOURCE_ONLY | source_claim | ;  |
| input | 140 | — | unknown | PIDPV8+Current | PIDPV8+Current | register value | 0.1mA | R | SOURCE_ONLY | source_claim | ;  |
| input | 141 | — | unknown | PIDStatus | PIDStatus | register value | — | W | SOURCE_ONLY | source_claim | ;  |
| input | 142 | — | unknown | V_String1 | V_String1 | register value | 0.1V | R | SOURCE_ONLY | source_claim | ;  |
| input | 143 | — | unknown | Curr_String1 | Curr_String1 | register value | 0.1A | R | SOURCE_ONLY | source_claim | ;  |
| input | 144 | — | unknown | V_String2 | V_String2 | register value | 0.1V | R | SOURCE_ONLY | source_claim | ;  |
| input | 145 | — | unknown | Curr_String2 | PVString2current | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 146 | — | unknown | V_String3 | PVString3voltage | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 147 | — | unknown | Curr_String3 | PVString3current | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 148 | — | unknown | V_String4 | PVString4voltage | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 149 | — | unknown | Curr_String4 | PVString4current | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 150 | — | unknown | V_String5 | PVString5voltage | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 151 | — | unknown | Curr_String5 | PVString5current | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 152 | — | unknown | V_String6 | PVString6voltage | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 153 | — | unknown | Curr_String6 | PVString6current | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 154 | — | unknown | V_String7 | PVString7voltage | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 155 | — | unknown | Curr_String7 | PVString7current | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 156 | — | unknown | V_String8 | PVString8voltage | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 157 | — | unknown | Curr_String8 | PVString8current | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 158 | — | unknown | V_String9 | PVString9voltage | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 159 | — | unknown | Curr_String9 | PVString9current | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 160 | — | unknown | V_String10 | PVString10voltage | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 161 | — | unknown | Curr_String10 | PVString10current | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 162 | — | unknown | V_String11 | PVString11voltage | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 163 | — | unknown | Curr_String11 | PVString11current | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 164 | — | unknown | V_String12 | PVString12voltage | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 165 | — | unknown | Curr_String12 | PVString12current | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 166 | — | unknown | V_String13 | PVString13voltage | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 167 | — | unknown | Curr_String13 | PVString13current | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 168 | — | unknown | V_String14 | PVString14voltage | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 169 | — | unknown | Curr_String14 | PVString14current | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 170 | — | unknown | V_String15 | PVString15voltage | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 171 | — | unknown | Curr_String15 | PVString15current | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 172 | — | unknown | V_String16 | PVString16voltage | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 173 | — | unknown | Curr_String16 | PVString16current | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 174 | — | unknown | StrUnmatch | Bit0~15:String1~16unmatch | register value | suggestive | R | SOURCE_ONLY | source_claim | ;  |
| input | 175 | — | unknown | StrCurrentUnblan ce | Bit0~15:String1~16currentunblance | register value | suggestive | R | SOURCE_ONLY | source_claim | ;  |
| input | 176 | — | unknown | StrDisconnect | Bit0~15:String1~16disconnect | register value | suggestive | R | SOURCE_ONLY | source_claim | ;  |
| input | 177 | — | unknown | PIDFaultCode | Bit0:Outputovervoltage Bit1:ISOfault Bit2:BUSvoltageabnormal Bit3~15:reserved | register value | — | R | UNKNOWN_RESERVED | source_claim | ;  |
| input | 178 | — | unknown | StringPrompt | StringPrompt Bit0:StringUnmatch Bit1:StrDisconnect Bit2:StrCurrentUnblance | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 179 | — | unknown | PVWarningValue | PVWarningValue | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 180 | — | unknown | DSP075 Warning Value | DSP075WarningValue | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 181 | — | unknown | DSP075 Fault Value | DSP075FaultValue | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 182 | — | unknown | DSP067 Debug Data1 | DSP067DebugData1 | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 183 | — | unknown | DSP067 Debug Data2 | DSP067DebugData2 | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 184 | — | unknown | DSP067 Debug Data3 | DSP067DebugData3 | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 185 | — | unknown | DSP067 Debug Data4 | DSP067DebugData4 | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 186 | — | unknown | DSP067 Debug Data5 | DSP067DebugData5 | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 187 | — | unknown | DSP067 Debug Data6 | DSP067DebugData6 | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 188 | — | unknown | DSP067 Debug Data7 | DSP067DebugData7 | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 189 | — | unknown | DSP067 Debug Data8 | DSP067DebugData8 | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 190 | — | unknown | DSP075 Debug Data1 | DSP075DebugData1 | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 191 | — | unknown | DSP075 Debug Data2 | DSP075DebugData2 | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 192 | — | unknown | DSP075 Debug Data3 | DSP075DebugData3 | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 193 | — | unknown | DSP075 Debug Data4 | DSP075DebugData4 | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 194 | — | unknown | DSP075 Debug Data55 | DSP075DebugData5 | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 195 | — | unknown | DSP075 Debug Data6 | DSP075DebugData6 | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 196 | — | unknown | DSP075 Debug Data7 | DSP075DebugData7 | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 197 | — | unknown | DSP075 Debug Data8 | DSP075DebugData8 | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 198 | — | unknown | bUSBAgingTestOk Flag | USBAgingTestOkFlag | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 199 | — | unknown | bFlashEraseAging OkFlag | FlashEraseAgingOkFlag | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 200 | — | unknown | PVISO | PVISOValue | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 201 | — | unknown | R_DCI | RDCICurr | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 202 | — | unknown | S_DCI | SDCICurr | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 203 | — | unknown | T_DCI | TDCICurr | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 204 | — | unknown | PID_Bus | PIDBusVolt | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 205 | — | unknown | GFCI | GFCICurr | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 206 | — | unknown | SVG/APF Status+SVGAPFEq ualRatio | SVG/APFStatus+SVGAPFEqualRatio | register value | — | W | SOURCE_ONLY | source_claim | ;  |
| input | 207 | — | unknown | CT_I_R | RphaseloadsidecurrentforSVG | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 208 | — | unknown | CT_I_S | SphaseloadsidecurrentforSVG | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 209 | — | unknown | CT_I_T | TphaseloadsidecurrentforSVG | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 210 | — | unknown | CT_Q_RH | R phase load side output reactive powerforSVG(High) | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 211 | — | unknown | CT_Q_RL | R phase load side output reactive powerforSVG(low) | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 212 | — | unknown | CT_Q_SH | S phase load side output reactive powerforSVG(High) | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 213 | — | unknown | CT_Q_SL | S phase load side output reactive powerforSVG(low) | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 214 | — | unknown | CT_Q_TH | T phase load side output reactive powerforSVG(High) | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 215 | — | unknown | CT_Q_TL | T phase load side output reactive powerforSVG(low) | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 216 | — | unknown | CTHAR_I_R | Rphaseloadsideharmonic | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 217 | — | unknown | CTHAR_I_S | Sphaseloadsideharmonic | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 218 | — | unknown | CTHAR_I_T | Tphaseloadsideharmonic | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 219 | — | unknown | COMP_Q_RH | R phase compensate reactive power forSVG(High) | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 220 | — | unknown | COMP_Q_RL | R phase compensate reactive power forSVG(low) | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 221 | — | unknown | COMP_Q_SH | S phase compensate reactive power forSVG(High) | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 222 | — | unknown | COMP_Q_SL | S phase compensate reactive power | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 223 | — | unknown | COMP_Q_TH | T phase compensate reactive power forSVG(High) | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 224 | — | unknown | COMP_Q_TL | T phase compensate reactive power forSVG(low) | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 225 | — | unknown | COMPHAR_I_R | R phase compensate harmonic for SVG | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 226 | — | unknown | COMPHAR_I_S | S phase compensate harmonic for SVG | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 227 | — | unknown | COMPHAR_I_T | T phase compensate harmonic for SVG | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 228 | — | unknown | bRS232AgingTest OkFlag | RS232AgingTestOkFlag | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 229 | — | unknown | bFanFaultBit | Bit0:Fan1faultbit Bit1:Fan2faultbit Bit2:Fan3faultbit Bit3:Fan4faultbit Bit4-7:Reserved | register value | — | R | UNKNOWN_RESERVED | source_claim | ;  |
| input | 230 | — | unknown | SacH | OutputapparentpowerH | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 231 | — | unknown | SacL | OutputapparentpowerL | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 232 | — | unknown | ReActPowerH | RealOutputReactivePowerH | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 233 | — | unknown | ReActPowerL | RealOutputReactivePowerL | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 234 | — | unknown | Output reactive power | NominalOutputReactivePowerH | register value; /10 | var | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 235 | — | unknown | Output reactive power | NominalOutputReactivePowerL | register value; /10 | var | R | SOURCE_ONLY | source_claim | ;  |
| input | 236 | — | unknown | Reactive energy total | Reactivepowergeneration | register value; /10 | kvarh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 237 | — | unknown | Reactive energy total | Reactivepowergeneration | register value; /10 | kvarh | R | SOURCE_ONLY | source_claim | ;  |
| input | 238 | — | unknown | bAfciStatus | 0：Waiting 1：Self-checkstate 2：Detectpullarcstate 3：Fault 4：Update | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 239 | — | unknown | uwPresentFFTValu e[CHANNEL_A] | PresentFFTValue[CHANNEL_A] | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 240 | — | unknown | uwPresentFFTValu e[CHANNEL_B] | PresentFFTValue[CHANNEL_B] | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 241 | — | unknown | DSP067 Debug Data1 | DSP067DebugData1 | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 242 | — | unknown | DSP067 Debug Data2 | DSP067DebugData2 | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 243 | — | unknown | DSP067 Debug | DSP067DebugData3 | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 244 | — | unknown | DSP067 Debug Data4 | DSP067DebugData4 | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 245 | — | unknown | DSP067 Debug Data5 | DSP067DebugData5 | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 246 | — | unknown | DSP067 Debug Data6 | DSP067DebugData6 | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 247 | — | unknown | DSP067 Debug Data7 | DSP067DebugData7 | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 248 | — | unknown | DSP067 Debug Data8 | DSP067DebugData8 | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 249 | — | unknown | Register 249 | — | register value | reserved | R | UNKNOWN_RESERVED | source_claim | ;  |
| input | 875 | — | unknown | Vpv9 | PV9 voltage | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 876 | — | unknown | PV9Curr | PV9 Inputcurrent | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 877 | — | unknown | Ppv9H | PV9 inputpower(High) | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 878 | — | unknown | Ppv9L | PV9 inputpower(Low) | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 879 | — | unknown | Vpv10 | PV10voltage | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 880 | — | unknown | PV10Curr | PV10Inputcurrent | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 881 | — | unknown | Ppv10H | PV10inputpower(High) | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 882 | — | unknown | Ppv10L | PV10inputpower(Low) | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 883 | — | unknown | Vpv11 | PV11voltage | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 884 | — | unknown | PV11Curr | PV11Inputcurrent | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 885 | — | unknown | Ppv11H | PV11inputpower(High) | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 886 | — | unknown | Ppv11L | PV11inputpower(Low) | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 887 | — | unknown | Vpv12 | PV12voltage | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 888 | — | unknown | PV12Curr | PV12Inputcurrent | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 889 | — | unknown | Ppv12H | PV12inputpower(High) | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 890 | — | unknown | Ppv12L | PV12inputpower(Low) | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 891 | — | unknown | Vpv13 | PV13voltage | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 892 | — | unknown | PV13Curr | PV13Inputcurrent | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 893 | — | unknown | Ppv13H | PV13inputpower(High) | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 894 | — | unknown | Ppv13L | PV13inputpower(Low) | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 895 | — | unknown | Vpv14 | PV14voltage | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 896 | — | unknown | PV14Curr | PV14Inputcurrent | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 897 | — | unknown | Ppv14H | PV14inputpower(High) | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 898 | — | unknown | Ppv14L | PV14inputpower(Low) | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 899 | — | unknown | Vpv15 | PV15voltage | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 900 | — | unknown | PV15Curr | PV15Inputcurrent | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 901 | — | unknown | Ppv15H | PV15inputpower(High) | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 902 | — | unknown | Ppv15L | PV15inputpower(Low) | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 903 | — | unknown | Vpv16 | PV16voltage | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 904 | — | unknown | PV16Curr | PV16Inputcurrent | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 905 | — | unknown | Ppv16H | PV16inputpower(High) | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 906 | — | unknown | Ppv16L | PV16inputpower(Low) | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 907 | — | unknown | Epv9_todayH | PV9energytoday(High) | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 908 | — | unknown | Epv9_todayL | PV9energytoday(Low) | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 909 | — | unknown | Epv9_totalH | PV9energytotal(High) | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 910 | — | unknown | Epv9_totalL | PV9energytotal(Low) | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 911 | — | unknown | Epv10_todayH | PV10energytoday(High) | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 912 | — | unknown | Epv10_todayL | PV10energytoday(Low) | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 913 | — | unknown | Epv10_totalH | PV10energytotal(High) | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 914 | — | unknown | Epv10_totalL | PV10energytotal(Low) | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 915 | — | unknown | Epv11_todayH | PV11energytoday(High) | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 916 | — | unknown | Epv11_todayL | PV11energytoday(Low) | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 917 | — | unknown | Epv11_totalH | PV11energytotal(High) | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 918 | — | unknown | Epv11_totalL | PV11energytotal(Low) | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 919 | — | unknown | Epv12_todayH | PV12energytoday(High) | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 920 | — | unknown | Epv12_todayL | PV12energytoday(Low) | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 921 | — | unknown | Epv12_totalH | PV12energytotal(High) | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 922 | — | unknown | Epv12_totalL | PV12energytotal(Low) | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 923 | — | unknown | Epv13_todayH | PV13energytoday(High) | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 924 | — | unknown | Epv13_todayL | PV13energytoday(Low) | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 925 | — | unknown | Epv13_totalH | PV13energytotal(High) | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 926 | — | unknown | Epv13_totalL | PV13energytotal(Low) | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 927 | — | unknown | Epv14_todayH | PV14energytoday(High) | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 928 | — | unknown | Epv14_todayL | PV14energytoday(Low) | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 929 | — | unknown | Epv14_totalH | PV14energytotal(High) | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 930 | — | unknown | Epv14_totalL | PV14energytotal(Low) | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 931 | — | unknown | Epv15_todayH | PV15energytoday(High) | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 932 | — | unknown | Epv15_todayL | PV15energytoday(Low) | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 933 | — | unknown | Epv15_totalH | PV15energytotal(High) | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 934 | — | unknown | Epv15_totalL | PV15energytotal(Low) | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 935 | — | unknown | Epv16_todayH | PV16energytoday(High) | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 936 | — | unknown | Epv16_todayL | PV16energytoday(Low) | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 937 | — | unknown | Epv16_totalH | PV16energytotal(High) | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 938 | — | unknown | Epv16_totalL | PV16energytotal(Low) | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 939 | — | unknown | PIDPV9+Voltage | PID PV9PE Volt/ Flyspan voltage (MAXHV) | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 940 | — | unknown | PIDPV9+Current | PIDPV9PECurrent | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 941 | — | unknown | PID PV10+ Voltage | PID PV10PE/ Flyspan voltage (MAX HV) | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 942 | — | unknown | PID PV10+ Current | PIDPV10PECurrent | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 943 | — | unknown | PID PV11+ Voltage | PID PV11PE Volt/ Flyspan voltage (MAXHV) | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 944 | — | unknown | PID PV11+ Current | PIDPV11PECurrent | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 945 | — | unknown | PID PV12+ Voltage | PID PV12PE Volt/ Flyspan voltage (MAXHV) | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 946 | — | unknown | PID PV12+ Current | PIDPV12PECurrent | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 947 | — | unknown | PID PV13+ Voltage | PID PV13PE Volt/ Flyspan voltage (MAXHV) | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 948 | — | unknown | PID PV13+ Current | PIDPV13PECurrent | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 949 | — | unknown | PID PV14+ Voltage | PID PV14PE Volt/ Flyspan voltage (MAXHV) | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 950 | — | unknown | PID PV14+ Current | PIDPV14PECurrent | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 951 | — | unknown | PID PV15+ Voltage | PID PV15PE Volt/ Flyspan voltage (MAXHV) | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 952 | — | unknown | PID PV15+ Current | PIDPV15PECurrent | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 953 | — | unknown | PID PV16+ Voltage | PID PV16PE Volt/ Flyspan voltage (MAXHV) | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 954 | — | unknown | PID PV16+ Current | PIDPV16PECurrent | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 955 | — | unknown | V_String17 | PVString17voltage | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 956 | — | unknown | Curr_String17 | PVString17Current | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 957 | — | unknown | V_String18 | PVString18voltage | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 958 | — | unknown | Curr_String18 | PVString18Current | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 959 | — | unknown | V_String19 | PVString19voltage | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 960 | — | unknown | Curr_String19 | PVString19Current | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 961 | — | unknown | V_String20 | PVString20voltage | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 962 | — | unknown | Curr_String20 | PVString20Current | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 963 | — | unknown | V_String21 | PVString21voltage | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 964 | — | unknown | Curr_String21 | PVString21Current | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 965 | — | unknown | V_String22 | PVString22voltage | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 966 | — | unknown | Curr_String22 | PVString22Current | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 967 | — | unknown | V_String23 | PVString23voltage | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 968 | — | unknown | Curr_String23 | PVString23Current | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 969 | — | unknown | V_String24 | PVString24voltage | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 970 | — | unknown | Curr_String24 | 0.1A | register value | -15A~15A | R | SOURCE_ONLY | source_claim | ;  |
| input | 971 | — | unknown | V_String25 | 0.1V | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 972 | — | unknown | Curr_String25 | 0.1A | register value | -15A~15A | R | SOURCE_ONLY | source_claim | ;  |
| input | 973 | — | unknown | V_String26 | 0.1V | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 974 | — | unknown | Curr_String26 | 0.1A | register value | -15~15A | R | SOURCE_ONLY | source_claim | ;  |
| input | 975 | — | unknown | V_String27 | 0.1V | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 976 | — | unknown | Curr_String27 | 0.1A | register value | -15~15A | R | SOURCE_ONLY | source_claim | ;  |
| input | 977 | — | unknown | V_String28 | 0.1V | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 978 | — | unknown | Curr_String28 | 0.1A | register value | -15~15A | R | SOURCE_ONLY | source_claim | ;  |
| input | 979 | — | unknown | V_String29 | 0.1V | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 980 | — | unknown | Curr_String29 | 0.1A | register value | -15A~15A | R | SOURCE_ONLY | source_claim | ;  |
| input | 981 | — | unknown | V_String30 | 0.1V | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 982 | — | unknown | Curr_String30 | 0.1A | register value | -15~15A | R | SOURCE_ONLY | source_claim | ;  |
| input | 983 | — | unknown | V_String31 | 0.1V | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 984 | — | unknown | Curr_String31 | 0.1A | register value | -15~15A | R | SOURCE_ONLY | source_claim | ;  |
| input | 985 | — | unknown | V_String32 | 0.1V | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 986 | — | unknown | Curr_String32 | 0.1A | register value | -15~15A | R | SOURCE_ONLY | source_claim | ;  |
| input | 987 | — | unknown | StrUnmatch2 | Bit0~15:String17~32unmatch | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 988 | — | unknown | StrCurrentUnblan ce2 | Bit0~15:String 17~32 current unblance | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 989 | — | unknown | StrDisconnect2 | Bit0~15:String17~32disconnect | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 990 | — | unknown | PVWarningValue | PVWarningValue(PV9-PV16) Contains PV9~16 abnormal ， 和 Boost9~16Driveanomalies | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 991 | — | unknown | StrWaringvalue1 | string1~string16abnormal | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 992 | — | unknown | StrWaringvalue2 | string17~string32abnormal | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 993 | — | unknown | Register 993 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| input | 994 | — | unknown | Register 994 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| input | 995 | — | unknown | Register 995 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| input | 996 | — | unknown | Register 996 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| input | 997 | — | unknown | Register 997 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| input | 998 | — | unknown | Register 998 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| input | 999 | — | unknown | SystemCmd | M3toDSPsystemcommand | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 1009 | — | unknown | DischargePower | DischargePower | register value | W | UNKNOWN | SOURCE_ONLY | source_claim | ;  |
| input | 1011 | — | unknown | ChargePower | ChargePower | register value | W | UNKNOWN | SOURCE_ONLY | source_claim | ;  |
| input | 1013 | — | unknown | BatteryVoltage | BatteryVoltage | register value | V | UNKNOWN | SOURCE_ONLY | source_claim | ;  |
| input | 1014 | battery_soc | supported | SOC | SOC | register value | % | UNKNOWN | SOURCE_ONLY | source_claim | ;  |
| input | 1015 | — | unknown | ACPowerToUser | ACPowerToUser | register value | W | UNKNOWN | SOURCE_ONLY | source_claim | ;  |
| input | 1021 | — | unknown | ACPowerToUserTotal | ACPowerToUserTotal | register value | W | UNKNOWN | SOURCE_ONLY | source_claim | ;  |
| input | 1023 | — | unknown | ACPowerToGrid | ACPowerToGrid | register value | W | UNKNOWN | SOURCE_ONLY | source_claim | ;  |
| input | 1029 | — | unknown | ACPowerToGridTotal | ACPowerToGridTotal | register value | W | UNKNOWN | SOURCE_ONLY | source_claim | ;  |
| input | 1031 | — | unknown | INVPowerToLocalLoad | INVPowerToLocalLoad | register value | W | UNKNOWN | SOURCE_ONLY | source_claim | ;  |
| input | 1037 | — | unknown | INVPowerToLocalLoadTotal | INVPowerToLocalLoadTotal | register value | W | UNKNOWN | SOURCE_ONLY | source_claim | ;  |
| input | 1040 | — | unknown | BatteryTemperature | BatteryTemperature | register value | °C | UNKNOWN | SOURCE_ONLY | source_claim | ;  |
| input | 1041 | — | unknown | BatteryState | BatteryState | register value | — | UNKNOWN | SOURCE_ONLY | source_claim | ;  |
| input | 1044 | — | unknown | EnergyToUserToday | EnergyToUserToday | register value | kWh | UNKNOWN | SOURCE_ONLY | source_claim | ;  |
| input | 1046 | — | unknown | EnergyToUserTotal | EnergyToUserTotal | register value | kWh | UNKNOWN | SOURCE_ONLY | source_claim | ;  |
| input | 1048 | — | unknown | EnergyToGridToday | EnergyToGridToday | register value | kWh | UNKNOWN | SOURCE_ONLY | source_claim | ;  |
| input | 1050 | — | unknown | EnergyToGridTotal | EnergyToGridTotal | register value | kWh | UNKNOWN | SOURCE_ONLY | source_claim | ;  |
| input | 1052 | — | unknown | DischargeEnergyToday | DischargeEnergyToday | register value | kWh | UNKNOWN | SOURCE_ONLY | source_claim | ;  |
| input | 1054 | — | unknown | DischargeEnergyTotal | DischargeEnergyTotal | register value | kWh | UNKNOWN | SOURCE_ONLY | source_claim | ;  |
| input | 1056 | — | unknown | ChargeEnergyToday | ChargeEnergyToday | register value | kWh | UNKNOWN | SOURCE_ONLY | source_claim | ;  |
| input | 1058 | — | unknown | ChargeEnergyTotal | ChargeEnergyTotal | register value | kWh | UNKNOWN | SOURCE_ONLY | source_claim | ;  |
| input | 1060 | — | unknown | LocalLoadEnergyToday | LocalLoadEnergyToday | register value | kWh | UNKNOWN | SOURCE_ONLY | source_claim | ;  |
| input | 1062 | — | unknown | LocalLoadEnergyTotal | LocalLoadEnergyTotal | register value | kWh | UNKNOWN | SOURCE_ONLY | source_claim | ;  |
| input | 1124 | — | unknown | ACChargeEnergyToday | ACChargeEnergyToday | register value | kWh | UNKNOWN | SOURCE_ONLY | source_claim | ;  |
| input | 1126 | — | unknown | ACChargeEnergyTotal | ACChargeEnergyTotal | register value | kWh | UNKNOWN | SOURCE_ONLY | source_claim | ;  |

### MOD TL3-XH

Vendor/catalogue family; no model-specific live validation is claimed here.

| Table | Address | Semantic | Role | Name | Description | Encoding / scale | Unit | Access | Status | Evidence | Notes |
|---|---:|---|---|---|---|---|---|---|---|---|---|
| holding | 0 | — | unknown | Inverter Enabled | Theinvertercanbeswitched onandoff,andtheBDCcanbe switchedonandoffforthe battreadyfunction. | register value; /10 | — | R/W | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| holding | 1 | — | unknown | Safety function enable flags | SPI: system protection interface Bit0~3:forCEI0-21 Bit4~6:forSAA | register value | — | W | SOURCE_ONLY | source_claim | ;  |
| holding | 2 | — | unknown | Persist power-factor commands | Means these settings will be acting or not when next poweron | register value | — | W | RESOLVED | semantic_correlated, source_claim | ;  |
| holding | 3 | — | unknown | Active power limit setpoint | 255:powerisnotbelimited | register value; /1 | % | W | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| holding | 4 | — | unknown | Reactive power limit setpoint | 255:powerisnotbelimited | register value; /1 | % | W | SOURCE_ONLY | source_claim | ;  |
| holding | 5 | — | unknown | Power factor target | Inverter output power factor’s10000times | register value; /10000 | pf | W | SOURCE_ONLY | source_claim | ;  |
| holding | 6 | — | unknown | Rated apparent power | Normal power(high) | register value; /10 | 0.1VA | R | SOURCE_ONLY | source_claim | ;  |
| holding | 7 | — | unknown | Rated apparent power | Normal power(low) | register value; /10 | 0.1VA | R | SOURCE_ONLY | source_claim | ;  |
| holding | 8 | — | unknown | Nominal PV voltage | NormalworkPV voltage | register value; /10 | 0.1V | R | SOURCE_ONLY | source_claim | ;  |
| holding | 9 | — | unknown | Firmware | Firmwareversion (high) | firmware_version; /10 | ASCII | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| holding | 10 | — | unknown | Firmware | Firmwareversion (middle) | register value | ASCII | R | SOURCE_ONLY | source_claim | ;  |
| holding | 11 | — | unknown | Firmware | Firmwareversion(low) | register value | ASCII | R | SOURCE_ONLY | source_claim | ;  |
| holding | 12 | — | unknown | Firmware | ControlFirmware version(high) | register value | ASCII | R | SOURCE_ONLY | source_claim | ;  |
| holding | 13 | — | unknown | Firmware | ControlFirmware version(middle) | register value | ASCII | R | SOURCE_ONLY | source_claim | ;  |
| holding | 14 | — | unknown | Firmware | ControlFirmware version(low) | register value | ASCII | R | SOURCE_ONLY | source_claim | ;  |
| holding | 15 | — | unknown | LCD language selection | 0:Italian; 1:English; 2:German; 3:Spanish; 4:French; 5:Chinese; 6：Polish 7：Portugues 8：Hungary | register value | — | W | SOURCE_ONLY | source_claim | ;  |
| holding | 16 | — | unknown | Country profile configured | CountrySelectedor not | register value | — | W | SOURCE_ONLY | source_claim | ;  |
| holding | 17 | — | unknown | PV start voltage threshold | Inputstartvoltage | register value; /10 | 0.1V | W | SOURCE_ONLY | source_claim | ;  |
| holding | 18 | — | unknown | Start-up delay | Starttime | register value; /1 | 1s | W | SOURCE_ONLY | source_claim | ;  |
| holding | 19 | — | unknown | Restart delay | RestartDelayTime afterfaultback; | register value; /1 | 1s | W | SOURCE_ONLY | source_claim | ;  |
| holding | 20 | — | unknown | Active power ramp rate (startup) | Powerstartslope | register value; /10 | 0.1% | W | SOURCE_ONLY | source_claim | ;  |
| holding | 21 | — | unknown | Active power ramp rate (restart) | Powerrestartslope | register value; /10 | 0.1% | W | SOURCE_ONLY | source_claim | ;  |
| holding | 22 | — | unknown | Modbus RTU baud rate | Select communicationbaudrat e 0:9600bps 1:38400bps | register value | — | W | SOURCE_ONLY | source_claim | ;  |
| holding | 23 | — | unknown | Serial Number | The Home Assistant integration exposes this as the device serial number and reuses it as the unique identifier. | serial_number; /10 | ASCII | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| holding | 24 | — | unknown | Serial Number | The Home Assistant integration exposes this as the device serial number and reuses it as the unique identifier. | register value | ASCII | R | SOURCE_ONLY | source_claim | ;  |
| holding | 25 | — | unknown | Serial Number | The Home Assistant integration exposes this as the device serial number and reuses it as the unique identifier. | register value | ASCII | R | SOURCE_ONLY | source_claim | ;  |
| holding | 26 | — | unknown | Serial Number | The Home Assistant integration exposes this as the device serial number and reuses it as the unique identifier. | register value | ASCII | R | SOURCE_ONLY | source_claim | ;  |
| holding | 27 | — | unknown | Serial Number | The Home Assistant integration exposes this as the device serial number and reuses it as the unique identifier. | register value | ASCII | R | SOURCE_ONLY | source_claim | ;  |
| holding | 28 | — | unknown | Inverter Model | Home Assistant renders this value as the string A# B# D# T# P# U# M# S# via the integration's model() helper. Vendor spec lists value pattern `&*5`; digits appear to be stored without the leading letter codes, so treat as encoded tokens until verified on hardware. | register value; /10 | — | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| holding | 29 | — | unknown | Inverter Model | Home Assistant renders this value as the string A# B# D# T# P# U# M# S# via the integration's model() helper. Vendor spec lists value pattern `&*5`; digits appear to be stored without the leading letter codes, so treat as encoded tokens until verified on hardware. | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| holding | 30 | — | unknown | Modbus slave address | Communicate address | register value | — | W | SOURCE_ONLY | source_claim | ;  |
| holding | 31 | — | unknown | Firmware update trigger | Updatefirmware | register value | — | W | SOURCE_ONLY | source_claim | ;  |
| holding | 32 | — | unknown | Reset user configuration | Use with caution; the inverter immediately reboots and loses provisioning data. | register value | — | W | SOURCE_ONLY | source_claim | ;  |
| holding | 33 | — | unknown | Factory reset | Equivalent to the front-panel factory reset. Requires re-commissioning afterwards. | register value | — | W | SOURCE_ONLY | source_claim | ;  |
| holding | 34 | — | unknown | Manufacturer information string | The original table lists these words as Manufacturer Info 8-1 (high/middle/low); combine them to read the full string. | register value | ASCII | R | SOURCE_ONLY | source_claim | ;  |
| holding | 35 | — | unknown | Manufacturer information string | The original table lists these words as Manufacturer Info 8-1 (high/middle/low); combine them to read the full string. | register value | ASCII | R | SOURCE_ONLY | source_claim | ;  |
| holding | 36 | — | unknown | Manufacturer information string | The original table lists these words as Manufacturer Info 8-1 (high/middle/low); combine them to read the full string. | register value | ASCII | R | SOURCE_ONLY | source_claim | ;  |
| holding | 37 | — | unknown | Manufacturer information string | The original table lists these words as Manufacturer Info 8-1 (high/middle/low); combine them to read the full string. | register value | ASCII | R | SOURCE_ONLY | source_claim | ;  |
| holding | 38 | — | unknown | Manufacturer information string | The original table lists these words as Manufacturer Info 8-1 (high/middle/low); combine them to read the full string. | register value | ASCII | R | SOURCE_ONLY | source_claim | ;  |
| holding | 39 | — | unknown | Manufacturer information string | The original table lists these words as Manufacturer Info 8-1 (high/middle/low); combine them to read the full string. | register value | ASCII | R | SOURCE_ONLY | source_claim | ;  |
| holding | 40 | — | unknown | Manufacturer information string | The original table lists these words as Manufacturer Info 8-1 (high/middle/low); combine them to read the full string. | register value | ASCII | R | SOURCE_ONLY | source_claim | ;  |
| holding | 41 | — | unknown | Manufacturer information string | The original table lists these words as Manufacturer Info 8-1 (high/middle/low); combine them to read the full string. | register value | ASCII | R | SOURCE_ONLY | source_claim | ;  |
| holding | 42 | — | unknown | G100 failsafe enable | EnglishG100failsafeset | register value | — | W | SOURCE_ONLY | source_claim | ;  |
| holding | 43 | — | unknown | Device Type Code | Vendor spec provides value pattern `&*6`; handle as encoded type/family digits with implied prefixes pending confirmation. | register value; /10 | — | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| holding | 44 | — | unknown | Number Of Trackers And Phases | Inputtrackernumand outputphasenum | register value; /10 | — | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| holding | 45 | — | unknown | System clock year | Localtime | register value | — | W | SOURCE_ONLY | source_claim | ;  |
| holding | 46 | — | unknown | System clock month | Systemtime-Month | register value | — | W | SOURCE_ONLY | source_claim | ;  |
| holding | 47 | — | unknown | System clock day | Systemtime-Day | register value | — | W | SOURCE_ONLY | source_claim | ;  |
| holding | 48 | — | unknown | System clock hour | Systemtime-Hour | register value | — | W | SOURCE_ONLY | source_claim | ;  |
| holding | 49 | — | unknown | System clock minute | Systemtime-Min | register value | — | W | SOURCE_ONLY | source_claim | ;  |
| holding | 50 | — | unknown | System clock second | Systemtime-Second | register value | — | W | SOURCE_ONLY | source_claim | ;  |
| holding | 51 | — | unknown | System clock weekday | SystemWeekly | register value | — | W | SOURCE_ONLY | source_claim | ;  |
| holding | 52 | — | unknown | Stage 1 undervoltage limit | Gridvoltagelowlimit protect | register value | 0.1V | W | SOURCE_ONLY | source_claim | ;  |
| holding | 53 | — | unknown | Stage 1 overvoltage limit | Gridvoltagehighlimit protect | register value | 0.1V | W | SOURCE_ONLY | source_claim | ;  |
| holding | 54 | — | unknown | Stage 1 underfrequency limit | Gridfrequencylow limitprotect | register value | 0.01 Hz | W | SOURCE_ONLY | source_claim | ;  |
| holding | 55 | — | unknown | Stage 1 overfrequency limit | Gridhigh frequencylimitprotect | register value | 0.01 Hz | W | SOURCE_ONLY | source_claim | ;  |
| holding | 56 | — | unknown | Stage 2 undervoltage limit | Gridvoltagelowlimit protect2 | register value | 0.1V | W | SOURCE_ONLY | source_claim | ;  |
| holding | 57 | — | unknown | Stage 2 overvoltage limit | Gridvoltagehighlimit protect2 | register value | 0.1V | W | SOURCE_ONLY | source_claim | ;  |
| holding | 58 | — | unknown | Stage 2 underfrequency limit | Gridfrequencylow limitprotect2 | register value | 0.01 Hz | W | SOURCE_ONLY | source_claim | ;  |
| holding | 59 | — | unknown | Stage 2 overfrequency limit | Gridhighfrequency limitprotect2 | register value | 0.01 Hz | W | SOURCE_ONLY | source_claim | ;  |
| holding | 60 | — | unknown | Stage 3 undervoltage limit | Grid voltage low limit protect3 | register value | 0.1V | W | SOURCE_ONLY | source_claim | ;  |
| holding | 61 | — | unknown | Stage 3 overvoltage limit | Grid voltage high limit protect3 | register value | 0.1V | W | SOURCE_ONLY | source_claim | ;  |
| holding | 62 | grid_frequency | alternate | Stage 3 underfrequency limit | Grid frequency low limitprotect3 | register value | 0.01Hz | W | SOURCE_ONLY | source_claim | ; alternates: register:mod_tl3_xh:holding:63, register:mod_tl3_xh:holding:72, register:mod_tl3_xh:holding:73, register:mod_tl3_xh:holding:74, register:mod_tl3_xh:holding:75, register:mod_tl3_xh:holding:78, register:mod_tl3_xh:holding:79, register:mod_tl3_xh:input:3025 |
| holding | 63 | grid_frequency | alternate | Stage 3 overfrequency limit | Grid frequency high limitprotect3 | register value | 0.01Hz | W | SOURCE_ONLY | source_claim | ; alternates: register:mod_tl3_xh:holding:62, register:mod_tl3_xh:holding:72, register:mod_tl3_xh:holding:73, register:mod_tl3_xh:holding:74, register:mod_tl3_xh:holding:75, register:mod_tl3_xh:holding:78, register:mod_tl3_xh:holding:79, register:mod_tl3_xh:input:3025 |
| holding | 64 | — | unknown | Reconnect undervoltage limit | Gridlowvoltagelimit connecttoGrid | register value | 0.1V | W | SOURCE_ONLY | source_claim | ;  |
| holding | 65 | — | unknown | Reconnect overvoltage limit | Gridhighvoltagelimit connecttoGrid | register value | 0.1V | W | SOURCE_ONLY | source_claim | ;  |
| holding | 66 | — | unknown | Reconnect underfrequency limit | Gridlowfrequency | register value | 0.01 | W | SOURCE_ONLY | source_claim | ;  |
| holding | 67 | — | unknown | Reconnect overfrequency limit | Gridhighfrequency limitconnecttoGrid | register value | 0.01 Hz | W | SOURCE_ONLY | source_claim | ;  |
| holding | 68 | — | unknown | Stage 1 undervoltage trip delay | Grid voltage low limit protecttime 1 | register value | Cycle | W | SOURCE_ONLY | source_claim | ;  |
| holding | 69 | — | unknown | Stage 1 overvoltage trip delay | Grid voltage high limit protecttime 1 | register value | Cycle | W | SOURCE_ONLY | source_claim | ;  |
| holding | 70 | — | unknown | Stage 2 undervoltage trip delay | Grid voltage low limit protecttime 2 | register value | Cycle | W | SOURCE_ONLY | source_claim | ;  |
| holding | 71 | — | unknown | Stage 2 overvoltage trip delay | Grid voltage high limit protecttime 2 | register value | Cycle | W | SOURCE_ONLY | source_claim | ;  |
| holding | 72 | grid_frequency | alternate | Stage 1 underfrequency trip delay | Grid frequency low limitprotecttime 1 | register value | Cycle | W | SOURCE_ONLY | source_claim | ; alternates: register:mod_tl3_xh:holding:62, register:mod_tl3_xh:holding:63, register:mod_tl3_xh:holding:73, register:mod_tl3_xh:holding:74, register:mod_tl3_xh:holding:75, register:mod_tl3_xh:holding:78, register:mod_tl3_xh:holding:79, register:mod_tl3_xh:input:3025 |
| holding | 73 | grid_frequency | alternate | Modbus Version | Grid frequency high limitprotecttime 1 | register value | Cycle | W | SOURCE_ONLY | source_claim | ; alternates: register:mod_tl3_xh:holding:62, register:mod_tl3_xh:holding:63, register:mod_tl3_xh:holding:72, register:mod_tl3_xh:holding:74, register:mod_tl3_xh:holding:75, register:mod_tl3_xh:holding:78, register:mod_tl3_xh:holding:79, register:mod_tl3_xh:input:3025 |
| holding | 74 | grid_frequency | alternate | Stage 2 underfrequency trip delay | Grid frequency low limitprotecttime 2 | register value | Cycle | W | SOURCE_ONLY | source_claim | ; alternates: register:mod_tl3_xh:holding:62, register:mod_tl3_xh:holding:63, register:mod_tl3_xh:holding:72, register:mod_tl3_xh:holding:73, register:mod_tl3_xh:holding:75, register:mod_tl3_xh:holding:78, register:mod_tl3_xh:holding:79, register:mod_tl3_xh:input:3025 |
| holding | 75 | grid_frequency | alternate | Stage 2 overfrequency trip delay | Grid frequency high limitprotecttime 2 | register value | Cycle | W | SOURCE_ONLY | source_claim | ; alternates: register:mod_tl3_xh:holding:62, register:mod_tl3_xh:holding:63, register:mod_tl3_xh:holding:72, register:mod_tl3_xh:holding:73, register:mod_tl3_xh:holding:74, register:mod_tl3_xh:holding:78, register:mod_tl3_xh:holding:79, register:mod_tl3_xh:input:3025 |
| holding | 76 | — | unknown | Stage 3 undervoltage trip delay | Grid voltage low limit protecttime 3 | register value | Cycle | W | SOURCE_ONLY | source_claim | ;  |
| holding | 77 | — | unknown | Stage 3 overvoltage trip delay | Grid voltage high limit protecttime 3 | register value | Cycle | W | SOURCE_ONLY | source_claim | ;  |
| holding | 78 | grid_frequency | alternate | Stage 3 underfrequency trip delay | Grid frequency low limitprotecttime 3 | register value | Cycle | W | SOURCE_ONLY | source_claim | ; alternates: register:mod_tl3_xh:holding:62, register:mod_tl3_xh:holding:63, register:mod_tl3_xh:holding:72, register:mod_tl3_xh:holding:73, register:mod_tl3_xh:holding:74, register:mod_tl3_xh:holding:75, register:mod_tl3_xh:holding:79, register:mod_tl3_xh:input:3025 |
| holding | 79 | grid_frequency | alternate | Stage 3 overfrequency trip delay | Grid frequency high limitprotecttime 3 | register value | Cycle | W | SOURCE_ONLY | source_claim | ; alternates: register:mod_tl3_xh:holding:62, register:mod_tl3_xh:holding:63, register:mod_tl3_xh:holding:72, register:mod_tl3_xh:holding:73, register:mod_tl3_xh:holding:74, register:mod_tl3_xh:holding:75, register:mod_tl3_xh:holding:78, register:mod_tl3_xh:input:3025 |
| holding | 80 | — | unknown | Ten-minute overvoltage limit | Voltprotectionfor10 min | register value | 0.1V | W | SOURCE_ONLY | source_claim | ;  |
| holding | 81 | — | unknown | PV input high-voltage fault | PVVoltageHigh Fault | register value | 0.1V | W | SOURCE_ONLY | source_claim | ;  |
| holding | 82 | — | unknown | Controller firmware build string | Positions: 0-1 model letters, 2-3 model variant, 4-5 DSP1 build, 6-7 DSP2/M0 build, 8-9 CPLD/AFCI build, 10-11 M3 build. | register value | ASCII | R | SOURCE_ONLY | source_claim | ;  |
| holding | 83 | — | unknown | Controller firmware build string | Positions: 0-1 model letters, 2-3 model variant, 4-5 DSP1 build, 6-7 DSP2/M0 build, 8-9 CPLD/AFCI build, 10-11 M3 build. | register value | ASCII | R | SOURCE_ONLY | source_claim | ;  |
| holding | 84 | — | unknown | Controller firmware build string | Positions: 0-1 model letters, 2-3 model variant, 4-5 DSP1 build, 6-7 DSP2/M0 build, 8-9 CPLD/AFCI build, 10-11 M3 build. | register value | ASCII | R | SOURCE_ONLY | source_claim | ;  |
| holding | 85 | — | unknown | Controller firmware build string | Positions: 0-1 model letters, 2-3 model variant, 4-5 DSP1 build, 6-7 DSP2/M0 build, 8-9 CPLD/AFCI build, 10-11 M3 build. | register value | ASCII | R | SOURCE_ONLY | source_claim | ;  |
| holding | 86 | — | unknown | Controller firmware build string | Positions: 0-1 model letters, 2-3 model variant, 4-5 DSP1 build, 6-7 DSP2/M0 build, 8-9 CPLD/AFCI build, 10-11 M3 build. | register value | ASCII | R | SOURCE_ONLY | source_claim | ;  |
| holding | 87 | — | unknown | Controller firmware build string | Positions: 0-1 model letters, 2-3 model variant, 4-5 DSP1 build, 6-7 DSP2/M0 build, 8-9 CPLD/AFCI build, 10-11 M3 build. | register value | ASCII | R | SOURCE_ONLY | source_claim | ;  |
| holding | 88 | — | unknown | Modbus Version | ModbusVersion | register value; /100 | Int(16 bits) | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| holding | 89 | — | unknown | Power-factor control mode | 0=Unity PF, 1=Fixed PF setpoint, 2=Default PF line, 3=User-defined PF line, 4=Under-excited reactive power, 5=Over-excited reactive power, 6=Q(V) curve, 7=Direct control, 8=Static capacitive QV, 9=Static inductive QV. | register value | — | W | SOURCE_ONLY | source_claim | ;  |
| holding | 90 | — | unknown | GPRS modem IP/status flags | Bit 0-3: 0=idle, 1=IP read requested, 2=set IP succeeded; Bit 4-7: 0=unknown, 1=modem OK, 2=no SIM, 3=no network, 4=TCP connect fail, 5=TCP connected, etc. | register value | — | W | UNKNOWN_RESERVED | source_claim | ;  |
| holding | 91 | — | unknown | Frequency derating start | Frequencyderating startpoint | register value | 0.01H Z | W | SOURCE_ONLY | source_claim | ;  |
| holding | 92 | — | unknown | Frequency derating slope | Frequency–loadlimit rate | register value | 10tim es | W | SOURCE_ONLY | source_claim | ;  |
| holding | 93 | — | unknown | CEI 0-21 Q(V) point V1S | CEI021V1SQ(v) | register value | 0.1V | W | SOURCE_ONLY | source_claim | ;  |
| holding | 94 | — | unknown | CEI 0-21 Q(V) point V2S | CEI021V2SQ(v) | register value | 0.1V | W | SOURCE_ONLY | source_claim | ;  |
| holding | 95 | — | unknown | CEI 0-21 Q(V) point V1L | CEI021V1LQ(v) | register value | 0.1V | W | SOURCE_ONLY | source_claim | ;  |
| holding | 96 | — | unknown | CEI 0-21 Q(V) point V2L | CEI021V2LQ(v) | register value | 0.1V | W | SOURCE_ONLY | source_claim | ;  |
| holding | 97 | — | unknown | Q(V) lock-in active power | Q(v)lockinactive powerofCEI021 | register value | Percen t | W | SOURCE_ONLY | source_claim | ;  |
| holding | 98 | — | unknown | Q(V) lock-out active power | Q(v)lockOutactive powerofCEI021 | register value | Percen t | W | SOURCE_ONLY | source_claim | ;  |
| holding | 99 | — | unknown | Power-factor curve lock-in voltage | Lockingirdvoltof CEI021PFline | register value | 0.1V | W | SOURCE_ONLY | source_claim | ;  |
| holding | 100 | — | unknown | Power-factor curve lock-out voltage | Lockoutgirdvoltof CEI021PFline | register value | 0.1V | W | SOURCE_ONLY | source_claim | ;  |
| holding | 101 | — | unknown | Power-factor adjust value 1 | PFadjustvalue1 | register value | — | W | SOURCE_ONLY | source_claim | ;  |
| holding | 102 | — | unknown | Power-factor adjust value 2 | PFadjustvalue2 | register value | — | W | SOURCE_ONLY | source_claim | ;  |
| holding | 103 | — | unknown | Power-factor adjust value 3 | PFadjustvalue3 | register value | — | W | SOURCE_ONLY | source_claim | ;  |
| holding | 104 | — | unknown | Power-factor adjust value 4 | PFadjustvalue4 | register value | — | W | SOURCE_ONLY | source_claim | ;  |
| holding | 105 | — | unknown | Power-factor adjust value 5 | PFadjustvalue5 | register value | — | W | SOURCE_ONLY | source_claim | ;  |
| holding | 106 | — | unknown | Power-factor adjust value 6 | PFadjustvalue6 | register value | — | W | SOURCE_ONLY | source_claim | ;  |
| holding | 107 | — | unknown | Q(V) response delay | QV Reactive Power delaytime | register value | 1S | W | SOURCE_ONLY | source_claim | ;  |
| holding | 108 | — | unknown | Over-frequency derating delay | Overfrequency derati ngdelaytime | register value | 50ms | W | SOURCE_ONLY | source_claim | ;  |
| holding | 109 | — | unknown | Maximum reactive power magnitude | QmaxforQ(V)curve | register value | 0.1% | W | SOURCE_ONLY | source_claim | ;  |
| holding | 110 | — | unknown | PF curve point 1 load | 255meansnothispoint | register value | percen t | W | SOURCE_ONLY | source_claim | ;  |
| holding | 111 | — | unknown | PF curve point 1 target | PFlimitlinepoint1 powerfactor | register value | — | W | SOURCE_ONLY | source_claim | ;  |
| holding | 112 | — | unknown | PF curve point 2 load | 255meansnothispoint | register value | percen t | W | SOURCE_ONLY | source_claim | ;  |
| holding | 113 | — | unknown | PF curve point 2 target | PFlimitlinepoint 2powerfactor | register value | — | W | SOURCE_ONLY | source_claim | ;  |
| holding | 114 | — | unknown | PF curve point 3 load | 255meansnothispoint | register value | percen t | W | SOURCE_ONLY | source_claim | ;  |
| holding | 115 | — | unknown | PF curve point 3 target | PFlimitlinepoint3 powerfactor | register value | — | W | SOURCE_ONLY | source_claim | ;  |
| holding | 116 | — | unknown | PF curve point 4 load | 255meansnothispoint | register value | percen t | W | SOURCE_ONLY | source_claim | ;  |
| holding | 117 | — | unknown | PF curve point 4 target | PFlimitlinepoint4 powerfactor | register value | — | W | SOURCE_ONLY | source_claim | ;  |
| holding | 118 | — | unknown | Module code segments | SxxBxx | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| holding | 119 | — | unknown | Module code segments | DxxTxx | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| holding | 120 | — | unknown | Module code segments | PxxUxx | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| holding | 121 | — | unknown | Module code segments | Mxxxx Power | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| holding | 122 | — | unknown | Export limit enable mode | ExportLimitenable, 0:DisableexportLimit; 1:Enable485exportLimit; 2:Enable232exportLimit; 3:EnableCTexportLimit; | register value | — | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 123 | — | unknown | Export limit power setpoint | ExportLimitPowerRate | register value | 0.1% | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 124 | — | unknown | Tracker coupling mode | 0:Independent 1:DCSource 2:Parallel | register value | — | W | SOURCE_ONLY | source_claim | ;  |
| holding | 3000 | — | unknown | Export-limit fallback cap | Thepowerrate whenexportLimit failed | register value; /10 | 0.1% | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 3001 | — | unknown | Serial Number | Thenewmodel usesthefollowing registerstorecord theserialnumber; The representationis thesameasthe original:one registerholdstwo charactersandthe newserialnumber is30characters. | serial_number; /10 | ASCII | R/W | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| holding | 3002 | — | unknown | Serial Number | Serialnumber3-4 | register value | ASCII | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 3003 | — | unknown | Serial Number | Serialnumber5-6 | register value | ASCII | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 3004 | — | unknown | Serial Number | Serialnumber7-8 | register value | ASCII | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 3005 | — | unknown | Serial Number | Serialnumber9-10 | register value | ASCII | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 3006 | — | unknown | Serial Number | Serialnumber11-12 | register value | ASCII | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 3007 | — | unknown | Serial Number | Serialnumber13-14 | register value | ASCII | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 3008 | — | unknown | Serial Number | Serialnumber15-16 | register value | ASCII | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 3009 | — | unknown | Serial Number | Serialnumber17-18 | register value | ASCII | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 3010 | — | unknown | Serial Number | Serialnumber19-20 | register value | ASCII | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 3011 | — | unknown | Serial Number | Serialnumber21-22 | register value | ASCII | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 3012 | — | unknown | Serial Number | Serialnumber23-24 | register value | ASCII | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 3013 | — | unknown | Serial Number | Serialnumber25-26 | register value | ASCII | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 3014 | — | unknown | Serial Number | Serialnumber27-28 | register value | ASCII | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 3015 | — | unknown | Serial Number | Serialnumber29-30 | register value | ASCII | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 3016 | — | unknown | Dry-contact enable | DryContact functionenable | register value | — | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 3017 | — | unknown | Dry-contact close threshold | The power rate of drycontactturnon | register value | 0.1% | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 3018 | — | unknown | Hybrid work mode | MIN2.5~6KTL-XH/ XADoubleCT special | register value | — | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 3019 | — | unknown | Dry-contact release threshold | Drycontact closurepowerpe rcentage | register value | 0~100 0 | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 3020 | — | unknown | Off-grid box control | Leave at factory value unless instructed by Growatt support. | register value | — | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 3021 | — | unknown | External off-grid enable | 0x00: Disable; （default） 0x01:Enable; | register value | — | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 3022 | — | unknown | BDC stop-work bus voltage | BdcStopWorkOfBusVolt | register value | V | R | SOURCE_ONLY | source_claim | ;  |
| holding | 3023 | — | unknown | Grid topology selection | MIN2.5~6KTL-XH/ XADoubleCT special | register value | — | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 3024 | — | unknown | Float-charge current limit | CCcurrent | register value; /10 | 0.1A | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 3025 | — | unknown | Battery-low warning setpoint | Leadacidbattery LVvoltage | register value | 0.1V | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 3026 | — | unknown | Battery-low warning clear | Clearbatterylow voltageerror voltagepoint LoadPercent(only lead-Acid): 45.5V(Load< 20%); 48.0V(20%<=Load <=50%); 49.0V(Load> 50%); | register value | 0.1V | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 3027 | — | unknown | Battery discharge cutoff | Shouldstop dischargewhen lowerthanthis voltage(only lead-Acid): 46.0V(Load< 20%); 44.8V(20%<=Load <=50%); 44.2V(Load> 50%); | register value | 0.1V | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 3028 | — | unknown | Battery charge stop voltage | Shouldstop chargewhen higherthanthis voltage | register value; /100 | 0.01V | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 3029 | — | unknown | Battery discharge start voltage | Shouldnot dischargewhen lowerthanthis voltage | register value; /100 | 0.01V | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 3030 | — | unknown | Battery constant-charge voltage | CVvoltage（acid） canchargewhen lowerthanthis voltage | register value; /100 | 0.01V | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 3031 | — | unknown | Discharge low temperature limit | 0-200:0-20℃ 1000-1400： -40-0℃ | register value; /10 | 0.1℃ | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 3032 | — | unknown | Discharge high temperature limit | Batterytemperatureupper limitfordischarge | register value; /10 | 0.1℃ | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 3033 | — | unknown | Charge low temperature limit | Battery temperaturelower limit 0-200:0-20℃ 1000-1400： -40-0℃ | register value; /10 | 0.1℃ | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 3034 | — | unknown | Charge high temperature limit | Battery temperature upperlimit | register value; /10 | 0.1℃ | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 3035 | — | unknown | Under-frequency discharge delay | UnderFreDelay Time | register value | 50ms | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 3036 | grid_first_discharge_rate | supported | Grid-first discharge rate | DischargePowerRate whenGridFirst | register value | % | R/W | RESOLVED | semantic_correlated, source_claim | ;  |
| holding | 3037 | grid_first_stop_soc | supported | Grid-first stop SOC | StopDischargesocwhen GridFirst | register value | % | R/W | RESOLVED | semantic_correlated, source_claim | ;  |
| holding | 3038 | — | unknown | Grid-first period 1 control | Bit0~7:minutes; Bit8~12:hour; Bit13~14, 0:loadpriority; 1:batterypriority; 2:Gridpriority; Bit15, 0:prohibited;1: enabled; | register value | — | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 3039 | — | unknown | Grid-first period 1 end | Bit0~7:minutes; Bit8~12:hour; Bit13~15:reserved | register value | — | R/W | UNKNOWN_RESERVED | source_claim | ;  |
| holding | 3040 | — | unknown | Time2(xh) | Bit0~7:minutes; Bit8~12:hour; Bit13~14, 0:loadpriority; 1:batterypriority; 2:Gridpriority; Bit15, 0:prohibited;1: | register value | — | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 3041 | — | unknown | Register 3041 | Bit0~7:minutes; Bit8~12:hour; Bit13~15:reserved | register value; /10 | W | R/W | UNKNOWN_RESERVED | source_claim | ;  |
| holding | 3042 | — | unknown | Time3(xh) | WithTime1 | register value; /10 | W | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 3043 | — | unknown | Register 3043 | WithTime1 | register value; /10 | W | R/W | UNKNOWN_RESERVED | source_claim | ;  |
| holding | 3044 | — | unknown | Time4(xh) | WithTime1 | register value; /10 | W | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 3045 | — | unknown | Register 3045 | WithTime1 | register value; /10 | W | R/W | UNKNOWN_RESERVED | source_claim | ;  |
| holding | 3046 | — | unknown | Reserved | Reserved | register value; /10 | W | R | UNKNOWN_RESERVED | source_claim | ;  |
| holding | 3047 | — | unknown | BatFirstPower Rate | ChargePowerRatewhen BatFirst | register value | % | R | RESOLVED | semantic_correlated, source_claim | ;  |
| holding | 3048 | battery_soc | alternate | wBatFirststop SOC | StopChargesocwhenBat First | register value | % | R | RESOLVED | semantic_correlated, source_claim | ; alternates: register:mod_tl3_xh:input:3171, register:mod_tl3_xh:input:3196, register:mod_tl3_xh:input:3197, register:mod_tl3_xh:input:3215 |
| holding | 3049 | ac_charge_enabled | supported | AC Charge Enabled | Enable:1 Disable:0 | register value; /10 | — | R/W | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| holding | 3050 | — | unknown | Time5(xh) | WithTime1 | register value | — | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 3051 | — | unknown | Register 3051 | WithTime1 | register value; /10 | kWh | R/W | UNKNOWN_RESERVED | source_claim | ;  |
| holding | 3052 | — | unknown | Time6(xh) | WithTime1 | register value; /10 | kWh | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 3053 | — | unknown | Register 3053 | WithTime1 | register value; /10 | kWh | R/W | UNKNOWN_RESERVED | source_claim | ;  |
| holding | 3054 | — | unknown | Time7(xh) | WithTime1 | register value; /10 | kWh | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 3055 | — | unknown | Register 3055 | WithTime1 | register value; /10 | kWh | R/W | UNKNOWN_RESERVED | source_claim | ;  |
| holding | 3056 | — | unknown | Time8(xh) | WithTime1 | register value; /10 | kWh | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 3057 | — | unknown | Register 3057 | WithTime1 | register value; /10 | kWh | R/W | UNKNOWN_RESERVED | source_claim | ;  |
| holding | 3058 | — | unknown | Time9(xh) | WithTime1 | register value; /10 | kWh | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 3059 | — | unknown | Register 3059 | WithTime1 | register value; /10 | kWh | R/W | UNKNOWN_RESERVED | source_claim | ;  |
| holding | 3060 | — | unknown | Reserved | Reserved | register value; /10 | kWh | R | UNKNOWN_RESERVED | source_claim | ;  |
| holding | 3061 | — | unknown | Reserved | Reserved | register value; /10 | kWh | R | UNKNOWN_RESERVED | source_claim | ;  |
| holding | 3062 | — | unknown | Reserved | Reserved | register value; /10 | kWh | R | UNKNOWN_RESERVED | source_claim | ;  |
| holding | 3063 | — | unknown | Reserved | Reserved | register value; /10 | kWh | R | UNKNOWN_RESERVED | source_claim | ;  |
| holding | 3064 | — | unknown | Reserved | Reserved | register value; /10 | kWh | R | UNKNOWN_RESERVED | source_claim | ;  |
| holding | 3065 | — | unknown | Reserved | Reserved | register value; /10 | kWh | R | UNKNOWN_RESERVED | source_claim | ;  |
| holding | 3066 | — | unknown | Reserved | Reserved | register value; /10 | kWh | R | UNKNOWN_RESERVED | source_claim | ;  |
| holding | 3067 | — | unknown | Reserved | Reserved | register value; /10 | kWh | R | UNKNOWN_RESERVED | source_claim | ;  |
| holding | 3068 | — | unknown | Reserved | Reserved | register value; /10 | kWh | R | UNKNOWN_RESERVED | source_claim | ;  |
| holding | 3069 | — | unknown | Reserved | Reserved | register value; /10 | kWh | R | UNKNOWN_RESERVED | source_claim | ;  |
| holding | 3070 | — | unknown | BatteryType | Batterytype 0:Lithium 1:Lead-acid 2:other | register value; /10 | kWh | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 3071 | — | unknown | BatMdlSeria/ ParalNum | BatMdlSeria/Paral Num; SPH4-11Kused Theupper8bits indicatethe numberofseries segments； Thelower8bits indicatethe numberofparallel sections; | register value; /10 | kWh | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 3072 | — | unknown | Reserved | Reserved | register value; /10 | kWh | R | UNKNOWN_RESERVED | source_claim | ;  |
| holding | 3073 | — | unknown | Reserved | Reserved | register value; /10 | kWh | R | UNKNOWN_RESERVED | source_claim | ;  |
| holding | 3074 | — | unknown | Reserved | Reserved | register value; /10 | kWh | R | UNKNOWN_RESERVED | source_claim | ;  |
| holding | 3075 | — | unknown | Reserved | Reserved | register value; /10 | kWh | R | UNKNOWN_RESERVED | source_claim | ;  |
| holding | 3076 | — | unknown | Reserved | Reserved | register value; /10 | kWh | R | UNKNOWN_RESERVED | source_claim | ;  |
| holding | 3077 | — | unknown | Reserved | Reserved | register value; /10 | kWh | R | UNKNOWN_RESERVED | source_claim | ;  |
| holding | 3078 | — | unknown | Reserved | Reserved | register value; /10 | kWh | R | UNKNOWN_RESERVED | source_claim | ;  |
| holding | 3079 | — | unknown | UpsFunEn | 0:disable 1:enable | register value | bool | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 3080 | — | unknown | UPSVoltSet | 0:230V 1:208V 2:240V | register value | V | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 3081 | — | unknown | UPSFreqSet | 0:50Hz 1:60Hz | register value | Hz | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 3082 | — | unknown | bLoadFirstSto pSocSet | ratio | register value; /1 | % | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 3083 | — | unknown | Reserved | Reserved | register value; /10 | kWh | R | UNKNOWN_RESERVED | source_claim | ;  |
| holding | 3084 | — | unknown | Reserved | Reserved | register value; /10 | kWh | R | UNKNOWN_RESERVED | source_claim | ;  |
| holding | 3085 | — | unknown | Modbus slave address | 1:Communication addr=1 1~254: Communication addr=1~254 | register value | — | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 3086 | — | unknown | RS-485 baud rate | 0:9600bps 1:38400bps | register value | — | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 3087 | — | unknown | Battery rack serial | Forbattery | register value | ASCII | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 3088 | — | unknown | Battery rack serial | SerialNumber3-4 | register value | ASCII | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 3089 | — | unknown | Battery rack serial | SerialNumber5-6 | register value | ASCII | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 3090 | — | unknown | Battery rack serial | SerialNumber7-8 | register value | ASCII | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 3091 | — | unknown | Battery rack serial | SerialNumber9-10 | register value | ASCII | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 3092 | — | unknown | Battery rack serial | SerialNumber11-12 | register value | ASCII | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 3093 | — | unknown | Battery rack serial | SerialNumber13-14 | register value | ASCII | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 3094 | — | unknown | Battery rack serial | SerialNumber15-16 | register value | ASCII | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 3095 | — | unknown | BDC reset command | 0：Invaliddata 1：Resetsetting parameters 2：Resetcorrection parameter 3：Clearhistorical power | register value | — | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 3096 | — | unknown | BDC monitoring code | ZEBA | register value | ASCII | R | SOURCE_ONLY | source_claim | ;  |
| holding | 3097 | — | unknown | BDC monitoring code | Four-character identifier for the BDC monitoring firmware (e.g. ZEBA). | register value | ASCII | R | SOURCE_ONLY | source_claim | ;  |
| holding | 3098 | — | unknown | BDC DTC code | DTC | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| holding | 3099 | — | unknown | DSP firmware code | DSPsoftwarecode | register value | ASCII | R | SOURCE_ONLY | source_claim | ;  |
| holding | 3100 | — | unknown | DSP firmware code | Identifier for the inverter DSP firmware build. | register value | ASCII | R | SOURCE_ONLY | source_claim | ;  |
| holding | 3101 | — | unknown | DSP firmware version | DSPSoftwareVersion | register value | ASCII | R | SOURCE_ONLY | source_claim | ;  |
| holding | 3102 | — | unknown | Bus voltage reference | MinimumBUSvoltagefor charginganddischarging batteries | register value | V | R | SOURCE_ONLY | source_claim | ;  |
| holding | 3103 | — | unknown | BDC monitor firmware | BDCmonitoringsoftware version | register value | ASCII | R | SOURCE_ONLY | source_claim | ;  |
| holding | 3104 | — | unknown | BMS MCU hardware version | BMS hardware version information | register value | ASCII | R | SOURCE_ONLY | source_claim | ;  |
| holding | 3105 | — | unknown | BMS firmware version | BMSsoftwareversion information | register value | ASCII | R | SOURCE_ONLY | source_claim | ;  |
| holding | 3106 | — | unknown | BMS manufacturer | BMSManufacturerName | register value | ASCII | R | SOURCE_ONLY | source_claim | ;  |
| holding | 3107 | — | unknown | BMS communication interface | BMSCommunicati oninterfacetype： 0:RS485; 1:CAN; | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| holding | 3108 | — | unknown | BDC module identifier 4 | SxxBxx | register value | ASCII | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 3109 | — | unknown | BDC module identifier 3 | DxxTxx | register value | ASCII | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 3110 | — | unknown | BDC module identifier 2 | PxxUxx | register value | ASCII | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 3111 | — | unknown | BDC module identifier 1 | Mxxxx | register value | ASCII | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 3112 | — | unknown | Reserved | Reserved; reported as zero on known firmware. | register value | — | R | UNKNOWN_RESERVED | source_claim | ;  |
| holding | 3113 | — | unknown | BDC protocol version | Bit8-bit15The majorversion numberranges from0-256.In principle,itcannot bechanged Bit0-bit7Minor versionnumber [0-256].Ifthe protocolis changed,youneed toupdatethis version No. | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| holding | 3114 | — | unknown | BDC certification version | BDCCertificationVer | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| holding | 3115 | — | unknown | Reserved | Reserved for future use. | register value | — | R | UNKNOWN_RESERVED | source_claim | ;  |
| holding | 3116 | — | unknown | Reserved | Reserved for future use. | register value | — | R | UNKNOWN_RESERVED | source_claim | ;  |
| holding | 3117 | — | unknown | Reserved | Reserved for future use. | register value | — | R | UNKNOWN_RESERVED | source_claim | ;  |
| holding | 3118 | — | unknown | BDC on/off state | Indicates whether the battery DC converter is currently running (1) or idle (0). | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| holding | 3119 | — | unknown | Dry contact state | Current state of the dry-contact output (0 = open, 1 = closed). | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| holding | 3120 | — | unknown | Reserved | Reserved; reported as zero on TL-XH firmware. | register value | — | R | UNKNOWN_RESERVED | source_claim | ;  |
| holding | 3121 | — | unknown | Self-use power | Not yet surfaced by the Home Assistant integration. | register value; /10 | W | R | SOURCE_ONLY | source_claim | ;  |
| holding | 3122 | — | unknown | Self-use power | Not yet surfaced by the Home Assistant integration. | register value; /10 | W | R | SOURCE_ONLY | source_claim | ;  |
| holding | 3123 | — | unknown | System energy today | Available in firmware but not yet exposed as an integration attribute. | register value; /10 | kWh | R | SOURCE_ONLY | source_claim | ;  |
| holding | 3124 | — | unknown | System energy today | Available in firmware but not yet exposed as an integration attribute. | register value; /10 | kWh | R | SOURCE_ONLY | source_claim | ;  |
| holding | 5000 | — | unknown | Bdc Slot 1 Metadata | Repeat for additional BDCs at 40-register strides (5040-5079, 5080-5119, ). Stored as `bdc_metadata_block`. | register value | — | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 5001 | — | unknown | Bdc Slot 1 Metadata | Repeat for additional BDCs at 40-register strides (5040-5079, 5080-5119, ). Stored as `bdc_metadata_block`. | register value | — | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 5002 | — | unknown | Bdc Slot 1 Metadata | Repeat for additional BDCs at 40-register strides (5040-5079, 5080-5119, ). Stored as `bdc_metadata_block`. | register value | — | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 5003 | — | unknown | Bdc Slot 1 Metadata | Repeat for additional BDCs at 40-register strides (5040-5079, 5080-5119, ). Stored as `bdc_metadata_block`. | register value | — | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 5004 | — | unknown | Bdc Slot 1 Metadata | Repeat for additional BDCs at 40-register strides (5040-5079, 5080-5119, ). Stored as `bdc_metadata_block`. | register value | — | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 5005 | — | unknown | Bdc Slot 1 Metadata | Repeat for additional BDCs at 40-register strides (5040-5079, 5080-5119, ). Stored as `bdc_metadata_block`. | register value | — | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 5006 | — | unknown | Bdc Slot 1 Metadata | Repeat for additional BDCs at 40-register strides (5040-5079, 5080-5119, ). Stored as `bdc_metadata_block`. | register value | — | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 5007 | — | unknown | Bdc Slot 1 Metadata | Repeat for additional BDCs at 40-register strides (5040-5079, 5080-5119, ). Stored as `bdc_metadata_block`. | register value | — | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 5008 | — | unknown | Bdc Slot 1 Metadata | Repeat for additional BDCs at 40-register strides (5040-5079, 5080-5119, ). Stored as `bdc_metadata_block`. | register value | — | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 5009 | — | unknown | Bdc Slot 1 Metadata | Repeat for additional BDCs at 40-register strides (5040-5079, 5080-5119, ). Stored as `bdc_metadata_block`. | register value | — | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 5010 | — | unknown | Bdc Slot 1 Metadata | Repeat for additional BDCs at 40-register strides (5040-5079, 5080-5119, ). Stored as `bdc_metadata_block`. | register value | — | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 5011 | — | unknown | Bdc Slot 1 Metadata | Repeat for additional BDCs at 40-register strides (5040-5079, 5080-5119, ). Stored as `bdc_metadata_block`. | register value | — | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 5012 | — | unknown | Bdc Slot 1 Metadata | Repeat for additional BDCs at 40-register strides (5040-5079, 5080-5119, ). Stored as `bdc_metadata_block`. | register value | — | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 5013 | — | unknown | Bdc Slot 1 Metadata | Repeat for additional BDCs at 40-register strides (5040-5079, 5080-5119, ). Stored as `bdc_metadata_block`. | register value | — | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 5014 | — | unknown | Bdc Slot 1 Metadata | Repeat for additional BDCs at 40-register strides (5040-5079, 5080-5119, ). Stored as `bdc_metadata_block`. | register value | — | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 5015 | — | unknown | Bdc Slot 1 Metadata | Repeat for additional BDCs at 40-register strides (5040-5079, 5080-5119, ). Stored as `bdc_metadata_block`. | register value | — | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 5016 | — | unknown | Bdc Slot 1 Metadata | Repeat for additional BDCs at 40-register strides (5040-5079, 5080-5119, ). Stored as `bdc_metadata_block`. | register value | — | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 5017 | — | unknown | Bdc Slot 1 Metadata | Repeat for additional BDCs at 40-register strides (5040-5079, 5080-5119, ). Stored as `bdc_metadata_block`. | register value | — | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 5018 | — | unknown | Bdc Slot 1 Metadata | Repeat for additional BDCs at 40-register strides (5040-5079, 5080-5119, ). Stored as `bdc_metadata_block`. | register value | — | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 5019 | — | unknown | Bdc Slot 1 Metadata | Repeat for additional BDCs at 40-register strides (5040-5079, 5080-5119, ). Stored as `bdc_metadata_block`. | register value | — | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 5020 | — | unknown | Bdc Slot 1 Metadata | Repeat for additional BDCs at 40-register strides (5040-5079, 5080-5119, ). Stored as `bdc_metadata_block`. | register value | — | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 5021 | — | unknown | Bdc Slot 1 Metadata | Repeat for additional BDCs at 40-register strides (5040-5079, 5080-5119, ). Stored as `bdc_metadata_block`. | register value | — | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 5022 | — | unknown | Bdc Slot 1 Metadata | Repeat for additional BDCs at 40-register strides (5040-5079, 5080-5119, ). Stored as `bdc_metadata_block`. | register value | — | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 5023 | — | unknown | Bdc Slot 1 Metadata | Repeat for additional BDCs at 40-register strides (5040-5079, 5080-5119, ). Stored as `bdc_metadata_block`. | register value | — | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 5024 | — | unknown | Bdc Slot 1 Metadata | Repeat for additional BDCs at 40-register strides (5040-5079, 5080-5119, ). Stored as `bdc_metadata_block`. | register value | — | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 5025 | — | unknown | Bdc Slot 1 Metadata | Repeat for additional BDCs at 40-register strides (5040-5079, 5080-5119, ). Stored as `bdc_metadata_block`. | register value | — | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 5026 | — | unknown | Bdc Slot 1 Metadata | Repeat for additional BDCs at 40-register strides (5040-5079, 5080-5119, ). Stored as `bdc_metadata_block`. | register value | — | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 5027 | — | unknown | Bdc Slot 1 Metadata | Repeat for additional BDCs at 40-register strides (5040-5079, 5080-5119, ). Stored as `bdc_metadata_block`. | register value | — | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 5028 | — | unknown | Bdc Slot 1 Metadata | Repeat for additional BDCs at 40-register strides (5040-5079, 5080-5119, ). Stored as `bdc_metadata_block`. | register value | — | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 5029 | — | unknown | Bdc Slot 1 Metadata | Repeat for additional BDCs at 40-register strides (5040-5079, 5080-5119, ). Stored as `bdc_metadata_block`. | register value | — | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 5030 | — | unknown | Bdc Slot 1 Metadata | Repeat for additional BDCs at 40-register strides (5040-5079, 5080-5119, ). Stored as `bdc_metadata_block`. | register value | — | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 5031 | — | unknown | Bdc Slot 1 Metadata | Repeat for additional BDCs at 40-register strides (5040-5079, 5080-5119, ). Stored as `bdc_metadata_block`. | register value | — | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 5032 | — | unknown | Bdc Slot 1 Metadata | Repeat for additional BDCs at 40-register strides (5040-5079, 5080-5119, ). Stored as `bdc_metadata_block`. | register value | — | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 5033 | — | unknown | Bdc Slot 1 Metadata | Repeat for additional BDCs at 40-register strides (5040-5079, 5080-5119, ). Stored as `bdc_metadata_block`. | register value | — | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 5034 | — | unknown | Bdc Slot 1 Metadata | Repeat for additional BDCs at 40-register strides (5040-5079, 5080-5119, ). Stored as `bdc_metadata_block`. | register value | — | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 5035 | — | unknown | Bdc Slot 1 Metadata | Repeat for additional BDCs at 40-register strides (5040-5079, 5080-5119, ). Stored as `bdc_metadata_block`. | register value | — | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 5036 | — | unknown | Bdc Slot 1 Metadata | Repeat for additional BDCs at 40-register strides (5040-5079, 5080-5119, ). Stored as `bdc_metadata_block`. | register value | — | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 5037 | — | unknown | Bdc Slot 1 Metadata | Repeat for additional BDCs at 40-register strides (5040-5079, 5080-5119, ). Stored as `bdc_metadata_block`. | register value | — | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 5038 | — | unknown | Bdc Slot 1 Metadata | Repeat for additional BDCs at 40-register strides (5040-5079, 5080-5119, ). Stored as `bdc_metadata_block`. | register value | — | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 5039 | — | unknown | Bdc Slot 1 Metadata | Repeat for additional BDCs at 40-register strides (5040-5079, 5080-5119, ). Stored as `bdc_metadata_block`. | register value | — | R/W | SOURCE_ONLY | source_claim | ;  |
| input | 3000 | inverter_status | supported | Inverter status | Inverterrunstate High8bitsmode(specificmode) 0:Waitingmodule 1:Self-testmode,optional 2:Reserved 3：SysFault module 4:Flashmodule 5：PVBATOnlinemodule: 6：BatOnlinemodule | register value; /10 | — | R | UNKNOWN_RESERVED | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3001 | pv_total_power | supported | PV input power | PVtotalpower | register value; /10 | W | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3002 | — | unknown | PV input power | Total PV input power summed across all strings (0.1 W resolution). | register value; /10 | W | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3003 | — | unknown | PV1 DC voltage | PV1voltage | register value; /10 | V | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3004 | — | unknown | PV1 DC current | PV1inputcurrent | register value; /10 | A | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3005 | — | unknown | PV1 DC power | PV1power | register value; /10 | W | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3006 | — | unknown | PV1 DC power | Real-time DC power from PV1 computed from voltage and current readings. | register value; /10 | W | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3007 | — | unknown | PV2 DC voltage | PV2voltage | register value; /10 | V | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3008 | — | unknown | PV2 DC current | PV2inputcurrent | register value; /10 | A | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3009 | — | unknown | PV2 DC power | PV2power | register value; /10 | W | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3010 | — | unknown | PV2 DC power | Real-time DC power from PV2 computed from voltage and current readings. | register value; /10 | W | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3011 | — | unknown | PV3 DC voltage | PV3voltage | register value; /10 | V | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3012 | — | unknown | PV3 DC current | PV3inputcurrent | register value; /10 | A | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3013 | — | unknown | PV3 DC power | PV3power | register value; /10 | W | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3014 | — | unknown | PV3 DC power | Real-time DC power from PV3 computed from voltage and current readings. | register value; /10 | W | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3015 | — | unknown | PV4 DC voltage | PV4voltage | register value; /10 | V | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3016 | — | unknown | PV4 DC current | PV4inputcurrent | register value; /10 | A | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3017 | — | unknown | PV4 DC power | PV4power | register value; /10 | W | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3018 | — | unknown | PV4 DC power | Real-time DC power from PV4 computed from voltage and current readings. | register value; /10 | W | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3019 | — | unknown | System output power | Systemoutputpower | register value; /10 | W | R | RESOLVED | semantic_correlated, source_claim | ;  |
| input | 3020 | — | unknown | System output power | AC output power reported by the TL-XH mirror block (0.1 W resolution). Mirrors the value at register 35. | register value; /10 | W | R | RESOLVED | semantic_correlated, source_claim | ;  |
| input | 3021 | — | unknown | Output reactive power | reactivepower | register value; /10 | var | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3022 | — | unknown | Output reactive power | Instantaneous reactive power on the AC output (positive = inductive, negative = capacitive). | register value; /10 | var | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3023 | — | unknown | AC output power | Outputpower | register value; /10 | Output power | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3024 | — | unknown | AC output power | Active AC output power delivered by the inverter (0.1 W resolution). | register value; /10 | W | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3025 | grid_frequency | alternate | Grid frequency | Gridfrequency | register value; /100 | Grid frequency | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ; alternates: register:mod_tl3_xh:holding:62, register:mod_tl3_xh:holding:63, register:mod_tl3_xh:holding:72, register:mod_tl3_xh:holding:73, register:mod_tl3_xh:holding:74, register:mod_tl3_xh:holding:75, register:mod_tl3_xh:holding:78, register:mod_tl3_xh:holding:79 |
| input | 3026 | — | unknown | AC phase L1 voltage | Three/singlephasegridvoltage | register value; /10 | Three/single phase grid voltage | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3027 | — | unknown | AC phase L1 current | Three/singlephasegridoutputcurrent | register value; /10 | Three/single | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3028 | — | unknown | AC phase L1 power | Three/singlephasegridoutputwatt VA | register value; /10 | Three/single phasegrid outputwatt VA | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3029 | — | unknown | AC phase L1 power | Active power exported on phase L1. | register value; /10 | W | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3030 | — | unknown | AC phase L2 voltage | Threephasegridvoltage | register value; /10 | Threephase gridvoltage | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3031 | — | unknown | AC phase L2 current | Threephasegridoutputcurrent | register value; /10 | Threephase gridoutput current | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3032 | — | unknown | AC phase L2 power | Threephasegridoutputpower | register value; /10 | Threephase gridoutput power | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3033 | — | unknown | AC phase L2 power | Active power exported on phase L2. | register value; /10 | W | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3034 | — | unknown | AC phase L3 voltage | Threephasegridvoltage | register value; /10 | Threephase gridvoltage | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3035 | — | unknown | AC phase L3 current | Threephasegridoutputcurrent | register value; /10 | Threephase gridoutput current | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3036 | ac_phase_l3_power | alternate | AC phase L3 power | Threephasegridoutputpower | register value; /10 | Threephase gridoutput power | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ; alternates: register:mod_tl3_xh:input:3037, register:mod_tl3_xh:input:3156, register:mod_tl3_xh:input:3157 |
| input | 3037 | ac_phase_l3_power | alternate | AC phase L3 power | Active power exported on phase L3. | register value; /10 | W | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ; alternates: register:mod_tl3_xh:input:3036, register:mod_tl3_xh:input:3156, register:mod_tl3_xh:input:3157 |
| input | 3038 | — | unknown | RS line voltage | Threephasegridvoltage | register value; /10 | V | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3039 | — | unknown | ST line voltage | Threephasegridvoltage | register value; /10 | V | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3040 | — | unknown | TR line voltage | Threephasegridvoltage | register value; /10 | V | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3041 | grid_import_power | supported | Load supply power | Totalforwardpower | register value; /10 | Total forward power | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3042 | — | unknown | Load supply power | Real-time active power delivered to on-site (self-consumption) loads. | register value; /10 | W | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3043 | grid_export_power | alternate | Grid export power | Totalreversepower | register value; /10 | Totalreverse power | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ; alternates: register:mod_tl3_xh:input:3044, register:mod_tl3_xh:input:3071, register:mod_tl3_xh:input:3072, register:mod_tl3_xh:input:3073, register:mod_tl3_xh:input:3074 |
| input | 3044 | grid_export_power | alternate | Grid export power | Active power exported to the utility grid. | register value; /10 | W | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ; alternates: register:mod_tl3_xh:input:3043, register:mod_tl3_xh:input:3071, register:mod_tl3_xh:input:3072, register:mod_tl3_xh:input:3073, register:mod_tl3_xh:input:3074 |
| input | 3045 | house_load_power | supported | Home load power | Totalloadpower | register value; /10 | Total load power | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3046 | — | unknown | Home load power | Aggregate instantaneous demand from on-site loads. | register value; /10 | W | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3047 | inverter_runtime | supported | Run time | Raw counter counts seconds; divide by 7200 to obtain hours. | register value; /7200 | h | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3048 | — | unknown | Run time | Raw counter counts seconds; divide by 7200 to obtain hours. | register value; /7200 | h | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3049 | — | unknown | Output energy today | Todaygenerateenergy | register value; /10 | Today generate energy | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3050 | — | unknown | Output energy today | Energy exported to the AC output today (0.1 kWh resolution). | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3051 | — | unknown | Output energy total | Totalgenerateenergy | register value; /10 | Total generate | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3052 | — | unknown | Output energy total | Lifetime AC output energy (0.1 kWh resolution). | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3053 | — | unknown | PV energy total | PVenergytotal | register value; /10 | PVenergy total | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3054 | — | unknown | PV energy total | Total PV energy generated across all strings (0.1 kWh resolution). | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3055 | — | unknown | PV1 energy today | PV1energytoday | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3056 | — | unknown | PV1 energy today | Energy harvested by PV1 today. Values use 0.1 kWh resolution. | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3057 | — | unknown | PV1 energy total | PV1energytotal | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3058 | — | unknown | PV1 energy total | Lifetime energy harvested by PV1. Values use 0.1 kWh resolution. | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3059 | — | unknown | PV2 energy today | PV2energytoday | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3060 | — | unknown | PV2 energy today | Energy harvested by PV2 today. Values use 0.1 kWh resolution. | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3061 | — | unknown | PV2 energy total | PV2energytotal | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3062 | — | unknown | PV2 energy total | Lifetime energy harvested by PV2. Values use 0.1 kWh resolution. | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3063 | — | unknown | PV3 energy today | PV3energytoday | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3064 | — | unknown | PV3 energy today | Energy harvested by PV3 today. Values use 0.1 kWh resolution. | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3065 | — | unknown | PV3 energy total | PV3energytotal | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3066 | — | unknown | PV3 energy total | Lifetime energy harvested by PV3. Values use 0.1 kWh resolution. | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3067 | — | unknown | Load energy today | Todayenergytouser | register value; /10 | Todayenergy touser | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3068 | — | unknown | Load energy today | Energy delivered to on-site loads today (0.1 kWh resolution). | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3069 | — | unknown | Load energy total | Totalenergytouser | register value; /10 | Totalenergy touser | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3070 | — | unknown | Load energy total | Lifetime energy delivered to on-site loads (0.1 kWh resolution). | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3071 | grid_export_power | alternate | Export energy today | Todayenergytogrid | register value; /10 | Todayenergy togrid | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ; alternates: register:mod_tl3_xh:input:3043, register:mod_tl3_xh:input:3044, register:mod_tl3_xh:input:3072, register:mod_tl3_xh:input:3073, register:mod_tl3_xh:input:3074 |
| input | 3072 | grid_export_power | alternate | Export energy today | Energy exported to the grid today (0.1 kWh resolution). | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ; alternates: register:mod_tl3_xh:input:3043, register:mod_tl3_xh:input:3044, register:mod_tl3_xh:input:3071, register:mod_tl3_xh:input:3073, register:mod_tl3_xh:input:3074 |
| input | 3073 | grid_export_power | alternate | Export energy total | Totalenergytogrid | register value; /10 | Totalenergy togrid | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ; alternates: register:mod_tl3_xh:input:3043, register:mod_tl3_xh:input:3044, register:mod_tl3_xh:input:3071, register:mod_tl3_xh:input:3072, register:mod_tl3_xh:input:3074 |
| input | 3074 | grid_export_power | alternate | Export energy total | Lifetime energy exported to the grid (0.1 kWh resolution). | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ; alternates: register:mod_tl3_xh:input:3043, register:mod_tl3_xh:input:3044, register:mod_tl3_xh:input:3071, register:mod_tl3_xh:input:3072, register:mod_tl3_xh:input:3073 |
| input | 3075 | — | unknown | User load energy today | Todayenergyofuserload | register value; /10 | Todayenergy ofuserload | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3076 | — | unknown | User load energy today | Energy delivered to on-site loads today (0.1 kWh resolution). | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3077 | — | unknown | User load energy total | Totalenergyofuserload | register value; /10 | Totalenergy ofuserload | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3078 | — | unknown | User load energy total | Lifetime energy delivered to on-site loads (0.1 kWh resolution). | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3079 | — | unknown | PV4 energy today | PV4energytoday | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3080 | — | unknown | PV4 energy today | Energy harvested by PV string 4 today (0.1 kWh resolution). | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3081 | pv4_energy_total | alternate | PV4 energy total | PV4energytotal | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ; alternates: register:mod_tl3_xh:input:3082 |
| input | 3082 | pv4_energy_total | alternate | PV4 energy total | Lifetime energy harvested by PV string 4 (0.1 kWh resolution). | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ; alternates: register:mod_tl3_xh:input:3081 |
| input | 3083 | — | unknown | PV energy today | PVenergytoday | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3084 | — | unknown | PV energy today | Total PV energy harvested across all strings today (0.1 kWh resolution). | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3085 | — | unknown | Reserved | Reserved | register value; /1 | — | R | UNKNOWN_RESERVED | semantic_correlated, source_claim | ;  |
| input | 3086 | — | unknown | Derating mode | DeratingMode | register value; /1 | 0:cNOTDerate 1:cPVHighDer ate 2: cPowerCon stantDerate 3: cGridVHigh Derate 4:cFreqHighD erate 5:cDcSoureM odeDerate 6:cInvTemprD erate 7:cActivePow erOrder 8:cLoadSpeed Process 9:cOverBack byTime 10:cInternalT emprDerate 11:cOutTemp rDerate 12:cLineImpe CalcDerate 13: cParallelA ntiBackflowD erate 14:cLocalAnti BackflowDera te 15:cBdcLoadP riDerate 16:cChkCTErr Derate | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3087 | — | unknown | PV insulation resistance | PVISOvalue | register value; /1 | kΩ | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3088 | — | unknown | Residual current R | RDCICurr | register value; /10 | mA | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3089 | — | unknown | Residual current S | SDCICurr | register value; /10 | mA | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3090 | — | unknown | Residual current T | TDCICurr | register value; /10 | mA | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3091 | — | unknown | GFCI current | GFCICurr | register value; /1 | mA | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3092 | — | unknown | Total bus voltage | totalbusvoltage | register value; /10 | V | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3093 | — | unknown | Inverter temperature | Invertertemperature | register value; /10 | °C | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3094 | — | unknown | IPM temperature | TheinsideIPMininvertertemperature | register value; /10 | °C | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3095 | — | unknown | Boost temperature | Boosttemperature | register value; /10 | °C | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3096 | — | unknown | Temp4 | Reserved | register value; /10 | — | R | UNKNOWN_RESERVED | semantic_correlated, source_claim | ;  |
| input | 3097 | — | unknown | Communication board temperature | Commmunicationbroadtemperature | register value; /10 | °C | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3098 | — | unknown | P-bus voltage | PBusinsideVoltage | register value; /10 | V | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3099 | — | unknown | N-bus voltage | NBusinsideVoltage | register value; /10 | V | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3100 | — | unknown | Inverter output power factor | InverteroutputPFnow | register value; /1 | 0-20000 | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3101 | — | unknown | Output power percentage | RealOutputpowerPercent | register value; /1 | 1~100 | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3102 | — | unknown | Output max power limit | OutputMaxpowerLimited | register value; /10 | Output Maxpower Limited | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3103 | — | unknown | Output max power limit | Current active output power limit enforced by the inverter (0.1 W resolution). | register value; /10 | W | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3104 | — | unknown | Standby flags | Inverterstandbyflag | register value; /1 | bit0:turn off Order； bit1:PVLow； bit2:AC Volt/Freq outofscope； bit3~bit7 ： Reserved | R | RESOLVED | semantic_correlated, source_claim | ;  |
| input | 3105 | — | unknown | Fault code | Inverterfaultmaincode | register value; /1 | — | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3106 | — | unknown | Warning main code | InverterWarningmaincode | register value; /1 | — | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3107 | — | unknown | Fault subcode | Inverterfaultsubcode | register value; /1 | — | R | RESOLVED | semantic_correlated, source_claim | ;  |
| input | 3108 | — | unknown | Warning subcode | InverterWarningsubcode | register value; /1 | — | R | RESOLVED | semantic_correlated, source_claim | ;  |
| input | 3109 | — | unknown | Register 3109 | — | register value; /1 | — | R | UNKNOWN_RESERVED | semantic_correlated, source_claim | ;  |
| input | 3110 | — | unknown | Warning code | Current inverter warning code (vendor-defined bitmask). | register value; /1 | — | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3111 | — | unknown | Warning code | PresentFFTValue[CHANNEL_A] | register value; /1 | — | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3112 | — | unknown | AFCI status | AFCIStatus | register value; /1 | 0 ： waiting state 1：self-check 2：Detection of arcing state 3：faultstate 4 ： update state | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3113 | — | unknown | AFCI strength (channel A) | AFCIStrength[CHANNEL_A] | register value; /1 | — | R | RESOLVED | semantic_correlated, source_claim | ;  |
| input | 3114 | — | unknown | AFCI self-check (channel A) | AFCISelfCheck[CHANNEL_A] | register value; /1 | — | R | RESOLVED | semantic_correlated, source_claim | ;  |
| input | 3115 | — | unknown | Inverter start delay | invstartdelaytime | register value; /1 | invstartdelay time | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3116 | — | unknown | Reserved | Reserved | register value; /1 | — | R | UNKNOWN_RESERVED | semantic_correlated, source_claim | ;  |
| input | 3117 | — | unknown | Reserved | Reserved | register value; /1 | — | R | UNKNOWN_RESERVED | semantic_correlated, source_claim | ;  |
| input | 3118 | — | unknown | BDC connect state | BDCconnectstate | register value; /1 | 0:No BDC Connect 1:BDC1 Connect 2:BDC2 Connect 3:BDC1+BDC2 Connect | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3119 | — | unknown | Dry contact state | CurrentstatusofDryContact | register value; /1 | Current status of DryContact 0:turnoff; 1:turnon; | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3120 | — | unknown | Reserved | Reserved | register value; /1 | — | R | UNKNOWN_RESERVED | semantic_correlated, source_claim | ;  |
| input | 3121 | — | unknown | Self-use power | self-usepower | register value; /10 | W | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3122 | — | unknown | Self-use power | Real-time power consumed by on-site loads (0.1 W resolution). | register value; /10 | W | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3123 | — | unknown | System energy today | Systemenergytoday | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3124 | — | unknown | System energy today | Total energy processed by the hybrid system today (0.1 kWh resolution). | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3125 | — | unknown | Battery discharge today | Todaydischargeenergy | register value; /10 | Today discharge energy | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3126 | — | unknown | Battery discharge today | Energy discharged from the battery into the AC system today (0.1 kWh resolution). | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3127 | — | unknown | Battery discharge total | Totaldischargeenergy | register value; /10 | Total discharge energy | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3128 | — | unknown | Battery discharge total | Total energy discharged from the battery (0.1 kWh resolution). | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3129 | — | unknown | Battery charge today | Chargeenergytoday | register value; /10 | Charge energytoday | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3130 | — | unknown | Battery charge today | Energy charged into the battery today (0.1 kWh resolution). | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3131 | — | unknown | Battery charge total | Chargeenergytotal | register value; /10 | Charge energytotal | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3132 | — | unknown | Battery charge total | Total energy charged into the battery (0.1 kWh resolution). | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3133 | — | unknown | AC charge energy today | TodayenergyofACcharge | register value; /10 | Todayenergy ofACcharge | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3134 | — | unknown | AC charge energy today | Energy charged into the battery from AC today (0.1 kWh resolution). | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3135 | — | unknown | AC charge energy total | TotalenergyofACcharge | register value; /10 | Totalenergy ofACcharge | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3136 | — | unknown | AC charge energy total | Lifetime energy charged into the battery from AC (0.1 kWh resolution). | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3137 | — | unknown | System energy total | Lifetime hybrid system energy throughput (0.1 kWh resolution). | register value; /1 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3138 | — | unknown | System energy total | Totalenergyofsystemoutput\ | register value; /1 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3139 | — | unknown | Self-use energy today | TodayenergyofSelfoutput | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3140 | — | unknown | Self-use energy today | Energy supplied to on-site loads today (0.1 kWh resolution). | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3141 | — | unknown | Self-use energy total | TotalenergyofSelfoutput | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3142 | — | unknown | Self-use energy total | Lifetime energy supplied to on-site loads (0.1 kWh resolution). | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3143 | — | unknown | Reserved | Reserved | register value; /1 | — | R | UNKNOWN_RESERVED | semantic_correlated, source_claim | ;  |
| input | 3144 | — | unknown | Priority mode | WordMode | register value | 0 LoadFirst 1 BatteryFirs t 2 GridFirst | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3145 | — | unknown | EPS frequency | UPSfrequency | register value | Hz | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3146 | — | unknown | EPS phase R voltage | UPSphaseRoutputvoltage | register value; /10 | V | R | RESOLVED | semantic_correlated, source_claim | ;  |
| input | 3147 | — | unknown | EPS phase R current | UPSphaseRoutputcurrent | register value; /10 | A | R | RESOLVED | semantic_correlated, source_claim | ;  |
| input | 3148 | — | unknown | EPS phase R apparent power | UPSphaseRoutputpower | register value | VA | R | SOURCE_ONLY | source_claim | ;  |
| input | 3149 | — | unknown | EPS phase R apparent power | Phase R apparent power on the EPS output (0.1 VA resolution). | register value | VA | R | SOURCE_ONLY | source_claim | ;  |
| input | 3150 | — | unknown | EPS phase S voltage | UPSphaseSoutputvoltage | register value; /10 | V | R | RESOLVED | semantic_correlated, source_claim | ;  |
| input | 3151 | — | unknown | EPS phase S current | UPSphaseSoutputcurrent | register value; /10 | A | R | RESOLVED | semantic_correlated, source_claim | ;  |
| input | 3152 | — | unknown | EPS phase S apparent power | UPSphaseSoutputpower | register value; /10 | VA | R | RESOLVED | semantic_correlated, source_claim | ;  |
| input | 3153 | — | unknown | EPS phase S apparent power | Phase S apparent power on the EPS output (0.1 VA resolution). | register value; /10 | VA | R | RESOLVED | semantic_correlated, source_claim | ;  |
| input | 3154 | — | unknown | EPS phase T voltage | UPSphaseToutputvoltage | register value; /10 | V | R | RESOLVED | semantic_correlated, source_claim | ;  |
| input | 3155 | — | unknown | EPS phase T current | UPSphaseToutputcurrent | register value; /10 | A | R | RESOLVED | semantic_correlated, source_claim | ;  |
| input | 3156 | ac_phase_l3_power | alternate | EPS phase T apparent power | UPSphaseToutputpower | register value; /10 | VA | R | RESOLVED | semantic_correlated, source_claim | ; alternates: register:mod_tl3_xh:input:3036, register:mod_tl3_xh:input:3037, register:mod_tl3_xh:input:3157 |
| input | 3157 | ac_phase_l3_power | alternate | EPS phase T apparent power | Phase T apparent power on the EPS output (0.1 VA resolution). | register value; /10 | VA | R | RESOLVED | semantic_correlated, source_claim | ; alternates: register:mod_tl3_xh:input:3036, register:mod_tl3_xh:input:3037, register:mod_tl3_xh:input:3156 |
| input | 3158 | — | unknown | EPS total apparent power | UPSoutputpower | register value; /10 | VA | R | RESOLVED | semantic_correlated, source_claim | ;  |
| input | 3159 | — | unknown | EPS total apparent power | Total apparent power delivered by the EPS output (0.1 VA resolution). | register value; /10 | VA | R | RESOLVED | semantic_correlated, source_claim | ;  |
| input | 3160 | — | unknown | EPS load percentage | LoadpercentofUPSouput | register value; /10 | % | R | RESOLVED | semantic_correlated, source_claim | ;  |
| input | 3161 | — | unknown | BDC power factor | Powerfactor | register value; /10 | pf | R | RESOLVED | semantic_correlated, source_claim | ;  |
| input | 3162 | — | unknown | BDC DC voltage | DCvoltage | register value; /1 | V | R | RESOLVED | semantic_correlated, source_claim | ;  |
| input | 3163 | — | unknown | Reserved | Reserved | register value; /1 | — | R | UNKNOWN_RESERVED | semantic_correlated, source_claim | ;  |
| input | 3164 | — | unknown | BDC presence flag | WhethertoparseBDCdataseparately | register value; /1 | 0:Don'tneed 1：need | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3165 | — | unknown | BDC derating mode | BDCDeratingMode： 0:Normal,unrestricted 1：Standbyorfault 2：Maximumbatterycurrentlimit (discharge) 3：BatterydischargeEnable(Discharge) 4：Highbusdischargederating | register value; /1 | — | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3166 | — | unknown | BDC system mode | SystemworkStateandmodeThe upper8bitsindicatethemode; 0：Nochargeanddischarge； 1：charge； 2：Discharge； Thelower8bitsrepresentthestatus; 0:StandbyStatus; 1:NormalStatus; 2:FaultStatus 3：FlashStatus; | register value; /1 | BDC1 | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3167 | — | unknown | BDC fault code | Storgedevicefaultcode | register value; /1 | — | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3168 | — | unknown | BDC warning code | Storgedevicewarningcode | register value; /1 | — | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3169 | battery_voltage | alternate | Battery voltage | Batteryvoltage | register value; /100 | V | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ; alternates: register:mod_tl3_xh:input:3216 |
| input | 3170 | battery_current | alternate | Battery current | Batterycurrent | register value; /10 | A | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ; alternates: register:mod_tl3_xh:input:3217 |
| input | 3171 | battery_soc | alternate | Battery SOC | StateofchargeCapacity | register value; /1 | % | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ; alternates: register:mod_tl3_xh:holding:3048, register:mod_tl3_xh:input:3196, register:mod_tl3_xh:input:3197, register:mod_tl3_xh:input:3215 |
| input | 3172 | — | unknown | VBUS1 voltage | TotalBUSvoltage | register value; /10 | V | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3173 | — | unknown | VBUS2 voltage | OntheBUSvoltage | register value; /10 | V | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3174 | — | unknown | Buck/boost current | BUCK-BOOSTCurrent | register value; /10 | A | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3175 | — | unknown | LLC stage current | LLCCurrent | register value; /10 | A | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3176 | — | unknown | Battery temperature A | TempertureA | register value; /10 | °C | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3177 | — | unknown | Battery temperature B | TempertureB | register value; /10 | °C | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3178 | battery_discharge_power | alternate | Battery discharge power | Dischargepower | register value; /10 | W | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ; alternates: register:mod_tl3_xh:input:3179 |
| input | 3179 | battery_discharge_power | alternate | Battery discharge power | Real-time discharge power flowing from the battery (0.1 W resolution). | register value; /10 | W | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ; alternates: register:mod_tl3_xh:input:3178 |
| input | 3180 | battery_charge_power | alternate | Battery charge power | Chargepower | register value; /10 | W | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ; alternates: register:mod_tl3_xh:input:3181 |
| input | 3181 | battery_charge_power | alternate | Battery charge power | Real-time charge power flowing into the battery (0.1 W resolution). | register value; /10 | W | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ; alternates: register:mod_tl3_xh:input:3180 |
| input | 3182 | — | unknown | BDC discharge energy total | Dischargetotalenergyofstorgedevice | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3183 | — | unknown | BDC discharge energy total | Lifetime energy discharged by the battery DC converter (0.1 kWh resolution). | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3184 | — | unknown | BDC charge energy total | Chargetotalenergyofstorgedevice | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3185 | — | unknown | BDC charge energy total | Lifetime energy charged into the battery via the BDC (0.1 kWh resolution). | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3186 | — | unknown | Reserved | Reserved | register value; /1 | — | R | UNKNOWN_RESERVED | semantic_correlated, source_claim | ;  |
| input | 3187 | — | unknown | BDC flag word | BDCmark(chargeanddischarge, faultalarmcode) Bit0:ChargeEn;BDCallowscharging Bit1:DischargeEn;BDCallows discharge Bit2~7:Resvd;reserved Bit8~11:WarnSubCode;BDC sub-warningcode Bit12~15:FaultSubCode;BDC sub-errorcode | register value; /1 | — | R | UNKNOWN_RESERVED | semantic_correlated, source_claim | ;  |
| input | 3188 | — | unknown | VBUS2 low voltage | LowerBUSvoltage | register value; /10 | V | R | RESOLVED | semantic_correlated, source_claim | ;  |
| input | 3189 | — | unknown | BMS max cell index | BmsMaxVoltCellNo | register value; /1 | — | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3190 | — | unknown | BMS min cell index | BmsMinVoltCellNo | register value; /1 | — | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3191 | — | unknown | BMS average temperature A | BmsBatteryAvgTemp | register value; /1 | °C | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3192 | — | unknown | BMS max cell temperature A | BmsMaxCellTemp | register value; /10 | °C | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3193 | — | unknown | BMS average temperature B | BmsBatteryAvgTemp | register value; /10 | °C | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3194 | — | unknown | BMS max cell temperature B | BmsMaxCellTemp | register value; /1 | °C | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3195 | — | unknown | BMS average temperature C | BmsBatteryAvgTemp | register value; /1 | °C | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3196 | battery_soc | alternate | BMS max SOC | BmsMaxSOC | register value; /1 | % | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ; alternates: register:mod_tl3_xh:holding:3048, register:mod_tl3_xh:input:3171, register:mod_tl3_xh:input:3197, register:mod_tl3_xh:input:3215 |
| input | 3197 | battery_soc | alternate | BMS min SOC | BmsMinSOC | register value; /1 | % | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ; alternates: register:mod_tl3_xh:holding:3048, register:mod_tl3_xh:input:3171, register:mod_tl3_xh:input:3196, register:mod_tl3_xh:input:3215 |
| input | 3198 | — | unknown | Parallel battery count | ParallelBatteryNum | register value; /1 | — | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3199 | — | unknown | BMS derate reason | BmsDerateReason | register value; /1 | — | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3200 | — | unknown | BMS full charge capacity | BmsGaugeFCC（Ah） | register value; /1 | Ah | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3201 | — | unknown | BMS remaining capacity | BmsGaugeRM（Ah） | register value; /1 | Ah | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3202 | — | unknown | BMS protect flags 1 | BMSProtect1 | register value; /1 | — | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3203 | — | unknown | BMS warning flags 1 | BMSWarn1 | register value; /1 | — | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3204 | — | unknown | BMS fault flags 1 | BMSFault1 | register value; /1 | — | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3205 | — | unknown | BMS fault flags 2 | BMSFault2 | register value; /1 | — | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3206 | — | unknown | Reserved | Reserved | register value; /1 | — | R | UNKNOWN_RESERVED | semantic_correlated, source_claim | ;  |
| input | 3207 | — | unknown | Reserved | Reserved | register value; /1 | — | R | UNKNOWN_RESERVED | semantic_correlated, source_claim | ;  |
| input | 3208 | — | unknown | Reserved | Reserved | register value; /1 | — | R | UNKNOWN_RESERVED | semantic_correlated, source_claim | ;  |
| input | 3209 | — | unknown | Reserved | Reserved | register value; /1 | — | R | UNKNOWN_RESERVED | semantic_correlated, source_claim | ;  |
| input | 3210 | — | unknown | Battery insulation status | BatteryISOdetectionstatus | register value; /1 | 0：Not detected 1：Detection completed | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3211 | — | unknown | Battery request flags | batteryworkrequest | register value; /1 | — | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3212 | — | unknown | BMS status | batteryworkingstatus | register value; /1 | 0:dormancy 1:Charge 2:Discharge 3:free 4:standby 5:Softstart 6:fault 7:update | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3213 | — | unknown | BMS protect flags 2 | BMSProtect2 | register value; /1 | — | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3214 | — | unknown | BMS warning flags 2 | BMSWarn2 | register value; /1 | — | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3215 | battery_soc | alternate | BMS SOC | BMSSOC | register value; /1 | % | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ; alternates: register:mod_tl3_xh:holding:3048, register:mod_tl3_xh:input:3171, register:mod_tl3_xh:input:3196, register:mod_tl3_xh:input:3197 |
| input | 3216 | battery_voltage | alternate | BMS battery voltage | BMSBatteryVolt | register value; /100 | V | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ; alternates: register:mod_tl3_xh:input:3169 |
| input | 3217 | battery_current | alternate | BMS battery current | Positive values indicate discharge from the battery; negative values indicate charging. | register value; /100 | A | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ; alternates: register:mod_tl3_xh:input:3170 |
| input | 3218 | — | unknown | BMS max cell temperature | batterycellmaximumtemperature | register value; /10 | °C | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3219 | — | unknown | BMS max charge current | Maximumchargingcurrent | register value; /100 | A | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3220 | — | unknown | BMS max discharge current | Maximumdischargecurrent | register value; /100 | A | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3221 | — | unknown | BMS cycle count | BMSCycleCnt | register value; /1 | — | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3222 | — | unknown | BMS state of health | BMSSOH | register value; /1 | % | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3223 | — | unknown | BMS charge voltage limit | Batterychargingvoltagelimitvalue | register value; /100 | V | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3224 | — | unknown | BMS discharge voltage limit | Batterydischargevoltagelimitvalue | register value; /1 | V | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3225 | — | unknown | BMS warning flags 3 | BMSWarn3 | register value; /1 | — | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3226 | — | unknown | BMS protect flags 3 | BMSProtect3 | register value; /1 | — | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3227 | — | unknown | Reserved | Reserved | register value; /1 | — | R | UNKNOWN_RESERVED | semantic_correlated, source_claim | ;  |
| input | 3228 | — | unknown | Reserved | Reserved | register value; /1 | — | R | UNKNOWN_RESERVED | semantic_correlated, source_claim | ;  |
| input | 3229 | — | unknown | Reserved | Reserved | register value; /1 | — | R | UNKNOWN_RESERVED | semantic_correlated, source_claim | ;  |
| input | 3230 | — | unknown | BMS max cell voltage | BMSBatterySingleVoltMax | register value; /1 | V | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3231 | — | unknown | BMS min cell voltage | BMSBatterySingleVoltMin | register value; /1 | V | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3232 | — | unknown | Battery load voltage | BatteryLoadVolt | register value; /100 | [0，650.00] | R | RESOLVED | semantic_correlated, source_claim | ;  |
| input | 3233 | — | unknown | Register 3233 | — | register value; /1 | — | R | UNKNOWN_RESERVED | semantic_correlated, source_claim | ;  |
| input | 3234 | — | unknown | Debug data 1 | Debugdata1 | register value; /1 | — | R | RESOLVED | semantic_correlated, source_claim | ;  |
| input | 3235 | — | unknown | Debug data 2 | Debugdata2 | register value; /1 | — | R | RESOLVED | semantic_correlated, source_claim | ;  |
| input | 3236 | — | unknown | Debug data 3 | Debugdata3 | register value; /1 | — | R | RESOLVED | semantic_correlated, source_claim | ;  |
| input | 3237 | — | unknown | Debug data 4 | Debugdata4 | register value; /1 | — | R | RESOLVED | semantic_correlated, source_claim | ;  |
| input | 3238 | — | unknown | Debug data 5 | Debugdata5 | register value; /1 | — | R | RESOLVED | semantic_correlated, source_claim | ;  |
| input | 3239 | — | unknown | Debug data 6 | Debugdata6 | register value; /1 | — | R | RESOLVED | semantic_correlated, source_claim | ;  |
| input | 3240 | — | unknown | Debug data 7 | Debugdata7 | register value; /1 | — | R | RESOLVED | semantic_correlated, source_claim | ;  |
| input | 3241 | — | unknown | Debug data 8 | Debugdata8 | register value; /1 | — | R | RESOLVED | semantic_correlated, source_claim | ;  |
| input | 3242 | — | unknown | Debug data 9 | Debugdata9 | register value; /1 | — | R | RESOLVED | semantic_correlated, source_claim | ;  |
| input | 3243 | — | unknown | Debug data 10 | Debugdata10 | register value; /1 | — | R | RESOLVED | semantic_correlated, source_claim | ;  |
| input | 3244 | — | unknown | Debug data 11 | Debugdata10 | register value; /1 | — | R | RESOLVED | semantic_correlated, source_claim | ;  |
| input | 3245 | — | unknown | Debug data 12 | Debugdata12 | register value; /1 | — | R | RESOLVED | semantic_correlated, source_claim | ;  |
| input | 3246 | — | unknown | Debug data 13 | Debugdata13 | register value; /1 | — | R | RESOLVED | semantic_correlated, source_claim | ;  |
| input | 3247 | — | unknown | Debug data 14 | Debugdata14 | register value; /1 | — | R | RESOLVED | semantic_correlated, source_claim | ;  |
| input | 3248 | — | unknown | Debug data 15 | Debugdata15 | register value; /1 | — | R | RESOLVED | semantic_correlated, source_claim | ;  |
| input | 3249 | — | unknown | Debug data 16 | Debugdata16 | register value; /1 | — | R | RESOLVED | semantic_correlated, source_claim | ;  |

### MIX storage

Storage family applicability comes from the graph/catalogue ranges.

| Table | Address | Semantic | Role | Name | Description | Encoding / scale | Unit | Access | Status | Evidence | Notes |
|---|---:|---|---|---|---|---|---|---|---|---|---|
| holding | 0 | — | unknown | Inverter Enabled | Theinvertercanbeswitched onandoff,andtheBDCcanbe switchedonandoffforthe battreadyfunction. | register value; /10 | — | R/W | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| holding | 1 | — | unknown | Safety function enable flags | SPI: system protection interface Bit0~3:forCEI0-21 Bit4~6:forSAA | register value | — | W | SOURCE_ONLY | source_claim | ;  |
| holding | 2 | — | unknown | Persist power-factor commands | Means these settings will be acting or not when next poweron | register value | — | W | RESOLVED | semantic_correlated, source_claim | ;  |
| holding | 3 | — | unknown | Active power limit setpoint | 255:powerisnotbelimited | register value; /1 | % | W | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| holding | 4 | — | unknown | Reactive power limit setpoint | 255:powerisnotbelimited | register value; /1 | % | W | SOURCE_ONLY | source_claim | ;  |
| holding | 5 | — | unknown | Power factor target | Inverter output power factor’s10000times | register value; /10000 | pf | W | SOURCE_ONLY | source_claim | ;  |
| holding | 6 | — | unknown | Rated apparent power | Normal power(high) | register value; /10 | 0.1VA | R | SOURCE_ONLY | source_claim | ;  |
| holding | 7 | — | unknown | Rated apparent power | Normal power(low) | register value; /10 | 0.1VA | R | SOURCE_ONLY | source_claim | ;  |
| holding | 8 | — | unknown | Nominal PV voltage | NormalworkPV voltage | register value; /10 | 0.1V | R | SOURCE_ONLY | source_claim | ;  |
| holding | 9 | — | unknown | Firmware | Firmwareversion (high) | firmware_version; /10 | ASCII | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| holding | 10 | — | unknown | Firmware | Firmwareversion (middle) | register value | ASCII | R | SOURCE_ONLY | source_claim | ;  |
| holding | 11 | — | unknown | Firmware | Firmwareversion(low) | register value | ASCII | R | SOURCE_ONLY | source_claim | ;  |
| holding | 12 | — | unknown | Firmware | ControlFirmware version(high) | register value | ASCII | R | SOURCE_ONLY | source_claim | ;  |
| holding | 13 | — | unknown | Firmware | ControlFirmware version(middle) | register value | ASCII | R | SOURCE_ONLY | source_claim | ;  |
| holding | 14 | — | unknown | Firmware | ControlFirmware version(low) | register value | ASCII | R | SOURCE_ONLY | source_claim | ;  |
| holding | 15 | — | unknown | LCD language selection | 0:Italian; 1:English; 2:German; 3:Spanish; 4:French; 5:Chinese; 6：Polish 7：Portugues 8：Hungary | register value | — | W | SOURCE_ONLY | source_claim | ;  |
| holding | 16 | — | unknown | Country profile configured | CountrySelectedor not | register value | — | W | SOURCE_ONLY | source_claim | ;  |
| holding | 17 | — | unknown | PV start voltage threshold | Inputstartvoltage | register value; /10 | 0.1V | W | SOURCE_ONLY | source_claim | ;  |
| holding | 18 | — | unknown | Start-up delay | Starttime | register value; /1 | 1s | W | SOURCE_ONLY | source_claim | ;  |
| holding | 19 | — | unknown | Restart delay | RestartDelayTime afterfaultback; | register value; /1 | 1s | W | SOURCE_ONLY | source_claim | ;  |
| holding | 20 | — | unknown | Active power ramp rate (startup) | Powerstartslope | register value; /10 | 0.1% | W | SOURCE_ONLY | source_claim | ;  |
| holding | 21 | — | unknown | Active power ramp rate (restart) | Powerrestartslope | register value; /10 | 0.1% | W | SOURCE_ONLY | source_claim | ;  |
| holding | 22 | — | unknown | Modbus RTU baud rate | Select communicationbaudrat e 0:9600bps 1:38400bps | register value | — | W | SOURCE_ONLY | source_claim | ;  |
| holding | 23 | — | unknown | Serial Number | The Home Assistant integration exposes this as the device serial number and reuses it as the unique identifier. | serial_number; /10 | ASCII | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| holding | 24 | — | unknown | Serial Number | The Home Assistant integration exposes this as the device serial number and reuses it as the unique identifier. | register value | ASCII | R | SOURCE_ONLY | source_claim | ;  |
| holding | 25 | — | unknown | Serial Number | The Home Assistant integration exposes this as the device serial number and reuses it as the unique identifier. | register value | ASCII | R | SOURCE_ONLY | source_claim | ;  |
| holding | 26 | — | unknown | Serial Number | The Home Assistant integration exposes this as the device serial number and reuses it as the unique identifier. | register value | ASCII | R | SOURCE_ONLY | source_claim | ;  |
| holding | 27 | — | unknown | Serial Number | The Home Assistant integration exposes this as the device serial number and reuses it as the unique identifier. | register value | ASCII | R | SOURCE_ONLY | source_claim | ;  |
| holding | 28 | — | unknown | Inverter Model | Home Assistant renders this value as the string A# B# D# T# P# U# M# S# via the integration's model() helper. Vendor spec lists value pattern `&*5`; digits appear to be stored without the leading letter codes, so treat as encoded tokens until verified on hardware. | register value; /10 | — | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| holding | 29 | — | unknown | Inverter Model | Home Assistant renders this value as the string A# B# D# T# P# U# M# S# via the integration's model() helper. Vendor spec lists value pattern `&*5`; digits appear to be stored without the leading letter codes, so treat as encoded tokens until verified on hardware. | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| holding | 30 | — | unknown | Modbus slave address | Communicate address | register value | — | W | SOURCE_ONLY | source_claim | ;  |
| holding | 31 | — | unknown | Firmware update trigger | Updatefirmware | register value | — | W | SOURCE_ONLY | source_claim | ;  |
| holding | 32 | — | unknown | Reset user configuration | Use with caution; the inverter immediately reboots and loses provisioning data. | register value | — | W | SOURCE_ONLY | source_claim | ;  |
| holding | 33 | — | unknown | Factory reset | Equivalent to the front-panel factory reset. Requires re-commissioning afterwards. | register value | — | W | SOURCE_ONLY | source_claim | ;  |
| holding | 34 | — | unknown | Manufacturer information string | The original table lists these words as Manufacturer Info 8-1 (high/middle/low); combine them to read the full string. | register value | ASCII | R | SOURCE_ONLY | source_claim | ;  |
| holding | 35 | — | unknown | Manufacturer information string | The original table lists these words as Manufacturer Info 8-1 (high/middle/low); combine them to read the full string. | register value | ASCII | R | SOURCE_ONLY | source_claim | ;  |
| holding | 36 | — | unknown | Manufacturer information string | The original table lists these words as Manufacturer Info 8-1 (high/middle/low); combine them to read the full string. | register value | ASCII | R | SOURCE_ONLY | source_claim | ;  |
| holding | 37 | — | unknown | Manufacturer information string | The original table lists these words as Manufacturer Info 8-1 (high/middle/low); combine them to read the full string. | register value | ASCII | R | SOURCE_ONLY | source_claim | ;  |
| holding | 38 | — | unknown | Manufacturer information string | The original table lists these words as Manufacturer Info 8-1 (high/middle/low); combine them to read the full string. | register value | ASCII | R | SOURCE_ONLY | source_claim | ;  |
| holding | 39 | — | unknown | Manufacturer information string | The original table lists these words as Manufacturer Info 8-1 (high/middle/low); combine them to read the full string. | register value | ASCII | R | SOURCE_ONLY | source_claim | ;  |
| holding | 40 | — | unknown | Manufacturer information string | The original table lists these words as Manufacturer Info 8-1 (high/middle/low); combine them to read the full string. | register value | ASCII | R | SOURCE_ONLY | source_claim | ;  |
| holding | 41 | — | unknown | Manufacturer information string | The original table lists these words as Manufacturer Info 8-1 (high/middle/low); combine them to read the full string. | register value | ASCII | R | SOURCE_ONLY | source_claim | ;  |
| holding | 42 | — | unknown | G100 failsafe enable | EnglishG100failsafeset | register value | — | W | SOURCE_ONLY | source_claim | ;  |
| holding | 43 | — | unknown | Device Type Code | Vendor spec provides value pattern `&*6`; handle as encoded type/family digits with implied prefixes pending confirmation. | register value; /10 | — | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| holding | 44 | — | unknown | Number Of Trackers And Phases | Inputtrackernumand outputphasenum | register value; /10 | — | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| holding | 45 | — | unknown | System clock year | Localtime | register value | — | W | SOURCE_ONLY | source_claim | ;  |
| holding | 46 | — | unknown | System clock month | Systemtime-Month | register value | — | W | SOURCE_ONLY | source_claim | ;  |
| holding | 47 | — | unknown | System clock day | Systemtime-Day | register value | — | W | SOURCE_ONLY | source_claim | ;  |
| holding | 48 | — | unknown | System clock hour | Systemtime-Hour | register value | — | W | SOURCE_ONLY | source_claim | ;  |
| holding | 49 | — | unknown | System clock minute | Systemtime-Min | register value | — | W | SOURCE_ONLY | source_claim | ;  |
| holding | 50 | — | unknown | System clock second | Systemtime-Second | register value | — | W | SOURCE_ONLY | source_claim | ;  |
| holding | 51 | — | unknown | System clock weekday | SystemWeekly | register value | — | W | SOURCE_ONLY | source_claim | ;  |
| holding | 52 | — | unknown | Stage 1 undervoltage limit | Gridvoltagelowlimit protect | register value | 0.1V | W | SOURCE_ONLY | source_claim | ;  |
| holding | 53 | — | unknown | Stage 1 overvoltage limit | Gridvoltagehighlimit protect | register value | 0.1V | W | SOURCE_ONLY | source_claim | ;  |
| holding | 54 | — | unknown | Stage 1 underfrequency limit | Gridfrequencylow limitprotect | register value | 0.01 Hz | W | SOURCE_ONLY | source_claim | ;  |
| holding | 55 | — | unknown | Stage 1 overfrequency limit | Gridhigh frequencylimitprotect | register value | 0.01 Hz | W | SOURCE_ONLY | source_claim | ;  |
| holding | 56 | — | unknown | Stage 2 undervoltage limit | Gridvoltagelowlimit protect2 | register value | 0.1V | W | SOURCE_ONLY | source_claim | ;  |
| holding | 57 | — | unknown | Stage 2 overvoltage limit | Gridvoltagehighlimit protect2 | register value | 0.1V | W | SOURCE_ONLY | source_claim | ;  |
| holding | 58 | — | unknown | Stage 2 underfrequency limit | Gridfrequencylow limitprotect2 | register value | 0.01 Hz | W | SOURCE_ONLY | source_claim | ;  |
| holding | 59 | — | unknown | Stage 2 overfrequency limit | Gridhighfrequency limitprotect2 | register value | 0.01 Hz | W | SOURCE_ONLY | source_claim | ;  |
| holding | 60 | — | unknown | Stage 3 undervoltage limit | Grid voltage low limit protect3 | register value | 0.1V | W | SOURCE_ONLY | source_claim | ;  |
| holding | 61 | — | unknown | Stage 3 overvoltage limit | Grid voltage high limit protect3 | register value | 0.1V | W | SOURCE_ONLY | source_claim | ;  |
| holding | 62 | grid_frequency | alternate | Stage 3 underfrequency limit | Grid frequency low limitprotect3 | register value | 0.01Hz | W | SOURCE_ONLY | source_claim | ; alternates: register:storage_mix:holding:63, register:storage_mix:holding:72, register:storage_mix:holding:73, register:storage_mix:holding:74, register:storage_mix:holding:75, register:storage_mix:holding:78, register:storage_mix:holding:79, register:storage_mix:input:37 |
| holding | 63 | grid_frequency | alternate | Stage 3 overfrequency limit | Grid frequency high limitprotect3 | register value | 0.01Hz | W | SOURCE_ONLY | source_claim | ; alternates: register:storage_mix:holding:62, register:storage_mix:holding:72, register:storage_mix:holding:73, register:storage_mix:holding:74, register:storage_mix:holding:75, register:storage_mix:holding:78, register:storage_mix:holding:79, register:storage_mix:input:37 |
| holding | 64 | — | unknown | Reconnect undervoltage limit | Gridlowvoltagelimit connecttoGrid | register value | 0.1V | W | SOURCE_ONLY | source_claim | ;  |
| holding | 65 | — | unknown | Reconnect overvoltage limit | Gridhighvoltagelimit connecttoGrid | register value | 0.1V | W | SOURCE_ONLY | source_claim | ;  |
| holding | 66 | — | unknown | Reconnect underfrequency limit | Gridlowfrequency | register value | 0.01 | W | SOURCE_ONLY | source_claim | ;  |
| holding | 67 | — | unknown | Reconnect overfrequency limit | Gridhighfrequency limitconnecttoGrid | register value | 0.01 Hz | W | SOURCE_ONLY | source_claim | ;  |
| holding | 68 | — | unknown | Stage 1 undervoltage trip delay | Grid voltage low limit protecttime 1 | register value | Cycle | W | SOURCE_ONLY | source_claim | ;  |
| holding | 69 | — | unknown | Stage 1 overvoltage trip delay | Grid voltage high limit protecttime 1 | register value | Cycle | W | SOURCE_ONLY | source_claim | ;  |
| holding | 70 | — | unknown | Stage 2 undervoltage trip delay | Grid voltage low limit protecttime 2 | register value | Cycle | W | SOURCE_ONLY | source_claim | ;  |
| holding | 71 | — | unknown | Stage 2 overvoltage trip delay | Grid voltage high limit protecttime 2 | register value | Cycle | W | SOURCE_ONLY | source_claim | ;  |
| holding | 72 | grid_frequency | alternate | Stage 1 underfrequency trip delay | Grid frequency low limitprotecttime 1 | register value | Cycle | W | SOURCE_ONLY | source_claim | ; alternates: register:storage_mix:holding:62, register:storage_mix:holding:63, register:storage_mix:holding:73, register:storage_mix:holding:74, register:storage_mix:holding:75, register:storage_mix:holding:78, register:storage_mix:holding:79, register:storage_mix:input:37 |
| holding | 73 | grid_frequency | alternate | Modbus Version | Grid frequency high limitprotecttime 1 | register value | Cycle | W | SOURCE_ONLY | source_claim | ; alternates: register:storage_mix:holding:62, register:storage_mix:holding:63, register:storage_mix:holding:72, register:storage_mix:holding:74, register:storage_mix:holding:75, register:storage_mix:holding:78, register:storage_mix:holding:79, register:storage_mix:input:37 |
| holding | 74 | grid_frequency | alternate | Stage 2 underfrequency trip delay | Grid frequency low limitprotecttime 2 | register value | Cycle | W | SOURCE_ONLY | source_claim | ; alternates: register:storage_mix:holding:62, register:storage_mix:holding:63, register:storage_mix:holding:72, register:storage_mix:holding:73, register:storage_mix:holding:75, register:storage_mix:holding:78, register:storage_mix:holding:79, register:storage_mix:input:37 |
| holding | 75 | grid_frequency | alternate | Stage 2 overfrequency trip delay | Grid frequency high limitprotecttime 2 | register value | Cycle | W | SOURCE_ONLY | source_claim | ; alternates: register:storage_mix:holding:62, register:storage_mix:holding:63, register:storage_mix:holding:72, register:storage_mix:holding:73, register:storage_mix:holding:74, register:storage_mix:holding:78, register:storage_mix:holding:79, register:storage_mix:input:37 |
| holding | 76 | — | unknown | Stage 3 undervoltage trip delay | Grid voltage low limit protecttime 3 | register value | Cycle | W | SOURCE_ONLY | source_claim | ;  |
| holding | 77 | — | unknown | Stage 3 overvoltage trip delay | Grid voltage high limit protecttime 3 | register value | Cycle | W | SOURCE_ONLY | source_claim | ;  |
| holding | 78 | grid_frequency | alternate | Stage 3 underfrequency trip delay | Grid frequency low limitprotecttime 3 | register value | Cycle | W | SOURCE_ONLY | source_claim | ; alternates: register:storage_mix:holding:62, register:storage_mix:holding:63, register:storage_mix:holding:72, register:storage_mix:holding:73, register:storage_mix:holding:74, register:storage_mix:holding:75, register:storage_mix:holding:79, register:storage_mix:input:37 |
| holding | 79 | grid_frequency | alternate | Stage 3 overfrequency trip delay | Grid frequency high limitprotecttime 3 | register value | Cycle | W | SOURCE_ONLY | source_claim | ; alternates: register:storage_mix:holding:62, register:storage_mix:holding:63, register:storage_mix:holding:72, register:storage_mix:holding:73, register:storage_mix:holding:74, register:storage_mix:holding:75, register:storage_mix:holding:78, register:storage_mix:input:37 |
| holding | 80 | — | unknown | Ten-minute overvoltage limit | Voltprotectionfor10 min | register value | 0.1V | W | SOURCE_ONLY | source_claim | ;  |
| holding | 81 | — | unknown | PV input high-voltage fault | PVVoltageHigh Fault | register value | 0.1V | W | SOURCE_ONLY | source_claim | ;  |
| holding | 82 | — | unknown | Controller firmware build string | Positions: 0-1 model letters, 2-3 model variant, 4-5 DSP1 build, 6-7 DSP2/M0 build, 8-9 CPLD/AFCI build, 10-11 M3 build. | register value | ASCII | R | SOURCE_ONLY | source_claim | ;  |
| holding | 83 | — | unknown | Controller firmware build string | Positions: 0-1 model letters, 2-3 model variant, 4-5 DSP1 build, 6-7 DSP2/M0 build, 8-9 CPLD/AFCI build, 10-11 M3 build. | register value | ASCII | R | SOURCE_ONLY | source_claim | ;  |
| holding | 84 | — | unknown | Controller firmware build string | Positions: 0-1 model letters, 2-3 model variant, 4-5 DSP1 build, 6-7 DSP2/M0 build, 8-9 CPLD/AFCI build, 10-11 M3 build. | register value | ASCII | R | SOURCE_ONLY | source_claim | ;  |
| holding | 85 | — | unknown | Controller firmware build string | Positions: 0-1 model letters, 2-3 model variant, 4-5 DSP1 build, 6-7 DSP2/M0 build, 8-9 CPLD/AFCI build, 10-11 M3 build. | register value | ASCII | R | SOURCE_ONLY | source_claim | ;  |
| holding | 86 | — | unknown | Controller firmware build string | Positions: 0-1 model letters, 2-3 model variant, 4-5 DSP1 build, 6-7 DSP2/M0 build, 8-9 CPLD/AFCI build, 10-11 M3 build. | register value | ASCII | R | SOURCE_ONLY | source_claim | ;  |
| holding | 87 | — | unknown | Controller firmware build string | Positions: 0-1 model letters, 2-3 model variant, 4-5 DSP1 build, 6-7 DSP2/M0 build, 8-9 CPLD/AFCI build, 10-11 M3 build. | register value | ASCII | R | SOURCE_ONLY | source_claim | ;  |
| holding | 88 | — | unknown | Modbus Version | ModbusVersion | register value; /100 | Int(16 bits) | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| holding | 89 | — | unknown | Power-factor control mode | 0=Unity PF, 1=Fixed PF setpoint, 2=Default PF line, 3=User-defined PF line, 4=Under-excited reactive power, 5=Over-excited reactive power, 6=Q(V) curve, 7=Direct control, 8=Static capacitive QV, 9=Static inductive QV. | register value | — | W | SOURCE_ONLY | source_claim | ;  |
| holding | 90 | — | unknown | GPRS modem IP/status flags | Bit 0-3: 0=idle, 1=IP read requested, 2=set IP succeeded; Bit 4-7: 0=unknown, 1=modem OK, 2=no SIM, 3=no network, 4=TCP connect fail, 5=TCP connected, etc. | register value | — | W | UNKNOWN_RESERVED | source_claim | ;  |
| holding | 91 | — | unknown | Frequency derating start | Frequencyderating startpoint | register value | 0.01H Z | W | SOURCE_ONLY | source_claim | ;  |
| holding | 92 | — | unknown | Frequency derating slope | Frequency–loadlimit rate | register value | 10tim es | W | SOURCE_ONLY | source_claim | ;  |
| holding | 93 | — | unknown | CEI 0-21 Q(V) point V1S | CEI021V1SQ(v) | register value | 0.1V | W | SOURCE_ONLY | source_claim | ;  |
| holding | 94 | — | unknown | CEI 0-21 Q(V) point V2S | CEI021V2SQ(v) | register value | 0.1V | W | SOURCE_ONLY | source_claim | ;  |
| holding | 95 | — | unknown | CEI 0-21 Q(V) point V1L | CEI021V1LQ(v) | register value | 0.1V | W | SOURCE_ONLY | source_claim | ;  |
| holding | 96 | — | unknown | CEI 0-21 Q(V) point V2L | CEI021V2LQ(v) | register value | 0.1V | W | SOURCE_ONLY | source_claim | ;  |
| holding | 97 | — | unknown | Q(V) lock-in active power | Q(v)lockinactive powerofCEI021 | register value | Percen t | W | SOURCE_ONLY | source_claim | ;  |
| holding | 98 | — | unknown | Q(V) lock-out active power | Q(v)lockOutactive powerofCEI021 | register value | Percen t | W | SOURCE_ONLY | source_claim | ;  |
| holding | 99 | — | unknown | Power-factor curve lock-in voltage | Lockingirdvoltof CEI021PFline | register value | 0.1V | W | SOURCE_ONLY | source_claim | ;  |
| holding | 100 | — | unknown | Power-factor curve lock-out voltage | Lockoutgirdvoltof CEI021PFline | register value | 0.1V | W | SOURCE_ONLY | source_claim | ;  |
| holding | 101 | — | unknown | Power-factor adjust value 1 | PFadjustvalue1 | register value | — | W | SOURCE_ONLY | source_claim | ;  |
| holding | 102 | — | unknown | Power-factor adjust value 2 | PFadjustvalue2 | register value | — | W | SOURCE_ONLY | source_claim | ;  |
| holding | 103 | — | unknown | Power-factor adjust value 3 | PFadjustvalue3 | register value | — | W | SOURCE_ONLY | source_claim | ;  |
| holding | 104 | — | unknown | Power-factor adjust value 4 | PFadjustvalue4 | register value | — | W | SOURCE_ONLY | source_claim | ;  |
| holding | 105 | — | unknown | Power-factor adjust value 5 | PFadjustvalue5 | register value | — | W | SOURCE_ONLY | source_claim | ;  |
| holding | 106 | — | unknown | Power-factor adjust value 6 | PFadjustvalue6 | register value | — | W | SOURCE_ONLY | source_claim | ;  |
| holding | 107 | — | unknown | Q(V) response delay | QV Reactive Power delaytime | register value | 1S | W | SOURCE_ONLY | source_claim | ;  |
| holding | 108 | — | unknown | Over-frequency derating delay | Overfrequency derati ngdelaytime | register value | 50ms | W | SOURCE_ONLY | source_claim | ;  |
| holding | 109 | — | unknown | Maximum reactive power magnitude | QmaxforQ(V)curve | register value | 0.1% | W | SOURCE_ONLY | source_claim | ;  |
| holding | 110 | — | unknown | PF curve point 1 load | 255meansnothispoint | register value | percen t | W | SOURCE_ONLY | source_claim | ;  |
| holding | 111 | — | unknown | PF curve point 1 target | PFlimitlinepoint1 powerfactor | register value | — | W | SOURCE_ONLY | source_claim | ;  |
| holding | 112 | — | unknown | PF curve point 2 load | 255meansnothispoint | register value | percen t | W | SOURCE_ONLY | source_claim | ;  |
| holding | 113 | — | unknown | PF curve point 2 target | PFlimitlinepoint 2powerfactor | register value | — | W | SOURCE_ONLY | source_claim | ;  |
| holding | 114 | — | unknown | PF curve point 3 load | 255meansnothispoint | register value | percen t | W | SOURCE_ONLY | source_claim | ;  |
| holding | 115 | — | unknown | PF curve point 3 target | PFlimitlinepoint3 powerfactor | register value | — | W | SOURCE_ONLY | source_claim | ;  |
| holding | 116 | — | unknown | PF curve point 4 load | 255meansnothispoint | register value | percen t | W | SOURCE_ONLY | source_claim | ;  |
| holding | 117 | — | unknown | PF curve point 4 target | PFlimitlinepoint4 powerfactor | register value | — | W | SOURCE_ONLY | source_claim | ;  |
| holding | 118 | — | unknown | Module code segments | SxxBxx | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| holding | 119 | — | unknown | Module code segments | DxxTxx | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| holding | 120 | — | unknown | Module code segments | PxxUxx | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| holding | 121 | — | unknown | Module code segments | Mxxxx Power | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| holding | 122 | — | unknown | Export limit enable mode | ExportLimitenable, 0:DisableexportLimit; 1:Enable485exportLimit; 2:Enable232exportLimit; 3:EnableCTexportLimit; | register value | — | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 123 | — | unknown | Export limit power setpoint | ExportLimitPowerRate | register value | 0.1% | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 124 | — | unknown | Tracker coupling mode | 0:Independent 1:DCSource 2:Parallel | register value | — | W | SOURCE_ONLY | source_claim | ;  |
| holding | 1000 | — | unknown | Float charge current limit i | Float charge current limit i | register value | — | W | SOURCE_ONLY | source_claim | ;  |
| holding | 1001 | — | unknown | PF CMD memory state | PF CMD memory state | register value | 0or1, | W | SOURCE_ONLY | source_claim | ;  |
| holding | 1002 | — | unknown | VbatStartF orDischarg e | VbatStartF orDischarg e | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| holding | 1003 | — | unknown | VbatlowWa rnClr l | VbatlowWa rnClr l | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| holding | 1004 | — | unknown | Vbatstopfo rdischarge | Vbatstopfo rdischarge | register value | — | W | SOURCE_ONLY | source_claim | ;  |
| holding | 1005 | — | unknown | Vbat stop forcharge | Shouldstopcharge whenhigherthanthis voltage | register value | 0.01V | W | SOURCE_ONLY | source_claim | ;  |
| holding | 1006 | — | unknown | Vbat start for discharge | Should not discharge when lower than this voltage | register value | 0.01V | W | SOURCE_ONLY | source_claim | ;  |
| holding | 1007 | — | unknown | Vbat constant charge | CVvoltage（acid） | register value | 0.01V | W | SOURCE_ONLY | source_claim | ;  |
| holding | 1008 | — | unknown | EESysInfo.S ysSetEn | SystemEnable | register value | — | W | SOURCE_ONLY | source_claim | ;  |
| holding | 1009 | — | unknown | Battemp lower limit d | Batterytemperature lowerlimitfordischarge | register value | 0.1℃ | W | SOURCE_ONLY | source_claim | ;  |
| holding | 1010 | — | unknown | Bat temp upper limit d | Batterytemperature upperlimitfordischarge | register value | 0.1℃ | W | SOURCE_ONLY | source_claim | ;  |
| holding | 1011 | — | unknown | Bat temp lower limit c | Lowertemperaturelimit | register value | 0.1℃ | W | SOURCE_ONLY | source_claim | ;  |
| holding | 1012 | — | unknown | Bat temp upper limit c | Uppertemperaturelimit | register value | 0.1℃ | W | SOURCE_ONLY | source_claim | ;  |
| holding | 1013 | — | unknown | uwUnderFr eDischarge DelyTime | UnderFreDelayTime | register value | 50ms | R | SOURCE_ONLY | source_claim | ;  |
| holding | 1014 | — | unknown | BatMdlSeri alNum | SPH4-11Kused | register value | — | W | SOURCE_ONLY | source_claim | ;  |
| holding | 1015 | — | unknown | BatMdlPara llNum | SPH4-11Kused | register value | — | W | SOURCE_ONLY | source_claim | ;  |
| holding | 1016 | — | unknown | DRMS_EN | 0：disable 1：enable | register value | / | R | SOURCE_ONLY | source_claim | ;  |
| holding | 1017 | — | unknown | Bat First Start Time 4 | Higheight:hours Loweight:minutes | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| holding | 1018 | — | unknown | Bat First Stop Time 4 | Higheight:hours Loweight:minutes | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| holding | 1019 | — | unknown | BatFirst on/off Switch4 | Batterypriorityenable1 | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| holding | 1020 | — | unknown | Bat First Start Time 5 | Higheight:hours Loweight:minutes | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| holding | 1021 | — | unknown | BatFirst StopTime 5 | Higheight:hours Loweight:minutes | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| holding | 1022 | — | unknown | BatFirst on/off Switch5 | Batterypriorityenable1 | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| holding | 1023 | — | unknown | BatFirst StartTime 6 | Higheight:hours Loweight:minutes | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| holding | 1024 | — | unknown | BatFirst StopTime 6 | Higheight:hours Loweight:minutes | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| holding | 1025 | — | unknown | BatFirst on/off Switch6 | Batterypriorityenable1 | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| holding | 1026 | — | unknown | GridFirst StartTime | Higheight:hours Loweight:minutes | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| holding | 1027 | — | unknown | GridFirst StopTime 4 | Higheight:hours Loweight:minutes | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| holding | 1028 | — | unknown | Grid First Stop Switch4 | Gridpriorityenable | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| holding | 1029 | — | unknown | GridFirst StartTime 5 | Higheight:hours Loweight:minutes | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| holding | 1030 | — | unknown | GridFirst StopTime 5 | Higheight:hours Loweight:minutes | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| holding | 1031 | — | unknown | Grid First Stop Switch5 | Gridpriorityenable | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| holding | 1032 | — | unknown | GridFirst StartTime 6 | Higheight:hours Loweight:minutes | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| holding | 1033 | — | unknown | GridFirst StopTime 6 | Higheight:hours Loweight:minutes | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| holding | 1034 | — | unknown | Grid First Stop Switch6 | Gridpriorityenable | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| holding | 1035 | — | unknown | BatFirst StartTime 4 | Higheight:hours Loweight:minutes | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| holding | 1036 | — | unknown | / | Reserve | register value | / | R | SOURCE_ONLY | source_claim | ;  |
| holding | 1037 | — | unknown | bCTMode | UsetheCTModeto ChooseRFCT\Cable CT\METER | register value | — | W | SOURCE_ONLY | source_claim | ;  |
| holding | 1038 | — | unknown | CTAdjust | CTAdjustenable | register value | — | W | SOURCE_ONLY | source_claim | ;  |
| holding | 1039 | — | unknown | / | Reserve | register value | / | R | SOURCE_ONLY | source_claim | ;  |
| holding | 1040 | — | unknown | / | / | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| holding | 1041 | — | unknown | / | / | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| holding | 1042 | — | unknown | / | / | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| holding | 1043 | — | unknown | / | / | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| holding | 1044 | — | unknown | Priority | ForceChrEn/ForceDischr En Load first/bat first /grid first | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| holding | 1045 | — | unknown | / | / | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| holding | 1046 | — | unknown | / | / | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| holding | 1047 | — | unknown | AgingTestSt ep Cmd | Commandforagingtest | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| holding | 1048 | — | unknown | BatteryTyp e | Batterytypechooseof buck-boostinput | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| holding | 1049 | — | unknown | / | / | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| holding | 1050 | — | unknown | / | / | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| holding | 1051 | — | unknown | / | / | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| holding | 1052 | — | unknown | / | / | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| holding | 1053 | — | unknown | / | / | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| holding | 1054 | — | unknown | / | / | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| holding | 1055 | — | unknown | Register 1055 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| holding | 1056 | — | unknown | Register 1056 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| holding | 1057 | — | unknown | Register 1057 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| holding | 1058 | — | unknown | Register 1058 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| holding | 1059 | — | unknown | Register 1059 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| holding | 1060 | — | unknown | BuckUpsFunE n | 0:disable 1:enable | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| holding | 1061 | — | unknown | BuckUPSVoltS et | UPSoutputvoltage | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| holding | 1062 | — | unknown | UPSFreqSet | UPSoutputfrequency | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| holding | 1063 | — | unknown | Register 1063 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| holding | 1064 | — | unknown | Register 1064 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| holding | 1065 | — | unknown | Register 1065 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| holding | 1066 | — | unknown | Register 1066 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| holding | 1067 | — | unknown | Register 1067 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| holding | 1068 | — | unknown | Register 1068 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| holding | 1069 | — | unknown | Register 1069 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| holding | 1070 | grid_first_discharge_rate | supported | Grid-first discharge limit | Discharge Power Rate whenGridFirst | register value | 1% | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 1071 | grid_first_stop_soc | supported | Grid-first stop SOC | Stop Discharge soc when GridFirst | register value | 1% | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 1072 | — | unknown | / | / | register value | / | R | SOURCE_ONLY | source_claim | ;  |
| holding | 1073 | — | unknown | / | / | register value | / | R | SOURCE_ONLY | source_claim | ;  |
| holding | 1074 | — | unknown | / | / | register value | / | R | SOURCE_ONLY | source_claim | ;  |
| holding | 1075 | — | unknown | / | / | register value | / | R | SOURCE_ONLY | source_claim | ;  |
| holding | 1076 | — | unknown | / | / | register value | / | R | SOURCE_ONLY | source_claim | ;  |
| holding | 1077 | — | unknown | / | / | register value | / | R | SOURCE_ONLY | source_claim | ;  |
| holding | 1078 | — | unknown | / | / | register value | / | R | SOURCE_ONLY | source_claim | ;  |
| holding | 1079 | — | unknown | / | / | register value | / | R | SOURCE_ONLY | source_claim | ;  |
| holding | 1080 | — | unknown | Grid-first slot 1 start | High byte = hour (0-23); low byte = minute (0-59). | register value | hh:mm | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 1081 | — | unknown | Grid-first slot 1 stop | High byte = hour (0-23); low byte = minute (0-59). | register value | hh:mm | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 1082 | — | unknown | Grid-first slot 1 enable | Enable:1 Disable:0 | register value | — | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 1083 | — | unknown | Grid-first slot 2 start | High byte = hour (0-23); low byte = minute (0-59). | register value | hh:mm | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 1084 | — | unknown | Grid-first slot 2 stop | High byte = hour (0-23); low byte = minute (0-59). | register value | hh:mm | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 1085 | — | unknown | Grid-first slot 2 enable | When set from the LCD, this slot can be tied to the Force Discharge command. | register value | — | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 1086 | — | unknown | Grid-first slot 3 start | High byte = hour (0-23); low byte = minute (0-59). | register value | hh:mm | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 1087 | — | unknown | Grid-first slot 3 stop | High byte = hour (0-23); low byte = minute (0-59). | register value | hh:mm | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 1088 | — | unknown | Grid-first slot 3 enable | Enable:1 Disable:0 | register value | — | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 1089 | — | unknown | / | / | register value | / | R | SOURCE_ONLY | source_claim | ;  |
| holding | 1090 | battery_first_charge_rate | supported | Battery-first charge limit | Charge Power Rate when BatFirst | register value | 1% | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 1091 | battery_first_stop_soc | supported | Battery-first stop SOC | Stop Charge soc when Bat First | register value | 1% | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 1092 | — | unknown | Battery-first AC charge enable | WhenBatFirst Enable:1 Disable:0 | register value | — | R/W | RESOLVED | semantic_correlated, source_claim | ;  |
| holding | 1093 | — | unknown | Register 1093 | — | register value | — | R | UNKNOWN_RESERVED | source_claim | ;  |
| holding | 1094 | — | unknown | Register 1094 | — | register value | — | R | UNKNOWN_RESERVED | source_claim | ;  |
| holding | 1095 | — | unknown | Register 1095 | — | register value | — | R | UNKNOWN_RESERVED | source_claim | ;  |
| holding | 1096 | — | unknown | Register 1096 | — | register value | — | R | UNKNOWN_RESERVED | source_claim | ;  |
| holding | 1097 | — | unknown | Register 1097 | — | register value | — | R | UNKNOWN_RESERVED | source_claim | ;  |
| holding | 1098 | — | unknown | Register 1098 | — | register value | — | R | UNKNOWN_RESERVED | source_claim | ;  |
| holding | 1099 | — | unknown | Register 1099 | — | register value | — | R | UNKNOWN_RESERVED | source_claim | ;  |
| holding | 1100 | — | unknown | Battery-first slot 1 start | High byte = hour (0-23); low byte = minute (0-59). | register value | hh:mm | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 1101 | — | unknown | Battery-first slot 1 stop | High byte = hour (0-23); low byte = minute (0-59). | register value | hh:mm | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 1102 | — | unknown | Battery-first slot 1 enable | Enable:1 Disable:0 | register value | — | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 1103 | — | unknown | Battery-first slot 2 start | High byte = hour (0-23); low byte = minute (0-59). | register value | hh:mm | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 1104 | — | unknown | Battery-first slot 2 stop | High byte = hour (0-23); low byte = minute (0-59). | register value | hh:mm | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 1105 | — | unknown | Battery-first slot 2 enable | Enable:1 Disable:0 | register value | — | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 1106 | — | unknown | Battery-first slot 3 start | High byte = hour (0-23); low byte = minute (0-59). | register value | hh:mm | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 1107 | — | unknown | Battery-first slot 3 stop | High byte = hour (0-23); low byte = minute (0-59). | register value | hh:mm | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 1108 | — | unknown | Battery-first slot 3 enable | Enable:1 Disable:0 | register value | — | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 1109 | — | unknown | / | reserve | register value | / | R | SOURCE_ONLY | source_claim | ;  |
| holding | 1110 | — | unknown | Load-first slot 1 start | SPA/reserve | register value | hh:mm | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 1111 | — | unknown | Load-first slot 1 stop | SPA/reserve | register value | hh:mm | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 1112 | — | unknown | Load-first slot 1 enable | SPA/reserve | register value | — | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 1113 | — | unknown | Load-first slot 2 start | SPA/reserve | register value | hh:mm | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 1114 | — | unknown | Load-first slot 2 stop | SPA/reserve | register value | hh:mm | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 1115 | — | unknown | Load-first slot 2 enable | SPA/reserve | register value | — | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 1116 | — | unknown | Load-first slot 3 start | SPA/reserve | register value | hh:mm | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 1117 | — | unknown | Load-first slot 3 stop | SPA/reserve | register value | hh:mm | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 1118 | — | unknown | Load-first slot 3 enable | SPA/reserve | register value | — | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 1119 | — | unknown | Energy calculation formula | 0：Theoldformula 1 ： The new formula | register value | / | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 1120 | — | unknown | Backup enable | MIXUS | register value | — | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 1121 | — | unknown | SGIP enable | MIXUS | register value | — | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 1122 | — | unknown | Register 1122 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| holding | 1123 | — | unknown | Register 1123 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| holding | 1124 | — | unknown | Register 1124 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| holding | 3000 | — | unknown | Export-limit fallback cap | Thepowerrate whenexportLimit failed | register value; /10 | 0.1% | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 3001 | — | unknown | Serial Number | Thenewmodel usesthefollowing registerstorecord theserialnumber; The representationis thesameasthe original:one registerholdstwo charactersandthe newserialnumber is30characters. | serial_number; /10 | ASCII | R/W | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| holding | 3002 | — | unknown | Serial Number | Serialnumber3-4 | register value | ASCII | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 3003 | — | unknown | Serial Number | Serialnumber5-6 | register value | ASCII | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 3004 | — | unknown | Serial Number | Serialnumber7-8 | register value | ASCII | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 3005 | — | unknown | Serial Number | Serialnumber9-10 | register value | ASCII | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 3006 | — | unknown | Serial Number | Serialnumber11-12 | register value | ASCII | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 3007 | — | unknown | Serial Number | Serialnumber13-14 | register value | ASCII | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 3008 | — | unknown | Serial Number | Serialnumber15-16 | register value | ASCII | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 3009 | — | unknown | Serial Number | Serialnumber17-18 | register value | ASCII | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 3010 | — | unknown | Serial Number | Serialnumber19-20 | register value | ASCII | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 3011 | — | unknown | Serial Number | Serialnumber21-22 | register value | ASCII | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 3012 | — | unknown | Serial Number | Serialnumber23-24 | register value | ASCII | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 3013 | — | unknown | Serial Number | Serialnumber25-26 | register value | ASCII | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 3014 | — | unknown | Serial Number | Serialnumber27-28 | register value | ASCII | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 3015 | — | unknown | Serial Number | Serialnumber29-30 | register value | ASCII | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 3016 | — | unknown | Dry-contact enable | DryContact functionenable | register value | — | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 3018 | — | unknown | Hybrid work mode | MIN2.5~6KTL-XH/ XADoubleCT special | register value | — | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 3021 | — | unknown | External off-grid enable | 0x00: Disable; （default） 0x01:Enable; | register value | — | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 3023 | — | unknown | Grid topology selection | MIN2.5~6KTL-XH/ XADoubleCT special | register value | — | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 3024 | — | unknown | Float-charge current limit | CCcurrent | register value; /10 | 0.1A | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 3028 | — | unknown | Battery charge stop voltage | Shouldstop chargewhen higherthanthis voltage | register value; /100 | 0.01V | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 3029 | — | unknown | Battery discharge start voltage | Shouldnot dischargewhen lowerthanthis voltage | register value; /100 | 0.01V | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 3030 | — | unknown | Battery constant-charge voltage | CVvoltage（acid） canchargewhen lowerthanthis voltage | register value; /100 | 0.01V | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 3031 | — | unknown | Discharge low temperature limit | 0-200:0-20℃ 1000-1400： -40-0℃ | register value; /10 | 0.1℃ | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 3032 | — | unknown | Discharge high temperature limit | Batterytemperatureupper limitfordischarge | register value; /10 | 0.1℃ | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 3033 | — | unknown | Charge low temperature limit | Battery temperaturelower limit 0-200:0-20℃ 1000-1400： -40-0℃ | register value; /10 | 0.1℃ | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 3034 | — | unknown | Charge high temperature limit | Battery temperature upperlimit | register value; /10 | 0.1℃ | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 3038 | — | unknown | Grid-first period 1 control | Bit0~7:minutes; Bit8~12:hour; Bit13~14, 0:loadpriority; 1:batterypriority; 2:Gridpriority; Bit15, 0:prohibited;1: enabled; | register value | — | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 3039 | — | unknown | Grid-first period 1 end | Bit0~7:minutes; Bit8~12:hour; Bit13~15:reserved | register value | — | R/W | UNKNOWN_RESERVED | source_claim | ;  |
| holding | 3041 | — | unknown | Register 3041 | Bit0~7:minutes; Bit8~12:hour; Bit13~15:reserved | register value; /10 | W | R/W | UNKNOWN_RESERVED | source_claim | ;  |
| holding | 3042 | — | unknown | Time3(xh) | WithTime1 | register value; /10 | W | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 3043 | — | unknown | Register 3043 | WithTime1 | register value; /10 | W | R/W | UNKNOWN_RESERVED | source_claim | ;  |
| holding | 3044 | — | unknown | Time4(xh) | WithTime1 | register value; /10 | W | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 3045 | — | unknown | Register 3045 | WithTime1 | register value; /10 | W | R/W | UNKNOWN_RESERVED | source_claim | ;  |
| holding | 3046 | — | unknown | Reserved | Reserved | register value; /10 | W | R | UNKNOWN_RESERVED | source_claim | ;  |
| holding | 3049 | ac_charge_enabled | supported | AC Charge Enabled | Enable:1 Disable:0 | register value; /10 | — | R/W | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| holding | 3051 | — | unknown | Register 3051 | WithTime1 | register value; /10 | kWh | R/W | UNKNOWN_RESERVED | source_claim | ;  |
| holding | 3052 | — | unknown | Time6(xh) | WithTime1 | register value; /10 | kWh | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 3053 | — | unknown | Register 3053 | WithTime1 | register value; /10 | kWh | R/W | UNKNOWN_RESERVED | source_claim | ;  |
| holding | 3054 | — | unknown | Time7(xh) | WithTime1 | register value; /10 | kWh | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 3055 | — | unknown | Register 3055 | WithTime1 | register value; /10 | kWh | R/W | UNKNOWN_RESERVED | source_claim | ;  |
| holding | 3056 | — | unknown | Time8(xh) | WithTime1 | register value; /10 | kWh | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 3057 | — | unknown | Register 3057 | WithTime1 | register value; /10 | kWh | R/W | UNKNOWN_RESERVED | source_claim | ;  |
| holding | 3058 | — | unknown | Time9(xh) | WithTime1 | register value; /10 | kWh | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 3059 | — | unknown | Register 3059 | WithTime1 | register value; /10 | kWh | R/W | UNKNOWN_RESERVED | source_claim | ;  |
| holding | 3060 | — | unknown | Reserved | Reserved | register value; /10 | kWh | R | UNKNOWN_RESERVED | source_claim | ;  |
| holding | 3061 | — | unknown | Reserved | Reserved | register value; /10 | kWh | R | UNKNOWN_RESERVED | source_claim | ;  |
| holding | 3062 | — | unknown | Reserved | Reserved | register value; /10 | kWh | R | UNKNOWN_RESERVED | source_claim | ;  |
| holding | 3063 | — | unknown | Reserved | Reserved | register value; /10 | kWh | R | UNKNOWN_RESERVED | source_claim | ;  |
| holding | 3064 | — | unknown | Reserved | Reserved | register value; /10 | kWh | R | UNKNOWN_RESERVED | source_claim | ;  |
| holding | 3065 | — | unknown | Reserved | Reserved | register value; /10 | kWh | R | UNKNOWN_RESERVED | source_claim | ;  |
| holding | 3066 | — | unknown | Reserved | Reserved | register value; /10 | kWh | R | UNKNOWN_RESERVED | source_claim | ;  |
| holding | 3067 | — | unknown | Reserved | Reserved | register value; /10 | kWh | R | UNKNOWN_RESERVED | source_claim | ;  |
| holding | 3068 | — | unknown | Reserved | Reserved | register value; /10 | kWh | R | UNKNOWN_RESERVED | source_claim | ;  |
| holding | 3069 | — | unknown | Reserved | Reserved | register value; /10 | kWh | R | UNKNOWN_RESERVED | source_claim | ;  |
| holding | 3070 | — | unknown | BatteryType | Batterytype 0:Lithium 1:Lead-acid 2:other | register value; /10 | kWh | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 3071 | — | unknown | BatMdlSeria/ ParalNum | BatMdlSeria/Paral Num; SPH4-11Kused Theupper8bits indicatethe numberofseries segments； Thelower8bits indicatethe numberofparallel sections; | register value; /10 | kWh | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 3072 | — | unknown | Reserved | Reserved | register value; /10 | kWh | R | UNKNOWN_RESERVED | source_claim | ;  |
| holding | 3073 | — | unknown | Reserved | Reserved | register value; /10 | kWh | R | UNKNOWN_RESERVED | source_claim | ;  |
| holding | 3074 | — | unknown | Reserved | Reserved | register value; /10 | kWh | R | UNKNOWN_RESERVED | source_claim | ;  |
| holding | 3075 | — | unknown | Reserved | Reserved | register value; /10 | kWh | R | UNKNOWN_RESERVED | source_claim | ;  |
| holding | 3076 | — | unknown | Reserved | Reserved | register value; /10 | kWh | R | UNKNOWN_RESERVED | source_claim | ;  |
| holding | 3077 | — | unknown | Reserved | Reserved | register value; /10 | kWh | R | UNKNOWN_RESERVED | source_claim | ;  |
| holding | 3078 | — | unknown | Reserved | Reserved | register value; /10 | kWh | R | UNKNOWN_RESERVED | source_claim | ;  |
| holding | 3079 | — | unknown | UpsFunEn | 0:disable 1:enable | register value | bool | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 3080 | — | unknown | UPSVoltSet | 0:230V 1:208V 2:240V | register value | V | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 3081 | — | unknown | UPSFreqSet | 0:50Hz 1:60Hz | register value | Hz | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 3082 | — | unknown | bLoadFirstSto pSocSet | ratio | register value; /1 | % | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 3083 | — | unknown | Reserved | Reserved | register value; /10 | kWh | R | UNKNOWN_RESERVED | source_claim | ;  |
| holding | 3084 | — | unknown | Reserved | Reserved | register value; /10 | kWh | R | UNKNOWN_RESERVED | source_claim | ;  |
| holding | 3087 | — | unknown | Battery rack serial | Forbattery | register value | ASCII | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 3088 | — | unknown | Battery rack serial | SerialNumber3-4 | register value | ASCII | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 3089 | — | unknown | Battery rack serial | SerialNumber5-6 | register value | ASCII | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 3090 | — | unknown | Battery rack serial | SerialNumber7-8 | register value | ASCII | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 3091 | — | unknown | Battery rack serial | SerialNumber9-10 | register value | ASCII | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 3092 | — | unknown | Battery rack serial | SerialNumber11-12 | register value | ASCII | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 3093 | — | unknown | Battery rack serial | SerialNumber13-14 | register value | ASCII | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 3094 | — | unknown | Battery rack serial | SerialNumber15-16 | register value | ASCII | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 3095 | — | unknown | BDC reset command | 0：Invaliddata 1：Resetsetting parameters 2：Resetcorrection parameter 3：Clearhistorical power | register value | — | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 3096 | — | unknown | BDC monitoring code | ZEBA | register value | ASCII | R | SOURCE_ONLY | source_claim | ;  |
| holding | 3097 | — | unknown | BDC monitoring code | Four-character identifier for the BDC monitoring firmware (e.g. ZEBA). | register value | ASCII | R | SOURCE_ONLY | source_claim | ;  |
| holding | 3099 | — | unknown | DSP firmware code | DSPsoftwarecode | register value | ASCII | R | SOURCE_ONLY | source_claim | ;  |
| holding | 3100 | — | unknown | DSP firmware code | Identifier for the inverter DSP firmware build. | register value | ASCII | R | SOURCE_ONLY | source_claim | ;  |
| holding | 3101 | — | unknown | DSP firmware version | DSPSoftwareVersion | register value | ASCII | R | SOURCE_ONLY | source_claim | ;  |
| holding | 3103 | — | unknown | BDC monitor firmware | BDCmonitoringsoftware version | register value | ASCII | R | SOURCE_ONLY | source_claim | ;  |
| holding | 3104 | — | unknown | BMS MCU hardware version | BMS hardware version information | register value | ASCII | R | SOURCE_ONLY | source_claim | ;  |
| holding | 3105 | — | unknown | BMS firmware version | BMSsoftwareversion information | register value | ASCII | R | SOURCE_ONLY | source_claim | ;  |
| holding | 3106 | — | unknown | BMS manufacturer | BMSManufacturerName | register value | ASCII | R | SOURCE_ONLY | source_claim | ;  |
| holding | 3107 | — | unknown | BMS communication interface | BMSCommunicati oninterfacetype： 0:RS485; 1:CAN; | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| holding | 3108 | — | unknown | BDC module identifier 4 | SxxBxx | register value | ASCII | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 3109 | — | unknown | BDC module identifier 3 | DxxTxx | register value | ASCII | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 3110 | — | unknown | BDC module identifier 2 | PxxUxx | register value | ASCII | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 3111 | — | unknown | BDC module identifier 1 | Mxxxx | register value | ASCII | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 3113 | — | unknown | BDC protocol version | Bit8-bit15The majorversion numberranges from0-256.In principle,itcannot bechanged Bit0-bit7Minor versionnumber [0-256].Ifthe protocolis changed,youneed toupdatethis version No. | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| holding | 3118 | — | unknown | BDC on/off state | Indicates whether the battery DC converter is currently running (1) or idle (0). | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| holding | 3121 | — | unknown | Self-use power | Not yet surfaced by the Home Assistant integration. | register value; /10 | W | R | SOURCE_ONLY | source_claim | ;  |
| holding | 3122 | — | unknown | Self-use power | Not yet surfaced by the Home Assistant integration. | register value; /10 | W | R | SOURCE_ONLY | source_claim | ;  |
| holding | 3123 | — | unknown | System energy today | Available in firmware but not yet exposed as an integration attribute. | register value; /10 | kWh | R | SOURCE_ONLY | source_claim | ;  |
| holding | 3124 | — | unknown | System energy today | Available in firmware but not yet exposed as an integration attribute. | register value; /10 | kWh | R | SOURCE_ONLY | source_claim | ;  |
| input | 0 | inverter_status | supported | Inverter status | InverterStatus | register value; /10 | — | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 1 | pv_total_power | alternate | PV input power | PpvH | register value; /10 | 0.1W | R/W | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ; alternates: register:storage_mix:input:2, register:storage_mix:input:5, register:storage_mix:input:6, register:storage_mix:input:9, register:storage_mix:input:10, register:storage_mix:input:13, register:storage_mix:input:14, register:storage_mix:input:17, register:storage_mix:input:18, register:storage_mix:input:21, register:storage_mix:input:22, register:storage_mix:input:25, register:storage_mix:input:26, register:storage_mix:input:29, register:storage_mix:input:30, register:storage_mix:input:33, register:storage_mix:input:34 |
| input | 2 | pv_total_power | alternate | PV input power | PpvL | register value; /10 | 0.1W | R/W | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ; alternates: register:storage_mix:input:1, register:storage_mix:input:5, register:storage_mix:input:6, register:storage_mix:input:9, register:storage_mix:input:10, register:storage_mix:input:13, register:storage_mix:input:14, register:storage_mix:input:17, register:storage_mix:input:18, register:storage_mix:input:21, register:storage_mix:input:22, register:storage_mix:input:25, register:storage_mix:input:26, register:storage_mix:input:29, register:storage_mix:input:30, register:storage_mix:input:33, register:storage_mix:input:34 |
| input | 3 | — | unknown | PV1 DC voltage | Vpv1 | register value; /10 | 0.1V | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 4 | — | unknown | PV1 DC current | PV1Curr | register value; /10 | 0.1A | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 5 | pv_total_power | alternate | PV1 DC power | Ppv1H | register value; /10 | 0.1W | R/W | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ; alternates: register:storage_mix:input:1, register:storage_mix:input:2, register:storage_mix:input:6, register:storage_mix:input:9, register:storage_mix:input:10, register:storage_mix:input:13, register:storage_mix:input:14, register:storage_mix:input:17, register:storage_mix:input:18, register:storage_mix:input:21, register:storage_mix:input:22, register:storage_mix:input:25, register:storage_mix:input:26, register:storage_mix:input:29, register:storage_mix:input:30, register:storage_mix:input:33, register:storage_mix:input:34 |
| input | 6 | pv_total_power | alternate | PV1 DC power | Ppv1L | register value; /10 | 0.1W | R/W | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ; alternates: register:storage_mix:input:1, register:storage_mix:input:2, register:storage_mix:input:5, register:storage_mix:input:9, register:storage_mix:input:10, register:storage_mix:input:13, register:storage_mix:input:14, register:storage_mix:input:17, register:storage_mix:input:18, register:storage_mix:input:21, register:storage_mix:input:22, register:storage_mix:input:25, register:storage_mix:input:26, register:storage_mix:input:29, register:storage_mix:input:30, register:storage_mix:input:33, register:storage_mix:input:34 |
| input | 7 | — | unknown | PV2 DC voltage | Vpv2 | register value; /10 | 0.1V | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 8 | — | unknown | PV2 DC current | PV2Curr | register value; /10 | 0.1A | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 9 | pv_total_power | alternate | PV2 DC power | Ppv2H | register value; /10 | 0.1W | R/W | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ; alternates: register:storage_mix:input:1, register:storage_mix:input:2, register:storage_mix:input:5, register:storage_mix:input:6, register:storage_mix:input:10, register:storage_mix:input:13, register:storage_mix:input:14, register:storage_mix:input:17, register:storage_mix:input:18, register:storage_mix:input:21, register:storage_mix:input:22, register:storage_mix:input:25, register:storage_mix:input:26, register:storage_mix:input:29, register:storage_mix:input:30, register:storage_mix:input:33, register:storage_mix:input:34 |
| input | 10 | pv_total_power | alternate | PV2 DC power | Ppv2L | register value; /10 | 0.1W | R/W | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ; alternates: register:storage_mix:input:1, register:storage_mix:input:2, register:storage_mix:input:5, register:storage_mix:input:6, register:storage_mix:input:9, register:storage_mix:input:13, register:storage_mix:input:14, register:storage_mix:input:17, register:storage_mix:input:18, register:storage_mix:input:21, register:storage_mix:input:22, register:storage_mix:input:25, register:storage_mix:input:26, register:storage_mix:input:29, register:storage_mix:input:30, register:storage_mix:input:33, register:storage_mix:input:34 |
| input | 11 | — | unknown | PV3 DC voltage | Vpv3 | register value; /10 | 0.1V | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 12 | — | unknown | PV3 DC current | PV3Curr | register value; /10 | 0.1A | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 13 | pv_total_power | alternate | PV3 DC power | Ppv3H | register value; /10 | 0.1W | R/W | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ; alternates: register:storage_mix:input:1, register:storage_mix:input:2, register:storage_mix:input:5, register:storage_mix:input:6, register:storage_mix:input:9, register:storage_mix:input:10, register:storage_mix:input:14, register:storage_mix:input:17, register:storage_mix:input:18, register:storage_mix:input:21, register:storage_mix:input:22, register:storage_mix:input:25, register:storage_mix:input:26, register:storage_mix:input:29, register:storage_mix:input:30, register:storage_mix:input:33, register:storage_mix:input:34 |
| input | 14 | pv_total_power | alternate | PV3 DC power | Ppv3L | register value; /10 | 0.1W | R/W | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ; alternates: register:storage_mix:input:1, register:storage_mix:input:2, register:storage_mix:input:5, register:storage_mix:input:6, register:storage_mix:input:9, register:storage_mix:input:10, register:storage_mix:input:13, register:storage_mix:input:17, register:storage_mix:input:18, register:storage_mix:input:21, register:storage_mix:input:22, register:storage_mix:input:25, register:storage_mix:input:26, register:storage_mix:input:29, register:storage_mix:input:30, register:storage_mix:input:33, register:storage_mix:input:34 |
| input | 15 | — | unknown | PV4 DC voltage | Vpv4 | register value; /10 | 0.1V | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 16 | — | unknown | PV4 DC current | PV4Curr | register value; /10 | 0.1A | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 17 | pv_total_power | alternate | PV4 DC power | Ppv4H | register value; /10 | 0.1W | R/W | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ; alternates: register:storage_mix:input:1, register:storage_mix:input:2, register:storage_mix:input:5, register:storage_mix:input:6, register:storage_mix:input:9, register:storage_mix:input:10, register:storage_mix:input:13, register:storage_mix:input:14, register:storage_mix:input:18, register:storage_mix:input:21, register:storage_mix:input:22, register:storage_mix:input:25, register:storage_mix:input:26, register:storage_mix:input:29, register:storage_mix:input:30, register:storage_mix:input:33, register:storage_mix:input:34 |
| input | 18 | pv_total_power | alternate | PV4 DC power | Ppv4L | register value; /10 | 0.1W | R/W | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ; alternates: register:storage_mix:input:1, register:storage_mix:input:2, register:storage_mix:input:5, register:storage_mix:input:6, register:storage_mix:input:9, register:storage_mix:input:10, register:storage_mix:input:13, register:storage_mix:input:14, register:storage_mix:input:17, register:storage_mix:input:21, register:storage_mix:input:22, register:storage_mix:input:25, register:storage_mix:input:26, register:storage_mix:input:29, register:storage_mix:input:30, register:storage_mix:input:33, register:storage_mix:input:34 |
| input | 19 | — | unknown | PV5 DC voltage | Vpv5 | register value; /10 | 0.1V | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 20 | — | unknown | PV5 DC current | PV5Curr | register value; /10 | 0.1A | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 21 | pv_total_power | alternate | PV5 DC power | Ppv5H | register value; /10 | 0.1W | R/W | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ; alternates: register:storage_mix:input:1, register:storage_mix:input:2, register:storage_mix:input:5, register:storage_mix:input:6, register:storage_mix:input:9, register:storage_mix:input:10, register:storage_mix:input:13, register:storage_mix:input:14, register:storage_mix:input:17, register:storage_mix:input:18, register:storage_mix:input:22, register:storage_mix:input:25, register:storage_mix:input:26, register:storage_mix:input:29, register:storage_mix:input:30, register:storage_mix:input:33, register:storage_mix:input:34 |
| input | 22 | pv_total_power | alternate | PV5 DC power | Ppv5L | register value; /10 | 0.1W | R/W | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ; alternates: register:storage_mix:input:1, register:storage_mix:input:2, register:storage_mix:input:5, register:storage_mix:input:6, register:storage_mix:input:9, register:storage_mix:input:10, register:storage_mix:input:13, register:storage_mix:input:14, register:storage_mix:input:17, register:storage_mix:input:18, register:storage_mix:input:21, register:storage_mix:input:25, register:storage_mix:input:26, register:storage_mix:input:29, register:storage_mix:input:30, register:storage_mix:input:33, register:storage_mix:input:34 |
| input | 23 | — | unknown | PV6 DC voltage | Vpv6 | register value; /10 | 0.1V | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 24 | — | unknown | PV6 DC current | PV6Curr | register value; /10 | 0.1A | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 25 | pv_total_power | alternate | PV6 DC power | PV6inputpower(high) | register value; /10 | W | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ; alternates: register:storage_mix:input:1, register:storage_mix:input:2, register:storage_mix:input:5, register:storage_mix:input:6, register:storage_mix:input:9, register:storage_mix:input:10, register:storage_mix:input:13, register:storage_mix:input:14, register:storage_mix:input:17, register:storage_mix:input:18, register:storage_mix:input:21, register:storage_mix:input:22, register:storage_mix:input:26, register:storage_mix:input:29, register:storage_mix:input:30, register:storage_mix:input:33, register:storage_mix:input:34 |
| input | 26 | pv_total_power | alternate | PV6 DC power | PV6inputpower(low) | register value; /10 | W | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ; alternates: register:storage_mix:input:1, register:storage_mix:input:2, register:storage_mix:input:5, register:storage_mix:input:6, register:storage_mix:input:9, register:storage_mix:input:10, register:storage_mix:input:13, register:storage_mix:input:14, register:storage_mix:input:17, register:storage_mix:input:18, register:storage_mix:input:21, register:storage_mix:input:22, register:storage_mix:input:25, register:storage_mix:input:29, register:storage_mix:input:30, register:storage_mix:input:33, register:storage_mix:input:34 |
| input | 27 | — | unknown | PV7 DC voltage | PV7voltage | register value; /10 | V | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 28 | — | unknown | PV7 DC current | PV7inputcurrent | register value; /10 | A | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 29 | pv_total_power | alternate | PV7 DC power | PV7inputpower(high) | register value; /10 | W | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ; alternates: register:storage_mix:input:1, register:storage_mix:input:2, register:storage_mix:input:5, register:storage_mix:input:6, register:storage_mix:input:9, register:storage_mix:input:10, register:storage_mix:input:13, register:storage_mix:input:14, register:storage_mix:input:17, register:storage_mix:input:18, register:storage_mix:input:21, register:storage_mix:input:22, register:storage_mix:input:25, register:storage_mix:input:26, register:storage_mix:input:30, register:storage_mix:input:33, register:storage_mix:input:34 |
| input | 30 | pv_total_power | alternate | PV7 DC power | PV7inputpower(low) | register value; /10 | W | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ; alternates: register:storage_mix:input:1, register:storage_mix:input:2, register:storage_mix:input:5, register:storage_mix:input:6, register:storage_mix:input:9, register:storage_mix:input:10, register:storage_mix:input:13, register:storage_mix:input:14, register:storage_mix:input:17, register:storage_mix:input:18, register:storage_mix:input:21, register:storage_mix:input:22, register:storage_mix:input:25, register:storage_mix:input:26, register:storage_mix:input:29, register:storage_mix:input:33, register:storage_mix:input:34 |
| input | 31 | — | unknown | PV8 DC voltage | PV8voltage | register value; /10 | V | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 32 | — | unknown | PV8 DC current | PV8inputcurrent | register value; /10 | A | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 33 | pv_total_power | alternate | PV8 DC power | PV8inputpower(high) | register value; /10 | W | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ; alternates: register:storage_mix:input:1, register:storage_mix:input:2, register:storage_mix:input:5, register:storage_mix:input:6, register:storage_mix:input:9, register:storage_mix:input:10, register:storage_mix:input:13, register:storage_mix:input:14, register:storage_mix:input:17, register:storage_mix:input:18, register:storage_mix:input:21, register:storage_mix:input:22, register:storage_mix:input:25, register:storage_mix:input:26, register:storage_mix:input:29, register:storage_mix:input:30, register:storage_mix:input:34 |
| input | 34 | pv_total_power | alternate | PV8 DC power | PV8inputpower(low) | register value; /10 | W | R | RESOLVED | semantic_correlated, source_claim | ; alternates: register:storage_mix:input:1, register:storage_mix:input:2, register:storage_mix:input:5, register:storage_mix:input:6, register:storage_mix:input:9, register:storage_mix:input:10, register:storage_mix:input:13, register:storage_mix:input:14, register:storage_mix:input:17, register:storage_mix:input:18, register:storage_mix:input:21, register:storage_mix:input:22, register:storage_mix:input:25, register:storage_mix:input:26, register:storage_mix:input:29, register:storage_mix:input:30, register:storage_mix:input:33 |
| input | 35 | — | unknown | AC output power | Outputpower(high) | register value; /10 | W | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 36 | — | unknown | AC output power | Outputpower(low) | register value; /10 | W | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 37 | grid_frequency | alternate | Grid frequency | Gridfrequency | register value; /100 | Hz | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ; alternates: register:storage_mix:holding:62, register:storage_mix:holding:63, register:storage_mix:holding:72, register:storage_mix:holding:73, register:storage_mix:holding:74, register:storage_mix:holding:75, register:storage_mix:holding:78, register:storage_mix:holding:79 |
| input | 38 | — | unknown | AC phase L1 voltage | Three/singlephasegridvoltage | register value; /10 | V | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 39 | — | unknown | AC phase L1 current | Three/singlephasegridoutputcurrent | register value; /10 | A | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 40 | — | unknown | AC phase L1 power | Three/single phase grid output watt VA(high) | register value; /10 | W | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 41 | — | unknown | AC phase L1 power | Three/single phase grid output watt VA(low) | register value; /10 | W | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 42 | — | unknown | AC phase L2 voltage | Threephasegridvoltage | register value; /10 | V | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 43 | — | unknown | AC phase L2 current | Threephasegridoutputcurrent | register value; /10 | A | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 44 | — | unknown | AC phase L2 power | Threephasegridoutputpower(high) | register value; /10 | W | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 45 | — | unknown | AC phase L2 power | Threephasegridoutputpower(low) | register value; /10 | W | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 46 | — | unknown | AC phase L3 voltage | Threephasegridvoltage | register value; /10 | V | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 47 | — | unknown | AC phase L3 current | Threephasegridoutputcurrent | register value; /10 | A | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 48 | ac_phase_l3_power | alternate | AC phase L3 power | Threephasegridoutputpower(high) | register value; /10 | W | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ; alternates: register:storage_mix:input:49 |
| input | 49 | ac_phase_l3_power | alternate | AC phase L3 power | Threephasegridoutputpower(low) | register value; /10 | W | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ; alternates: register:storage_mix:input:48 |
| input | 50 | — | unknown | Vac_RS | Threephasegridvoltage | register value | Linevoltage | R | RESOLVED | semantic_correlated, source_claim | ;  |
| input | 51 | — | unknown | Vac_ST | Threephasegridvoltage | register value | Linevoltage | R | RESOLVED | semantic_correlated, source_claim | ;  |
| input | 52 | — | unknown | Vac_TR | Threephasegridvoltage | register value | Linevoltage | R | RESOLVED | semantic_correlated, source_claim | ;  |
| input | 53 | — | unknown | Output energy today | Todaygenerateenergy(high) | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 54 | — | unknown | Output energy today | Todaygenerateenergy(low) | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 55 | — | unknown | Output energy total | Totalgenerateenergy(high) | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 56 | — | unknown | Output energy total | Totalgenerateenergy(low) | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 57 | inverter_runtime | supported | Run time | Raw counter counts seconds; divide by 7200 to obtain hours. | register value; /7200 | h | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 58 | — | unknown | Run time | Raw counter counts seconds; divide by 7200 to obtain hours. | register value; /7200 | h | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 59 | — | unknown | PV1 energy today | PV1Energytoday(high) | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 60 | — | unknown | PV1 energy today | PV1Energytoday(low) | register value; /10 | kWh | R | RESOLVED | semantic_correlated, source_claim | ;  |
| input | 61 | — | unknown | PV1 energy total | PV1Energytotal(high) | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 62 | — | unknown | PV1 energy total | PV1Energytotal(low) | register value; /10 | kWh | R | RESOLVED | semantic_correlated, source_claim | ;  |
| input | 63 | — | unknown | PV2 energy today | PV2Energytoday(high) | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 64 | — | unknown | PV2 energy today | PV2Energytoday(low) | register value; /10 | kWh | R | RESOLVED | semantic_correlated, source_claim | ;  |
| input | 65 | — | unknown | PV2 energy total | PV2Energytotal(high) | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 66 | — | unknown | PV2 energy total | PV2Energytotal(low) | register value; /10 | kWh | R | RESOLVED | semantic_correlated, source_claim | ;  |
| input | 67 | — | unknown | PV3 energy today | PV3Energytoday(high) | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 68 | — | unknown | PV3 energy today | PV3Energytoday(low) | register value; /10 | kWh | R | RESOLVED | semantic_correlated, source_claim | ;  |
| input | 69 | — | unknown | PV3 energy total | PV3Energytotal(high) | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 70 | — | unknown | PV3 energy total | PV3Energytotal(low) | register value; /10 | kWh | R | RESOLVED | semantic_correlated, source_claim | ;  |
| input | 71 | — | unknown | PV4 energy today | PV4Energytoday(high) | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 72 | — | unknown | PV4 energy today | PV4Energytoday(low) | register value; /10 | kWh | R | RESOLVED | semantic_correlated, source_claim | ;  |
| input | 73 | pv4_energy_total | alternate | PV4 energy total | PV4Energytotal(high) | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ; alternates: register:storage_mix:input:74 |
| input | 74 | pv4_energy_total | alternate | PV4 energy total | PV4Energytotal(low) | register value; /10 | kWh | R | RESOLVED | semantic_correlated, source_claim | ; alternates: register:storage_mix:input:73 |
| input | 75 | — | unknown | PV5 energy today | PV5Energytoday(high) | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 76 | — | unknown | PV5 energy today | PV5Energytoday(low) | register value; /10 | kWh | R | RESOLVED | semantic_correlated, source_claim | ;  |
| input | 77 | — | unknown | PV5 energy total | PV5Energytotal(high) | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 78 | — | unknown | PV5 energy total | PV5Energytotal(low) | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 79 | — | unknown | PV6 energy today | PV6Energytoday(high) | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 80 | — | unknown | PV6 energy today | PV6Energytoday(low) | register value; /10 | kWh | R | RESOLVED | semantic_correlated, source_claim | ;  |
| input | 81 | — | unknown | PV6 energy total | PV6Energytotal(high) | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 82 | — | unknown | PV6 energy total | PV6Energytotal(low) | register value; /10 | kWh | R | RESOLVED | semantic_correlated, source_claim | ;  |
| input | 83 | — | unknown | PV7 energy today | PV7Energytoday(high) | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 84 | — | unknown | PV7 energy today | PV7Energytoday(low) | register value; /10 | kWh | R | RESOLVED | semantic_correlated, source_claim | ;  |
| input | 85 | — | unknown | PV7 energy total | PV7Energytotal(high) | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 86 | — | unknown | PV7 energy total | PV7Energytotal(low) | register value; /10 | kWh | R | RESOLVED | semantic_correlated, source_claim | ;  |
| input | 87 | — | unknown | PV8 energy today | PV8Energytoday(high) | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 88 | — | unknown | PV8 energy today | PV8Energytoday(low) | register value; /10 | kWh | R | RESOLVED | semantic_correlated, source_claim | ;  |
| input | 89 | — | unknown | PV8 energy total | PV8Energytotal(high) | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 90 | — | unknown | PV8 energy total | PV8Energytotal(low) | register value; /10 | kWh | R | RESOLVED | semantic_correlated, source_claim | ;  |
| input | 91 | — | unknown | PV energy total | PVEnergytotal(high) | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 92 | — | unknown | PV energy total | PVEnergytotal(low) | register value; /10 | kWh | R | RESOLVED | semantic_correlated, source_claim | ;  |
| input | 93 | — | unknown | Inverter temperature | Invertertemperature | register value; /10 | °C | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 94 | — | unknown | IPM temperature | TheinsideIPMininverterTemperature | register value; /10 | °C | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 95 | — | unknown | Boost temperature | Boosttemperature | register value; /10 | °C | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 96 | — | unknown | Temp4 | Temp4 | register value | reserved | R | SOURCE_ONLY | source_claim | ;  |
| input | 97 | — | unknown | uwBatVolt_DSP | BatVolt_DSP | register value | BatVolt(DSP) | R | SOURCE_ONLY | source_claim | ;  |
| input | 98 | — | unknown | P-bus voltage | PBusinsideVoltage | register value; /10 | V | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 99 | — | unknown | N-bus voltage | NBusinsideVoltage | register value; /10 | V | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 100 | — | unknown | IPF | InverteroutputPFnow | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 101 | — | unknown | Output power percentage | RealOutputpowerPercent | register value; /10 | % | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 102 | — | unknown | OPFullwattH | OutputMaxpowerLimitedhigh | register value | W | R | RESOLVED | semantic_correlated, source_claim | ;  |
| input | 103 | — | unknown | OPFullwattL | OutputMaxpowerLimitedlow | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 104 | — | unknown | Derating mode | DeratingMode | register value; /10 | — | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 105 | — | unknown | Fault code | Inverterfaultmaincode | register value; /10 | — | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 106 | — | unknown | Register 106 | — | register value | — | R | UNKNOWN_RESERVED | source_claim | ;  |
| input | 107 | — | unknown | FaultSubcode | Inverterfaultsubcode | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 108 | — | unknown | RemoteCtrlEn | / | register value | StoragePow er(SPA) | R | SOURCE_ONLY | source_claim | ;  |
| input | 109 | — | unknown | RemoteCtrlPow er | / | register value | StoragePow er(SPA) | R | SOURCE_ONLY | source_claim | ;  |
| input | 110 | — | unknown | Warning code | WarningbitH | register value; /10 | — | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 111 | — | unknown | Warning code | Inverterwarnsubcode | register value; /10 | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 112 | — | unknown | WarnMaincode | Inverterwarnmaincode | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 113 | — | unknown | real Power Percent | realPowerPercent | register value | MAX | R | SOURCE_ONLY | source_claim | ;  |
| input | 114 | — | unknown | inv start delay time | invstartdelaytime | register value | MAX | R | SOURCE_ONLY | source_claim | ;  |
| input | 115 | — | unknown | bINVAllFaultCod e | bINVAllFaultCode | register value | MAX | R | SOURCE_ONLY | source_claim | ;  |
| input | 116 | — | unknown | AC charge Power_H | Gridpowertolocalload | register value | Storage Power | R | SOURCE_ONLY | source_claim | ;  |
| input | 117 | — | unknown | AC charge Power_L | Gridpowertolocalload | register value | Storage Power | R | SOURCE_ONLY | source_claim | ;  |
| input | 118 | — | unknown | Priority | 0:LoadFirst | register value | Storage | R | RESOLVED | semantic_correlated, source_claim | ;  |
| input | 119 | — | unknown | BatteryType | 0：Lead-acid 1：Lithiumbattery | register value | — | R | RESOLVED | semantic_correlated, source_claim | ;  |
| input | 120 | — | unknown | AutoProofreadC MD | Aging mode Auto-calibration command | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 121 | — | unknown | Register 121 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| input | 122 | — | unknown | Register 122 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| input | 123 | — | unknown | Register 123 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| input | 124 | — | unknown | reserved | reserved | register value | — | R | UNKNOWN_RESERVED | source_claim | ;  |
| input | 1000 | — | unknown | uwSysWorkMode | uwSysWorkMode | register value | — | W | SOURCE_ONLY | source_claim | ;  |
| input | 1001 | — | unknown | Systemfaultword0 | Systemfaultword0 | register value | Please refer to thefault description of Hybrid | R | SOURCE_ONLY | source_claim | ;  |
| input | 1002 | — | unknown | Systemfaultword1 | Systemfaultword1 | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 1003 | — | unknown | Systemfaultword2 | Systemfaultword2 | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 1004 | — | unknown | Systemfaultword3 | Systemfaultword3 | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 1005 | — | unknown | Systemfaultword4 | Systemfaultword4 | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 1006 | — | unknown | Systemfaultword5 | Systemfaultword5 | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 1007 | — | unknown | Systemfaultword6 | Systemfaultword6 | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 1008 | — | unknown | Systemfaultword7 | Systemfaultword7 | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 1009 | battery_discharge_power | alternate | Pdischarge1H | Dischargepower(high) | register value; /10 | W | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ; alternates: register:storage_mix:input:3178, register:storage_mix:input:3179 |
| input | 1010 | — | unknown | Pdischarge1L | Dischargepower(low) | register value; /10 | W | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 1011 | battery_charge_power | alternate | Pcharge1H | Chargepower(high) | register value; /10 | W | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ; alternates: register:storage_mix:input:3180, register:storage_mix:input:3181 |
| input | 1012 | — | unknown | Pcharge1L | Chargepower(low) | register value; /10 | W | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 1013 | — | unknown | Vbat | Batteryvoltage | register value | V | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 1014 | battery_soc | alternate | SOC | StateofchargeCapacity | register value; /10 | lith/leadacid | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ; alternates: register:storage_mix:input:3171, register:storage_mix:input:3196, register:storage_mix:input:3197, register:storage_mix:input:3215 |
| input | 1015 | — | unknown | PactouserR H | ACpowertouserH | register value | W | R | RESOLVED | semantic_correlated, source_claim | ;  |
| input | 1016 | — | unknown | PactouserR L | ACpowertouserL | register value | W | R | RESOLVED | semantic_correlated, source_claim | ;  |
| input | 1017 | — | unknown | PactouserS H | PactouserS H | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 1018 | — | unknown | PactouserS L | PactouserS L | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 1019 | — | unknown | PactouserT H | PactouserT H | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 1020 | — | unknown | PactouserT L | PactouserT H | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 1021 | — | unknown | PactouserTotalH | ACpowertousertotalH | register value; /10 | W | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 1022 | — | unknown | PactouserTotalL | ACpowertousertotalL | register value; /10 | W | R | RESOLVED | semantic_correlated, source_claim | ;  |
| input | 1023 | — | unknown | PactogridR H | ACpowertogridH | register value | Ac output | R | RESOLVED | semantic_correlated, source_claim | ;  |
| input | 1024 | — | unknown | PactogridR L | ACpowertogridL | register value | W | R | RESOLVED | semantic_correlated, source_claim | ;  |
| input | 1025 | — | unknown | PactogridS H | PactogridS H | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 1026 | — | unknown | PactogridS L | PactogridS L | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 1027 | — | unknown | PactogridTH | 0.1w | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 1028 | — | unknown | PactogridTL | 0.1w | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 1029 | — | unknown | pac_to_grid_total | 0.1w | register value; /10 | W | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 1030 | — | unknown | PactogridtotalL | 0.1w | register value; /10 | W | R | RESOLVED | semantic_correlated, source_claim | ;  |
| input | 1031 | — | unknown | PLocalLoadR H | 0.1w | register value | W | R | RESOLVED | semantic_correlated, source_claim | ;  |
| input | 1032 | — | unknown | PLocalLoadR L | 0.1w | register value | W | R | RESOLVED | semantic_correlated, source_claim | ;  |
| input | 1033 | — | unknown | PLocalLoadS H | 0.1w | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 1034 | — | unknown | PLocalLoadS L | 0.1w | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 1035 | — | unknown | PLocalLoadT H | 0.1w | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 1036 | — | unknown | PLocalLoadT L | 0.1w | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 1037 | — | unknown | PLocalLoadtotalH | 0.1w | register value | W | R | RESOLVED | semantic_correlated, source_claim | ;  |
| input | 1038 | — | unknown | PLocalLoadtotalL | 0.1w | register value | W | R | RESOLVED | semantic_correlated, source_claim | ;  |
| input | 1039 | — | unknown | IP2MTemperature | 0.1℃ | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 1040 | — | unknown | B2attery Temperature | 0.1℃ | register value | °C | R | RESOLVED | semantic_correlated, source_claim | ;  |
| input | 1041 | — | unknown | SPDSPStatus | SPDSPStatus | register value | — | R | RESOLVED | semantic_correlated, source_claim | ;  |
| input | 1042 | — | unknown | SPBusVolt | 0.1V | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 1043 | — | unknown | Register 1043 | — | register value | — | R | UNKNOWN_RESERVED | source_claim | ;  |
| input | 1044 | — | unknown | Etouser_todayH | Etouser_todayH | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 1045 | — | unknown | Etouser_todayL | Etouser_todayL | register value; /10 | kWh | W | RESOLVED | semantic_correlated, source_claim | ;  |
| input | 1046 | — | unknown | Etouser_totalH | Etouser_totalH | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 1047 | — | unknown | Etouser_totalL | Etouser_totalL | register value; /10 | kWh | R | RESOLVED | semantic_correlated, source_claim | ;  |
| input | 1048 | — | unknown | Etogrid_todayH | Etogrid_todayH | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 1049 | — | unknown | Etogrid_todayL | Etogrid_todayL | register value; /10 | kWh | W | RESOLVED | semantic_correlated, source_claim | ;  |
| input | 1050 | — | unknown | Etogrid_totalH | Etogrid_totalH | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 1051 | — | unknown | Etogrid_totalL | Etogrid_totalL | register value; /10 | kWh | R | RESOLVED | semantic_correlated, source_claim | ;  |
| input | 1052 | — | unknown | Edischarge1_toda yH | Edischarge1_toda yH | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 1053 | — | unknown | Edischarge1_toda yL | Edischarge1_toda yL | register value; /10 | kWh | R | RESOLVED | semantic_correlated, source_claim | ;  |
| input | 1054 | — | unknown | Edischarge1_total H | Edischarge1_total H | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 1055 | — | unknown | Edischarge1_total L | Edischarge1_total L | register value; /10 | kWh | W | RESOLVED | semantic_correlated, source_claim | ;  |
| input | 1056 | — | unknown | Echarge1_todayH | Echarge1_todayH | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 1057 | — | unknown | Echarge1_today L | Echarge1_today L | register value; /10 | kWh | R | RESOLVED | semantic_correlated, source_claim | ;  |
| input | 1058 | — | unknown | Echarge1_totalH | Echarge1_totalH | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 1059 | — | unknown | Echarge1_totalL | Echarge1_totalL | register value; /10 | kWh | R | RESOLVED | semantic_correlated, source_claim | ;  |
| input | 1060 | — | unknown | Register 1060 | Localloadenergytoday | register value | kWh | R | UNKNOWN_RESERVED | semantic_correlated, source_claim | ;  |
| input | 1061 | — | unknown | Register 1061 | Localloadenergytoday | register value | kWh | R | UNKNOWN_RESERVED | semantic_correlated, source_claim | ;  |
| input | 1062 | — | unknown | Register 1062 | Localloadenergytotal | register value | kWh | R | UNKNOWN_RESERVED | semantic_correlated, source_claim | ;  |
| input | 1063 | — | unknown | Register 1063 | Localloadenergytotal | register value | kWh | R | UNKNOWN_RESERVED | semantic_correlated, source_claim | ;  |
| input | 1064 | — | unknown | Register 1064 | ExportLimitApparentPowerH | register value | — | W | UNKNOWN_RESERVED | source_claim | ;  |
| input | 1065 | — | unknown | Register 1065 | ExportLimitApparentPowerL | register value | — | W | UNKNOWN_RESERVED | source_claim | ;  |
| input | 1066 | — | unknown | Register 1066 | / | register value | — | R | UNKNOWN_RESERVED | source_claim | ;  |
| input | 1067 | — | unknown | EpsFac | UPSfrequency | register value | — | R | RESOLVED | semantic_correlated, source_claim | ;  |
| input | 1068 | — | unknown | EpsVac1 | UPSphaseRoutputvoltage | register value | — | R | RESOLVED | semantic_correlated, source_claim | ;  |
| input | 1069 | — | unknown | EpsIac1 | UPSphaseRoutputcurrent | register value | — | R | RESOLVED | semantic_correlated, source_claim | ;  |
| input | 1070 | — | unknown | EpsPac1 | UPSphaseRoutputpower(H) | register value | — | R | RESOLVED | semantic_correlated, source_claim | ;  |
| input | 1071 | — | unknown | EpsPac1 | UPSphaseRoutputpower(L) | register value | — | R | RESOLVED | semantic_correlated, source_claim | ;  |
| input | 1072 | — | unknown | EpsVac2 | UPSphaseSoutputvoltage | register value | — | R | RESOLVED | semantic_correlated, source_claim | ;  |
| input | 1073 | — | unknown | EpsIac2 | UPSphaseSoutputcurrent | register value | — | R | RESOLVED | semantic_correlated, source_claim | ;  |
| input | 1074 | — | unknown | EpsPac2 | UPSphaseSoutputpower(H) | register value | — | R | RESOLVED | semantic_correlated, source_claim | ;  |
| input | 1075 | — | unknown | EpsPac2 | UPSphaseSoutputpower(L) | register value | — | R | RESOLVED | semantic_correlated, source_claim | ;  |
| input | 1076 | — | unknown | EpsVac3 | UPSphaseToutputvoltage | register value | — | R | RESOLVED | semantic_correlated, source_claim | ;  |
| input | 1077 | — | unknown | EpsIac3 | UPSphaseToutputcurrent | register value | — | R | RESOLVED | semantic_correlated, source_claim | ;  |
| input | 1078 | — | unknown | EpsPac3 | UPSphaseToutputpower(H) | register value | — | R | RESOLVED | semantic_correlated, source_claim | ;  |
| input | 1079 | — | unknown | EpsPac3 | UPSphaseToutputpower(L) | register value | — | R | RESOLVED | semantic_correlated, source_claim | ;  |
| input | 1080 | — | unknown | EpsLoadPercent | LoadpercentofUPSouput | register value | — | R | RESOLVED | semantic_correlated, source_claim | ;  |
| input | 1081 | — | unknown | EpsPF | Powerfactor | register value | — | R | RESOLVED | semantic_correlated, source_claim | ;  |
| input | 1082 | — | unknown | Register 1082 | StatusOldfromBMS | register value | — | R | UNKNOWN_RESERVED | source_claim | ;  |
| input | 1083 | — | unknown | Register 1083 | StatusfromBMS | register value | — | R | UNKNOWN_RESERVED | source_claim | ;  |
| input | 1084 | — | unknown | Register 1084 | ErrorinfoOldfromBMS | register value | — | R | UNKNOWN_RESERVED | source_claim | ;  |
| input | 1085 | — | unknown | Register 1085 | ErrorinfomationfromBMS | register value | — | R | UNKNOWN_RESERVED | source_claim | ;  |
| input | 1086 | — | unknown | Register 1086 | SOCfromBMS | register value | — | R | UNKNOWN_RESERVED | source_claim | ;  |
| input | 1087 | — | unknown | Register 1087 | BatteryvoltagefromBMS | register value | — | R | UNKNOWN_RESERVED | source_claim | ;  |
| input | 1088 | — | unknown | Register 1088 | BatterycurrentfromBMS | register value | — | R | UNKNOWN_RESERVED | source_claim | ;  |
| input | 1089 | — | unknown | Register 1089 | BatterytemperaturefromBMS | register value | — | R | UNKNOWN_RESERVED | source_claim | ;  |
| input | 1090 | — | unknown | BMS_MaxCurr | Max. charge/discharge current fromBMS(pylon) | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 1091 | — | unknown | BMS_GaugeRM | GaugeRMfromBMS | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 1092 | — | unknown | BMS_GaugeFCC | GaugeFCCfromBMS | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 1093 | — | unknown | BMS_FW | BMS_FW | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 1094 | — | unknown | BMS_DeltaVolt | DeltaVfromBMS | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 1095 | — | unknown | BMS_CycleCnt | CycleCountfromBMS | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 1096 | — | unknown | BMS_SOH | SOHfromBMS | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 1097 | — | unknown | BMS_ConstantV olt | CVvoltagefromBMS | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 1098 | — | unknown | BMS_WarnInfoO ld | WarninginfooldfromBMS | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 1099 | — | unknown | BMS_WarnInfo | WarninginfofromBMS | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 1100 | — | unknown | BMS_GaugeICCu rr | GaugeICcurrentfromBMS | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 1101 | — | unknown | BMS_MCUVersi on | MCUSoftwareversionfromBMS | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 1102 | — | unknown | BMS_GaugeVers ion | GaugeVersionfromBMS | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 1103 | — | unknown | BMS_wGaugeFR Version_L | GaugeFRVersionL16fromBMS | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 1104 | — | unknown | BMS_wGaugeFR Version_H | GaugeFRVersionH16fromBMS | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 1105 | — | unknown | BMS_BMSInfo | BMSInformationfromBMS | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 1106 | — | unknown | BMS_PackInfo | PackInformationfromBMS | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 1107 | — | unknown | BMS_UsingCap | UsingCapfromBMS | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 1108 | — | unknown | uwMaxCellVolt | Maximumsinglebatteryvoltage | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 1109 | — | unknown | uwMinCellVolt | Lowestsinglebatteryvoltage | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 1110 | — | unknown | bModuleNum | Batteryparallelnumber | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 1111 | — | unknown | Numberofbatteries | Numberofbatteries | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 1112 | — | unknown | uwMaxVoltCellN o | MaxVoltCellNo | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 1113 | — | unknown | uwMinVoltCellN o | MinVoltCellNo | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 1114 | — | unknown | uwMaxTemprCe ll_10T | MaxTemprCell_10T | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 1115 | — | unknown | uwMinTemprCel l_10T | MinTemprCell_10T | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 1116 | — | unknown | uwMaxTemprCe llNo | MaxVoltTemprCellNo | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 1117 | — | unknown | uwMinTemprCel | MinVoltTemprCellNo | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 1118 | — | unknown | ProtectpackID | FaultyBatteryAddress | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 1119 | — | unknown | MaxSOC | ParallelmaximumSOC | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 1120 | — | unknown | MinSOC | ParallelminimumSOC | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 1121 | — | unknown | BMS_Error2 | BatteryProtection2 | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 1122 | — | unknown | BMS_Error3 | BatteryProtection3 | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 1123 | — | unknown | BMS_WarnInfo2 | BatteryWarn2 | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 1124 | — | unknown | ACCharge EnergyTodayH | ACChargeEnergytoday | register value | kWh | W | RESOLVED | semantic_correlated, source_claim | ;  |
| input | 3041 | grid_import_power | supported | Load supply power | Totalforwardpower | register value; /10 | Total forward power | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3042 | — | unknown | Load supply power | Real-time active power delivered to on-site (self-consumption) loads. | register value; /10 | W | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3043 | grid_export_power | alternate | Grid export power | Totalreversepower | register value; /10 | Totalreverse power | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ; alternates: register:storage_mix:input:3044, register:storage_mix:input:3071, register:storage_mix:input:3072, register:storage_mix:input:3073, register:storage_mix:input:3074 |
| input | 3044 | grid_export_power | alternate | Grid export power | Active power exported to the utility grid. | register value; /10 | W | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ; alternates: register:storage_mix:input:3043, register:storage_mix:input:3071, register:storage_mix:input:3072, register:storage_mix:input:3073, register:storage_mix:input:3074 |
| input | 3045 | house_load_power | supported | Home load power | Totalloadpower | register value; /10 | Total load power | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3046 | — | unknown | Home load power | Aggregate instantaneous demand from on-site loads. | register value; /10 | W | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3067 | — | unknown | Load energy today | Todayenergytouser | register value; /10 | Todayenergy touser | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3068 | — | unknown | Load energy today | Energy delivered to on-site loads today (0.1 kWh resolution). | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3069 | — | unknown | Load energy total | Totalenergytouser | register value; /10 | Totalenergy touser | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3070 | — | unknown | Load energy total | Lifetime energy delivered to on-site loads (0.1 kWh resolution). | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3071 | grid_export_power | alternate | Export energy today | Todayenergytogrid | register value; /10 | Todayenergy togrid | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ; alternates: register:storage_mix:input:3043, register:storage_mix:input:3044, register:storage_mix:input:3072, register:storage_mix:input:3073, register:storage_mix:input:3074 |
| input | 3072 | grid_export_power | alternate | Export energy today | Energy exported to the grid today (0.1 kWh resolution). | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ; alternates: register:storage_mix:input:3043, register:storage_mix:input:3044, register:storage_mix:input:3071, register:storage_mix:input:3073, register:storage_mix:input:3074 |
| input | 3073 | grid_export_power | alternate | Export energy total | Totalenergytogrid | register value; /10 | Totalenergy togrid | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ; alternates: register:storage_mix:input:3043, register:storage_mix:input:3044, register:storage_mix:input:3071, register:storage_mix:input:3072, register:storage_mix:input:3074 |
| input | 3074 | grid_export_power | alternate | Export energy total | Lifetime energy exported to the grid (0.1 kWh resolution). | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ; alternates: register:storage_mix:input:3043, register:storage_mix:input:3044, register:storage_mix:input:3071, register:storage_mix:input:3072, register:storage_mix:input:3073 |
| input | 3097 | — | unknown | Communication board temperature | Commmunicationbroadtemperature | register value; /10 | °C | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3111 | — | unknown | Warning code | PresentFFTValue[CHANNEL_A] | register value; /1 | — | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3115 | — | unknown | Inverter start delay | invstartdelaytime | register value; /1 | invstartdelay time | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3125 | — | unknown | Battery discharge today | Todaydischargeenergy | register value; /10 | Today discharge energy | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3126 | — | unknown | Battery discharge today | Energy discharged from the battery into the AC system today (0.1 kWh resolution). | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3127 | — | unknown | Battery discharge total | Totaldischargeenergy | register value; /10 | Total discharge energy | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3128 | — | unknown | Battery discharge total | Total energy discharged from the battery (0.1 kWh resolution). | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3129 | — | unknown | Battery charge today | Chargeenergytoday | register value; /10 | Charge energytoday | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3130 | — | unknown | Battery charge today | Energy charged into the battery today (0.1 kWh resolution). | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3131 | — | unknown | Battery charge total | Chargeenergytotal | register value; /10 | Charge energytotal | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3132 | — | unknown | Battery charge total | Total energy charged into the battery (0.1 kWh resolution). | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3164 | — | unknown | BDC presence flag | WhethertoparseBDCdataseparately | register value; /1 | 0:Don'tneed 1：need | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3169 | battery_voltage | alternate | Battery voltage | Batteryvoltage | register value; /100 | V | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ; alternates: register:storage_mix:input:3216 |
| input | 3170 | battery_current | alternate | Battery current | Batterycurrent | register value; /10 | A | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ; alternates: register:storage_mix:input:3217 |
| input | 3171 | battery_soc | alternate | Battery SOC | StateofchargeCapacity | register value; /1 | % | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ; alternates: register:storage_mix:input:1014, register:storage_mix:input:3196, register:storage_mix:input:3197, register:storage_mix:input:3215 |
| input | 3172 | — | unknown | VBUS1 voltage | TotalBUSvoltage | register value; /10 | V | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3173 | — | unknown | VBUS2 voltage | OntheBUSvoltage | register value; /10 | V | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3174 | — | unknown | Buck/boost current | BUCK-BOOSTCurrent | register value; /10 | A | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3175 | — | unknown | LLC stage current | LLCCurrent | register value; /10 | A | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3176 | — | unknown | Battery temperature A | TempertureA | register value; /10 | °C | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3177 | — | unknown | Battery temperature B | TempertureB | register value; /10 | °C | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3178 | battery_discharge_power | alternate | Battery discharge power | Dischargepower | register value; /10 | W | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ; alternates: register:storage_mix:input:1009, register:storage_mix:input:3179 |
| input | 3179 | battery_discharge_power | alternate | Battery discharge power | Real-time discharge power flowing from the battery (0.1 W resolution). | register value; /10 | W | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ; alternates: register:storage_mix:input:1009, register:storage_mix:input:3178 |
| input | 3180 | battery_charge_power | alternate | Battery charge power | Chargepower | register value; /10 | W | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ; alternates: register:storage_mix:input:1011, register:storage_mix:input:3181 |
| input | 3181 | battery_charge_power | alternate | Battery charge power | Real-time charge power flowing into the battery (0.1 W resolution). | register value; /10 | W | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ; alternates: register:storage_mix:input:1011, register:storage_mix:input:3180 |
| input | 3189 | — | unknown | BMS max cell index | BmsMaxVoltCellNo | register value; /1 | — | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3190 | — | unknown | BMS min cell index | BmsMinVoltCellNo | register value; /1 | — | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3191 | — | unknown | BMS average temperature A | BmsBatteryAvgTemp | register value; /1 | °C | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3192 | — | unknown | BMS max cell temperature A | BmsMaxCellTemp | register value; /10 | °C | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3193 | — | unknown | BMS average temperature B | BmsBatteryAvgTemp | register value; /10 | °C | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3194 | — | unknown | BMS max cell temperature B | BmsMaxCellTemp | register value; /1 | °C | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3195 | — | unknown | BMS average temperature C | BmsBatteryAvgTemp | register value; /1 | °C | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3196 | battery_soc | alternate | BMS max SOC | BmsMaxSOC | register value; /1 | % | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ; alternates: register:storage_mix:input:1014, register:storage_mix:input:3171, register:storage_mix:input:3197, register:storage_mix:input:3215 |
| input | 3197 | battery_soc | alternate | BMS min SOC | BmsMinSOC | register value; /1 | % | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ; alternates: register:storage_mix:input:1014, register:storage_mix:input:3171, register:storage_mix:input:3196, register:storage_mix:input:3215 |
| input | 3198 | — | unknown | Parallel battery count | ParallelBatteryNum | register value; /1 | — | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3199 | — | unknown | BMS derate reason | BmsDerateReason | register value; /1 | — | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3200 | — | unknown | BMS full charge capacity | BmsGaugeFCC（Ah） | register value; /1 | Ah | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3201 | — | unknown | BMS remaining capacity | BmsGaugeRM（Ah） | register value; /1 | Ah | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3202 | — | unknown | BMS protect flags 1 | BMSProtect1 | register value; /1 | — | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3203 | — | unknown | BMS warning flags 1 | BMSWarn1 | register value; /1 | — | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3204 | — | unknown | BMS fault flags 1 | BMSFault1 | register value; /1 | — | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3205 | — | unknown | BMS fault flags 2 | BMSFault2 | register value; /1 | — | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3210 | — | unknown | Battery insulation status | BatteryISOdetectionstatus | register value; /1 | 0：Not detected 1：Detection completed | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3211 | — | unknown | Battery request flags | batteryworkrequest | register value; /1 | — | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3212 | — | unknown | BMS status | batteryworkingstatus | register value; /1 | 0:dormancy 1:Charge 2:Discharge 3:free 4:standby 5:Softstart 6:fault 7:update | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3213 | — | unknown | BMS protect flags 2 | BMSProtect2 | register value; /1 | — | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3214 | — | unknown | BMS warning flags 2 | BMSWarn2 | register value; /1 | — | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3215 | battery_soc | alternate | BMS SOC | BMSSOC | register value; /1 | % | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ; alternates: register:storage_mix:input:1014, register:storage_mix:input:3171, register:storage_mix:input:3196, register:storage_mix:input:3197 |
| input | 3216 | battery_voltage | alternate | BMS battery voltage | BMSBatteryVolt | register value; /100 | V | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ; alternates: register:storage_mix:input:3169 |
| input | 3217 | battery_current | alternate | BMS battery current | Positive values indicate discharge from the battery; negative values indicate charging. | register value; /100 | A | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ; alternates: register:storage_mix:input:3170 |
| input | 3218 | — | unknown | BMS max cell temperature | batterycellmaximumtemperature | register value; /10 | °C | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3219 | — | unknown | BMS max charge current | Maximumchargingcurrent | register value; /100 | A | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3220 | — | unknown | BMS max discharge current | Maximumdischargecurrent | register value; /100 | A | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3221 | — | unknown | BMS cycle count | BMSCycleCnt | register value; /1 | — | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3222 | — | unknown | BMS state of health | BMSSOH | register value; /1 | % | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3223 | — | unknown | BMS charge voltage limit | Batterychargingvoltagelimitvalue | register value; /100 | V | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3224 | — | unknown | BMS discharge voltage limit | Batterydischargevoltagelimitvalue | register value; /1 | V | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3225 | — | unknown | BMS warning flags 3 | BMSWarn3 | register value; /1 | — | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3226 | — | unknown | BMS protect flags 3 | BMSProtect3 | register value; /1 | — | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3230 | — | unknown | BMS max cell voltage | BMSBatterySingleVoltMax | register value; /1 | V | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 3231 | — | unknown | BMS min cell voltage | BMSBatterySingleVoltMin | register value; /1 | V | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |

### SPA storage

Storage family applicability comes from the graph/catalogue ranges.

| Table | Address | Semantic | Role | Name | Description | Encoding / scale | Unit | Access | Status | Evidence | Notes |
|---|---:|---|---|---|---|---|---|---|---|---|---|
| holding | 0 | — | unknown | Inverter Enabled | Theinvertercanbeswitched onandoff,andtheBDCcanbe switchedonandoffforthe battreadyfunction. | register value; /10 | — | R/W | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| holding | 1 | — | unknown | Safety function enable flags | SPI: system protection interface Bit0~3:forCEI0-21 Bit4~6:forSAA | register value | — | W | SOURCE_ONLY | source_claim | ;  |
| holding | 2 | — | unknown | Persist power-factor commands | Means these settings will be acting or not when next poweron | register value | — | W | RESOLVED | semantic_correlated, source_claim | ;  |
| holding | 3 | — | unknown | Active power limit setpoint | 255:powerisnotbelimited | register value; /1 | % | W | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| holding | 4 | — | unknown | Reactive power limit setpoint | 255:powerisnotbelimited | register value; /1 | % | W | SOURCE_ONLY | source_claim | ;  |
| holding | 5 | — | unknown | Power factor target | Inverter output power factor’s10000times | register value; /10000 | pf | W | SOURCE_ONLY | source_claim | ;  |
| holding | 6 | — | unknown | Rated apparent power | Normal power(high) | register value; /10 | 0.1VA | R | SOURCE_ONLY | source_claim | ;  |
| holding | 7 | — | unknown | Rated apparent power | Normal power(low) | register value; /10 | 0.1VA | R | SOURCE_ONLY | source_claim | ;  |
| holding | 8 | — | unknown | Nominal PV voltage | NormalworkPV voltage | register value; /10 | 0.1V | R | SOURCE_ONLY | source_claim | ;  |
| holding | 9 | — | unknown | Firmware | Firmwareversion (high) | firmware_version; /10 | ASCII | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| holding | 10 | — | unknown | Firmware | Firmwareversion (middle) | register value | ASCII | R | SOURCE_ONLY | source_claim | ;  |
| holding | 11 | — | unknown | Firmware | Firmwareversion(low) | register value | ASCII | R | SOURCE_ONLY | source_claim | ;  |
| holding | 12 | — | unknown | Firmware | ControlFirmware version(high) | register value | ASCII | R | SOURCE_ONLY | source_claim | ;  |
| holding | 13 | — | unknown | Firmware | ControlFirmware version(middle) | register value | ASCII | R | SOURCE_ONLY | source_claim | ;  |
| holding | 14 | — | unknown | Firmware | ControlFirmware version(low) | register value | ASCII | R | SOURCE_ONLY | source_claim | ;  |
| holding | 15 | — | unknown | LCD language selection | 0:Italian; 1:English; 2:German; 3:Spanish; 4:French; 5:Chinese; 6：Polish 7：Portugues 8：Hungary | register value | — | W | SOURCE_ONLY | source_claim | ;  |
| holding | 16 | — | unknown | Country profile configured | CountrySelectedor not | register value | — | W | SOURCE_ONLY | source_claim | ;  |
| holding | 17 | — | unknown | PV start voltage threshold | Inputstartvoltage | register value; /10 | 0.1V | W | SOURCE_ONLY | source_claim | ;  |
| holding | 18 | — | unknown | Start-up delay | Starttime | register value; /1 | 1s | W | SOURCE_ONLY | source_claim | ;  |
| holding | 19 | — | unknown | Restart delay | RestartDelayTime afterfaultback; | register value; /1 | 1s | W | SOURCE_ONLY | source_claim | ;  |
| holding | 20 | — | unknown | Active power ramp rate (startup) | Powerstartslope | register value; /10 | 0.1% | W | SOURCE_ONLY | source_claim | ;  |
| holding | 21 | — | unknown | Active power ramp rate (restart) | Powerrestartslope | register value; /10 | 0.1% | W | SOURCE_ONLY | source_claim | ;  |
| holding | 22 | — | unknown | Modbus RTU baud rate | Select communicationbaudrat e 0:9600bps 1:38400bps | register value | — | W | SOURCE_ONLY | source_claim | ;  |
| holding | 23 | — | unknown | Serial Number | The Home Assistant integration exposes this as the device serial number and reuses it as the unique identifier. | serial_number; /10 | ASCII | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| holding | 24 | — | unknown | Serial Number | The Home Assistant integration exposes this as the device serial number and reuses it as the unique identifier. | register value | ASCII | R | SOURCE_ONLY | source_claim | ;  |
| holding | 25 | — | unknown | Serial Number | The Home Assistant integration exposes this as the device serial number and reuses it as the unique identifier. | register value | ASCII | R | SOURCE_ONLY | source_claim | ;  |
| holding | 26 | — | unknown | Serial Number | The Home Assistant integration exposes this as the device serial number and reuses it as the unique identifier. | register value | ASCII | R | SOURCE_ONLY | source_claim | ;  |
| holding | 27 | — | unknown | Serial Number | The Home Assistant integration exposes this as the device serial number and reuses it as the unique identifier. | register value | ASCII | R | SOURCE_ONLY | source_claim | ;  |
| holding | 28 | — | unknown | Inverter Model | Home Assistant renders this value as the string A# B# D# T# P# U# M# S# via the integration's model() helper. Vendor spec lists value pattern `&*5`; digits appear to be stored without the leading letter codes, so treat as encoded tokens until verified on hardware. | register value; /10 | — | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| holding | 29 | — | unknown | Inverter Model | Home Assistant renders this value as the string A# B# D# T# P# U# M# S# via the integration's model() helper. Vendor spec lists value pattern `&*5`; digits appear to be stored without the leading letter codes, so treat as encoded tokens until verified on hardware. | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| holding | 30 | — | unknown | Modbus slave address | Communicate address | register value | — | W | SOURCE_ONLY | source_claim | ;  |
| holding | 31 | — | unknown | Firmware update trigger | Updatefirmware | register value | — | W | SOURCE_ONLY | source_claim | ;  |
| holding | 32 | — | unknown | Reset user configuration | Use with caution; the inverter immediately reboots and loses provisioning data. | register value | — | W | SOURCE_ONLY | source_claim | ;  |
| holding | 33 | — | unknown | Factory reset | Equivalent to the front-panel factory reset. Requires re-commissioning afterwards. | register value | — | W | SOURCE_ONLY | source_claim | ;  |
| holding | 34 | — | unknown | Manufacturer information string | The original table lists these words as Manufacturer Info 8-1 (high/middle/low); combine them to read the full string. | register value | ASCII | R | SOURCE_ONLY | source_claim | ;  |
| holding | 35 | — | unknown | Manufacturer information string | The original table lists these words as Manufacturer Info 8-1 (high/middle/low); combine them to read the full string. | register value | ASCII | R | SOURCE_ONLY | source_claim | ;  |
| holding | 36 | — | unknown | Manufacturer information string | The original table lists these words as Manufacturer Info 8-1 (high/middle/low); combine them to read the full string. | register value | ASCII | R | SOURCE_ONLY | source_claim | ;  |
| holding | 37 | — | unknown | Manufacturer information string | The original table lists these words as Manufacturer Info 8-1 (high/middle/low); combine them to read the full string. | register value | ASCII | R | SOURCE_ONLY | source_claim | ;  |
| holding | 38 | — | unknown | Manufacturer information string | The original table lists these words as Manufacturer Info 8-1 (high/middle/low); combine them to read the full string. | register value | ASCII | R | SOURCE_ONLY | source_claim | ;  |
| holding | 39 | — | unknown | Manufacturer information string | The original table lists these words as Manufacturer Info 8-1 (high/middle/low); combine them to read the full string. | register value | ASCII | R | SOURCE_ONLY | source_claim | ;  |
| holding | 40 | — | unknown | Manufacturer information string | The original table lists these words as Manufacturer Info 8-1 (high/middle/low); combine them to read the full string. | register value | ASCII | R | SOURCE_ONLY | source_claim | ;  |
| holding | 41 | — | unknown | Manufacturer information string | The original table lists these words as Manufacturer Info 8-1 (high/middle/low); combine them to read the full string. | register value | ASCII | R | SOURCE_ONLY | source_claim | ;  |
| holding | 42 | — | unknown | G100 failsafe enable | EnglishG100failsafeset | register value | — | W | SOURCE_ONLY | source_claim | ;  |
| holding | 43 | — | unknown | Device Type Code | Vendor spec provides value pattern `&*6`; handle as encoded type/family digits with implied prefixes pending confirmation. | register value; /10 | — | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| holding | 44 | — | unknown | Number Of Trackers And Phases | Inputtrackernumand outputphasenum | register value; /10 | — | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| holding | 45 | — | unknown | System clock year | Localtime | register value | — | W | SOURCE_ONLY | source_claim | ;  |
| holding | 46 | — | unknown | System clock month | Systemtime-Month | register value | — | W | SOURCE_ONLY | source_claim | ;  |
| holding | 47 | — | unknown | System clock day | Systemtime-Day | register value | — | W | SOURCE_ONLY | source_claim | ;  |
| holding | 48 | — | unknown | System clock hour | Systemtime-Hour | register value | — | W | SOURCE_ONLY | source_claim | ;  |
| holding | 49 | — | unknown | System clock minute | Systemtime-Min | register value | — | W | SOURCE_ONLY | source_claim | ;  |
| holding | 50 | — | unknown | System clock second | Systemtime-Second | register value | — | W | SOURCE_ONLY | source_claim | ;  |
| holding | 51 | — | unknown | System clock weekday | SystemWeekly | register value | — | W | SOURCE_ONLY | source_claim | ;  |
| holding | 52 | — | unknown | Stage 1 undervoltage limit | Gridvoltagelowlimit protect | register value | 0.1V | W | SOURCE_ONLY | source_claim | ;  |
| holding | 53 | — | unknown | Stage 1 overvoltage limit | Gridvoltagehighlimit protect | register value | 0.1V | W | SOURCE_ONLY | source_claim | ;  |
| holding | 54 | — | unknown | Stage 1 underfrequency limit | Gridfrequencylow limitprotect | register value | 0.01 Hz | W | SOURCE_ONLY | source_claim | ;  |
| holding | 55 | — | unknown | Stage 1 overfrequency limit | Gridhigh frequencylimitprotect | register value | 0.01 Hz | W | SOURCE_ONLY | source_claim | ;  |
| holding | 56 | — | unknown | Stage 2 undervoltage limit | Gridvoltagelowlimit protect2 | register value | 0.1V | W | SOURCE_ONLY | source_claim | ;  |
| holding | 57 | — | unknown | Stage 2 overvoltage limit | Gridvoltagehighlimit protect2 | register value | 0.1V | W | SOURCE_ONLY | source_claim | ;  |
| holding | 58 | — | unknown | Stage 2 underfrequency limit | Gridfrequencylow limitprotect2 | register value | 0.01 Hz | W | SOURCE_ONLY | source_claim | ;  |
| holding | 59 | — | unknown | Stage 2 overfrequency limit | Gridhighfrequency limitprotect2 | register value | 0.01 Hz | W | SOURCE_ONLY | source_claim | ;  |
| holding | 60 | — | unknown | Stage 3 undervoltage limit | Grid voltage low limit protect3 | register value | 0.1V | W | SOURCE_ONLY | source_claim | ;  |
| holding | 61 | — | unknown | Stage 3 overvoltage limit | Grid voltage high limit protect3 | register value | 0.1V | W | SOURCE_ONLY | source_claim | ;  |
| holding | 62 | grid_frequency | alternate | Stage 3 underfrequency limit | Grid frequency low limitprotect3 | register value | 0.01Hz | W | SOURCE_ONLY | source_claim | ; alternates: register:storage_spa:holding:63, register:storage_spa:holding:72, register:storage_spa:holding:73, register:storage_spa:holding:74, register:storage_spa:holding:75, register:storage_spa:holding:78, register:storage_spa:holding:79 |
| holding | 63 | grid_frequency | alternate | Stage 3 overfrequency limit | Grid frequency high limitprotect3 | register value | 0.01Hz | W | SOURCE_ONLY | source_claim | ; alternates: register:storage_spa:holding:62, register:storage_spa:holding:72, register:storage_spa:holding:73, register:storage_spa:holding:74, register:storage_spa:holding:75, register:storage_spa:holding:78, register:storage_spa:holding:79 |
| holding | 64 | — | unknown | Reconnect undervoltage limit | Gridlowvoltagelimit connecttoGrid | register value | 0.1V | W | SOURCE_ONLY | source_claim | ;  |
| holding | 65 | — | unknown | Reconnect overvoltage limit | Gridhighvoltagelimit connecttoGrid | register value | 0.1V | W | SOURCE_ONLY | source_claim | ;  |
| holding | 66 | — | unknown | Reconnect underfrequency limit | Gridlowfrequency | register value | 0.01 | W | SOURCE_ONLY | source_claim | ;  |
| holding | 67 | — | unknown | Reconnect overfrequency limit | Gridhighfrequency limitconnecttoGrid | register value | 0.01 Hz | W | SOURCE_ONLY | source_claim | ;  |
| holding | 68 | — | unknown | Stage 1 undervoltage trip delay | Grid voltage low limit protecttime 1 | register value | Cycle | W | SOURCE_ONLY | source_claim | ;  |
| holding | 69 | — | unknown | Stage 1 overvoltage trip delay | Grid voltage high limit protecttime 1 | register value | Cycle | W | SOURCE_ONLY | source_claim | ;  |
| holding | 70 | — | unknown | Stage 2 undervoltage trip delay | Grid voltage low limit protecttime 2 | register value | Cycle | W | SOURCE_ONLY | source_claim | ;  |
| holding | 71 | — | unknown | Stage 2 overvoltage trip delay | Grid voltage high limit protecttime 2 | register value | Cycle | W | SOURCE_ONLY | source_claim | ;  |
| holding | 72 | grid_frequency | alternate | Stage 1 underfrequency trip delay | Grid frequency low limitprotecttime 1 | register value | Cycle | W | SOURCE_ONLY | source_claim | ; alternates: register:storage_spa:holding:62, register:storage_spa:holding:63, register:storage_spa:holding:73, register:storage_spa:holding:74, register:storage_spa:holding:75, register:storage_spa:holding:78, register:storage_spa:holding:79 |
| holding | 73 | grid_frequency | alternate | Modbus Version | Grid frequency high limitprotecttime 1 | register value | Cycle | W | SOURCE_ONLY | source_claim | ; alternates: register:storage_spa:holding:62, register:storage_spa:holding:63, register:storage_spa:holding:72, register:storage_spa:holding:74, register:storage_spa:holding:75, register:storage_spa:holding:78, register:storage_spa:holding:79 |
| holding | 74 | grid_frequency | alternate | Stage 2 underfrequency trip delay | Grid frequency low limitprotecttime 2 | register value | Cycle | W | SOURCE_ONLY | source_claim | ; alternates: register:storage_spa:holding:62, register:storage_spa:holding:63, register:storage_spa:holding:72, register:storage_spa:holding:73, register:storage_spa:holding:75, register:storage_spa:holding:78, register:storage_spa:holding:79 |
| holding | 75 | grid_frequency | alternate | Stage 2 overfrequency trip delay | Grid frequency high limitprotecttime 2 | register value | Cycle | W | SOURCE_ONLY | source_claim | ; alternates: register:storage_spa:holding:62, register:storage_spa:holding:63, register:storage_spa:holding:72, register:storage_spa:holding:73, register:storage_spa:holding:74, register:storage_spa:holding:78, register:storage_spa:holding:79 |
| holding | 76 | — | unknown | Stage 3 undervoltage trip delay | Grid voltage low limit protecttime 3 | register value | Cycle | W | SOURCE_ONLY | source_claim | ;  |
| holding | 77 | — | unknown | Stage 3 overvoltage trip delay | Grid voltage high limit protecttime 3 | register value | Cycle | W | SOURCE_ONLY | source_claim | ;  |
| holding | 78 | grid_frequency | alternate | Stage 3 underfrequency trip delay | Grid frequency low limitprotecttime 3 | register value | Cycle | W | SOURCE_ONLY | source_claim | ; alternates: register:storage_spa:holding:62, register:storage_spa:holding:63, register:storage_spa:holding:72, register:storage_spa:holding:73, register:storage_spa:holding:74, register:storage_spa:holding:75, register:storage_spa:holding:79 |
| holding | 79 | grid_frequency | alternate | Stage 3 overfrequency trip delay | Grid frequency high limitprotecttime 3 | register value | Cycle | W | SOURCE_ONLY | source_claim | ; alternates: register:storage_spa:holding:62, register:storage_spa:holding:63, register:storage_spa:holding:72, register:storage_spa:holding:73, register:storage_spa:holding:74, register:storage_spa:holding:75, register:storage_spa:holding:78 |
| holding | 80 | — | unknown | Ten-minute overvoltage limit | Voltprotectionfor10 min | register value | 0.1V | W | SOURCE_ONLY | source_claim | ;  |
| holding | 81 | — | unknown | PV input high-voltage fault | PVVoltageHigh Fault | register value | 0.1V | W | SOURCE_ONLY | source_claim | ;  |
| holding | 82 | — | unknown | Controller firmware build string | Positions: 0-1 model letters, 2-3 model variant, 4-5 DSP1 build, 6-7 DSP2/M0 build, 8-9 CPLD/AFCI build, 10-11 M3 build. | register value | ASCII | R | SOURCE_ONLY | source_claim | ;  |
| holding | 83 | — | unknown | Controller firmware build string | Positions: 0-1 model letters, 2-3 model variant, 4-5 DSP1 build, 6-7 DSP2/M0 build, 8-9 CPLD/AFCI build, 10-11 M3 build. | register value | ASCII | R | SOURCE_ONLY | source_claim | ;  |
| holding | 84 | — | unknown | Controller firmware build string | Positions: 0-1 model letters, 2-3 model variant, 4-5 DSP1 build, 6-7 DSP2/M0 build, 8-9 CPLD/AFCI build, 10-11 M3 build. | register value | ASCII | R | SOURCE_ONLY | source_claim | ;  |
| holding | 85 | — | unknown | Controller firmware build string | Positions: 0-1 model letters, 2-3 model variant, 4-5 DSP1 build, 6-7 DSP2/M0 build, 8-9 CPLD/AFCI build, 10-11 M3 build. | register value | ASCII | R | SOURCE_ONLY | source_claim | ;  |
| holding | 86 | — | unknown | Controller firmware build string | Positions: 0-1 model letters, 2-3 model variant, 4-5 DSP1 build, 6-7 DSP2/M0 build, 8-9 CPLD/AFCI build, 10-11 M3 build. | register value | ASCII | R | SOURCE_ONLY | source_claim | ;  |
| holding | 87 | — | unknown | Controller firmware build string | Positions: 0-1 model letters, 2-3 model variant, 4-5 DSP1 build, 6-7 DSP2/M0 build, 8-9 CPLD/AFCI build, 10-11 M3 build. | register value | ASCII | R | SOURCE_ONLY | source_claim | ;  |
| holding | 88 | — | unknown | Modbus Version | ModbusVersion | register value; /100 | Int(16 bits) | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| holding | 89 | — | unknown | Power-factor control mode | 0=Unity PF, 1=Fixed PF setpoint, 2=Default PF line, 3=User-defined PF line, 4=Under-excited reactive power, 5=Over-excited reactive power, 6=Q(V) curve, 7=Direct control, 8=Static capacitive QV, 9=Static inductive QV. | register value | — | W | SOURCE_ONLY | source_claim | ;  |
| holding | 90 | — | unknown | GPRS modem IP/status flags | Bit 0-3: 0=idle, 1=IP read requested, 2=set IP succeeded; Bit 4-7: 0=unknown, 1=modem OK, 2=no SIM, 3=no network, 4=TCP connect fail, 5=TCP connected, etc. | register value | — | W | UNKNOWN_RESERVED | source_claim | ;  |
| holding | 91 | — | unknown | Frequency derating start | Frequencyderating startpoint | register value | 0.01H Z | W | SOURCE_ONLY | source_claim | ;  |
| holding | 92 | — | unknown | Frequency derating slope | Frequency–loadlimit rate | register value | 10tim es | W | SOURCE_ONLY | source_claim | ;  |
| holding | 93 | — | unknown | CEI 0-21 Q(V) point V1S | CEI021V1SQ(v) | register value | 0.1V | W | SOURCE_ONLY | source_claim | ;  |
| holding | 94 | — | unknown | CEI 0-21 Q(V) point V2S | CEI021V2SQ(v) | register value | 0.1V | W | SOURCE_ONLY | source_claim | ;  |
| holding | 95 | — | unknown | CEI 0-21 Q(V) point V1L | CEI021V1LQ(v) | register value | 0.1V | W | SOURCE_ONLY | source_claim | ;  |
| holding | 96 | — | unknown | CEI 0-21 Q(V) point V2L | CEI021V2LQ(v) | register value | 0.1V | W | SOURCE_ONLY | source_claim | ;  |
| holding | 97 | — | unknown | Q(V) lock-in active power | Q(v)lockinactive powerofCEI021 | register value | Percen t | W | SOURCE_ONLY | source_claim | ;  |
| holding | 98 | — | unknown | Q(V) lock-out active power | Q(v)lockOutactive powerofCEI021 | register value | Percen t | W | SOURCE_ONLY | source_claim | ;  |
| holding | 99 | — | unknown | Power-factor curve lock-in voltage | Lockingirdvoltof CEI021PFline | register value | 0.1V | W | SOURCE_ONLY | source_claim | ;  |
| holding | 100 | — | unknown | Power-factor curve lock-out voltage | Lockoutgirdvoltof CEI021PFline | register value | 0.1V | W | SOURCE_ONLY | source_claim | ;  |
| holding | 101 | — | unknown | Power-factor adjust value 1 | PFadjustvalue1 | register value | — | W | SOURCE_ONLY | source_claim | ;  |
| holding | 102 | — | unknown | Power-factor adjust value 2 | PFadjustvalue2 | register value | — | W | SOURCE_ONLY | source_claim | ;  |
| holding | 103 | — | unknown | Power-factor adjust value 3 | PFadjustvalue3 | register value | — | W | SOURCE_ONLY | source_claim | ;  |
| holding | 104 | — | unknown | Power-factor adjust value 4 | PFadjustvalue4 | register value | — | W | SOURCE_ONLY | source_claim | ;  |
| holding | 105 | — | unknown | Power-factor adjust value 5 | PFadjustvalue5 | register value | — | W | SOURCE_ONLY | source_claim | ;  |
| holding | 106 | — | unknown | Power-factor adjust value 6 | PFadjustvalue6 | register value | — | W | SOURCE_ONLY | source_claim | ;  |
| holding | 107 | — | unknown | Q(V) response delay | QV Reactive Power delaytime | register value | 1S | W | SOURCE_ONLY | source_claim | ;  |
| holding | 108 | — | unknown | Over-frequency derating delay | Overfrequency derati ngdelaytime | register value | 50ms | W | SOURCE_ONLY | source_claim | ;  |
| holding | 109 | — | unknown | Maximum reactive power magnitude | QmaxforQ(V)curve | register value | 0.1% | W | SOURCE_ONLY | source_claim | ;  |
| holding | 110 | — | unknown | PF curve point 1 load | 255meansnothispoint | register value | percen t | W | SOURCE_ONLY | source_claim | ;  |
| holding | 111 | — | unknown | PF curve point 1 target | PFlimitlinepoint1 powerfactor | register value | — | W | SOURCE_ONLY | source_claim | ;  |
| holding | 112 | — | unknown | PF curve point 2 load | 255meansnothispoint | register value | percen t | W | SOURCE_ONLY | source_claim | ;  |
| holding | 113 | — | unknown | PF curve point 2 target | PFlimitlinepoint 2powerfactor | register value | — | W | SOURCE_ONLY | source_claim | ;  |
| holding | 114 | — | unknown | PF curve point 3 load | 255meansnothispoint | register value | percen t | W | SOURCE_ONLY | source_claim | ;  |
| holding | 115 | — | unknown | PF curve point 3 target | PFlimitlinepoint3 powerfactor | register value | — | W | SOURCE_ONLY | source_claim | ;  |
| holding | 116 | — | unknown | PF curve point 4 load | 255meansnothispoint | register value | percen t | W | SOURCE_ONLY | source_claim | ;  |
| holding | 117 | — | unknown | PF curve point 4 target | PFlimitlinepoint4 powerfactor | register value | — | W | SOURCE_ONLY | source_claim | ;  |
| holding | 118 | — | unknown | Module code segments | SxxBxx | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| holding | 119 | — | unknown | Module code segments | DxxTxx | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| holding | 120 | — | unknown | Module code segments | PxxUxx | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| holding | 121 | — | unknown | Module code segments | Mxxxx Power | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| holding | 122 | — | unknown | Export limit enable mode | ExportLimitenable, 0:DisableexportLimit; 1:Enable485exportLimit; 2:Enable232exportLimit; 3:EnableCTexportLimit; | register value | — | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 123 | — | unknown | Export limit power setpoint | ExportLimitPowerRate | register value | 0.1% | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 124 | — | unknown | Tracker coupling mode | 0:Independent 1:DCSource 2:Parallel | register value | — | W | SOURCE_ONLY | source_claim | ;  |
| holding | 1000 | — | unknown | Float charge current limit i | Float charge current limit i | register value | — | W | SOURCE_ONLY | source_claim | ;  |
| holding | 1001 | — | unknown | PF CMD memory state | PF CMD memory state | register value | 0or1, | W | SOURCE_ONLY | source_claim | ;  |
| holding | 1002 | — | unknown | VbatStartF orDischarg e | VbatStartF orDischarg e | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| holding | 1003 | — | unknown | VbatlowWa rnClr l | VbatlowWa rnClr l | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| holding | 1004 | — | unknown | Vbatstopfo rdischarge | Vbatstopfo rdischarge | register value | — | W | SOURCE_ONLY | source_claim | ;  |
| holding | 1005 | — | unknown | Vbat stop forcharge | Shouldstopcharge whenhigherthanthis voltage | register value | 0.01V | W | SOURCE_ONLY | source_claim | ;  |
| holding | 1006 | — | unknown | Vbat start for discharge | Should not discharge when lower than this voltage | register value | 0.01V | W | SOURCE_ONLY | source_claim | ;  |
| holding | 1007 | — | unknown | Vbat constant charge | CVvoltage（acid） | register value | 0.01V | W | SOURCE_ONLY | source_claim | ;  |
| holding | 1008 | — | unknown | EESysInfo.S ysSetEn | SystemEnable | register value | — | W | SOURCE_ONLY | source_claim | ;  |
| holding | 1009 | — | unknown | Battemp lower limit d | Batterytemperature lowerlimitfordischarge | register value | 0.1℃ | W | SOURCE_ONLY | source_claim | ;  |
| holding | 1010 | — | unknown | Bat temp upper limit d | Batterytemperature upperlimitfordischarge | register value | 0.1℃ | W | SOURCE_ONLY | source_claim | ;  |
| holding | 1011 | — | unknown | Bat temp lower limit c | Lowertemperaturelimit | register value | 0.1℃ | W | SOURCE_ONLY | source_claim | ;  |
| holding | 1012 | — | unknown | Bat temp upper limit c | Uppertemperaturelimit | register value | 0.1℃ | W | SOURCE_ONLY | source_claim | ;  |
| holding | 1013 | — | unknown | uwUnderFr eDischarge DelyTime | UnderFreDelayTime | register value | 50ms | R | SOURCE_ONLY | source_claim | ;  |
| holding | 1014 | — | unknown | BatMdlSeri alNum | SPH4-11Kused | register value | — | W | SOURCE_ONLY | source_claim | ;  |
| holding | 1015 | — | unknown | BatMdlPara llNum | SPH4-11Kused | register value | — | W | SOURCE_ONLY | source_claim | ;  |
| holding | 1016 | — | unknown | DRMS_EN | 0：disable 1：enable | register value | / | R | SOURCE_ONLY | source_claim | ;  |
| holding | 1017 | — | unknown | Bat First Start Time 4 | Higheight:hours Loweight:minutes | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| holding | 1018 | — | unknown | Bat First Stop Time 4 | Higheight:hours Loweight:minutes | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| holding | 1019 | — | unknown | BatFirst on/off Switch4 | Batterypriorityenable1 | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| holding | 1020 | — | unknown | Bat First Start Time 5 | Higheight:hours Loweight:minutes | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| holding | 1021 | — | unknown | BatFirst StopTime 5 | Higheight:hours Loweight:minutes | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| holding | 1022 | — | unknown | BatFirst on/off Switch5 | Batterypriorityenable1 | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| holding | 1023 | — | unknown | BatFirst StartTime 6 | Higheight:hours Loweight:minutes | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| holding | 1024 | — | unknown | BatFirst StopTime 6 | Higheight:hours Loweight:minutes | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| holding | 1025 | — | unknown | BatFirst on/off Switch6 | Batterypriorityenable1 | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| holding | 1026 | — | unknown | GridFirst StartTime | Higheight:hours Loweight:minutes | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| holding | 1027 | — | unknown | GridFirst StopTime 4 | Higheight:hours Loweight:minutes | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| holding | 1028 | — | unknown | Grid First Stop Switch4 | Gridpriorityenable | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| holding | 1029 | — | unknown | GridFirst StartTime 5 | Higheight:hours Loweight:minutes | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| holding | 1030 | — | unknown | GridFirst StopTime 5 | Higheight:hours Loweight:minutes | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| holding | 1031 | — | unknown | Grid First Stop Switch5 | Gridpriorityenable | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| holding | 1032 | — | unknown | GridFirst StartTime 6 | Higheight:hours Loweight:minutes | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| holding | 1033 | — | unknown | GridFirst StopTime 6 | Higheight:hours Loweight:minutes | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| holding | 1034 | — | unknown | Grid First Stop Switch6 | Gridpriorityenable | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| holding | 1035 | — | unknown | BatFirst StartTime 4 | Higheight:hours Loweight:minutes | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| holding | 1036 | — | unknown | / | Reserve | register value | / | R | SOURCE_ONLY | source_claim | ;  |
| holding | 1037 | — | unknown | bCTMode | UsetheCTModeto ChooseRFCT\Cable CT\METER | register value | — | W | SOURCE_ONLY | source_claim | ;  |
| holding | 1038 | — | unknown | CTAdjust | CTAdjustenable | register value | — | W | SOURCE_ONLY | source_claim | ;  |
| holding | 1039 | — | unknown | / | Reserve | register value | / | R | SOURCE_ONLY | source_claim | ;  |
| holding | 1040 | — | unknown | / | / | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| holding | 1041 | — | unknown | / | / | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| holding | 1042 | — | unknown | / | / | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| holding | 1043 | — | unknown | / | / | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| holding | 1044 | — | unknown | Priority | ForceChrEn/ForceDischr En Load first/bat first /grid first | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| holding | 1045 | — | unknown | / | / | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| holding | 1046 | — | unknown | / | / | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| holding | 1047 | — | unknown | AgingTestSt ep Cmd | Commandforagingtest | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| holding | 1048 | — | unknown | BatteryTyp e | Batterytypechooseof buck-boostinput | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| holding | 1049 | — | unknown | / | / | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| holding | 1050 | — | unknown | / | / | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| holding | 1051 | — | unknown | / | / | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| holding | 1052 | — | unknown | / | / | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| holding | 1053 | — | unknown | / | / | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| holding | 1054 | — | unknown | / | / | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| holding | 1055 | — | unknown | Register 1055 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| holding | 1056 | — | unknown | Register 1056 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| holding | 1057 | — | unknown | Register 1057 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| holding | 1058 | — | unknown | Register 1058 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| holding | 1059 | — | unknown | Register 1059 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| holding | 1060 | — | unknown | BuckUpsFunE n | 0:disable 1:enable | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| holding | 1061 | — | unknown | BuckUPSVoltS et | UPSoutputvoltage | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| holding | 1062 | — | unknown | UPSFreqSet | UPSoutputfrequency | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| holding | 1063 | — | unknown | Register 1063 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| holding | 1064 | — | unknown | Register 1064 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| holding | 1065 | — | unknown | Register 1065 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| holding | 1066 | — | unknown | Register 1066 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| holding | 1067 | — | unknown | Register 1067 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| holding | 1068 | — | unknown | Register 1068 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| holding | 1069 | — | unknown | Register 1069 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| holding | 1070 | grid_first_discharge_rate | supported | Grid-first discharge limit | Discharge Power Rate whenGridFirst | register value | 1% | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 1071 | grid_first_stop_soc | supported | Grid-first stop SOC | Stop Discharge soc when GridFirst | register value | 1% | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 1072 | — | unknown | / | / | register value | / | R | SOURCE_ONLY | source_claim | ;  |
| holding | 1073 | — | unknown | / | / | register value | / | R | SOURCE_ONLY | source_claim | ;  |
| holding | 1074 | — | unknown | / | / | register value | / | R | SOURCE_ONLY | source_claim | ;  |
| holding | 1075 | — | unknown | / | / | register value | / | R | SOURCE_ONLY | source_claim | ;  |
| holding | 1076 | — | unknown | / | / | register value | / | R | SOURCE_ONLY | source_claim | ;  |
| holding | 1077 | — | unknown | / | / | register value | / | R | SOURCE_ONLY | source_claim | ;  |
| holding | 1078 | — | unknown | / | / | register value | / | R | SOURCE_ONLY | source_claim | ;  |
| holding | 1079 | — | unknown | / | / | register value | / | R | SOURCE_ONLY | source_claim | ;  |
| holding | 1080 | — | unknown | Grid-first slot 1 start | High byte = hour (0-23); low byte = minute (0-59). | register value | hh:mm | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 1081 | — | unknown | Grid-first slot 1 stop | High byte = hour (0-23); low byte = minute (0-59). | register value | hh:mm | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 1082 | — | unknown | Grid-first slot 1 enable | Enable:1 Disable:0 | register value | — | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 1083 | — | unknown | Grid-first slot 2 start | High byte = hour (0-23); low byte = minute (0-59). | register value | hh:mm | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 1084 | — | unknown | Grid-first slot 2 stop | High byte = hour (0-23); low byte = minute (0-59). | register value | hh:mm | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 1085 | — | unknown | Grid-first slot 2 enable | When set from the LCD, this slot can be tied to the Force Discharge command. | register value | — | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 1086 | — | unknown | Grid-first slot 3 start | High byte = hour (0-23); low byte = minute (0-59). | register value | hh:mm | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 1087 | — | unknown | Grid-first slot 3 stop | High byte = hour (0-23); low byte = minute (0-59). | register value | hh:mm | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 1088 | — | unknown | Grid-first slot 3 enable | Enable:1 Disable:0 | register value | — | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 1089 | — | unknown | / | / | register value | / | R | SOURCE_ONLY | source_claim | ;  |
| holding | 1090 | battery_first_charge_rate | supported | Battery-first charge limit | Charge Power Rate when BatFirst | register value | 1% | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 1091 | battery_first_stop_soc | supported | Battery-first stop SOC | Stop Charge soc when Bat First | register value | 1% | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 1092 | — | unknown | Battery-first AC charge enable | WhenBatFirst Enable:1 Disable:0 | register value | — | R/W | RESOLVED | semantic_correlated, source_claim | ;  |
| holding | 1093 | — | unknown | Register 1093 | — | register value | — | R | UNKNOWN_RESERVED | source_claim | ;  |
| holding | 1094 | — | unknown | Register 1094 | — | register value | — | R | UNKNOWN_RESERVED | source_claim | ;  |
| holding | 1095 | — | unknown | Register 1095 | — | register value | — | R | UNKNOWN_RESERVED | source_claim | ;  |
| holding | 1096 | — | unknown | Register 1096 | — | register value | — | R | UNKNOWN_RESERVED | source_claim | ;  |
| holding | 1097 | — | unknown | Register 1097 | — | register value | — | R | UNKNOWN_RESERVED | source_claim | ;  |
| holding | 1098 | — | unknown | Register 1098 | — | register value | — | R | UNKNOWN_RESERVED | source_claim | ;  |
| holding | 1099 | — | unknown | Register 1099 | — | register value | — | R | UNKNOWN_RESERVED | source_claim | ;  |
| holding | 1100 | — | unknown | Battery-first slot 1 start | High byte = hour (0-23); low byte = minute (0-59). | register value | hh:mm | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 1101 | — | unknown | Battery-first slot 1 stop | High byte = hour (0-23); low byte = minute (0-59). | register value | hh:mm | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 1102 | — | unknown | Battery-first slot 1 enable | Enable:1 Disable:0 | register value | — | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 1103 | — | unknown | Battery-first slot 2 start | High byte = hour (0-23); low byte = minute (0-59). | register value | hh:mm | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 1104 | — | unknown | Battery-first slot 2 stop | High byte = hour (0-23); low byte = minute (0-59). | register value | hh:mm | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 1105 | — | unknown | Battery-first slot 2 enable | Enable:1 Disable:0 | register value | — | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 1106 | — | unknown | Battery-first slot 3 start | High byte = hour (0-23); low byte = minute (0-59). | register value | hh:mm | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 1107 | — | unknown | Battery-first slot 3 stop | High byte = hour (0-23); low byte = minute (0-59). | register value | hh:mm | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 1108 | — | unknown | Battery-first slot 3 enable | Enable:1 Disable:0 | register value | — | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 1109 | — | unknown | / | reserve | register value | / | R | SOURCE_ONLY | source_claim | ;  |
| holding | 1110 | — | unknown | Load-first slot 1 start | SPA/reserve | register value | hh:mm | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 1111 | — | unknown | Load-first slot 1 stop | SPA/reserve | register value | hh:mm | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 1112 | — | unknown | Load-first slot 1 enable | SPA/reserve | register value | — | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 1113 | — | unknown | Load-first slot 2 start | SPA/reserve | register value | hh:mm | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 1114 | — | unknown | Load-first slot 2 stop | SPA/reserve | register value | hh:mm | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 1115 | — | unknown | Load-first slot 2 enable | SPA/reserve | register value | — | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 1116 | — | unknown | Load-first slot 3 start | SPA/reserve | register value | hh:mm | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 1117 | — | unknown | Load-first slot 3 stop | SPA/reserve | register value | hh:mm | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 1118 | — | unknown | Load-first slot 3 enable | SPA/reserve | register value | — | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 1119 | — | unknown | Energy calculation formula | 0：Theoldformula 1 ： The new formula | register value | / | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 1120 | — | unknown | Backup enable | MIXUS | register value | — | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 1121 | — | unknown | SGIP enable | MIXUS | register value | — | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 1122 | — | unknown | Register 1122 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| holding | 1123 | — | unknown | Register 1123 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| holding | 1124 | — | unknown | Register 1124 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| input | 1000 | — | unknown | uwSysWorkMode | uwSysWorkMode | register value | — | W | SOURCE_ONLY | source_claim | ;  |
| input | 1001 | — | unknown | Systemfaultword0 | Systemfaultword0 | register value | Please refer to thefault description of Hybrid | R | SOURCE_ONLY | source_claim | ;  |
| input | 1002 | — | unknown | Systemfaultword1 | Systemfaultword1 | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 1003 | — | unknown | Systemfaultword2 | Systemfaultword2 | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 1004 | — | unknown | Systemfaultword3 | Systemfaultword3 | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 1005 | — | unknown | Systemfaultword4 | Systemfaultword4 | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 1006 | — | unknown | Systemfaultword5 | Systemfaultword5 | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 1007 | — | unknown | Systemfaultword6 | Systemfaultword6 | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 1008 | — | unknown | Systemfaultword7 | Systemfaultword7 | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 1009 | battery_discharge_power | supported | Pdischarge1H | Dischargepower(high) | register value; /10 | W | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 1010 | — | unknown | Pdischarge1L | Dischargepower(low) | register value; /10 | W | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 1011 | battery_charge_power | supported | Pcharge1H | Chargepower(high) | register value; /10 | W | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 1012 | — | unknown | Pcharge1L | Chargepower(low) | register value; /10 | W | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 1013 | — | unknown | Vbat | Batteryvoltage | register value | V | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 1014 | battery_soc | supported | SOC | StateofchargeCapacity | register value; /10 | lith/leadacid | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 1015 | — | unknown | PactouserR H | ACpowertouserH | register value | W | R | RESOLVED | semantic_correlated, source_claim | ;  |
| input | 1016 | — | unknown | PactouserR L | ACpowertouserL | register value | W | R | RESOLVED | semantic_correlated, source_claim | ;  |
| input | 1017 | — | unknown | PactouserS H | PactouserS H | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 1018 | — | unknown | PactouserS L | PactouserS L | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 1019 | — | unknown | PactouserT H | PactouserT H | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 1020 | — | unknown | PactouserT L | PactouserT H | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 1021 | — | unknown | PactouserTotalH | ACpowertousertotalH | register value; /10 | W | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 1022 | — | unknown | PactouserTotalL | ACpowertousertotalL | register value; /10 | W | R | RESOLVED | semantic_correlated, source_claim | ;  |
| input | 1023 | — | unknown | PactogridR H | ACpowertogridH | register value | Ac output | R | RESOLVED | semantic_correlated, source_claim | ;  |
| input | 1024 | — | unknown | PactogridR L | ACpowertogridL | register value | W | R | RESOLVED | semantic_correlated, source_claim | ;  |
| input | 1025 | — | unknown | PactogridS H | PactogridS H | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 1026 | — | unknown | PactogridS L | PactogridS L | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 1027 | — | unknown | PactogridTH | 0.1w | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 1028 | — | unknown | PactogridTL | 0.1w | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 1029 | — | unknown | pac_to_grid_total | 0.1w | register value; /10 | W | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 1030 | — | unknown | PactogridtotalL | 0.1w | register value; /10 | W | R | RESOLVED | semantic_correlated, source_claim | ;  |
| input | 1031 | — | unknown | PLocalLoadR H | 0.1w | register value | W | R | RESOLVED | semantic_correlated, source_claim | ;  |
| input | 1032 | — | unknown | PLocalLoadR L | 0.1w | register value | W | R | RESOLVED | semantic_correlated, source_claim | ;  |
| input | 1033 | — | unknown | PLocalLoadS H | 0.1w | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 1034 | — | unknown | PLocalLoadS L | 0.1w | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 1035 | — | unknown | PLocalLoadT H | 0.1w | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 1036 | — | unknown | PLocalLoadT L | 0.1w | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 1037 | — | unknown | PLocalLoadtotalH | 0.1w | register value | W | R | RESOLVED | semantic_correlated, source_claim | ;  |
| input | 1038 | — | unknown | PLocalLoadtotalL | 0.1w | register value | W | R | RESOLVED | semantic_correlated, source_claim | ;  |
| input | 1039 | — | unknown | IP2MTemperature | 0.1℃ | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 1040 | — | unknown | B2attery Temperature | 0.1℃ | register value | °C | R | RESOLVED | semantic_correlated, source_claim | ;  |
| input | 1041 | — | unknown | SPDSPStatus | SPDSPStatus | register value | — | R | RESOLVED | semantic_correlated, source_claim | ;  |
| input | 1042 | — | unknown | SPBusVolt | 0.1V | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 1043 | — | unknown | Register 1043 | — | register value | — | R | UNKNOWN_RESERVED | source_claim | ;  |
| input | 1044 | — | unknown | Etouser_todayH | Etouser_todayH | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 1045 | — | unknown | Etouser_todayL | Etouser_todayL | register value; /10 | kWh | W | RESOLVED | semantic_correlated, source_claim | ;  |
| input | 1046 | — | unknown | Etouser_totalH | Etouser_totalH | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 1047 | — | unknown | Etouser_totalL | Etouser_totalL | register value; /10 | kWh | R | RESOLVED | semantic_correlated, source_claim | ;  |
| input | 1048 | — | unknown | Etogrid_todayH | Etogrid_todayH | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 1049 | — | unknown | Etogrid_todayL | Etogrid_todayL | register value; /10 | kWh | W | RESOLVED | semantic_correlated, source_claim | ;  |
| input | 1050 | — | unknown | Etogrid_totalH | Etogrid_totalH | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 1051 | — | unknown | Etogrid_totalL | Etogrid_totalL | register value; /10 | kWh | R | RESOLVED | semantic_correlated, source_claim | ;  |
| input | 1052 | — | unknown | Edischarge1_toda yH | Edischarge1_toda yH | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 1053 | — | unknown | Edischarge1_toda yL | Edischarge1_toda yL | register value; /10 | kWh | R | RESOLVED | semantic_correlated, source_claim | ;  |
| input | 1054 | — | unknown | Edischarge1_total H | Edischarge1_total H | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 1055 | — | unknown | Edischarge1_total L | Edischarge1_total L | register value; /10 | kWh | W | RESOLVED | semantic_correlated, source_claim | ;  |
| input | 1056 | — | unknown | Echarge1_todayH | Echarge1_todayH | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 1057 | — | unknown | Echarge1_today L | Echarge1_today L | register value; /10 | kWh | R | RESOLVED | semantic_correlated, source_claim | ;  |
| input | 1058 | — | unknown | Echarge1_totalH | Echarge1_totalH | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 1059 | — | unknown | Echarge1_totalL | Echarge1_totalL | register value; /10 | kWh | R | RESOLVED | semantic_correlated, source_claim | ;  |
| input | 1060 | — | unknown | Register 1060 | Localloadenergytoday | register value | kWh | R | UNKNOWN_RESERVED | semantic_correlated, source_claim | ;  |
| input | 1061 | — | unknown | Register 1061 | Localloadenergytoday | register value | kWh | R | UNKNOWN_RESERVED | semantic_correlated, source_claim | ;  |
| input | 1062 | — | unknown | Register 1062 | Localloadenergytotal | register value | kWh | R | UNKNOWN_RESERVED | semantic_correlated, source_claim | ;  |
| input | 1063 | — | unknown | Register 1063 | Localloadenergytotal | register value | kWh | R | UNKNOWN_RESERVED | semantic_correlated, source_claim | ;  |
| input | 1064 | — | unknown | Register 1064 | ExportLimitApparentPowerH | register value | — | W | UNKNOWN_RESERVED | source_claim | ;  |
| input | 1065 | — | unknown | Register 1065 | ExportLimitApparentPowerL | register value | — | W | UNKNOWN_RESERVED | source_claim | ;  |
| input | 1066 | — | unknown | Register 1066 | / | register value | — | R | UNKNOWN_RESERVED | source_claim | ;  |
| input | 1067 | — | unknown | EpsFac | UPSfrequency | register value | — | R | RESOLVED | semantic_correlated, source_claim | ;  |
| input | 1068 | — | unknown | EpsVac1 | UPSphaseRoutputvoltage | register value | — | R | RESOLVED | semantic_correlated, source_claim | ;  |
| input | 1069 | — | unknown | EpsIac1 | UPSphaseRoutputcurrent | register value | — | R | RESOLVED | semantic_correlated, source_claim | ;  |
| input | 1070 | — | unknown | EpsPac1 | UPSphaseRoutputpower(H) | register value | — | R | RESOLVED | semantic_correlated, source_claim | ;  |
| input | 1071 | — | unknown | EpsPac1 | UPSphaseRoutputpower(L) | register value | — | R | RESOLVED | semantic_correlated, source_claim | ;  |
| input | 1072 | — | unknown | EpsVac2 | UPSphaseSoutputvoltage | register value | — | R | RESOLVED | semantic_correlated, source_claim | ;  |
| input | 1073 | — | unknown | EpsIac2 | UPSphaseSoutputcurrent | register value | — | R | RESOLVED | semantic_correlated, source_claim | ;  |
| input | 1074 | — | unknown | EpsPac2 | UPSphaseSoutputpower(H) | register value | — | R | RESOLVED | semantic_correlated, source_claim | ;  |
| input | 1075 | — | unknown | EpsPac2 | UPSphaseSoutputpower(L) | register value | — | R | RESOLVED | semantic_correlated, source_claim | ;  |
| input | 1076 | — | unknown | EpsVac3 | UPSphaseToutputvoltage | register value | — | R | RESOLVED | semantic_correlated, source_claim | ;  |
| input | 1077 | — | unknown | EpsIac3 | UPSphaseToutputcurrent | register value | — | R | RESOLVED | semantic_correlated, source_claim | ;  |
| input | 1078 | — | unknown | EpsPac3 | UPSphaseToutputpower(H) | register value | — | R | RESOLVED | semantic_correlated, source_claim | ;  |
| input | 1079 | — | unknown | EpsPac3 | UPSphaseToutputpower(L) | register value | — | R | RESOLVED | semantic_correlated, source_claim | ;  |
| input | 1080 | — | unknown | EpsLoadPercent | LoadpercentofUPSouput | register value | — | R | RESOLVED | semantic_correlated, source_claim | ;  |
| input | 1081 | — | unknown | EpsPF | Powerfactor | register value | — | R | RESOLVED | semantic_correlated, source_claim | ;  |
| input | 1082 | — | unknown | Register 1082 | StatusOldfromBMS | register value | — | R | UNKNOWN_RESERVED | source_claim | ;  |
| input | 1083 | — | unknown | Register 1083 | StatusfromBMS | register value | — | R | UNKNOWN_RESERVED | source_claim | ;  |
| input | 1084 | — | unknown | Register 1084 | ErrorinfoOldfromBMS | register value | — | R | UNKNOWN_RESERVED | source_claim | ;  |
| input | 1085 | — | unknown | Register 1085 | ErrorinfomationfromBMS | register value | — | R | UNKNOWN_RESERVED | source_claim | ;  |
| input | 1086 | — | unknown | Register 1086 | SOCfromBMS | register value | — | R | UNKNOWN_RESERVED | source_claim | ;  |
| input | 1087 | — | unknown | Register 1087 | BatteryvoltagefromBMS | register value | — | R | UNKNOWN_RESERVED | source_claim | ;  |
| input | 1088 | — | unknown | Register 1088 | BatterycurrentfromBMS | register value | — | R | UNKNOWN_RESERVED | source_claim | ;  |
| input | 1089 | — | unknown | Register 1089 | BatterytemperaturefromBMS | register value | — | R | UNKNOWN_RESERVED | source_claim | ;  |
| input | 1090 | — | unknown | BMS_MaxCurr | Max. charge/discharge current fromBMS(pylon) | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 1091 | — | unknown | BMS_GaugeRM | GaugeRMfromBMS | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 1092 | — | unknown | BMS_GaugeFCC | GaugeFCCfromBMS | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 1093 | — | unknown | BMS_FW | BMS_FW | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 1094 | — | unknown | BMS_DeltaVolt | DeltaVfromBMS | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 1095 | — | unknown | BMS_CycleCnt | CycleCountfromBMS | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 1096 | — | unknown | BMS_SOH | SOHfromBMS | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 1097 | — | unknown | BMS_ConstantV olt | CVvoltagefromBMS | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 1098 | — | unknown | BMS_WarnInfoO ld | WarninginfooldfromBMS | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 1099 | — | unknown | BMS_WarnInfo | WarninginfofromBMS | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 1100 | — | unknown | BMS_GaugeICCu rr | GaugeICcurrentfromBMS | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 1101 | — | unknown | BMS_MCUVersi on | MCUSoftwareversionfromBMS | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 1102 | — | unknown | BMS_GaugeVers ion | GaugeVersionfromBMS | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 1103 | — | unknown | BMS_wGaugeFR Version_L | GaugeFRVersionL16fromBMS | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 1104 | — | unknown | BMS_wGaugeFR Version_H | GaugeFRVersionH16fromBMS | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 1105 | — | unknown | BMS_BMSInfo | BMSInformationfromBMS | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 1106 | — | unknown | BMS_PackInfo | PackInformationfromBMS | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 1107 | — | unknown | BMS_UsingCap | UsingCapfromBMS | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 1108 | — | unknown | uwMaxCellVolt | Maximumsinglebatteryvoltage | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 1109 | — | unknown | uwMinCellVolt | Lowestsinglebatteryvoltage | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 1110 | — | unknown | bModuleNum | Batteryparallelnumber | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 1111 | — | unknown | Numberofbatteries | Numberofbatteries | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 1112 | — | unknown | uwMaxVoltCellN o | MaxVoltCellNo | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 1113 | — | unknown | uwMinVoltCellN o | MinVoltCellNo | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 1114 | — | unknown | uwMaxTemprCe ll_10T | MaxTemprCell_10T | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 1115 | — | unknown | uwMinTemprCel l_10T | MinTemprCell_10T | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 1116 | — | unknown | uwMaxTemprCe llNo | MaxVoltTemprCellNo | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 1117 | — | unknown | uwMinTemprCel | MinVoltTemprCellNo | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 1118 | — | unknown | ProtectpackID | FaultyBatteryAddress | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 1119 | — | unknown | MaxSOC | ParallelmaximumSOC | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 1120 | — | unknown | MinSOC | ParallelminimumSOC | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 1121 | — | unknown | BMS_Error2 | BatteryProtection2 | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 1122 | — | unknown | BMS_Error3 | BatteryProtection3 | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 1123 | — | unknown | BMS_WarnInfo2 | BatteryWarn2 | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 1124 | — | unknown | ACCharge EnergyTodayH | ACChargeEnergytoday | register value | kWh | W | RESOLVED | semantic_correlated, source_claim | ;  |
| input | 1125 | — | unknown | ACCharge EnergyTodayL | ACChargeEnergytoday | register value | kWh | W | RESOLVED | semantic_correlated, source_claim | ;  |
| input | 1126 | — | unknown | A1CCharge EnergyTotalH | A1CCharge EnergyTotalH | register value | kWh | R | RESOLVED | semantic_correlated, source_claim | ;  |
| input | 1127 | — | unknown | ACCharge EnergyTotalL | ACCharge EnergyTotalL | register value | kWh | R | RESOLVED | semantic_correlated, source_claim | ;  |
| input | 1128 | — | unknown | AC Charge Power H | ACChargePower | register value | — | W | SOURCE_ONLY | source_claim | ;  |
| input | 1129 | — | unknown | AC Charge PowerL | ACChargePower | register value | — | W | SOURCE_ONLY | source_claim | ;  |
| input | 1130 | — | unknown | 70% INV Power adjust | uwGridPower_70_AdjEE_SP | register value | — | W | SOURCE_ONLY | source_claim | ;  |
| input | 1131 | — | unknown | Extra AC Power to grid_H | ExtrainverteACPowertogrid High | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 1132 | — | unknown | Extra AC Power to grid_L | ExtrainverteACPowertogridLow | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 1133 | — | unknown | Eextra_todayH | ExtrainverterPowerTOUser_Extra today(high) | register value | 0.1kWh | R | SOURCE_ONLY | source_claim | ;  |
| input | 1134 | — | unknown | Eextra_todayL | ExtrainverterPowerTOUser_Extra today(low) | register value | 0.1kWh | R | SOURCE_ONLY | source_claim | ;  |
| input | 1135 | — | unknown | Eextra_totalH | ExtrainverterPowerTOUser_Extra total(high) | register value | 0.1kWh | R | SOURCE_ONLY | source_claim | ;  |
| input | 1136 | — | unknown | Eextra_totalL | ExtrainverterPowerTOUser_Extra total(low) | register value | 0.1kWh | R | SOURCE_ONLY | source_claim | ;  |
| input | 1137 | — | unknown | Esystem_today H | SystemelectricenergytodayH | register value | 0.1kWh | R | SOURCE_ONLY | source_claim | ;  |
| input | 1138 | — | unknown | Esystem_ today L | SystemelectricenergytodayL | register value | SPA used System electric energytodayL | R | SOURCE_ONLY | source_claim | ;  |
| input | 1139 | — | unknown | Esystem_totalH | SystemelectricenergytotalH | register value | SPA used System electric energytotalH | R | SOURCE_ONLY | source_claim | ;  |
| input | 1140 | — | unknown | Esystem_totalL | SystemelectricenergytotalL | register value | SPA used System electric energytotalL | R | SOURCE_ONLY | source_claim | ;  |
| input | 1141 | — | unknown | Eself_todayH | selfelectricenergytodayH | register value | self electric energytodayH | R | SOURCE_ONLY | source_claim | ;  |
| input | 1142 | — | unknown | Eself_todayL | selfelectricenergytodayL | register value | self electric energytodayL | R | SOURCE_ONLY | source_claim | ;  |
| input | 1143 | — | unknown | Eself_totalH | selfelectricenergytotalH | register value | self electric energytotalH | R | SOURCE_ONLY | source_claim | ;  |
| input | 1144 | — | unknown | Eself_totalL | selfelectricenergytotalL | register value | self electric energytotalL | R | SOURCE_ONLY | source_claim | ;  |
| input | 1145 | — | unknown | PSystemH | SystempowerH | register value | SystempowerH | R | SOURCE_ONLY | source_claim | ;  |
| input | 1146 | — | unknown | PSystemL | SystempowerL | register value | SystempowerL | R | SOURCE_ONLY | source_claim | ;  |
| input | 1147 | — | unknown | PSelfH | selfpowerH | register value | selfpowerH | R | SOURCE_ONLY | source_claim | ;  |
| input | 1148 | — | unknown | PSelfL | selfpowerL | register value | selfpowerL | R | SOURCE_ONLY | source_claim | ;  |
| input | 1149 | — | unknown | EPVAll_TodayH | PVelectricenergytodayH | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 1150 | — | unknown | EPVAll_TodayL | PVelectricenergytodayL | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 1151 | — | unknown | AcDischarge PackSn | Discharge power pack serial number | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 1152 | — | unknown | Accdischarge power_H | Cumulative discharge power high 16-bitbyte | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 1153 | — | unknown | Accdischarge power_L | Cumulative discharge power low 16-bitbyte | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 1154 | — | unknown | AccCharge PackSn | chargepowerpackserialnumber | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 1155 | — | unknown | AccCharge power_H | Cumulative charge power high 16-bitbyte | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 1156 | — | unknown | AccCharge power_L | Cumulative charge power low 16-bitbyte | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 1157 | — | unknown | FirstBattFaultSn | FirstBattFaultSn | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 1158 | — | unknown | Second BattFaultSn | Second BattFaultSn | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 1159 | — | unknown | Third BattFaultSn | Third BattFaultSn | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 1160 | — | unknown | Fourth BattFaultSn | Fourth BattFaultSn | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 1161 | — | unknown | Batteryhistory faultcode1 | Batteryhistoryfaultcode1 | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 1162 | — | unknown | Batteryhistory faultcode2 | Batteryhistoryfaultcode2 | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 1163 | — | unknown | Batteryhistory faultcode3 | Batteryhistoryfaultcode3 | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 1164 | — | unknown | Batteryhistory faultcode4 | Batteryhistoryfaultcode4 | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 1165 | — | unknown | Batteryhistory faultcode5 | Batteryhistoryfaultcode5 | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 1166 | — | unknown | Batteryhistory faultcode6 | Batteryhistoryfaultcode6 | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 1167 | — | unknown | Batteryhistory faultcode7 | Batteryhistoryfaultcode7 | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 1168 | — | unknown | Batteryhistory faultcode8 | Batteryhistoryfaultcode8 | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 1169 | — | unknown | Number of battery codes | Number of battery codes PACK number + BIC forward and reversecodes | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 1170 | — | unknown | Register 1170 | — | register value | — | R | UNKNOWN_RESERVED | source_claim | ;  |
| input | 1171 | — | unknown | Register 1171 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| input | 1172 | — | unknown | Register 1172 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| input | 1173 | — | unknown | Register 1173 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| input | 1174 | — | unknown | Register 1174 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| input | 1175 | — | unknown | Register 1175 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| input | 1176 | — | unknown | Register 1176 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| input | 1177 | — | unknown | Register 1177 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| input | 1178 | — | unknown | Register 1178 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| input | 1179 | — | unknown | Register 1179 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| input | 1180 | — | unknown | Register 1180 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| input | 1181 | — | unknown | Register 1181 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| input | 1182 | — | unknown | Register 1182 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| input | 1183 | — | unknown | Register 1183 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| input | 1184 | — | unknown | Register 1184 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| input | 1185 | — | unknown | Register 1185 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| input | 1186 | — | unknown | Register 1186 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| input | 1187 | — | unknown | Register 1187 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| input | 1188 | — | unknown | Register 1188 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| input | 1189 | — | unknown | Register 1189 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| input | 1190 | — | unknown | Register 1190 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| input | 1191 | — | unknown | Register 1191 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| input | 1192 | — | unknown | Register 1192 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| input | 1193 | — | unknown | Register 1193 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| input | 1194 | — | unknown | Register 1194 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| input | 1195 | — | unknown | Register 1195 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| input | 1196 | — | unknown | Register 1196 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| input | 1197 | — | unknown | Register 1197 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| input | 1198 | — | unknown | Register 1198 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| input | 1199 | — | unknown | NewEPowerCalc Flag | Intelligent reading is used to identify software compatibility features | register value | 0 ： Old energy calculation； 1 ： new energy calculation | R | SOURCE_ONLY | source_claim | ;  |
| input | 1200 | — | unknown | MaxCellVolt | Maximumcellvoltage | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 1201 | — | unknown | MinCellVolt | Minimumcellvoltage | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 1202 | — | unknown | ModuleNum | NumberofBatterymodules | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 1203 | — | unknown | TotalCellNum | Totalnumberofcells | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 1204 | — | unknown | MaxVoltCellNo | MaxVoltCellNo | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 1205 | — | unknown | MinVoltCellNo | MinVoltCellNo | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 1206 | — | unknown | MaxTemprCell_ 10T | MaxTemprCell_10T | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 1207 | — | unknown | MinTemprCell_1 0T | MinTemprCell_10T | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 1208 | — | unknown | MaxTemprCellN o | MaxTemprCellNo | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 1209 | — | unknown | MinTemprCellN o | MinTemprCellNo | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 1210 | — | unknown | ProtectPackID | FaultPackID | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 1211 | — | unknown | MaxSOC | ParallelmaximumSOC | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 1212 | — | unknown | MinSOC | ParallelminimumSOC | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 1213 | — | unknown | BatProtect1Add | BatProtect1Add | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 1214 | — | unknown | BatProtect2Add | BatProtect2Add | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 1215 | — | unknown | BatWarn1Add | BatWarn1Add | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 1216 | — | unknown | BMS_HighestSof tVersion | BMS_HighestSoftVersion | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 1217 | — | unknown | BMS_Hardware Version | BMS_HardwareVersion | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 1218 | — | unknown | BMS_RequestTy pe | BMS_RequestType | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 1219 | — | unknown | Register 1219 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| input | 1220 | — | unknown | Register 1220 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| input | 1221 | — | unknown | Register 1221 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| input | 1222 | — | unknown | Register 1222 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| input | 1223 | — | unknown | Register 1223 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| input | 1224 | — | unknown | Register 1224 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| input | 1225 | — | unknown | Register 1225 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| input | 1226 | — | unknown | Register 1226 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| input | 1227 | — | unknown | Register 1227 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| input | 1228 | — | unknown | Register 1228 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| input | 1229 | — | unknown | Register 1229 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| input | 1230 | — | unknown | Register 1230 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| input | 1231 | — | unknown | Register 1231 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| input | 1232 | — | unknown | Register 1232 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| input | 1233 | — | unknown | Register 1233 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| input | 1234 | — | unknown | Register 1234 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| input | 1235 | — | unknown | Register 1235 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| input | 1236 | — | unknown | Register 1236 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| input | 1237 | — | unknown | Register 1237 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| input | 1238 | — | unknown | Register 1238 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| input | 1239 | — | unknown | Register 1239 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| input | 1240 | — | unknown | Register 1240 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| input | 1241 | — | unknown | Register 1241 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| input | 1242 | — | unknown | Register 1242 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| input | 1243 | — | unknown | Register 1243 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| input | 1244 | — | unknown | Register 1244 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| input | 1245 | — | unknown | Register 1245 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| input | 1246 | — | unknown | Register 1246 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| input | 1247 | — | unknown | Register 1247 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| input | 1248 | — | unknown | bKeyAgingTestO kFlag | Success sign of key detection beforeaging | register value | 1：Finishedtest 0 ： test not completed | R | SOURCE_ONLY | source_claim | ;  |
| input | 1249 | — | unknown | / | / | register value | reversed | R | SOURCE_ONLY | source_claim | ;  |
| input | 2000 | — | unknown | InverterStatus | Inverterrunstate | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 2001 | — | unknown | Register 2001 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| input | 2002 | — | unknown | Register 2002 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| input | 2003 | — | unknown | Register 2003 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| input | 2004 | — | unknown | Register 2004 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| input | 2005 | — | unknown | Register 2005 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| input | 2006 | — | unknown | Register 2006 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| input | 2007 | — | unknown | Register 2007 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| input | 2008 | — | unknown | Register 2008 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| input | 2009 | — | unknown | Register 2009 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| input | 2010 | — | unknown | Register 2010 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| input | 2011 | — | unknown | Register 2011 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| input | 2012 | — | unknown | Register 2012 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| input | 2013 | — | unknown | Register 2013 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| input | 2014 | — | unknown | Register 2014 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| input | 2015 | — | unknown | Register 2015 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| input | 2016 | — | unknown | Register 2016 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| input | 2017 | — | unknown | Register 2017 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| input | 2018 | — | unknown | Register 2018 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| input | 2019 | — | unknown | Register 2019 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| input | 2020 | — | unknown | Register 2020 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| input | 2021 | — | unknown | Register 2021 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| input | 2022 | — | unknown | Register 2022 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| input | 2023 | — | unknown | Register 2023 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| input | 2024 | — | unknown | Register 2024 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| input | 2025 | — | unknown | Register 2025 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| input | 2026 | — | unknown | Register 2026 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| input | 2027 | — | unknown | Register 2027 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| input | 2028 | — | unknown | Register 2028 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| input | 2029 | — | unknown | Register 2029 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| input | 2030 | — | unknown | Register 2030 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| input | 2031 | — | unknown | Register 2031 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| input | 2032 | — | unknown | Register 2032 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| input | 2033 | — | unknown | Register 2033 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| input | 2034 | — | unknown | Register 2034 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| input | 2035 | — | unknown | PacH | Outputpower(high) | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 2036 | — | unknown | PacL | Outputpower(low) | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 2037 | — | unknown | Fac | Gridfrequency | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 2038 | — | unknown | Vac1 | Three/singlephasegridvoltage | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 2039 | — | unknown | Iac1 | Three/singlephasegridoutputcurrent | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 2040 | — | unknown | Pac1H | Three/single phase grid output watt VA(high) | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 2041 | — | unknown | Pac1L | Three/single phase grid output watt VA(low) | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 2042 | — | unknown | Register 2042 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| input | 2043 | — | unknown | Register 2043 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| input | 2044 | — | unknown | Register 2044 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| input | 2045 | — | unknown | Register 2045 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| input | 2046 | — | unknown | Register 2046 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| input | 2047 | — | unknown | Register 2047 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| input | 2048 | — | unknown | Register 2048 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| input | 2049 | — | unknown | Register 2049 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| input | 2050 | — | unknown | Register 2050 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| input | 2051 | — | unknown | Register 2051 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| input | 2052 | — | unknown | Register 2052 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| input | 2053 | — | unknown | EactodayH | Todaygenerateenergy(high) | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 2054 | — | unknown | EactodayL | Todaygenerateenergy(low) | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 2055 | — | unknown | EactotalH | Totalgenerateenergy(high) | register value | SPA | R | SOURCE_ONLY | source_claim | ;  |
| input | 2056 | — | unknown | EactotalL | Totalgenerateenergy(low) | register value | SPA | R | SOURCE_ONLY | source_claim | ;  |
| input | 2057 | — | unknown | TimetotalH | Worktimetotal(high) | register value | SPA | R | SOURCE_ONLY | source_claim | ;  |
| input | 2058 | — | unknown | TimetotalL | Worktimetotal(low) | register value | SPA | R | SOURCE_ONLY | source_claim | ;  |
| input | 2059 | — | unknown | Register 2059 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| input | 2060 | — | unknown | Register 2060 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| input | 2061 | — | unknown | Register 2061 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| input | 2062 | — | unknown | Register 2062 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| input | 2063 | — | unknown | Register 2063 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| input | 2064 | — | unknown | Register 2064 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| input | 2065 | — | unknown | Register 2065 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| input | 2066 | — | unknown | Register 2066 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| input | 2067 | — | unknown | Register 2067 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| input | 2068 | — | unknown | Register 2068 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| input | 2069 | — | unknown | Register 2069 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| input | 2070 | — | unknown | Register 2070 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| input | 2071 | — | unknown | Register 2071 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| input | 2072 | — | unknown | Register 2072 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| input | 2073 | — | unknown | Register 2073 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| input | 2074 | — | unknown | Register 2074 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| input | 2075 | — | unknown | Register 2075 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| input | 2076 | — | unknown | Register 2076 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| input | 2077 | — | unknown | Register 2077 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| input | 2078 | — | unknown | Register 2078 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| input | 2079 | — | unknown | Register 2079 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| input | 2080 | — | unknown | Register 2080 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| input | 2081 | — | unknown | Register 2081 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| input | 2082 | — | unknown | Register 2082 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| input | 2083 | — | unknown | Register 2083 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| input | 2084 | — | unknown | Register 2084 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| input | 2085 | — | unknown | Register 2085 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| input | 2086 | — | unknown | Register 2086 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| input | 2087 | — | unknown | Register 2087 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| input | 2088 | — | unknown | Register 2088 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| input | 2089 | — | unknown | Register 2089 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| input | 2090 | — | unknown | Register 2090 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| input | 2091 | — | unknown | Register 2091 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| input | 2092 | — | unknown | Register 2092 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| input | 2093 | — | unknown | Temp1 | Invertertemperature | register value | SPA | R | SOURCE_ONLY | source_claim | ;  |
| input | 2094 | — | unknown | Temp2 | TheinsideIPMininverterTemperature | register value | SPA | R | SOURCE_ONLY | source_claim | ;  |
| input | 2095 | — | unknown | Temp3 | Boosttemperature | register value | SPA | R | SOURCE_ONLY | source_claim | ;  |
| input | 2096 | — | unknown | Temp4 | Temp4 | register value | reserved | R | SOURCE_ONLY | source_claim | ;  |
| input | 2097 | — | unknown | uwBatVolt_DSP | BatVolt_DSP | register value | BatVolt(DSP) | R | SOURCE_ONLY | source_claim | ;  |
| input | 2098 | — | unknown | PBusVoltage | PBusinsideVoltage | register value | SPA | R | SOURCE_ONLY | source_claim | ;  |
| input | 2099 | — | unknown | NBusVoltage | NBusinsideVoltage | register value | SPA | R | SOURCE_ONLY | source_claim | ;  |
| input | 2100 | — | unknown | RemoteCtrlEn | / | register value | Remote setup enable | R | SOURCE_ONLY | source_claim | ;  |
| input | 2101 | — | unknown | RemoteCtrlPow er | / | register value | Remotely setpower | R | SOURCE_ONLY | source_claim | ;  |
| input | 2102 | — | unknown | Extra AC Power to grid_H | ExtrainverteACPowertogridHigh | register value | SPAused | R | SOURCE_ONLY | source_claim | ;  |
| input | 2103 | — | unknown | Extra AC Power to grid_L | ExtrainverteACPowertogridLow | register value | SPAused | R | SOURCE_ONLY | source_claim | ;  |
| input | 2104 | — | unknown | Eextra_todayH | ExtrainverterPowerTOUser_Extra today(high) | register value | SPA used | R | SOURCE_ONLY | source_claim | ;  |
| input | 2105 | — | unknown | Eextra_todayL | ExtrainverterPowerTOUser_Extra today(low) | register value | SPA used | R | SOURCE_ONLY | source_claim | ;  |
| input | 2106 | — | unknown | Eextra_totalH | Extrainverter PowerTOUser_Extratotal(high) | register value | SPA used | R | SOURCE_ONLY | source_claim | ;  |
| input | 2107 | — | unknown | Eextra_totalL | ExtrainverterPowerTOUser_Extra total(low) | register value | SPA used | R | SOURCE_ONLY | source_claim | ;  |
| input | 2108 | — | unknown | Esystem_today H | SystemelectricenergytodayH | register value | SPA used System electric energy todayH | R | SOURCE_ONLY | source_claim | ;  |
| input | 2109 | — | unknown | Esystem_ today L | SystemelectricenergytodayL | register value | SPA used System electric energy todayL | R | SOURCE_ONLY | source_claim | ;  |
| input | 2110 | — | unknown | Esystem_totalH | SystemelectricenergytotalH | register value | SPA used System | R | SOURCE_ONLY | source_claim | ;  |
| input | 2111 | — | unknown | Esystem_totalL | SystemelectricenergytotalL | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 2112 | — | unknown | EACharge_Today _H | ACChargeenergytoday | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 2113 | — | unknown | EACharge_Today _L | ACChargeenergytoday | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 2114 | — | unknown | EACharge_Total _H | ACChargeenergytotal | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 2115 | — | unknown | EACharge_Total _L | ACChargeenergytotal | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 2116 | — | unknown | AC charge Power_H | Gridpowertolocalload | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 2117 | — | unknown | AC charge Power_L | Gridpowertolocalload | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 2118 | — | unknown | Priority | 0:LoadFirst 1:BatteryFirst 2:GridFirst | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 2119 | — | unknown | BatteryType | 0：Lead-acid 1：Lithiumbattery | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 2120 | — | unknown | AutoProofreadC MD | Agingmode | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 2121 | — | unknown | Register 2121 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| input | 2122 | — | unknown | Register 2122 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| input | 2123 | — | unknown | Register 2123 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| input | 2124 | — | unknown | reserved | reserved | register value | — | R | UNKNOWN_RESERVED | source_claim | ;  |

### SPH storage

Storage family applicability comes from the graph/catalogue ranges.

| Table | Address | Semantic | Role | Name | Description | Encoding / scale | Unit | Access | Status | Evidence | Notes |
|---|---:|---|---|---|---|---|---|---|---|---|---|
| holding | 0 | — | unknown | Inverter Enabled | Theinvertercanbeswitched onandoff,andtheBDCcanbe switchedonandoffforthe battreadyfunction. | register value; /10 | — | R/W | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| holding | 1 | — | unknown | Safety function enable flags | SPI: system protection interface Bit0~3:forCEI0-21 Bit4~6:forSAA | register value | — | W | SOURCE_ONLY | source_claim | ;  |
| holding | 2 | — | unknown | Persist power-factor commands | Means these settings will be acting or not when next poweron | register value | — | W | RESOLVED | semantic_correlated, source_claim | ;  |
| holding | 3 | — | unknown | Active power limit setpoint | 255:powerisnotbelimited | register value; /1 | % | W | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| holding | 4 | — | unknown | Reactive power limit setpoint | 255:powerisnotbelimited | register value; /1 | % | W | SOURCE_ONLY | source_claim | ;  |
| holding | 5 | — | unknown | Power factor target | Inverter output power factor’s10000times | register value; /10000 | pf | W | SOURCE_ONLY | source_claim | ;  |
| holding | 6 | — | unknown | Rated apparent power | Normal power(high) | register value; /10 | 0.1VA | R | SOURCE_ONLY | source_claim | ;  |
| holding | 7 | — | unknown | Rated apparent power | Normal power(low) | register value; /10 | 0.1VA | R | SOURCE_ONLY | source_claim | ;  |
| holding | 8 | — | unknown | Nominal PV voltage | NormalworkPV voltage | register value; /10 | 0.1V | R | SOURCE_ONLY | source_claim | ;  |
| holding | 9 | — | unknown | Firmware | Firmwareversion (high) | firmware_version; /10 | ASCII | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| holding | 10 | — | unknown | Firmware | Firmwareversion (middle) | register value | ASCII | R | SOURCE_ONLY | source_claim | ;  |
| holding | 11 | — | unknown | Firmware | Firmwareversion(low) | register value | ASCII | R | SOURCE_ONLY | source_claim | ;  |
| holding | 12 | — | unknown | Firmware | ControlFirmware version(high) | register value | ASCII | R | SOURCE_ONLY | source_claim | ;  |
| holding | 13 | — | unknown | Firmware | ControlFirmware version(middle) | register value | ASCII | R | SOURCE_ONLY | source_claim | ;  |
| holding | 14 | — | unknown | Firmware | ControlFirmware version(low) | register value | ASCII | R | SOURCE_ONLY | source_claim | ;  |
| holding | 15 | — | unknown | LCD language selection | 0:Italian; 1:English; 2:German; 3:Spanish; 4:French; 5:Chinese; 6：Polish 7：Portugues 8：Hungary | register value | — | W | SOURCE_ONLY | source_claim | ;  |
| holding | 16 | — | unknown | Country profile configured | CountrySelectedor not | register value | — | W | SOURCE_ONLY | source_claim | ;  |
| holding | 17 | — | unknown | PV start voltage threshold | Inputstartvoltage | register value; /10 | 0.1V | W | SOURCE_ONLY | source_claim | ;  |
| holding | 18 | — | unknown | Start-up delay | Starttime | register value; /1 | 1s | W | SOURCE_ONLY | source_claim | ;  |
| holding | 19 | — | unknown | Restart delay | RestartDelayTime afterfaultback; | register value; /1 | 1s | W | SOURCE_ONLY | source_claim | ;  |
| holding | 20 | — | unknown | Active power ramp rate (startup) | Powerstartslope | register value; /10 | 0.1% | W | SOURCE_ONLY | source_claim | ;  |
| holding | 21 | — | unknown | Active power ramp rate (restart) | Powerrestartslope | register value; /10 | 0.1% | W | SOURCE_ONLY | source_claim | ;  |
| holding | 22 | — | unknown | Modbus RTU baud rate | Select communicationbaudrat e 0:9600bps 1:38400bps | register value | — | W | SOURCE_ONLY | source_claim | ;  |
| holding | 23 | — | unknown | Serial Number | The Home Assistant integration exposes this as the device serial number and reuses it as the unique identifier. | serial_number; /10 | ASCII | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| holding | 24 | — | unknown | Serial Number | The Home Assistant integration exposes this as the device serial number and reuses it as the unique identifier. | register value | ASCII | R | SOURCE_ONLY | source_claim | ;  |
| holding | 25 | — | unknown | Serial Number | The Home Assistant integration exposes this as the device serial number and reuses it as the unique identifier. | register value | ASCII | R | SOURCE_ONLY | source_claim | ;  |
| holding | 26 | — | unknown | Serial Number | The Home Assistant integration exposes this as the device serial number and reuses it as the unique identifier. | register value | ASCII | R | SOURCE_ONLY | source_claim | ;  |
| holding | 27 | — | unknown | Serial Number | The Home Assistant integration exposes this as the device serial number and reuses it as the unique identifier. | register value | ASCII | R | SOURCE_ONLY | source_claim | ;  |
| holding | 28 | — | unknown | Inverter Model | Home Assistant renders this value as the string A# B# D# T# P# U# M# S# via the integration's model() helper. Vendor spec lists value pattern `&*5`; digits appear to be stored without the leading letter codes, so treat as encoded tokens until verified on hardware. | register value; /10 | — | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| holding | 29 | — | unknown | Inverter Model | Home Assistant renders this value as the string A# B# D# T# P# U# M# S# via the integration's model() helper. Vendor spec lists value pattern `&*5`; digits appear to be stored without the leading letter codes, so treat as encoded tokens until verified on hardware. | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| holding | 30 | — | unknown | Modbus slave address | Communicate address | register value | — | W | SOURCE_ONLY | source_claim | ;  |
| holding | 31 | — | unknown | Firmware update trigger | Updatefirmware | register value | — | W | SOURCE_ONLY | source_claim | ;  |
| holding | 32 | — | unknown | Reset user configuration | Use with caution; the inverter immediately reboots and loses provisioning data. | register value | — | W | SOURCE_ONLY | source_claim | ;  |
| holding | 33 | — | unknown | Factory reset | Equivalent to the front-panel factory reset. Requires re-commissioning afterwards. | register value | — | W | SOURCE_ONLY | source_claim | ;  |
| holding | 34 | — | unknown | Manufacturer information string | The original table lists these words as Manufacturer Info 8-1 (high/middle/low); combine them to read the full string. | register value | ASCII | R | SOURCE_ONLY | source_claim | ;  |
| holding | 35 | — | unknown | Manufacturer information string | The original table lists these words as Manufacturer Info 8-1 (high/middle/low); combine them to read the full string. | register value | ASCII | R | SOURCE_ONLY | source_claim | ;  |
| holding | 36 | — | unknown | Manufacturer information string | The original table lists these words as Manufacturer Info 8-1 (high/middle/low); combine them to read the full string. | register value | ASCII | R | SOURCE_ONLY | source_claim | ;  |
| holding | 37 | — | unknown | Manufacturer information string | The original table lists these words as Manufacturer Info 8-1 (high/middle/low); combine them to read the full string. | register value | ASCII | R | SOURCE_ONLY | source_claim | ;  |
| holding | 38 | — | unknown | Manufacturer information string | The original table lists these words as Manufacturer Info 8-1 (high/middle/low); combine them to read the full string. | register value | ASCII | R | SOURCE_ONLY | source_claim | ;  |
| holding | 39 | — | unknown | Manufacturer information string | The original table lists these words as Manufacturer Info 8-1 (high/middle/low); combine them to read the full string. | register value | ASCII | R | SOURCE_ONLY | source_claim | ;  |
| holding | 40 | — | unknown | Manufacturer information string | The original table lists these words as Manufacturer Info 8-1 (high/middle/low); combine them to read the full string. | register value | ASCII | R | SOURCE_ONLY | source_claim | ;  |
| holding | 41 | — | unknown | Manufacturer information string | The original table lists these words as Manufacturer Info 8-1 (high/middle/low); combine them to read the full string. | register value | ASCII | R | SOURCE_ONLY | source_claim | ;  |
| holding | 42 | — | unknown | G100 failsafe enable | EnglishG100failsafeset | register value | — | W | SOURCE_ONLY | source_claim | ;  |
| holding | 43 | — | unknown | Device Type Code | Vendor spec provides value pattern `&*6`; handle as encoded type/family digits with implied prefixes pending confirmation. | register value; /10 | — | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| holding | 44 | — | unknown | Number Of Trackers And Phases | Inputtrackernumand outputphasenum | register value; /10 | — | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| holding | 45 | — | unknown | System clock year | Localtime | register value | — | W | SOURCE_ONLY | source_claim | ;  |
| holding | 46 | — | unknown | System clock month | Systemtime-Month | register value | — | W | SOURCE_ONLY | source_claim | ;  |
| holding | 47 | — | unknown | System clock day | Systemtime-Day | register value | — | W | SOURCE_ONLY | source_claim | ;  |
| holding | 48 | — | unknown | System clock hour | Systemtime-Hour | register value | — | W | SOURCE_ONLY | source_claim | ;  |
| holding | 49 | — | unknown | System clock minute | Systemtime-Min | register value | — | W | SOURCE_ONLY | source_claim | ;  |
| holding | 50 | — | unknown | System clock second | Systemtime-Second | register value | — | W | SOURCE_ONLY | source_claim | ;  |
| holding | 51 | — | unknown | System clock weekday | SystemWeekly | register value | — | W | SOURCE_ONLY | source_claim | ;  |
| holding | 52 | — | unknown | Stage 1 undervoltage limit | Gridvoltagelowlimit protect | register value | 0.1V | W | SOURCE_ONLY | source_claim | ;  |
| holding | 53 | — | unknown | Stage 1 overvoltage limit | Gridvoltagehighlimit protect | register value | 0.1V | W | SOURCE_ONLY | source_claim | ;  |
| holding | 54 | — | unknown | Stage 1 underfrequency limit | Gridfrequencylow limitprotect | register value | 0.01 Hz | W | SOURCE_ONLY | source_claim | ;  |
| holding | 55 | — | unknown | Stage 1 overfrequency limit | Gridhigh frequencylimitprotect | register value | 0.01 Hz | W | SOURCE_ONLY | source_claim | ;  |
| holding | 56 | — | unknown | Stage 2 undervoltage limit | Gridvoltagelowlimit protect2 | register value | 0.1V | W | SOURCE_ONLY | source_claim | ;  |
| holding | 57 | — | unknown | Stage 2 overvoltage limit | Gridvoltagehighlimit protect2 | register value | 0.1V | W | SOURCE_ONLY | source_claim | ;  |
| holding | 58 | — | unknown | Stage 2 underfrequency limit | Gridfrequencylow limitprotect2 | register value | 0.01 Hz | W | SOURCE_ONLY | source_claim | ;  |
| holding | 59 | — | unknown | Stage 2 overfrequency limit | Gridhighfrequency limitprotect2 | register value | 0.01 Hz | W | SOURCE_ONLY | source_claim | ;  |
| holding | 60 | — | unknown | Stage 3 undervoltage limit | Grid voltage low limit protect3 | register value | 0.1V | W | SOURCE_ONLY | source_claim | ;  |
| holding | 61 | — | unknown | Stage 3 overvoltage limit | Grid voltage high limit protect3 | register value | 0.1V | W | SOURCE_ONLY | source_claim | ;  |
| holding | 62 | grid_frequency | alternate | Stage 3 underfrequency limit | Grid frequency low limitprotect3 | register value | 0.01Hz | W | SOURCE_ONLY | source_claim | ; alternates: register:storage_sph:holding:63, register:storage_sph:holding:72, register:storage_sph:holding:73, register:storage_sph:holding:74, register:storage_sph:holding:75, register:storage_sph:holding:78, register:storage_sph:holding:79, register:storage_sph:input:37 |
| holding | 63 | grid_frequency | alternate | Stage 3 overfrequency limit | Grid frequency high limitprotect3 | register value | 0.01Hz | W | SOURCE_ONLY | source_claim | ; alternates: register:storage_sph:holding:62, register:storage_sph:holding:72, register:storage_sph:holding:73, register:storage_sph:holding:74, register:storage_sph:holding:75, register:storage_sph:holding:78, register:storage_sph:holding:79, register:storage_sph:input:37 |
| holding | 64 | — | unknown | Reconnect undervoltage limit | Gridlowvoltagelimit connecttoGrid | register value | 0.1V | W | SOURCE_ONLY | source_claim | ;  |
| holding | 65 | — | unknown | Reconnect overvoltage limit | Gridhighvoltagelimit connecttoGrid | register value | 0.1V | W | SOURCE_ONLY | source_claim | ;  |
| holding | 66 | — | unknown | Reconnect underfrequency limit | Gridlowfrequency | register value | 0.01 | W | SOURCE_ONLY | source_claim | ;  |
| holding | 67 | — | unknown | Reconnect overfrequency limit | Gridhighfrequency limitconnecttoGrid | register value | 0.01 Hz | W | SOURCE_ONLY | source_claim | ;  |
| holding | 68 | — | unknown | Stage 1 undervoltage trip delay | Grid voltage low limit protecttime 1 | register value | Cycle | W | SOURCE_ONLY | source_claim | ;  |
| holding | 69 | — | unknown | Stage 1 overvoltage trip delay | Grid voltage high limit protecttime 1 | register value | Cycle | W | SOURCE_ONLY | source_claim | ;  |
| holding | 70 | — | unknown | Stage 2 undervoltage trip delay | Grid voltage low limit protecttime 2 | register value | Cycle | W | SOURCE_ONLY | source_claim | ;  |
| holding | 71 | — | unknown | Stage 2 overvoltage trip delay | Grid voltage high limit protecttime 2 | register value | Cycle | W | SOURCE_ONLY | source_claim | ;  |
| holding | 72 | grid_frequency | alternate | Stage 1 underfrequency trip delay | Grid frequency low limitprotecttime 1 | register value | Cycle | W | SOURCE_ONLY | source_claim | ; alternates: register:storage_sph:holding:62, register:storage_sph:holding:63, register:storage_sph:holding:73, register:storage_sph:holding:74, register:storage_sph:holding:75, register:storage_sph:holding:78, register:storage_sph:holding:79, register:storage_sph:input:37 |
| holding | 73 | grid_frequency | alternate | Modbus Version | Grid frequency high limitprotecttime 1 | register value | Cycle | W | SOURCE_ONLY | source_claim | ; alternates: register:storage_sph:holding:62, register:storage_sph:holding:63, register:storage_sph:holding:72, register:storage_sph:holding:74, register:storage_sph:holding:75, register:storage_sph:holding:78, register:storage_sph:holding:79, register:storage_sph:input:37 |
| holding | 74 | grid_frequency | alternate | Stage 2 underfrequency trip delay | Grid frequency low limitprotecttime 2 | register value | Cycle | W | SOURCE_ONLY | source_claim | ; alternates: register:storage_sph:holding:62, register:storage_sph:holding:63, register:storage_sph:holding:72, register:storage_sph:holding:73, register:storage_sph:holding:75, register:storage_sph:holding:78, register:storage_sph:holding:79, register:storage_sph:input:37 |
| holding | 75 | grid_frequency | alternate | Stage 2 overfrequency trip delay | Grid frequency high limitprotecttime 2 | register value | Cycle | W | SOURCE_ONLY | source_claim | ; alternates: register:storage_sph:holding:62, register:storage_sph:holding:63, register:storage_sph:holding:72, register:storage_sph:holding:73, register:storage_sph:holding:74, register:storage_sph:holding:78, register:storage_sph:holding:79, register:storage_sph:input:37 |
| holding | 76 | — | unknown | Stage 3 undervoltage trip delay | Grid voltage low limit protecttime 3 | register value | Cycle | W | SOURCE_ONLY | source_claim | ;  |
| holding | 77 | — | unknown | Stage 3 overvoltage trip delay | Grid voltage high limit protecttime 3 | register value | Cycle | W | SOURCE_ONLY | source_claim | ;  |
| holding | 78 | grid_frequency | alternate | Stage 3 underfrequency trip delay | Grid frequency low limitprotecttime 3 | register value | Cycle | W | SOURCE_ONLY | source_claim | ; alternates: register:storage_sph:holding:62, register:storage_sph:holding:63, register:storage_sph:holding:72, register:storage_sph:holding:73, register:storage_sph:holding:74, register:storage_sph:holding:75, register:storage_sph:holding:79, register:storage_sph:input:37 |
| holding | 79 | grid_frequency | alternate | Stage 3 overfrequency trip delay | Grid frequency high limitprotecttime 3 | register value | Cycle | W | SOURCE_ONLY | source_claim | ; alternates: register:storage_sph:holding:62, register:storage_sph:holding:63, register:storage_sph:holding:72, register:storage_sph:holding:73, register:storage_sph:holding:74, register:storage_sph:holding:75, register:storage_sph:holding:78, register:storage_sph:input:37 |
| holding | 80 | — | unknown | Ten-minute overvoltage limit | Voltprotectionfor10 min | register value | 0.1V | W | SOURCE_ONLY | source_claim | ;  |
| holding | 81 | — | unknown | PV input high-voltage fault | PVVoltageHigh Fault | register value | 0.1V | W | SOURCE_ONLY | source_claim | ;  |
| holding | 82 | — | unknown | Controller firmware build string | Positions: 0-1 model letters, 2-3 model variant, 4-5 DSP1 build, 6-7 DSP2/M0 build, 8-9 CPLD/AFCI build, 10-11 M3 build. | register value | ASCII | R | SOURCE_ONLY | source_claim | ;  |
| holding | 83 | — | unknown | Controller firmware build string | Positions: 0-1 model letters, 2-3 model variant, 4-5 DSP1 build, 6-7 DSP2/M0 build, 8-9 CPLD/AFCI build, 10-11 M3 build. | register value | ASCII | R | SOURCE_ONLY | source_claim | ;  |
| holding | 84 | — | unknown | Controller firmware build string | Positions: 0-1 model letters, 2-3 model variant, 4-5 DSP1 build, 6-7 DSP2/M0 build, 8-9 CPLD/AFCI build, 10-11 M3 build. | register value | ASCII | R | SOURCE_ONLY | source_claim | ;  |
| holding | 85 | — | unknown | Controller firmware build string | Positions: 0-1 model letters, 2-3 model variant, 4-5 DSP1 build, 6-7 DSP2/M0 build, 8-9 CPLD/AFCI build, 10-11 M3 build. | register value | ASCII | R | SOURCE_ONLY | source_claim | ;  |
| holding | 86 | — | unknown | Controller firmware build string | Positions: 0-1 model letters, 2-3 model variant, 4-5 DSP1 build, 6-7 DSP2/M0 build, 8-9 CPLD/AFCI build, 10-11 M3 build. | register value | ASCII | R | SOURCE_ONLY | source_claim | ;  |
| holding | 87 | — | unknown | Controller firmware build string | Positions: 0-1 model letters, 2-3 model variant, 4-5 DSP1 build, 6-7 DSP2/M0 build, 8-9 CPLD/AFCI build, 10-11 M3 build. | register value | ASCII | R | SOURCE_ONLY | source_claim | ;  |
| holding | 88 | — | unknown | Modbus Version | ModbusVersion | register value; /100 | Int(16 bits) | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| holding | 89 | — | unknown | Power-factor control mode | 0=Unity PF, 1=Fixed PF setpoint, 2=Default PF line, 3=User-defined PF line, 4=Under-excited reactive power, 5=Over-excited reactive power, 6=Q(V) curve, 7=Direct control, 8=Static capacitive QV, 9=Static inductive QV. | register value | — | W | SOURCE_ONLY | source_claim | ;  |
| holding | 90 | — | unknown | GPRS modem IP/status flags | Bit 0-3: 0=idle, 1=IP read requested, 2=set IP succeeded; Bit 4-7: 0=unknown, 1=modem OK, 2=no SIM, 3=no network, 4=TCP connect fail, 5=TCP connected, etc. | register value | — | W | UNKNOWN_RESERVED | source_claim | ;  |
| holding | 91 | — | unknown | Frequency derating start | Frequencyderating startpoint | register value | 0.01H Z | W | SOURCE_ONLY | source_claim | ;  |
| holding | 92 | — | unknown | Frequency derating slope | Frequency–loadlimit rate | register value | 10tim es | W | SOURCE_ONLY | source_claim | ;  |
| holding | 93 | — | unknown | CEI 0-21 Q(V) point V1S | CEI021V1SQ(v) | register value | 0.1V | W | SOURCE_ONLY | source_claim | ;  |
| holding | 94 | — | unknown | CEI 0-21 Q(V) point V2S | CEI021V2SQ(v) | register value | 0.1V | W | SOURCE_ONLY | source_claim | ;  |
| holding | 95 | — | unknown | CEI 0-21 Q(V) point V1L | CEI021V1LQ(v) | register value | 0.1V | W | SOURCE_ONLY | source_claim | ;  |
| holding | 96 | — | unknown | CEI 0-21 Q(V) point V2L | CEI021V2LQ(v) | register value | 0.1V | W | SOURCE_ONLY | source_claim | ;  |
| holding | 97 | — | unknown | Q(V) lock-in active power | Q(v)lockinactive powerofCEI021 | register value | Percen t | W | SOURCE_ONLY | source_claim | ;  |
| holding | 98 | — | unknown | Q(V) lock-out active power | Q(v)lockOutactive powerofCEI021 | register value | Percen t | W | SOURCE_ONLY | source_claim | ;  |
| holding | 99 | — | unknown | Power-factor curve lock-in voltage | Lockingirdvoltof CEI021PFline | register value | 0.1V | W | SOURCE_ONLY | source_claim | ;  |
| holding | 100 | — | unknown | Power-factor curve lock-out voltage | Lockoutgirdvoltof CEI021PFline | register value | 0.1V | W | SOURCE_ONLY | source_claim | ;  |
| holding | 101 | — | unknown | Power-factor adjust value 1 | PFadjustvalue1 | register value | — | W | SOURCE_ONLY | source_claim | ;  |
| holding | 102 | — | unknown | Power-factor adjust value 2 | PFadjustvalue2 | register value | — | W | SOURCE_ONLY | source_claim | ;  |
| holding | 103 | — | unknown | Power-factor adjust value 3 | PFadjustvalue3 | register value | — | W | SOURCE_ONLY | source_claim | ;  |
| holding | 104 | — | unknown | Power-factor adjust value 4 | PFadjustvalue4 | register value | — | W | SOURCE_ONLY | source_claim | ;  |
| holding | 105 | — | unknown | Power-factor adjust value 5 | PFadjustvalue5 | register value | — | W | SOURCE_ONLY | source_claim | ;  |
| holding | 106 | — | unknown | Power-factor adjust value 6 | PFadjustvalue6 | register value | — | W | SOURCE_ONLY | source_claim | ;  |
| holding | 107 | — | unknown | Q(V) response delay | QV Reactive Power delaytime | register value | 1S | W | SOURCE_ONLY | source_claim | ;  |
| holding | 108 | — | unknown | Over-frequency derating delay | Overfrequency derati ngdelaytime | register value | 50ms | W | SOURCE_ONLY | source_claim | ;  |
| holding | 109 | — | unknown | Maximum reactive power magnitude | QmaxforQ(V)curve | register value | 0.1% | W | SOURCE_ONLY | source_claim | ;  |
| holding | 110 | — | unknown | PF curve point 1 load | 255meansnothispoint | register value | percen t | W | SOURCE_ONLY | source_claim | ;  |
| holding | 111 | — | unknown | PF curve point 1 target | PFlimitlinepoint1 powerfactor | register value | — | W | SOURCE_ONLY | source_claim | ;  |
| holding | 112 | — | unknown | PF curve point 2 load | 255meansnothispoint | register value | percen t | W | SOURCE_ONLY | source_claim | ;  |
| holding | 113 | — | unknown | PF curve point 2 target | PFlimitlinepoint 2powerfactor | register value | — | W | SOURCE_ONLY | source_claim | ;  |
| holding | 114 | — | unknown | PF curve point 3 load | 255meansnothispoint | register value | percen t | W | SOURCE_ONLY | source_claim | ;  |
| holding | 115 | — | unknown | PF curve point 3 target | PFlimitlinepoint3 powerfactor | register value | — | W | SOURCE_ONLY | source_claim | ;  |
| holding | 116 | — | unknown | PF curve point 4 load | 255meansnothispoint | register value | percen t | W | SOURCE_ONLY | source_claim | ;  |
| holding | 117 | — | unknown | PF curve point 4 target | PFlimitlinepoint4 powerfactor | register value | — | W | SOURCE_ONLY | source_claim | ;  |
| holding | 118 | — | unknown | Module code segments | SxxBxx | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| holding | 119 | — | unknown | Module code segments | DxxTxx | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| holding | 120 | — | unknown | Module code segments | PxxUxx | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| holding | 121 | — | unknown | Module code segments | Mxxxx Power | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| holding | 122 | — | unknown | Export limit enable mode | ExportLimitenable, 0:DisableexportLimit; 1:Enable485exportLimit; 2:Enable232exportLimit; 3:EnableCTexportLimit; | register value | — | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 123 | — | unknown | Export limit power setpoint | ExportLimitPowerRate | register value | 0.1% | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 124 | — | unknown | Tracker coupling mode | 0:Independent 1:DCSource 2:Parallel | register value | — | W | SOURCE_ONLY | source_claim | ;  |
| holding | 1000 | — | unknown | Float charge current limit i | Float charge current limit i | register value | — | W | SOURCE_ONLY | source_claim | ;  |
| holding | 1001 | — | unknown | PF CMD memory state | PF CMD memory state | register value | 0or1, | W | SOURCE_ONLY | source_claim | ;  |
| holding | 1002 | — | unknown | VbatStartF orDischarg e | VbatStartF orDischarg e | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| holding | 1003 | — | unknown | VbatlowWa rnClr l | VbatlowWa rnClr l | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| holding | 1004 | — | unknown | Vbatstopfo rdischarge | Vbatstopfo rdischarge | register value | — | W | SOURCE_ONLY | source_claim | ;  |
| holding | 1005 | — | unknown | Vbat stop forcharge | Shouldstopcharge whenhigherthanthis voltage | register value | 0.01V | W | SOURCE_ONLY | source_claim | ;  |
| holding | 1006 | — | unknown | Vbat start for discharge | Should not discharge when lower than this voltage | register value | 0.01V | W | SOURCE_ONLY | source_claim | ;  |
| holding | 1007 | — | unknown | Vbat constant charge | CVvoltage（acid） | register value | 0.01V | W | SOURCE_ONLY | source_claim | ;  |
| holding | 1008 | — | unknown | EESysInfo.S ysSetEn | SystemEnable | register value | — | W | SOURCE_ONLY | source_claim | ;  |
| holding | 1009 | — | unknown | Battemp lower limit d | Batterytemperature lowerlimitfordischarge | register value | 0.1℃ | W | SOURCE_ONLY | source_claim | ;  |
| holding | 1010 | — | unknown | Bat temp upper limit d | Batterytemperature upperlimitfordischarge | register value | 0.1℃ | W | SOURCE_ONLY | source_claim | ;  |
| holding | 1011 | — | unknown | Bat temp lower limit c | Lowertemperaturelimit | register value | 0.1℃ | W | SOURCE_ONLY | source_claim | ;  |
| holding | 1012 | — | unknown | Bat temp upper limit c | Uppertemperaturelimit | register value | 0.1℃ | W | SOURCE_ONLY | source_claim | ;  |
| holding | 1013 | — | unknown | uwUnderFr eDischarge DelyTime | UnderFreDelayTime | register value | 50ms | R | SOURCE_ONLY | source_claim | ;  |
| holding | 1014 | — | unknown | BatMdlSeri alNum | SPH4-11Kused | register value | — | W | SOURCE_ONLY | source_claim | ;  |
| holding | 1015 | — | unknown | BatMdlPara llNum | SPH4-11Kused | register value | — | W | SOURCE_ONLY | source_claim | ;  |
| holding | 1016 | — | unknown | DRMS_EN | 0：disable 1：enable | register value | / | R | SOURCE_ONLY | source_claim | ;  |
| holding | 1017 | — | unknown | Bat First Start Time 4 | Higheight:hours Loweight:minutes | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| holding | 1018 | — | unknown | Bat First Stop Time 4 | Higheight:hours Loweight:minutes | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| holding | 1019 | — | unknown | BatFirst on/off Switch4 | Batterypriorityenable1 | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| holding | 1020 | — | unknown | Bat First Start Time 5 | Higheight:hours Loweight:minutes | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| holding | 1021 | — | unknown | BatFirst StopTime 5 | Higheight:hours Loweight:minutes | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| holding | 1022 | — | unknown | BatFirst on/off Switch5 | Batterypriorityenable1 | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| holding | 1023 | — | unknown | BatFirst StartTime 6 | Higheight:hours Loweight:minutes | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| holding | 1024 | — | unknown | BatFirst StopTime 6 | Higheight:hours Loweight:minutes | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| holding | 1025 | — | unknown | BatFirst on/off Switch6 | Batterypriorityenable1 | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| holding | 1026 | — | unknown | GridFirst StartTime | Higheight:hours Loweight:minutes | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| holding | 1027 | — | unknown | GridFirst StopTime 4 | Higheight:hours Loweight:minutes | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| holding | 1028 | — | unknown | Grid First Stop Switch4 | Gridpriorityenable | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| holding | 1029 | — | unknown | GridFirst StartTime 5 | Higheight:hours Loweight:minutes | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| holding | 1030 | — | unknown | GridFirst StopTime 5 | Higheight:hours Loweight:minutes | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| holding | 1031 | — | unknown | Grid First Stop Switch5 | Gridpriorityenable | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| holding | 1032 | — | unknown | GridFirst StartTime 6 | Higheight:hours Loweight:minutes | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| holding | 1033 | — | unknown | GridFirst StopTime 6 | Higheight:hours Loweight:minutes | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| holding | 1034 | — | unknown | Grid First Stop Switch6 | Gridpriorityenable | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| holding | 1035 | — | unknown | BatFirst StartTime 4 | Higheight:hours Loweight:minutes | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| holding | 1036 | — | unknown | / | Reserve | register value | / | R | SOURCE_ONLY | source_claim | ;  |
| holding | 1037 | — | unknown | bCTMode | UsetheCTModeto ChooseRFCT\Cable CT\METER | register value | — | W | SOURCE_ONLY | source_claim | ;  |
| holding | 1038 | — | unknown | CTAdjust | CTAdjustenable | register value | — | W | SOURCE_ONLY | source_claim | ;  |
| holding | 1039 | — | unknown | / | Reserve | register value | / | R | SOURCE_ONLY | source_claim | ;  |
| holding | 1040 | — | unknown | / | / | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| holding | 1041 | — | unknown | / | / | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| holding | 1042 | — | unknown | / | / | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| holding | 1043 | — | unknown | / | / | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| holding | 1044 | — | unknown | Priority | ForceChrEn/ForceDischr En Load first/bat first /grid first | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| holding | 1045 | — | unknown | / | / | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| holding | 1046 | — | unknown | / | / | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| holding | 1047 | — | unknown | AgingTestSt ep Cmd | Commandforagingtest | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| holding | 1048 | — | unknown | BatteryTyp e | Batterytypechooseof buck-boostinput | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| holding | 1049 | — | unknown | / | / | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| holding | 1050 | — | unknown | / | / | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| holding | 1051 | — | unknown | / | / | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| holding | 1052 | — | unknown | / | / | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| holding | 1053 | — | unknown | / | / | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| holding | 1054 | — | unknown | / | / | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| holding | 1055 | — | unknown | Register 1055 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| holding | 1056 | — | unknown | Register 1056 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| holding | 1057 | — | unknown | Register 1057 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| holding | 1058 | — | unknown | Register 1058 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| holding | 1059 | — | unknown | Register 1059 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| holding | 1060 | — | unknown | BuckUpsFunE n | 0:disable 1:enable | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| holding | 1061 | — | unknown | BuckUPSVoltS et | UPSoutputvoltage | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| holding | 1062 | — | unknown | UPSFreqSet | UPSoutputfrequency | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| holding | 1063 | — | unknown | Register 1063 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| holding | 1064 | — | unknown | Register 1064 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| holding | 1065 | — | unknown | Register 1065 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| holding | 1066 | — | unknown | Register 1066 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| holding | 1067 | — | unknown | Register 1067 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| holding | 1068 | — | unknown | Register 1068 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| holding | 1069 | — | unknown | Register 1069 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| holding | 1070 | grid_first_discharge_rate | supported | Grid-first discharge limit | Discharge Power Rate whenGridFirst | register value | 1% | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 1071 | grid_first_stop_soc | supported | Grid-first stop SOC | Stop Discharge soc when GridFirst | register value | 1% | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 1072 | — | unknown | / | / | register value | / | R | SOURCE_ONLY | source_claim | ;  |
| holding | 1073 | — | unknown | / | / | register value | / | R | SOURCE_ONLY | source_claim | ;  |
| holding | 1074 | — | unknown | / | / | register value | / | R | SOURCE_ONLY | source_claim | ;  |
| holding | 1075 | — | unknown | / | / | register value | / | R | SOURCE_ONLY | source_claim | ;  |
| holding | 1076 | — | unknown | / | / | register value | / | R | SOURCE_ONLY | source_claim | ;  |
| holding | 1077 | — | unknown | / | / | register value | / | R | SOURCE_ONLY | source_claim | ;  |
| holding | 1078 | — | unknown | / | / | register value | / | R | SOURCE_ONLY | source_claim | ;  |
| holding | 1079 | — | unknown | / | / | register value | / | R | SOURCE_ONLY | source_claim | ;  |
| holding | 1080 | — | unknown | Grid-first slot 1 start | High byte = hour (0-23); low byte = minute (0-59). | register value | hh:mm | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 1081 | — | unknown | Grid-first slot 1 stop | High byte = hour (0-23); low byte = minute (0-59). | register value | hh:mm | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 1082 | — | unknown | Grid-first slot 1 enable | Enable:1 Disable:0 | register value | — | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 1083 | — | unknown | Grid-first slot 2 start | High byte = hour (0-23); low byte = minute (0-59). | register value | hh:mm | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 1084 | — | unknown | Grid-first slot 2 stop | High byte = hour (0-23); low byte = minute (0-59). | register value | hh:mm | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 1085 | — | unknown | Grid-first slot 2 enable | When set from the LCD, this slot can be tied to the Force Discharge command. | register value | — | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 1086 | — | unknown | Grid-first slot 3 start | High byte = hour (0-23); low byte = minute (0-59). | register value | hh:mm | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 1087 | — | unknown | Grid-first slot 3 stop | High byte = hour (0-23); low byte = minute (0-59). | register value | hh:mm | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 1088 | — | unknown | Grid-first slot 3 enable | Enable:1 Disable:0 | register value | — | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 1089 | — | unknown | / | / | register value | / | R | SOURCE_ONLY | source_claim | ;  |
| holding | 1090 | battery_first_charge_rate | supported | Battery-first charge limit | Charge Power Rate when BatFirst | register value | 1% | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 1091 | battery_first_stop_soc | supported | Battery-first stop SOC | Stop Charge soc when Bat First | register value | 1% | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 1092 | — | unknown | Battery-first AC charge enable | WhenBatFirst Enable:1 Disable:0 | register value | — | R/W | RESOLVED | semantic_correlated, source_claim | ;  |
| holding | 1093 | — | unknown | Register 1093 | — | register value | — | R | UNKNOWN_RESERVED | source_claim | ;  |
| holding | 1094 | — | unknown | Register 1094 | — | register value | — | R | UNKNOWN_RESERVED | source_claim | ;  |
| holding | 1095 | — | unknown | Register 1095 | — | register value | — | R | UNKNOWN_RESERVED | source_claim | ;  |
| holding | 1096 | — | unknown | Register 1096 | — | register value | — | R | UNKNOWN_RESERVED | source_claim | ;  |
| holding | 1097 | — | unknown | Register 1097 | — | register value | — | R | UNKNOWN_RESERVED | source_claim | ;  |
| holding | 1098 | — | unknown | Register 1098 | — | register value | — | R | UNKNOWN_RESERVED | source_claim | ;  |
| holding | 1099 | — | unknown | Register 1099 | — | register value | — | R | UNKNOWN_RESERVED | source_claim | ;  |
| holding | 1100 | — | unknown | Battery-first slot 1 start | High byte = hour (0-23); low byte = minute (0-59). | register value | hh:mm | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 1101 | — | unknown | Battery-first slot 1 stop | High byte = hour (0-23); low byte = minute (0-59). | register value | hh:mm | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 1102 | — | unknown | Battery-first slot 1 enable | Enable:1 Disable:0 | register value | — | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 1103 | — | unknown | Battery-first slot 2 start | High byte = hour (0-23); low byte = minute (0-59). | register value | hh:mm | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 1104 | — | unknown | Battery-first slot 2 stop | High byte = hour (0-23); low byte = minute (0-59). | register value | hh:mm | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 1105 | — | unknown | Battery-first slot 2 enable | Enable:1 Disable:0 | register value | — | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 1106 | — | unknown | Battery-first slot 3 start | High byte = hour (0-23); low byte = minute (0-59). | register value | hh:mm | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 1107 | — | unknown | Battery-first slot 3 stop | High byte = hour (0-23); low byte = minute (0-59). | register value | hh:mm | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 1108 | — | unknown | Battery-first slot 3 enable | Enable:1 Disable:0 | register value | — | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 1109 | — | unknown | / | reserve | register value | / | R | SOURCE_ONLY | source_claim | ;  |
| holding | 1110 | — | unknown | Load-first slot 1 start | SPA/reserve | register value | hh:mm | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 1111 | — | unknown | Load-first slot 1 stop | SPA/reserve | register value | hh:mm | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 1112 | — | unknown | Load-first slot 1 enable | SPA/reserve | register value | — | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 1113 | — | unknown | Load-first slot 2 start | SPA/reserve | register value | hh:mm | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 1114 | — | unknown | Load-first slot 2 stop | SPA/reserve | register value | hh:mm | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 1115 | — | unknown | Load-first slot 2 enable | SPA/reserve | register value | — | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 1116 | — | unknown | Load-first slot 3 start | SPA/reserve | register value | hh:mm | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 1117 | — | unknown | Load-first slot 3 stop | SPA/reserve | register value | hh:mm | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 1118 | — | unknown | Load-first slot 3 enable | SPA/reserve | register value | — | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 1119 | — | unknown | Energy calculation formula | 0：Theoldformula 1 ： The new formula | register value | / | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 1120 | — | unknown | Backup enable | MIXUS | register value | — | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 1121 | — | unknown | SGIP enable | MIXUS | register value | — | R/W | SOURCE_ONLY | source_claim | ;  |
| holding | 1122 | — | unknown | Register 1122 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| holding | 1123 | — | unknown | Register 1123 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| holding | 1124 | — | unknown | Register 1124 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| input | 0 | inverter_status | supported | Inverter status | InverterStatus | register value; /10 | — | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 1 | pv_total_power | alternate | PV input power | PpvH | register value; /10 | 0.1W | R/W | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ; alternates: register:storage_sph:input:2, register:storage_sph:input:5, register:storage_sph:input:6, register:storage_sph:input:9, register:storage_sph:input:10, register:storage_sph:input:13, register:storage_sph:input:14, register:storage_sph:input:17, register:storage_sph:input:18, register:storage_sph:input:21, register:storage_sph:input:22, register:storage_sph:input:25, register:storage_sph:input:26, register:storage_sph:input:29, register:storage_sph:input:30, register:storage_sph:input:33, register:storage_sph:input:34 |
| input | 2 | pv_total_power | alternate | PV input power | PpvL | register value; /10 | 0.1W | R/W | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ; alternates: register:storage_sph:input:1, register:storage_sph:input:5, register:storage_sph:input:6, register:storage_sph:input:9, register:storage_sph:input:10, register:storage_sph:input:13, register:storage_sph:input:14, register:storage_sph:input:17, register:storage_sph:input:18, register:storage_sph:input:21, register:storage_sph:input:22, register:storage_sph:input:25, register:storage_sph:input:26, register:storage_sph:input:29, register:storage_sph:input:30, register:storage_sph:input:33, register:storage_sph:input:34 |
| input | 3 | — | unknown | PV1 DC voltage | Vpv1 | register value; /10 | 0.1V | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 4 | — | unknown | PV1 DC current | PV1Curr | register value; /10 | 0.1A | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 5 | pv_total_power | alternate | PV1 DC power | Ppv1H | register value; /10 | 0.1W | R/W | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ; alternates: register:storage_sph:input:1, register:storage_sph:input:2, register:storage_sph:input:6, register:storage_sph:input:9, register:storage_sph:input:10, register:storage_sph:input:13, register:storage_sph:input:14, register:storage_sph:input:17, register:storage_sph:input:18, register:storage_sph:input:21, register:storage_sph:input:22, register:storage_sph:input:25, register:storage_sph:input:26, register:storage_sph:input:29, register:storage_sph:input:30, register:storage_sph:input:33, register:storage_sph:input:34 |
| input | 6 | pv_total_power | alternate | PV1 DC power | Ppv1L | register value; /10 | 0.1W | R/W | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ; alternates: register:storage_sph:input:1, register:storage_sph:input:2, register:storage_sph:input:5, register:storage_sph:input:9, register:storage_sph:input:10, register:storage_sph:input:13, register:storage_sph:input:14, register:storage_sph:input:17, register:storage_sph:input:18, register:storage_sph:input:21, register:storage_sph:input:22, register:storage_sph:input:25, register:storage_sph:input:26, register:storage_sph:input:29, register:storage_sph:input:30, register:storage_sph:input:33, register:storage_sph:input:34 |
| input | 7 | — | unknown | PV2 DC voltage | Vpv2 | register value; /10 | 0.1V | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 8 | — | unknown | PV2 DC current | PV2Curr | register value; /10 | 0.1A | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 9 | pv_total_power | alternate | PV2 DC power | Ppv2H | register value; /10 | 0.1W | R/W | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ; alternates: register:storage_sph:input:1, register:storage_sph:input:2, register:storage_sph:input:5, register:storage_sph:input:6, register:storage_sph:input:10, register:storage_sph:input:13, register:storage_sph:input:14, register:storage_sph:input:17, register:storage_sph:input:18, register:storage_sph:input:21, register:storage_sph:input:22, register:storage_sph:input:25, register:storage_sph:input:26, register:storage_sph:input:29, register:storage_sph:input:30, register:storage_sph:input:33, register:storage_sph:input:34 |
| input | 10 | pv_total_power | alternate | PV2 DC power | Ppv2L | register value; /10 | 0.1W | R/W | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ; alternates: register:storage_sph:input:1, register:storage_sph:input:2, register:storage_sph:input:5, register:storage_sph:input:6, register:storage_sph:input:9, register:storage_sph:input:13, register:storage_sph:input:14, register:storage_sph:input:17, register:storage_sph:input:18, register:storage_sph:input:21, register:storage_sph:input:22, register:storage_sph:input:25, register:storage_sph:input:26, register:storage_sph:input:29, register:storage_sph:input:30, register:storage_sph:input:33, register:storage_sph:input:34 |
| input | 11 | — | unknown | PV3 DC voltage | Vpv3 | register value; /10 | 0.1V | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 12 | — | unknown | PV3 DC current | PV3Curr | register value; /10 | 0.1A | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 13 | pv_total_power | alternate | PV3 DC power | Ppv3H | register value; /10 | 0.1W | R/W | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ; alternates: register:storage_sph:input:1, register:storage_sph:input:2, register:storage_sph:input:5, register:storage_sph:input:6, register:storage_sph:input:9, register:storage_sph:input:10, register:storage_sph:input:14, register:storage_sph:input:17, register:storage_sph:input:18, register:storage_sph:input:21, register:storage_sph:input:22, register:storage_sph:input:25, register:storage_sph:input:26, register:storage_sph:input:29, register:storage_sph:input:30, register:storage_sph:input:33, register:storage_sph:input:34 |
| input | 14 | pv_total_power | alternate | PV3 DC power | Ppv3L | register value; /10 | 0.1W | R/W | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ; alternates: register:storage_sph:input:1, register:storage_sph:input:2, register:storage_sph:input:5, register:storage_sph:input:6, register:storage_sph:input:9, register:storage_sph:input:10, register:storage_sph:input:13, register:storage_sph:input:17, register:storage_sph:input:18, register:storage_sph:input:21, register:storage_sph:input:22, register:storage_sph:input:25, register:storage_sph:input:26, register:storage_sph:input:29, register:storage_sph:input:30, register:storage_sph:input:33, register:storage_sph:input:34 |
| input | 15 | — | unknown | PV4 DC voltage | Vpv4 | register value; /10 | 0.1V | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 16 | — | unknown | PV4 DC current | PV4Curr | register value; /10 | 0.1A | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 17 | pv_total_power | alternate | PV4 DC power | Ppv4H | register value; /10 | 0.1W | R/W | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ; alternates: register:storage_sph:input:1, register:storage_sph:input:2, register:storage_sph:input:5, register:storage_sph:input:6, register:storage_sph:input:9, register:storage_sph:input:10, register:storage_sph:input:13, register:storage_sph:input:14, register:storage_sph:input:18, register:storage_sph:input:21, register:storage_sph:input:22, register:storage_sph:input:25, register:storage_sph:input:26, register:storage_sph:input:29, register:storage_sph:input:30, register:storage_sph:input:33, register:storage_sph:input:34 |
| input | 18 | pv_total_power | alternate | PV4 DC power | Ppv4L | register value; /10 | 0.1W | R/W | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ; alternates: register:storage_sph:input:1, register:storage_sph:input:2, register:storage_sph:input:5, register:storage_sph:input:6, register:storage_sph:input:9, register:storage_sph:input:10, register:storage_sph:input:13, register:storage_sph:input:14, register:storage_sph:input:17, register:storage_sph:input:21, register:storage_sph:input:22, register:storage_sph:input:25, register:storage_sph:input:26, register:storage_sph:input:29, register:storage_sph:input:30, register:storage_sph:input:33, register:storage_sph:input:34 |
| input | 19 | — | unknown | PV5 DC voltage | Vpv5 | register value; /10 | 0.1V | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 20 | — | unknown | PV5 DC current | PV5Curr | register value; /10 | 0.1A | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 21 | pv_total_power | alternate | PV5 DC power | Ppv5H | register value; /10 | 0.1W | R/W | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ; alternates: register:storage_sph:input:1, register:storage_sph:input:2, register:storage_sph:input:5, register:storage_sph:input:6, register:storage_sph:input:9, register:storage_sph:input:10, register:storage_sph:input:13, register:storage_sph:input:14, register:storage_sph:input:17, register:storage_sph:input:18, register:storage_sph:input:22, register:storage_sph:input:25, register:storage_sph:input:26, register:storage_sph:input:29, register:storage_sph:input:30, register:storage_sph:input:33, register:storage_sph:input:34 |
| input | 22 | pv_total_power | alternate | PV5 DC power | Ppv5L | register value; /10 | 0.1W | R/W | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ; alternates: register:storage_sph:input:1, register:storage_sph:input:2, register:storage_sph:input:5, register:storage_sph:input:6, register:storage_sph:input:9, register:storage_sph:input:10, register:storage_sph:input:13, register:storage_sph:input:14, register:storage_sph:input:17, register:storage_sph:input:18, register:storage_sph:input:21, register:storage_sph:input:25, register:storage_sph:input:26, register:storage_sph:input:29, register:storage_sph:input:30, register:storage_sph:input:33, register:storage_sph:input:34 |
| input | 23 | — | unknown | PV6 DC voltage | Vpv6 | register value; /10 | 0.1V | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 24 | — | unknown | PV6 DC current | PV6Curr | register value; /10 | 0.1A | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 25 | pv_total_power | alternate | PV6 DC power | PV6inputpower(high) | register value; /10 | W | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ; alternates: register:storage_sph:input:1, register:storage_sph:input:2, register:storage_sph:input:5, register:storage_sph:input:6, register:storage_sph:input:9, register:storage_sph:input:10, register:storage_sph:input:13, register:storage_sph:input:14, register:storage_sph:input:17, register:storage_sph:input:18, register:storage_sph:input:21, register:storage_sph:input:22, register:storage_sph:input:26, register:storage_sph:input:29, register:storage_sph:input:30, register:storage_sph:input:33, register:storage_sph:input:34 |
| input | 26 | pv_total_power | alternate | PV6 DC power | PV6inputpower(low) | register value; /10 | W | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ; alternates: register:storage_sph:input:1, register:storage_sph:input:2, register:storage_sph:input:5, register:storage_sph:input:6, register:storage_sph:input:9, register:storage_sph:input:10, register:storage_sph:input:13, register:storage_sph:input:14, register:storage_sph:input:17, register:storage_sph:input:18, register:storage_sph:input:21, register:storage_sph:input:22, register:storage_sph:input:25, register:storage_sph:input:29, register:storage_sph:input:30, register:storage_sph:input:33, register:storage_sph:input:34 |
| input | 27 | — | unknown | PV7 DC voltage | PV7voltage | register value; /10 | V | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 28 | — | unknown | PV7 DC current | PV7inputcurrent | register value; /10 | A | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 29 | pv_total_power | alternate | PV7 DC power | PV7inputpower(high) | register value; /10 | W | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ; alternates: register:storage_sph:input:1, register:storage_sph:input:2, register:storage_sph:input:5, register:storage_sph:input:6, register:storage_sph:input:9, register:storage_sph:input:10, register:storage_sph:input:13, register:storage_sph:input:14, register:storage_sph:input:17, register:storage_sph:input:18, register:storage_sph:input:21, register:storage_sph:input:22, register:storage_sph:input:25, register:storage_sph:input:26, register:storage_sph:input:30, register:storage_sph:input:33, register:storage_sph:input:34 |
| input | 30 | pv_total_power | alternate | PV7 DC power | PV7inputpower(low) | register value; /10 | W | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ; alternates: register:storage_sph:input:1, register:storage_sph:input:2, register:storage_sph:input:5, register:storage_sph:input:6, register:storage_sph:input:9, register:storage_sph:input:10, register:storage_sph:input:13, register:storage_sph:input:14, register:storage_sph:input:17, register:storage_sph:input:18, register:storage_sph:input:21, register:storage_sph:input:22, register:storage_sph:input:25, register:storage_sph:input:26, register:storage_sph:input:29, register:storage_sph:input:33, register:storage_sph:input:34 |
| input | 31 | — | unknown | PV8 DC voltage | PV8voltage | register value; /10 | V | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 32 | — | unknown | PV8 DC current | PV8inputcurrent | register value; /10 | A | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 33 | pv_total_power | alternate | PV8 DC power | PV8inputpower(high) | register value; /10 | W | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ; alternates: register:storage_sph:input:1, register:storage_sph:input:2, register:storage_sph:input:5, register:storage_sph:input:6, register:storage_sph:input:9, register:storage_sph:input:10, register:storage_sph:input:13, register:storage_sph:input:14, register:storage_sph:input:17, register:storage_sph:input:18, register:storage_sph:input:21, register:storage_sph:input:22, register:storage_sph:input:25, register:storage_sph:input:26, register:storage_sph:input:29, register:storage_sph:input:30, register:storage_sph:input:34 |
| input | 34 | pv_total_power | alternate | PV8 DC power | PV8inputpower(low) | register value; /10 | W | R | RESOLVED | semantic_correlated, source_claim | ; alternates: register:storage_sph:input:1, register:storage_sph:input:2, register:storage_sph:input:5, register:storage_sph:input:6, register:storage_sph:input:9, register:storage_sph:input:10, register:storage_sph:input:13, register:storage_sph:input:14, register:storage_sph:input:17, register:storage_sph:input:18, register:storage_sph:input:21, register:storage_sph:input:22, register:storage_sph:input:25, register:storage_sph:input:26, register:storage_sph:input:29, register:storage_sph:input:30, register:storage_sph:input:33 |
| input | 35 | — | unknown | AC output power | Outputpower(high) | register value; /10 | W | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 36 | — | unknown | AC output power | Outputpower(low) | register value; /10 | W | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 37 | grid_frequency | alternate | Grid frequency | Gridfrequency | register value; /100 | Hz | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ; alternates: register:storage_sph:holding:62, register:storage_sph:holding:63, register:storage_sph:holding:72, register:storage_sph:holding:73, register:storage_sph:holding:74, register:storage_sph:holding:75, register:storage_sph:holding:78, register:storage_sph:holding:79 |
| input | 38 | — | unknown | AC phase L1 voltage | Three/singlephasegridvoltage | register value; /10 | V | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 39 | — | unknown | AC phase L1 current | Three/singlephasegridoutputcurrent | register value; /10 | A | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 40 | — | unknown | AC phase L1 power | Three/single phase grid output watt VA(high) | register value; /10 | W | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 41 | — | unknown | AC phase L1 power | Three/single phase grid output watt VA(low) | register value; /10 | W | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 42 | — | unknown | AC phase L2 voltage | Threephasegridvoltage | register value; /10 | V | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 43 | — | unknown | AC phase L2 current | Threephasegridoutputcurrent | register value; /10 | A | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 44 | — | unknown | AC phase L2 power | Threephasegridoutputpower(high) | register value; /10 | W | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 45 | — | unknown | AC phase L2 power | Threephasegridoutputpower(low) | register value; /10 | W | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 46 | — | unknown | AC phase L3 voltage | Threephasegridvoltage | register value; /10 | V | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 47 | — | unknown | AC phase L3 current | Threephasegridoutputcurrent | register value; /10 | A | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 48 | ac_phase_l3_power | alternate | AC phase L3 power | Threephasegridoutputpower(high) | register value; /10 | W | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ; alternates: register:storage_sph:input:49 |
| input | 49 | ac_phase_l3_power | alternate | AC phase L3 power | Threephasegridoutputpower(low) | register value; /10 | W | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ; alternates: register:storage_sph:input:48 |
| input | 50 | — | unknown | Vac_RS | Threephasegridvoltage | register value | Linevoltage | R | RESOLVED | semantic_correlated, source_claim | ;  |
| input | 51 | — | unknown | Vac_ST | Threephasegridvoltage | register value | Linevoltage | R | RESOLVED | semantic_correlated, source_claim | ;  |
| input | 52 | — | unknown | Vac_TR | Threephasegridvoltage | register value | Linevoltage | R | RESOLVED | semantic_correlated, source_claim | ;  |
| input | 53 | — | unknown | Output energy today | Todaygenerateenergy(high) | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 54 | — | unknown | Output energy today | Todaygenerateenergy(low) | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 55 | — | unknown | Output energy total | Totalgenerateenergy(high) | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 56 | — | unknown | Output energy total | Totalgenerateenergy(low) | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 57 | inverter_runtime | supported | Run time | Raw counter counts seconds; divide by 7200 to obtain hours. | register value; /7200 | h | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 58 | — | unknown | Run time | Raw counter counts seconds; divide by 7200 to obtain hours. | register value; /7200 | h | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 59 | — | unknown | PV1 energy today | PV1Energytoday(high) | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 60 | — | unknown | PV1 energy today | PV1Energytoday(low) | register value; /10 | kWh | R | RESOLVED | semantic_correlated, source_claim | ;  |
| input | 61 | — | unknown | PV1 energy total | PV1Energytotal(high) | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 62 | — | unknown | PV1 energy total | PV1Energytotal(low) | register value; /10 | kWh | R | RESOLVED | semantic_correlated, source_claim | ;  |
| input | 63 | — | unknown | PV2 energy today | PV2Energytoday(high) | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 64 | — | unknown | PV2 energy today | PV2Energytoday(low) | register value; /10 | kWh | R | RESOLVED | semantic_correlated, source_claim | ;  |
| input | 65 | — | unknown | PV2 energy total | PV2Energytotal(high) | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 66 | — | unknown | PV2 energy total | PV2Energytotal(low) | register value; /10 | kWh | R | RESOLVED | semantic_correlated, source_claim | ;  |
| input | 67 | — | unknown | PV3 energy today | PV3Energytoday(high) | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 68 | — | unknown | PV3 energy today | PV3Energytoday(low) | register value; /10 | kWh | R | RESOLVED | semantic_correlated, source_claim | ;  |
| input | 69 | — | unknown | PV3 energy total | PV3Energytotal(high) | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 70 | — | unknown | PV3 energy total | PV3Energytotal(low) | register value; /10 | kWh | R | RESOLVED | semantic_correlated, source_claim | ;  |
| input | 71 | — | unknown | PV4 energy today | PV4Energytoday(high) | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 72 | — | unknown | PV4 energy today | PV4Energytoday(low) | register value; /10 | kWh | R | RESOLVED | semantic_correlated, source_claim | ;  |
| input | 73 | pv4_energy_total | alternate | PV4 energy total | PV4Energytotal(high) | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ; alternates: register:storage_sph:input:74 |
| input | 74 | pv4_energy_total | alternate | PV4 energy total | PV4Energytotal(low) | register value; /10 | kWh | R | RESOLVED | semantic_correlated, source_claim | ; alternates: register:storage_sph:input:73 |
| input | 75 | — | unknown | PV5 energy today | PV5Energytoday(high) | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 76 | — | unknown | PV5 energy today | PV5Energytoday(low) | register value; /10 | kWh | R | RESOLVED | semantic_correlated, source_claim | ;  |
| input | 77 | — | unknown | PV5 energy total | PV5Energytotal(high) | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 78 | — | unknown | PV5 energy total | PV5Energytotal(low) | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 79 | — | unknown | PV6 energy today | PV6Energytoday(high) | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 80 | — | unknown | PV6 energy today | PV6Energytoday(low) | register value; /10 | kWh | R | RESOLVED | semantic_correlated, source_claim | ;  |
| input | 81 | — | unknown | PV6 energy total | PV6Energytotal(high) | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 82 | — | unknown | PV6 energy total | PV6Energytotal(low) | register value; /10 | kWh | R | RESOLVED | semantic_correlated, source_claim | ;  |
| input | 83 | — | unknown | PV7 energy today | PV7Energytoday(high) | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 84 | — | unknown | PV7 energy today | PV7Energytoday(low) | register value; /10 | kWh | R | RESOLVED | semantic_correlated, source_claim | ;  |
| input | 85 | — | unknown | PV7 energy total | PV7Energytotal(high) | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 86 | — | unknown | PV7 energy total | PV7Energytotal(low) | register value; /10 | kWh | R | RESOLVED | semantic_correlated, source_claim | ;  |
| input | 87 | — | unknown | PV8 energy today | PV8Energytoday(high) | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 88 | — | unknown | PV8 energy today | PV8Energytoday(low) | register value; /10 | kWh | R | RESOLVED | semantic_correlated, source_claim | ;  |
| input | 89 | — | unknown | PV8 energy total | PV8Energytotal(high) | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 90 | — | unknown | PV8 energy total | PV8Energytotal(low) | register value; /10 | kWh | R | RESOLVED | semantic_correlated, source_claim | ;  |
| input | 91 | — | unknown | PV energy total | PVEnergytotal(high) | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 92 | — | unknown | PV energy total | PVEnergytotal(low) | register value; /10 | kWh | R | RESOLVED | semantic_correlated, source_claim | ;  |
| input | 93 | — | unknown | Inverter temperature | Invertertemperature | register value; /10 | °C | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 94 | — | unknown | IPM temperature | TheinsideIPMininverterTemperature | register value; /10 | °C | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 95 | — | unknown | Boost temperature | Boosttemperature | register value; /10 | °C | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 96 | — | unknown | Temp4 | Temp4 | register value | reserved | R | SOURCE_ONLY | source_claim | ;  |
| input | 97 | — | unknown | uwBatVolt_DSP | BatVolt_DSP | register value | BatVolt(DSP) | R | SOURCE_ONLY | source_claim | ;  |
| input | 98 | — | unknown | P-bus voltage | PBusinsideVoltage | register value; /10 | V | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 99 | — | unknown | N-bus voltage | NBusinsideVoltage | register value; /10 | V | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 100 | — | unknown | IPF | InverteroutputPFnow | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 101 | — | unknown | Output power percentage | RealOutputpowerPercent | register value; /10 | % | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 102 | — | unknown | OPFullwattH | OutputMaxpowerLimitedhigh | register value | W | R | RESOLVED | semantic_correlated, source_claim | ;  |
| input | 103 | — | unknown | OPFullwattL | OutputMaxpowerLimitedlow | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 104 | — | unknown | Derating mode | DeratingMode | register value; /10 | — | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 105 | — | unknown | Fault code | Inverterfaultmaincode | register value; /10 | — | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 106 | — | unknown | Register 106 | — | register value | — | R | UNKNOWN_RESERVED | source_claim | ;  |
| input | 107 | — | unknown | FaultSubcode | Inverterfaultsubcode | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 108 | — | unknown | RemoteCtrlEn | / | register value | StoragePow er(SPA) | R | SOURCE_ONLY | source_claim | ;  |
| input | 109 | — | unknown | RemoteCtrlPow er | / | register value | StoragePow er(SPA) | R | SOURCE_ONLY | source_claim | ;  |
| input | 110 | — | unknown | Warning code | WarningbitH | register value; /10 | — | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 111 | — | unknown | Warning code | Inverterwarnsubcode | register value; /10 | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 112 | — | unknown | WarnMaincode | Inverterwarnmaincode | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 113 | — | unknown | real Power Percent | realPowerPercent | register value | MAX | R | SOURCE_ONLY | source_claim | ;  |
| input | 114 | — | unknown | inv start delay time | invstartdelaytime | register value | MAX | R | SOURCE_ONLY | source_claim | ;  |
| input | 115 | — | unknown | bINVAllFaultCod e | bINVAllFaultCode | register value | MAX | R | SOURCE_ONLY | source_claim | ;  |
| input | 116 | — | unknown | AC charge Power_H | Gridpowertolocalload | register value | Storage Power | R | SOURCE_ONLY | source_claim | ;  |
| input | 117 | — | unknown | AC charge Power_L | Gridpowertolocalload | register value | Storage Power | R | SOURCE_ONLY | source_claim | ;  |
| input | 118 | — | unknown | Priority | 0:LoadFirst | register value | Storage | R | RESOLVED | semantic_correlated, source_claim | ;  |
| input | 119 | — | unknown | BatteryType | 0：Lead-acid 1：Lithiumbattery | register value | — | R | RESOLVED | semantic_correlated, source_claim | ;  |
| input | 120 | — | unknown | AutoProofreadC MD | Aging mode Auto-calibration command | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 121 | — | unknown | Register 121 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| input | 122 | — | unknown | Register 122 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| input | 123 | — | unknown | Register 123 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| input | 124 | — | unknown | reserved | reserved | register value | — | R | UNKNOWN_RESERVED | source_claim | ;  |
| input | 1000 | — | unknown | uwSysWorkMode | uwSysWorkMode | register value | — | W | SOURCE_ONLY | source_claim | ;  |
| input | 1001 | — | unknown | Systemfaultword0 | Systemfaultword0 | register value | Please refer to thefault description of Hybrid | R | SOURCE_ONLY | source_claim | ;  |
| input | 1002 | — | unknown | Systemfaultword1 | Systemfaultword1 | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 1003 | — | unknown | Systemfaultword2 | Systemfaultword2 | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 1004 | — | unknown | Systemfaultword3 | Systemfaultword3 | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 1005 | — | unknown | Systemfaultword4 | Systemfaultword4 | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 1006 | — | unknown | Systemfaultword5 | Systemfaultword5 | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 1007 | — | unknown | Systemfaultword6 | Systemfaultword6 | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 1008 | — | unknown | Systemfaultword7 | Systemfaultword7 | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 1009 | battery_discharge_power | supported | Pdischarge1H | Dischargepower(high) | register value; /10 | W | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 1010 | — | unknown | Pdischarge1L | Dischargepower(low) | register value; /10 | W | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 1011 | battery_charge_power | supported | Pcharge1H | Chargepower(high) | register value; /10 | W | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 1012 | — | unknown | Pcharge1L | Chargepower(low) | register value; /10 | W | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 1013 | — | unknown | Vbat | Batteryvoltage | register value | V | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 1014 | battery_soc | supported | SOC | StateofchargeCapacity | register value; /10 | lith/leadacid | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 1015 | — | unknown | PactouserR H | ACpowertouserH | register value | W | R | RESOLVED | semantic_correlated, source_claim | ;  |
| input | 1016 | — | unknown | PactouserR L | ACpowertouserL | register value | W | R | RESOLVED | semantic_correlated, source_claim | ;  |
| input | 1017 | — | unknown | PactouserS H | PactouserS H | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 1018 | — | unknown | PactouserS L | PactouserS L | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 1019 | — | unknown | PactouserT H | PactouserT H | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 1020 | — | unknown | PactouserT L | PactouserT H | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 1021 | — | unknown | PactouserTotalH | ACpowertousertotalH | register value; /10 | W | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 1022 | — | unknown | PactouserTotalL | ACpowertousertotalL | register value; /10 | W | R | RESOLVED | semantic_correlated, source_claim | ;  |
| input | 1023 | — | unknown | PactogridR H | ACpowertogridH | register value | Ac output | R | RESOLVED | semantic_correlated, source_claim | ;  |
| input | 1024 | — | unknown | PactogridR L | ACpowertogridL | register value | W | R | RESOLVED | semantic_correlated, source_claim | ;  |
| input | 1025 | — | unknown | PactogridS H | PactogridS H | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 1026 | — | unknown | PactogridS L | PactogridS L | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 1027 | — | unknown | PactogridTH | 0.1w | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 1028 | — | unknown | PactogridTL | 0.1w | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 1029 | — | unknown | pac_to_grid_total | 0.1w | register value; /10 | W | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 1030 | — | unknown | PactogridtotalL | 0.1w | register value; /10 | W | R | RESOLVED | semantic_correlated, source_claim | ;  |
| input | 1031 | — | unknown | PLocalLoadR H | 0.1w | register value | W | R | RESOLVED | semantic_correlated, source_claim | ;  |
| input | 1032 | — | unknown | PLocalLoadR L | 0.1w | register value | W | R | RESOLVED | semantic_correlated, source_claim | ;  |
| input | 1033 | — | unknown | PLocalLoadS H | 0.1w | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 1034 | — | unknown | PLocalLoadS L | 0.1w | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 1035 | — | unknown | PLocalLoadT H | 0.1w | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 1036 | — | unknown | PLocalLoadT L | 0.1w | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 1037 | — | unknown | PLocalLoadtotalH | 0.1w | register value | W | R | RESOLVED | semantic_correlated, source_claim | ;  |
| input | 1038 | — | unknown | PLocalLoadtotalL | 0.1w | register value | W | R | RESOLVED | semantic_correlated, source_claim | ;  |
| input | 1039 | — | unknown | IP2MTemperature | 0.1℃ | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 1040 | — | unknown | B2attery Temperature | 0.1℃ | register value | °C | R | RESOLVED | semantic_correlated, source_claim | ;  |
| input | 1041 | — | unknown | SPDSPStatus | SPDSPStatus | register value | — | R | RESOLVED | semantic_correlated, source_claim | ;  |
| input | 1042 | — | unknown | SPBusVolt | 0.1V | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 1043 | — | unknown | Register 1043 | — | register value | — | R | UNKNOWN_RESERVED | source_claim | ;  |
| input | 1044 | — | unknown | Etouser_todayH | Etouser_todayH | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 1045 | — | unknown | Etouser_todayL | Etouser_todayL | register value; /10 | kWh | W | RESOLVED | semantic_correlated, source_claim | ;  |
| input | 1046 | — | unknown | Etouser_totalH | Etouser_totalH | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 1047 | — | unknown | Etouser_totalL | Etouser_totalL | register value; /10 | kWh | R | RESOLVED | semantic_correlated, source_claim | ;  |
| input | 1048 | — | unknown | Etogrid_todayH | Etogrid_todayH | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 1049 | — | unknown | Etogrid_todayL | Etogrid_todayL | register value; /10 | kWh | W | RESOLVED | semantic_correlated, source_claim | ;  |
| input | 1050 | — | unknown | Etogrid_totalH | Etogrid_totalH | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 1051 | — | unknown | Etogrid_totalL | Etogrid_totalL | register value; /10 | kWh | R | RESOLVED | semantic_correlated, source_claim | ;  |
| input | 1052 | — | unknown | Edischarge1_toda yH | Edischarge1_toda yH | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 1053 | — | unknown | Edischarge1_toda yL | Edischarge1_toda yL | register value; /10 | kWh | R | RESOLVED | semantic_correlated, source_claim | ;  |
| input | 1054 | — | unknown | Edischarge1_total H | Edischarge1_total H | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 1055 | — | unknown | Edischarge1_total L | Edischarge1_total L | register value; /10 | kWh | W | RESOLVED | semantic_correlated, source_claim | ;  |
| input | 1056 | — | unknown | Echarge1_todayH | Echarge1_todayH | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 1057 | — | unknown | Echarge1_today L | Echarge1_today L | register value; /10 | kWh | R | RESOLVED | semantic_correlated, source_claim | ;  |
| input | 1058 | — | unknown | Echarge1_totalH | Echarge1_totalH | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; ;  |
| input | 1059 | — | unknown | Echarge1_totalL | Echarge1_totalL | register value; /10 | kWh | R | RESOLVED | semantic_correlated, source_claim | ;  |
| input | 1060 | — | unknown | Register 1060 | Localloadenergytoday | register value | kWh | R | UNKNOWN_RESERVED | semantic_correlated, source_claim | ;  |
| input | 1061 | — | unknown | Register 1061 | Localloadenergytoday | register value | kWh | R | UNKNOWN_RESERVED | semantic_correlated, source_claim | ;  |
| input | 1062 | — | unknown | Register 1062 | Localloadenergytotal | register value | kWh | R | UNKNOWN_RESERVED | semantic_correlated, source_claim | ;  |
| input | 1063 | — | unknown | Register 1063 | Localloadenergytotal | register value | kWh | R | UNKNOWN_RESERVED | semantic_correlated, source_claim | ;  |
| input | 1064 | — | unknown | Register 1064 | ExportLimitApparentPowerH | register value | — | W | UNKNOWN_RESERVED | source_claim | ;  |
| input | 1065 | — | unknown | Register 1065 | ExportLimitApparentPowerL | register value | — | W | UNKNOWN_RESERVED | source_claim | ;  |
| input | 1066 | — | unknown | Register 1066 | / | register value | — | R | UNKNOWN_RESERVED | source_claim | ;  |
| input | 1067 | — | unknown | EpsFac | UPSfrequency | register value | — | R | RESOLVED | semantic_correlated, source_claim | ;  |
| input | 1068 | — | unknown | EpsVac1 | UPSphaseRoutputvoltage | register value | — | R | RESOLVED | semantic_correlated, source_claim | ;  |
| input | 1069 | — | unknown | EpsIac1 | UPSphaseRoutputcurrent | register value | — | R | RESOLVED | semantic_correlated, source_claim | ;  |
| input | 1070 | — | unknown | EpsPac1 | UPSphaseRoutputpower(H) | register value | — | R | RESOLVED | semantic_correlated, source_claim | ;  |
| input | 1071 | — | unknown | EpsPac1 | UPSphaseRoutputpower(L) | register value | — | R | RESOLVED | semantic_correlated, source_claim | ;  |
| input | 1072 | — | unknown | EpsVac2 | UPSphaseSoutputvoltage | register value | — | R | RESOLVED | semantic_correlated, source_claim | ;  |
| input | 1073 | — | unknown | EpsIac2 | UPSphaseSoutputcurrent | register value | — | R | RESOLVED | semantic_correlated, source_claim | ;  |
| input | 1074 | — | unknown | EpsPac2 | UPSphaseSoutputpower(H) | register value | — | R | RESOLVED | semantic_correlated, source_claim | ;  |
| input | 1075 | — | unknown | EpsPac2 | UPSphaseSoutputpower(L) | register value | — | R | RESOLVED | semantic_correlated, source_claim | ;  |
| input | 1076 | — | unknown | EpsVac3 | UPSphaseToutputvoltage | register value | — | R | RESOLVED | semantic_correlated, source_claim | ;  |
| input | 1077 | — | unknown | EpsIac3 | UPSphaseToutputcurrent | register value | — | R | RESOLVED | semantic_correlated, source_claim | ;  |
| input | 1078 | — | unknown | EpsPac3 | UPSphaseToutputpower(H) | register value | — | R | RESOLVED | semantic_correlated, source_claim | ;  |
| input | 1079 | — | unknown | EpsPac3 | UPSphaseToutputpower(L) | register value | — | R | RESOLVED | semantic_correlated, source_claim | ;  |
| input | 1080 | — | unknown | EpsLoadPercent | LoadpercentofUPSouput | register value | — | R | RESOLVED | semantic_correlated, source_claim | ;  |
| input | 1081 | — | unknown | EpsPF | Powerfactor | register value | — | R | RESOLVED | semantic_correlated, source_claim | ;  |
| input | 1082 | — | unknown | Register 1082 | StatusOldfromBMS | register value | — | R | UNKNOWN_RESERVED | source_claim | ;  |
| input | 1083 | — | unknown | Register 1083 | StatusfromBMS | register value | — | R | UNKNOWN_RESERVED | source_claim | ;  |
| input | 1084 | — | unknown | Register 1084 | ErrorinfoOldfromBMS | register value | — | R | UNKNOWN_RESERVED | source_claim | ;  |
| input | 1085 | — | unknown | Register 1085 | ErrorinfomationfromBMS | register value | — | R | UNKNOWN_RESERVED | source_claim | ;  |
| input | 1086 | — | unknown | Register 1086 | SOCfromBMS | register value | — | R | UNKNOWN_RESERVED | source_claim | ;  |
| input | 1087 | — | unknown | Register 1087 | BatteryvoltagefromBMS | register value | — | R | UNKNOWN_RESERVED | source_claim | ;  |
| input | 1088 | — | unknown | Register 1088 | BatterycurrentfromBMS | register value | — | R | UNKNOWN_RESERVED | source_claim | ;  |
| input | 1089 | — | unknown | Register 1089 | BatterytemperaturefromBMS | register value | — | R | UNKNOWN_RESERVED | source_claim | ;  |
| input | 1090 | — | unknown | BMS_MaxCurr | Max. charge/discharge current fromBMS(pylon) | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 1091 | — | unknown | BMS_GaugeRM | GaugeRMfromBMS | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 1092 | — | unknown | BMS_GaugeFCC | GaugeFCCfromBMS | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 1093 | — | unknown | BMS_FW | BMS_FW | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 1094 | — | unknown | BMS_DeltaVolt | DeltaVfromBMS | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 1095 | — | unknown | BMS_CycleCnt | CycleCountfromBMS | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 1096 | — | unknown | BMS_SOH | SOHfromBMS | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 1097 | — | unknown | BMS_ConstantV olt | CVvoltagefromBMS | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 1098 | — | unknown | BMS_WarnInfoO ld | WarninginfooldfromBMS | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 1099 | — | unknown | BMS_WarnInfo | WarninginfofromBMS | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 1100 | — | unknown | BMS_GaugeICCu rr | GaugeICcurrentfromBMS | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 1101 | — | unknown | BMS_MCUVersi on | MCUSoftwareversionfromBMS | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 1102 | — | unknown | BMS_GaugeVers ion | GaugeVersionfromBMS | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 1103 | — | unknown | BMS_wGaugeFR Version_L | GaugeFRVersionL16fromBMS | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 1104 | — | unknown | BMS_wGaugeFR Version_H | GaugeFRVersionH16fromBMS | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 1105 | — | unknown | BMS_BMSInfo | BMSInformationfromBMS | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 1106 | — | unknown | BMS_PackInfo | PackInformationfromBMS | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 1107 | — | unknown | BMS_UsingCap | UsingCapfromBMS | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 1108 | — | unknown | uwMaxCellVolt | Maximumsinglebatteryvoltage | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 1109 | — | unknown | uwMinCellVolt | Lowestsinglebatteryvoltage | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 1110 | — | unknown | bModuleNum | Batteryparallelnumber | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 1111 | — | unknown | Numberofbatteries | Numberofbatteries | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 1112 | — | unknown | uwMaxVoltCellN o | MaxVoltCellNo | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 1113 | — | unknown | uwMinVoltCellN o | MinVoltCellNo | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 1114 | — | unknown | uwMaxTemprCe ll_10T | MaxTemprCell_10T | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 1115 | — | unknown | uwMinTemprCel l_10T | MinTemprCell_10T | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 1116 | — | unknown | uwMaxTemprCe llNo | MaxVoltTemprCellNo | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 1117 | — | unknown | uwMinTemprCel | MinVoltTemprCellNo | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 1118 | — | unknown | ProtectpackID | FaultyBatteryAddress | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 1119 | — | unknown | MaxSOC | ParallelmaximumSOC | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 1120 | — | unknown | MinSOC | ParallelminimumSOC | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 1121 | — | unknown | BMS_Error2 | BatteryProtection2 | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 1122 | — | unknown | BMS_Error3 | BatteryProtection3 | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 1123 | — | unknown | BMS_WarnInfo2 | BatteryWarn2 | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 1124 | — | unknown | ACCharge EnergyTodayH | ACChargeEnergytoday | register value | kWh | W | RESOLVED | semantic_correlated, source_claim | ;  |
| input | 1125 | — | unknown | ACCharge EnergyTodayL | ACChargeEnergytoday | register value | kWh | W | RESOLVED | semantic_correlated, source_claim | ;  |
| input | 1126 | — | unknown | A1CCharge EnergyTotalH | A1CCharge EnergyTotalH | register value | kWh | R | RESOLVED | semantic_correlated, source_claim | ;  |
| input | 1127 | — | unknown | ACCharge EnergyTotalL | ACCharge EnergyTotalL | register value | kWh | R | RESOLVED | semantic_correlated, source_claim | ;  |
| input | 1128 | — | unknown | AC Charge Power H | ACChargePower | register value | — | W | SOURCE_ONLY | source_claim | ;  |
| input | 1129 | — | unknown | AC Charge PowerL | ACChargePower | register value | — | W | SOURCE_ONLY | source_claim | ;  |
| input | 1130 | — | unknown | 70% INV Power adjust | uwGridPower_70_AdjEE_SP | register value | — | W | SOURCE_ONLY | source_claim | ;  |
| input | 1131 | — | unknown | Extra AC Power to grid_H | ExtrainverteACPowertogrid High | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 1132 | — | unknown | Extra AC Power to grid_L | ExtrainverteACPowertogridLow | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 1133 | — | unknown | Eextra_todayH | ExtrainverterPowerTOUser_Extra today(high) | register value | 0.1kWh | R | SOURCE_ONLY | source_claim | ;  |
| input | 1134 | — | unknown | Eextra_todayL | ExtrainverterPowerTOUser_Extra today(low) | register value | 0.1kWh | R | SOURCE_ONLY | source_claim | ;  |
| input | 1135 | — | unknown | Eextra_totalH | ExtrainverterPowerTOUser_Extra total(high) | register value | 0.1kWh | R | SOURCE_ONLY | source_claim | ;  |
| input | 1136 | — | unknown | Eextra_totalL | ExtrainverterPowerTOUser_Extra total(low) | register value | 0.1kWh | R | SOURCE_ONLY | source_claim | ;  |
| input | 1137 | — | unknown | Esystem_today H | SystemelectricenergytodayH | register value | 0.1kWh | R | SOURCE_ONLY | source_claim | ;  |
| input | 1138 | — | unknown | Esystem_ today L | SystemelectricenergytodayL | register value | SPA used System electric energytodayL | R | SOURCE_ONLY | source_claim | ;  |
| input | 1139 | — | unknown | Esystem_totalH | SystemelectricenergytotalH | register value | SPA used System electric energytotalH | R | SOURCE_ONLY | source_claim | ;  |
| input | 1140 | — | unknown | Esystem_totalL | SystemelectricenergytotalL | register value | SPA used System electric energytotalL | R | SOURCE_ONLY | source_claim | ;  |
| input | 1141 | — | unknown | Eself_todayH | selfelectricenergytodayH | register value | self electric energytodayH | R | SOURCE_ONLY | source_claim | ;  |
| input | 1142 | — | unknown | Eself_todayL | selfelectricenergytodayL | register value | self electric energytodayL | R | SOURCE_ONLY | source_claim | ;  |
| input | 1143 | — | unknown | Eself_totalH | selfelectricenergytotalH | register value | self electric energytotalH | R | SOURCE_ONLY | source_claim | ;  |
| input | 1144 | — | unknown | Eself_totalL | selfelectricenergytotalL | register value | self electric energytotalL | R | SOURCE_ONLY | source_claim | ;  |
| input | 1145 | — | unknown | PSystemH | SystempowerH | register value | SystempowerH | R | SOURCE_ONLY | source_claim | ;  |
| input | 1146 | — | unknown | PSystemL | SystempowerL | register value | SystempowerL | R | SOURCE_ONLY | source_claim | ;  |
| input | 1147 | — | unknown | PSelfH | selfpowerH | register value | selfpowerH | R | SOURCE_ONLY | source_claim | ;  |
| input | 1148 | — | unknown | PSelfL | selfpowerL | register value | selfpowerL | R | SOURCE_ONLY | source_claim | ;  |
| input | 1149 | — | unknown | EPVAll_TodayH | PVelectricenergytodayH | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 1150 | — | unknown | EPVAll_TodayL | PVelectricenergytodayL | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 1151 | — | unknown | AcDischarge PackSn | Discharge power pack serial number | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 1152 | — | unknown | Accdischarge power_H | Cumulative discharge power high 16-bitbyte | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 1153 | — | unknown | Accdischarge power_L | Cumulative discharge power low 16-bitbyte | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 1154 | — | unknown | AccCharge PackSn | chargepowerpackserialnumber | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 1155 | — | unknown | AccCharge power_H | Cumulative charge power high 16-bitbyte | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 1156 | — | unknown | AccCharge power_L | Cumulative charge power low 16-bitbyte | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 1157 | — | unknown | FirstBattFaultSn | FirstBattFaultSn | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 1158 | — | unknown | Second BattFaultSn | Second BattFaultSn | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 1159 | — | unknown | Third BattFaultSn | Third BattFaultSn | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 1160 | — | unknown | Fourth BattFaultSn | Fourth BattFaultSn | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 1161 | — | unknown | Batteryhistory faultcode1 | Batteryhistoryfaultcode1 | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 1162 | — | unknown | Batteryhistory faultcode2 | Batteryhistoryfaultcode2 | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 1163 | — | unknown | Batteryhistory faultcode3 | Batteryhistoryfaultcode3 | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 1164 | — | unknown | Batteryhistory faultcode4 | Batteryhistoryfaultcode4 | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 1165 | — | unknown | Batteryhistory faultcode5 | Batteryhistoryfaultcode5 | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 1166 | — | unknown | Batteryhistory faultcode6 | Batteryhistoryfaultcode6 | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 1167 | — | unknown | Batteryhistory faultcode7 | Batteryhistoryfaultcode7 | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 1168 | — | unknown | Batteryhistory faultcode8 | Batteryhistoryfaultcode8 | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 1169 | — | unknown | Number of battery codes | Number of battery codes PACK number + BIC forward and reversecodes | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 1170 | — | unknown | Register 1170 | — | register value | — | R | UNKNOWN_RESERVED | source_claim | ;  |
| input | 1171 | — | unknown | Register 1171 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| input | 1172 | — | unknown | Register 1172 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| input | 1173 | — | unknown | Register 1173 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| input | 1174 | — | unknown | Register 1174 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| input | 1175 | — | unknown | Register 1175 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| input | 1176 | — | unknown | Register 1176 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| input | 1177 | — | unknown | Register 1177 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| input | 1178 | — | unknown | Register 1178 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| input | 1179 | — | unknown | Register 1179 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| input | 1180 | — | unknown | Register 1180 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| input | 1181 | — | unknown | Register 1181 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| input | 1182 | — | unknown | Register 1182 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| input | 1183 | — | unknown | Register 1183 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| input | 1184 | — | unknown | Register 1184 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| input | 1185 | — | unknown | Register 1185 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| input | 1186 | — | unknown | Register 1186 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| input | 1187 | — | unknown | Register 1187 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| input | 1188 | — | unknown | Register 1188 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| input | 1189 | — | unknown | Register 1189 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| input | 1190 | — | unknown | Register 1190 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| input | 1191 | — | unknown | Register 1191 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| input | 1192 | — | unknown | Register 1192 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| input | 1193 | — | unknown | Register 1193 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| input | 1194 | — | unknown | Register 1194 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| input | 1195 | — | unknown | Register 1195 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| input | 1196 | — | unknown | Register 1196 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| input | 1197 | — | unknown | Register 1197 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| input | 1198 | — | unknown | Register 1198 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| input | 1199 | — | unknown | NewEPowerCalc Flag | Intelligent reading is used to identify software compatibility features | register value | 0 ： Old energy calculation； 1 ： new energy calculation | R | SOURCE_ONLY | source_claim | ;  |
| input | 1200 | — | unknown | MaxCellVolt | Maximumcellvoltage | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 1201 | — | unknown | MinCellVolt | Minimumcellvoltage | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 1202 | — | unknown | ModuleNum | NumberofBatterymodules | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 1203 | — | unknown | TotalCellNum | Totalnumberofcells | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 1204 | — | unknown | MaxVoltCellNo | MaxVoltCellNo | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 1205 | — | unknown | MinVoltCellNo | MinVoltCellNo | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 1206 | — | unknown | MaxTemprCell_ 10T | MaxTemprCell_10T | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 1207 | — | unknown | MinTemprCell_1 0T | MinTemprCell_10T | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 1208 | — | unknown | MaxTemprCellN o | MaxTemprCellNo | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 1209 | — | unknown | MinTemprCellN o | MinTemprCellNo | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 1210 | — | unknown | ProtectPackID | FaultPackID | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 1211 | — | unknown | MaxSOC | ParallelmaximumSOC | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 1212 | — | unknown | MinSOC | ParallelminimumSOC | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 1213 | — | unknown | BatProtect1Add | BatProtect1Add | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 1214 | — | unknown | BatProtect2Add | BatProtect2Add | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 1215 | — | unknown | BatWarn1Add | BatWarn1Add | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 1216 | — | unknown | BMS_HighestSof tVersion | BMS_HighestSoftVersion | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 1217 | — | unknown | BMS_Hardware Version | BMS_HardwareVersion | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 1218 | — | unknown | BMS_RequestTy pe | BMS_RequestType | register value | — | R | SOURCE_ONLY | source_claim | ;  |
| input | 1219 | — | unknown | Register 1219 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| input | 1220 | — | unknown | Register 1220 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| input | 1221 | — | unknown | Register 1221 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| input | 1222 | — | unknown | Register 1222 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| input | 1223 | — | unknown | Register 1223 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| input | 1224 | — | unknown | Register 1224 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| input | 1225 | — | unknown | Register 1225 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| input | 1226 | — | unknown | Register 1226 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| input | 1227 | — | unknown | Register 1227 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| input | 1228 | — | unknown | Register 1228 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| input | 1229 | — | unknown | Register 1229 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| input | 1230 | — | unknown | Register 1230 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| input | 1231 | — | unknown | Register 1231 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| input | 1232 | — | unknown | Register 1232 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| input | 1233 | — | unknown | Register 1233 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| input | 1234 | — | unknown | Register 1234 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| input | 1235 | — | unknown | Register 1235 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| input | 1236 | — | unknown | Register 1236 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| input | 1237 | — | unknown | Register 1237 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| input | 1238 | — | unknown | Register 1238 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| input | 1239 | — | unknown | Register 1239 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| input | 1240 | — | unknown | Register 1240 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| input | 1241 | — | unknown | Register 1241 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| input | 1242 | — | unknown | Register 1242 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| input | 1243 | — | unknown | Register 1243 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| input | 1244 | — | unknown | Register 1244 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| input | 1245 | — | unknown | Register 1245 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| input | 1246 | — | unknown | Register 1246 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| input | 1247 | — | unknown | Register 1247 | — | register value | — | R | UNKNOWN_RESERVED | — | ;  |
| input | 1248 | — | unknown | bKeyAgingTestO kFlag | Success sign of key detection beforeaging | register value | 1：Finishedtest 0 ： test not completed | R | SOURCE_ONLY | source_claim | ;  |
| input | 1249 | — | unknown | / | / | register value | reversed | R | SOURCE_ONLY | source_claim | ;  |

### Older inverter / 3.15 family

Source-only external layout coverage; no live hardware resolution is claimed.

| Table | Address | Semantic | Role | Name | Description | Encoding / scale | Unit | Access | Status | Evidence | Notes |
|---|---:|---|---|---|---|---|---|---|---|---|---|
| input | 0 | — | unknown | InverterStatus | InverterStatus | register value | — | UNKNOWN | SOURCE_ONLY | source_claim | ;  |
| input | 1 | — | unknown | DcPower | DcPower | register value | W | UNKNOWN | SOURCE_ONLY | source_claim | ;  |
| input | 3 | — | unknown | DcVoltage | DcVoltage | register value | V | UNKNOWN | SOURCE_ONLY | source_claim | ;  |
| input | 4 | — | unknown | DcInputCurrent | DcInputCurrent | register value | A | UNKNOWN | SOURCE_ONLY | source_claim | ;  |
| input | 13 | — | unknown | AcFrequency | AcFrequency | register value | Hz | UNKNOWN | SOURCE_ONLY | source_claim | ;  |
| input | 14 | — | unknown | AcVoltage | AcVoltage | register value | V | UNKNOWN | SOURCE_ONLY | source_claim | ;  |
| input | 15 | — | unknown | AcOutputCurrent | AcOutputCurrent | register value | A | UNKNOWN | SOURCE_ONLY | source_claim | ;  |
| input | 16 | — | unknown | AcPower | AcPower | register value | W | UNKNOWN | SOURCE_ONLY | source_claim | ;  |
| input | 26 | — | unknown | EnergyToday | EnergyToday | register value | kWh | UNKNOWN | SOURCE_ONLY | source_claim | ;  |
| input | 28 | — | unknown | EnergyTotal | EnergyTotal | register value | kWh | UNKNOWN | SOURCE_ONLY | source_claim | ;  |
| input | 30 | — | unknown | OperatingTime | OperatingTime | register value | s | UNKNOWN | SOURCE_ONLY | source_claim | ;  |
| input | 32 | — | unknown | Temperature | Temperature | register value | °C | UNKNOWN | SOURCE_ONLY | source_claim | ;  |

### SPF off-grid / hybrid

Source-only external layout coverage; no live hardware resolution is claimed.

| Table | Address | Semantic | Role | Name | Description | Encoding / scale | Unit | Access | Status | Evidence | Notes |
|---|---:|---|---|---|---|---|---|---|---|---|---|
| input | 0 | — | unknown | InverterStatus | InverterStatus | register value | — | UNKNOWN | SOURCE_ONLY | source_claim | ;  |
| input | 1 | — | unknown | PV1Voltage | PV1Voltage | register value | V | UNKNOWN | SOURCE_ONLY | source_claim | ;  |
| input | 2 | — | unknown | PV2Voltage | PV2Voltage | register value | V | UNKNOWN | SOURCE_ONLY | source_claim | ;  |
| input | 3 | — | unknown | PV1ChargePwr | PV1ChargePwr | register value | W | UNKNOWN | SOURCE_ONLY | source_claim | ;  |
| input | 5 | — | unknown | PV2ChargePwr | PV2ChargePwr | register value | W | UNKNOWN | SOURCE_ONLY | source_claim | ;  |
| input | 7 | — | unknown | Buck1Current | Buck1Current | register value | A | UNKNOWN | SOURCE_ONLY | source_claim | ;  |
| input | 8 | — | unknown | Buck2Current | Buck2Current | register value | A | UNKNOWN | SOURCE_ONLY | source_claim | ;  |
| input | 9 | — | unknown | OutActivePwr | OutActivePwr | register value | W | UNKNOWN | SOURCE_ONLY | source_claim | ;  |
| input | 11 | — | unknown | OutVA | OutVA | register value | VA | UNKNOWN | SOURCE_ONLY | source_claim | ;  |
| input | 13 | — | unknown | ACChargePwr | ACChargePwr | register value | W | UNKNOWN | SOURCE_ONLY | source_claim | ;  |
| input | 15 | — | unknown | ACChargeVA | ACChargeVA | register value | VA | UNKNOWN | SOURCE_ONLY | source_claim | ;  |
| input | 17 | — | unknown | BattVoltage | BattVoltage | register value | V | UNKNOWN | SOURCE_ONLY | source_claim | ;  |
| input | 18 | — | unknown | BattSOC | BattSOC | register value | % | UNKNOWN | SOURCE_ONLY | source_claim | ;  |
| input | 19 | — | unknown | BusVoltage | BusVoltage | register value | V | UNKNOWN | SOURCE_ONLY | source_claim | ;  |
| input | 20 | — | unknown | GridInVoltage | GridInVoltage | register value | V | UNKNOWN | SOURCE_ONLY | source_claim | ;  |
| input | 21 | — | unknown | LineFrequency | LineFrequency | register value | Hz | UNKNOWN | SOURCE_ONLY | source_claim | ;  |
| input | 22 | — | unknown | OutVoltage | OutVoltage | register value | V | UNKNOWN | SOURCE_ONLY | source_claim | ;  |
| input | 23 | — | unknown | OutFrequency | OutFrequency | register value | Hz | UNKNOWN | SOURCE_ONLY | source_claim | ;  |
| input | 24 | — | unknown | OutDCVoltage | OutDCVoltage | register value | V | UNKNOWN | SOURCE_ONLY | source_claim | ;  |
| input | 25 | — | unknown | InverterTemp | InverterTemp | register value | °C | UNKNOWN | SOURCE_ONLY | source_claim | ;  |
| input | 26 | — | unknown | DCDCTemp | DCDCTemp | register value | °C | UNKNOWN | SOURCE_ONLY | source_claim | ;  |
| input | 27 | — | unknown | LoadPercent | LoadPercent | register value | % | UNKNOWN | SOURCE_ONLY | source_claim | ;  |
| input | 32 | — | unknown | Buck1Temp | Buck1Temp | register value | °C | UNKNOWN | SOURCE_ONLY | source_claim | ;  |
| input | 33 | — | unknown | Buck2Temp | Buck2Temp | register value | °C | UNKNOWN | SOURCE_ONLY | source_claim | ;  |
| input | 36 | — | unknown | ACInPwr | ACInPwr | register value | W | UNKNOWN | SOURCE_ONLY | source_claim | ;  |
| input | 38 | — | unknown | ACInVA | ACInVA | register value | VA | UNKNOWN | SOURCE_ONLY | source_claim | ;  |
| input | 77 | — | unknown | BattPwr | BattPwr | register value | W | UNKNOWN | SOURCE_ONLY | source_claim | ;  |

## Remaining gaps

- MIN/TL-XH is materially stronger than the other families because it has model-specific live reads; the other families are primarily source/correlation based.
- No register has genuine write-accepted, write-reversible or behavior-verified evidence in this release.
- Some vendor, Grott and external layouts use different width/signedness conventions; alternatives and conflicts remain attached to the JSON records.
- Shine/proprietary protocol traffic and broker transport behavior are intentionally outside this register-reference release.

Original evidence files are retained in `doc/` and the local research checkouts; this generated reference is the recommended normal lookup.
