# Growatt resolved register reference

> This file is generated from `doc/growatt_register_reference.json`. The JSON file is the primary machine-readable public reference; the original vendor, runtime, external and live-evidence files remain the provenance corpus.

Reference version: `2026.09-resolved`  
Records: **4047** (1805 holding, 2242 input)  
Live read verified: **60**  
Write verified: **0** (the current hardware evidence is read-only)

## Family overview

| Family | Holding coverage | Input coverage | Resolution quality | Live validation |
|---|---:|---:|---|---:|
| MIN / TL-XH | 415 | 479 | RESOLVED=82, RESOLVED_WITH_NOTES=287, SOURCE_ONLY=377, UNKNOWN_RESERVED=148 | 60 |
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

## Register tables by family

### MIN / TL-XH

Best-supported model family; MIN 6000TL-XH is live read validated.

| Table | Address | Name | Description | Encoding / scale | Unit | Access | Status | Evidence | Notes |
|---|---:|---|---|---|---|---|---|---|---|
| holding | 0 | Inverter enable flags | Inverter enable flags | u16 bitfield | — | R/W | RESOLVED_WITH_NOTES | read_verified, semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| holding | 1 | Safety function enable flags | SPI: system protection interface Bit0~3:forCEI0-21 Bit4~6:forSAA | register value | — | W | SOURCE_ONLY | source_claim | — |
| holding | 2 | Persist power-factor commands | Means these settings will be acting or not when next poweron | register value | — | W | RESOLVED | semantic_correlated, source_claim | — |
| holding | 3 | Active power limit setpoint | 255:powerisnotbelimited | register value; /1 | % | W | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| holding | 4 | Reactive power limit setpoint | 255:powerisnotbelimited | register value; /1 | % | W | SOURCE_ONLY | source_claim | — |
| holding | 5 | Power factor target | Inverter output power factor’s10000times | register value; /10000 | pf | W | SOURCE_ONLY | source_claim | — |
| holding | 6 | Rated apparent power | Normal power(high) | register value; /10 | 0.1VA | R | SOURCE_ONLY | source_claim | — |
| holding | 7 | Rated apparent power | Normal power(low) | register value; /10 | 0.1VA | R | SOURCE_ONLY | source_claim | — |
| holding | 8 | Nominal PV voltage | NormalworkPV voltage | register value; /10 | 0.1V | R | SOURCE_ONLY | source_claim | — |
| holding | 9 | Firmware | Firmwareversion (high) | firmware_version; /10 | ASCII | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| holding | 10 | Firmware | Firmwareversion (middle) | register value | ASCII | R | SOURCE_ONLY | source_claim | — |
| holding | 11 | Firmware | Firmwareversion(low) | register value | ASCII | R | SOURCE_ONLY | source_claim | — |
| holding | 12 | Firmware | ControlFirmware version(high) | register value | ASCII | R | SOURCE_ONLY | source_claim | — |
| holding | 13 | Firmware | ControlFirmware version(middle) | register value | ASCII | R | SOURCE_ONLY | source_claim | — |
| holding | 14 | Firmware | ControlFirmware version(low) | register value | ASCII | R | SOURCE_ONLY | source_claim | — |
| holding | 15 | LCD language selection | 0:Italian; 1:English; 2:German; 3:Spanish; 4:French; 5:Chinese; 6：Polish 7：Portugues 8：Hungary | register value | — | W | SOURCE_ONLY | source_claim | — |
| holding | 16 | Country profile configured | CountrySelectedor not | register value | — | W | SOURCE_ONLY | source_claim | — |
| holding | 17 | PV start voltage threshold | Inputstartvoltage | register value; /10 | 0.1V | W | SOURCE_ONLY | source_claim | — |
| holding | 18 | Start-up delay | Starttime | register value; /1 | 1s | W | SOURCE_ONLY | source_claim | — |
| holding | 19 | Restart delay | RestartDelayTime afterfaultback; | register value; /1 | 1s | W | SOURCE_ONLY | source_claim | — |
| holding | 20 | Active power ramp rate (startup) | Powerstartslope | register value; /10 | 0.1% | W | SOURCE_ONLY | source_claim | — |
| holding | 21 | Active power ramp rate (restart) | Powerrestartslope | register value; /10 | 0.1% | W | SOURCE_ONLY | source_claim | — |
| holding | 22 | Modbus RTU baud rate | Select communicationbaudrat e 0:9600bps 1:38400bps | register value | — | W | SOURCE_ONLY | source_claim | — |
| holding | 23 | Inverter serial number | Inverter serial number | ASCII, 10 characters | ASCII | R | RESOLVED_WITH_NOTES | read_verified, semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| holding | 24 | Serial Number | The Home Assistant integration exposes this as the device serial number and reuses it as the unique identifier. | register value | ASCII | R | SOURCE_ONLY | source_claim | — |
| holding | 25 | Serial Number | The Home Assistant integration exposes this as the device serial number and reuses it as the unique identifier. | register value | ASCII | R | SOURCE_ONLY | source_claim | — |
| holding | 26 | Serial Number | The Home Assistant integration exposes this as the device serial number and reuses it as the unique identifier. | register value | ASCII | R | SOURCE_ONLY | source_claim | — |
| holding | 27 | Serial Number | The Home Assistant integration exposes this as the device serial number and reuses it as the unique identifier. | register value | ASCII | R | SOURCE_ONLY | source_claim | — |
| holding | 28 | Inverter Model | Home Assistant renders this value as the string A# B# D# T# P# U# M# S# via the integration's model() helper. Vendor spec lists value pattern `&*5`; digits appear to be stored without the leading letter codes, so treat as encoded tokens until verified on hardware. | register value; /10 | — | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| holding | 29 | Inverter Model | Home Assistant renders this value as the string A# B# D# T# P# U# M# S# via the integration's model() helper. Vendor spec lists value pattern `&*5`; digits appear to be stored without the leading letter codes, so treat as encoded tokens until verified on hardware. | register value | — | R | SOURCE_ONLY | source_claim | — |
| holding | 30 | Modbus slave address | Communicate address | register value | — | W | SOURCE_ONLY | source_claim | — |
| holding | 31 | Firmware update trigger | Updatefirmware | register value | — | W | SOURCE_ONLY | source_claim | — |
| holding | 32 | Reset user configuration | Use with caution; the inverter immediately reboots and loses provisioning data. | register value | — | W | SOURCE_ONLY | source_claim | — |
| holding | 33 | Factory reset | Equivalent to the front-panel factory reset. Requires re-commissioning afterwards. | register value | — | W | SOURCE_ONLY | source_claim | — |
| holding | 34 | Manufacturer information string | The original table lists these words as Manufacturer Info 8-1 (high/middle/low); combine them to read the full string. | register value | ASCII | R | SOURCE_ONLY | source_claim | — |
| holding | 35 | Manufacturer information string | The original table lists these words as Manufacturer Info 8-1 (high/middle/low); combine them to read the full string. | register value | ASCII | R | SOURCE_ONLY | source_claim | — |
| holding | 36 | Manufacturer information string | The original table lists these words as Manufacturer Info 8-1 (high/middle/low); combine them to read the full string. | register value | ASCII | R | SOURCE_ONLY | source_claim | — |
| holding | 37 | Manufacturer information string | The original table lists these words as Manufacturer Info 8-1 (high/middle/low); combine them to read the full string. | register value | ASCII | R | SOURCE_ONLY | source_claim | — |
| holding | 38 | Manufacturer information string | The original table lists these words as Manufacturer Info 8-1 (high/middle/low); combine them to read the full string. | register value | ASCII | R | SOURCE_ONLY | source_claim | — |
| holding | 39 | Manufacturer information string | The original table lists these words as Manufacturer Info 8-1 (high/middle/low); combine them to read the full string. | register value | ASCII | R | SOURCE_ONLY | source_claim | — |
| holding | 40 | Manufacturer information string | The original table lists these words as Manufacturer Info 8-1 (high/middle/low); combine them to read the full string. | register value | ASCII | R | SOURCE_ONLY | source_claim | — |
| holding | 41 | Manufacturer information string | The original table lists these words as Manufacturer Info 8-1 (high/middle/low); combine them to read the full string. | register value | ASCII | R | SOURCE_ONLY | source_claim | — |
| holding | 42 | G100 failsafe enable | EnglishG100failsafeset | register value | — | W | SOURCE_ONLY | source_claim | — |
| holding | 43 | Device type code | Device type code | vendor encoded | — | R | RESOLVED_WITH_NOTES | read_verified, semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| holding | 44 | Trackers and phases | Trackers and phases | high byte trackers, low byte phases | — | R | RESOLVED_WITH_NOTES | read_verified, semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| holding | 45 | System clock year | Localtime | register value | — | W | SOURCE_ONLY | source_claim | — |
| holding | 46 | System clock month | Systemtime-Month | register value | — | W | SOURCE_ONLY | source_claim | — |
| holding | 47 | System clock day | Systemtime-Day | register value | — | W | SOURCE_ONLY | source_claim | — |
| holding | 48 | System clock hour | Systemtime-Hour | register value | — | W | SOURCE_ONLY | source_claim | — |
| holding | 49 | System clock minute | Systemtime-Min | register value | — | W | SOURCE_ONLY | source_claim | — |
| holding | 50 | System clock second | Systemtime-Second | register value | — | W | SOURCE_ONLY | source_claim | — |
| holding | 51 | System clock weekday | SystemWeekly | register value | — | W | SOURCE_ONLY | source_claim | — |
| holding | 52 | Stage 1 undervoltage limit | Gridvoltagelowlimit protect | register value | 0.1V | W | SOURCE_ONLY | source_claim | — |
| holding | 53 | Stage 1 overvoltage limit | Gridvoltagehighlimit protect | register value | 0.1V | W | SOURCE_ONLY | source_claim | — |
| holding | 54 | Stage 1 underfrequency limit | Gridfrequencylow limitprotect | register value | 0.01 Hz | W | SOURCE_ONLY | source_claim | — |
| holding | 55 | Stage 1 overfrequency limit | Gridhigh frequencylimitprotect | register value | 0.01 Hz | W | SOURCE_ONLY | source_claim | — |
| holding | 56 | Stage 2 undervoltage limit | Gridvoltagelowlimit protect2 | register value | 0.1V | W | SOURCE_ONLY | source_claim | — |
| holding | 57 | Stage 2 overvoltage limit | Gridvoltagehighlimit protect2 | register value | 0.1V | W | SOURCE_ONLY | source_claim | — |
| holding | 58 | Stage 2 underfrequency limit | Gridfrequencylow limitprotect2 | register value | 0.01 Hz | W | SOURCE_ONLY | source_claim | — |
| holding | 59 | Stage 2 overfrequency limit | Gridhighfrequency limitprotect2 | register value | 0.01 Hz | W | SOURCE_ONLY | source_claim | — |
| holding | 60 | Stage 3 undervoltage limit | Grid voltage low limit protect3 | register value | 0.1V | W | SOURCE_ONLY | source_claim | — |
| holding | 61 | Stage 3 overvoltage limit | Grid voltage high limit protect3 | register value | 0.1V | W | SOURCE_ONLY | source_claim | — |
| holding | 62 | Stage 3 underfrequency limit | Grid frequency low limitprotect3 | register value | 0.01Hz | W | SOURCE_ONLY | source_claim | — |
| holding | 63 | Stage 3 overfrequency limit | Grid frequency high limitprotect3 | register value | 0.01Hz | W | SOURCE_ONLY | source_claim | — |
| holding | 64 | Reconnect undervoltage limit | Gridlowvoltagelimit connecttoGrid | register value | 0.1V | W | SOURCE_ONLY | source_claim | — |
| holding | 65 | Reconnect overvoltage limit | Gridhighvoltagelimit connecttoGrid | register value | 0.1V | W | SOURCE_ONLY | source_claim | — |
| holding | 66 | Reconnect underfrequency limit | Gridlowfrequency | register value | 0.01 | W | SOURCE_ONLY | source_claim | — |
| holding | 67 | Reconnect overfrequency limit | Gridhighfrequency limitconnecttoGrid | register value | 0.01 Hz | W | SOURCE_ONLY | source_claim | — |
| holding | 68 | Stage 1 undervoltage trip delay | Grid voltage low limit protecttime 1 | register value | Cycle | W | SOURCE_ONLY | source_claim | — |
| holding | 69 | Stage 1 overvoltage trip delay | Grid voltage high limit protecttime 1 | register value | Cycle | W | SOURCE_ONLY | source_claim | — |
| holding | 70 | Stage 2 undervoltage trip delay | Grid voltage low limit protecttime 2 | register value | Cycle | W | SOURCE_ONLY | source_claim | — |
| holding | 71 | Stage 2 overvoltage trip delay | Grid voltage high limit protecttime 2 | register value | Cycle | W | SOURCE_ONLY | source_claim | — |
| holding | 72 | Stage 1 underfrequency trip delay | Grid frequency low limitprotecttime 1 | register value | Cycle | W | SOURCE_ONLY | source_claim | — |
| holding | 73 | Modbus Version | Grid frequency high limitprotecttime 1 | register value | Cycle | W | SOURCE_ONLY | source_claim | — |
| holding | 74 | Stage 2 underfrequency trip delay | Grid frequency low limitprotecttime 2 | register value | Cycle | W | SOURCE_ONLY | source_claim | — |
| holding | 75 | Stage 2 overfrequency trip delay | Grid frequency high limitprotecttime 2 | register value | Cycle | W | SOURCE_ONLY | source_claim | — |
| holding | 76 | Stage 3 undervoltage trip delay | Grid voltage low limit protecttime 3 | register value | Cycle | W | SOURCE_ONLY | source_claim | — |
| holding | 77 | Stage 3 overvoltage trip delay | Grid voltage high limit protecttime 3 | register value | Cycle | W | SOURCE_ONLY | source_claim | — |
| holding | 78 | Stage 3 underfrequency trip delay | Grid frequency low limitprotecttime 3 | register value | Cycle | W | SOURCE_ONLY | source_claim | — |
| holding | 79 | Stage 3 overfrequency trip delay | Grid frequency high limitprotecttime 3 | register value | Cycle | W | SOURCE_ONLY | source_claim | — |
| holding | 80 | Ten-minute overvoltage limit | Voltprotectionfor10 min | register value | 0.1V | W | SOURCE_ONLY | source_claim | — |
| holding | 81 | PV input high-voltage fault | PVVoltageHigh Fault | register value | 0.1V | W | SOURCE_ONLY | source_claim | — |
| holding | 82 | Controller firmware build string | Positions: 0-1 model letters, 2-3 model variant, 4-5 DSP1 build, 6-7 DSP2/M0 build, 8-9 CPLD/AFCI build, 10-11 M3 build. | register value | ASCII | R | SOURCE_ONLY | source_claim | — |
| holding | 83 | Controller firmware build string | Positions: 0-1 model letters, 2-3 model variant, 4-5 DSP1 build, 6-7 DSP2/M0 build, 8-9 CPLD/AFCI build, 10-11 M3 build. | register value | ASCII | R | SOURCE_ONLY | source_claim | — |
| holding | 84 | Controller firmware build string | Positions: 0-1 model letters, 2-3 model variant, 4-5 DSP1 build, 6-7 DSP2/M0 build, 8-9 CPLD/AFCI build, 10-11 M3 build. | register value | ASCII | R | SOURCE_ONLY | source_claim | — |
| holding | 85 | Controller firmware build string | Positions: 0-1 model letters, 2-3 model variant, 4-5 DSP1 build, 6-7 DSP2/M0 build, 8-9 CPLD/AFCI build, 10-11 M3 build. | register value | ASCII | R | SOURCE_ONLY | source_claim | — |
| holding | 86 | Controller firmware build string | Positions: 0-1 model letters, 2-3 model variant, 4-5 DSP1 build, 6-7 DSP2/M0 build, 8-9 CPLD/AFCI build, 10-11 M3 build. | register value | ASCII | R | SOURCE_ONLY | source_claim | — |
| holding | 87 | Controller firmware build string | Positions: 0-1 model letters, 2-3 model variant, 4-5 DSP1 build, 6-7 DSP2/M0 build, 8-9 CPLD/AFCI build, 10-11 M3 build. | register value | ASCII | R | SOURCE_ONLY | source_claim | — |
| holding | 88 | Modbus version | Modbus version | u16 / 100; /100 | version | R | RESOLVED_WITH_NOTES | read_verified, semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| holding | 89 | Power-factor control mode | 0=Unity PF, 1=Fixed PF setpoint, 2=Default PF line, 3=User-defined PF line, 4=Under-excited reactive power, 5=Over-excited reactive power, 6=Q(V) curve, 7=Direct control, 8=Static capacitive QV, 9=Static inductive QV. | register value | — | W | SOURCE_ONLY | source_claim | — |
| holding | 90 | GPRS modem IP/status flags | Bit 0-3: 0=idle, 1=IP read requested, 2=set IP succeeded; Bit 4-7: 0=unknown, 1=modem OK, 2=no SIM, 3=no network, 4=TCP connect fail, 5=TCP connected, etc. | register value | — | W | UNKNOWN_RESERVED | source_claim | — |
| holding | 91 | Frequency derating start | Frequencyderating startpoint | register value | 0.01H Z | W | SOURCE_ONLY | source_claim | — |
| holding | 92 | Frequency derating slope | Frequency–loadlimit rate | register value | 10tim es | W | SOURCE_ONLY | source_claim | — |
| holding | 93 | CEI 0-21 Q(V) point V1S | CEI021V1SQ(v) | register value | 0.1V | W | SOURCE_ONLY | source_claim | — |
| holding | 94 | CEI 0-21 Q(V) point V2S | CEI021V2SQ(v) | register value | 0.1V | W | SOURCE_ONLY | source_claim | — |
| holding | 95 | CEI 0-21 Q(V) point V1L | CEI021V1LQ(v) | register value | 0.1V | W | SOURCE_ONLY | source_claim | — |
| holding | 96 | CEI 0-21 Q(V) point V2L | CEI021V2LQ(v) | register value | 0.1V | W | SOURCE_ONLY | source_claim | — |
| holding | 97 | Q(V) lock-in active power | Q(v)lockinactive powerofCEI021 | register value | Percen t | W | SOURCE_ONLY | source_claim | — |
| holding | 98 | Q(V) lock-out active power | Q(v)lockOutactive powerofCEI021 | register value | Percen t | W | SOURCE_ONLY | source_claim | — |
| holding | 99 | Power-factor curve lock-in voltage | Lockingirdvoltof CEI021PFline | register value | 0.1V | W | SOURCE_ONLY | source_claim | — |
| holding | 100 | Power-factor curve lock-out voltage | Lockoutgirdvoltof CEI021PFline | register value | 0.1V | W | SOURCE_ONLY | source_claim | — |
| holding | 101 | Power-factor adjust value 1 | PFadjustvalue1 | register value | — | W | SOURCE_ONLY | source_claim | — |
| holding | 102 | Power-factor adjust value 2 | PFadjustvalue2 | register value | — | W | SOURCE_ONLY | source_claim | — |
| holding | 103 | Power-factor adjust value 3 | PFadjustvalue3 | register value | — | W | SOURCE_ONLY | source_claim | — |
| holding | 104 | Power-factor adjust value 4 | PFadjustvalue4 | register value | — | W | SOURCE_ONLY | source_claim | — |
| holding | 105 | Power-factor adjust value 5 | PFadjustvalue5 | register value | — | W | SOURCE_ONLY | source_claim | — |
| holding | 106 | Power-factor adjust value 6 | PFadjustvalue6 | register value | — | W | SOURCE_ONLY | source_claim | — |
| holding | 107 | Q(V) response delay | QV Reactive Power delaytime | register value | 1S | W | SOURCE_ONLY | source_claim | — |
| holding | 108 | Over-frequency derating delay | Overfrequency derati ngdelaytime | register value | 50ms | W | SOURCE_ONLY | source_claim | — |
| holding | 109 | Maximum reactive power magnitude | QmaxforQ(V)curve | register value | 0.1% | W | SOURCE_ONLY | source_claim | — |
| holding | 110 | PF curve point 1 load | 255meansnothispoint | register value | percen t | W | SOURCE_ONLY | source_claim | — |
| holding | 111 | PF curve point 1 target | PFlimitlinepoint1 powerfactor | register value | — | W | SOURCE_ONLY | source_claim | — |
| holding | 112 | PF curve point 2 load | 255meansnothispoint | register value | percen t | W | SOURCE_ONLY | source_claim | — |
| holding | 113 | PF curve point 2 target | PFlimitlinepoint 2powerfactor | register value | — | W | SOURCE_ONLY | source_claim | — |
| holding | 114 | PF curve point 3 load | 255meansnothispoint | register value | percen t | W | SOURCE_ONLY | source_claim | — |
| holding | 115 | PF curve point 3 target | PFlimitlinepoint3 powerfactor | register value | — | W | SOURCE_ONLY | source_claim | — |
| holding | 116 | PF curve point 4 load | 255meansnothispoint | register value | percen t | W | SOURCE_ONLY | source_claim | — |
| holding | 117 | PF curve point 4 target | PFlimitlinepoint4 powerfactor | register value | — | W | SOURCE_ONLY | source_claim | — |
| holding | 118 | Module code segments | SxxBxx | register value | — | R | SOURCE_ONLY | source_claim | — |
| holding | 119 | Module code segments | DxxTxx | register value | — | R | SOURCE_ONLY | source_claim | — |
| holding | 120 | Module code segments | PxxUxx | register value | — | R | SOURCE_ONLY | source_claim | — |
| holding | 121 | Module code segments | Mxxxx Power | register value | — | R | SOURCE_ONLY | source_claim | — |
| holding | 122 | Export limit enable mode | ExportLimitenable, 0:DisableexportLimit; 1:Enable485exportLimit; 2:Enable232exportLimit; 3:EnableCTexportLimit; | register value | — | R/W | SOURCE_ONLY | source_claim | — |
| holding | 123 | Export limit power setpoint | ExportLimitPowerRate | register value | 0.1% | R/W | SOURCE_ONLY | source_claim | — |
| holding | 124 | Tracker coupling mode | 0:Independent 1:DCSource 2:Parallel | register value | — | W | SOURCE_ONLY | source_claim | — |
| holding | 3000 | Export-limit fallback cap | Thepowerrate whenexportLimit failed | register value; /10 | 0.1% | R/W | SOURCE_ONLY | source_claim | — |
| holding | 3001 | Serial Number | Thenewmodel usesthefollowing registerstorecord theserialnumber; The representationis thesameasthe original:one registerholdstwo charactersandthe newserialnumber is30characters. | serial_number; /10 | ASCII | R/W | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| holding | 3002 | Serial Number | Serialnumber3-4 | register value | ASCII | R/W | SOURCE_ONLY | source_claim | — |
| holding | 3003 | Serial Number | Serialnumber5-6 | register value | ASCII | R/W | SOURCE_ONLY | source_claim | — |
| holding | 3004 | Serial Number | Serialnumber7-8 | register value | ASCII | R/W | SOURCE_ONLY | source_claim | — |
| holding | 3005 | Serial Number | Serialnumber9-10 | register value | ASCII | R/W | SOURCE_ONLY | source_claim | — |
| holding | 3006 | Serial Number | Serialnumber11-12 | register value | ASCII | R/W | SOURCE_ONLY | source_claim | — |
| holding | 3007 | Serial Number | Serialnumber13-14 | register value | ASCII | R/W | SOURCE_ONLY | source_claim | — |
| holding | 3008 | Serial Number | Serialnumber15-16 | register value | ASCII | R/W | SOURCE_ONLY | source_claim | — |
| holding | 3009 | Serial Number | Serialnumber17-18 | register value | ASCII | R/W | SOURCE_ONLY | source_claim | — |
| holding | 3010 | Serial Number | Serialnumber19-20 | register value | ASCII | R/W | SOURCE_ONLY | source_claim | — |
| holding | 3011 | Serial Number | Serialnumber21-22 | register value | ASCII | R/W | SOURCE_ONLY | source_claim | — |
| holding | 3012 | Serial Number | Serialnumber23-24 | register value | ASCII | R/W | SOURCE_ONLY | source_claim | — |
| holding | 3013 | Serial Number | Serialnumber25-26 | register value | ASCII | R/W | SOURCE_ONLY | source_claim | — |
| holding | 3014 | Serial Number | Serialnumber27-28 | register value | ASCII | R/W | SOURCE_ONLY | source_claim | — |
| holding | 3015 | Serial Number | Serialnumber29-30 | register value | ASCII | R/W | SOURCE_ONLY | source_claim | — |
| holding | 3016 | Dry-contact enable | DryContact functionenable | register value | — | R/W | SOURCE_ONLY | source_claim | — |
| holding | 3017 | Dry-contact close threshold | The power rate of drycontactturnon | register value | 0.1% | R/W | SOURCE_ONLY | source_claim | — |
| holding | 3018 | Hybrid work mode | MIN2.5~6KTL-XH/ XADoubleCT special | register value | — | R/W | SOURCE_ONLY | source_claim | — |
| holding | 3019 | Dry-contact release threshold | Drycontact closurepowerpe rcentage | register value | 0~100 0 | R/W | SOURCE_ONLY | source_claim | — |
| holding | 3020 | Off-grid box control | Leave at factory value unless instructed by Growatt support. | register value | — | R/W | SOURCE_ONLY | source_claim | — |
| holding | 3021 | External off-grid enable | 0x00: Disable; （default） 0x01:Enable; | register value | — | R/W | SOURCE_ONLY | source_claim | — |
| holding | 3022 | BDC stop-work bus voltage | BdcStopWorkOfBusVolt | register value | V | R | SOURCE_ONLY | source_claim | — |
| holding | 3023 | Grid topology selection | MIN2.5~6KTL-XH/ XADoubleCT special | register value | — | R/W | SOURCE_ONLY | source_claim | — |
| holding | 3024 | Float-charge current limit | CCcurrent | register value; /10 | 0.1A | R/W | SOURCE_ONLY | source_claim | — |
| holding | 3025 | Battery-low warning setpoint | Leadacidbattery LVvoltage | register value | 0.1V | R/W | SOURCE_ONLY | source_claim | — |
| holding | 3026 | Battery-low warning clear | Clearbatterylow voltageerror voltagepoint LoadPercent(only lead-Acid): 45.5V(Load< 20%); 48.0V(20%<=Load <=50%); 49.0V(Load> 50%); | register value | 0.1V | R/W | SOURCE_ONLY | source_claim | — |
| holding | 3027 | Battery discharge cutoff | Shouldstop dischargewhen lowerthanthis voltage(only lead-Acid): 46.0V(Load< 20%); 44.8V(20%<=Load <=50%); 44.2V(Load> 50%); | register value | 0.1V | R/W | SOURCE_ONLY | source_claim | — |
| holding | 3028 | Battery charge stop voltage | Shouldstop chargewhen higherthanthis voltage | register value; /100 | 0.01V | R/W | SOURCE_ONLY | source_claim | — |
| holding | 3029 | Battery discharge start voltage | Shouldnot dischargewhen lowerthanthis voltage | register value; /100 | 0.01V | R/W | SOURCE_ONLY | source_claim | — |
| holding | 3030 | Battery constant-charge voltage | CVvoltage（acid） canchargewhen lowerthanthis voltage | register value; /100 | 0.01V | R/W | SOURCE_ONLY | source_claim | — |
| holding | 3031 | Discharge low temperature limit | 0-200:0-20℃ 1000-1400： -40-0℃ | register value; /10 | 0.1℃ | R/W | SOURCE_ONLY | source_claim | — |
| holding | 3032 | Discharge high temperature limit | Batterytemperatureupper limitfordischarge | register value; /10 | 0.1℃ | R/W | SOURCE_ONLY | source_claim | — |
| holding | 3033 | Charge low temperature limit | Battery temperaturelower limit 0-200:0-20℃ 1000-1400： -40-0℃ | register value; /10 | 0.1℃ | R/W | SOURCE_ONLY | source_claim | — |
| holding | 3034 | Charge high temperature limit | Battery temperature upperlimit | register value; /10 | 0.1℃ | R/W | SOURCE_ONLY | source_claim | — |
| holding | 3035 | Under-frequency discharge delay | UnderFreDelay Time | register value | 50ms | R/W | SOURCE_ONLY | source_claim | — |
| holding | 3036 | Grid-first discharge power rate | Grid-first discharge power rate | u16 percentage; 255 disables limit | % | R/W | RESOLVED | read_verified, semantic_correlated, source_claim | — |
| holding | 3037 | Grid-first stop SOC | Grid-first stop SOC | u16 | % | R/W | RESOLVED | read_verified, semantic_correlated, source_claim | — |
| holding | 3038 | Grid-first schedule 1 start/control | Grid-first schedule 1 start/control | packed minute/hour/priority/enable | — | R/W | RESOLVED | read_verified, source_claim | — |
| holding | 3039 | Grid-first schedule 1 end | Grid-first schedule 1 end | packed minute/hour | — | R/W | RESOLVED | read_verified, source_claim | — |
| holding | 3040 | Grid-first schedule 2 start/control | Grid-first schedule 2 start/control | packed minute/hour/priority/enable | — | R/W | RESOLVED | read_verified, source_claim | — |
| holding | 3041 | Grid-first schedule 2 end | Grid-first schedule 2 end | packed minute/hour | W | R/W | RESOLVED | read_verified, source_claim | — |
| holding | 3042 | Grid-first schedule 3 start/control | Grid-first schedule 3 start/control | packed minute/hour/priority/enable | W | R/W | RESOLVED | read_verified, source_claim | — |
| holding | 3043 | Grid-first schedule 3 end | Grid-first schedule 3 end | packed minute/hour | W | R/W | RESOLVED | read_verified, source_claim | — |
| holding | 3044 | Grid-first schedule 4 start/control | Grid-first schedule 4 start/control | packed minute/hour/priority/enable | W | R/W | RESOLVED | read_verified, source_claim | — |
| holding | 3045 | Grid-first schedule 4 end | Grid-first schedule 4 end | packed minute/hour | W | R/W | RESOLVED | read_verified, source_claim | — |
| holding | 3046 | Reserved | Reserved | u16 raw | W | R | RESOLVED | read_verified, source_claim | — |
| holding | 3047 | Battery-first charge power rate | Battery-first charge power rate | u16 percentage | % | R/W | RESOLVED_WITH_NOTES | read_verified, semantic_correlated, source_claim | Legacy data-type catalogue incorrectly labels this as a two-word runtime counter. |
| holding | 3048 | Battery-first stop SOC | Battery-first stop SOC | u16 | % | R/W | RESOLVED_WITH_NOTES | read_verified, semantic_correlated, source_claim | Legacy data-type catalogue incorrectly labels this as the low word of runtime. |
| holding | 3049 | AC charge enabled | AC charge enabled | u16 enum 0=disabled, 1=enabled | — | R/W | RESOLVED_WITH_NOTES | read_verified, semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| holding | 3050 | Battery-first schedule 1 start/control | Battery-first schedule 1 start/control | packed minute/hour/priority/enable | — | R/W | RESOLVED | read_verified, source_claim | — |
| holding | 3051 | Battery-first schedule 1 end | Battery-first schedule 1 end | packed minute/hour | kWh | R/W | RESOLVED | read_verified, source_claim | — |
| holding | 3052 | Battery-first schedule 2 start/control | Battery-first schedule 2 start/control | packed minute/hour/priority/enable | kWh | R/W | RESOLVED | read_verified, source_claim | — |
| holding | 3053 | Battery-first schedule 2 end | Battery-first schedule 2 end | packed minute/hour | kWh | R/W | RESOLVED | read_verified, source_claim | — |
| holding | 3054 | Battery-first schedule 3 start/control | Battery-first schedule 3 start/control | packed minute/hour/priority/enable | kWh | R/W | RESOLVED | read_verified, source_claim | — |
| holding | 3055 | Battery-first schedule 3 end | Battery-first schedule 3 end | packed minute/hour | kWh | R/W | RESOLVED | read_verified, source_claim | — |
| holding | 3056 | Battery-first schedule 4 start/control | Battery-first schedule 4 start/control | packed minute/hour/priority/enable | kWh | R/W | RESOLVED | read_verified, source_claim | — |
| holding | 3057 | Battery-first schedule 4 end | Battery-first schedule 4 end | packed minute/hour | kWh | R/W | RESOLVED | read_verified, source_claim | — |
| holding | 3058 | Battery-first schedule 5 start/control | Battery-first schedule 5 start/control | packed minute/hour/priority/enable | kWh | R/W | RESOLVED | read_verified, source_claim | — |
| holding | 3059 | Battery-first schedule 5 end | Battery-first schedule 5 end | packed minute/hour | kWh | R/W | RESOLVED | read_verified, source_claim | — |
| holding | 3060 | Reserved | Reserved | register value; /10 | kWh | R | UNKNOWN_RESERVED | source_claim | — |
| holding | 3061 | Reserved | Reserved | register value; /10 | kWh | R | UNKNOWN_RESERVED | source_claim | — |
| holding | 3062 | Reserved | Reserved | register value; /10 | kWh | R | UNKNOWN_RESERVED | source_claim | — |
| holding | 3063 | Reserved | Reserved | register value; /10 | kWh | R | UNKNOWN_RESERVED | source_claim | — |
| holding | 3064 | Reserved | Reserved | register value; /10 | kWh | R | UNKNOWN_RESERVED | source_claim | — |
| holding | 3065 | Reserved | Reserved | register value; /10 | kWh | R | UNKNOWN_RESERVED | source_claim | — |
| holding | 3066 | Reserved | Reserved | register value; /10 | kWh | R | UNKNOWN_RESERVED | source_claim | — |
| holding | 3067 | Reserved | Reserved | register value; /10 | kWh | R | UNKNOWN_RESERVED | source_claim | — |
| holding | 3068 | Reserved | Reserved | register value; /10 | kWh | R | UNKNOWN_RESERVED | source_claim | — |
| holding | 3069 | Reserved | Reserved | register value; /10 | kWh | R | UNKNOWN_RESERVED | source_claim | — |
| holding | 3070 | BatteryType | Batterytype 0:Lithium 1:Lead-acid 2:other | register value; /10 | kWh | R/W | SOURCE_ONLY | source_claim | — |
| holding | 3071 | BatMdlSeria/ ParalNum | BatMdlSeria/Paral Num; SPH4-11Kused Theupper8bits indicatethe numberofseries segments； Thelower8bits indicatethe numberofparallel sections; | register value; /10 | kWh | R/W | SOURCE_ONLY | source_claim | — |
| holding | 3072 | Reserved | Reserved | register value; /10 | kWh | R | UNKNOWN_RESERVED | source_claim | — |
| holding | 3073 | Reserved | Reserved | register value; /10 | kWh | R | UNKNOWN_RESERVED | source_claim | — |
| holding | 3074 | Reserved | Reserved | register value; /10 | kWh | R | UNKNOWN_RESERVED | source_claim | — |
| holding | 3075 | Reserved | Reserved | register value; /10 | kWh | R | UNKNOWN_RESERVED | source_claim | — |
| holding | 3076 | Reserved | Reserved | register value; /10 | kWh | R | UNKNOWN_RESERVED | source_claim | — |
| holding | 3077 | Reserved | Reserved | register value; /10 | kWh | R | UNKNOWN_RESERVED | source_claim | — |
| holding | 3078 | Reserved | Reserved | register value; /10 | kWh | R | UNKNOWN_RESERVED | source_claim | — |
| holding | 3079 | UPS/EPS function enable | UPS/EPS function enable | u16 enum 0=disabled, 1=enabled | bool | R/W | RESOLVED | read_verified, source_claim | — |
| holding | 3080 | UPS/EPS voltage selection | UPS/EPS voltage selection | u16 enum 0=230 V, 1=208 V, 2=240 V | V | R/W | RESOLVED | read_verified, source_claim | — |
| holding | 3081 | UPS/EPS frequency selection | UPS/EPS frequency selection | u16 enum 0=50 Hz, 1=60 Hz | Hz | R/W | RESOLVED_WITH_NOTES | read_verified, source_claim | FC04 3081 is PV4 lifetime-energy high word; FC03 3081 is UPSFreqSet. |
| holding | 3082 | Load-first stop SOC | Load-first stop SOC | u16 percentage | % | R/W | RESOLVED | read_verified, source_claim | — |
| holding | 3083 | Reserved | Reserved | register value; /10 | kWh | R | UNKNOWN_RESERVED | source_claim | — |
| holding | 3084 | Reserved | Reserved | register value; /10 | kWh | R | UNKNOWN_RESERVED | source_claim | — |
| holding | 3085 | Modbus slave address | 1:Communication addr=1 1~254: Communication addr=1~254 | register value | — | R/W | SOURCE_ONLY | source_claim | — |
| holding | 3086 | RS-485 baud rate | 0:9600bps 1:38400bps | register value | — | R/W | SOURCE_ONLY | source_claim | — |
| holding | 3087 | Battery rack serial | Forbattery | register value | ASCII | R/W | SOURCE_ONLY | source_claim | — |
| holding | 3088 | Battery rack serial | SerialNumber3-4 | register value | ASCII | R/W | SOURCE_ONLY | source_claim | — |
| holding | 3089 | Battery rack serial | SerialNumber5-6 | register value | ASCII | R/W | SOURCE_ONLY | source_claim | — |
| holding | 3090 | Battery rack serial | SerialNumber7-8 | register value | ASCII | R/W | SOURCE_ONLY | source_claim | — |
| holding | 3091 | Battery rack serial | SerialNumber9-10 | register value | ASCII | R/W | SOURCE_ONLY | source_claim | — |
| holding | 3092 | Battery rack serial | SerialNumber11-12 | register value | ASCII | R/W | SOURCE_ONLY | source_claim | — |
| holding | 3093 | Battery rack serial | SerialNumber13-14 | register value | ASCII | R/W | SOURCE_ONLY | source_claim | — |
| holding | 3094 | Battery rack serial | SerialNumber15-16 | register value | ASCII | R/W | SOURCE_ONLY | source_claim | — |
| holding | 3095 | BDC reset command | 0：Invaliddata 1：Resetsetting parameters 2：Resetcorrection parameter 3：Clearhistorical power | register value | — | R/W | SOURCE_ONLY | source_claim | — |
| holding | 3096 | BDC monitoring code | ZEBA | register value | ASCII | R | SOURCE_ONLY | source_claim | — |
| holding | 3097 | BDC monitoring code | Four-character identifier for the BDC monitoring firmware (e.g. ZEBA). | register value | ASCII | R | SOURCE_ONLY | source_claim | — |
| holding | 3098 | BDC DTC code | DTC | register value | — | R | SOURCE_ONLY | source_claim | — |
| holding | 3099 | DSP firmware code | DSPsoftwarecode | register value | ASCII | R | SOURCE_ONLY | source_claim | — |
| holding | 3100 | DSP firmware code | Identifier for the inverter DSP firmware build. | register value | ASCII | R | SOURCE_ONLY | source_claim | — |
| holding | 3101 | DSP firmware version | DSPSoftwareVersion | register value | ASCII | R | SOURCE_ONLY | source_claim | — |
| holding | 3102 | Bus voltage reference | MinimumBUSvoltagefor charginganddischarging batteries | register value | V | R | SOURCE_ONLY | source_claim | — |
| holding | 3103 | BDC monitor firmware | BDCmonitoringsoftware version | register value | ASCII | R | SOURCE_ONLY | source_claim | — |
| holding | 3104 | BMS MCU hardware version | BMS hardware version information | register value | ASCII | R | SOURCE_ONLY | source_claim | — |
| holding | 3105 | BMS firmware version | BMSsoftwareversion information | register value | ASCII | R | SOURCE_ONLY | source_claim | — |
| holding | 3106 | BMS manufacturer | BMSManufacturerName | register value | ASCII | R | SOURCE_ONLY | source_claim | — |
| holding | 3107 | BMS communication interface | BMSCommunicati oninterfacetype： 0:RS485; 1:CAN; | register value | — | R | SOURCE_ONLY | source_claim | — |
| holding | 3108 | BDC module identifier 4 | SxxBxx | register value | ASCII | R/W | SOURCE_ONLY | source_claim | — |
| holding | 3109 | BDC module identifier 3 | DxxTxx | register value | ASCII | R/W | SOURCE_ONLY | source_claim | — |
| holding | 3110 | BDC module identifier 2 | PxxUxx | register value | ASCII | R/W | SOURCE_ONLY | source_claim | — |
| holding | 3111 | BDC module identifier 1 | Mxxxx | register value | ASCII | R/W | SOURCE_ONLY | source_claim | — |
| holding | 3112 | Reserved | Reserved; reported as zero on known firmware. | register value | — | R | UNKNOWN_RESERVED | source_claim | — |
| holding | 3113 | BDC protocol version | Bit8-bit15The majorversion numberranges from0-256.In principle,itcannot bechanged Bit0-bit7Minor versionnumber [0-256].Ifthe protocolis changed,youneed toupdatethis version No. | register value | — | R | SOURCE_ONLY | source_claim | — |
| holding | 3114 | BDC certification version | BDCCertificationVer | register value | — | R | SOURCE_ONLY | source_claim | — |
| holding | 3115 | Reserved | Reserved for future use. | register value | — | R | UNKNOWN_RESERVED | source_claim | — |
| holding | 3116 | Reserved | Reserved for future use. | register value | — | R | UNKNOWN_RESERVED | source_claim | — |
| holding | 3117 | Reserved | Reserved for future use. | register value | — | R | UNKNOWN_RESERVED | source_claim | — |
| holding | 3118 | BDC on/off state | Indicates whether the battery DC converter is currently running (1) or idle (0). | register value | — | R | SOURCE_ONLY | source_claim | — |
| holding | 3119 | Dry contact state | Current state of the dry-contact output (0 = open, 1 = closed). | register value | — | R | SOURCE_ONLY | source_claim | — |
| holding | 3120 | Reserved | Reserved; reported as zero on TL-XH firmware. | register value | — | R | UNKNOWN_RESERVED | source_claim | — |
| holding | 3121 | Self-use power | Not yet surfaced by the Home Assistant integration. | register value; /10 | W | R | SOURCE_ONLY | source_claim | — |
| holding | 3122 | Self-use power | Not yet surfaced by the Home Assistant integration. | register value; /10 | W | R | SOURCE_ONLY | source_claim | — |
| holding | 3123 | System energy today | Available in firmware but not yet exposed as an integration attribute. | register value; /10 | kWh | R | SOURCE_ONLY | source_claim | — |
| holding | 3124 | System energy today | Available in firmware but not yet exposed as an integration attribute. | register value; /10 | kWh | R | SOURCE_ONLY | source_claim | — |
| holding | 3125 | Us Tou Month Groups | bit0~3:month_L； bit4~7:month_H bit8, 0:disable1：enable Bit9~15:reserve | register value | — | R/W | SOURCE_ONLY | source_claim | — |
| holding | 3126 | Us Tou Month Groups | WithTimeMonth1 | register value | — | R/W | SOURCE_ONLY | source_claim | — |
| holding | 3127 | Us Tou Month Groups | WithTimeMonth1 | register value | — | R/W | SOURCE_ONLY | source_claim | — |
| holding | 3128 | Us Tou Month Groups | WithTimeMonth1 | register value | — | R/W | SOURCE_ONLY | source_claim | — |
| holding | 3129 | Us Tou Slot Table | bit0~6:min； bit7~11:hour； bit12~14, 0:loadfirst; | register value | — | R/W | SOURCE_ONLY | source_claim | — |
| holding | 3130 | Us Tou Slot Table | bit0~6:min； bit7~11:hour； bit12-13, 0:Weekday 1:Weekend 2:WeeK bit14~15：reserve | register value | — | R/W | SOURCE_ONLY | source_claim | — |
| holding | 3131 | Us Tou Slot Table | SameasTime1 （us） | register value | — | R/W | SOURCE_ONLY | source_claim | — |
| holding | 3132 | Us Tou Slot Table | SameasTime1 （us） | register value | — | R/W | SOURCE_ONLY | source_claim | — |
| holding | 3133 | Us Tou Slot Table | SameasTime1 （us） | register value | — | R/W | SOURCE_ONLY | source_claim | — |
| holding | 3134 | Us Tou Slot Table | SameasTime1 （us） | register value | — | R/W | SOURCE_ONLY | source_claim | — |
| holding | 3135 | Us Tou Slot Table | SameasTime1 （us） | register value | — | R/W | SOURCE_ONLY | source_claim | — |
| holding | 3136 | Us Tou Slot Table | SameasTime1 （us） | register value | — | R/W | SOURCE_ONLY | source_claim | — |
| holding | 3137 | Us Tou Slot Table | SameasTime1 （us） | register value | — | R/W | SOURCE_ONLY | source_claim | — |
| holding | 3138 | Us Tou Slot Table | SameasTime1 （us） | register value | — | R/W | SOURCE_ONLY | source_claim | — |
| holding | 3139 | Us Tou Slot Table | SameasTime1 （us） | register value | — | R/W | SOURCE_ONLY | source_claim | — |
| holding | 3140 | Us Tou Slot Table | SameasTime1 （us） | register value | — | R/W | SOURCE_ONLY | source_claim | — |
| holding | 3141 | Us Tou Slot Table | SameasTime1 （us） | register value | — | R/W | SOURCE_ONLY | source_claim | — |
| holding | 3142 | Us Tou Slot Table | SameasTime1 （us） | register value | — | R/W | SOURCE_ONLY | source_claim | — |
| holding | 3143 | Us Tou Slot Table | SameasTime1 （us） | register value | — | R/W | SOURCE_ONLY | source_claim | — |
| holding | 3144 | Us Tou Slot Table | SameasTime1 （us） | register value | — | R/W | SOURCE_ONLY | source_claim | — |
| holding | 3145 | Us Tou Slot Table | SameasTime1 （us） | register value | — | R/W | SOURCE_ONLY | source_claim | — |
| holding | 3146 | Us Tou Slot Table | SameasTime1 （us） | register value | — | R/W | SOURCE_ONLY | source_claim | — |
| holding | 3147 | Us Tou Slot Table | SameasTime1 （us） | register value | — | R/W | SOURCE_ONLY | source_claim | — |
| holding | 3148 | Us Tou Slot Table | SameasTime1 （us） | register value | — | R/W | SOURCE_ONLY | source_claim | — |
| holding | 3149 | Us Tou Slot Table | SameasTime1 （us） | register value | — | R/W | SOURCE_ONLY | source_claim | — |
| holding | 3150 | Us Tou Slot Table | SameasTime1 （us） | register value | — | R/W | SOURCE_ONLY | source_claim | — |
| holding | 3151 | Us Tou Slot Table | SameasTime1 （us） | register value | — | R/W | SOURCE_ONLY | source_claim | — |
| holding | 3152 | Us Tou Slot Table | SameasTime1 （us） | register value | — | R/W | SOURCE_ONLY | source_claim | — |
| holding | 3153 | Us Tou Slot Table | SameasTime1 （us） | register value | — | R/W | SOURCE_ONLY | source_claim | — |
| holding | 3154 | Us Tou Slot Table | SameasTime1 （us） | register value | — | R/W | SOURCE_ONLY | source_claim | — |
| holding | 3155 | Us Tou Slot Table | SameasTime1 （us） | register value | — | R/W | SOURCE_ONLY | source_claim | — |
| holding | 3156 | Us Tou Slot Table | SameasTime1 （us） | register value | — | R/W | SOURCE_ONLY | source_claim | — |
| holding | 3157 | Us Tou Slot Table | SameasTime1 （us） | register value | — | R/W | SOURCE_ONLY | source_claim | — |
| holding | 3158 | Us Tou Slot Table | SameasTime1 （us） | register value | — | R/W | SOURCE_ONLY | source_claim | — |
| holding | 3159 | Us Tou Slot Table | SameasTime1 （us） | register value | — | R/W | SOURCE_ONLY | source_claim | — |
| holding | 3160 | Us Tou Slot Table | SameasTime1 （us） | register value | — | R/W | SOURCE_ONLY | source_claim | — |
| holding | 3161 | Us Tou Slot Table | SameasTime1 （us） | register value | — | R/W | SOURCE_ONLY | source_claim | — |
| holding | 3162 | Us Tou Slot Table | SameasTime1 （us） | register value | — | R/W | SOURCE_ONLY | source_claim | — |
| holding | 3163 | Us Tou Slot Table | SameasTime1 （us） | register value | — | R/W | SOURCE_ONLY | source_claim | — |
| holding | 3164 | Us Tou Slot Table | SameasTime1 （us） | register value | — | R/W | SOURCE_ONLY | source_claim | — |
| holding | 3165 | Us Tou Slot Table | SameasTime1 （us） | register value | — | R/W | SOURCE_ONLY | source_claim | — |
| holding | 3166 | Us Tou Slot Table | SameasTime1 （us） | register value | — | R/W | SOURCE_ONLY | source_claim | — |
| holding | 3167 | Us Tou Slot Table | SameasTime1 （us） | register value | — | R/W | SOURCE_ONLY | source_claim | — |
| holding | 3168 | Us Tou Slot Table | SameasTime1 （us） | register value | — | R/W | SOURCE_ONLY | source_claim | — |
| holding | 3169 | Us Tou Slot Table | SameasTime1 （us） | register value | — | R/W | SOURCE_ONLY | source_claim | — |
| holding | 3170 | Us Tou Slot Table | SameasTime1 （us） | register value | — | R/W | SOURCE_ONLY | source_claim | — |
| holding | 3171 | Us Tou Slot Table | SameasTime1 （us） | register value | — | R/W | SOURCE_ONLY | source_claim | — |
| holding | 3172 | Us Tou Slot Table | SameasTime1 （us） | register value | — | R/W | SOURCE_ONLY | source_claim | — |
| holding | 3173 | Us Tou Slot Table | SameasTime1 （us） | register value | — | R/W | SOURCE_ONLY | source_claim | — |
| holding | 3174 | Us Tou Slot Table | SameasTime1 （us） | register value | — | R/W | SOURCE_ONLY | source_claim | — |
| holding | 3175 | Us Tou Slot Table | SameasTime1 （us） | register value | — | R/W | SOURCE_ONLY | source_claim | — |
| holding | 3176 | Us Tou Slot Table | SameasTime1 （us） | register value | — | R/W | SOURCE_ONLY | source_claim | — |
| holding | 3177 | Us Tou Slot Table | SameasTime1 （us） | register value | — | R/W | SOURCE_ONLY | source_claim | — |
| holding | 3178 | Us Tou Slot Table | SameasTime1 （us） | register value | — | R/W | SOURCE_ONLY | source_claim | — |
| holding | 3179 | Us Tou Slot Table | SameasTime1 （us） | register value | — | R/W | SOURCE_ONLY | source_claim | — |
| holding | 3180 | Us Tou Slot Table | SameasTime1 （us） | register value | — | R/W | SOURCE_ONLY | source_claim | — |
| holding | 3181 | Us Tou Slot Table | SameasTime1 （us） | register value | — | R/W | SOURCE_ONLY | source_claim | — |
| holding | 3182 | Us Tou Slot Table | SameasTime1 （us） | register value | — | R/W | SOURCE_ONLY | source_claim | — |
| holding | 3183 | Us Tou Slot Table | SameasTime1 （us） | register value | — | R/W | SOURCE_ONLY | source_claim | — |
| holding | 3184 | Us Tou Slot Table | SameasTime1 （us） | register value | — | R/W | SOURCE_ONLY | source_claim | — |
| holding | 3185 | Us Tou Slot Table | SameasTime1 （us） | register value | — | R/W | SOURCE_ONLY | source_claim | — |
| holding | 3186 | Us Tou Slot Table | SameasTime1 （us） | register value | — | R/W | SOURCE_ONLY | source_claim | — |
| holding | 3187 | Us Tou Slot Table | SameasTime1 （us） | register value | — | R/W | SOURCE_ONLY | source_claim | — |
| holding | 3188 | Us Tou Slot Table | SameasTime1 （us） | register value | — | R/W | SOURCE_ONLY | source_claim | — |
| holding | 3189 | Us Tou Slot Table | SameasTime1 （us） | register value | — | R/W | SOURCE_ONLY | source_claim | — |
| holding | 3190 | Us Tou Slot Table | SameasTime1 （us） | register value | — | R/W | SOURCE_ONLY | source_claim | — |
| holding | 3191 | Us Tou Slot Table | SameasTime1 （us） | register value | — | R/W | SOURCE_ONLY | source_claim | — |
| holding | 3192 | Us Tou Slot Table | SameasTime1 （us） | register value | — | R/W | SOURCE_ONLY | source_claim | — |
| holding | 3193 | Us Tou Slot Table | SameasTime1 （us） | register value | — | R/W | SOURCE_ONLY | source_claim | — |
| holding | 3194 | Us Tou Slot Table | SameasTime1 （us） | register value | — | R/W | SOURCE_ONLY | source_claim | — |
| holding | 3195 | Us Tou Slot Table | SameasTime1 （us） | register value | — | R/W | SOURCE_ONLY | source_claim | — |
| holding | 3196 | Us Tou Slot Table | SameasTime1 （us） | register value | — | R/W | SOURCE_ONLY | source_claim | — |
| holding | 3197 | Us Tou Slot Table | SameasTime1 （us） | register value | — | R/W | SOURCE_ONLY | source_claim | — |
| holding | 3198 | Us Tou Slot Table | SameasTime1 （us） | register value | — | R/W | SOURCE_ONLY | source_claim | — |
| holding | 3199 | Us Tou Slot Table | SameasTime1 （us） | register value | — | R/W | SOURCE_ONLY | source_claim | — |
| holding | 3200 | Us Tou Slot Table | SameasTime1 （us） | register value | — | R/W | SOURCE_ONLY | source_claim | — |
| holding | 3201 | Us Tou Special Day 1 | bit0~7:day； bit8~14:month bit15， 0：disable1： enable | register value | — | R/W | SOURCE_ONLY | source_claim | — |
| holding | 3202 | Us Tou Special Day 1 | bit0~6:min； bit7~11:hour； bit12~14, 0:loadfirst; 1:batfirst； 2:gridfirst； 3:anti-reflux bit15, 0:disable; 1:enable; | register value | — | R/W | SOURCE_ONLY | source_claim | — |
| holding | 3203 | Us Tou Special Day 1 | bit0~6:min； bit7~11:hour； bit12~15：reserve | register value | — | R/W | SOURCE_ONLY | source_claim | — |
| holding | 3204 | Us Tou Special Day 1 | Sameas SpecialDay1_Time 1 | register value | — | R/W | SOURCE_ONLY | source_claim | — |
| holding | 3205 | Us Tou Special Day 1 | Sameas SpecialDay1_Time 1 | register value | — | R/W | SOURCE_ONLY | source_claim | — |
| holding | 3206 | Us Tou Special Day 1 | Sameas SpecialDay1_Time 1 | register value | — | R/W | SOURCE_ONLY | source_claim | — |
| holding | 3207 | Us Tou Special Day 1 | Sameas SpecialDay1_Time 1 | register value | — | R/W | SOURCE_ONLY | source_claim | — |
| holding | 3208 | Us Tou Special Day 1 | Sameas SpecialDay1_Time 1 | register value | — | R/W | SOURCE_ONLY | source_claim | — |
| holding | 3209 | Us Tou Special Day 1 | Sameas SpecialDay1_Time 1 | register value | — | R/W | SOURCE_ONLY | source_claim | — |
| holding | 3210 | Us Tou Special Day 1 | Sameas SpecialDay1_Time 1 | register value | — | R/W | SOURCE_ONLY | source_claim | — |
| holding | 3211 | Us Tou Special Day 1 | Sameas SpecialDay1_Time 1 | register value | — | R/W | SOURCE_ONLY | source_claim | — |
| holding | 3212 | Us Tou Special Day 1 | Sameas SpecialDay1_Time 1 | register value | — | R/W | SOURCE_ONLY | source_claim | — |
| holding | 3213 | Us Tou Special Day 1 | Sameas SpecialDay1_Time 1 | register value | — | R/W | SOURCE_ONLY | source_claim | — |
| holding | 3214 | Us Tou Special Day 1 | Sameas SpecialDay1_Time 1 | register value | — | R/W | SOURCE_ONLY | source_claim | — |
| holding | 3215 | Us Tou Special Day 1 | Sameas SpecialDay1_Time 1 | register value | — | R/W | SOURCE_ONLY | source_claim | — |
| holding | 3216 | Us Tou Special Day 1 | Sameas SpecialDay1_Time 1 | register value | — | R/W | SOURCE_ONLY | source_claim | — |
| holding | 3217 | Us Tou Special Day 1 | Sameas SpecialDay1_Time 1 | register value | — | R/W | SOURCE_ONLY | source_claim | — |
| holding | 3218 | Us Tou Special Day 1 | Sameas SpecialDay1_Time 1 | register value | — | R/W | SOURCE_ONLY | source_claim | — |
| holding | 3219 | Us Tou Special Day 1 | Sameas SpecialDay1_Time 1 | register value | — | R/W | SOURCE_ONLY | source_claim | — |
| holding | 3220 | Us Tou Special Day 2 | bit0~7:day； bit8~14:month bit15， 0：disable 1：enable | register value | — | R/W | SOURCE_ONLY | source_claim | — |
| holding | 3221 | Us Tou Special Day 2 | bit0~6:min； bit7~11:hour； bit12~14, 0:loadfirst; 1:batfirst； 2:gridfirst； 3:anti-reflux bit15, 0:disable; 1:enable; | register value | — | R/W | SOURCE_ONLY | source_claim | — |
| holding | 3222 | Us Tou Special Day 2 | bit0~6:min； bit7~11:hour； bit12~15：reserve | register value | — | R/W | SOURCE_ONLY | source_claim | — |
| holding | 3223 | Us Tou Special Day 2 | Sameas SpecialDay2_Time 1 | register value | — | R/W | SOURCE_ONLY | source_claim | — |
| holding | 3224 | Us Tou Special Day 2 | Sameas SpecialDay2_Time 1 | register value | — | R/W | SOURCE_ONLY | source_claim | — |
| holding | 3225 | Us Tou Special Day 2 | Sameas SpecialDay2_Time 1 | register value | — | R/W | SOURCE_ONLY | source_claim | — |
| holding | 3226 | Us Tou Special Day 2 | Sameas SpecialDay2_Time 1 | register value | — | R/W | SOURCE_ONLY | source_claim | — |
| holding | 3227 | Us Tou Special Day 2 | Sameas SpecialDay2_Time 1 | register value | — | R/W | SOURCE_ONLY | source_claim | — |
| holding | 3228 | Us Tou Special Day 2 | Sameas SpecialDay2_Time 1 | register value | — | R/W | SOURCE_ONLY | source_claim | — |
| holding | 3229 | Us Tou Special Day 2 | Sameas SpecialDay2_Time 1 | register value | — | R/W | SOURCE_ONLY | source_claim | — |
| holding | 3230 | Us Tou Special Day 2 | Sameas SpecialDay2_Time 1 | register value | — | R/W | SOURCE_ONLY | source_claim | — |
| holding | 3231 | Us Tou Special Day 2 | Sameas SpecialDay2_Time 1 | register value | — | R/W | SOURCE_ONLY | source_claim | — |
| holding | 3232 | Us Tou Special Day 2 | Sameas SpecialDay2_Time 1 | register value | — | R/W | SOURCE_ONLY | source_claim | — |
| holding | 3233 | Us Tou Special Day 2 | Sameas SpecialDay2_Time 1 | register value | — | R/W | SOURCE_ONLY | source_claim | — |
| holding | 3234 | Us Tou Special Day 2 | Sameas SpecialDay2_Time 1 | register value | — | R/W | SOURCE_ONLY | source_claim | — |
| holding | 3235 | Us Tou Special Day 2 | Sameas SpecialDay2_Time 1 | register value | — | R/W | SOURCE_ONLY | source_claim | — |
| holding | 3236 | Us Tou Special Day 2 | Sameas SpecialDay2_Time 1 | register value | — | R/W | SOURCE_ONLY | source_claim | — |
| holding | 3237 | Us Tou Special Day 2 | Sameas SpecialDay2_Time 1 | register value | — | R/W | SOURCE_ONLY | source_claim | — |
| holding | 3238 | Us Tou Special Day 2 | Sameas SpecialDay2_Time 1 | register value | — | R/W | SOURCE_ONLY | source_claim | — |
| holding | 3239 | Us Tou Reserved Block | Vendor documentation marks these addresses as reserved; observed values remain zero on known firmware. | register value | — | R/W | UNKNOWN_RESERVED | source_claim | — |
| holding | 3240 | Us Tou Reserved Block | Vendor documentation marks these addresses as reserved; observed values remain zero on known firmware. | register value | — | R/W | UNKNOWN_RESERVED | source_claim | — |
| holding | 3241 | Us Tou Reserved Block | Vendor documentation marks these addresses as reserved; observed values remain zero on known firmware. | register value | — | R/W | UNKNOWN_RESERVED | source_claim | — |
| holding | 3242 | Us Tou Reserved Block | Vendor documentation marks these addresses as reserved; observed values remain zero on known firmware. | register value | — | R/W | UNKNOWN_RESERVED | source_claim | — |
| holding | 3243 | Us Tou Reserved Block | Vendor documentation marks these addresses as reserved; observed values remain zero on known firmware. | register value | — | R/W | UNKNOWN_RESERVED | source_claim | — |
| holding | 3244 | Us Tou Reserved Block | Vendor documentation marks these addresses as reserved; observed values remain zero on known firmware. | register value | — | R/W | UNKNOWN_RESERVED | source_claim | — |
| holding | 3245 | Us Tou Reserved Block | Vendor documentation marks these addresses as reserved; observed values remain zero on known firmware. | register value | — | R/W | UNKNOWN_RESERVED | source_claim | — |
| holding | 3246 | Us Tou Reserved Block | Vendor documentation marks these addresses as reserved; observed values remain zero on known firmware. | register value | — | R/W | UNKNOWN_RESERVED | source_claim | — |
| holding | 3247 | Us Tou Reserved Block | Vendor documentation marks these addresses as reserved; observed values remain zero on known firmware. | register value | — | R/W | UNKNOWN_RESERVED | source_claim | — |
| holding | 3248 | Us Tou Reserved Block | Vendor documentation marks these addresses as reserved; observed values remain zero on known firmware. | register value | — | R/W | UNKNOWN_RESERVED | source_claim | — |
| holding | 3249 | Us Tou Reserved Block | Vendor documentation marks these addresses as reserved; observed values remain zero on known firmware. | register value | — | R/W | UNKNOWN_RESERVED | source_claim | — |
| holding | 5000 | Bdc Slot 1 Metadata | Repeat for additional BDCs at 40-register strides (5040-5079, 5080-5119, ). Stored as `bdc_metadata_block`. | register value | — | R/W | SOURCE_ONLY | source_claim | — |
| holding | 5001 | Bdc Slot 1 Metadata | Repeat for additional BDCs at 40-register strides (5040-5079, 5080-5119, ). Stored as `bdc_metadata_block`. | register value | — | R/W | SOURCE_ONLY | source_claim | — |
| holding | 5002 | Bdc Slot 1 Metadata | Repeat for additional BDCs at 40-register strides (5040-5079, 5080-5119, ). Stored as `bdc_metadata_block`. | register value | — | R/W | SOURCE_ONLY | source_claim | — |
| holding | 5003 | Bdc Slot 1 Metadata | Repeat for additional BDCs at 40-register strides (5040-5079, 5080-5119, ). Stored as `bdc_metadata_block`. | register value | — | R/W | SOURCE_ONLY | source_claim | — |
| holding | 5004 | Bdc Slot 1 Metadata | Repeat for additional BDCs at 40-register strides (5040-5079, 5080-5119, ). Stored as `bdc_metadata_block`. | register value | — | R/W | SOURCE_ONLY | source_claim | — |
| holding | 5005 | Bdc Slot 1 Metadata | Repeat for additional BDCs at 40-register strides (5040-5079, 5080-5119, ). Stored as `bdc_metadata_block`. | register value | — | R/W | SOURCE_ONLY | source_claim | — |
| holding | 5006 | Bdc Slot 1 Metadata | Repeat for additional BDCs at 40-register strides (5040-5079, 5080-5119, ). Stored as `bdc_metadata_block`. | register value | — | R/W | SOURCE_ONLY | source_claim | — |
| holding | 5007 | Bdc Slot 1 Metadata | Repeat for additional BDCs at 40-register strides (5040-5079, 5080-5119, ). Stored as `bdc_metadata_block`. | register value | — | R/W | SOURCE_ONLY | source_claim | — |
| holding | 5008 | Bdc Slot 1 Metadata | Repeat for additional BDCs at 40-register strides (5040-5079, 5080-5119, ). Stored as `bdc_metadata_block`. | register value | — | R/W | SOURCE_ONLY | source_claim | — |
| holding | 5009 | Bdc Slot 1 Metadata | Repeat for additional BDCs at 40-register strides (5040-5079, 5080-5119, ). Stored as `bdc_metadata_block`. | register value | — | R/W | SOURCE_ONLY | source_claim | — |
| holding | 5010 | Bdc Slot 1 Metadata | Repeat for additional BDCs at 40-register strides (5040-5079, 5080-5119, ). Stored as `bdc_metadata_block`. | register value | — | R/W | SOURCE_ONLY | source_claim | — |
| holding | 5011 | Bdc Slot 1 Metadata | Repeat for additional BDCs at 40-register strides (5040-5079, 5080-5119, ). Stored as `bdc_metadata_block`. | register value | — | R/W | SOURCE_ONLY | source_claim | — |
| holding | 5012 | Bdc Slot 1 Metadata | Repeat for additional BDCs at 40-register strides (5040-5079, 5080-5119, ). Stored as `bdc_metadata_block`. | register value | — | R/W | SOURCE_ONLY | source_claim | — |
| holding | 5013 | Bdc Slot 1 Metadata | Repeat for additional BDCs at 40-register strides (5040-5079, 5080-5119, ). Stored as `bdc_metadata_block`. | register value | — | R/W | SOURCE_ONLY | source_claim | — |
| holding | 5014 | Bdc Slot 1 Metadata | Repeat for additional BDCs at 40-register strides (5040-5079, 5080-5119, ). Stored as `bdc_metadata_block`. | register value | — | R/W | SOURCE_ONLY | source_claim | — |
| holding | 5015 | Bdc Slot 1 Metadata | Repeat for additional BDCs at 40-register strides (5040-5079, 5080-5119, ). Stored as `bdc_metadata_block`. | register value | — | R/W | SOURCE_ONLY | source_claim | — |
| holding | 5016 | Bdc Slot 1 Metadata | Repeat for additional BDCs at 40-register strides (5040-5079, 5080-5119, ). Stored as `bdc_metadata_block`. | register value | — | R/W | SOURCE_ONLY | source_claim | — |
| holding | 5017 | Bdc Slot 1 Metadata | Repeat for additional BDCs at 40-register strides (5040-5079, 5080-5119, ). Stored as `bdc_metadata_block`. | register value | — | R/W | SOURCE_ONLY | source_claim | — |
| holding | 5018 | Bdc Slot 1 Metadata | Repeat for additional BDCs at 40-register strides (5040-5079, 5080-5119, ). Stored as `bdc_metadata_block`. | register value | — | R/W | SOURCE_ONLY | source_claim | — |
| holding | 5019 | Bdc Slot 1 Metadata | Repeat for additional BDCs at 40-register strides (5040-5079, 5080-5119, ). Stored as `bdc_metadata_block`. | register value | — | R/W | SOURCE_ONLY | source_claim | — |
| holding | 5020 | Bdc Slot 1 Metadata | Repeat for additional BDCs at 40-register strides (5040-5079, 5080-5119, ). Stored as `bdc_metadata_block`. | register value | — | R/W | SOURCE_ONLY | source_claim | — |
| holding | 5021 | Bdc Slot 1 Metadata | Repeat for additional BDCs at 40-register strides (5040-5079, 5080-5119, ). Stored as `bdc_metadata_block`. | register value | — | R/W | SOURCE_ONLY | source_claim | — |
| holding | 5022 | Bdc Slot 1 Metadata | Repeat for additional BDCs at 40-register strides (5040-5079, 5080-5119, ). Stored as `bdc_metadata_block`. | register value | — | R/W | SOURCE_ONLY | source_claim | — |
| holding | 5023 | Bdc Slot 1 Metadata | Repeat for additional BDCs at 40-register strides (5040-5079, 5080-5119, ). Stored as `bdc_metadata_block`. | register value | — | R/W | SOURCE_ONLY | source_claim | — |
| holding | 5024 | Bdc Slot 1 Metadata | Repeat for additional BDCs at 40-register strides (5040-5079, 5080-5119, ). Stored as `bdc_metadata_block`. | register value | — | R/W | SOURCE_ONLY | source_claim | — |
| holding | 5025 | Bdc Slot 1 Metadata | Repeat for additional BDCs at 40-register strides (5040-5079, 5080-5119, ). Stored as `bdc_metadata_block`. | register value | — | R/W | SOURCE_ONLY | source_claim | — |
| holding | 5026 | Bdc Slot 1 Metadata | Repeat for additional BDCs at 40-register strides (5040-5079, 5080-5119, ). Stored as `bdc_metadata_block`. | register value | — | R/W | SOURCE_ONLY | source_claim | — |
| holding | 5027 | Bdc Slot 1 Metadata | Repeat for additional BDCs at 40-register strides (5040-5079, 5080-5119, ). Stored as `bdc_metadata_block`. | register value | — | R/W | SOURCE_ONLY | source_claim | — |
| holding | 5028 | Bdc Slot 1 Metadata | Repeat for additional BDCs at 40-register strides (5040-5079, 5080-5119, ). Stored as `bdc_metadata_block`. | register value | — | R/W | SOURCE_ONLY | source_claim | — |
| holding | 5029 | Bdc Slot 1 Metadata | Repeat for additional BDCs at 40-register strides (5040-5079, 5080-5119, ). Stored as `bdc_metadata_block`. | register value | — | R/W | SOURCE_ONLY | source_claim | — |
| holding | 5030 | Bdc Slot 1 Metadata | Repeat for additional BDCs at 40-register strides (5040-5079, 5080-5119, ). Stored as `bdc_metadata_block`. | register value | — | R/W | SOURCE_ONLY | source_claim | — |
| holding | 5031 | Bdc Slot 1 Metadata | Repeat for additional BDCs at 40-register strides (5040-5079, 5080-5119, ). Stored as `bdc_metadata_block`. | register value | — | R/W | SOURCE_ONLY | source_claim | — |
| holding | 5032 | Bdc Slot 1 Metadata | Repeat for additional BDCs at 40-register strides (5040-5079, 5080-5119, ). Stored as `bdc_metadata_block`. | register value | — | R/W | SOURCE_ONLY | source_claim | — |
| holding | 5033 | Bdc Slot 1 Metadata | Repeat for additional BDCs at 40-register strides (5040-5079, 5080-5119, ). Stored as `bdc_metadata_block`. | register value | — | R/W | SOURCE_ONLY | source_claim | — |
| holding | 5034 | Bdc Slot 1 Metadata | Repeat for additional BDCs at 40-register strides (5040-5079, 5080-5119, ). Stored as `bdc_metadata_block`. | register value | — | R/W | SOURCE_ONLY | source_claim | — |
| holding | 5035 | Bdc Slot 1 Metadata | Repeat for additional BDCs at 40-register strides (5040-5079, 5080-5119, ). Stored as `bdc_metadata_block`. | register value | — | R/W | SOURCE_ONLY | source_claim | — |
| holding | 5036 | Bdc Slot 1 Metadata | Repeat for additional BDCs at 40-register strides (5040-5079, 5080-5119, ). Stored as `bdc_metadata_block`. | register value | — | R/W | SOURCE_ONLY | source_claim | — |
| holding | 5037 | Bdc Slot 1 Metadata | Repeat for additional BDCs at 40-register strides (5040-5079, 5080-5119, ). Stored as `bdc_metadata_block`. | register value | — | R/W | SOURCE_ONLY | source_claim | — |
| holding | 5038 | Bdc Slot 1 Metadata | Repeat for additional BDCs at 40-register strides (5040-5079, 5080-5119, ). Stored as `bdc_metadata_block`. | register value | — | R/W | SOURCE_ONLY | source_claim | — |
| holding | 5039 | Bdc Slot 1 Metadata | Repeat for additional BDCs at 40-register strides (5040-5079, 5080-5119, ). Stored as `bdc_metadata_block`. | register value | — | R/W | SOURCE_ONLY | source_claim | — |
| input | 0 | Inverter status | InverterStatus | register value; /10 | — | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 1 | PV input power | PpvH | register value; /10 | 0.1W | R/W | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 2 | PV input power | PpvL | register value; /10 | 0.1W | R/W | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3 | PV1 DC voltage | Vpv1 | register value; /10 | 0.1V | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 4 | PV1 DC current | PV1Curr | register value; /10 | 0.1A | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 5 | PV1 DC power | Ppv1H | register value; /10 | 0.1W | R/W | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 6 | PV1 DC power | Ppv1L | register value; /10 | 0.1W | R/W | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 7 | PV2 DC voltage | Vpv2 | register value; /10 | 0.1V | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 8 | PV2 DC current | PV2Curr | register value; /10 | 0.1A | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 9 | PV2 DC power | Ppv2H | register value; /10 | 0.1W | R/W | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 10 | PV2 DC power | Ppv2L | register value; /10 | 0.1W | R/W | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 11 | PV3 DC voltage | Vpv3 | register value; /10 | 0.1V | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 12 | PV3 DC current | PV3Curr | register value; /10 | 0.1A | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 13 | PV3 DC power | Ppv3H | register value; /10 | 0.1W | R/W | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 14 | PV3 DC power | Ppv3L | register value; /10 | 0.1W | R/W | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 15 | PV4 DC voltage | Vpv4 | register value; /10 | 0.1V | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 16 | PV4 DC current | PV4Curr | register value; /10 | 0.1A | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 17 | PV4 DC power | Ppv4H | register value; /10 | 0.1W | R/W | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 18 | PV4 DC power | Ppv4L | register value; /10 | 0.1W | R/W | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 19 | PV5 DC voltage | Vpv5 | register value; /10 | 0.1V | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 20 | PV5 DC current | PV5Curr | register value; /10 | 0.1A | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 21 | PV5 DC power | Ppv5H | register value; /10 | 0.1W | R/W | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 22 | PV5 DC power | Ppv5L | register value; /10 | 0.1W | R/W | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 23 | PV6 DC voltage | Vpv6 | register value; /10 | 0.1V | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 24 | PV6 DC current | PV6Curr | register value; /10 | 0.1A | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 25 | PV6 DC power | PV6inputpower(high) | register value; /10 | W | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 26 | PV6 DC power | PV6inputpower(low) | register value; /10 | W | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 27 | PV7 DC voltage | PV7voltage | register value; /10 | V | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 28 | PV7 DC current | PV7inputcurrent | register value; /10 | A | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 29 | PV7 DC power | PV7inputpower(high) | register value; /10 | W | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 30 | PV7 DC power | PV7inputpower(low) | register value; /10 | W | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 31 | PV8 DC voltage | PV8voltage | register value; /10 | V | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 32 | PV8 DC current | PV8inputcurrent | register value; /10 | A | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 33 | PV8 DC power | PV8inputpower(high) | register value; /10 | W | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 34 | PV8 DC power | PV8inputpower(low) | register value; /10 | W | R | RESOLVED | semantic_correlated, source_claim | — |
| input | 35 | AC output power | Outputpower(high) | register value; /10 | W | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 36 | AC output power | Outputpower(low) | register value; /10 | W | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 37 | Grid frequency | Gridfrequency | register value; /100 | Hz | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 38 | AC phase L1 voltage | Three/singlephasegridvoltage | register value; /10 | V | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 39 | AC phase L1 current | Three/singlephasegridoutputcurrent | register value; /10 | A | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 40 | AC phase L1 power | Three/single phase grid output watt VA(high) | register value; /10 | W | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 41 | AC phase L1 power | Three/single phase grid output watt VA(low) | register value; /10 | W | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 42 | AC phase L2 voltage | Threephasegridvoltage | register value; /10 | V | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 43 | AC phase L2 current | Threephasegridoutputcurrent | register value; /10 | A | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 44 | AC phase L2 power | Threephasegridoutputpower(high) | register value; /10 | W | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 45 | AC phase L2 power | Threephasegridoutputpower(low) | register value; /10 | W | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 46 | AC phase L3 voltage | Threephasegridvoltage | register value; /10 | V | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 47 | AC phase L3 current | Threephasegridoutputcurrent | register value; /10 | A | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 48 | AC phase L3 power | Threephasegridoutputpower(high) | register value; /10 | W | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 49 | AC phase L3 power | Threephasegridoutputpower(low) | register value; /10 | W | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 53 | Output energy today | Todaygenerateenergy(high) | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 54 | Output energy today | Todaygenerateenergy(low) | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 55 | Output energy total | Totalgenerateenergy(high) | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 56 | Output energy total | Totalgenerateenergy(low) | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 57 | Run time | Raw counter counts seconds; divide by 7200 to obtain hours. | register value; /7200 | h | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 58 | Run time | Raw counter counts seconds; divide by 7200 to obtain hours. | register value; /7200 | h | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 59 | PV1 energy today | PV1Energytoday(high) | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 60 | PV1 energy today | PV1Energytoday(low) | register value; /10 | kWh | R | RESOLVED | semantic_correlated, source_claim | — |
| input | 61 | PV1 energy total | PV1Energytotal(high) | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 62 | PV1 energy total | PV1Energytotal(low) | register value; /10 | kWh | R | RESOLVED | semantic_correlated, source_claim | — |
| input | 63 | PV2 energy today | PV2Energytoday(high) | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 64 | PV2 energy today | PV2Energytoday(low) | register value; /10 | kWh | R | RESOLVED | semantic_correlated, source_claim | — |
| input | 65 | PV2 energy total | PV2Energytotal(high) | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 66 | PV2 energy total | PV2Energytotal(low) | register value; /10 | kWh | R | RESOLVED | semantic_correlated, source_claim | — |
| input | 67 | PV3 energy today | PV3Energytoday(high) | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 68 | PV3 energy today | PV3Energytoday(low) | register value; /10 | kWh | R | RESOLVED | semantic_correlated, source_claim | — |
| input | 69 | PV3 energy total | PV3Energytotal(high) | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 70 | PV3 energy total | PV3Energytotal(low) | register value; /10 | kWh | R | RESOLVED | semantic_correlated, source_claim | — |
| input | 71 | PV4 energy today | PV4Energytoday(high) | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 72 | PV4 energy today | PV4Energytoday(low) | register value; /10 | kWh | R | RESOLVED | semantic_correlated, source_claim | — |
| input | 73 | PV4 energy total | PV4Energytotal(high) | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 74 | PV4 energy total | PV4Energytotal(low) | register value; /10 | kWh | R | RESOLVED | semantic_correlated, source_claim | — |
| input | 75 | PV5 energy today | PV5Energytoday(high) | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 76 | PV5 energy today | PV5Energytoday(low) | register value; /10 | kWh | R | RESOLVED | semantic_correlated, source_claim | — |
| input | 77 | PV5 energy total | PV5Energytotal(high) | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 78 | PV5 energy total | PV5Energytotal(low) | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 79 | PV6 energy today | PV6Energytoday(high) | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 80 | PV6 energy today | PV6Energytoday(low) | register value; /10 | kWh | R | RESOLVED | semantic_correlated, source_claim | — |
| input | 81 | PV6 energy total | PV6Energytotal(high) | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 82 | PV6 energy total | PV6Energytotal(low) | register value; /10 | kWh | R | RESOLVED | semantic_correlated, source_claim | — |
| input | 83 | PV7 energy today | PV7Energytoday(high) | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 84 | PV7 energy today | PV7Energytoday(low) | register value; /10 | kWh | R | RESOLVED | semantic_correlated, source_claim | — |
| input | 85 | PV7 energy total | PV7Energytotal(high) | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 86 | PV7 energy total | PV7Energytotal(low) | register value; /10 | kWh | R | RESOLVED | semantic_correlated, source_claim | — |
| input | 87 | PV8 energy today | PV8Energytoday(high) | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 88 | PV8 energy today | PV8Energytoday(low) | register value; /10 | kWh | R | RESOLVED | semantic_correlated, source_claim | — |
| input | 89 | PV8 energy total | PV8Energytotal(high) | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 90 | PV8 energy total | PV8Energytotal(low) | register value; /10 | kWh | R | RESOLVED | semantic_correlated, source_claim | — |
| input | 91 | PV energy total | PVEnergytotal(high) | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 92 | PV energy total | PVEnergytotal(low) | register value; /10 | kWh | R | RESOLVED | semantic_correlated, source_claim | — |
| input | 93 | Inverter temperature | Invertertemperature | register value; /10 | °C | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 94 | IPM temperature | TheinsideIPMininverterTemperature | register value; /10 | °C | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 95 | Boost temperature | Boosttemperature | register value; /10 | °C | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 98 | P-bus voltage | PBusinsideVoltage | register value; /10 | V | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 99 | N-bus voltage | NBusinsideVoltage | register value; /10 | V | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 101 | Output power percentage | RealOutputpowerPercent | register value; /10 | % | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 104 | Derating mode | DeratingMode | register value; /10 | — | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 105 | Fault code | Inverterfaultmaincode | register value; /10 | — | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 110 | Warning code | WarningbitH | register value; /10 | — | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 111 | Warning code | Inverterwarnsubcode | register value; /10 | — | R | SOURCE_ONLY | source_claim | — |
| input | 234 | Output reactive power | NominalOutputReactivePowerH | register value; /10 | var | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 235 | Output reactive power | NominalOutputReactivePowerL | register value; /10 | var | R | SOURCE_ONLY | source_claim | — |
| input | 236 | Reactive energy total | Reactivepowergeneration | register value; /10 | kvarh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 237 | Reactive energy total | Reactivepowergeneration | register value; /10 | kvarh | R | SOURCE_ONLY | source_claim | — |
| input | 3000 | Inverter status | Inverter status | u16 enum; 1=normal | — | R | RESOLVED_WITH_NOTES | read_verified, semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3001 | Total PV/input power | Total PV/input power | u32 / 10; /10 | W | R | RESOLVED_WITH_NOTES | read_verified, semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3002 | PV input power | Total PV input power summed across all strings (0.1 W resolution). | register value; /10 | W | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3003 | PV1 voltage | PV1 voltage | u16 / 10; /10 | V | R | RESOLVED_WITH_NOTES | read_verified, semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3004 | PV1 current | PV1 current | u16 / 10; /10 | A | R | RESOLVED_WITH_NOTES | read_verified, semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3005 | PV1 power | PV1 power | u32 / 10; /10 | W | R | RESOLVED_WITH_NOTES | read_verified, semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3006 | PV1 DC power | Real-time DC power from PV1 computed from voltage and current readings. | register value; /10 | W | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3007 | PV2 voltage | PV2 voltage | u16 / 10; /10 | V | R | RESOLVED_WITH_NOTES | read_verified, semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3008 | PV2 current | PV2 current | u16 / 10; /10 | A | R | RESOLVED_WITH_NOTES | read_verified, semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3009 | PV2 power | PV2 power | u32 / 10; /10 | W | R | RESOLVED_WITH_NOTES | read_verified, semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3010 | PV2 DC power | Real-time DC power from PV2 computed from voltage and current readings. | register value; /10 | W | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3011 | PV3 DC voltage | PV3voltage | register value; /10 | V | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3012 | PV3 DC current | PV3inputcurrent | register value; /10 | A | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3013 | PV3 DC power | PV3power | register value; /10 | W | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3014 | PV3 DC power | Real-time DC power from PV3 computed from voltage and current readings. | register value; /10 | W | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3015 | PV4 DC voltage | PV4voltage | register value; /10 | V | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3016 | PV4 DC current | PV4inputcurrent | register value; /10 | A | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3017 | PV4 DC power | PV4power | register value; /10 | W | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3018 | PV4 DC power | Real-time DC power from PV4 computed from voltage and current readings. | register value; /10 | W | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3019 | System output power | Systemoutputpower | register value; /10 | W | R | RESOLVED | semantic_correlated, source_claim | — |
| input | 3020 | System output power | AC output power reported by the TL-XH mirror block (0.1 W resolution). Mirrors the value at register 35. | register value; /10 | W | R | RESOLVED | semantic_correlated, source_claim | — |
| input | 3021 | Output reactive power | reactivepower | register value; /10 | POWER_REACTIVE | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3022 | Output reactive power | Instantaneous reactive power on the AC output (positive = inductive, negative = capacitive). | register value; /10 | var | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3023 | AC output power | AC output power | u32 / 10; /10 | W | R | RESOLVED_WITH_NOTES | read_verified, semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3024 | AC output power | Active AC output power delivered by the inverter (0.1 W resolution). | register value; /10 | W | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3025 | Grid frequency | Grid frequency | u16 / 100; /100 | Hz | R | RESOLVED_WITH_NOTES | read_verified, semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3026 | AC phase L1 voltage | AC phase L1 voltage | u16 / 10; /10 | V | R | RESOLVED_WITH_NOTES | read_verified, semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3027 | AC phase L1 current | AC phase L1 current | u16 / 10; /10 | A | R | RESOLVED_WITH_NOTES | read_verified, semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3028 | AC phase L1 power | AC phase L1 power | u32 / 10; /10 | W | R | RESOLVED_WITH_NOTES | read_verified, semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3029 | AC phase L1 power | Active power exported on phase L1. | register value; /10 | W | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3030 | AC phase L2 voltage | Threephasegridvoltage | register value; /10 | V | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3031 | AC phase L2 current | Threephasegridoutputcurrent | register value; /10 | A | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3032 | AC phase L2 power | Threephasegridoutputpower | register value; /10 | VA | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3033 | AC phase L2 power | Active power exported on phase L2. | register value; /10 | W | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3034 | AC phase L3 voltage | Threephasegridvoltage | register value; /10 | V | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3035 | AC phase L3 current | Threephasegridoutputcurrent | register value; /10 | A | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3036 | AC phase L3 power | Threephasegridoutputpower | register value; /10 | VA | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3037 | AC phase L3 power | Active power exported on phase L3. | register value; /10 | W | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3038 | RS line voltage | Threephasegridvoltage | register value; /10 | V | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3039 | ST line voltage | Threephasegridvoltage | register value; /10 | V | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3040 | TR line voltage | Threephasegridvoltage | register value; /10 | V | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3041 | Power to user/grid import | Power to user/grid import | s32 / 10; /10 | W | R | RESOLVED_WITH_NOTES | read_verified, semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3042 | Load supply power | Real-time active power delivered to on-site (self-consumption) loads. | register value; /10 | W | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3043 | Power to grid/export | Power to grid/export | s32 / 10; /10 | W | R | RESOLVED_WITH_NOTES | read_verified, semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3044 | Grid export power | Active power exported to the utility grid. | register value; /10 | W | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3045 | User load power | User load power | s32 / 10; /10 | W | R | RESOLVED_WITH_NOTES | read_verified, semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3046 | Home load power | Aggregate instantaneous demand from on-site loads. | register value; /10 | W | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3047 | Inverter runtime | Inverter runtime | u32 / 7200; /7200 | h | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3048 | Inverter runtime | Raw counter counts seconds; divide by 7200 to obtain hours. | register value; /7200 | h | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3049 | AC energy today | AC energy today | u32 / 10; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3050 | Output energy today | Energy exported to the AC output today (0.1 kWh resolution). | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3051 | Output energy total | Totalgenerateenergy | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3052 | Output energy total | Lifetime AC output energy (0.1 kWh resolution). | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3053 | PV energy total | PVenergytotal | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3054 | PV energy total | Total PV energy generated across all strings (0.1 kWh resolution). | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3055 | PV1 energy today | PV1energytoday | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3056 | PV1 energy today | Energy harvested by PV1 today. Values use 0.1 kWh resolution. | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3057 | PV1 energy total | PV1energytotal | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3058 | PV1 energy total | Lifetime energy harvested by PV1. Values use 0.1 kWh resolution. | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3059 | PV2 energy today | PV2energytoday | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3060 | PV2 energy today | Energy harvested by PV2 today. Values use 0.1 kWh resolution. | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3061 | PV2 energy total | PV2energytotal | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3062 | PV2 energy total | Lifetime energy harvested by PV2. Values use 0.1 kWh resolution. | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3063 | PV3 energy today | PV3energytoday | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3064 | PV3 energy today | Energy harvested by PV3 today. Values use 0.1 kWh resolution. | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3065 | PV3 energy total | PV3energytotal | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3066 | PV3 energy total | Lifetime energy harvested by PV3. Values use 0.1 kWh resolution. | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3067 | Load energy today | Todayenergytouser | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3068 | Load energy today | Energy delivered to on-site loads today (0.1 kWh resolution). | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3069 | Load energy total | Totalenergytouser | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3070 | Load energy total | Lifetime energy delivered to on-site loads (0.1 kWh resolution). | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3071 | Export energy today | Todayenergytogrid | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3072 | Export energy today | Energy exported to the grid today (0.1 kWh resolution). | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3073 | Export energy total | Totalenergytogrid | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3074 | Export energy total | Lifetime energy exported to the grid (0.1 kWh resolution). | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3075 | User load energy today | Todayenergyofuserload | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3076 | User load energy today | Energy delivered to on-site loads today (0.1 kWh resolution). | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3077 | User load energy total | Totalenergyofuserload | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3078 | User load energy total | Lifetime energy delivered to on-site loads (0.1 kWh resolution). | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3079 | PV4 energy today | PV4 energy today | u32 / 10; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3080 | PV4 energy today | Energy harvested by PV string 4 today (0.1 kWh resolution). | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3081 | PV4 energy total | PV4 energy total | u32 / 10; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; FC03 3081 is UPSFreqSet; this input-space meaning is independent. |
| input | 3082 | PV4 energy total | Lifetime energy harvested by PV string 4 (0.1 kWh resolution). | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3083 | PV energy today | PVenergytoday | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3084 | PV energy today | Total PV energy harvested across all strings today (0.1 kWh resolution). | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3085 | Reserved | Reserved | register value; /1 | — | R | UNKNOWN_RESERVED | semantic_correlated, source_claim | — |
| input | 3086 | Derating mode | DeratingMode | register value; /1 | — | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3087 | PV insulation resistance | PVISOvalue | register value; /1 | kΩ | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3088 | Residual current R | RDCICurr | register value; /10 | A | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3089 | Residual current S | SDCICurr | register value; /10 | A | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3090 | Residual current T | TDCICurr | register value; /10 | A | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3091 | GFCI current | GFCICurr | register value; /1 | A | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3092 | Total bus voltage | totalbusvoltage | register value; /10 | V | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3093 | Inverter temperature | Invertertemperature | register value; /10 | °C | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3094 | IPM temperature | TheinsideIPMininvertertemperature | register value; /10 | °C | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3095 | Boost temperature | Boosttemperature | register value; /10 | °C | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3096 | Temp4 | Reserved | register value; /10 | — | R | UNKNOWN_RESERVED | semantic_correlated, source_claim | — |
| input | 3097 | Communication board temperature | Commmunicationbroadtemperature | register value; /10 | °C | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3098 | P-bus voltage | PBusinsideVoltage | register value; /10 | V | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3099 | N-bus voltage | NBusinsideVoltage | register value; /10 | V | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3100 | Inverter output power factor | InverteroutputPFnow | register value; /1 | — | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3101 | Output power percentage | RealOutputpowerPercent | register value; /1 | % | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3102 | Output max power limit | OutputMaxpowerLimited | register value; /10 | W | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3103 | Output max power limit | Current active output power limit enforced by the inverter (0.1 W resolution). | register value; /10 | W | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3104 | Standby flags | Inverterstandbyflag | register value; /1 | bit0:turn off Order； bit1:PVLow； bit2:AC Volt/Freq outofscope； bit3~bit7 ： Reserved | R | RESOLVED | semantic_correlated, source_claim | — |
| input | 3105 | Fault code | Inverterfaultmaincode | register value; /1 | — | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3106 | Warning main code | InverterWarningmaincode | register value; /1 | — | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3107 | Fault subcode | Inverterfaultsubcode | register value; /1 | — | R | RESOLVED | semantic_correlated, source_claim | — |
| input | 3108 | Warning subcode | InverterWarningsubcode | register value; /1 | — | R | RESOLVED | semantic_correlated, source_claim | — |
| input | 3109 | Register 3109 | — | register value; /1 | — | R | UNKNOWN_RESERVED | semantic_correlated, source_claim | — |
| input | 3110 | Warning code | Current inverter warning code (vendor-defined bitmask). | register value; /1 | — | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3111 | Warning code | PresentFFTValue[CHANNEL_A] | register value; /1 | — | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3112 | AFCI status | AFCIStatus | register value; /1 | — | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3113 | AFCI strength (channel A) | AFCIStrength[CHANNEL_A] | register value; /1 | — | R | RESOLVED | semantic_correlated, source_claim | — |
| input | 3114 | AFCI self-check (channel A) | AFCISelfCheck[CHANNEL_A] | register value; /1 | — | R | RESOLVED | semantic_correlated, source_claim | — |
| input | 3115 | Inverter start delay | invstartdelaytime | register value; /1 | s | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3116 | Reserved | Reserved | register value; /1 | — | R | UNKNOWN_RESERVED | semantic_correlated, source_claim | — |
| input | 3117 | Reserved | Reserved | register value; /1 | — | R | UNKNOWN_RESERVED | semantic_correlated, source_claim | — |
| input | 3118 | BDC connect state | BDCconnectstate | register value; /1 | — | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3119 | Dry contact state | CurrentstatusofDryContact | register value; /1 | — | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3120 | Reserved | Reserved | register value; /1 | — | R | UNKNOWN_RESERVED | semantic_correlated, source_claim | — |
| input | 3121 | Self-use power | self-usepower | register value; /10 | W | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3122 | Self-use power | Real-time power consumed by on-site loads (0.1 W resolution). | register value; /10 | W | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3123 | System energy today | Systemenergytoday | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3124 | System energy today | Total energy processed by the hybrid system today (0.1 kWh resolution). | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3125 | Battery discharge today | Todaydischargeenergy | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3126 | Battery discharge today | Energy discharged from the battery into the AC system today (0.1 kWh resolution). | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3127 | Battery discharge total | Totaldischargeenergy | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3128 | Battery discharge total | Total energy discharged from the battery (0.1 kWh resolution). | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3129 | Battery charge today | Chargeenergytoday | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3130 | Battery charge today | Energy charged into the battery today (0.1 kWh resolution). | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3131 | Battery charge total | Chargeenergytotal | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3132 | Battery charge total | Total energy charged into the battery (0.1 kWh resolution). | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3133 | AC charge energy today | TodayenergyofACcharge | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3134 | AC charge energy today | Energy charged into the battery from AC today (0.1 kWh resolution). | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3135 | AC charge energy total | TotalenergyofACcharge | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3136 | AC charge energy total | Lifetime energy charged into the battery from AC (0.1 kWh resolution). | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3137 | System energy total | Lifetime hybrid system energy throughput (0.1 kWh resolution). | register value; /1 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3138 | System energy total | Totalenergyofsystemoutput\ | register value; /1 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3139 | Self-use energy today | TodayenergyofSelfoutput | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3140 | Self-use energy today | Energy supplied to on-site loads today (0.1 kWh resolution). | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3141 | Self-use energy total | TotalenergyofSelfoutput | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3142 | Self-use energy total | Lifetime energy supplied to on-site loads (0.1 kWh resolution). | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3143 | Reserved | Reserved | register value; /1 | — | R | UNKNOWN_RESERVED | semantic_correlated, source_claim | — |
| input | 3144 | Priority mode | WordMode | register value | — | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3145 | EPS frequency | UPSfrequency | register value | Hz | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3146 | EPS phase R voltage | UPSphaseRoutputvoltage | register value; /10 | V | R | RESOLVED | semantic_correlated, source_claim | — |
| input | 3147 | EPS phase R current | UPSphaseRoutputcurrent | register value; /10 | A | R | RESOLVED | semantic_correlated, source_claim | — |
| input | 3148 | EPS phase R apparent power | UPSphaseRoutputpower | register value | VA | R | SOURCE_ONLY | source_claim | — |
| input | 3149 | EPS phase R apparent power | Phase R apparent power on the EPS output (0.1 VA resolution). | register value | VA | R | SOURCE_ONLY | source_claim | — |
| input | 3150 | EPS phase S voltage | UPSphaseSoutputvoltage | register value; /10 | V | R | RESOLVED | semantic_correlated, source_claim | — |
| input | 3151 | EPS phase S current | UPSphaseSoutputcurrent | register value; /10 | A | R | RESOLVED | semantic_correlated, source_claim | — |
| input | 3152 | EPS phase S apparent power | UPSphaseSoutputpower | register value; /10 | VA | R | RESOLVED | semantic_correlated, source_claim | — |
| input | 3153 | EPS phase S apparent power | Phase S apparent power on the EPS output (0.1 VA resolution). | register value; /10 | VA | R | RESOLVED | semantic_correlated, source_claim | — |
| input | 3154 | EPS phase T voltage | UPSphaseToutputvoltage | register value; /10 | V | R | RESOLVED | semantic_correlated, source_claim | — |
| input | 3155 | EPS phase T current | UPSphaseToutputcurrent | register value; /10 | A | R | RESOLVED | semantic_correlated, source_claim | — |
| input | 3156 | EPS phase T apparent power | UPSphaseToutputpower | register value; /10 | VA | R | RESOLVED | semantic_correlated, source_claim | — |
| input | 3157 | EPS phase T apparent power | Phase T apparent power on the EPS output (0.1 VA resolution). | register value; /10 | VA | R | RESOLVED | semantic_correlated, source_claim | — |
| input | 3158 | EPS total apparent power | UPSoutputpower | register value; /10 | VA | R | RESOLVED | semantic_correlated, source_claim | — |
| input | 3159 | EPS total apparent power | Total apparent power delivered by the EPS output (0.1 VA resolution). | register value; /10 | VA | R | RESOLVED | semantic_correlated, source_claim | — |
| input | 3160 | EPS load percentage | LoadpercentofUPSouput | register value; /10 | % | R | RESOLVED | semantic_correlated, source_claim | — |
| input | 3161 | BDC power factor | Powerfactor | register value; /10 | pf | R | RESOLVED | semantic_correlated, source_claim | — |
| input | 3162 | BDC DC voltage | DCvoltage | register value; /1 | V | R | RESOLVED | semantic_correlated, source_claim | — |
| input | 3163 | Reserved | Reserved | register value; /1 | — | R | UNKNOWN_RESERVED | semantic_correlated, source_claim | — |
| input | 3164 | BDC presence flag | BDC presence flag | u16 flag | 0:Don'tneed 1：need | R | RESOLVED_WITH_NOTES | read_verified, semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3165 | BDC derating mode | BDCDeratingMode： 0:Normal,unrestricted 1：Standbyorfault 2：Maximumbatterycurrentlimit (discharge) 3：BatterydischargeEnable(Discharge) 4：Highbusdischargederating | register value; /1 | — | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3166 | BDC system mode | SystemworkStateandmodeThe upper8bitsindicatethemode; 0：Nochargeanddischarge； 1：charge； 2：Discharge； Thelower8bitsrepresentthestatus; 0:StandbyStatus; 1:NormalStatus; 2:FaultStatus 3：FlashStatus; | register value; /1 | — | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3167 | BDC fault code | Storgedevicefaultcode | register value; /1 | — | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3168 | BDC warning code | Storgedevicewarningcode | register value; /1 | — | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3169 | Battery voltage | Battery voltage | u16 / 100; /100 | V | R | RESOLVED_WITH_NOTES | read_verified, semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives.; OpenInverter lists /10; live raw 21146 is plausible as 211.46 V and not 2114.6 V. |
| input | 3170 | Battery current | Battery current | s16 / 10; /10 | A | R | RESOLVED_WITH_NOTES | read_verified, semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3171 | Battery SOC | Battery SOC | u16 percentage | % | R | RESOLVED_WITH_NOTES | read_verified, semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3172 | VBUS1 voltage | TotalBUSvoltage | register value; /10 | A | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3173 | VBUS2 voltage | OntheBUSvoltage | register value; /10 | A | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3174 | Buck/boost current | BUCK-BOOSTCurrent | register value; /10 | A | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3175 | LLC stage current | LLCCurrent | register value; /10 | A | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3176 | Battery temperature A | TempertureA | register value; /10 | °C | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3177 | Battery temperature B | TempertureB | register value; /10 | °C | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3178 | Battery discharge power | Battery discharge power | s32 / 10; /10 | W | R | RESOLVED_WITH_NOTES | read_verified, semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3179 | Battery discharge power | Real-time discharge power flowing from the battery (0.1 W resolution). | register value; /10 | W | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3180 | Battery charge power | Battery charge power | s32 / 10; /10 | W | R | RESOLVED_WITH_NOTES | read_verified, semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3181 | Battery charge power | Real-time charge power flowing into the battery (0.1 W resolution). | register value; /10 | W | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3182 | BDC discharge energy total | Dischargetotalenergyofstorgedevice | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3183 | BDC discharge energy total | Lifetime energy discharged by the battery DC converter (0.1 kWh resolution). | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3184 | BDC charge energy total | Chargetotalenergyofstorgedevice | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3185 | BDC charge energy total | Lifetime energy charged into the battery via the BDC (0.1 kWh resolution). | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3186 | Reserved | Reserved | register value; /1 | — | R | UNKNOWN_RESERVED | semantic_correlated, source_claim | — |
| input | 3187 | BDC flag word | BDCmark(chargeanddischarge, faultalarmcode) Bit0:ChargeEn;BDCallowscharging Bit1:DischargeEn;BDCallows discharge Bit2~7:Resvd;reserved Bit8~11:WarnSubCode;BDC sub-warningcode Bit12~15:FaultSubCode;BDC sub-errorcode | register value; /1 | — | R | UNKNOWN_RESERVED | semantic_correlated, source_claim | — |
| input | 3188 | VBUS2 low voltage | LowerBUSvoltage | register value; /10 | V | R | RESOLVED | semantic_correlated, source_claim | — |
| input | 3189 | BMS max cell index | BmsMaxVoltCellNo | register value; /1 | — | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3190 | BMS min cell index | BmsMinVoltCellNo | register value; /1 | — | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3191 | BMS average temperature A | BmsBatteryAvgTemp | register value; /1 | °C | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3192 | BMS max cell temperature A | BmsMaxCellTemp | register value; /10 | °C | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3193 | BMS average temperature B | BmsBatteryAvgTemp | register value; /10 | °C | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3194 | BMS max cell temperature B | BmsMaxCellTemp | register value; /1 | °C | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3195 | BMS average temperature C | BmsBatteryAvgTemp | register value; /1 | °C | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3196 | BMS max SOC | BmsMaxSOC | register value; /1 | % | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3197 | BMS min SOC | BmsMinSOC | register value; /1 | % | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3198 | Parallel battery count | ParallelBatteryNum | register value; /1 | — | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3199 | BMS derate reason | BmsDerateReason | register value; /1 | — | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3200 | BMS full charge capacity | BmsGaugeFCC（Ah） | register value; /1 | Ah | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3201 | BMS remaining capacity | BmsGaugeRM（Ah） | register value; /1 | Ah | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3202 | BMS protect flags 1 | BMSProtect1 | register value; /1 | — | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3203 | BMS warning flags 1 | BMSWarn1 | register value; /1 | — | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3204 | BMS fault flags 1 | BMSFault1 | register value; /1 | — | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3205 | BMS fault flags 2 | BMSFault2 | register value; /1 | — | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3206 | Reserved | Reserved | register value; /1 | — | R | UNKNOWN_RESERVED | semantic_correlated, source_claim | — |
| input | 3207 | Reserved | Reserved | register value; /1 | — | R | UNKNOWN_RESERVED | semantic_correlated, source_claim | — |
| input | 3208 | Reserved | Reserved | register value; /1 | — | R | UNKNOWN_RESERVED | semantic_correlated, source_claim | — |
| input | 3209 | Reserved | Reserved | register value; /1 | — | R | UNKNOWN_RESERVED | semantic_correlated, source_claim | — |
| input | 3210 | Battery insulation status | BatteryISOdetectionstatus | register value; /1 | 0：Not detected 1：Detection completed | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3211 | Battery request flags | batteryworkrequest | register value; /1 | — | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3212 | BMS status | BMS status | u16 enum | 0:dormancy 1:Charge 2:Discharge 3:free 4:standby 5:Softstart 6:fault 7:update | R | RESOLVED_WITH_NOTES | read_verified, semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3213 | BMS protect flags 2 | BMSProtect2 | register value; /1 | — | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3214 | BMS warning flags 2 | BMSWarn2 | register value; /1 | — | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3215 | BMS SOC | BMS SOC | u16 percentage | % | R | RESOLVED_WITH_NOTES | read_verified, semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3216 | BMS battery voltage | BMS battery voltage | u16 / 100; /100 | V | R | RESOLVED_WITH_NOTES | read_verified, semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3217 | BMS battery current | BMS battery current | s16 / 100; /100 | A | R | RESOLVED_WITH_NOTES | read_verified, semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3218 | BMS max cell temperature | batterycellmaximumtemperature | register value; /10 | °C | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3219 | BMS max charge current | Maximumchargingcurrent | register value; /100 | A | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3220 | BMS max discharge current | Maximumdischargecurrent | register value; /100 | A | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3221 | BMS cycle count | BMSCycleCnt | register value; /1 | — | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3222 | BMS SOH | BMS SOH | u16 percentage | % | R | RESOLVED_WITH_NOTES | read_verified, semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3223 | BMS charge voltage limit | Batterychargingvoltagelimitvalue | register value; /100 | V | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3224 | BMS discharge voltage limit | Batterydischargevoltagelimitvalue | register value; /1 | V | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3225 | BMS warning flags 3 | BMSWarn3 | register value; /1 | — | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3226 | BMS protect flags 3 | BMSProtect3 | register value; /1 | — | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3227 | Reserved | Reserved | register value; /1 | — | R | UNKNOWN_RESERVED | semantic_correlated, source_claim | — |
| input | 3228 | Reserved | Reserved | register value; /1 | — | R | UNKNOWN_RESERVED | semantic_correlated, source_claim | — |
| input | 3229 | Reserved | Reserved | register value; /1 | — | R | UNKNOWN_RESERVED | semantic_correlated, source_claim | — |
| input | 3230 | BMS max cell voltage | BMSBatterySingleVoltMax | register value; /1 | V | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3231 | BMS min cell voltage | BMSBatterySingleVoltMin | register value; /1 | V | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3232 | Battery load voltage | BatteryLoadVolt | register value; /100 | [0，650.00] | R | RESOLVED | semantic_correlated, source_claim | — |
| input | 3233 | Register 3233 | — | register value; /1 | — | R | UNKNOWN_RESERVED | semantic_correlated, source_claim | — |
| input | 3234 | Debug data 1 | Debugdata1 | register value; /1 | — | R | RESOLVED | semantic_correlated, source_claim | — |
| input | 3235 | Debug data 2 | Debugdata2 | register value; /1 | — | R | RESOLVED | semantic_correlated, source_claim | — |
| input | 3236 | Debug data 3 | Debugdata3 | register value; /1 | — | R | RESOLVED | semantic_correlated, source_claim | — |
| input | 3237 | Debug data 4 | Debugdata4 | register value; /1 | — | R | RESOLVED | semantic_correlated, source_claim | — |
| input | 3238 | Debug data 5 | Debugdata5 | register value; /1 | — | R | RESOLVED | semantic_correlated, source_claim | — |
| input | 3239 | Debug data 6 | Debugdata6 | register value; /1 | — | R | RESOLVED | semantic_correlated, source_claim | — |
| input | 3240 | Debug data 7 | Debugdata7 | register value; /1 | — | R | RESOLVED | semantic_correlated, source_claim | — |
| input | 3241 | Debug data 8 | Debugdata8 | register value; /1 | — | R | RESOLVED | semantic_correlated, source_claim | — |
| input | 3242 | Debug data 9 | Debugdata9 | register value; /1 | — | R | RESOLVED | semantic_correlated, source_claim | — |
| input | 3243 | Debug data 10 | Debugdata10 | register value; /1 | — | R | RESOLVED | semantic_correlated, source_claim | — |
| input | 3244 | Debug data 11 | Debugdata10 | register value; /1 | — | R | RESOLVED | semantic_correlated, source_claim | — |
| input | 3245 | Debug data 12 | Debugdata12 | register value; /1 | — | R | RESOLVED | semantic_correlated, source_claim | — |
| input | 3246 | Debug data 13 | Debugdata13 | register value; /1 | — | R | RESOLVED | semantic_correlated, source_claim | — |
| input | 3247 | Debug data 14 | Debugdata14 | register value; /1 | — | R | RESOLVED | semantic_correlated, source_claim | — |
| input | 3248 | Debug data 15 | Debugdata15 | register value; /1 | — | R | RESOLVED | semantic_correlated, source_claim | — |
| input | 3249 | Debug data 16 | Debugdata16 | register value; /1 | — | R | RESOLVED | semantic_correlated, source_claim | — |
| input | 3250 | Pex1H | PVinverter1outputpowerH | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 3251 | Pex1L | PVinverter1outputpowerL | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 3252 | Pex2H | PVinverter2outputpowerH | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 3253 | Pex2L | PVinverter2outputpowerL | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 3254 | Eex1TodayH | PVinverter1energyTodayH | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 3255 | Eex1TodayL | PVinverter1energyTodayL | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 3256 | Eex2TodayH | PVinverter2energyTodayH | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 3257 | Eex2TodayL | PVinverter2energyTodayL | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 3258 | Eex1TotalH | PVinverter1energyTotalH | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 3259 | Eex1TotalL | PVinverter1energyTotalL | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 3260 | Eex2TotalH | PVinverter2energyTotalH | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 3261 | Eex2TotalL | PVinverter2energyTotalL | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 3262 | uwBatNo | batterypacknumber | register value | BDC reports are updated every 15 minutes | R | SOURCE_ONLY | source_claim | — |
| input | 3263 | BatSerialNum1 | BatterypackserialnumberSN[0]SN[1] | register value | BDC reports are updated every 15 minutes | R | SOURCE_ONLY | source_claim | — |
| input | 3264 | BatSerialNum2 | BatterypackserialnumberSN[2]SN[3] | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 3265 | BatSerialNum3 | BatterypackserialnumberSN[4]SN[5] | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 3266 | BatSerialNum4 | BatterypackserialnumberSN[6]SN[7] | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 3267 | BatSerialNum5 | BatterypackserialnumberSN[8]SN[9] | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 3268 | BatSerialNum6 | Batterypackserial numberSN[10]SN[11] | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 3269 | BatSerialNum7 | Batterypackserial numberSN[12]SN[13] | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 3270 | BatSerialNum8 | Batterypackserial numberSN[14]SN[15] | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 3271 | Reserve | Reserve | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 3272 | Reserve | Reserve | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 3273 | Reserve | Reserve | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 3274 | Reserve | Reserve | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 3275 | Reserve | Reserve | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 3276 | Reserve | Reserve | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 3277 | Reserve | Reserve | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 3278 | Reserve | Reserve | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 3279 | Reserve | Reserve | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 3280 | bClrTodayDataFl ag | Cleardaydataflag | register value | Data of the current day that the server | R | SOURCE_ONLY | source_claim | — |
| input | 3281 | Register 3281 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| input | 3282 | Register 3282 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| input | 3283 | Register 3283 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| input | 3284 | Register 3284 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| input | 3285 | Register 3285 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| input | 3286 | Register 3286 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| input | 3287 | Register 3287 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| input | 3288 | Register 3288 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| input | 3289 | Register 3289 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| input | 3290 | Register 3290 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| input | 3291 | Register 3291 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| input | 3292 | Register 3292 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| input | 3293 | Register 3293 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| input | 3294 | Register 3294 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| input | 3295 | Register 3295 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| input | 3296 | Register 3296 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| input | 3297 | Register 3297 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| input | 3298 | Register 3298 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| input | 3299 | Register 3299 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| input | 3300 | Register 3300 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| input | 3301 | Register 3301 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| input | 3302 | Register 3302 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| input | 3303 | Register 3303 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| input | 3304 | Register 3304 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| input | 3305 | Register 3305 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| input | 3306 | Register 3306 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| input | 3307 | Register 3307 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| input | 3308 | Register 3308 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| input | 3309 | Register 3309 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| input | 3310 | Register 3310 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| input | 3311 | Register 3311 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| input | 3312 | Register 3312 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| input | 3313 | Register 3313 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| input | 3314 | Register 3314 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| input | 3315 | Register 3315 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| input | 3316 | Register 3316 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| input | 3317 | Register 3317 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| input | 3318 | Register 3318 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| input | 3319 | Register 3319 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| input | 3320 | Register 3320 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| input | 3321 | Register 3321 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| input | 3322 | Register 3322 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| input | 3323 | Register 3323 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| input | 3324 | Register 3324 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| input | 3325 | Register 3325 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| input | 3326 | Register 3326 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| input | 3327 | Register 3327 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| input | 3328 | Register 3328 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| input | 3329 | Register 3329 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| input | 3330 | Register 3330 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| input | 3331 | Register 3331 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| input | 3332 | Register 3332 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| input | 3333 | Register 3333 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| input | 3334 | Register 3334 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| input | 3335 | Register 3335 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| input | 3336 | Register 3336 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| input | 3337 | Register 3337 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| input | 3338 | Register 3338 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| input | 3339 | Register 3339 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| input | 3340 | Register 3340 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| input | 3341 | Register 3341 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| input | 3342 | Register 3342 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| input | 3343 | Register 3343 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| input | 3344 | Register 3344 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| input | 3345 | Register 3345 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| input | 3346 | Register 3346 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| input | 3347 | Register 3347 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| input | 3348 | Register 3348 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| input | 3349 | Register 3349 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| input | 3350 | Register 3350 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| input | 3351 | Register 3351 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| input | 3352 | Register 3352 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| input | 3353 | Register 3353 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| input | 3354 | Register 3354 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| input | 3355 | Register 3355 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| input | 3356 | Register 3356 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| input | 3357 | Register 3357 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| input | 3358 | Register 3358 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| input | 3359 | Register 3359 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| input | 3360 | Register 3360 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| input | 3361 | Register 3361 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| input | 3362 | Register 3362 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| input | 3363 | Register 3363 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| input | 3364 | Register 3364 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| input | 3365 | Register 3365 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| input | 3366 | Register 3366 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| input | 3367 | Register 3367 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| input | 3368 | Register 3368 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| input | 3369 | Register 3369 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| input | 3370 | Register 3370 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| input | 3371 | Register 3371 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| input | 3372 | Register 3372 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| input | 3373 | Register 3373 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| input | 3374 | Register 3374 | — | register value | — | R | UNKNOWN_RESERVED | — | — |

### TL3-X / MAX / MID / MAC

The repository groups these 120-family inverter layouts; model-specific differences remain possible.

| Table | Address | Name | Description | Encoding / scale | Unit | Access | Status | Evidence | Notes |
|---|---:|---|---|---|---|---|---|---|---|
| holding | 0 | Inverter Enabled | Theinvertercanbeswitched onandoff,andtheBDCcanbe switchedonandoffforthe battreadyfunction. | register value; /10 | — | R/W | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| holding | 1 | Safety function enable flags | SPI: system protection interface Bit0~3:forCEI0-21 Bit4~6:forSAA | register value | — | W | SOURCE_ONLY | source_claim | — |
| holding | 2 | Persist power-factor commands | Means these settings will be acting or not when next poweron | register value | — | W | RESOLVED | semantic_correlated, source_claim | — |
| holding | 3 | Active power limit setpoint | 255:powerisnotbelimited | register value; /1 | % | W | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| holding | 4 | Reactive power limit setpoint | 255:powerisnotbelimited | register value; /1 | % | W | SOURCE_ONLY | source_claim | — |
| holding | 5 | Power factor target | Inverter output power factor’s10000times | register value; /10000 | pf | W | SOURCE_ONLY | source_claim | — |
| holding | 6 | Rated apparent power | Normal power(high) | register value; /10 | 0.1VA | R | SOURCE_ONLY | source_claim | — |
| holding | 7 | Rated apparent power | Normal power(low) | register value; /10 | 0.1VA | R | SOURCE_ONLY | source_claim | — |
| holding | 8 | Nominal PV voltage | NormalworkPV voltage | register value; /10 | 0.1V | R | SOURCE_ONLY | source_claim | — |
| holding | 9 | Firmware | Firmwareversion (high) | firmware_version; /10 | ASCII | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| holding | 10 | Firmware | Firmwareversion (middle) | register value | ASCII | R | SOURCE_ONLY | source_claim | — |
| holding | 11 | Firmware | Firmwareversion(low) | register value | ASCII | R | SOURCE_ONLY | source_claim | — |
| holding | 12 | Firmware | ControlFirmware version(high) | register value | ASCII | R | SOURCE_ONLY | source_claim | — |
| holding | 13 | Firmware | ControlFirmware version(middle) | register value | ASCII | R | SOURCE_ONLY | source_claim | — |
| holding | 14 | Firmware | ControlFirmware version(low) | register value | ASCII | R | SOURCE_ONLY | source_claim | — |
| holding | 15 | LCD language selection | 0:Italian; 1:English; 2:German; 3:Spanish; 4:French; 5:Chinese; 6：Polish 7：Portugues 8：Hungary | register value | — | W | SOURCE_ONLY | source_claim | — |
| holding | 16 | Country profile configured | CountrySelectedor not | register value | — | W | SOURCE_ONLY | source_claim | — |
| holding | 17 | PV start voltage threshold | Inputstartvoltage | register value; /10 | 0.1V | W | SOURCE_ONLY | source_claim | — |
| holding | 18 | Start-up delay | Starttime | register value; /1 | 1s | W | SOURCE_ONLY | source_claim | — |
| holding | 19 | Restart delay | RestartDelayTime afterfaultback; | register value; /1 | 1s | W | SOURCE_ONLY | source_claim | — |
| holding | 20 | Active power ramp rate (startup) | Powerstartslope | register value; /10 | 0.1% | W | SOURCE_ONLY | source_claim | — |
| holding | 21 | Active power ramp rate (restart) | Powerrestartslope | register value; /10 | 0.1% | W | SOURCE_ONLY | source_claim | — |
| holding | 22 | Modbus RTU baud rate | Select communicationbaudrat e 0:9600bps 1:38400bps | register value | — | W | SOURCE_ONLY | source_claim | — |
| holding | 23 | Serial Number | The Home Assistant integration exposes this as the device serial number and reuses it as the unique identifier. | serial_number; /10 | ASCII | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| holding | 24 | Serial Number | The Home Assistant integration exposes this as the device serial number and reuses it as the unique identifier. | register value | ASCII | R | SOURCE_ONLY | source_claim | — |
| holding | 25 | Serial Number | The Home Assistant integration exposes this as the device serial number and reuses it as the unique identifier. | register value | ASCII | R | SOURCE_ONLY | source_claim | — |
| holding | 26 | Serial Number | The Home Assistant integration exposes this as the device serial number and reuses it as the unique identifier. | register value | ASCII | R | SOURCE_ONLY | source_claim | — |
| holding | 27 | Serial Number | The Home Assistant integration exposes this as the device serial number and reuses it as the unique identifier. | register value | ASCII | R | SOURCE_ONLY | source_claim | — |
| holding | 28 | Inverter Model | Home Assistant renders this value as the string A# B# D# T# P# U# M# S# via the integration's model() helper. Vendor spec lists value pattern `&*5`; digits appear to be stored without the leading letter codes, so treat as encoded tokens until verified on hardware. | register value; /10 | — | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| holding | 29 | Inverter Model | Home Assistant renders this value as the string A# B# D# T# P# U# M# S# via the integration's model() helper. Vendor spec lists value pattern `&*5`; digits appear to be stored without the leading letter codes, so treat as encoded tokens until verified on hardware. | register value | — | R | SOURCE_ONLY | source_claim | — |
| holding | 30 | Modbus slave address | Communicate address | register value | — | W | SOURCE_ONLY | source_claim | — |
| holding | 31 | Firmware update trigger | Updatefirmware | register value | — | W | SOURCE_ONLY | source_claim | — |
| holding | 32 | Reset user configuration | Use with caution; the inverter immediately reboots and loses provisioning data. | register value | — | W | SOURCE_ONLY | source_claim | — |
| holding | 33 | Factory reset | Equivalent to the front-panel factory reset. Requires re-commissioning afterwards. | register value | — | W | SOURCE_ONLY | source_claim | — |
| holding | 34 | Manufacturer information string | The original table lists these words as Manufacturer Info 8-1 (high/middle/low); combine them to read the full string. | register value | ASCII | R | SOURCE_ONLY | source_claim | — |
| holding | 35 | Manufacturer information string | The original table lists these words as Manufacturer Info 8-1 (high/middle/low); combine them to read the full string. | register value | ASCII | R | SOURCE_ONLY | source_claim | — |
| holding | 36 | Manufacturer information string | The original table lists these words as Manufacturer Info 8-1 (high/middle/low); combine them to read the full string. | register value | ASCII | R | SOURCE_ONLY | source_claim | — |
| holding | 37 | Manufacturer information string | The original table lists these words as Manufacturer Info 8-1 (high/middle/low); combine them to read the full string. | register value | ASCII | R | SOURCE_ONLY | source_claim | — |
| holding | 38 | Manufacturer information string | The original table lists these words as Manufacturer Info 8-1 (high/middle/low); combine them to read the full string. | register value | ASCII | R | SOURCE_ONLY | source_claim | — |
| holding | 39 | Manufacturer information string | The original table lists these words as Manufacturer Info 8-1 (high/middle/low); combine them to read the full string. | register value | ASCII | R | SOURCE_ONLY | source_claim | — |
| holding | 40 | Manufacturer information string | The original table lists these words as Manufacturer Info 8-1 (high/middle/low); combine them to read the full string. | register value | ASCII | R | SOURCE_ONLY | source_claim | — |
| holding | 41 | Manufacturer information string | The original table lists these words as Manufacturer Info 8-1 (high/middle/low); combine them to read the full string. | register value | ASCII | R | SOURCE_ONLY | source_claim | — |
| holding | 42 | G100 failsafe enable | EnglishG100failsafeset | register value | — | W | SOURCE_ONLY | source_claim | — |
| holding | 43 | Device Type Code | Vendor spec provides value pattern `&*6`; handle as encoded type/family digits with implied prefixes pending confirmation. | register value; /10 | — | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| holding | 44 | Number Of Trackers And Phases | Inputtrackernumand outputphasenum | register value; /10 | — | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| holding | 45 | System clock year | Localtime | register value | — | W | SOURCE_ONLY | source_claim | — |
| holding | 46 | System clock month | Systemtime-Month | register value | — | W | SOURCE_ONLY | source_claim | — |
| holding | 47 | System clock day | Systemtime-Day | register value | — | W | SOURCE_ONLY | source_claim | — |
| holding | 48 | System clock hour | Systemtime-Hour | register value | — | W | SOURCE_ONLY | source_claim | — |
| holding | 49 | System clock minute | Systemtime-Min | register value | — | W | SOURCE_ONLY | source_claim | — |
| holding | 50 | System clock second | Systemtime-Second | register value | — | W | SOURCE_ONLY | source_claim | — |
| holding | 51 | System clock weekday | SystemWeekly | register value | — | W | SOURCE_ONLY | source_claim | — |
| holding | 52 | Stage 1 undervoltage limit | Gridvoltagelowlimit protect | register value | 0.1V | W | SOURCE_ONLY | source_claim | — |
| holding | 53 | Stage 1 overvoltage limit | Gridvoltagehighlimit protect | register value | 0.1V | W | SOURCE_ONLY | source_claim | — |
| holding | 54 | Stage 1 underfrequency limit | Gridfrequencylow limitprotect | register value | 0.01 Hz | W | SOURCE_ONLY | source_claim | — |
| holding | 55 | Stage 1 overfrequency limit | Gridhigh frequencylimitprotect | register value | 0.01 Hz | W | SOURCE_ONLY | source_claim | — |
| holding | 56 | Stage 2 undervoltage limit | Gridvoltagelowlimit protect2 | register value | 0.1V | W | SOURCE_ONLY | source_claim | — |
| holding | 57 | Stage 2 overvoltage limit | Gridvoltagehighlimit protect2 | register value | 0.1V | W | SOURCE_ONLY | source_claim | — |
| holding | 58 | Stage 2 underfrequency limit | Gridfrequencylow limitprotect2 | register value | 0.01 Hz | W | SOURCE_ONLY | source_claim | — |
| holding | 59 | Stage 2 overfrequency limit | Gridhighfrequency limitprotect2 | register value | 0.01 Hz | W | SOURCE_ONLY | source_claim | — |
| holding | 60 | Stage 3 undervoltage limit | Grid voltage low limit protect3 | register value | 0.1V | W | SOURCE_ONLY | source_claim | — |
| holding | 61 | Stage 3 overvoltage limit | Grid voltage high limit protect3 | register value | 0.1V | W | SOURCE_ONLY | source_claim | — |
| holding | 62 | Stage 3 underfrequency limit | Grid frequency low limitprotect3 | register value | 0.01Hz | W | SOURCE_ONLY | source_claim | — |
| holding | 63 | Stage 3 overfrequency limit | Grid frequency high limitprotect3 | register value | 0.01Hz | W | SOURCE_ONLY | source_claim | — |
| holding | 64 | Reconnect undervoltage limit | Gridlowvoltagelimit connecttoGrid | register value | 0.1V | W | SOURCE_ONLY | source_claim | — |
| holding | 65 | Reconnect overvoltage limit | Gridhighvoltagelimit connecttoGrid | register value | 0.1V | W | SOURCE_ONLY | source_claim | — |
| holding | 66 | Reconnect underfrequency limit | Gridlowfrequency | register value | 0.01 | W | SOURCE_ONLY | source_claim | — |
| holding | 67 | Reconnect overfrequency limit | Gridhighfrequency limitconnecttoGrid | register value | 0.01 Hz | W | SOURCE_ONLY | source_claim | — |
| holding | 68 | Stage 1 undervoltage trip delay | Grid voltage low limit protecttime 1 | register value | Cycle | W | SOURCE_ONLY | source_claim | — |
| holding | 69 | Stage 1 overvoltage trip delay | Grid voltage high limit protecttime 1 | register value | Cycle | W | SOURCE_ONLY | source_claim | — |
| holding | 70 | Stage 2 undervoltage trip delay | Grid voltage low limit protecttime 2 | register value | Cycle | W | SOURCE_ONLY | source_claim | — |
| holding | 71 | Stage 2 overvoltage trip delay | Grid voltage high limit protecttime 2 | register value | Cycle | W | SOURCE_ONLY | source_claim | — |
| holding | 72 | Stage 1 underfrequency trip delay | Grid frequency low limitprotecttime 1 | register value | Cycle | W | SOURCE_ONLY | source_claim | — |
| holding | 73 | Modbus Version | Grid frequency high limitprotecttime 1 | register value | Cycle | W | SOURCE_ONLY | source_claim | — |
| holding | 74 | Stage 2 underfrequency trip delay | Grid frequency low limitprotecttime 2 | register value | Cycle | W | SOURCE_ONLY | source_claim | — |
| holding | 75 | Stage 2 overfrequency trip delay | Grid frequency high limitprotecttime 2 | register value | Cycle | W | SOURCE_ONLY | source_claim | — |
| holding | 76 | Stage 3 undervoltage trip delay | Grid voltage low limit protecttime 3 | register value | Cycle | W | SOURCE_ONLY | source_claim | — |
| holding | 77 | Stage 3 overvoltage trip delay | Grid voltage high limit protecttime 3 | register value | Cycle | W | SOURCE_ONLY | source_claim | — |
| holding | 78 | Stage 3 underfrequency trip delay | Grid frequency low limitprotecttime 3 | register value | Cycle | W | SOURCE_ONLY | source_claim | — |
| holding | 79 | Stage 3 overfrequency trip delay | Grid frequency high limitprotecttime 3 | register value | Cycle | W | SOURCE_ONLY | source_claim | — |
| holding | 80 | Ten-minute overvoltage limit | Voltprotectionfor10 min | register value | 0.1V | W | SOURCE_ONLY | source_claim | — |
| holding | 81 | PV input high-voltage fault | PVVoltageHigh Fault | register value | 0.1V | W | SOURCE_ONLY | source_claim | — |
| holding | 82 | Controller firmware build string | Positions: 0-1 model letters, 2-3 model variant, 4-5 DSP1 build, 6-7 DSP2/M0 build, 8-9 CPLD/AFCI build, 10-11 M3 build. | register value | ASCII | R | SOURCE_ONLY | source_claim | — |
| holding | 83 | Controller firmware build string | Positions: 0-1 model letters, 2-3 model variant, 4-5 DSP1 build, 6-7 DSP2/M0 build, 8-9 CPLD/AFCI build, 10-11 M3 build. | register value | ASCII | R | SOURCE_ONLY | source_claim | — |
| holding | 84 | Controller firmware build string | Positions: 0-1 model letters, 2-3 model variant, 4-5 DSP1 build, 6-7 DSP2/M0 build, 8-9 CPLD/AFCI build, 10-11 M3 build. | register value | ASCII | R | SOURCE_ONLY | source_claim | — |
| holding | 85 | Controller firmware build string | Positions: 0-1 model letters, 2-3 model variant, 4-5 DSP1 build, 6-7 DSP2/M0 build, 8-9 CPLD/AFCI build, 10-11 M3 build. | register value | ASCII | R | SOURCE_ONLY | source_claim | — |
| holding | 86 | Controller firmware build string | Positions: 0-1 model letters, 2-3 model variant, 4-5 DSP1 build, 6-7 DSP2/M0 build, 8-9 CPLD/AFCI build, 10-11 M3 build. | register value | ASCII | R | SOURCE_ONLY | source_claim | — |
| holding | 87 | Controller firmware build string | Positions: 0-1 model letters, 2-3 model variant, 4-5 DSP1 build, 6-7 DSP2/M0 build, 8-9 CPLD/AFCI build, 10-11 M3 build. | register value | ASCII | R | SOURCE_ONLY | source_claim | — |
| holding | 88 | Modbus Version | ModbusVersion | register value; /100 | Int(16 bits) | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| holding | 89 | Power-factor control mode | 0=Unity PF, 1=Fixed PF setpoint, 2=Default PF line, 3=User-defined PF line, 4=Under-excited reactive power, 5=Over-excited reactive power, 6=Q(V) curve, 7=Direct control, 8=Static capacitive QV, 9=Static inductive QV. | register value | — | W | SOURCE_ONLY | source_claim | — |
| holding | 90 | GPRS modem IP/status flags | Bit 0-3: 0=idle, 1=IP read requested, 2=set IP succeeded; Bit 4-7: 0=unknown, 1=modem OK, 2=no SIM, 3=no network, 4=TCP connect fail, 5=TCP connected, etc. | register value | — | W | UNKNOWN_RESERVED | source_claim | — |
| holding | 91 | Frequency derating start | Frequencyderating startpoint | register value | 0.01H Z | W | SOURCE_ONLY | source_claim | — |
| holding | 92 | Frequency derating slope | Frequency–loadlimit rate | register value | 10tim es | W | SOURCE_ONLY | source_claim | — |
| holding | 93 | CEI 0-21 Q(V) point V1S | CEI021V1SQ(v) | register value | 0.1V | W | SOURCE_ONLY | source_claim | — |
| holding | 94 | CEI 0-21 Q(V) point V2S | CEI021V2SQ(v) | register value | 0.1V | W | SOURCE_ONLY | source_claim | — |
| holding | 95 | CEI 0-21 Q(V) point V1L | CEI021V1LQ(v) | register value | 0.1V | W | SOURCE_ONLY | source_claim | — |
| holding | 96 | CEI 0-21 Q(V) point V2L | CEI021V2LQ(v) | register value | 0.1V | W | SOURCE_ONLY | source_claim | — |
| holding | 97 | Q(V) lock-in active power | Q(v)lockinactive powerofCEI021 | register value | Percen t | W | SOURCE_ONLY | source_claim | — |
| holding | 98 | Q(V) lock-out active power | Q(v)lockOutactive powerofCEI021 | register value | Percen t | W | SOURCE_ONLY | source_claim | — |
| holding | 99 | Power-factor curve lock-in voltage | Lockingirdvoltof CEI021PFline | register value | 0.1V | W | SOURCE_ONLY | source_claim | — |
| holding | 100 | Power-factor curve lock-out voltage | Lockoutgirdvoltof CEI021PFline | register value | 0.1V | W | SOURCE_ONLY | source_claim | — |
| holding | 101 | Power-factor adjust value 1 | PFadjustvalue1 | register value | — | W | SOURCE_ONLY | source_claim | — |
| holding | 102 | Power-factor adjust value 2 | PFadjustvalue2 | register value | — | W | SOURCE_ONLY | source_claim | — |
| holding | 103 | Power-factor adjust value 3 | PFadjustvalue3 | register value | — | W | SOURCE_ONLY | source_claim | — |
| holding | 104 | Power-factor adjust value 4 | PFadjustvalue4 | register value | — | W | SOURCE_ONLY | source_claim | — |
| holding | 105 | Power-factor adjust value 5 | PFadjustvalue5 | register value | — | W | SOURCE_ONLY | source_claim | — |
| holding | 106 | Power-factor adjust value 6 | PFadjustvalue6 | register value | — | W | SOURCE_ONLY | source_claim | — |
| holding | 107 | Q(V) response delay | QV Reactive Power delaytime | register value | 1S | W | SOURCE_ONLY | source_claim | — |
| holding | 108 | Over-frequency derating delay | Overfrequency derati ngdelaytime | register value | 50ms | W | SOURCE_ONLY | source_claim | — |
| holding | 109 | Maximum reactive power magnitude | QmaxforQ(V)curve | register value | 0.1% | W | SOURCE_ONLY | source_claim | — |
| holding | 110 | PF curve point 1 load | 255meansnothispoint | register value | percen t | W | SOURCE_ONLY | source_claim | — |
| holding | 111 | PF curve point 1 target | PFlimitlinepoint1 powerfactor | register value | — | W | SOURCE_ONLY | source_claim | — |
| holding | 112 | PF curve point 2 load | 255meansnothispoint | register value | percen t | W | SOURCE_ONLY | source_claim | — |
| holding | 113 | PF curve point 2 target | PFlimitlinepoint 2powerfactor | register value | — | W | SOURCE_ONLY | source_claim | — |
| holding | 114 | PF curve point 3 load | 255meansnothispoint | register value | percen t | W | SOURCE_ONLY | source_claim | — |
| holding | 115 | PF curve point 3 target | PFlimitlinepoint3 powerfactor | register value | — | W | SOURCE_ONLY | source_claim | — |
| holding | 116 | PF curve point 4 load | 255meansnothispoint | register value | percen t | W | SOURCE_ONLY | source_claim | — |
| holding | 117 | PF curve point 4 target | PFlimitlinepoint4 powerfactor | register value | — | W | SOURCE_ONLY | source_claim | — |
| holding | 118 | Module code segments | SxxBxx | register value | — | R | SOURCE_ONLY | source_claim | — |
| holding | 119 | Module code segments | DxxTxx | register value | — | R | SOURCE_ONLY | source_claim | — |
| holding | 120 | Module code segments | PxxUxx | register value | — | R | SOURCE_ONLY | source_claim | — |
| holding | 121 | Module code segments | Mxxxx Power | register value | — | R | SOURCE_ONLY | source_claim | — |
| holding | 122 | Export limit enable mode | ExportLimitenable, 0:DisableexportLimit; 1:Enable485exportLimit; 2:Enable232exportLimit; 3:EnableCTexportLimit; | register value | — | R/W | SOURCE_ONLY | source_claim | — |
| holding | 123 | Export limit power setpoint | ExportLimitPowerRate | register value | 0.1% | R/W | SOURCE_ONLY | source_claim | — |
| holding | 124 | Tracker coupling mode | 0:Independent 1:DCSource 2:Parallel | register value | — | W | SOURCE_ONLY | source_claim | — |
| holding | 125 | Inverter type identifier | Reserved | register value | ASCII | R | UNKNOWN_RESERVED | source_claim | — |
| holding | 126 | Inverter type identifier | Reserved for factory diagnostics; not currently surfaced by the Home Assistant integration. | register value | ASCII | R | UNKNOWN_RESERVED | source_claim | — |
| holding | 127 | Inverter type identifier | Reserved for factory diagnostics; not currently surfaced by the Home Assistant integration. | register value | ASCII | R | UNKNOWN_RESERVED | source_claim | — |
| holding | 128 | Inverter type identifier | Reserved for factory diagnostics; not currently surfaced by the Home Assistant integration. | register value | ASCII | R | UNKNOWN_RESERVED | source_claim | — |
| holding | 129 | Inverter type identifier | Reserved for factory diagnostics; not currently surfaced by the Home Assistant integration. | register value | ASCII | R | UNKNOWN_RESERVED | source_claim | — |
| holding | 130 | Inverter type identifier | Reserved for factory diagnostics; not currently surfaced by the Home Assistant integration. | register value | ASCII | R | UNKNOWN_RESERVED | source_claim | — |
| holding | 131 | Inverter type identifier | Reserved for factory diagnostics; not currently surfaced by the Home Assistant integration. | register value | ASCII | R | UNKNOWN_RESERVED | source_claim | — |
| holding | 132 | Inverter type identifier | Reserved for factory diagnostics; not currently surfaced by the Home Assistant integration. | register value | ASCII | R | UNKNOWN_RESERVED | source_claim | — |
| holding | 133 | Bootloader identifier string | Reserved | register value | ASCII | R | UNKNOWN_RESERVED | source_claim | — |
| holding | 134 | Bootloader identifier string | Reserved | register value | ASCII | R | UNKNOWN_RESERVED | source_claim | — |
| holding | 135 | Bootloader identifier string | Reserved | register value | ASCII | R | UNKNOWN_RESERVED | source_claim | — |
| holding | 136 | Bootloader identifier string | Reserved | register value | ASCII | R | UNKNOWN_RESERVED | source_claim | — |
| holding | 137 | Reactive power direct-control setpoint | Positive values command inductive (lagging) vars; negative values request capacitive (leading) vars. | register value | 0.1var | R/W | SOURCE_ONLY | source_claim | — |
| holding | 138 | Reactive power direct-control setpoint | Positive values command inductive (lagging) vars; negative values request capacitive (leading) vars. | register value | 0.1var | R/W | SOURCE_ONLY | source_claim | — |
| holding | 139 | Reactive priority enable | 0：disable 1：enable | register value | 0/1 | R/W | SOURCE_ONLY | source_claim | — |
| holding | 140 | Reactive priority ratio | Tune together with the direct-control setpoint to limit how much active power is sacrificed for reactive support. | register value | 0.1 | R/W | SOURCE_ONLY | source_claim | — |
| holding | 141 | Night reactive support (SVG) | 0：disable 1：enable | register value | 0/1 | R/W | SOURCE_ONLY | source_claim | — |
| holding | 142 | Frequency-watt boost start | Pair with registers 151, 175, and 176 to set the under-frequency support profile. | register value | 0.01H Z | R/W | SOURCE_ONLY | source_claim | — |
| holding | 143 | Over-frequency recovery point | Works with registers 154-155 and the recovery delay in register 144. | register value | 0.01H Z | R/W | SOURCE_ONLY | source_claim | — |
| holding | 144 | Over-frequency recovery delay | OFDerate RecoverDelayTime | register value | 50ms | R/W | SOURCE_ONLY | source_claim | — |
| holding | 145 | Zero-current detection enable | Disable only when local interconnection rules explicitly forbid the zero-current method. | register value | — | R/W | SOURCE_ONLY | source_claim | — |
| holding | 146 | Zero-current low voltage | ZeroCurrent StaticlowVolt | register value | 0.1V | R/W | SOURCE_ONLY | source_claim | — |
| holding | 147 | Zero-current high voltage | ZeroCurrent StaticHighVolt | register value | 0.1V | R/W | SOURCE_ONLY | source_claim | — |
| holding | 148 | High-voltage derate start | HVoltDerateHighPoint | register value | 0.1V | R/W | SOURCE_ONLY | source_claim | — |
| holding | 149 | High-voltage derate end | Configure together with register 148 to define the slope of the derating curve. | register value | 0.1V | R/W | SOURCE_ONLY | source_claim | — |
| holding | 150 | Q(V) stabilisation time | QVPowerStableTime | register value | 0.1S | R/W | SOURCE_ONLY | source_claim | — |
| holding | 151 | Frequency-watt boost stop | Defines the end point of the frequency-watt boost region together with register 142. | register value | 0.01H Z | R/W | SOURCE_ONLY | source_claim | — |
| holding | 152 | CEI under-frequency ramp start | CEI | register value | 0.01Hz | R/W | SOURCE_ONLY | source_claim | — |
| holding | 153 | CEI under-frequency ramp end | CEI | register value | 0.01Hz | R/W | SOURCE_ONLY | source_claim | — |
| holding | 154 | CEI over-frequency ramp start | CEI | register value | 0.01Hz | R/W | SOURCE_ONLY | source_claim | — |
| holding | 155 | CEI over-frequency ramp end | CEI | register value | 0.01Hz | R/W | SOURCE_ONLY | source_claim | — |
| holding | 156 | CEI undervoltage ramp start | CEI | register value | 0.1V | R/W | SOURCE_ONLY | source_claim | — |
| holding | 157 | CEI undervoltage ramp end | CEI | register value | 0.1V | R/W | SOURCE_ONLY | source_claim | — |
| holding | 158 | CEI overvoltage ramp start | CEI | register value | 0.1V | R/W | SOURCE_ONLY | source_claim | — |
| holding | 159 | CEI overvoltage ramp end | CEI | register value | 0.1V | R/W | SOURCE_ONLY | source_claim | — |
| holding | 160 | Nominal grid voltage selection | UL | register value | — | R/W | SOURCE_ONLY | source_claim | — |
| holding | 161 | Grid watt restoration delay | UL | register value | 20ms | R/W | SOURCE_ONLY | source_claim | — |
| holding | 162 | Reconnect ramp slope | UL | register value | 0.1 | R/W | SOURCE_ONLY | source_claim | — |
| holding | 163 | LFRT stage 1 frequency | UL | register value | 0.01Hz | R/W | SOURCE_ONLY | source_claim | — |
| holding | 164 | LFRT stage 1 duration | UL | register value | 20ms | R/W | SOURCE_ONLY | source_claim | — |
| holding | 165 | LFRT stage 2 frequency | UL | register value | 0.01Hz | R/W | SOURCE_ONLY | source_claim | — |
| holding | 166 | LFRT stage 2 duration | UL | register value | 20ms | R/W | SOURCE_ONLY | source_claim | — |
| holding | 167 | HFRT stage 1 frequency | UL | register value | 0.01Hz | R/W | SOURCE_ONLY | source_claim | — |
| holding | 168 | HFRT stage 1 duration | UL | register value | 20ms | R/W | SOURCE_ONLY | source_claim | — |
| holding | 169 | HFRT stage 2 frequency | UL | register value | 0.01Hz | R/W | SOURCE_ONLY | source_claim | — |
| holding | 170 | HFRT stage 2 duration | UL | register value | 20ms | R/W | SOURCE_ONLY | source_claim | — |
| holding | 171 | HVRT stage 1 voltage | UL | register value | 0.001 Un | R/W | SOURCE_ONLY | source_claim | — |
| holding | 172 | HVRT stage 1 duration | UL | register value | 20ms | R/W | SOURCE_ONLY | source_claim | — |
| holding | 173 | HVRT stage 2 voltage | UL | register value | 0.001 Un | R/W | SOURCE_ONLY | source_claim | — |
| holding | 174 | HVRT stage 2 duration | UL | register value | 0.001 Un | R/W | SOURCE_ONLY | source_claim | — |
| holding | 175 | Under-frequency boost delay | 50549 | register value | 50ms | R/W | SOURCE_ONLY | source_claim | — |
| holding | 176 | Under-frequency boost rate | 50549 | register value | — | R/W | SOURCE_ONLY | source_claim | — |
| holding | 177 | Grid restart high-frequency limit | 50549 | register value | 0.01Hz | R/W | SOURCE_ONLY | source_claim | — |
| holding | 178 | Over-frequency derate response time | Growatt documentation implies steps of roughly 0.1 s; confirm on-site before changing. | register value | — | R/W | SOURCE_ONLY | source_claim | — |
| holding | 179 | Under-frequency boost response time | Steps are vendor-defined; treat as a tuning knob for the frequency-watt boost ramp rate. | register value | — | R/W | SOURCE_ONLY | source_claim | — |
| holding | 180 | Meter link status | 0:Missed,1:Received | register value | — | R/W | SOURCE_ONLY | source_claim | — |
| holding | 181 | Optimizer count | Thetotalnumberofoptimizers connectedtotheinverter | register value | — | R/W | SOURCE_ONLY | source_claim | — |
| holding | 182 | Optimizer configuration flag | 0x00:Notconfiguredsuccess 0x01:Configurationiscomplete | register value | — | R/W | SOURCE_ONLY | source_claim | — |
| holding | 183 | PV string scan mode | 0：Notsupport Other：PvStringNum | register value | — | R/W | SOURCE_ONLY | source_claim | — |
| holding | 184 | BDC parallel count | ThenumberofBDCs | register value | — | R/W | SOURCE_ONLY | source_claim | — |
| holding | 185 | Battery pack count | Totalnumberofbattery | register value | — | R | SOURCE_ONLY | source_claim | — |
| holding | 186 | Reserved | No documented function. | register value | — | R | UNKNOWN_RESERVED | source_claim | — |
| holding | 187 | VPP function enable status | 0：Disable | register value | — | R | SOURCE_ONLY | source_claim | — |
| holding | 188 | Datalogger server status | 0：connectionsucceeded | register value | — | R | SOURCE_ONLY | source_claim | — |
| holding | 189 | Register 189 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| holding | 190 | Register 190 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| holding | 191 | Register 191 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| holding | 192 | Register 192 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| holding | 193 | Register 193 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| holding | 194 | Register 194 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| holding | 195 | Register 195 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| holding | 196 | Register 196 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| holding | 197 | Register 197 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| holding | 198 | Register 198 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| holding | 199 | Register 199 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| holding | 200 | PID control reserved | Reserved | register value | — | R | UNKNOWN_RESERVED | source_claim | — |
| holding | 201 | PID operating mode | 0=Automatic on demand, 1=Continuous, 2=All-night forced run. | register value | — | W | SOURCE_ONLY | source_claim | — |
| holding | 202 | PID breaker control | Leave enabled unless servicing the PID circuit. | register value | — | W | SOURCE_ONLY | source_claim | — |
| holding | 203 | PID output voltage setpoint | PID Output voltage option | register value | V | W | SOURCE_ONLY | source_claim | — |
| holding | 204 | Register 204 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| holding | 205 | Register 205 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| holding | 206 | Register 206 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| holding | 207 | Register 207 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| holding | 208 | Register 208 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| holding | 209 | Alternate serial number | Used by newer dataloggers; apply via commissioning tools when required. | register value | ASCII | R | SOURCE_ONLY | source_claim | — |
| holding | 210 | Alternate serial number | Used by newer dataloggers; apply via commissioning tools when required. | register value | ASCII | R | SOURCE_ONLY | source_claim | — |
| holding | 211 | Alternate serial number | Used by newer dataloggers; apply via commissioning tools when required. | register value | ASCII | R | SOURCE_ONLY | source_claim | — |
| holding | 212 | Alternate serial number | Used by newer dataloggers; apply via commissioning tools when required. | register value | ASCII | R | SOURCE_ONLY | source_claim | — |
| holding | 213 | Alternate serial number | Used by newer dataloggers; apply via commissioning tools when required. | register value | ASCII | R | SOURCE_ONLY | source_claim | — |
| holding | 214 | Alternate serial number | Used by newer dataloggers; apply via commissioning tools when required. | register value | ASCII | R | SOURCE_ONLY | source_claim | — |
| holding | 215 | Alternate serial number | Used by newer dataloggers; apply via commissioning tools when required. | register value | ASCII | R | SOURCE_ONLY | source_claim | — |
| holding | 216 | Alternate serial number | Used by newer dataloggers; apply via commissioning tools when required. | register value | ASCII | R | SOURCE_ONLY | source_claim | — |
| holding | 217 | Alternate serial number | Used by newer dataloggers; apply via commissioning tools when required. | register value | ASCII | R | SOURCE_ONLY | source_claim | — |
| holding | 218 | Alternate serial number | Used by newer dataloggers; apply via commissioning tools when required. | register value | ASCII | R | SOURCE_ONLY | source_claim | — |
| holding | 219 | Alternate serial number | Used by newer dataloggers; apply via commissioning tools when required. | register value | ASCII | R | SOURCE_ONLY | source_claim | — |
| holding | 220 | Alternate serial number | Used by newer dataloggers; apply via commissioning tools when required. | register value | ASCII | R | SOURCE_ONLY | source_claim | — |
| holding | 221 | Alternate serial number | Used by newer dataloggers; apply via commissioning tools when required. | register value | ASCII | R | SOURCE_ONLY | source_claim | — |
| holding | 222 | Alternate serial number | Used by newer dataloggers; apply via commissioning tools when required. | register value | ASCII | R | SOURCE_ONLY | source_claim | — |
| holding | 223 | Alternate serial number | Used by newer dataloggers; apply via commissioning tools when required. | register value | ASCII | R | SOURCE_ONLY | source_claim | — |
| holding | 224 | Register 224 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| holding | 225 | Register 225 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| holding | 226 | Register 226 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| holding | 227 | Register 227 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| holding | 228 | Register 228 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| holding | 229 | Energy calibration factor | 1-1000,(Percentratio) | register value | 0.1% | R/W | SOURCE_ONLY | source_claim | — |
| holding | 230 | Anti-islanding override | Never disable anti-islanding on a grid-connected installation unless explicitly authorised. | register value | — | W | SOURCE_ONLY | source_claim | — |
| holding | 231 | Fan self-test trigger | The inverter clears the flag automatically once the test completes. | register value | — | W | SOURCE_ONLY | source_claim | — |
| holding | 232 | Neutral line monitoring enable | EnableNLineofgrid | register value | — | W | SOURCE_ONLY | source_claim | — |
| holding | 233 | Hardware warning flags | wCheckHardware Bit0:GFCIBreak; Bit1:SPSDamage Bit8:EepromReadWarni ng Bit9:EEWriteWarning …… | register value | — | R | SOURCE_ONLY | source_claim | — |
| holding | 234 | Hardware warning flags (reserved word) | Monitor for future firmware updates. | register value | — | R | UNKNOWN_RESERVED | source_claim | — |
| holding | 235 | Neutral-to-ground detection | Should remain enabled for safety compliance. | register value | — | W | SOURCE_ONLY | source_claim | — |
| holding | 236 | Non-standard voltage range | 0=Standard range, 1=Voltage grade 1, 2=Voltage grade 2. | register value | — | W | SOURCE_ONLY | source_claim | — |
| holding | 237 | Appointed spec override | Bit 0: Hungary | register value | Binary | W | SOURCE_ONLY | source_claim | — |
| holding | 238 | Fast MPPT mode | Reserved | register value | — | W | UNKNOWN_RESERVED | source_claim | — |
| holding | 239 | Reserved | Reserved | register value | — | R | UNKNOWN_RESERVED | source_claim | — |
| holding | 240 | Commissioning step index | Internal step counter used during factory self-check sequences. Installers should leave this value unchanged. | register value | — | R/W | SOURCE_ONLY | source_claim | — |
| holding | 241 | Installer longitude word | Longitude | register value | — | R/W | SOURCE_ONLY | source_claim | — |
| holding | 242 | Installer latitude word | Latitude | register value | — | R/W | SOURCE_ONLY | source_claim | — |
| holding | 243 | Register 243 | — | register value | — | R | UNKNOWN_RESERVED | source_claim | — |
| holding | 244 | Register 244 | — | register value | — | R | UNKNOWN_RESERVED | source_claim | — |
| holding | 245 | Register 245 | — | register value | — | R | UNKNOWN_RESERVED | source_claim | — |
| holding | 246 | Register 246 | — | register value | — | R | UNKNOWN_RESERVED | source_claim | — |
| holding | 247 | Register 247 | — | register value | — | R | UNKNOWN_RESERVED | source_claim | — |
| holding | 248 | Register 248 | — | register value | — | R | UNKNOWN_RESERVED | source_claim | — |
| holding | 249 | Register 249 | — | register value | — | R | UNKNOWN_RESERVED | source_claim | — |
| input | 0 | Inverter status | InverterStatus | register value; /10 | — | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 1 | PV input power | PpvH | register value; /10 | W | R/W | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 2 | PV input power | PpvL | register value; /10 | 0.1W | R/W | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3 | PV1 DC voltage | Vpv1 | register value; /10 | V | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 4 | PV1 DC current | PV1Curr | register value; /10 | A | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 5 | PV1 DC power | Ppv1H | register value; /10 | W | R/W | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 6 | PV1 DC power | Ppv1L | register value; /10 | 0.1W | R/W | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 7 | PV2 DC voltage | Vpv2 | register value; /10 | V | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 8 | PV2 DC current | PV2Curr | register value; /10 | A | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 9 | PV2 DC power | Ppv2H | register value; /10 | W | R/W | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 10 | PV2 DC power | Ppv2L | register value; /10 | 0.1W | R/W | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 11 | PV3 DC voltage | Vpv3 | register value; /10 | V | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 12 | PV3 DC current | PV3Curr | register value; /10 | A | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 13 | PV3 DC power | Ppv3H | register value; /10 | W | R/W | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 14 | PV3 DC power | Ppv3L | register value; /10 | 0.1W | R/W | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 15 | PV4 DC voltage | Vpv4 | register value; /10 | V | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 16 | PV4 DC current | PV4Curr | register value; /10 | A | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 17 | PV4 DC power | Ppv4H | register value; /10 | W | R/W | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 18 | PV4 DC power | Ppv4L | register value; /10 | 0.1W | R/W | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 19 | PV5 DC voltage | Vpv5 | register value; /10 | V | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 20 | PV5 DC current | PV5Curr | register value; /10 | A | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 21 | PV5 DC power | Ppv5H | register value; /10 | W | R/W | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 22 | PV5 DC power | Ppv5L | register value; /10 | 0.1W | R/W | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 23 | PV6 DC voltage | Vpv6 | register value; /10 | V | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 24 | PV6 DC current | PV6Curr | register value; /10 | A | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 25 | PV6 DC power | PV6inputpower(high) | register value; /10 | W | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 26 | PV6 DC power | PV6inputpower(low) | register value; /10 | W | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 27 | PV7 DC voltage | PV7voltage | register value; /10 | V | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 28 | PV7 DC current | PV7inputcurrent | register value; /10 | A | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 29 | PV7 DC power | PV7inputpower(high) | register value; /10 | W | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 30 | PV7 DC power | PV7inputpower(low) | register value; /10 | W | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 31 | PV8 DC voltage | PV8voltage | register value; /10 | V | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 32 | PV8 DC current | PV8inputcurrent | register value; /10 | A | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 33 | PV8 DC power | PV8inputpower(high) | register value; /10 | W | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 34 | PV8 DC power | PV8inputpower(low) | register value; /10 | W | R | RESOLVED | semantic_correlated, source_claim | — |
| input | 35 | AC output power | Outputpower(high) | register value; /10 | W | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 36 | AC output power | Outputpower(low) | register value; /10 | W | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 37 | Grid frequency | Gridfrequency | register value; /100 | Hz | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 38 | AC phase L1 voltage | Three/singlephasegridvoltage | register value; /10 | V | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 39 | AC phase L1 current | Three/singlephasegridoutputcurrent | register value; /10 | A | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 40 | AC phase L1 power | Three/single phase grid output watt VA(high) | register value; /10 | VA | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 41 | AC phase L1 power | Three/single phase grid output watt VA(low) | register value; /10 | W | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 42 | AC phase L2 voltage | Threephasegridvoltage | register value; /10 | V | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 43 | AC phase L2 current | Threephasegridoutputcurrent | register value; /10 | A | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 44 | AC phase L2 power | Threephasegridoutputpower(high) | register value; /10 | VA | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 45 | AC phase L2 power | Threephasegridoutputpower(low) | register value; /10 | W | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 46 | AC phase L3 voltage | Threephasegridvoltage | register value; /10 | V | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 47 | AC phase L3 current | Threephasegridoutputcurrent | register value; /10 | A | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 48 | AC phase L3 power | Threephasegridoutputpower(high) | register value; /10 | VA | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 49 | AC phase L3 power | Threephasegridoutputpower(low) | register value; /10 | W | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 50 | Vac_RS | Threephasegridvoltage | register value | V | R | RESOLVED | semantic_correlated, source_claim | — |
| input | 51 | Vac_ST | Threephasegridvoltage | register value | V | R | RESOLVED | semantic_correlated, source_claim | — |
| input | 52 | Vac_TR | Threephasegridvoltage | register value | V | R | RESOLVED | semantic_correlated, source_claim | — |
| input | 53 | Output energy today | Todaygenerateenergy(high) | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 54 | Output energy today | Todaygenerateenergy(low) | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 55 | Output energy total | Totalgenerateenergy(high) | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 56 | Output energy total | Totalgenerateenergy(low) | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 57 | Run time | Raw counter counts seconds; divide by 7200 to obtain hours. | register value; /7200 | s | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 58 | Run time | Raw counter counts seconds; divide by 7200 to obtain hours. | register value; /7200 | h | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 59 | PV1 energy today | PV1Energytoday(high) | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 60 | PV1 energy today | PV1Energytoday(low) | register value; /10 | kWh | R | RESOLVED | semantic_correlated, source_claim | — |
| input | 61 | PV1 energy total | PV1Energytotal(high) | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 62 | PV1 energy total | PV1Energytotal(low) | register value; /10 | kWh | R | RESOLVED | semantic_correlated, source_claim | — |
| input | 63 | PV2 energy today | PV2Energytoday(high) | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 64 | PV2 energy today | PV2Energytoday(low) | register value; /10 | kWh | R | RESOLVED | semantic_correlated, source_claim | — |
| input | 65 | PV2 energy total | PV2Energytotal(high) | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 66 | PV2 energy total | PV2Energytotal(low) | register value; /10 | kWh | R | RESOLVED | semantic_correlated, source_claim | — |
| input | 67 | PV3 energy today | PV3Energytoday(high) | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 68 | PV3 energy today | PV3Energytoday(low) | register value; /10 | kWh | R | RESOLVED | semantic_correlated, source_claim | — |
| input | 69 | PV3 energy total | PV3Energytotal(high) | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 70 | PV3 energy total | PV3Energytotal(low) | register value; /10 | kWh | R | RESOLVED | semantic_correlated, source_claim | — |
| input | 71 | PV4 energy today | PV4Energytoday(high) | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 72 | PV4 energy today | PV4Energytoday(low) | register value; /10 | kWh | R | RESOLVED | semantic_correlated, source_claim | — |
| input | 73 | PV4 energy total | PV4Energytotal(high) | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 74 | PV4 energy total | PV4Energytotal(low) | register value; /10 | kWh | R | RESOLVED | semantic_correlated, source_claim | — |
| input | 75 | PV5 energy today | PV5Energytoday(high) | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 76 | PV5 energy today | PV5Energytoday(low) | register value; /10 | kWh | R | RESOLVED | semantic_correlated, source_claim | — |
| input | 77 | PV5 energy total | PV5Energytotal(high) | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 78 | PV5 energy total | PV5Energytotal(low) | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 79 | PV6 energy today | PV6Energytoday(high) | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 80 | PV6 energy today | PV6Energytoday(low) | register value; /10 | kWh | R | RESOLVED | semantic_correlated, source_claim | — |
| input | 81 | PV6 energy total | PV6Energytotal(high) | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 82 | PV6 energy total | PV6Energytotal(low) | register value; /10 | kWh | R | RESOLVED | semantic_correlated, source_claim | — |
| input | 83 | PV7 energy today | PV7Energytoday(high) | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 84 | PV7 energy today | PV7Energytoday(low) | register value; /10 | kWh | R | RESOLVED | semantic_correlated, source_claim | — |
| input | 85 | PV7 energy total | PV7Energytotal(high) | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 86 | PV7 energy total | PV7Energytotal(low) | register value; /10 | kWh | R | RESOLVED | semantic_correlated, source_claim | — |
| input | 87 | PV8 energy today | PV8Energytoday(high) | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 88 | PV8 energy today | PV8Energytoday(low) | register value; /10 | kWh | R | RESOLVED | semantic_correlated, source_claim | — |
| input | 89 | PV8 energy total | PV8Energytotal(high) | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 90 | PV8 energy total | PV8Energytotal(low) | register value; /10 | kWh | R | RESOLVED | semantic_correlated, source_claim | — |
| input | 91 | PV energy total | PVEnergytotal(high) | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 92 | PV energy total | PVEnergytotal(low) | register value; /10 | kWh | R | RESOLVED | semantic_correlated, source_claim | — |
| input | 93 | Inverter temperature | Invertertemperature | register value; /10 | °C | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 94 | IPM temperature | TheinsideIPMininverterTemperature | register value; /10 | °C | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 95 | Boost temperature | Boosttemperature | register value; /10 | °C | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 96 | Temp4 | Temp4 | register value | reserved | R | SOURCE_ONLY | source_claim | — |
| input | 97 | uwBatVolt_DSP | BatVolt_DSP | register value | BatVolt(DSP) | R | SOURCE_ONLY | source_claim | — |
| input | 98 | P-bus voltage | PBusinsideVoltage | register value; /10 | V | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 99 | N-bus voltage | NBusinsideVoltage | register value; /10 | V | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 100 | IPF | InverteroutputPFnow | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 101 | Output power percentage | RealOutputpowerPercent | register value; /10 | % | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 102 | OPFullwattH | OutputMaxpowerLimitedhigh | register value | W | R | RESOLVED | semantic_correlated, source_claim | — |
| input | 103 | OPFullwattL | OutputMaxpowerLimitedlow | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 104 | Derating mode | DeratingMode | register value; /10 | — | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 105 | Fault code | Inverterfaultmaincode | register value; /10 | — | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 106 | Register 106 | — | register value | — | R | UNKNOWN_RESERVED | source_claim | — |
| input | 107 | FaultSubcode | Inverterfaultsubcode | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 108 | RemoteCtrlEn | / | register value | StoragePow er(SPA) | R | SOURCE_ONLY | source_claim | — |
| input | 109 | RemoteCtrlPow er | / | register value | StoragePow er(SPA) | R | SOURCE_ONLY | source_claim | — |
| input | 110 | Warning code | WarningbitH | register value; /10 | — | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 111 | Warning code | Inverterwarnsubcode | register value; /10 | — | R | SOURCE_ONLY | source_claim | — |
| input | 112 | WarnMaincode | Inverterwarnmaincode | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 113 | real Power Percent | realPowerPercent | register value | MAX | R | SOURCE_ONLY | source_claim | — |
| input | 114 | inv start delay time | invstartdelaytime | register value | MAX | R | SOURCE_ONLY | source_claim | — |
| input | 115 | bINVAllFaultCod e | bINVAllFaultCode | register value | MAX | R | SOURCE_ONLY | source_claim | — |
| input | 116 | AC charge Power_H | Gridpowertolocalload | register value | Storage Power | R | SOURCE_ONLY | source_claim | — |
| input | 117 | AC charge Power_L | Gridpowertolocalload | register value | Storage Power | R | SOURCE_ONLY | source_claim | — |
| input | 118 | Priority | 0:LoadFirst | register value | Storage | R | RESOLVED | semantic_correlated, source_claim | — |
| input | 119 | BatteryType | 0：Lead-acid 1：Lithiumbattery | register value | — | R | RESOLVED | semantic_correlated, source_claim | — |
| input | 120 | AutoProofreadC MD | Aging mode Auto-calibration command | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 121 | Register 121 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| input | 122 | Register 122 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| input | 123 | Register 123 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| input | 124 | reserved | reserved | register value | — | R | UNKNOWN_RESERVED | source_claim | — |
| input | 125 | PIDPV1+Voltage | PIDPV1+Voltage | register value | 0.1V | R | SOURCE_ONLY | source_claim | — |
| input | 126 | PIDPV1+Current | PIDPV1+Current | register value | 0.1mA | R | SOURCE_ONLY | source_claim | — |
| input | 127 | PIDPV2+Voltage | PIDPV2+Voltage | register value | 0.1V | R | SOURCE_ONLY | source_claim | — |
| input | 128 | PIDPV2+Current | PIDPV2+Current | register value | 0.1mA | R | SOURCE_ONLY | source_claim | — |
| input | 129 | PIDPV3+Voltage | PIDPV3+Voltage | register value | 0.1V | R | SOURCE_ONLY | source_claim | — |
| input | 130 | PIDPV3+Current | PIDPV3+Current | register value | 0.1mA | R | SOURCE_ONLY | source_claim | — |
| input | 131 | PIDPV4+Voltage | PIDPV4+Voltage | register value | 0.1V | R | SOURCE_ONLY | source_claim | — |
| input | 132 | PIDPV4+Current | PIDPV4+Current | register value | 0.1mA | R | SOURCE_ONLY | source_claim | — |
| input | 133 | PIDPV5+Voltage | PIDPV5+Voltage | register value | 0.1V | R | SOURCE_ONLY | source_claim | — |
| input | 134 | PIDPV5+Current | PIDPV5+Current | register value | 0.1mA | R | SOURCE_ONLY | source_claim | — |
| input | 135 | PIDPV6+Voltage | PIDPV6+Voltage | register value | 0.1V | R | SOURCE_ONLY | source_claim | — |
| input | 136 | PIDPV6+Current | PIDPV6+Current | register value | 0.1mA | R | SOURCE_ONLY | source_claim | — |
| input | 137 | PIDPV7+Voltage | PIDPV7+Voltage | register value | 0.1V | R | SOURCE_ONLY | source_claim | — |
| input | 138 | PIDPV7+Current | PIDPV7+Current | register value | 0.1mA | R | SOURCE_ONLY | source_claim | — |
| input | 139 | PIDPV8+Voltage | PIDPV8+Voltage | register value | 0.1V | R | SOURCE_ONLY | source_claim | — |
| input | 140 | PIDPV8+Current | PIDPV8+Current | register value | 0.1mA | R | SOURCE_ONLY | source_claim | — |
| input | 141 | PIDStatus | PIDStatus | register value | — | W | SOURCE_ONLY | source_claim | — |
| input | 142 | V_String1 | V_String1 | register value | 0.1V | R | SOURCE_ONLY | source_claim | — |
| input | 143 | Curr_String1 | Curr_String1 | register value | 0.1A | R | SOURCE_ONLY | source_claim | — |
| input | 144 | V_String2 | V_String2 | register value | 0.1V | R | SOURCE_ONLY | source_claim | — |
| input | 145 | Curr_String2 | PVString2current | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 146 | V_String3 | PVString3voltage | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 147 | Curr_String3 | PVString3current | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 148 | V_String4 | PVString4voltage | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 149 | Curr_String4 | PVString4current | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 150 | V_String5 | PVString5voltage | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 151 | Curr_String5 | PVString5current | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 152 | V_String6 | PVString6voltage | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 153 | Curr_String6 | PVString6current | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 154 | V_String7 | PVString7voltage | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 155 | Curr_String7 | PVString7current | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 156 | V_String8 | PVString8voltage | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 157 | Curr_String8 | PVString8current | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 158 | V_String9 | PVString9voltage | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 159 | Curr_String9 | PVString9current | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 160 | V_String10 | PVString10voltage | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 161 | Curr_String10 | PVString10current | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 162 | V_String11 | PVString11voltage | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 163 | Curr_String11 | PVString11current | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 164 | V_String12 | PVString12voltage | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 165 | Curr_String12 | PVString12current | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 166 | V_String13 | PVString13voltage | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 167 | Curr_String13 | PVString13current | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 168 | V_String14 | PVString14voltage | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 169 | Curr_String14 | PVString14current | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 170 | V_String15 | PVString15voltage | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 171 | Curr_String15 | PVString15current | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 172 | V_String16 | PVString16voltage | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 173 | Curr_String16 | PVString16current | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 174 | StrUnmatch | Bit0~15:String1~16unmatch | register value | suggestive | R | SOURCE_ONLY | source_claim | — |
| input | 175 | StrCurrentUnblan ce | Bit0~15:String1~16currentunblance | register value | suggestive | R | SOURCE_ONLY | source_claim | — |
| input | 176 | StrDisconnect | Bit0~15:String1~16disconnect | register value | suggestive | R | SOURCE_ONLY | source_claim | — |
| input | 177 | PIDFaultCode | Bit0:Outputovervoltage Bit1:ISOfault Bit2:BUSvoltageabnormal Bit3~15:reserved | register value | — | R | UNKNOWN_RESERVED | source_claim | — |
| input | 178 | StringPrompt | StringPrompt Bit0:StringUnmatch Bit1:StrDisconnect Bit2:StrCurrentUnblance | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 179 | PVWarningValue | PVWarningValue | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 180 | DSP075 Warning Value | DSP075WarningValue | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 181 | DSP075 Fault Value | DSP075FaultValue | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 182 | DSP067 Debug Data1 | DSP067DebugData1 | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 183 | DSP067 Debug Data2 | DSP067DebugData2 | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 184 | DSP067 Debug Data3 | DSP067DebugData3 | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 185 | DSP067 Debug Data4 | DSP067DebugData4 | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 186 | DSP067 Debug Data5 | DSP067DebugData5 | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 187 | DSP067 Debug Data6 | DSP067DebugData6 | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 188 | DSP067 Debug Data7 | DSP067DebugData7 | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 189 | DSP067 Debug Data8 | DSP067DebugData8 | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 190 | DSP075 Debug Data1 | DSP075DebugData1 | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 191 | DSP075 Debug Data2 | DSP075DebugData2 | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 192 | DSP075 Debug Data3 | DSP075DebugData3 | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 193 | DSP075 Debug Data4 | DSP075DebugData4 | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 194 | DSP075 Debug Data55 | DSP075DebugData5 | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 195 | DSP075 Debug Data6 | DSP075DebugData6 | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 196 | DSP075 Debug Data7 | DSP075DebugData7 | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 197 | DSP075 Debug Data8 | DSP075DebugData8 | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 198 | bUSBAgingTestOk Flag | USBAgingTestOkFlag | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 199 | bFlashEraseAging OkFlag | FlashEraseAgingOkFlag | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 200 | PVISO | PVISOValue | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 201 | R_DCI | RDCICurr | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 202 | S_DCI | SDCICurr | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 203 | T_DCI | TDCICurr | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 204 | PID_Bus | PIDBusVolt | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 205 | GFCI | GFCICurr | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 206 | SVG/APF Status+SVGAPFEq ualRatio | SVG/APFStatus+SVGAPFEqualRatio | register value | — | W | SOURCE_ONLY | source_claim | — |
| input | 207 | CT_I_R | RphaseloadsidecurrentforSVG | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 208 | CT_I_S | SphaseloadsidecurrentforSVG | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 209 | CT_I_T | TphaseloadsidecurrentforSVG | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 210 | CT_Q_RH | R phase load side output reactive powerforSVG(High) | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 211 | CT_Q_RL | R phase load side output reactive powerforSVG(low) | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 212 | CT_Q_SH | S phase load side output reactive powerforSVG(High) | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 213 | CT_Q_SL | S phase load side output reactive powerforSVG(low) | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 214 | CT_Q_TH | T phase load side output reactive powerforSVG(High) | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 215 | CT_Q_TL | T phase load side output reactive powerforSVG(low) | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 216 | CTHAR_I_R | Rphaseloadsideharmonic | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 217 | CTHAR_I_S | Sphaseloadsideharmonic | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 218 | CTHAR_I_T | Tphaseloadsideharmonic | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 219 | COMP_Q_RH | R phase compensate reactive power forSVG(High) | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 220 | COMP_Q_RL | R phase compensate reactive power forSVG(low) | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 221 | COMP_Q_SH | S phase compensate reactive power forSVG(High) | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 222 | COMP_Q_SL | S phase compensate reactive power | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 223 | COMP_Q_TH | T phase compensate reactive power forSVG(High) | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 224 | COMP_Q_TL | T phase compensate reactive power forSVG(low) | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 225 | COMPHAR_I_R | R phase compensate harmonic for SVG | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 226 | COMPHAR_I_S | S phase compensate harmonic for SVG | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 227 | COMPHAR_I_T | T phase compensate harmonic for SVG | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 228 | bRS232AgingTest OkFlag | RS232AgingTestOkFlag | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 229 | bFanFaultBit | Bit0:Fan1faultbit Bit1:Fan2faultbit Bit2:Fan3faultbit Bit3:Fan4faultbit Bit4-7:Reserved | register value | — | R | UNKNOWN_RESERVED | source_claim | — |
| input | 230 | SacH | OutputapparentpowerH | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 231 | SacL | OutputapparentpowerL | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 232 | ReActPowerH | RealOutputReactivePowerH | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 233 | ReActPowerL | RealOutputReactivePowerL | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 234 | Output reactive power | NominalOutputReactivePowerH | register value; /10 | var | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 235 | Output reactive power | NominalOutputReactivePowerL | register value; /10 | var | R | SOURCE_ONLY | source_claim | — |
| input | 236 | Reactive energy total | Reactivepowergeneration | register value; /10 | kvarh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 237 | Reactive energy total | Reactivepowergeneration | register value; /10 | kvarh | R | SOURCE_ONLY | source_claim | — |
| input | 238 | bAfciStatus | 0：Waiting 1：Self-checkstate 2：Detectpullarcstate 3：Fault 4：Update | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 239 | uwPresentFFTValu e[CHANNEL_A] | PresentFFTValue[CHANNEL_A] | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 240 | uwPresentFFTValu e[CHANNEL_B] | PresentFFTValue[CHANNEL_B] | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 241 | DSP067 Debug Data1 | DSP067DebugData1 | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 242 | DSP067 Debug Data2 | DSP067DebugData2 | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 243 | DSP067 Debug | DSP067DebugData3 | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 244 | DSP067 Debug Data4 | DSP067DebugData4 | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 245 | DSP067 Debug Data5 | DSP067DebugData5 | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 246 | DSP067 Debug Data6 | DSP067DebugData6 | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 247 | DSP067 Debug Data7 | DSP067DebugData7 | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 248 | DSP067 Debug Data8 | DSP067DebugData8 | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 249 | Register 249 | — | register value | reserved | R | UNKNOWN_RESERVED | source_claim | — |
| input | 875 | Vpv9 | PV9 voltage | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 876 | PV9Curr | PV9 Inputcurrent | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 877 | Ppv9H | PV9 inputpower(High) | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 878 | Ppv9L | PV9 inputpower(Low) | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 879 | Vpv10 | PV10voltage | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 880 | PV10Curr | PV10Inputcurrent | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 881 | Ppv10H | PV10inputpower(High) | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 882 | Ppv10L | PV10inputpower(Low) | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 883 | Vpv11 | PV11voltage | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 884 | PV11Curr | PV11Inputcurrent | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 885 | Ppv11H | PV11inputpower(High) | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 886 | Ppv11L | PV11inputpower(Low) | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 887 | Vpv12 | PV12voltage | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 888 | PV12Curr | PV12Inputcurrent | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 889 | Ppv12H | PV12inputpower(High) | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 890 | Ppv12L | PV12inputpower(Low) | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 891 | Vpv13 | PV13voltage | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 892 | PV13Curr | PV13Inputcurrent | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 893 | Ppv13H | PV13inputpower(High) | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 894 | Ppv13L | PV13inputpower(Low) | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 895 | Vpv14 | PV14voltage | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 896 | PV14Curr | PV14Inputcurrent | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 897 | Ppv14H | PV14inputpower(High) | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 898 | Ppv14L | PV14inputpower(Low) | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 899 | Vpv15 | PV15voltage | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 900 | PV15Curr | PV15Inputcurrent | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 901 | Ppv15H | PV15inputpower(High) | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 902 | Ppv15L | PV15inputpower(Low) | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 903 | Vpv16 | PV16voltage | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 904 | PV16Curr | PV16Inputcurrent | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 905 | Ppv16H | PV16inputpower(High) | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 906 | Ppv16L | PV16inputpower(Low) | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 907 | Epv9_todayH | PV9energytoday(High) | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 908 | Epv9_todayL | PV9energytoday(Low) | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 909 | Epv9_totalH | PV9energytotal(High) | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 910 | Epv9_totalL | PV9energytotal(Low) | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 911 | Epv10_todayH | PV10energytoday(High) | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 912 | Epv10_todayL | PV10energytoday(Low) | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 913 | Epv10_totalH | PV10energytotal(High) | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 914 | Epv10_totalL | PV10energytotal(Low) | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 915 | Epv11_todayH | PV11energytoday(High) | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 916 | Epv11_todayL | PV11energytoday(Low) | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 917 | Epv11_totalH | PV11energytotal(High) | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 918 | Epv11_totalL | PV11energytotal(Low) | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 919 | Epv12_todayH | PV12energytoday(High) | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 920 | Epv12_todayL | PV12energytoday(Low) | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 921 | Epv12_totalH | PV12energytotal(High) | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 922 | Epv12_totalL | PV12energytotal(Low) | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 923 | Epv13_todayH | PV13energytoday(High) | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 924 | Epv13_todayL | PV13energytoday(Low) | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 925 | Epv13_totalH | PV13energytotal(High) | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 926 | Epv13_totalL | PV13energytotal(Low) | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 927 | Epv14_todayH | PV14energytoday(High) | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 928 | Epv14_todayL | PV14energytoday(Low) | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 929 | Epv14_totalH | PV14energytotal(High) | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 930 | Epv14_totalL | PV14energytotal(Low) | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 931 | Epv15_todayH | PV15energytoday(High) | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 932 | Epv15_todayL | PV15energytoday(Low) | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 933 | Epv15_totalH | PV15energytotal(High) | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 934 | Epv15_totalL | PV15energytotal(Low) | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 935 | Epv16_todayH | PV16energytoday(High) | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 936 | Epv16_todayL | PV16energytoday(Low) | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 937 | Epv16_totalH | PV16energytotal(High) | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 938 | Epv16_totalL | PV16energytotal(Low) | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 939 | PIDPV9+Voltage | PID PV9PE Volt/ Flyspan voltage (MAXHV) | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 940 | PIDPV9+Current | PIDPV9PECurrent | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 941 | PID PV10+ Voltage | PID PV10PE/ Flyspan voltage (MAX HV) | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 942 | PID PV10+ Current | PIDPV10PECurrent | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 943 | PID PV11+ Voltage | PID PV11PE Volt/ Flyspan voltage (MAXHV) | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 944 | PID PV11+ Current | PIDPV11PECurrent | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 945 | PID PV12+ Voltage | PID PV12PE Volt/ Flyspan voltage (MAXHV) | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 946 | PID PV12+ Current | PIDPV12PECurrent | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 947 | PID PV13+ Voltage | PID PV13PE Volt/ Flyspan voltage (MAXHV) | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 948 | PID PV13+ Current | PIDPV13PECurrent | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 949 | PID PV14+ Voltage | PID PV14PE Volt/ Flyspan voltage (MAXHV) | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 950 | PID PV14+ Current | PIDPV14PECurrent | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 951 | PID PV15+ Voltage | PID PV15PE Volt/ Flyspan voltage (MAXHV) | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 952 | PID PV15+ Current | PIDPV15PECurrent | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 953 | PID PV16+ Voltage | PID PV16PE Volt/ Flyspan voltage (MAXHV) | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 954 | PID PV16+ Current | PIDPV16PECurrent | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 955 | V_String17 | PVString17voltage | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 956 | Curr_String17 | PVString17Current | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 957 | V_String18 | PVString18voltage | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 958 | Curr_String18 | PVString18Current | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 959 | V_String19 | PVString19voltage | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 960 | Curr_String19 | PVString19Current | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 961 | V_String20 | PVString20voltage | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 962 | Curr_String20 | PVString20Current | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 963 | V_String21 | PVString21voltage | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 964 | Curr_String21 | PVString21Current | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 965 | V_String22 | PVString22voltage | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 966 | Curr_String22 | PVString22Current | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 967 | V_String23 | PVString23voltage | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 968 | Curr_String23 | PVString23Current | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 969 | V_String24 | PVString24voltage | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 970 | Curr_String24 | 0.1A | register value | -15A~15A | R | SOURCE_ONLY | source_claim | — |
| input | 971 | V_String25 | 0.1V | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 972 | Curr_String25 | 0.1A | register value | -15A~15A | R | SOURCE_ONLY | source_claim | — |
| input | 973 | V_String26 | 0.1V | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 974 | Curr_String26 | 0.1A | register value | -15~15A | R | SOURCE_ONLY | source_claim | — |
| input | 975 | V_String27 | 0.1V | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 976 | Curr_String27 | 0.1A | register value | -15~15A | R | SOURCE_ONLY | source_claim | — |
| input | 977 | V_String28 | 0.1V | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 978 | Curr_String28 | 0.1A | register value | -15~15A | R | SOURCE_ONLY | source_claim | — |
| input | 979 | V_String29 | 0.1V | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 980 | Curr_String29 | 0.1A | register value | -15A~15A | R | SOURCE_ONLY | source_claim | — |
| input | 981 | V_String30 | 0.1V | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 982 | Curr_String30 | 0.1A | register value | -15~15A | R | SOURCE_ONLY | source_claim | — |
| input | 983 | V_String31 | 0.1V | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 984 | Curr_String31 | 0.1A | register value | -15~15A | R | SOURCE_ONLY | source_claim | — |
| input | 985 | V_String32 | 0.1V | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 986 | Curr_String32 | 0.1A | register value | -15~15A | R | SOURCE_ONLY | source_claim | — |
| input | 987 | StrUnmatch2 | Bit0~15:String17~32unmatch | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 988 | StrCurrentUnblan ce2 | Bit0~15:String 17~32 current unblance | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 989 | StrDisconnect2 | Bit0~15:String17~32disconnect | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 990 | PVWarningValue | PVWarningValue(PV9-PV16) Contains PV9~16 abnormal ， 和 Boost9~16Driveanomalies | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 991 | StrWaringvalue1 | string1~string16abnormal | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 992 | StrWaringvalue2 | string17~string32abnormal | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 993 | Register 993 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| input | 994 | Register 994 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| input | 995 | Register 995 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| input | 996 | Register 996 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| input | 997 | Register 997 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| input | 998 | Register 998 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| input | 999 | SystemCmd | M3toDSPsystemcommand | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 1009 | DischargePower | DischargePower | register value | W | UNKNOWN | SOURCE_ONLY | source_claim | — |
| input | 1011 | ChargePower | ChargePower | register value | W | UNKNOWN | SOURCE_ONLY | source_claim | — |
| input | 1013 | BatteryVoltage | BatteryVoltage | register value | V | UNKNOWN | SOURCE_ONLY | source_claim | — |
| input | 1014 | SOC | SOC | register value | % | UNKNOWN | SOURCE_ONLY | source_claim | — |
| input | 1015 | ACPowerToUser | ACPowerToUser | register value | W | UNKNOWN | SOURCE_ONLY | source_claim | — |
| input | 1021 | ACPowerToUserTotal | ACPowerToUserTotal | register value | W | UNKNOWN | SOURCE_ONLY | source_claim | — |
| input | 1023 | ACPowerToGrid | ACPowerToGrid | register value | W | UNKNOWN | SOURCE_ONLY | source_claim | — |
| input | 1029 | ACPowerToGridTotal | ACPowerToGridTotal | register value | W | UNKNOWN | SOURCE_ONLY | source_claim | — |
| input | 1031 | INVPowerToLocalLoad | INVPowerToLocalLoad | register value | W | UNKNOWN | SOURCE_ONLY | source_claim | — |
| input | 1037 | INVPowerToLocalLoadTotal | INVPowerToLocalLoadTotal | register value | W | UNKNOWN | SOURCE_ONLY | source_claim | — |
| input | 1040 | BatteryTemperature | BatteryTemperature | register value | °C | UNKNOWN | SOURCE_ONLY | source_claim | — |
| input | 1041 | BatteryState | BatteryState | register value | — | UNKNOWN | SOURCE_ONLY | source_claim | — |
| input | 1044 | EnergyToUserToday | EnergyToUserToday | register value | kWh | UNKNOWN | SOURCE_ONLY | source_claim | — |
| input | 1046 | EnergyToUserTotal | EnergyToUserTotal | register value | kWh | UNKNOWN | SOURCE_ONLY | source_claim | — |
| input | 1048 | EnergyToGridToday | EnergyToGridToday | register value | kWh | UNKNOWN | SOURCE_ONLY | source_claim | — |
| input | 1050 | EnergyToGridTotal | EnergyToGridTotal | register value | kWh | UNKNOWN | SOURCE_ONLY | source_claim | — |
| input | 1052 | DischargeEnergyToday | DischargeEnergyToday | register value | kWh | UNKNOWN | SOURCE_ONLY | source_claim | — |
| input | 1054 | DischargeEnergyTotal | DischargeEnergyTotal | register value | kWh | UNKNOWN | SOURCE_ONLY | source_claim | — |
| input | 1056 | ChargeEnergyToday | ChargeEnergyToday | register value | kWh | UNKNOWN | SOURCE_ONLY | source_claim | — |
| input | 1058 | ChargeEnergyTotal | ChargeEnergyTotal | register value | kWh | UNKNOWN | SOURCE_ONLY | source_claim | — |
| input | 1060 | LocalLoadEnergyToday | LocalLoadEnergyToday | register value | kWh | UNKNOWN | SOURCE_ONLY | source_claim | — |
| input | 1062 | LocalLoadEnergyTotal | LocalLoadEnergyTotal | register value | kWh | UNKNOWN | SOURCE_ONLY | source_claim | — |
| input | 1124 | ACChargeEnergyToday | ACChargeEnergyToday | register value | kWh | UNKNOWN | SOURCE_ONLY | source_claim | — |
| input | 1126 | ACChargeEnergyTotal | ACChargeEnergyTotal | register value | kWh | UNKNOWN | SOURCE_ONLY | source_claim | — |

### MOD TL3-XH

Vendor/catalogue family; no model-specific live validation is claimed here.

| Table | Address | Name | Description | Encoding / scale | Unit | Access | Status | Evidence | Notes |
|---|---:|---|---|---|---|---|---|---|---|
| holding | 0 | Inverter Enabled | Theinvertercanbeswitched onandoff,andtheBDCcanbe switchedonandoffforthe battreadyfunction. | register value; /10 | — | R/W | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| holding | 1 | Safety function enable flags | SPI: system protection interface Bit0~3:forCEI0-21 Bit4~6:forSAA | register value | — | W | SOURCE_ONLY | source_claim | — |
| holding | 2 | Persist power-factor commands | Means these settings will be acting or not when next poweron | register value | — | W | RESOLVED | semantic_correlated, source_claim | — |
| holding | 3 | Active power limit setpoint | 255:powerisnotbelimited | register value; /1 | % | W | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| holding | 4 | Reactive power limit setpoint | 255:powerisnotbelimited | register value; /1 | % | W | SOURCE_ONLY | source_claim | — |
| holding | 5 | Power factor target | Inverter output power factor’s10000times | register value; /10000 | pf | W | SOURCE_ONLY | source_claim | — |
| holding | 6 | Rated apparent power | Normal power(high) | register value; /10 | 0.1VA | R | SOURCE_ONLY | source_claim | — |
| holding | 7 | Rated apparent power | Normal power(low) | register value; /10 | 0.1VA | R | SOURCE_ONLY | source_claim | — |
| holding | 8 | Nominal PV voltage | NormalworkPV voltage | register value; /10 | 0.1V | R | SOURCE_ONLY | source_claim | — |
| holding | 9 | Firmware | Firmwareversion (high) | firmware_version; /10 | ASCII | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| holding | 10 | Firmware | Firmwareversion (middle) | register value | ASCII | R | SOURCE_ONLY | source_claim | — |
| holding | 11 | Firmware | Firmwareversion(low) | register value | ASCII | R | SOURCE_ONLY | source_claim | — |
| holding | 12 | Firmware | ControlFirmware version(high) | register value | ASCII | R | SOURCE_ONLY | source_claim | — |
| holding | 13 | Firmware | ControlFirmware version(middle) | register value | ASCII | R | SOURCE_ONLY | source_claim | — |
| holding | 14 | Firmware | ControlFirmware version(low) | register value | ASCII | R | SOURCE_ONLY | source_claim | — |
| holding | 15 | LCD language selection | 0:Italian; 1:English; 2:German; 3:Spanish; 4:French; 5:Chinese; 6：Polish 7：Portugues 8：Hungary | register value | — | W | SOURCE_ONLY | source_claim | — |
| holding | 16 | Country profile configured | CountrySelectedor not | register value | — | W | SOURCE_ONLY | source_claim | — |
| holding | 17 | PV start voltage threshold | Inputstartvoltage | register value; /10 | 0.1V | W | SOURCE_ONLY | source_claim | — |
| holding | 18 | Start-up delay | Starttime | register value; /1 | 1s | W | SOURCE_ONLY | source_claim | — |
| holding | 19 | Restart delay | RestartDelayTime afterfaultback; | register value; /1 | 1s | W | SOURCE_ONLY | source_claim | — |
| holding | 20 | Active power ramp rate (startup) | Powerstartslope | register value; /10 | 0.1% | W | SOURCE_ONLY | source_claim | — |
| holding | 21 | Active power ramp rate (restart) | Powerrestartslope | register value; /10 | 0.1% | W | SOURCE_ONLY | source_claim | — |
| holding | 22 | Modbus RTU baud rate | Select communicationbaudrat e 0:9600bps 1:38400bps | register value | — | W | SOURCE_ONLY | source_claim | — |
| holding | 23 | Serial Number | The Home Assistant integration exposes this as the device serial number and reuses it as the unique identifier. | serial_number; /10 | ASCII | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| holding | 24 | Serial Number | The Home Assistant integration exposes this as the device serial number and reuses it as the unique identifier. | register value | ASCII | R | SOURCE_ONLY | source_claim | — |
| holding | 25 | Serial Number | The Home Assistant integration exposes this as the device serial number and reuses it as the unique identifier. | register value | ASCII | R | SOURCE_ONLY | source_claim | — |
| holding | 26 | Serial Number | The Home Assistant integration exposes this as the device serial number and reuses it as the unique identifier. | register value | ASCII | R | SOURCE_ONLY | source_claim | — |
| holding | 27 | Serial Number | The Home Assistant integration exposes this as the device serial number and reuses it as the unique identifier. | register value | ASCII | R | SOURCE_ONLY | source_claim | — |
| holding | 28 | Inverter Model | Home Assistant renders this value as the string A# B# D# T# P# U# M# S# via the integration's model() helper. Vendor spec lists value pattern `&*5`; digits appear to be stored without the leading letter codes, so treat as encoded tokens until verified on hardware. | register value; /10 | — | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| holding | 29 | Inverter Model | Home Assistant renders this value as the string A# B# D# T# P# U# M# S# via the integration's model() helper. Vendor spec lists value pattern `&*5`; digits appear to be stored without the leading letter codes, so treat as encoded tokens until verified on hardware. | register value | — | R | SOURCE_ONLY | source_claim | — |
| holding | 30 | Modbus slave address | Communicate address | register value | — | W | SOURCE_ONLY | source_claim | — |
| holding | 31 | Firmware update trigger | Updatefirmware | register value | — | W | SOURCE_ONLY | source_claim | — |
| holding | 32 | Reset user configuration | Use with caution; the inverter immediately reboots and loses provisioning data. | register value | — | W | SOURCE_ONLY | source_claim | — |
| holding | 33 | Factory reset | Equivalent to the front-panel factory reset. Requires re-commissioning afterwards. | register value | — | W | SOURCE_ONLY | source_claim | — |
| holding | 34 | Manufacturer information string | The original table lists these words as Manufacturer Info 8-1 (high/middle/low); combine them to read the full string. | register value | ASCII | R | SOURCE_ONLY | source_claim | — |
| holding | 35 | Manufacturer information string | The original table lists these words as Manufacturer Info 8-1 (high/middle/low); combine them to read the full string. | register value | ASCII | R | SOURCE_ONLY | source_claim | — |
| holding | 36 | Manufacturer information string | The original table lists these words as Manufacturer Info 8-1 (high/middle/low); combine them to read the full string. | register value | ASCII | R | SOURCE_ONLY | source_claim | — |
| holding | 37 | Manufacturer information string | The original table lists these words as Manufacturer Info 8-1 (high/middle/low); combine them to read the full string. | register value | ASCII | R | SOURCE_ONLY | source_claim | — |
| holding | 38 | Manufacturer information string | The original table lists these words as Manufacturer Info 8-1 (high/middle/low); combine them to read the full string. | register value | ASCII | R | SOURCE_ONLY | source_claim | — |
| holding | 39 | Manufacturer information string | The original table lists these words as Manufacturer Info 8-1 (high/middle/low); combine them to read the full string. | register value | ASCII | R | SOURCE_ONLY | source_claim | — |
| holding | 40 | Manufacturer information string | The original table lists these words as Manufacturer Info 8-1 (high/middle/low); combine them to read the full string. | register value | ASCII | R | SOURCE_ONLY | source_claim | — |
| holding | 41 | Manufacturer information string | The original table lists these words as Manufacturer Info 8-1 (high/middle/low); combine them to read the full string. | register value | ASCII | R | SOURCE_ONLY | source_claim | — |
| holding | 42 | G100 failsafe enable | EnglishG100failsafeset | register value | — | W | SOURCE_ONLY | source_claim | — |
| holding | 43 | Device Type Code | Vendor spec provides value pattern `&*6`; handle as encoded type/family digits with implied prefixes pending confirmation. | register value; /10 | — | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| holding | 44 | Number Of Trackers And Phases | Inputtrackernumand outputphasenum | register value; /10 | — | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| holding | 45 | System clock year | Localtime | register value | — | W | SOURCE_ONLY | source_claim | — |
| holding | 46 | System clock month | Systemtime-Month | register value | — | W | SOURCE_ONLY | source_claim | — |
| holding | 47 | System clock day | Systemtime-Day | register value | — | W | SOURCE_ONLY | source_claim | — |
| holding | 48 | System clock hour | Systemtime-Hour | register value | — | W | SOURCE_ONLY | source_claim | — |
| holding | 49 | System clock minute | Systemtime-Min | register value | — | W | SOURCE_ONLY | source_claim | — |
| holding | 50 | System clock second | Systemtime-Second | register value | — | W | SOURCE_ONLY | source_claim | — |
| holding | 51 | System clock weekday | SystemWeekly | register value | — | W | SOURCE_ONLY | source_claim | — |
| holding | 52 | Stage 1 undervoltage limit | Gridvoltagelowlimit protect | register value | 0.1V | W | SOURCE_ONLY | source_claim | — |
| holding | 53 | Stage 1 overvoltage limit | Gridvoltagehighlimit protect | register value | 0.1V | W | SOURCE_ONLY | source_claim | — |
| holding | 54 | Stage 1 underfrequency limit | Gridfrequencylow limitprotect | register value | 0.01 Hz | W | SOURCE_ONLY | source_claim | — |
| holding | 55 | Stage 1 overfrequency limit | Gridhigh frequencylimitprotect | register value | 0.01 Hz | W | SOURCE_ONLY | source_claim | — |
| holding | 56 | Stage 2 undervoltage limit | Gridvoltagelowlimit protect2 | register value | 0.1V | W | SOURCE_ONLY | source_claim | — |
| holding | 57 | Stage 2 overvoltage limit | Gridvoltagehighlimit protect2 | register value | 0.1V | W | SOURCE_ONLY | source_claim | — |
| holding | 58 | Stage 2 underfrequency limit | Gridfrequencylow limitprotect2 | register value | 0.01 Hz | W | SOURCE_ONLY | source_claim | — |
| holding | 59 | Stage 2 overfrequency limit | Gridhighfrequency limitprotect2 | register value | 0.01 Hz | W | SOURCE_ONLY | source_claim | — |
| holding | 60 | Stage 3 undervoltage limit | Grid voltage low limit protect3 | register value | 0.1V | W | SOURCE_ONLY | source_claim | — |
| holding | 61 | Stage 3 overvoltage limit | Grid voltage high limit protect3 | register value | 0.1V | W | SOURCE_ONLY | source_claim | — |
| holding | 62 | Stage 3 underfrequency limit | Grid frequency low limitprotect3 | register value | 0.01Hz | W | SOURCE_ONLY | source_claim | — |
| holding | 63 | Stage 3 overfrequency limit | Grid frequency high limitprotect3 | register value | 0.01Hz | W | SOURCE_ONLY | source_claim | — |
| holding | 64 | Reconnect undervoltage limit | Gridlowvoltagelimit connecttoGrid | register value | 0.1V | W | SOURCE_ONLY | source_claim | — |
| holding | 65 | Reconnect overvoltage limit | Gridhighvoltagelimit connecttoGrid | register value | 0.1V | W | SOURCE_ONLY | source_claim | — |
| holding | 66 | Reconnect underfrequency limit | Gridlowfrequency | register value | 0.01 | W | SOURCE_ONLY | source_claim | — |
| holding | 67 | Reconnect overfrequency limit | Gridhighfrequency limitconnecttoGrid | register value | 0.01 Hz | W | SOURCE_ONLY | source_claim | — |
| holding | 68 | Stage 1 undervoltage trip delay | Grid voltage low limit protecttime 1 | register value | Cycle | W | SOURCE_ONLY | source_claim | — |
| holding | 69 | Stage 1 overvoltage trip delay | Grid voltage high limit protecttime 1 | register value | Cycle | W | SOURCE_ONLY | source_claim | — |
| holding | 70 | Stage 2 undervoltage trip delay | Grid voltage low limit protecttime 2 | register value | Cycle | W | SOURCE_ONLY | source_claim | — |
| holding | 71 | Stage 2 overvoltage trip delay | Grid voltage high limit protecttime 2 | register value | Cycle | W | SOURCE_ONLY | source_claim | — |
| holding | 72 | Stage 1 underfrequency trip delay | Grid frequency low limitprotecttime 1 | register value | Cycle | W | SOURCE_ONLY | source_claim | — |
| holding | 73 | Modbus Version | Grid frequency high limitprotecttime 1 | register value | Cycle | W | SOURCE_ONLY | source_claim | — |
| holding | 74 | Stage 2 underfrequency trip delay | Grid frequency low limitprotecttime 2 | register value | Cycle | W | SOURCE_ONLY | source_claim | — |
| holding | 75 | Stage 2 overfrequency trip delay | Grid frequency high limitprotecttime 2 | register value | Cycle | W | SOURCE_ONLY | source_claim | — |
| holding | 76 | Stage 3 undervoltage trip delay | Grid voltage low limit protecttime 3 | register value | Cycle | W | SOURCE_ONLY | source_claim | — |
| holding | 77 | Stage 3 overvoltage trip delay | Grid voltage high limit protecttime 3 | register value | Cycle | W | SOURCE_ONLY | source_claim | — |
| holding | 78 | Stage 3 underfrequency trip delay | Grid frequency low limitprotecttime 3 | register value | Cycle | W | SOURCE_ONLY | source_claim | — |
| holding | 79 | Stage 3 overfrequency trip delay | Grid frequency high limitprotecttime 3 | register value | Cycle | W | SOURCE_ONLY | source_claim | — |
| holding | 80 | Ten-minute overvoltage limit | Voltprotectionfor10 min | register value | 0.1V | W | SOURCE_ONLY | source_claim | — |
| holding | 81 | PV input high-voltage fault | PVVoltageHigh Fault | register value | 0.1V | W | SOURCE_ONLY | source_claim | — |
| holding | 82 | Controller firmware build string | Positions: 0-1 model letters, 2-3 model variant, 4-5 DSP1 build, 6-7 DSP2/M0 build, 8-9 CPLD/AFCI build, 10-11 M3 build. | register value | ASCII | R | SOURCE_ONLY | source_claim | — |
| holding | 83 | Controller firmware build string | Positions: 0-1 model letters, 2-3 model variant, 4-5 DSP1 build, 6-7 DSP2/M0 build, 8-9 CPLD/AFCI build, 10-11 M3 build. | register value | ASCII | R | SOURCE_ONLY | source_claim | — |
| holding | 84 | Controller firmware build string | Positions: 0-1 model letters, 2-3 model variant, 4-5 DSP1 build, 6-7 DSP2/M0 build, 8-9 CPLD/AFCI build, 10-11 M3 build. | register value | ASCII | R | SOURCE_ONLY | source_claim | — |
| holding | 85 | Controller firmware build string | Positions: 0-1 model letters, 2-3 model variant, 4-5 DSP1 build, 6-7 DSP2/M0 build, 8-9 CPLD/AFCI build, 10-11 M3 build. | register value | ASCII | R | SOURCE_ONLY | source_claim | — |
| holding | 86 | Controller firmware build string | Positions: 0-1 model letters, 2-3 model variant, 4-5 DSP1 build, 6-7 DSP2/M0 build, 8-9 CPLD/AFCI build, 10-11 M3 build. | register value | ASCII | R | SOURCE_ONLY | source_claim | — |
| holding | 87 | Controller firmware build string | Positions: 0-1 model letters, 2-3 model variant, 4-5 DSP1 build, 6-7 DSP2/M0 build, 8-9 CPLD/AFCI build, 10-11 M3 build. | register value | ASCII | R | SOURCE_ONLY | source_claim | — |
| holding | 88 | Modbus Version | ModbusVersion | register value; /100 | Int(16 bits) | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| holding | 89 | Power-factor control mode | 0=Unity PF, 1=Fixed PF setpoint, 2=Default PF line, 3=User-defined PF line, 4=Under-excited reactive power, 5=Over-excited reactive power, 6=Q(V) curve, 7=Direct control, 8=Static capacitive QV, 9=Static inductive QV. | register value | — | W | SOURCE_ONLY | source_claim | — |
| holding | 90 | GPRS modem IP/status flags | Bit 0-3: 0=idle, 1=IP read requested, 2=set IP succeeded; Bit 4-7: 0=unknown, 1=modem OK, 2=no SIM, 3=no network, 4=TCP connect fail, 5=TCP connected, etc. | register value | — | W | UNKNOWN_RESERVED | source_claim | — |
| holding | 91 | Frequency derating start | Frequencyderating startpoint | register value | 0.01H Z | W | SOURCE_ONLY | source_claim | — |
| holding | 92 | Frequency derating slope | Frequency–loadlimit rate | register value | 10tim es | W | SOURCE_ONLY | source_claim | — |
| holding | 93 | CEI 0-21 Q(V) point V1S | CEI021V1SQ(v) | register value | 0.1V | W | SOURCE_ONLY | source_claim | — |
| holding | 94 | CEI 0-21 Q(V) point V2S | CEI021V2SQ(v) | register value | 0.1V | W | SOURCE_ONLY | source_claim | — |
| holding | 95 | CEI 0-21 Q(V) point V1L | CEI021V1LQ(v) | register value | 0.1V | W | SOURCE_ONLY | source_claim | — |
| holding | 96 | CEI 0-21 Q(V) point V2L | CEI021V2LQ(v) | register value | 0.1V | W | SOURCE_ONLY | source_claim | — |
| holding | 97 | Q(V) lock-in active power | Q(v)lockinactive powerofCEI021 | register value | Percen t | W | SOURCE_ONLY | source_claim | — |
| holding | 98 | Q(V) lock-out active power | Q(v)lockOutactive powerofCEI021 | register value | Percen t | W | SOURCE_ONLY | source_claim | — |
| holding | 99 | Power-factor curve lock-in voltage | Lockingirdvoltof CEI021PFline | register value | 0.1V | W | SOURCE_ONLY | source_claim | — |
| holding | 100 | Power-factor curve lock-out voltage | Lockoutgirdvoltof CEI021PFline | register value | 0.1V | W | SOURCE_ONLY | source_claim | — |
| holding | 101 | Power-factor adjust value 1 | PFadjustvalue1 | register value | — | W | SOURCE_ONLY | source_claim | — |
| holding | 102 | Power-factor adjust value 2 | PFadjustvalue2 | register value | — | W | SOURCE_ONLY | source_claim | — |
| holding | 103 | Power-factor adjust value 3 | PFadjustvalue3 | register value | — | W | SOURCE_ONLY | source_claim | — |
| holding | 104 | Power-factor adjust value 4 | PFadjustvalue4 | register value | — | W | SOURCE_ONLY | source_claim | — |
| holding | 105 | Power-factor adjust value 5 | PFadjustvalue5 | register value | — | W | SOURCE_ONLY | source_claim | — |
| holding | 106 | Power-factor adjust value 6 | PFadjustvalue6 | register value | — | W | SOURCE_ONLY | source_claim | — |
| holding | 107 | Q(V) response delay | QV Reactive Power delaytime | register value | 1S | W | SOURCE_ONLY | source_claim | — |
| holding | 108 | Over-frequency derating delay | Overfrequency derati ngdelaytime | register value | 50ms | W | SOURCE_ONLY | source_claim | — |
| holding | 109 | Maximum reactive power magnitude | QmaxforQ(V)curve | register value | 0.1% | W | SOURCE_ONLY | source_claim | — |
| holding | 110 | PF curve point 1 load | 255meansnothispoint | register value | percen t | W | SOURCE_ONLY | source_claim | — |
| holding | 111 | PF curve point 1 target | PFlimitlinepoint1 powerfactor | register value | — | W | SOURCE_ONLY | source_claim | — |
| holding | 112 | PF curve point 2 load | 255meansnothispoint | register value | percen t | W | SOURCE_ONLY | source_claim | — |
| holding | 113 | PF curve point 2 target | PFlimitlinepoint 2powerfactor | register value | — | W | SOURCE_ONLY | source_claim | — |
| holding | 114 | PF curve point 3 load | 255meansnothispoint | register value | percen t | W | SOURCE_ONLY | source_claim | — |
| holding | 115 | PF curve point 3 target | PFlimitlinepoint3 powerfactor | register value | — | W | SOURCE_ONLY | source_claim | — |
| holding | 116 | PF curve point 4 load | 255meansnothispoint | register value | percen t | W | SOURCE_ONLY | source_claim | — |
| holding | 117 | PF curve point 4 target | PFlimitlinepoint4 powerfactor | register value | — | W | SOURCE_ONLY | source_claim | — |
| holding | 118 | Module code segments | SxxBxx | register value | — | R | SOURCE_ONLY | source_claim | — |
| holding | 119 | Module code segments | DxxTxx | register value | — | R | SOURCE_ONLY | source_claim | — |
| holding | 120 | Module code segments | PxxUxx | register value | — | R | SOURCE_ONLY | source_claim | — |
| holding | 121 | Module code segments | Mxxxx Power | register value | — | R | SOURCE_ONLY | source_claim | — |
| holding | 122 | Export limit enable mode | ExportLimitenable, 0:DisableexportLimit; 1:Enable485exportLimit; 2:Enable232exportLimit; 3:EnableCTexportLimit; | register value | — | R/W | SOURCE_ONLY | source_claim | — |
| holding | 123 | Export limit power setpoint | ExportLimitPowerRate | register value | 0.1% | R/W | SOURCE_ONLY | source_claim | — |
| holding | 124 | Tracker coupling mode | 0:Independent 1:DCSource 2:Parallel | register value | — | W | SOURCE_ONLY | source_claim | — |
| holding | 3000 | Export-limit fallback cap | Thepowerrate whenexportLimit failed | register value; /10 | 0.1% | R/W | SOURCE_ONLY | source_claim | — |
| holding | 3001 | Serial Number | Thenewmodel usesthefollowing registerstorecord theserialnumber; The representationis thesameasthe original:one registerholdstwo charactersandthe newserialnumber is30characters. | serial_number; /10 | ASCII | R/W | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| holding | 3002 | Serial Number | Serialnumber3-4 | register value | ASCII | R/W | SOURCE_ONLY | source_claim | — |
| holding | 3003 | Serial Number | Serialnumber5-6 | register value | ASCII | R/W | SOURCE_ONLY | source_claim | — |
| holding | 3004 | Serial Number | Serialnumber7-8 | register value | ASCII | R/W | SOURCE_ONLY | source_claim | — |
| holding | 3005 | Serial Number | Serialnumber9-10 | register value | ASCII | R/W | SOURCE_ONLY | source_claim | — |
| holding | 3006 | Serial Number | Serialnumber11-12 | register value | ASCII | R/W | SOURCE_ONLY | source_claim | — |
| holding | 3007 | Serial Number | Serialnumber13-14 | register value | ASCII | R/W | SOURCE_ONLY | source_claim | — |
| holding | 3008 | Serial Number | Serialnumber15-16 | register value | ASCII | R/W | SOURCE_ONLY | source_claim | — |
| holding | 3009 | Serial Number | Serialnumber17-18 | register value | ASCII | R/W | SOURCE_ONLY | source_claim | — |
| holding | 3010 | Serial Number | Serialnumber19-20 | register value | ASCII | R/W | SOURCE_ONLY | source_claim | — |
| holding | 3011 | Serial Number | Serialnumber21-22 | register value | ASCII | R/W | SOURCE_ONLY | source_claim | — |
| holding | 3012 | Serial Number | Serialnumber23-24 | register value | ASCII | R/W | SOURCE_ONLY | source_claim | — |
| holding | 3013 | Serial Number | Serialnumber25-26 | register value | ASCII | R/W | SOURCE_ONLY | source_claim | — |
| holding | 3014 | Serial Number | Serialnumber27-28 | register value | ASCII | R/W | SOURCE_ONLY | source_claim | — |
| holding | 3015 | Serial Number | Serialnumber29-30 | register value | ASCII | R/W | SOURCE_ONLY | source_claim | — |
| holding | 3016 | Dry-contact enable | DryContact functionenable | register value | — | R/W | SOURCE_ONLY | source_claim | — |
| holding | 3017 | Dry-contact close threshold | The power rate of drycontactturnon | register value | 0.1% | R/W | SOURCE_ONLY | source_claim | — |
| holding | 3018 | Hybrid work mode | MIN2.5~6KTL-XH/ XADoubleCT special | register value | — | R/W | SOURCE_ONLY | source_claim | — |
| holding | 3019 | Dry-contact release threshold | Drycontact closurepowerpe rcentage | register value | 0~100 0 | R/W | SOURCE_ONLY | source_claim | — |
| holding | 3020 | Off-grid box control | Leave at factory value unless instructed by Growatt support. | register value | — | R/W | SOURCE_ONLY | source_claim | — |
| holding | 3021 | External off-grid enable | 0x00: Disable; （default） 0x01:Enable; | register value | — | R/W | SOURCE_ONLY | source_claim | — |
| holding | 3022 | BDC stop-work bus voltage | BdcStopWorkOfBusVolt | register value | V | R | SOURCE_ONLY | source_claim | — |
| holding | 3023 | Grid topology selection | MIN2.5~6KTL-XH/ XADoubleCT special | register value | — | R/W | SOURCE_ONLY | source_claim | — |
| holding | 3024 | Float-charge current limit | CCcurrent | register value; /10 | 0.1A | R/W | SOURCE_ONLY | source_claim | — |
| holding | 3025 | Battery-low warning setpoint | Leadacidbattery LVvoltage | register value | 0.1V | R/W | SOURCE_ONLY | source_claim | — |
| holding | 3026 | Battery-low warning clear | Clearbatterylow voltageerror voltagepoint LoadPercent(only lead-Acid): 45.5V(Load< 20%); 48.0V(20%<=Load <=50%); 49.0V(Load> 50%); | register value | 0.1V | R/W | SOURCE_ONLY | source_claim | — |
| holding | 3027 | Battery discharge cutoff | Shouldstop dischargewhen lowerthanthis voltage(only lead-Acid): 46.0V(Load< 20%); 44.8V(20%<=Load <=50%); 44.2V(Load> 50%); | register value | 0.1V | R/W | SOURCE_ONLY | source_claim | — |
| holding | 3028 | Battery charge stop voltage | Shouldstop chargewhen higherthanthis voltage | register value; /100 | 0.01V | R/W | SOURCE_ONLY | source_claim | — |
| holding | 3029 | Battery discharge start voltage | Shouldnot dischargewhen lowerthanthis voltage | register value; /100 | 0.01V | R/W | SOURCE_ONLY | source_claim | — |
| holding | 3030 | Battery constant-charge voltage | CVvoltage（acid） canchargewhen lowerthanthis voltage | register value; /100 | 0.01V | R/W | SOURCE_ONLY | source_claim | — |
| holding | 3031 | Discharge low temperature limit | 0-200:0-20℃ 1000-1400： -40-0℃ | register value; /10 | 0.1℃ | R/W | SOURCE_ONLY | source_claim | — |
| holding | 3032 | Discharge high temperature limit | Batterytemperatureupper limitfordischarge | register value; /10 | 0.1℃ | R/W | SOURCE_ONLY | source_claim | — |
| holding | 3033 | Charge low temperature limit | Battery temperaturelower limit 0-200:0-20℃ 1000-1400： -40-0℃ | register value; /10 | 0.1℃ | R/W | SOURCE_ONLY | source_claim | — |
| holding | 3034 | Charge high temperature limit | Battery temperature upperlimit | register value; /10 | 0.1℃ | R/W | SOURCE_ONLY | source_claim | — |
| holding | 3035 | Under-frequency discharge delay | UnderFreDelay Time | register value | 50ms | R/W | SOURCE_ONLY | source_claim | — |
| holding | 3036 | Grid-first discharge rate | DischargePowerRate whenGridFirst | register value | % | R/W | RESOLVED | semantic_correlated, source_claim | — |
| holding | 3037 | Grid-first stop SOC | StopDischargesocwhen GridFirst | register value | % | R/W | RESOLVED | semantic_correlated, source_claim | — |
| holding | 3038 | Grid-first period 1 control | Bit0~7:minutes; Bit8~12:hour; Bit13~14, 0:loadpriority; 1:batterypriority; 2:Gridpriority; Bit15, 0:prohibited;1: enabled; | register value | — | R/W | SOURCE_ONLY | source_claim | — |
| holding | 3039 | Grid-first period 1 end | Bit0~7:minutes; Bit8~12:hour; Bit13~15:reserved | register value | — | R/W | UNKNOWN_RESERVED | source_claim | — |
| holding | 3040 | Time2(xh) | Bit0~7:minutes; Bit8~12:hour; Bit13~14, 0:loadpriority; 1:batterypriority; 2:Gridpriority; Bit15, 0:prohibited;1: | register value | — | R/W | SOURCE_ONLY | source_claim | — |
| holding | 3041 | Register 3041 | Bit0~7:minutes; Bit8~12:hour; Bit13~15:reserved | register value; /10 | W | R/W | UNKNOWN_RESERVED | source_claim | — |
| holding | 3042 | Time3(xh) | WithTime1 | register value; /10 | W | R/W | SOURCE_ONLY | source_claim | — |
| holding | 3043 | Register 3043 | WithTime1 | register value; /10 | W | R/W | UNKNOWN_RESERVED | source_claim | — |
| holding | 3044 | Time4(xh) | WithTime1 | register value; /10 | W | R/W | SOURCE_ONLY | source_claim | — |
| holding | 3045 | Register 3045 | WithTime1 | register value; /10 | W | R/W | UNKNOWN_RESERVED | source_claim | — |
| holding | 3046 | Reserved | Reserved | register value; /10 | W | R | UNKNOWN_RESERVED | source_claim | — |
| holding | 3047 | BatFirstPower Rate | ChargePowerRatewhen BatFirst | register value | % | R | RESOLVED | semantic_correlated, source_claim | — |
| holding | 3048 | wBatFirststop SOC | StopChargesocwhenBat First | register value | % | R | RESOLVED | semantic_correlated, source_claim | — |
| holding | 3049 | AC Charge Enabled | Enable:1 Disable:0 | register value; /10 | — | R/W | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| holding | 3050 | Time5(xh) | WithTime1 | register value | — | R/W | SOURCE_ONLY | source_claim | — |
| holding | 3051 | Register 3051 | WithTime1 | register value; /10 | kWh | R/W | UNKNOWN_RESERVED | source_claim | — |
| holding | 3052 | Time6(xh) | WithTime1 | register value; /10 | kWh | R/W | SOURCE_ONLY | source_claim | — |
| holding | 3053 | Register 3053 | WithTime1 | register value; /10 | kWh | R/W | UNKNOWN_RESERVED | source_claim | — |
| holding | 3054 | Time7(xh) | WithTime1 | register value; /10 | kWh | R/W | SOURCE_ONLY | source_claim | — |
| holding | 3055 | Register 3055 | WithTime1 | register value; /10 | kWh | R/W | UNKNOWN_RESERVED | source_claim | — |
| holding | 3056 | Time8(xh) | WithTime1 | register value; /10 | kWh | R/W | SOURCE_ONLY | source_claim | — |
| holding | 3057 | Register 3057 | WithTime1 | register value; /10 | kWh | R/W | UNKNOWN_RESERVED | source_claim | — |
| holding | 3058 | Time9(xh) | WithTime1 | register value; /10 | kWh | R/W | SOURCE_ONLY | source_claim | — |
| holding | 3059 | Register 3059 | WithTime1 | register value; /10 | kWh | R/W | UNKNOWN_RESERVED | source_claim | — |
| holding | 3060 | Reserved | Reserved | register value; /10 | kWh | R | UNKNOWN_RESERVED | source_claim | — |
| holding | 3061 | Reserved | Reserved | register value; /10 | kWh | R | UNKNOWN_RESERVED | source_claim | — |
| holding | 3062 | Reserved | Reserved | register value; /10 | kWh | R | UNKNOWN_RESERVED | source_claim | — |
| holding | 3063 | Reserved | Reserved | register value; /10 | kWh | R | UNKNOWN_RESERVED | source_claim | — |
| holding | 3064 | Reserved | Reserved | register value; /10 | kWh | R | UNKNOWN_RESERVED | source_claim | — |
| holding | 3065 | Reserved | Reserved | register value; /10 | kWh | R | UNKNOWN_RESERVED | source_claim | — |
| holding | 3066 | Reserved | Reserved | register value; /10 | kWh | R | UNKNOWN_RESERVED | source_claim | — |
| holding | 3067 | Reserved | Reserved | register value; /10 | kWh | R | UNKNOWN_RESERVED | source_claim | — |
| holding | 3068 | Reserved | Reserved | register value; /10 | kWh | R | UNKNOWN_RESERVED | source_claim | — |
| holding | 3069 | Reserved | Reserved | register value; /10 | kWh | R | UNKNOWN_RESERVED | source_claim | — |
| holding | 3070 | BatteryType | Batterytype 0:Lithium 1:Lead-acid 2:other | register value; /10 | kWh | R/W | SOURCE_ONLY | source_claim | — |
| holding | 3071 | BatMdlSeria/ ParalNum | BatMdlSeria/Paral Num; SPH4-11Kused Theupper8bits indicatethe numberofseries segments； Thelower8bits indicatethe numberofparallel sections; | register value; /10 | kWh | R/W | SOURCE_ONLY | source_claim | — |
| holding | 3072 | Reserved | Reserved | register value; /10 | kWh | R | UNKNOWN_RESERVED | source_claim | — |
| holding | 3073 | Reserved | Reserved | register value; /10 | kWh | R | UNKNOWN_RESERVED | source_claim | — |
| holding | 3074 | Reserved | Reserved | register value; /10 | kWh | R | UNKNOWN_RESERVED | source_claim | — |
| holding | 3075 | Reserved | Reserved | register value; /10 | kWh | R | UNKNOWN_RESERVED | source_claim | — |
| holding | 3076 | Reserved | Reserved | register value; /10 | kWh | R | UNKNOWN_RESERVED | source_claim | — |
| holding | 3077 | Reserved | Reserved | register value; /10 | kWh | R | UNKNOWN_RESERVED | source_claim | — |
| holding | 3078 | Reserved | Reserved | register value; /10 | kWh | R | UNKNOWN_RESERVED | source_claim | — |
| holding | 3079 | UpsFunEn | 0:disable 1:enable | register value | bool | R/W | SOURCE_ONLY | source_claim | — |
| holding | 3080 | UPSVoltSet | 0:230V 1:208V 2:240V | register value | V | R/W | SOURCE_ONLY | source_claim | — |
| holding | 3081 | UPSFreqSet | 0:50Hz 1:60Hz | register value | Hz | R/W | SOURCE_ONLY | source_claim | — |
| holding | 3082 | bLoadFirstSto pSocSet | ratio | register value; /1 | % | R/W | SOURCE_ONLY | source_claim | — |
| holding | 3083 | Reserved | Reserved | register value; /10 | kWh | R | UNKNOWN_RESERVED | source_claim | — |
| holding | 3084 | Reserved | Reserved | register value; /10 | kWh | R | UNKNOWN_RESERVED | source_claim | — |
| holding | 3085 | Modbus slave address | 1:Communication addr=1 1~254: Communication addr=1~254 | register value | — | R/W | SOURCE_ONLY | source_claim | — |
| holding | 3086 | RS-485 baud rate | 0:9600bps 1:38400bps | register value | — | R/W | SOURCE_ONLY | source_claim | — |
| holding | 3087 | Battery rack serial | Forbattery | register value | ASCII | R/W | SOURCE_ONLY | source_claim | — |
| holding | 3088 | Battery rack serial | SerialNumber3-4 | register value | ASCII | R/W | SOURCE_ONLY | source_claim | — |
| holding | 3089 | Battery rack serial | SerialNumber5-6 | register value | ASCII | R/W | SOURCE_ONLY | source_claim | — |
| holding | 3090 | Battery rack serial | SerialNumber7-8 | register value | ASCII | R/W | SOURCE_ONLY | source_claim | — |
| holding | 3091 | Battery rack serial | SerialNumber9-10 | register value | ASCII | R/W | SOURCE_ONLY | source_claim | — |
| holding | 3092 | Battery rack serial | SerialNumber11-12 | register value | ASCII | R/W | SOURCE_ONLY | source_claim | — |
| holding | 3093 | Battery rack serial | SerialNumber13-14 | register value | ASCII | R/W | SOURCE_ONLY | source_claim | — |
| holding | 3094 | Battery rack serial | SerialNumber15-16 | register value | ASCII | R/W | SOURCE_ONLY | source_claim | — |
| holding | 3095 | BDC reset command | 0：Invaliddata 1：Resetsetting parameters 2：Resetcorrection parameter 3：Clearhistorical power | register value | — | R/W | SOURCE_ONLY | source_claim | — |
| holding | 3096 | BDC monitoring code | ZEBA | register value | ASCII | R | SOURCE_ONLY | source_claim | — |
| holding | 3097 | BDC monitoring code | Four-character identifier for the BDC monitoring firmware (e.g. ZEBA). | register value | ASCII | R | SOURCE_ONLY | source_claim | — |
| holding | 3098 | BDC DTC code | DTC | register value | — | R | SOURCE_ONLY | source_claim | — |
| holding | 3099 | DSP firmware code | DSPsoftwarecode | register value | ASCII | R | SOURCE_ONLY | source_claim | — |
| holding | 3100 | DSP firmware code | Identifier for the inverter DSP firmware build. | register value | ASCII | R | SOURCE_ONLY | source_claim | — |
| holding | 3101 | DSP firmware version | DSPSoftwareVersion | register value | ASCII | R | SOURCE_ONLY | source_claim | — |
| holding | 3102 | Bus voltage reference | MinimumBUSvoltagefor charginganddischarging batteries | register value | V | R | SOURCE_ONLY | source_claim | — |
| holding | 3103 | BDC monitor firmware | BDCmonitoringsoftware version | register value | ASCII | R | SOURCE_ONLY | source_claim | — |
| holding | 3104 | BMS MCU hardware version | BMS hardware version information | register value | ASCII | R | SOURCE_ONLY | source_claim | — |
| holding | 3105 | BMS firmware version | BMSsoftwareversion information | register value | ASCII | R | SOURCE_ONLY | source_claim | — |
| holding | 3106 | BMS manufacturer | BMSManufacturerName | register value | ASCII | R | SOURCE_ONLY | source_claim | — |
| holding | 3107 | BMS communication interface | BMSCommunicati oninterfacetype： 0:RS485; 1:CAN; | register value | — | R | SOURCE_ONLY | source_claim | — |
| holding | 3108 | BDC module identifier 4 | SxxBxx | register value | ASCII | R/W | SOURCE_ONLY | source_claim | — |
| holding | 3109 | BDC module identifier 3 | DxxTxx | register value | ASCII | R/W | SOURCE_ONLY | source_claim | — |
| holding | 3110 | BDC module identifier 2 | PxxUxx | register value | ASCII | R/W | SOURCE_ONLY | source_claim | — |
| holding | 3111 | BDC module identifier 1 | Mxxxx | register value | ASCII | R/W | SOURCE_ONLY | source_claim | — |
| holding | 3112 | Reserved | Reserved; reported as zero on known firmware. | register value | — | R | UNKNOWN_RESERVED | source_claim | — |
| holding | 3113 | BDC protocol version | Bit8-bit15The majorversion numberranges from0-256.In principle,itcannot bechanged Bit0-bit7Minor versionnumber [0-256].Ifthe protocolis changed,youneed toupdatethis version No. | register value | — | R | SOURCE_ONLY | source_claim | — |
| holding | 3114 | BDC certification version | BDCCertificationVer | register value | — | R | SOURCE_ONLY | source_claim | — |
| holding | 3115 | Reserved | Reserved for future use. | register value | — | R | UNKNOWN_RESERVED | source_claim | — |
| holding | 3116 | Reserved | Reserved for future use. | register value | — | R | UNKNOWN_RESERVED | source_claim | — |
| holding | 3117 | Reserved | Reserved for future use. | register value | — | R | UNKNOWN_RESERVED | source_claim | — |
| holding | 3118 | BDC on/off state | Indicates whether the battery DC converter is currently running (1) or idle (0). | register value | — | R | SOURCE_ONLY | source_claim | — |
| holding | 3119 | Dry contact state | Current state of the dry-contact output (0 = open, 1 = closed). | register value | — | R | SOURCE_ONLY | source_claim | — |
| holding | 3120 | Reserved | Reserved; reported as zero on TL-XH firmware. | register value | — | R | UNKNOWN_RESERVED | source_claim | — |
| holding | 3121 | Self-use power | Not yet surfaced by the Home Assistant integration. | register value; /10 | W | R | SOURCE_ONLY | source_claim | — |
| holding | 3122 | Self-use power | Not yet surfaced by the Home Assistant integration. | register value; /10 | W | R | SOURCE_ONLY | source_claim | — |
| holding | 3123 | System energy today | Available in firmware but not yet exposed as an integration attribute. | register value; /10 | kWh | R | SOURCE_ONLY | source_claim | — |
| holding | 3124 | System energy today | Available in firmware but not yet exposed as an integration attribute. | register value; /10 | kWh | R | SOURCE_ONLY | source_claim | — |
| holding | 5000 | Bdc Slot 1 Metadata | Repeat for additional BDCs at 40-register strides (5040-5079, 5080-5119, ). Stored as `bdc_metadata_block`. | register value | — | R/W | SOURCE_ONLY | source_claim | — |
| holding | 5001 | Bdc Slot 1 Metadata | Repeat for additional BDCs at 40-register strides (5040-5079, 5080-5119, ). Stored as `bdc_metadata_block`. | register value | — | R/W | SOURCE_ONLY | source_claim | — |
| holding | 5002 | Bdc Slot 1 Metadata | Repeat for additional BDCs at 40-register strides (5040-5079, 5080-5119, ). Stored as `bdc_metadata_block`. | register value | — | R/W | SOURCE_ONLY | source_claim | — |
| holding | 5003 | Bdc Slot 1 Metadata | Repeat for additional BDCs at 40-register strides (5040-5079, 5080-5119, ). Stored as `bdc_metadata_block`. | register value | — | R/W | SOURCE_ONLY | source_claim | — |
| holding | 5004 | Bdc Slot 1 Metadata | Repeat for additional BDCs at 40-register strides (5040-5079, 5080-5119, ). Stored as `bdc_metadata_block`. | register value | — | R/W | SOURCE_ONLY | source_claim | — |
| holding | 5005 | Bdc Slot 1 Metadata | Repeat for additional BDCs at 40-register strides (5040-5079, 5080-5119, ). Stored as `bdc_metadata_block`. | register value | — | R/W | SOURCE_ONLY | source_claim | — |
| holding | 5006 | Bdc Slot 1 Metadata | Repeat for additional BDCs at 40-register strides (5040-5079, 5080-5119, ). Stored as `bdc_metadata_block`. | register value | — | R/W | SOURCE_ONLY | source_claim | — |
| holding | 5007 | Bdc Slot 1 Metadata | Repeat for additional BDCs at 40-register strides (5040-5079, 5080-5119, ). Stored as `bdc_metadata_block`. | register value | — | R/W | SOURCE_ONLY | source_claim | — |
| holding | 5008 | Bdc Slot 1 Metadata | Repeat for additional BDCs at 40-register strides (5040-5079, 5080-5119, ). Stored as `bdc_metadata_block`. | register value | — | R/W | SOURCE_ONLY | source_claim | — |
| holding | 5009 | Bdc Slot 1 Metadata | Repeat for additional BDCs at 40-register strides (5040-5079, 5080-5119, ). Stored as `bdc_metadata_block`. | register value | — | R/W | SOURCE_ONLY | source_claim | — |
| holding | 5010 | Bdc Slot 1 Metadata | Repeat for additional BDCs at 40-register strides (5040-5079, 5080-5119, ). Stored as `bdc_metadata_block`. | register value | — | R/W | SOURCE_ONLY | source_claim | — |
| holding | 5011 | Bdc Slot 1 Metadata | Repeat for additional BDCs at 40-register strides (5040-5079, 5080-5119, ). Stored as `bdc_metadata_block`. | register value | — | R/W | SOURCE_ONLY | source_claim | — |
| holding | 5012 | Bdc Slot 1 Metadata | Repeat for additional BDCs at 40-register strides (5040-5079, 5080-5119, ). Stored as `bdc_metadata_block`. | register value | — | R/W | SOURCE_ONLY | source_claim | — |
| holding | 5013 | Bdc Slot 1 Metadata | Repeat for additional BDCs at 40-register strides (5040-5079, 5080-5119, ). Stored as `bdc_metadata_block`. | register value | — | R/W | SOURCE_ONLY | source_claim | — |
| holding | 5014 | Bdc Slot 1 Metadata | Repeat for additional BDCs at 40-register strides (5040-5079, 5080-5119, ). Stored as `bdc_metadata_block`. | register value | — | R/W | SOURCE_ONLY | source_claim | — |
| holding | 5015 | Bdc Slot 1 Metadata | Repeat for additional BDCs at 40-register strides (5040-5079, 5080-5119, ). Stored as `bdc_metadata_block`. | register value | — | R/W | SOURCE_ONLY | source_claim | — |
| holding | 5016 | Bdc Slot 1 Metadata | Repeat for additional BDCs at 40-register strides (5040-5079, 5080-5119, ). Stored as `bdc_metadata_block`. | register value | — | R/W | SOURCE_ONLY | source_claim | — |
| holding | 5017 | Bdc Slot 1 Metadata | Repeat for additional BDCs at 40-register strides (5040-5079, 5080-5119, ). Stored as `bdc_metadata_block`. | register value | — | R/W | SOURCE_ONLY | source_claim | — |
| holding | 5018 | Bdc Slot 1 Metadata | Repeat for additional BDCs at 40-register strides (5040-5079, 5080-5119, ). Stored as `bdc_metadata_block`. | register value | — | R/W | SOURCE_ONLY | source_claim | — |
| holding | 5019 | Bdc Slot 1 Metadata | Repeat for additional BDCs at 40-register strides (5040-5079, 5080-5119, ). Stored as `bdc_metadata_block`. | register value | — | R/W | SOURCE_ONLY | source_claim | — |
| holding | 5020 | Bdc Slot 1 Metadata | Repeat for additional BDCs at 40-register strides (5040-5079, 5080-5119, ). Stored as `bdc_metadata_block`. | register value | — | R/W | SOURCE_ONLY | source_claim | — |
| holding | 5021 | Bdc Slot 1 Metadata | Repeat for additional BDCs at 40-register strides (5040-5079, 5080-5119, ). Stored as `bdc_metadata_block`. | register value | — | R/W | SOURCE_ONLY | source_claim | — |
| holding | 5022 | Bdc Slot 1 Metadata | Repeat for additional BDCs at 40-register strides (5040-5079, 5080-5119, ). Stored as `bdc_metadata_block`. | register value | — | R/W | SOURCE_ONLY | source_claim | — |
| holding | 5023 | Bdc Slot 1 Metadata | Repeat for additional BDCs at 40-register strides (5040-5079, 5080-5119, ). Stored as `bdc_metadata_block`. | register value | — | R/W | SOURCE_ONLY | source_claim | — |
| holding | 5024 | Bdc Slot 1 Metadata | Repeat for additional BDCs at 40-register strides (5040-5079, 5080-5119, ). Stored as `bdc_metadata_block`. | register value | — | R/W | SOURCE_ONLY | source_claim | — |
| holding | 5025 | Bdc Slot 1 Metadata | Repeat for additional BDCs at 40-register strides (5040-5079, 5080-5119, ). Stored as `bdc_metadata_block`. | register value | — | R/W | SOURCE_ONLY | source_claim | — |
| holding | 5026 | Bdc Slot 1 Metadata | Repeat for additional BDCs at 40-register strides (5040-5079, 5080-5119, ). Stored as `bdc_metadata_block`. | register value | — | R/W | SOURCE_ONLY | source_claim | — |
| holding | 5027 | Bdc Slot 1 Metadata | Repeat for additional BDCs at 40-register strides (5040-5079, 5080-5119, ). Stored as `bdc_metadata_block`. | register value | — | R/W | SOURCE_ONLY | source_claim | — |
| holding | 5028 | Bdc Slot 1 Metadata | Repeat for additional BDCs at 40-register strides (5040-5079, 5080-5119, ). Stored as `bdc_metadata_block`. | register value | — | R/W | SOURCE_ONLY | source_claim | — |
| holding | 5029 | Bdc Slot 1 Metadata | Repeat for additional BDCs at 40-register strides (5040-5079, 5080-5119, ). Stored as `bdc_metadata_block`. | register value | — | R/W | SOURCE_ONLY | source_claim | — |
| holding | 5030 | Bdc Slot 1 Metadata | Repeat for additional BDCs at 40-register strides (5040-5079, 5080-5119, ). Stored as `bdc_metadata_block`. | register value | — | R/W | SOURCE_ONLY | source_claim | — |
| holding | 5031 | Bdc Slot 1 Metadata | Repeat for additional BDCs at 40-register strides (5040-5079, 5080-5119, ). Stored as `bdc_metadata_block`. | register value | — | R/W | SOURCE_ONLY | source_claim | — |
| holding | 5032 | Bdc Slot 1 Metadata | Repeat for additional BDCs at 40-register strides (5040-5079, 5080-5119, ). Stored as `bdc_metadata_block`. | register value | — | R/W | SOURCE_ONLY | source_claim | — |
| holding | 5033 | Bdc Slot 1 Metadata | Repeat for additional BDCs at 40-register strides (5040-5079, 5080-5119, ). Stored as `bdc_metadata_block`. | register value | — | R/W | SOURCE_ONLY | source_claim | — |
| holding | 5034 | Bdc Slot 1 Metadata | Repeat for additional BDCs at 40-register strides (5040-5079, 5080-5119, ). Stored as `bdc_metadata_block`. | register value | — | R/W | SOURCE_ONLY | source_claim | — |
| holding | 5035 | Bdc Slot 1 Metadata | Repeat for additional BDCs at 40-register strides (5040-5079, 5080-5119, ). Stored as `bdc_metadata_block`. | register value | — | R/W | SOURCE_ONLY | source_claim | — |
| holding | 5036 | Bdc Slot 1 Metadata | Repeat for additional BDCs at 40-register strides (5040-5079, 5080-5119, ). Stored as `bdc_metadata_block`. | register value | — | R/W | SOURCE_ONLY | source_claim | — |
| holding | 5037 | Bdc Slot 1 Metadata | Repeat for additional BDCs at 40-register strides (5040-5079, 5080-5119, ). Stored as `bdc_metadata_block`. | register value | — | R/W | SOURCE_ONLY | source_claim | — |
| holding | 5038 | Bdc Slot 1 Metadata | Repeat for additional BDCs at 40-register strides (5040-5079, 5080-5119, ). Stored as `bdc_metadata_block`. | register value | — | R/W | SOURCE_ONLY | source_claim | — |
| holding | 5039 | Bdc Slot 1 Metadata | Repeat for additional BDCs at 40-register strides (5040-5079, 5080-5119, ). Stored as `bdc_metadata_block`. | register value | — | R/W | SOURCE_ONLY | source_claim | — |
| input | 3000 | Inverter status | Inverterrunstate High8bitsmode(specificmode) 0:Waitingmodule 1:Self-testmode,optional 2:Reserved 3：SysFault module 4:Flashmodule 5：PVBATOnlinemodule: 6：BatOnlinemodule | register value; /10 | — | R | UNKNOWN_RESERVED | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3001 | PV input power | PVtotalpower | register value; /10 | W | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3002 | PV input power | Total PV input power summed across all strings (0.1 W resolution). | register value; /10 | W | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3003 | PV1 DC voltage | PV1voltage | register value; /10 | V | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3004 | PV1 DC current | PV1inputcurrent | register value; /10 | A | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3005 | PV1 DC power | PV1power | register value; /10 | W | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3006 | PV1 DC power | Real-time DC power from PV1 computed from voltage and current readings. | register value; /10 | W | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3007 | PV2 DC voltage | PV2voltage | register value; /10 | V | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3008 | PV2 DC current | PV2inputcurrent | register value; /10 | A | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3009 | PV2 DC power | PV2power | register value; /10 | W | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3010 | PV2 DC power | Real-time DC power from PV2 computed from voltage and current readings. | register value; /10 | W | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3011 | PV3 DC voltage | PV3voltage | register value; /10 | V | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3012 | PV3 DC current | PV3inputcurrent | register value; /10 | A | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3013 | PV3 DC power | PV3power | register value; /10 | W | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3014 | PV3 DC power | Real-time DC power from PV3 computed from voltage and current readings. | register value; /10 | W | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3015 | PV4 DC voltage | PV4voltage | register value; /10 | V | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3016 | PV4 DC current | PV4inputcurrent | register value; /10 | A | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3017 | PV4 DC power | PV4power | register value; /10 | W | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3018 | PV4 DC power | Real-time DC power from PV4 computed from voltage and current readings. | register value; /10 | W | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3019 | System output power | Systemoutputpower | register value; /10 | W | R | RESOLVED | semantic_correlated, source_claim | — |
| input | 3020 | System output power | AC output power reported by the TL-XH mirror block (0.1 W resolution). Mirrors the value at register 35. | register value; /10 | W | R | RESOLVED | semantic_correlated, source_claim | — |
| input | 3021 | Output reactive power | reactivepower | register value; /10 | var | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3022 | Output reactive power | Instantaneous reactive power on the AC output (positive = inductive, negative = capacitive). | register value; /10 | var | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3023 | AC output power | Outputpower | register value; /10 | Output power | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3024 | AC output power | Active AC output power delivered by the inverter (0.1 W resolution). | register value; /10 | W | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3025 | Grid frequency | Gridfrequency | register value; /100 | Grid frequency | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3026 | AC phase L1 voltage | Three/singlephasegridvoltage | register value; /10 | Three/single phase grid voltage | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3027 | AC phase L1 current | Three/singlephasegridoutputcurrent | register value; /10 | Three/single | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3028 | AC phase L1 power | Three/singlephasegridoutputwatt VA | register value; /10 | Three/single phasegrid outputwatt VA | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3029 | AC phase L1 power | Active power exported on phase L1. | register value; /10 | W | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3030 | AC phase L2 voltage | Threephasegridvoltage | register value; /10 | Threephase gridvoltage | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3031 | AC phase L2 current | Threephasegridoutputcurrent | register value; /10 | Threephase gridoutput current | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3032 | AC phase L2 power | Threephasegridoutputpower | register value; /10 | Threephase gridoutput power | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3033 | AC phase L2 power | Active power exported on phase L2. | register value; /10 | W | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3034 | AC phase L3 voltage | Threephasegridvoltage | register value; /10 | Threephase gridvoltage | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3035 | AC phase L3 current | Threephasegridoutputcurrent | register value; /10 | Threephase gridoutput current | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3036 | AC phase L3 power | Threephasegridoutputpower | register value; /10 | Threephase gridoutput power | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3037 | AC phase L3 power | Active power exported on phase L3. | register value; /10 | W | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3038 | RS line voltage | Threephasegridvoltage | register value; /10 | V | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3039 | ST line voltage | Threephasegridvoltage | register value; /10 | V | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3040 | TR line voltage | Threephasegridvoltage | register value; /10 | V | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3041 | Load supply power | Totalforwardpower | register value; /10 | Total forward power | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3042 | Load supply power | Real-time active power delivered to on-site (self-consumption) loads. | register value; /10 | W | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3043 | Grid export power | Totalreversepower | register value; /10 | Totalreverse power | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3044 | Grid export power | Active power exported to the utility grid. | register value; /10 | W | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3045 | Home load power | Totalloadpower | register value; /10 | Total load power | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3046 | Home load power | Aggregate instantaneous demand from on-site loads. | register value; /10 | W | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3047 | Run time | Raw counter counts seconds; divide by 7200 to obtain hours. | register value; /7200 | h | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3048 | Run time | Raw counter counts seconds; divide by 7200 to obtain hours. | register value; /7200 | h | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3049 | Output energy today | Todaygenerateenergy | register value; /10 | Today generate energy | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3050 | Output energy today | Energy exported to the AC output today (0.1 kWh resolution). | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3051 | Output energy total | Totalgenerateenergy | register value; /10 | Total generate | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3052 | Output energy total | Lifetime AC output energy (0.1 kWh resolution). | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3053 | PV energy total | PVenergytotal | register value; /10 | PVenergy total | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3054 | PV energy total | Total PV energy generated across all strings (0.1 kWh resolution). | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3055 | PV1 energy today | PV1energytoday | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3056 | PV1 energy today | Energy harvested by PV1 today. Values use 0.1 kWh resolution. | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3057 | PV1 energy total | PV1energytotal | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3058 | PV1 energy total | Lifetime energy harvested by PV1. Values use 0.1 kWh resolution. | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3059 | PV2 energy today | PV2energytoday | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3060 | PV2 energy today | Energy harvested by PV2 today. Values use 0.1 kWh resolution. | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3061 | PV2 energy total | PV2energytotal | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3062 | PV2 energy total | Lifetime energy harvested by PV2. Values use 0.1 kWh resolution. | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3063 | PV3 energy today | PV3energytoday | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3064 | PV3 energy today | Energy harvested by PV3 today. Values use 0.1 kWh resolution. | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3065 | PV3 energy total | PV3energytotal | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3066 | PV3 energy total | Lifetime energy harvested by PV3. Values use 0.1 kWh resolution. | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3067 | Load energy today | Todayenergytouser | register value; /10 | Todayenergy touser | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3068 | Load energy today | Energy delivered to on-site loads today (0.1 kWh resolution). | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3069 | Load energy total | Totalenergytouser | register value; /10 | Totalenergy touser | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3070 | Load energy total | Lifetime energy delivered to on-site loads (0.1 kWh resolution). | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3071 | Export energy today | Todayenergytogrid | register value; /10 | Todayenergy togrid | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3072 | Export energy today | Energy exported to the grid today (0.1 kWh resolution). | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3073 | Export energy total | Totalenergytogrid | register value; /10 | Totalenergy togrid | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3074 | Export energy total | Lifetime energy exported to the grid (0.1 kWh resolution). | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3075 | User load energy today | Todayenergyofuserload | register value; /10 | Todayenergy ofuserload | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3076 | User load energy today | Energy delivered to on-site loads today (0.1 kWh resolution). | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3077 | User load energy total | Totalenergyofuserload | register value; /10 | Totalenergy ofuserload | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3078 | User load energy total | Lifetime energy delivered to on-site loads (0.1 kWh resolution). | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3079 | PV4 energy today | PV4energytoday | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3080 | PV4 energy today | Energy harvested by PV string 4 today (0.1 kWh resolution). | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3081 | PV4 energy total | PV4energytotal | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3082 | PV4 energy total | Lifetime energy harvested by PV string 4 (0.1 kWh resolution). | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3083 | PV energy today | PVenergytoday | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3084 | PV energy today | Total PV energy harvested across all strings today (0.1 kWh resolution). | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3085 | Reserved | Reserved | register value; /1 | — | R | UNKNOWN_RESERVED | semantic_correlated, source_claim | — |
| input | 3086 | Derating mode | DeratingMode | register value; /1 | 0:cNOTDerate 1:cPVHighDer ate 2: cPowerCon stantDerate 3: cGridVHigh Derate 4:cFreqHighD erate 5:cDcSoureM odeDerate 6:cInvTemprD erate 7:cActivePow erOrder 8:cLoadSpeed Process 9:cOverBack byTime 10:cInternalT emprDerate 11:cOutTemp rDerate 12:cLineImpe CalcDerate 13: cParallelA ntiBackflowD erate 14:cLocalAnti BackflowDera te 15:cBdcLoadP riDerate 16:cChkCTErr Derate | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3087 | PV insulation resistance | PVISOvalue | register value; /1 | kΩ | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3088 | Residual current R | RDCICurr | register value; /10 | mA | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3089 | Residual current S | SDCICurr | register value; /10 | mA | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3090 | Residual current T | TDCICurr | register value; /10 | mA | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3091 | GFCI current | GFCICurr | register value; /1 | mA | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3092 | Total bus voltage | totalbusvoltage | register value; /10 | V | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3093 | Inverter temperature | Invertertemperature | register value; /10 | °C | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3094 | IPM temperature | TheinsideIPMininvertertemperature | register value; /10 | °C | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3095 | Boost temperature | Boosttemperature | register value; /10 | °C | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3096 | Temp4 | Reserved | register value; /10 | — | R | UNKNOWN_RESERVED | semantic_correlated, source_claim | — |
| input | 3097 | Communication board temperature | Commmunicationbroadtemperature | register value; /10 | °C | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3098 | P-bus voltage | PBusinsideVoltage | register value; /10 | V | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3099 | N-bus voltage | NBusinsideVoltage | register value; /10 | V | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3100 | Inverter output power factor | InverteroutputPFnow | register value; /1 | 0-20000 | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3101 | Output power percentage | RealOutputpowerPercent | register value; /1 | 1~100 | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3102 | Output max power limit | OutputMaxpowerLimited | register value; /10 | Output Maxpower Limited | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3103 | Output max power limit | Current active output power limit enforced by the inverter (0.1 W resolution). | register value; /10 | W | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3104 | Standby flags | Inverterstandbyflag | register value; /1 | bit0:turn off Order； bit1:PVLow； bit2:AC Volt/Freq outofscope； bit3~bit7 ： Reserved | R | RESOLVED | semantic_correlated, source_claim | — |
| input | 3105 | Fault code | Inverterfaultmaincode | register value; /1 | — | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3106 | Warning main code | InverterWarningmaincode | register value; /1 | — | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3107 | Fault subcode | Inverterfaultsubcode | register value; /1 | — | R | RESOLVED | semantic_correlated, source_claim | — |
| input | 3108 | Warning subcode | InverterWarningsubcode | register value; /1 | — | R | RESOLVED | semantic_correlated, source_claim | — |
| input | 3109 | Register 3109 | — | register value; /1 | — | R | UNKNOWN_RESERVED | semantic_correlated, source_claim | — |
| input | 3110 | Warning code | Current inverter warning code (vendor-defined bitmask). | register value; /1 | — | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3111 | Warning code | PresentFFTValue[CHANNEL_A] | register value; /1 | — | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3112 | AFCI status | AFCIStatus | register value; /1 | 0 ： waiting state 1：self-check 2：Detection of arcing state 3：faultstate 4 ： update state | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3113 | AFCI strength (channel A) | AFCIStrength[CHANNEL_A] | register value; /1 | — | R | RESOLVED | semantic_correlated, source_claim | — |
| input | 3114 | AFCI self-check (channel A) | AFCISelfCheck[CHANNEL_A] | register value; /1 | — | R | RESOLVED | semantic_correlated, source_claim | — |
| input | 3115 | Inverter start delay | invstartdelaytime | register value; /1 | invstartdelay time | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3116 | Reserved | Reserved | register value; /1 | — | R | UNKNOWN_RESERVED | semantic_correlated, source_claim | — |
| input | 3117 | Reserved | Reserved | register value; /1 | — | R | UNKNOWN_RESERVED | semantic_correlated, source_claim | — |
| input | 3118 | BDC connect state | BDCconnectstate | register value; /1 | 0:No BDC Connect 1:BDC1 Connect 2:BDC2 Connect 3:BDC1+BDC2 Connect | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3119 | Dry contact state | CurrentstatusofDryContact | register value; /1 | Current status of DryContact 0:turnoff; 1:turnon; | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3120 | Reserved | Reserved | register value; /1 | — | R | UNKNOWN_RESERVED | semantic_correlated, source_claim | — |
| input | 3121 | Self-use power | self-usepower | register value; /10 | W | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3122 | Self-use power | Real-time power consumed by on-site loads (0.1 W resolution). | register value; /10 | W | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3123 | System energy today | Systemenergytoday | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3124 | System energy today | Total energy processed by the hybrid system today (0.1 kWh resolution). | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3125 | Battery discharge today | Todaydischargeenergy | register value; /10 | Today discharge energy | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3126 | Battery discharge today | Energy discharged from the battery into the AC system today (0.1 kWh resolution). | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3127 | Battery discharge total | Totaldischargeenergy | register value; /10 | Total discharge energy | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3128 | Battery discharge total | Total energy discharged from the battery (0.1 kWh resolution). | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3129 | Battery charge today | Chargeenergytoday | register value; /10 | Charge energytoday | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3130 | Battery charge today | Energy charged into the battery today (0.1 kWh resolution). | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3131 | Battery charge total | Chargeenergytotal | register value; /10 | Charge energytotal | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3132 | Battery charge total | Total energy charged into the battery (0.1 kWh resolution). | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3133 | AC charge energy today | TodayenergyofACcharge | register value; /10 | Todayenergy ofACcharge | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3134 | AC charge energy today | Energy charged into the battery from AC today (0.1 kWh resolution). | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3135 | AC charge energy total | TotalenergyofACcharge | register value; /10 | Totalenergy ofACcharge | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3136 | AC charge energy total | Lifetime energy charged into the battery from AC (0.1 kWh resolution). | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3137 | System energy total | Lifetime hybrid system energy throughput (0.1 kWh resolution). | register value; /1 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3138 | System energy total | Totalenergyofsystemoutput\ | register value; /1 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3139 | Self-use energy today | TodayenergyofSelfoutput | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3140 | Self-use energy today | Energy supplied to on-site loads today (0.1 kWh resolution). | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3141 | Self-use energy total | TotalenergyofSelfoutput | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3142 | Self-use energy total | Lifetime energy supplied to on-site loads (0.1 kWh resolution). | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3143 | Reserved | Reserved | register value; /1 | — | R | UNKNOWN_RESERVED | semantic_correlated, source_claim | — |
| input | 3144 | Priority mode | WordMode | register value | 0 LoadFirst 1 BatteryFirs t 2 GridFirst | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3145 | EPS frequency | UPSfrequency | register value | Hz | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3146 | EPS phase R voltage | UPSphaseRoutputvoltage | register value; /10 | V | R | RESOLVED | semantic_correlated, source_claim | — |
| input | 3147 | EPS phase R current | UPSphaseRoutputcurrent | register value; /10 | A | R | RESOLVED | semantic_correlated, source_claim | — |
| input | 3148 | EPS phase R apparent power | UPSphaseRoutputpower | register value | VA | R | SOURCE_ONLY | source_claim | — |
| input | 3149 | EPS phase R apparent power | Phase R apparent power on the EPS output (0.1 VA resolution). | register value | VA | R | SOURCE_ONLY | source_claim | — |
| input | 3150 | EPS phase S voltage | UPSphaseSoutputvoltage | register value; /10 | V | R | RESOLVED | semantic_correlated, source_claim | — |
| input | 3151 | EPS phase S current | UPSphaseSoutputcurrent | register value; /10 | A | R | RESOLVED | semantic_correlated, source_claim | — |
| input | 3152 | EPS phase S apparent power | UPSphaseSoutputpower | register value; /10 | VA | R | RESOLVED | semantic_correlated, source_claim | — |
| input | 3153 | EPS phase S apparent power | Phase S apparent power on the EPS output (0.1 VA resolution). | register value; /10 | VA | R | RESOLVED | semantic_correlated, source_claim | — |
| input | 3154 | EPS phase T voltage | UPSphaseToutputvoltage | register value; /10 | V | R | RESOLVED | semantic_correlated, source_claim | — |
| input | 3155 | EPS phase T current | UPSphaseToutputcurrent | register value; /10 | A | R | RESOLVED | semantic_correlated, source_claim | — |
| input | 3156 | EPS phase T apparent power | UPSphaseToutputpower | register value; /10 | VA | R | RESOLVED | semantic_correlated, source_claim | — |
| input | 3157 | EPS phase T apparent power | Phase T apparent power on the EPS output (0.1 VA resolution). | register value; /10 | VA | R | RESOLVED | semantic_correlated, source_claim | — |
| input | 3158 | EPS total apparent power | UPSoutputpower | register value; /10 | VA | R | RESOLVED | semantic_correlated, source_claim | — |
| input | 3159 | EPS total apparent power | Total apparent power delivered by the EPS output (0.1 VA resolution). | register value; /10 | VA | R | RESOLVED | semantic_correlated, source_claim | — |
| input | 3160 | EPS load percentage | LoadpercentofUPSouput | register value; /10 | % | R | RESOLVED | semantic_correlated, source_claim | — |
| input | 3161 | BDC power factor | Powerfactor | register value; /10 | pf | R | RESOLVED | semantic_correlated, source_claim | — |
| input | 3162 | BDC DC voltage | DCvoltage | register value; /1 | V | R | RESOLVED | semantic_correlated, source_claim | — |
| input | 3163 | Reserved | Reserved | register value; /1 | — | R | UNKNOWN_RESERVED | semantic_correlated, source_claim | — |
| input | 3164 | BDC presence flag | WhethertoparseBDCdataseparately | register value; /1 | 0:Don'tneed 1：need | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3165 | BDC derating mode | BDCDeratingMode： 0:Normal,unrestricted 1：Standbyorfault 2：Maximumbatterycurrentlimit (discharge) 3：BatterydischargeEnable(Discharge) 4：Highbusdischargederating | register value; /1 | — | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3166 | BDC system mode | SystemworkStateandmodeThe upper8bitsindicatethemode; 0：Nochargeanddischarge； 1：charge； 2：Discharge； Thelower8bitsrepresentthestatus; 0:StandbyStatus; 1:NormalStatus; 2:FaultStatus 3：FlashStatus; | register value; /1 | BDC1 | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3167 | BDC fault code | Storgedevicefaultcode | register value; /1 | — | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3168 | BDC warning code | Storgedevicewarningcode | register value; /1 | — | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3169 | Battery voltage | Batteryvoltage | register value; /100 | V | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3170 | Battery current | Batterycurrent | register value; /10 | A | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3171 | Battery SOC | StateofchargeCapacity | register value; /1 | % | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3172 | VBUS1 voltage | TotalBUSvoltage | register value; /10 | V | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3173 | VBUS2 voltage | OntheBUSvoltage | register value; /10 | V | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3174 | Buck/boost current | BUCK-BOOSTCurrent | register value; /10 | A | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3175 | LLC stage current | LLCCurrent | register value; /10 | A | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3176 | Battery temperature A | TempertureA | register value; /10 | °C | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3177 | Battery temperature B | TempertureB | register value; /10 | °C | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3178 | Battery discharge power | Dischargepower | register value; /10 | W | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3179 | Battery discharge power | Real-time discharge power flowing from the battery (0.1 W resolution). | register value; /10 | W | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3180 | Battery charge power | Chargepower | register value; /10 | W | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3181 | Battery charge power | Real-time charge power flowing into the battery (0.1 W resolution). | register value; /10 | W | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3182 | BDC discharge energy total | Dischargetotalenergyofstorgedevice | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3183 | BDC discharge energy total | Lifetime energy discharged by the battery DC converter (0.1 kWh resolution). | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3184 | BDC charge energy total | Chargetotalenergyofstorgedevice | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3185 | BDC charge energy total | Lifetime energy charged into the battery via the BDC (0.1 kWh resolution). | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3186 | Reserved | Reserved | register value; /1 | — | R | UNKNOWN_RESERVED | semantic_correlated, source_claim | — |
| input | 3187 | BDC flag word | BDCmark(chargeanddischarge, faultalarmcode) Bit0:ChargeEn;BDCallowscharging Bit1:DischargeEn;BDCallows discharge Bit2~7:Resvd;reserved Bit8~11:WarnSubCode;BDC sub-warningcode Bit12~15:FaultSubCode;BDC sub-errorcode | register value; /1 | — | R | UNKNOWN_RESERVED | semantic_correlated, source_claim | — |
| input | 3188 | VBUS2 low voltage | LowerBUSvoltage | register value; /10 | V | R | RESOLVED | semantic_correlated, source_claim | — |
| input | 3189 | BMS max cell index | BmsMaxVoltCellNo | register value; /1 | — | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3190 | BMS min cell index | BmsMinVoltCellNo | register value; /1 | — | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3191 | BMS average temperature A | BmsBatteryAvgTemp | register value; /1 | °C | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3192 | BMS max cell temperature A | BmsMaxCellTemp | register value; /10 | °C | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3193 | BMS average temperature B | BmsBatteryAvgTemp | register value; /10 | °C | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3194 | BMS max cell temperature B | BmsMaxCellTemp | register value; /1 | °C | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3195 | BMS average temperature C | BmsBatteryAvgTemp | register value; /1 | °C | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3196 | BMS max SOC | BmsMaxSOC | register value; /1 | % | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3197 | BMS min SOC | BmsMinSOC | register value; /1 | % | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3198 | Parallel battery count | ParallelBatteryNum | register value; /1 | — | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3199 | BMS derate reason | BmsDerateReason | register value; /1 | — | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3200 | BMS full charge capacity | BmsGaugeFCC（Ah） | register value; /1 | Ah | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3201 | BMS remaining capacity | BmsGaugeRM（Ah） | register value; /1 | Ah | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3202 | BMS protect flags 1 | BMSProtect1 | register value; /1 | — | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3203 | BMS warning flags 1 | BMSWarn1 | register value; /1 | — | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3204 | BMS fault flags 1 | BMSFault1 | register value; /1 | — | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3205 | BMS fault flags 2 | BMSFault2 | register value; /1 | — | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3206 | Reserved | Reserved | register value; /1 | — | R | UNKNOWN_RESERVED | semantic_correlated, source_claim | — |
| input | 3207 | Reserved | Reserved | register value; /1 | — | R | UNKNOWN_RESERVED | semantic_correlated, source_claim | — |
| input | 3208 | Reserved | Reserved | register value; /1 | — | R | UNKNOWN_RESERVED | semantic_correlated, source_claim | — |
| input | 3209 | Reserved | Reserved | register value; /1 | — | R | UNKNOWN_RESERVED | semantic_correlated, source_claim | — |
| input | 3210 | Battery insulation status | BatteryISOdetectionstatus | register value; /1 | 0：Not detected 1：Detection completed | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3211 | Battery request flags | batteryworkrequest | register value; /1 | — | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3212 | BMS status | batteryworkingstatus | register value; /1 | 0:dormancy 1:Charge 2:Discharge 3:free 4:standby 5:Softstart 6:fault 7:update | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3213 | BMS protect flags 2 | BMSProtect2 | register value; /1 | — | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3214 | BMS warning flags 2 | BMSWarn2 | register value; /1 | — | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3215 | BMS SOC | BMSSOC | register value; /1 | % | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3216 | BMS battery voltage | BMSBatteryVolt | register value; /100 | V | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3217 | BMS battery current | Positive values indicate discharge from the battery; negative values indicate charging. | register value; /100 | A | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3218 | BMS max cell temperature | batterycellmaximumtemperature | register value; /10 | °C | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3219 | BMS max charge current | Maximumchargingcurrent | register value; /100 | A | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3220 | BMS max discharge current | Maximumdischargecurrent | register value; /100 | A | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3221 | BMS cycle count | BMSCycleCnt | register value; /1 | — | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3222 | BMS state of health | BMSSOH | register value; /1 | % | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3223 | BMS charge voltage limit | Batterychargingvoltagelimitvalue | register value; /100 | V | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3224 | BMS discharge voltage limit | Batterydischargevoltagelimitvalue | register value; /1 | V | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3225 | BMS warning flags 3 | BMSWarn3 | register value; /1 | — | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3226 | BMS protect flags 3 | BMSProtect3 | register value; /1 | — | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3227 | Reserved | Reserved | register value; /1 | — | R | UNKNOWN_RESERVED | semantic_correlated, source_claim | — |
| input | 3228 | Reserved | Reserved | register value; /1 | — | R | UNKNOWN_RESERVED | semantic_correlated, source_claim | — |
| input | 3229 | Reserved | Reserved | register value; /1 | — | R | UNKNOWN_RESERVED | semantic_correlated, source_claim | — |
| input | 3230 | BMS max cell voltage | BMSBatterySingleVoltMax | register value; /1 | V | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3231 | BMS min cell voltage | BMSBatterySingleVoltMin | register value; /1 | V | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3232 | Battery load voltage | BatteryLoadVolt | register value; /100 | [0，650.00] | R | RESOLVED | semantic_correlated, source_claim | — |
| input | 3233 | Register 3233 | — | register value; /1 | — | R | UNKNOWN_RESERVED | semantic_correlated, source_claim | — |
| input | 3234 | Debug data 1 | Debugdata1 | register value; /1 | — | R | RESOLVED | semantic_correlated, source_claim | — |
| input | 3235 | Debug data 2 | Debugdata2 | register value; /1 | — | R | RESOLVED | semantic_correlated, source_claim | — |
| input | 3236 | Debug data 3 | Debugdata3 | register value; /1 | — | R | RESOLVED | semantic_correlated, source_claim | — |
| input | 3237 | Debug data 4 | Debugdata4 | register value; /1 | — | R | RESOLVED | semantic_correlated, source_claim | — |
| input | 3238 | Debug data 5 | Debugdata5 | register value; /1 | — | R | RESOLVED | semantic_correlated, source_claim | — |
| input | 3239 | Debug data 6 | Debugdata6 | register value; /1 | — | R | RESOLVED | semantic_correlated, source_claim | — |
| input | 3240 | Debug data 7 | Debugdata7 | register value; /1 | — | R | RESOLVED | semantic_correlated, source_claim | — |
| input | 3241 | Debug data 8 | Debugdata8 | register value; /1 | — | R | RESOLVED | semantic_correlated, source_claim | — |
| input | 3242 | Debug data 9 | Debugdata9 | register value; /1 | — | R | RESOLVED | semantic_correlated, source_claim | — |
| input | 3243 | Debug data 10 | Debugdata10 | register value; /1 | — | R | RESOLVED | semantic_correlated, source_claim | — |
| input | 3244 | Debug data 11 | Debugdata10 | register value; /1 | — | R | RESOLVED | semantic_correlated, source_claim | — |
| input | 3245 | Debug data 12 | Debugdata12 | register value; /1 | — | R | RESOLVED | semantic_correlated, source_claim | — |
| input | 3246 | Debug data 13 | Debugdata13 | register value; /1 | — | R | RESOLVED | semantic_correlated, source_claim | — |
| input | 3247 | Debug data 14 | Debugdata14 | register value; /1 | — | R | RESOLVED | semantic_correlated, source_claim | — |
| input | 3248 | Debug data 15 | Debugdata15 | register value; /1 | — | R | RESOLVED | semantic_correlated, source_claim | — |
| input | 3249 | Debug data 16 | Debugdata16 | register value; /1 | — | R | RESOLVED | semantic_correlated, source_claim | — |

### MIX storage

Storage family applicability comes from the graph/catalogue ranges.

| Table | Address | Name | Description | Encoding / scale | Unit | Access | Status | Evidence | Notes |
|---|---:|---|---|---|---|---|---|---|---|
| holding | 0 | Inverter Enabled | Theinvertercanbeswitched onandoff,andtheBDCcanbe switchedonandoffforthe battreadyfunction. | register value; /10 | — | R/W | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| holding | 1 | Safety function enable flags | SPI: system protection interface Bit0~3:forCEI0-21 Bit4~6:forSAA | register value | — | W | SOURCE_ONLY | source_claim | — |
| holding | 2 | Persist power-factor commands | Means these settings will be acting or not when next poweron | register value | — | W | RESOLVED | semantic_correlated, source_claim | — |
| holding | 3 | Active power limit setpoint | 255:powerisnotbelimited | register value; /1 | % | W | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| holding | 4 | Reactive power limit setpoint | 255:powerisnotbelimited | register value; /1 | % | W | SOURCE_ONLY | source_claim | — |
| holding | 5 | Power factor target | Inverter output power factor’s10000times | register value; /10000 | pf | W | SOURCE_ONLY | source_claim | — |
| holding | 6 | Rated apparent power | Normal power(high) | register value; /10 | 0.1VA | R | SOURCE_ONLY | source_claim | — |
| holding | 7 | Rated apparent power | Normal power(low) | register value; /10 | 0.1VA | R | SOURCE_ONLY | source_claim | — |
| holding | 8 | Nominal PV voltage | NormalworkPV voltage | register value; /10 | 0.1V | R | SOURCE_ONLY | source_claim | — |
| holding | 9 | Firmware | Firmwareversion (high) | firmware_version; /10 | ASCII | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| holding | 10 | Firmware | Firmwareversion (middle) | register value | ASCII | R | SOURCE_ONLY | source_claim | — |
| holding | 11 | Firmware | Firmwareversion(low) | register value | ASCII | R | SOURCE_ONLY | source_claim | — |
| holding | 12 | Firmware | ControlFirmware version(high) | register value | ASCII | R | SOURCE_ONLY | source_claim | — |
| holding | 13 | Firmware | ControlFirmware version(middle) | register value | ASCII | R | SOURCE_ONLY | source_claim | — |
| holding | 14 | Firmware | ControlFirmware version(low) | register value | ASCII | R | SOURCE_ONLY | source_claim | — |
| holding | 15 | LCD language selection | 0:Italian; 1:English; 2:German; 3:Spanish; 4:French; 5:Chinese; 6：Polish 7：Portugues 8：Hungary | register value | — | W | SOURCE_ONLY | source_claim | — |
| holding | 16 | Country profile configured | CountrySelectedor not | register value | — | W | SOURCE_ONLY | source_claim | — |
| holding | 17 | PV start voltage threshold | Inputstartvoltage | register value; /10 | 0.1V | W | SOURCE_ONLY | source_claim | — |
| holding | 18 | Start-up delay | Starttime | register value; /1 | 1s | W | SOURCE_ONLY | source_claim | — |
| holding | 19 | Restart delay | RestartDelayTime afterfaultback; | register value; /1 | 1s | W | SOURCE_ONLY | source_claim | — |
| holding | 20 | Active power ramp rate (startup) | Powerstartslope | register value; /10 | 0.1% | W | SOURCE_ONLY | source_claim | — |
| holding | 21 | Active power ramp rate (restart) | Powerrestartslope | register value; /10 | 0.1% | W | SOURCE_ONLY | source_claim | — |
| holding | 22 | Modbus RTU baud rate | Select communicationbaudrat e 0:9600bps 1:38400bps | register value | — | W | SOURCE_ONLY | source_claim | — |
| holding | 23 | Serial Number | The Home Assistant integration exposes this as the device serial number and reuses it as the unique identifier. | serial_number; /10 | ASCII | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| holding | 24 | Serial Number | The Home Assistant integration exposes this as the device serial number and reuses it as the unique identifier. | register value | ASCII | R | SOURCE_ONLY | source_claim | — |
| holding | 25 | Serial Number | The Home Assistant integration exposes this as the device serial number and reuses it as the unique identifier. | register value | ASCII | R | SOURCE_ONLY | source_claim | — |
| holding | 26 | Serial Number | The Home Assistant integration exposes this as the device serial number and reuses it as the unique identifier. | register value | ASCII | R | SOURCE_ONLY | source_claim | — |
| holding | 27 | Serial Number | The Home Assistant integration exposes this as the device serial number and reuses it as the unique identifier. | register value | ASCII | R | SOURCE_ONLY | source_claim | — |
| holding | 28 | Inverter Model | Home Assistant renders this value as the string A# B# D# T# P# U# M# S# via the integration's model() helper. Vendor spec lists value pattern `&*5`; digits appear to be stored without the leading letter codes, so treat as encoded tokens until verified on hardware. | register value; /10 | — | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| holding | 29 | Inverter Model | Home Assistant renders this value as the string A# B# D# T# P# U# M# S# via the integration's model() helper. Vendor spec lists value pattern `&*5`; digits appear to be stored without the leading letter codes, so treat as encoded tokens until verified on hardware. | register value | — | R | SOURCE_ONLY | source_claim | — |
| holding | 30 | Modbus slave address | Communicate address | register value | — | W | SOURCE_ONLY | source_claim | — |
| holding | 31 | Firmware update trigger | Updatefirmware | register value | — | W | SOURCE_ONLY | source_claim | — |
| holding | 32 | Reset user configuration | Use with caution; the inverter immediately reboots and loses provisioning data. | register value | — | W | SOURCE_ONLY | source_claim | — |
| holding | 33 | Factory reset | Equivalent to the front-panel factory reset. Requires re-commissioning afterwards. | register value | — | W | SOURCE_ONLY | source_claim | — |
| holding | 34 | Manufacturer information string | The original table lists these words as Manufacturer Info 8-1 (high/middle/low); combine them to read the full string. | register value | ASCII | R | SOURCE_ONLY | source_claim | — |
| holding | 35 | Manufacturer information string | The original table lists these words as Manufacturer Info 8-1 (high/middle/low); combine them to read the full string. | register value | ASCII | R | SOURCE_ONLY | source_claim | — |
| holding | 36 | Manufacturer information string | The original table lists these words as Manufacturer Info 8-1 (high/middle/low); combine them to read the full string. | register value | ASCII | R | SOURCE_ONLY | source_claim | — |
| holding | 37 | Manufacturer information string | The original table lists these words as Manufacturer Info 8-1 (high/middle/low); combine them to read the full string. | register value | ASCII | R | SOURCE_ONLY | source_claim | — |
| holding | 38 | Manufacturer information string | The original table lists these words as Manufacturer Info 8-1 (high/middle/low); combine them to read the full string. | register value | ASCII | R | SOURCE_ONLY | source_claim | — |
| holding | 39 | Manufacturer information string | The original table lists these words as Manufacturer Info 8-1 (high/middle/low); combine them to read the full string. | register value | ASCII | R | SOURCE_ONLY | source_claim | — |
| holding | 40 | Manufacturer information string | The original table lists these words as Manufacturer Info 8-1 (high/middle/low); combine them to read the full string. | register value | ASCII | R | SOURCE_ONLY | source_claim | — |
| holding | 41 | Manufacturer information string | The original table lists these words as Manufacturer Info 8-1 (high/middle/low); combine them to read the full string. | register value | ASCII | R | SOURCE_ONLY | source_claim | — |
| holding | 42 | G100 failsafe enable | EnglishG100failsafeset | register value | — | W | SOURCE_ONLY | source_claim | — |
| holding | 43 | Device Type Code | Vendor spec provides value pattern `&*6`; handle as encoded type/family digits with implied prefixes pending confirmation. | register value; /10 | — | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| holding | 44 | Number Of Trackers And Phases | Inputtrackernumand outputphasenum | register value; /10 | — | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| holding | 45 | System clock year | Localtime | register value | — | W | SOURCE_ONLY | source_claim | — |
| holding | 46 | System clock month | Systemtime-Month | register value | — | W | SOURCE_ONLY | source_claim | — |
| holding | 47 | System clock day | Systemtime-Day | register value | — | W | SOURCE_ONLY | source_claim | — |
| holding | 48 | System clock hour | Systemtime-Hour | register value | — | W | SOURCE_ONLY | source_claim | — |
| holding | 49 | System clock minute | Systemtime-Min | register value | — | W | SOURCE_ONLY | source_claim | — |
| holding | 50 | System clock second | Systemtime-Second | register value | — | W | SOURCE_ONLY | source_claim | — |
| holding | 51 | System clock weekday | SystemWeekly | register value | — | W | SOURCE_ONLY | source_claim | — |
| holding | 52 | Stage 1 undervoltage limit | Gridvoltagelowlimit protect | register value | 0.1V | W | SOURCE_ONLY | source_claim | — |
| holding | 53 | Stage 1 overvoltage limit | Gridvoltagehighlimit protect | register value | 0.1V | W | SOURCE_ONLY | source_claim | — |
| holding | 54 | Stage 1 underfrequency limit | Gridfrequencylow limitprotect | register value | 0.01 Hz | W | SOURCE_ONLY | source_claim | — |
| holding | 55 | Stage 1 overfrequency limit | Gridhigh frequencylimitprotect | register value | 0.01 Hz | W | SOURCE_ONLY | source_claim | — |
| holding | 56 | Stage 2 undervoltage limit | Gridvoltagelowlimit protect2 | register value | 0.1V | W | SOURCE_ONLY | source_claim | — |
| holding | 57 | Stage 2 overvoltage limit | Gridvoltagehighlimit protect2 | register value | 0.1V | W | SOURCE_ONLY | source_claim | — |
| holding | 58 | Stage 2 underfrequency limit | Gridfrequencylow limitprotect2 | register value | 0.01 Hz | W | SOURCE_ONLY | source_claim | — |
| holding | 59 | Stage 2 overfrequency limit | Gridhighfrequency limitprotect2 | register value | 0.01 Hz | W | SOURCE_ONLY | source_claim | — |
| holding | 60 | Stage 3 undervoltage limit | Grid voltage low limit protect3 | register value | 0.1V | W | SOURCE_ONLY | source_claim | — |
| holding | 61 | Stage 3 overvoltage limit | Grid voltage high limit protect3 | register value | 0.1V | W | SOURCE_ONLY | source_claim | — |
| holding | 62 | Stage 3 underfrequency limit | Grid frequency low limitprotect3 | register value | 0.01Hz | W | SOURCE_ONLY | source_claim | — |
| holding | 63 | Stage 3 overfrequency limit | Grid frequency high limitprotect3 | register value | 0.01Hz | W | SOURCE_ONLY | source_claim | — |
| holding | 64 | Reconnect undervoltage limit | Gridlowvoltagelimit connecttoGrid | register value | 0.1V | W | SOURCE_ONLY | source_claim | — |
| holding | 65 | Reconnect overvoltage limit | Gridhighvoltagelimit connecttoGrid | register value | 0.1V | W | SOURCE_ONLY | source_claim | — |
| holding | 66 | Reconnect underfrequency limit | Gridlowfrequency | register value | 0.01 | W | SOURCE_ONLY | source_claim | — |
| holding | 67 | Reconnect overfrequency limit | Gridhighfrequency limitconnecttoGrid | register value | 0.01 Hz | W | SOURCE_ONLY | source_claim | — |
| holding | 68 | Stage 1 undervoltage trip delay | Grid voltage low limit protecttime 1 | register value | Cycle | W | SOURCE_ONLY | source_claim | — |
| holding | 69 | Stage 1 overvoltage trip delay | Grid voltage high limit protecttime 1 | register value | Cycle | W | SOURCE_ONLY | source_claim | — |
| holding | 70 | Stage 2 undervoltage trip delay | Grid voltage low limit protecttime 2 | register value | Cycle | W | SOURCE_ONLY | source_claim | — |
| holding | 71 | Stage 2 overvoltage trip delay | Grid voltage high limit protecttime 2 | register value | Cycle | W | SOURCE_ONLY | source_claim | — |
| holding | 72 | Stage 1 underfrequency trip delay | Grid frequency low limitprotecttime 1 | register value | Cycle | W | SOURCE_ONLY | source_claim | — |
| holding | 73 | Modbus Version | Grid frequency high limitprotecttime 1 | register value | Cycle | W | SOURCE_ONLY | source_claim | — |
| holding | 74 | Stage 2 underfrequency trip delay | Grid frequency low limitprotecttime 2 | register value | Cycle | W | SOURCE_ONLY | source_claim | — |
| holding | 75 | Stage 2 overfrequency trip delay | Grid frequency high limitprotecttime 2 | register value | Cycle | W | SOURCE_ONLY | source_claim | — |
| holding | 76 | Stage 3 undervoltage trip delay | Grid voltage low limit protecttime 3 | register value | Cycle | W | SOURCE_ONLY | source_claim | — |
| holding | 77 | Stage 3 overvoltage trip delay | Grid voltage high limit protecttime 3 | register value | Cycle | W | SOURCE_ONLY | source_claim | — |
| holding | 78 | Stage 3 underfrequency trip delay | Grid frequency low limitprotecttime 3 | register value | Cycle | W | SOURCE_ONLY | source_claim | — |
| holding | 79 | Stage 3 overfrequency trip delay | Grid frequency high limitprotecttime 3 | register value | Cycle | W | SOURCE_ONLY | source_claim | — |
| holding | 80 | Ten-minute overvoltage limit | Voltprotectionfor10 min | register value | 0.1V | W | SOURCE_ONLY | source_claim | — |
| holding | 81 | PV input high-voltage fault | PVVoltageHigh Fault | register value | 0.1V | W | SOURCE_ONLY | source_claim | — |
| holding | 82 | Controller firmware build string | Positions: 0-1 model letters, 2-3 model variant, 4-5 DSP1 build, 6-7 DSP2/M0 build, 8-9 CPLD/AFCI build, 10-11 M3 build. | register value | ASCII | R | SOURCE_ONLY | source_claim | — |
| holding | 83 | Controller firmware build string | Positions: 0-1 model letters, 2-3 model variant, 4-5 DSP1 build, 6-7 DSP2/M0 build, 8-9 CPLD/AFCI build, 10-11 M3 build. | register value | ASCII | R | SOURCE_ONLY | source_claim | — |
| holding | 84 | Controller firmware build string | Positions: 0-1 model letters, 2-3 model variant, 4-5 DSP1 build, 6-7 DSP2/M0 build, 8-9 CPLD/AFCI build, 10-11 M3 build. | register value | ASCII | R | SOURCE_ONLY | source_claim | — |
| holding | 85 | Controller firmware build string | Positions: 0-1 model letters, 2-3 model variant, 4-5 DSP1 build, 6-7 DSP2/M0 build, 8-9 CPLD/AFCI build, 10-11 M3 build. | register value | ASCII | R | SOURCE_ONLY | source_claim | — |
| holding | 86 | Controller firmware build string | Positions: 0-1 model letters, 2-3 model variant, 4-5 DSP1 build, 6-7 DSP2/M0 build, 8-9 CPLD/AFCI build, 10-11 M3 build. | register value | ASCII | R | SOURCE_ONLY | source_claim | — |
| holding | 87 | Controller firmware build string | Positions: 0-1 model letters, 2-3 model variant, 4-5 DSP1 build, 6-7 DSP2/M0 build, 8-9 CPLD/AFCI build, 10-11 M3 build. | register value | ASCII | R | SOURCE_ONLY | source_claim | — |
| holding | 88 | Modbus Version | ModbusVersion | register value; /100 | Int(16 bits) | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| holding | 89 | Power-factor control mode | 0=Unity PF, 1=Fixed PF setpoint, 2=Default PF line, 3=User-defined PF line, 4=Under-excited reactive power, 5=Over-excited reactive power, 6=Q(V) curve, 7=Direct control, 8=Static capacitive QV, 9=Static inductive QV. | register value | — | W | SOURCE_ONLY | source_claim | — |
| holding | 90 | GPRS modem IP/status flags | Bit 0-3: 0=idle, 1=IP read requested, 2=set IP succeeded; Bit 4-7: 0=unknown, 1=modem OK, 2=no SIM, 3=no network, 4=TCP connect fail, 5=TCP connected, etc. | register value | — | W | UNKNOWN_RESERVED | source_claim | — |
| holding | 91 | Frequency derating start | Frequencyderating startpoint | register value | 0.01H Z | W | SOURCE_ONLY | source_claim | — |
| holding | 92 | Frequency derating slope | Frequency–loadlimit rate | register value | 10tim es | W | SOURCE_ONLY | source_claim | — |
| holding | 93 | CEI 0-21 Q(V) point V1S | CEI021V1SQ(v) | register value | 0.1V | W | SOURCE_ONLY | source_claim | — |
| holding | 94 | CEI 0-21 Q(V) point V2S | CEI021V2SQ(v) | register value | 0.1V | W | SOURCE_ONLY | source_claim | — |
| holding | 95 | CEI 0-21 Q(V) point V1L | CEI021V1LQ(v) | register value | 0.1V | W | SOURCE_ONLY | source_claim | — |
| holding | 96 | CEI 0-21 Q(V) point V2L | CEI021V2LQ(v) | register value | 0.1V | W | SOURCE_ONLY | source_claim | — |
| holding | 97 | Q(V) lock-in active power | Q(v)lockinactive powerofCEI021 | register value | Percen t | W | SOURCE_ONLY | source_claim | — |
| holding | 98 | Q(V) lock-out active power | Q(v)lockOutactive powerofCEI021 | register value | Percen t | W | SOURCE_ONLY | source_claim | — |
| holding | 99 | Power-factor curve lock-in voltage | Lockingirdvoltof CEI021PFline | register value | 0.1V | W | SOURCE_ONLY | source_claim | — |
| holding | 100 | Power-factor curve lock-out voltage | Lockoutgirdvoltof CEI021PFline | register value | 0.1V | W | SOURCE_ONLY | source_claim | — |
| holding | 101 | Power-factor adjust value 1 | PFadjustvalue1 | register value | — | W | SOURCE_ONLY | source_claim | — |
| holding | 102 | Power-factor adjust value 2 | PFadjustvalue2 | register value | — | W | SOURCE_ONLY | source_claim | — |
| holding | 103 | Power-factor adjust value 3 | PFadjustvalue3 | register value | — | W | SOURCE_ONLY | source_claim | — |
| holding | 104 | Power-factor adjust value 4 | PFadjustvalue4 | register value | — | W | SOURCE_ONLY | source_claim | — |
| holding | 105 | Power-factor adjust value 5 | PFadjustvalue5 | register value | — | W | SOURCE_ONLY | source_claim | — |
| holding | 106 | Power-factor adjust value 6 | PFadjustvalue6 | register value | — | W | SOURCE_ONLY | source_claim | — |
| holding | 107 | Q(V) response delay | QV Reactive Power delaytime | register value | 1S | W | SOURCE_ONLY | source_claim | — |
| holding | 108 | Over-frequency derating delay | Overfrequency derati ngdelaytime | register value | 50ms | W | SOURCE_ONLY | source_claim | — |
| holding | 109 | Maximum reactive power magnitude | QmaxforQ(V)curve | register value | 0.1% | W | SOURCE_ONLY | source_claim | — |
| holding | 110 | PF curve point 1 load | 255meansnothispoint | register value | percen t | W | SOURCE_ONLY | source_claim | — |
| holding | 111 | PF curve point 1 target | PFlimitlinepoint1 powerfactor | register value | — | W | SOURCE_ONLY | source_claim | — |
| holding | 112 | PF curve point 2 load | 255meansnothispoint | register value | percen t | W | SOURCE_ONLY | source_claim | — |
| holding | 113 | PF curve point 2 target | PFlimitlinepoint 2powerfactor | register value | — | W | SOURCE_ONLY | source_claim | — |
| holding | 114 | PF curve point 3 load | 255meansnothispoint | register value | percen t | W | SOURCE_ONLY | source_claim | — |
| holding | 115 | PF curve point 3 target | PFlimitlinepoint3 powerfactor | register value | — | W | SOURCE_ONLY | source_claim | — |
| holding | 116 | PF curve point 4 load | 255meansnothispoint | register value | percen t | W | SOURCE_ONLY | source_claim | — |
| holding | 117 | PF curve point 4 target | PFlimitlinepoint4 powerfactor | register value | — | W | SOURCE_ONLY | source_claim | — |
| holding | 118 | Module code segments | SxxBxx | register value | — | R | SOURCE_ONLY | source_claim | — |
| holding | 119 | Module code segments | DxxTxx | register value | — | R | SOURCE_ONLY | source_claim | — |
| holding | 120 | Module code segments | PxxUxx | register value | — | R | SOURCE_ONLY | source_claim | — |
| holding | 121 | Module code segments | Mxxxx Power | register value | — | R | SOURCE_ONLY | source_claim | — |
| holding | 122 | Export limit enable mode | ExportLimitenable, 0:DisableexportLimit; 1:Enable485exportLimit; 2:Enable232exportLimit; 3:EnableCTexportLimit; | register value | — | R/W | SOURCE_ONLY | source_claim | — |
| holding | 123 | Export limit power setpoint | ExportLimitPowerRate | register value | 0.1% | R/W | SOURCE_ONLY | source_claim | — |
| holding | 124 | Tracker coupling mode | 0:Independent 1:DCSource 2:Parallel | register value | — | W | SOURCE_ONLY | source_claim | — |
| holding | 1000 | Float charge current limit i | Float charge current limit i | register value | — | W | SOURCE_ONLY | source_claim | — |
| holding | 1001 | PF CMD memory state | PF CMD memory state | register value | 0or1, | W | SOURCE_ONLY | source_claim | — |
| holding | 1002 | VbatStartF orDischarg e | VbatStartF orDischarg e | register value | — | R | SOURCE_ONLY | source_claim | — |
| holding | 1003 | VbatlowWa rnClr l | VbatlowWa rnClr l | register value | — | R | SOURCE_ONLY | source_claim | — |
| holding | 1004 | Vbatstopfo rdischarge | Vbatstopfo rdischarge | register value | — | W | SOURCE_ONLY | source_claim | — |
| holding | 1005 | Vbat stop forcharge | Shouldstopcharge whenhigherthanthis voltage | register value | 0.01V | W | SOURCE_ONLY | source_claim | — |
| holding | 1006 | Vbat start for discharge | Should not discharge when lower than this voltage | register value | 0.01V | W | SOURCE_ONLY | source_claim | — |
| holding | 1007 | Vbat constant charge | CVvoltage（acid） | register value | 0.01V | W | SOURCE_ONLY | source_claim | — |
| holding | 1008 | EESysInfo.S ysSetEn | SystemEnable | register value | — | W | SOURCE_ONLY | source_claim | — |
| holding | 1009 | Battemp lower limit d | Batterytemperature lowerlimitfordischarge | register value | 0.1℃ | W | SOURCE_ONLY | source_claim | — |
| holding | 1010 | Bat temp upper limit d | Batterytemperature upperlimitfordischarge | register value | 0.1℃ | W | SOURCE_ONLY | source_claim | — |
| holding | 1011 | Bat temp lower limit c | Lowertemperaturelimit | register value | 0.1℃ | W | SOURCE_ONLY | source_claim | — |
| holding | 1012 | Bat temp upper limit c | Uppertemperaturelimit | register value | 0.1℃ | W | SOURCE_ONLY | source_claim | — |
| holding | 1013 | uwUnderFr eDischarge DelyTime | UnderFreDelayTime | register value | 50ms | R | SOURCE_ONLY | source_claim | — |
| holding | 1014 | BatMdlSeri alNum | SPH4-11Kused | register value | — | W | SOURCE_ONLY | source_claim | — |
| holding | 1015 | BatMdlPara llNum | SPH4-11Kused | register value | — | W | SOURCE_ONLY | source_claim | — |
| holding | 1016 | DRMS_EN | 0：disable 1：enable | register value | / | R | SOURCE_ONLY | source_claim | — |
| holding | 1017 | Bat First Start Time 4 | Higheight:hours Loweight:minutes | register value | — | R | SOURCE_ONLY | source_claim | — |
| holding | 1018 | Bat First Stop Time 4 | Higheight:hours Loweight:minutes | register value | — | R | SOURCE_ONLY | source_claim | — |
| holding | 1019 | BatFirst on/off Switch4 | Batterypriorityenable1 | register value | — | R | SOURCE_ONLY | source_claim | — |
| holding | 1020 | Bat First Start Time 5 | Higheight:hours Loweight:minutes | register value | — | R | SOURCE_ONLY | source_claim | — |
| holding | 1021 | BatFirst StopTime 5 | Higheight:hours Loweight:minutes | register value | — | R | SOURCE_ONLY | source_claim | — |
| holding | 1022 | BatFirst on/off Switch5 | Batterypriorityenable1 | register value | — | R | SOURCE_ONLY | source_claim | — |
| holding | 1023 | BatFirst StartTime 6 | Higheight:hours Loweight:minutes | register value | — | R | SOURCE_ONLY | source_claim | — |
| holding | 1024 | BatFirst StopTime 6 | Higheight:hours Loweight:minutes | register value | — | R | SOURCE_ONLY | source_claim | — |
| holding | 1025 | BatFirst on/off Switch6 | Batterypriorityenable1 | register value | — | R | SOURCE_ONLY | source_claim | — |
| holding | 1026 | GridFirst StartTime | Higheight:hours Loweight:minutes | register value | — | R | SOURCE_ONLY | source_claim | — |
| holding | 1027 | GridFirst StopTime 4 | Higheight:hours Loweight:minutes | register value | — | R | SOURCE_ONLY | source_claim | — |
| holding | 1028 | Grid First Stop Switch4 | Gridpriorityenable | register value | — | R | SOURCE_ONLY | source_claim | — |
| holding | 1029 | GridFirst StartTime 5 | Higheight:hours Loweight:minutes | register value | — | R | SOURCE_ONLY | source_claim | — |
| holding | 1030 | GridFirst StopTime 5 | Higheight:hours Loweight:minutes | register value | — | R | SOURCE_ONLY | source_claim | — |
| holding | 1031 | Grid First Stop Switch5 | Gridpriorityenable | register value | — | R | SOURCE_ONLY | source_claim | — |
| holding | 1032 | GridFirst StartTime 6 | Higheight:hours Loweight:minutes | register value | — | R | SOURCE_ONLY | source_claim | — |
| holding | 1033 | GridFirst StopTime 6 | Higheight:hours Loweight:minutes | register value | — | R | SOURCE_ONLY | source_claim | — |
| holding | 1034 | Grid First Stop Switch6 | Gridpriorityenable | register value | — | R | SOURCE_ONLY | source_claim | — |
| holding | 1035 | BatFirst StartTime 4 | Higheight:hours Loweight:minutes | register value | — | R | SOURCE_ONLY | source_claim | — |
| holding | 1036 | / | Reserve | register value | / | R | SOURCE_ONLY | source_claim | — |
| holding | 1037 | bCTMode | UsetheCTModeto ChooseRFCT\Cable CT\METER | register value | — | W | SOURCE_ONLY | source_claim | — |
| holding | 1038 | CTAdjust | CTAdjustenable | register value | — | W | SOURCE_ONLY | source_claim | — |
| holding | 1039 | / | Reserve | register value | / | R | SOURCE_ONLY | source_claim | — |
| holding | 1040 | / | / | register value | — | R | SOURCE_ONLY | source_claim | — |
| holding | 1041 | / | / | register value | — | R | SOURCE_ONLY | source_claim | — |
| holding | 1042 | / | / | register value | — | R | SOURCE_ONLY | source_claim | — |
| holding | 1043 | / | / | register value | — | R | SOURCE_ONLY | source_claim | — |
| holding | 1044 | Priority | ForceChrEn/ForceDischr En Load first/bat first /grid first | register value | — | R | SOURCE_ONLY | source_claim | — |
| holding | 1045 | / | / | register value | — | R | SOURCE_ONLY | source_claim | — |
| holding | 1046 | / | / | register value | — | R | SOURCE_ONLY | source_claim | — |
| holding | 1047 | AgingTestSt ep Cmd | Commandforagingtest | register value | — | R | SOURCE_ONLY | source_claim | — |
| holding | 1048 | BatteryTyp e | Batterytypechooseof buck-boostinput | register value | — | R | SOURCE_ONLY | source_claim | — |
| holding | 1049 | / | / | register value | — | R | SOURCE_ONLY | source_claim | — |
| holding | 1050 | / | / | register value | — | R | SOURCE_ONLY | source_claim | — |
| holding | 1051 | / | / | register value | — | R | SOURCE_ONLY | source_claim | — |
| holding | 1052 | / | / | register value | — | R | SOURCE_ONLY | source_claim | — |
| holding | 1053 | / | / | register value | — | R | SOURCE_ONLY | source_claim | — |
| holding | 1054 | / | / | register value | — | R | SOURCE_ONLY | source_claim | — |
| holding | 1055 | Register 1055 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| holding | 1056 | Register 1056 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| holding | 1057 | Register 1057 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| holding | 1058 | Register 1058 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| holding | 1059 | Register 1059 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| holding | 1060 | BuckUpsFunE n | 0:disable 1:enable | register value | — | R | SOURCE_ONLY | source_claim | — |
| holding | 1061 | BuckUPSVoltS et | UPSoutputvoltage | register value | — | R | SOURCE_ONLY | source_claim | — |
| holding | 1062 | UPSFreqSet | UPSoutputfrequency | register value | — | R | SOURCE_ONLY | source_claim | — |
| holding | 1063 | Register 1063 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| holding | 1064 | Register 1064 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| holding | 1065 | Register 1065 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| holding | 1066 | Register 1066 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| holding | 1067 | Register 1067 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| holding | 1068 | Register 1068 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| holding | 1069 | Register 1069 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| holding | 1070 | Grid-first discharge limit | Discharge Power Rate whenGridFirst | register value | 1% | R/W | SOURCE_ONLY | source_claim | — |
| holding | 1071 | Grid-first stop SOC | Stop Discharge soc when GridFirst | register value | 1% | R/W | SOURCE_ONLY | source_claim | — |
| holding | 1072 | / | / | register value | / | R | SOURCE_ONLY | source_claim | — |
| holding | 1073 | / | / | register value | / | R | SOURCE_ONLY | source_claim | — |
| holding | 1074 | / | / | register value | / | R | SOURCE_ONLY | source_claim | — |
| holding | 1075 | / | / | register value | / | R | SOURCE_ONLY | source_claim | — |
| holding | 1076 | / | / | register value | / | R | SOURCE_ONLY | source_claim | — |
| holding | 1077 | / | / | register value | / | R | SOURCE_ONLY | source_claim | — |
| holding | 1078 | / | / | register value | / | R | SOURCE_ONLY | source_claim | — |
| holding | 1079 | / | / | register value | / | R | SOURCE_ONLY | source_claim | — |
| holding | 1080 | Grid-first slot 1 start | High byte = hour (0-23); low byte = minute (0-59). | register value | hh:mm | R/W | SOURCE_ONLY | source_claim | — |
| holding | 1081 | Grid-first slot 1 stop | High byte = hour (0-23); low byte = minute (0-59). | register value | hh:mm | R/W | SOURCE_ONLY | source_claim | — |
| holding | 1082 | Grid-first slot 1 enable | Enable:1 Disable:0 | register value | — | R/W | SOURCE_ONLY | source_claim | — |
| holding | 1083 | Grid-first slot 2 start | High byte = hour (0-23); low byte = minute (0-59). | register value | hh:mm | R/W | SOURCE_ONLY | source_claim | — |
| holding | 1084 | Grid-first slot 2 stop | High byte = hour (0-23); low byte = minute (0-59). | register value | hh:mm | R/W | SOURCE_ONLY | source_claim | — |
| holding | 1085 | Grid-first slot 2 enable | When set from the LCD, this slot can be tied to the Force Discharge command. | register value | — | R/W | SOURCE_ONLY | source_claim | — |
| holding | 1086 | Grid-first slot 3 start | High byte = hour (0-23); low byte = minute (0-59). | register value | hh:mm | R/W | SOURCE_ONLY | source_claim | — |
| holding | 1087 | Grid-first slot 3 stop | High byte = hour (0-23); low byte = minute (0-59). | register value | hh:mm | R/W | SOURCE_ONLY | source_claim | — |
| holding | 1088 | Grid-first slot 3 enable | Enable:1 Disable:0 | register value | — | R/W | SOURCE_ONLY | source_claim | — |
| holding | 1089 | / | / | register value | / | R | SOURCE_ONLY | source_claim | — |
| holding | 1090 | Battery-first charge limit | Charge Power Rate when BatFirst | register value | 1% | R/W | SOURCE_ONLY | source_claim | — |
| holding | 1091 | Battery-first stop SOC | Stop Charge soc when Bat First | register value | 1% | R/W | SOURCE_ONLY | source_claim | — |
| holding | 1092 | Battery-first AC charge enable | WhenBatFirst Enable:1 Disable:0 | register value | — | R/W | RESOLVED | semantic_correlated, source_claim | — |
| holding | 1093 | Register 1093 | — | register value | — | R | UNKNOWN_RESERVED | source_claim | — |
| holding | 1094 | Register 1094 | — | register value | — | R | UNKNOWN_RESERVED | source_claim | — |
| holding | 1095 | Register 1095 | — | register value | — | R | UNKNOWN_RESERVED | source_claim | — |
| holding | 1096 | Register 1096 | — | register value | — | R | UNKNOWN_RESERVED | source_claim | — |
| holding | 1097 | Register 1097 | — | register value | — | R | UNKNOWN_RESERVED | source_claim | — |
| holding | 1098 | Register 1098 | — | register value | — | R | UNKNOWN_RESERVED | source_claim | — |
| holding | 1099 | Register 1099 | — | register value | — | R | UNKNOWN_RESERVED | source_claim | — |
| holding | 1100 | Battery-first slot 1 start | High byte = hour (0-23); low byte = minute (0-59). | register value | hh:mm | R/W | SOURCE_ONLY | source_claim | — |
| holding | 1101 | Battery-first slot 1 stop | High byte = hour (0-23); low byte = minute (0-59). | register value | hh:mm | R/W | SOURCE_ONLY | source_claim | — |
| holding | 1102 | Battery-first slot 1 enable | Enable:1 Disable:0 | register value | — | R/W | SOURCE_ONLY | source_claim | — |
| holding | 1103 | Battery-first slot 2 start | High byte = hour (0-23); low byte = minute (0-59). | register value | hh:mm | R/W | SOURCE_ONLY | source_claim | — |
| holding | 1104 | Battery-first slot 2 stop | High byte = hour (0-23); low byte = minute (0-59). | register value | hh:mm | R/W | SOURCE_ONLY | source_claim | — |
| holding | 1105 | Battery-first slot 2 enable | Enable:1 Disable:0 | register value | — | R/W | SOURCE_ONLY | source_claim | — |
| holding | 1106 | Battery-first slot 3 start | High byte = hour (0-23); low byte = minute (0-59). | register value | hh:mm | R/W | SOURCE_ONLY | source_claim | — |
| holding | 1107 | Battery-first slot 3 stop | High byte = hour (0-23); low byte = minute (0-59). | register value | hh:mm | R/W | SOURCE_ONLY | source_claim | — |
| holding | 1108 | Battery-first slot 3 enable | Enable:1 Disable:0 | register value | — | R/W | SOURCE_ONLY | source_claim | — |
| holding | 1109 | / | reserve | register value | / | R | SOURCE_ONLY | source_claim | — |
| holding | 1110 | Load-first slot 1 start | SPA/reserve | register value | hh:mm | R/W | SOURCE_ONLY | source_claim | — |
| holding | 1111 | Load-first slot 1 stop | SPA/reserve | register value | hh:mm | R/W | SOURCE_ONLY | source_claim | — |
| holding | 1112 | Load-first slot 1 enable | SPA/reserve | register value | — | R/W | SOURCE_ONLY | source_claim | — |
| holding | 1113 | Load-first slot 2 start | SPA/reserve | register value | hh:mm | R/W | SOURCE_ONLY | source_claim | — |
| holding | 1114 | Load-first slot 2 stop | SPA/reserve | register value | hh:mm | R/W | SOURCE_ONLY | source_claim | — |
| holding | 1115 | Load-first slot 2 enable | SPA/reserve | register value | — | R/W | SOURCE_ONLY | source_claim | — |
| holding | 1116 | Load-first slot 3 start | SPA/reserve | register value | hh:mm | R/W | SOURCE_ONLY | source_claim | — |
| holding | 1117 | Load-first slot 3 stop | SPA/reserve | register value | hh:mm | R/W | SOURCE_ONLY | source_claim | — |
| holding | 1118 | Load-first slot 3 enable | SPA/reserve | register value | — | R/W | SOURCE_ONLY | source_claim | — |
| holding | 1119 | Energy calculation formula | 0：Theoldformula 1 ： The new formula | register value | / | R/W | SOURCE_ONLY | source_claim | — |
| holding | 1120 | Backup enable | MIXUS | register value | — | R/W | SOURCE_ONLY | source_claim | — |
| holding | 1121 | SGIP enable | MIXUS | register value | — | R/W | SOURCE_ONLY | source_claim | — |
| holding | 1122 | Register 1122 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| holding | 1123 | Register 1123 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| holding | 1124 | Register 1124 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| holding | 3000 | Export-limit fallback cap | Thepowerrate whenexportLimit failed | register value; /10 | 0.1% | R/W | SOURCE_ONLY | source_claim | — |
| holding | 3001 | Serial Number | Thenewmodel usesthefollowing registerstorecord theserialnumber; The representationis thesameasthe original:one registerholdstwo charactersandthe newserialnumber is30characters. | serial_number; /10 | ASCII | R/W | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| holding | 3002 | Serial Number | Serialnumber3-4 | register value | ASCII | R/W | SOURCE_ONLY | source_claim | — |
| holding | 3003 | Serial Number | Serialnumber5-6 | register value | ASCII | R/W | SOURCE_ONLY | source_claim | — |
| holding | 3004 | Serial Number | Serialnumber7-8 | register value | ASCII | R/W | SOURCE_ONLY | source_claim | — |
| holding | 3005 | Serial Number | Serialnumber9-10 | register value | ASCII | R/W | SOURCE_ONLY | source_claim | — |
| holding | 3006 | Serial Number | Serialnumber11-12 | register value | ASCII | R/W | SOURCE_ONLY | source_claim | — |
| holding | 3007 | Serial Number | Serialnumber13-14 | register value | ASCII | R/W | SOURCE_ONLY | source_claim | — |
| holding | 3008 | Serial Number | Serialnumber15-16 | register value | ASCII | R/W | SOURCE_ONLY | source_claim | — |
| holding | 3009 | Serial Number | Serialnumber17-18 | register value | ASCII | R/W | SOURCE_ONLY | source_claim | — |
| holding | 3010 | Serial Number | Serialnumber19-20 | register value | ASCII | R/W | SOURCE_ONLY | source_claim | — |
| holding | 3011 | Serial Number | Serialnumber21-22 | register value | ASCII | R/W | SOURCE_ONLY | source_claim | — |
| holding | 3012 | Serial Number | Serialnumber23-24 | register value | ASCII | R/W | SOURCE_ONLY | source_claim | — |
| holding | 3013 | Serial Number | Serialnumber25-26 | register value | ASCII | R/W | SOURCE_ONLY | source_claim | — |
| holding | 3014 | Serial Number | Serialnumber27-28 | register value | ASCII | R/W | SOURCE_ONLY | source_claim | — |
| holding | 3015 | Serial Number | Serialnumber29-30 | register value | ASCII | R/W | SOURCE_ONLY | source_claim | — |
| holding | 3016 | Dry-contact enable | DryContact functionenable | register value | — | R/W | SOURCE_ONLY | source_claim | — |
| holding | 3018 | Hybrid work mode | MIN2.5~6KTL-XH/ XADoubleCT special | register value | — | R/W | SOURCE_ONLY | source_claim | — |
| holding | 3021 | External off-grid enable | 0x00: Disable; （default） 0x01:Enable; | register value | — | R/W | SOURCE_ONLY | source_claim | — |
| holding | 3023 | Grid topology selection | MIN2.5~6KTL-XH/ XADoubleCT special | register value | — | R/W | SOURCE_ONLY | source_claim | — |
| holding | 3024 | Float-charge current limit | CCcurrent | register value; /10 | 0.1A | R/W | SOURCE_ONLY | source_claim | — |
| holding | 3028 | Battery charge stop voltage | Shouldstop chargewhen higherthanthis voltage | register value; /100 | 0.01V | R/W | SOURCE_ONLY | source_claim | — |
| holding | 3029 | Battery discharge start voltage | Shouldnot dischargewhen lowerthanthis voltage | register value; /100 | 0.01V | R/W | SOURCE_ONLY | source_claim | — |
| holding | 3030 | Battery constant-charge voltage | CVvoltage（acid） canchargewhen lowerthanthis voltage | register value; /100 | 0.01V | R/W | SOURCE_ONLY | source_claim | — |
| holding | 3031 | Discharge low temperature limit | 0-200:0-20℃ 1000-1400： -40-0℃ | register value; /10 | 0.1℃ | R/W | SOURCE_ONLY | source_claim | — |
| holding | 3032 | Discharge high temperature limit | Batterytemperatureupper limitfordischarge | register value; /10 | 0.1℃ | R/W | SOURCE_ONLY | source_claim | — |
| holding | 3033 | Charge low temperature limit | Battery temperaturelower limit 0-200:0-20℃ 1000-1400： -40-0℃ | register value; /10 | 0.1℃ | R/W | SOURCE_ONLY | source_claim | — |
| holding | 3034 | Charge high temperature limit | Battery temperature upperlimit | register value; /10 | 0.1℃ | R/W | SOURCE_ONLY | source_claim | — |
| holding | 3038 | Grid-first period 1 control | Bit0~7:minutes; Bit8~12:hour; Bit13~14, 0:loadpriority; 1:batterypriority; 2:Gridpriority; Bit15, 0:prohibited;1: enabled; | register value | — | R/W | SOURCE_ONLY | source_claim | — |
| holding | 3039 | Grid-first period 1 end | Bit0~7:minutes; Bit8~12:hour; Bit13~15:reserved | register value | — | R/W | UNKNOWN_RESERVED | source_claim | — |
| holding | 3041 | Register 3041 | Bit0~7:minutes; Bit8~12:hour; Bit13~15:reserved | register value; /10 | W | R/W | UNKNOWN_RESERVED | source_claim | — |
| holding | 3042 | Time3(xh) | WithTime1 | register value; /10 | W | R/W | SOURCE_ONLY | source_claim | — |
| holding | 3043 | Register 3043 | WithTime1 | register value; /10 | W | R/W | UNKNOWN_RESERVED | source_claim | — |
| holding | 3044 | Time4(xh) | WithTime1 | register value; /10 | W | R/W | SOURCE_ONLY | source_claim | — |
| holding | 3045 | Register 3045 | WithTime1 | register value; /10 | W | R/W | UNKNOWN_RESERVED | source_claim | — |
| holding | 3046 | Reserved | Reserved | register value; /10 | W | R | UNKNOWN_RESERVED | source_claim | — |
| holding | 3049 | AC Charge Enabled | Enable:1 Disable:0 | register value; /10 | — | R/W | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| holding | 3051 | Register 3051 | WithTime1 | register value; /10 | kWh | R/W | UNKNOWN_RESERVED | source_claim | — |
| holding | 3052 | Time6(xh) | WithTime1 | register value; /10 | kWh | R/W | SOURCE_ONLY | source_claim | — |
| holding | 3053 | Register 3053 | WithTime1 | register value; /10 | kWh | R/W | UNKNOWN_RESERVED | source_claim | — |
| holding | 3054 | Time7(xh) | WithTime1 | register value; /10 | kWh | R/W | SOURCE_ONLY | source_claim | — |
| holding | 3055 | Register 3055 | WithTime1 | register value; /10 | kWh | R/W | UNKNOWN_RESERVED | source_claim | — |
| holding | 3056 | Time8(xh) | WithTime1 | register value; /10 | kWh | R/W | SOURCE_ONLY | source_claim | — |
| holding | 3057 | Register 3057 | WithTime1 | register value; /10 | kWh | R/W | UNKNOWN_RESERVED | source_claim | — |
| holding | 3058 | Time9(xh) | WithTime1 | register value; /10 | kWh | R/W | SOURCE_ONLY | source_claim | — |
| holding | 3059 | Register 3059 | WithTime1 | register value; /10 | kWh | R/W | UNKNOWN_RESERVED | source_claim | — |
| holding | 3060 | Reserved | Reserved | register value; /10 | kWh | R | UNKNOWN_RESERVED | source_claim | — |
| holding | 3061 | Reserved | Reserved | register value; /10 | kWh | R | UNKNOWN_RESERVED | source_claim | — |
| holding | 3062 | Reserved | Reserved | register value; /10 | kWh | R | UNKNOWN_RESERVED | source_claim | — |
| holding | 3063 | Reserved | Reserved | register value; /10 | kWh | R | UNKNOWN_RESERVED | source_claim | — |
| holding | 3064 | Reserved | Reserved | register value; /10 | kWh | R | UNKNOWN_RESERVED | source_claim | — |
| holding | 3065 | Reserved | Reserved | register value; /10 | kWh | R | UNKNOWN_RESERVED | source_claim | — |
| holding | 3066 | Reserved | Reserved | register value; /10 | kWh | R | UNKNOWN_RESERVED | source_claim | — |
| holding | 3067 | Reserved | Reserved | register value; /10 | kWh | R | UNKNOWN_RESERVED | source_claim | — |
| holding | 3068 | Reserved | Reserved | register value; /10 | kWh | R | UNKNOWN_RESERVED | source_claim | — |
| holding | 3069 | Reserved | Reserved | register value; /10 | kWh | R | UNKNOWN_RESERVED | source_claim | — |
| holding | 3070 | BatteryType | Batterytype 0:Lithium 1:Lead-acid 2:other | register value; /10 | kWh | R/W | SOURCE_ONLY | source_claim | — |
| holding | 3071 | BatMdlSeria/ ParalNum | BatMdlSeria/Paral Num; SPH4-11Kused Theupper8bits indicatethe numberofseries segments； Thelower8bits indicatethe numberofparallel sections; | register value; /10 | kWh | R/W | SOURCE_ONLY | source_claim | — |
| holding | 3072 | Reserved | Reserved | register value; /10 | kWh | R | UNKNOWN_RESERVED | source_claim | — |
| holding | 3073 | Reserved | Reserved | register value; /10 | kWh | R | UNKNOWN_RESERVED | source_claim | — |
| holding | 3074 | Reserved | Reserved | register value; /10 | kWh | R | UNKNOWN_RESERVED | source_claim | — |
| holding | 3075 | Reserved | Reserved | register value; /10 | kWh | R | UNKNOWN_RESERVED | source_claim | — |
| holding | 3076 | Reserved | Reserved | register value; /10 | kWh | R | UNKNOWN_RESERVED | source_claim | — |
| holding | 3077 | Reserved | Reserved | register value; /10 | kWh | R | UNKNOWN_RESERVED | source_claim | — |
| holding | 3078 | Reserved | Reserved | register value; /10 | kWh | R | UNKNOWN_RESERVED | source_claim | — |
| holding | 3079 | UpsFunEn | 0:disable 1:enable | register value | bool | R/W | SOURCE_ONLY | source_claim | — |
| holding | 3080 | UPSVoltSet | 0:230V 1:208V 2:240V | register value | V | R/W | SOURCE_ONLY | source_claim | — |
| holding | 3081 | UPSFreqSet | 0:50Hz 1:60Hz | register value | Hz | R/W | SOURCE_ONLY | source_claim | — |
| holding | 3082 | bLoadFirstSto pSocSet | ratio | register value; /1 | % | R/W | SOURCE_ONLY | source_claim | — |
| holding | 3083 | Reserved | Reserved | register value; /10 | kWh | R | UNKNOWN_RESERVED | source_claim | — |
| holding | 3084 | Reserved | Reserved | register value; /10 | kWh | R | UNKNOWN_RESERVED | source_claim | — |
| holding | 3087 | Battery rack serial | Forbattery | register value | ASCII | R/W | SOURCE_ONLY | source_claim | — |
| holding | 3088 | Battery rack serial | SerialNumber3-4 | register value | ASCII | R/W | SOURCE_ONLY | source_claim | — |
| holding | 3089 | Battery rack serial | SerialNumber5-6 | register value | ASCII | R/W | SOURCE_ONLY | source_claim | — |
| holding | 3090 | Battery rack serial | SerialNumber7-8 | register value | ASCII | R/W | SOURCE_ONLY | source_claim | — |
| holding | 3091 | Battery rack serial | SerialNumber9-10 | register value | ASCII | R/W | SOURCE_ONLY | source_claim | — |
| holding | 3092 | Battery rack serial | SerialNumber11-12 | register value | ASCII | R/W | SOURCE_ONLY | source_claim | — |
| holding | 3093 | Battery rack serial | SerialNumber13-14 | register value | ASCII | R/W | SOURCE_ONLY | source_claim | — |
| holding | 3094 | Battery rack serial | SerialNumber15-16 | register value | ASCII | R/W | SOURCE_ONLY | source_claim | — |
| holding | 3095 | BDC reset command | 0：Invaliddata 1：Resetsetting parameters 2：Resetcorrection parameter 3：Clearhistorical power | register value | — | R/W | SOURCE_ONLY | source_claim | — |
| holding | 3096 | BDC monitoring code | ZEBA | register value | ASCII | R | SOURCE_ONLY | source_claim | — |
| holding | 3097 | BDC monitoring code | Four-character identifier for the BDC monitoring firmware (e.g. ZEBA). | register value | ASCII | R | SOURCE_ONLY | source_claim | — |
| holding | 3099 | DSP firmware code | DSPsoftwarecode | register value | ASCII | R | SOURCE_ONLY | source_claim | — |
| holding | 3100 | DSP firmware code | Identifier for the inverter DSP firmware build. | register value | ASCII | R | SOURCE_ONLY | source_claim | — |
| holding | 3101 | DSP firmware version | DSPSoftwareVersion | register value | ASCII | R | SOURCE_ONLY | source_claim | — |
| holding | 3103 | BDC monitor firmware | BDCmonitoringsoftware version | register value | ASCII | R | SOURCE_ONLY | source_claim | — |
| holding | 3104 | BMS MCU hardware version | BMS hardware version information | register value | ASCII | R | SOURCE_ONLY | source_claim | — |
| holding | 3105 | BMS firmware version | BMSsoftwareversion information | register value | ASCII | R | SOURCE_ONLY | source_claim | — |
| holding | 3106 | BMS manufacturer | BMSManufacturerName | register value | ASCII | R | SOURCE_ONLY | source_claim | — |
| holding | 3107 | BMS communication interface | BMSCommunicati oninterfacetype： 0:RS485; 1:CAN; | register value | — | R | SOURCE_ONLY | source_claim | — |
| holding | 3108 | BDC module identifier 4 | SxxBxx | register value | ASCII | R/W | SOURCE_ONLY | source_claim | — |
| holding | 3109 | BDC module identifier 3 | DxxTxx | register value | ASCII | R/W | SOURCE_ONLY | source_claim | — |
| holding | 3110 | BDC module identifier 2 | PxxUxx | register value | ASCII | R/W | SOURCE_ONLY | source_claim | — |
| holding | 3111 | BDC module identifier 1 | Mxxxx | register value | ASCII | R/W | SOURCE_ONLY | source_claim | — |
| holding | 3113 | BDC protocol version | Bit8-bit15The majorversion numberranges from0-256.In principle,itcannot bechanged Bit0-bit7Minor versionnumber [0-256].Ifthe protocolis changed,youneed toupdatethis version No. | register value | — | R | SOURCE_ONLY | source_claim | — |
| holding | 3118 | BDC on/off state | Indicates whether the battery DC converter is currently running (1) or idle (0). | register value | — | R | SOURCE_ONLY | source_claim | — |
| holding | 3121 | Self-use power | Not yet surfaced by the Home Assistant integration. | register value; /10 | W | R | SOURCE_ONLY | source_claim | — |
| holding | 3122 | Self-use power | Not yet surfaced by the Home Assistant integration. | register value; /10 | W | R | SOURCE_ONLY | source_claim | — |
| holding | 3123 | System energy today | Available in firmware but not yet exposed as an integration attribute. | register value; /10 | kWh | R | SOURCE_ONLY | source_claim | — |
| holding | 3124 | System energy today | Available in firmware but not yet exposed as an integration attribute. | register value; /10 | kWh | R | SOURCE_ONLY | source_claim | — |
| input | 0 | Inverter status | InverterStatus | register value; /10 | — | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 1 | PV input power | PpvH | register value; /10 | 0.1W | R/W | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 2 | PV input power | PpvL | register value; /10 | 0.1W | R/W | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3 | PV1 DC voltage | Vpv1 | register value; /10 | 0.1V | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 4 | PV1 DC current | PV1Curr | register value; /10 | 0.1A | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 5 | PV1 DC power | Ppv1H | register value; /10 | 0.1W | R/W | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 6 | PV1 DC power | Ppv1L | register value; /10 | 0.1W | R/W | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 7 | PV2 DC voltage | Vpv2 | register value; /10 | 0.1V | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 8 | PV2 DC current | PV2Curr | register value; /10 | 0.1A | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 9 | PV2 DC power | Ppv2H | register value; /10 | 0.1W | R/W | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 10 | PV2 DC power | Ppv2L | register value; /10 | 0.1W | R/W | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 11 | PV3 DC voltage | Vpv3 | register value; /10 | 0.1V | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 12 | PV3 DC current | PV3Curr | register value; /10 | 0.1A | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 13 | PV3 DC power | Ppv3H | register value; /10 | 0.1W | R/W | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 14 | PV3 DC power | Ppv3L | register value; /10 | 0.1W | R/W | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 15 | PV4 DC voltage | Vpv4 | register value; /10 | 0.1V | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 16 | PV4 DC current | PV4Curr | register value; /10 | 0.1A | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 17 | PV4 DC power | Ppv4H | register value; /10 | 0.1W | R/W | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 18 | PV4 DC power | Ppv4L | register value; /10 | 0.1W | R/W | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 19 | PV5 DC voltage | Vpv5 | register value; /10 | 0.1V | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 20 | PV5 DC current | PV5Curr | register value; /10 | 0.1A | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 21 | PV5 DC power | Ppv5H | register value; /10 | 0.1W | R/W | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 22 | PV5 DC power | Ppv5L | register value; /10 | 0.1W | R/W | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 23 | PV6 DC voltage | Vpv6 | register value; /10 | 0.1V | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 24 | PV6 DC current | PV6Curr | register value; /10 | 0.1A | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 25 | PV6 DC power | PV6inputpower(high) | register value; /10 | W | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 26 | PV6 DC power | PV6inputpower(low) | register value; /10 | W | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 27 | PV7 DC voltage | PV7voltage | register value; /10 | V | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 28 | PV7 DC current | PV7inputcurrent | register value; /10 | A | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 29 | PV7 DC power | PV7inputpower(high) | register value; /10 | W | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 30 | PV7 DC power | PV7inputpower(low) | register value; /10 | W | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 31 | PV8 DC voltage | PV8voltage | register value; /10 | V | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 32 | PV8 DC current | PV8inputcurrent | register value; /10 | A | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 33 | PV8 DC power | PV8inputpower(high) | register value; /10 | W | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 34 | PV8 DC power | PV8inputpower(low) | register value; /10 | W | R | RESOLVED | semantic_correlated, source_claim | — |
| input | 35 | AC output power | Outputpower(high) | register value; /10 | W | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 36 | AC output power | Outputpower(low) | register value; /10 | W | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 37 | Grid frequency | Gridfrequency | register value; /100 | Hz | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 38 | AC phase L1 voltage | Three/singlephasegridvoltage | register value; /10 | V | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 39 | AC phase L1 current | Three/singlephasegridoutputcurrent | register value; /10 | A | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 40 | AC phase L1 power | Three/single phase grid output watt VA(high) | register value; /10 | W | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 41 | AC phase L1 power | Three/single phase grid output watt VA(low) | register value; /10 | W | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 42 | AC phase L2 voltage | Threephasegridvoltage | register value; /10 | V | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 43 | AC phase L2 current | Threephasegridoutputcurrent | register value; /10 | A | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 44 | AC phase L2 power | Threephasegridoutputpower(high) | register value; /10 | W | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 45 | AC phase L2 power | Threephasegridoutputpower(low) | register value; /10 | W | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 46 | AC phase L3 voltage | Threephasegridvoltage | register value; /10 | V | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 47 | AC phase L3 current | Threephasegridoutputcurrent | register value; /10 | A | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 48 | AC phase L3 power | Threephasegridoutputpower(high) | register value; /10 | W | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 49 | AC phase L3 power | Threephasegridoutputpower(low) | register value; /10 | W | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 50 | Vac_RS | Threephasegridvoltage | register value | Linevoltage | R | RESOLVED | semantic_correlated, source_claim | — |
| input | 51 | Vac_ST | Threephasegridvoltage | register value | Linevoltage | R | RESOLVED | semantic_correlated, source_claim | — |
| input | 52 | Vac_TR | Threephasegridvoltage | register value | Linevoltage | R | RESOLVED | semantic_correlated, source_claim | — |
| input | 53 | Output energy today | Todaygenerateenergy(high) | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 54 | Output energy today | Todaygenerateenergy(low) | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 55 | Output energy total | Totalgenerateenergy(high) | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 56 | Output energy total | Totalgenerateenergy(low) | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 57 | Run time | Raw counter counts seconds; divide by 7200 to obtain hours. | register value; /7200 | h | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 58 | Run time | Raw counter counts seconds; divide by 7200 to obtain hours. | register value; /7200 | h | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 59 | PV1 energy today | PV1Energytoday(high) | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 60 | PV1 energy today | PV1Energytoday(low) | register value; /10 | kWh | R | RESOLVED | semantic_correlated, source_claim | — |
| input | 61 | PV1 energy total | PV1Energytotal(high) | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 62 | PV1 energy total | PV1Energytotal(low) | register value; /10 | kWh | R | RESOLVED | semantic_correlated, source_claim | — |
| input | 63 | PV2 energy today | PV2Energytoday(high) | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 64 | PV2 energy today | PV2Energytoday(low) | register value; /10 | kWh | R | RESOLVED | semantic_correlated, source_claim | — |
| input | 65 | PV2 energy total | PV2Energytotal(high) | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 66 | PV2 energy total | PV2Energytotal(low) | register value; /10 | kWh | R | RESOLVED | semantic_correlated, source_claim | — |
| input | 67 | PV3 energy today | PV3Energytoday(high) | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 68 | PV3 energy today | PV3Energytoday(low) | register value; /10 | kWh | R | RESOLVED | semantic_correlated, source_claim | — |
| input | 69 | PV3 energy total | PV3Energytotal(high) | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 70 | PV3 energy total | PV3Energytotal(low) | register value; /10 | kWh | R | RESOLVED | semantic_correlated, source_claim | — |
| input | 71 | PV4 energy today | PV4Energytoday(high) | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 72 | PV4 energy today | PV4Energytoday(low) | register value; /10 | kWh | R | RESOLVED | semantic_correlated, source_claim | — |
| input | 73 | PV4 energy total | PV4Energytotal(high) | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 74 | PV4 energy total | PV4Energytotal(low) | register value; /10 | kWh | R | RESOLVED | semantic_correlated, source_claim | — |
| input | 75 | PV5 energy today | PV5Energytoday(high) | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 76 | PV5 energy today | PV5Energytoday(low) | register value; /10 | kWh | R | RESOLVED | semantic_correlated, source_claim | — |
| input | 77 | PV5 energy total | PV5Energytotal(high) | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 78 | PV5 energy total | PV5Energytotal(low) | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 79 | PV6 energy today | PV6Energytoday(high) | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 80 | PV6 energy today | PV6Energytoday(low) | register value; /10 | kWh | R | RESOLVED | semantic_correlated, source_claim | — |
| input | 81 | PV6 energy total | PV6Energytotal(high) | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 82 | PV6 energy total | PV6Energytotal(low) | register value; /10 | kWh | R | RESOLVED | semantic_correlated, source_claim | — |
| input | 83 | PV7 energy today | PV7Energytoday(high) | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 84 | PV7 energy today | PV7Energytoday(low) | register value; /10 | kWh | R | RESOLVED | semantic_correlated, source_claim | — |
| input | 85 | PV7 energy total | PV7Energytotal(high) | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 86 | PV7 energy total | PV7Energytotal(low) | register value; /10 | kWh | R | RESOLVED | semantic_correlated, source_claim | — |
| input | 87 | PV8 energy today | PV8Energytoday(high) | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 88 | PV8 energy today | PV8Energytoday(low) | register value; /10 | kWh | R | RESOLVED | semantic_correlated, source_claim | — |
| input | 89 | PV8 energy total | PV8Energytotal(high) | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 90 | PV8 energy total | PV8Energytotal(low) | register value; /10 | kWh | R | RESOLVED | semantic_correlated, source_claim | — |
| input | 91 | PV energy total | PVEnergytotal(high) | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 92 | PV energy total | PVEnergytotal(low) | register value; /10 | kWh | R | RESOLVED | semantic_correlated, source_claim | — |
| input | 93 | Inverter temperature | Invertertemperature | register value; /10 | °C | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 94 | IPM temperature | TheinsideIPMininverterTemperature | register value; /10 | °C | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 95 | Boost temperature | Boosttemperature | register value; /10 | °C | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 96 | Temp4 | Temp4 | register value | reserved | R | SOURCE_ONLY | source_claim | — |
| input | 97 | uwBatVolt_DSP | BatVolt_DSP | register value | BatVolt(DSP) | R | SOURCE_ONLY | source_claim | — |
| input | 98 | P-bus voltage | PBusinsideVoltage | register value; /10 | V | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 99 | N-bus voltage | NBusinsideVoltage | register value; /10 | V | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 100 | IPF | InverteroutputPFnow | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 101 | Output power percentage | RealOutputpowerPercent | register value; /10 | % | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 102 | OPFullwattH | OutputMaxpowerLimitedhigh | register value | W | R | RESOLVED | semantic_correlated, source_claim | — |
| input | 103 | OPFullwattL | OutputMaxpowerLimitedlow | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 104 | Derating mode | DeratingMode | register value; /10 | — | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 105 | Fault code | Inverterfaultmaincode | register value; /10 | — | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 106 | Register 106 | — | register value | — | R | UNKNOWN_RESERVED | source_claim | — |
| input | 107 | FaultSubcode | Inverterfaultsubcode | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 108 | RemoteCtrlEn | / | register value | StoragePow er(SPA) | R | SOURCE_ONLY | source_claim | — |
| input | 109 | RemoteCtrlPow er | / | register value | StoragePow er(SPA) | R | SOURCE_ONLY | source_claim | — |
| input | 110 | Warning code | WarningbitH | register value; /10 | — | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 111 | Warning code | Inverterwarnsubcode | register value; /10 | — | R | SOURCE_ONLY | source_claim | — |
| input | 112 | WarnMaincode | Inverterwarnmaincode | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 113 | real Power Percent | realPowerPercent | register value | MAX | R | SOURCE_ONLY | source_claim | — |
| input | 114 | inv start delay time | invstartdelaytime | register value | MAX | R | SOURCE_ONLY | source_claim | — |
| input | 115 | bINVAllFaultCod e | bINVAllFaultCode | register value | MAX | R | SOURCE_ONLY | source_claim | — |
| input | 116 | AC charge Power_H | Gridpowertolocalload | register value | Storage Power | R | SOURCE_ONLY | source_claim | — |
| input | 117 | AC charge Power_L | Gridpowertolocalload | register value | Storage Power | R | SOURCE_ONLY | source_claim | — |
| input | 118 | Priority | 0:LoadFirst | register value | Storage | R | RESOLVED | semantic_correlated, source_claim | — |
| input | 119 | BatteryType | 0：Lead-acid 1：Lithiumbattery | register value | — | R | RESOLVED | semantic_correlated, source_claim | — |
| input | 120 | AutoProofreadC MD | Aging mode Auto-calibration command | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 121 | Register 121 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| input | 122 | Register 122 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| input | 123 | Register 123 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| input | 124 | reserved | reserved | register value | — | R | UNKNOWN_RESERVED | source_claim | — |
| input | 1000 | uwSysWorkMode | uwSysWorkMode | register value | — | W | SOURCE_ONLY | source_claim | — |
| input | 1001 | Systemfaultword0 | Systemfaultword0 | register value | Please refer to thefault description of Hybrid | R | SOURCE_ONLY | source_claim | — |
| input | 1002 | Systemfaultword1 | Systemfaultword1 | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 1003 | Systemfaultword2 | Systemfaultword2 | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 1004 | Systemfaultword3 | Systemfaultword3 | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 1005 | Systemfaultword4 | Systemfaultword4 | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 1006 | Systemfaultword5 | Systemfaultword5 | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 1007 | Systemfaultword6 | Systemfaultword6 | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 1008 | Systemfaultword7 | Systemfaultword7 | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 1009 | Pdischarge1H | Dischargepower(high) | register value; /10 | W | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 1010 | Pdischarge1L | Dischargepower(low) | register value; /10 | W | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 1011 | Pcharge1H | Chargepower(high) | register value; /10 | W | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 1012 | Pcharge1L | Chargepower(low) | register value; /10 | W | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 1013 | Vbat | Batteryvoltage | register value | V | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 1014 | SOC | StateofchargeCapacity | register value; /10 | lith/leadacid | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 1015 | PactouserR H | ACpowertouserH | register value | W | R | RESOLVED | semantic_correlated, source_claim | — |
| input | 1016 | PactouserR L | ACpowertouserL | register value | W | R | RESOLVED | semantic_correlated, source_claim | — |
| input | 1017 | PactouserS H | PactouserS H | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 1018 | PactouserS L | PactouserS L | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 1019 | PactouserT H | PactouserT H | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 1020 | PactouserT L | PactouserT H | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 1021 | PactouserTotalH | ACpowertousertotalH | register value; /10 | W | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 1022 | PactouserTotalL | ACpowertousertotalL | register value; /10 | W | R | RESOLVED | semantic_correlated, source_claim | — |
| input | 1023 | PactogridR H | ACpowertogridH | register value | Ac output | R | RESOLVED | semantic_correlated, source_claim | — |
| input | 1024 | PactogridR L | ACpowertogridL | register value | W | R | RESOLVED | semantic_correlated, source_claim | — |
| input | 1025 | PactogridS H | PactogridS H | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 1026 | PactogridS L | PactogridS L | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 1027 | PactogridTH | 0.1w | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 1028 | PactogridTL | 0.1w | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 1029 | pac_to_grid_total | 0.1w | register value; /10 | W | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 1030 | PactogridtotalL | 0.1w | register value; /10 | W | R | RESOLVED | semantic_correlated, source_claim | — |
| input | 1031 | PLocalLoadR H | 0.1w | register value | W | R | RESOLVED | semantic_correlated, source_claim | — |
| input | 1032 | PLocalLoadR L | 0.1w | register value | W | R | RESOLVED | semantic_correlated, source_claim | — |
| input | 1033 | PLocalLoadS H | 0.1w | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 1034 | PLocalLoadS L | 0.1w | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 1035 | PLocalLoadT H | 0.1w | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 1036 | PLocalLoadT L | 0.1w | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 1037 | PLocalLoadtotalH | 0.1w | register value | W | R | RESOLVED | semantic_correlated, source_claim | — |
| input | 1038 | PLocalLoadtotalL | 0.1w | register value | W | R | RESOLVED | semantic_correlated, source_claim | — |
| input | 1039 | IP2MTemperature | 0.1℃ | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 1040 | B2attery Temperature | 0.1℃ | register value | °C | R | RESOLVED | semantic_correlated, source_claim | — |
| input | 1041 | SPDSPStatus | SPDSPStatus | register value | — | R | RESOLVED | semantic_correlated, source_claim | — |
| input | 1042 | SPBusVolt | 0.1V | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 1043 | Register 1043 | — | register value | — | R | UNKNOWN_RESERVED | source_claim | — |
| input | 1044 | Etouser_todayH | Etouser_todayH | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 1045 | Etouser_todayL | Etouser_todayL | register value; /10 | kWh | W | RESOLVED | semantic_correlated, source_claim | — |
| input | 1046 | Etouser_totalH | Etouser_totalH | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 1047 | Etouser_totalL | Etouser_totalL | register value; /10 | kWh | R | RESOLVED | semantic_correlated, source_claim | — |
| input | 1048 | Etogrid_todayH | Etogrid_todayH | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 1049 | Etogrid_todayL | Etogrid_todayL | register value; /10 | kWh | W | RESOLVED | semantic_correlated, source_claim | — |
| input | 1050 | Etogrid_totalH | Etogrid_totalH | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 1051 | Etogrid_totalL | Etogrid_totalL | register value; /10 | kWh | R | RESOLVED | semantic_correlated, source_claim | — |
| input | 1052 | Edischarge1_toda yH | Edischarge1_toda yH | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 1053 | Edischarge1_toda yL | Edischarge1_toda yL | register value; /10 | kWh | R | RESOLVED | semantic_correlated, source_claim | — |
| input | 1054 | Edischarge1_total H | Edischarge1_total H | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 1055 | Edischarge1_total L | Edischarge1_total L | register value; /10 | kWh | W | RESOLVED | semantic_correlated, source_claim | — |
| input | 1056 | Echarge1_todayH | Echarge1_todayH | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 1057 | Echarge1_today L | Echarge1_today L | register value; /10 | kWh | R | RESOLVED | semantic_correlated, source_claim | — |
| input | 1058 | Echarge1_totalH | Echarge1_totalH | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 1059 | Echarge1_totalL | Echarge1_totalL | register value; /10 | kWh | R | RESOLVED | semantic_correlated, source_claim | — |
| input | 1060 | Register 1060 | Localloadenergytoday | register value | kWh | R | UNKNOWN_RESERVED | semantic_correlated, source_claim | — |
| input | 1061 | Register 1061 | Localloadenergytoday | register value | kWh | R | UNKNOWN_RESERVED | semantic_correlated, source_claim | — |
| input | 1062 | Register 1062 | Localloadenergytotal | register value | kWh | R | UNKNOWN_RESERVED | semantic_correlated, source_claim | — |
| input | 1063 | Register 1063 | Localloadenergytotal | register value | kWh | R | UNKNOWN_RESERVED | semantic_correlated, source_claim | — |
| input | 1064 | Register 1064 | ExportLimitApparentPowerH | register value | — | W | UNKNOWN_RESERVED | source_claim | — |
| input | 1065 | Register 1065 | ExportLimitApparentPowerL | register value | — | W | UNKNOWN_RESERVED | source_claim | — |
| input | 1066 | Register 1066 | / | register value | — | R | UNKNOWN_RESERVED | source_claim | — |
| input | 1067 | EpsFac | UPSfrequency | register value | — | R | RESOLVED | semantic_correlated, source_claim | — |
| input | 1068 | EpsVac1 | UPSphaseRoutputvoltage | register value | — | R | RESOLVED | semantic_correlated, source_claim | — |
| input | 1069 | EpsIac1 | UPSphaseRoutputcurrent | register value | — | R | RESOLVED | semantic_correlated, source_claim | — |
| input | 1070 | EpsPac1 | UPSphaseRoutputpower(H) | register value | — | R | RESOLVED | semantic_correlated, source_claim | — |
| input | 1071 | EpsPac1 | UPSphaseRoutputpower(L) | register value | — | R | RESOLVED | semantic_correlated, source_claim | — |
| input | 1072 | EpsVac2 | UPSphaseSoutputvoltage | register value | — | R | RESOLVED | semantic_correlated, source_claim | — |
| input | 1073 | EpsIac2 | UPSphaseSoutputcurrent | register value | — | R | RESOLVED | semantic_correlated, source_claim | — |
| input | 1074 | EpsPac2 | UPSphaseSoutputpower(H) | register value | — | R | RESOLVED | semantic_correlated, source_claim | — |
| input | 1075 | EpsPac2 | UPSphaseSoutputpower(L) | register value | — | R | RESOLVED | semantic_correlated, source_claim | — |
| input | 1076 | EpsVac3 | UPSphaseToutputvoltage | register value | — | R | RESOLVED | semantic_correlated, source_claim | — |
| input | 1077 | EpsIac3 | UPSphaseToutputcurrent | register value | — | R | RESOLVED | semantic_correlated, source_claim | — |
| input | 1078 | EpsPac3 | UPSphaseToutputpower(H) | register value | — | R | RESOLVED | semantic_correlated, source_claim | — |
| input | 1079 | EpsPac3 | UPSphaseToutputpower(L) | register value | — | R | RESOLVED | semantic_correlated, source_claim | — |
| input | 1080 | EpsLoadPercent | LoadpercentofUPSouput | register value | — | R | RESOLVED | semantic_correlated, source_claim | — |
| input | 1081 | EpsPF | Powerfactor | register value | — | R | RESOLVED | semantic_correlated, source_claim | — |
| input | 1082 | Register 1082 | StatusOldfromBMS | register value | — | R | UNKNOWN_RESERVED | source_claim | — |
| input | 1083 | Register 1083 | StatusfromBMS | register value | — | R | UNKNOWN_RESERVED | source_claim | — |
| input | 1084 | Register 1084 | ErrorinfoOldfromBMS | register value | — | R | UNKNOWN_RESERVED | source_claim | — |
| input | 1085 | Register 1085 | ErrorinfomationfromBMS | register value | — | R | UNKNOWN_RESERVED | source_claim | — |
| input | 1086 | Register 1086 | SOCfromBMS | register value | — | R | UNKNOWN_RESERVED | source_claim | — |
| input | 1087 | Register 1087 | BatteryvoltagefromBMS | register value | — | R | UNKNOWN_RESERVED | source_claim | — |
| input | 1088 | Register 1088 | BatterycurrentfromBMS | register value | — | R | UNKNOWN_RESERVED | source_claim | — |
| input | 1089 | Register 1089 | BatterytemperaturefromBMS | register value | — | R | UNKNOWN_RESERVED | source_claim | — |
| input | 1090 | BMS_MaxCurr | Max. charge/discharge current fromBMS(pylon) | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 1091 | BMS_GaugeRM | GaugeRMfromBMS | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 1092 | BMS_GaugeFCC | GaugeFCCfromBMS | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 1093 | BMS_FW | BMS_FW | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 1094 | BMS_DeltaVolt | DeltaVfromBMS | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 1095 | BMS_CycleCnt | CycleCountfromBMS | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 1096 | BMS_SOH | SOHfromBMS | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 1097 | BMS_ConstantV olt | CVvoltagefromBMS | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 1098 | BMS_WarnInfoO ld | WarninginfooldfromBMS | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 1099 | BMS_WarnInfo | WarninginfofromBMS | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 1100 | BMS_GaugeICCu rr | GaugeICcurrentfromBMS | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 1101 | BMS_MCUVersi on | MCUSoftwareversionfromBMS | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 1102 | BMS_GaugeVers ion | GaugeVersionfromBMS | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 1103 | BMS_wGaugeFR Version_L | GaugeFRVersionL16fromBMS | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 1104 | BMS_wGaugeFR Version_H | GaugeFRVersionH16fromBMS | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 1105 | BMS_BMSInfo | BMSInformationfromBMS | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 1106 | BMS_PackInfo | PackInformationfromBMS | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 1107 | BMS_UsingCap | UsingCapfromBMS | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 1108 | uwMaxCellVolt | Maximumsinglebatteryvoltage | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 1109 | uwMinCellVolt | Lowestsinglebatteryvoltage | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 1110 | bModuleNum | Batteryparallelnumber | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 1111 | Numberofbatteries | Numberofbatteries | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 1112 | uwMaxVoltCellN o | MaxVoltCellNo | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 1113 | uwMinVoltCellN o | MinVoltCellNo | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 1114 | uwMaxTemprCe ll_10T | MaxTemprCell_10T | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 1115 | uwMinTemprCel l_10T | MinTemprCell_10T | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 1116 | uwMaxTemprCe llNo | MaxVoltTemprCellNo | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 1117 | uwMinTemprCel | MinVoltTemprCellNo | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 1118 | ProtectpackID | FaultyBatteryAddress | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 1119 | MaxSOC | ParallelmaximumSOC | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 1120 | MinSOC | ParallelminimumSOC | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 1121 | BMS_Error2 | BatteryProtection2 | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 1122 | BMS_Error3 | BatteryProtection3 | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 1123 | BMS_WarnInfo2 | BatteryWarn2 | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 1124 | ACCharge EnergyTodayH | ACChargeEnergytoday | register value | kWh | W | RESOLVED | semantic_correlated, source_claim | — |
| input | 3041 | Load supply power | Totalforwardpower | register value; /10 | Total forward power | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3042 | Load supply power | Real-time active power delivered to on-site (self-consumption) loads. | register value; /10 | W | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3043 | Grid export power | Totalreversepower | register value; /10 | Totalreverse power | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3044 | Grid export power | Active power exported to the utility grid. | register value; /10 | W | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3045 | Home load power | Totalloadpower | register value; /10 | Total load power | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3046 | Home load power | Aggregate instantaneous demand from on-site loads. | register value; /10 | W | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3067 | Load energy today | Todayenergytouser | register value; /10 | Todayenergy touser | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3068 | Load energy today | Energy delivered to on-site loads today (0.1 kWh resolution). | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3069 | Load energy total | Totalenergytouser | register value; /10 | Totalenergy touser | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3070 | Load energy total | Lifetime energy delivered to on-site loads (0.1 kWh resolution). | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3071 | Export energy today | Todayenergytogrid | register value; /10 | Todayenergy togrid | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3072 | Export energy today | Energy exported to the grid today (0.1 kWh resolution). | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3073 | Export energy total | Totalenergytogrid | register value; /10 | Totalenergy togrid | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3074 | Export energy total | Lifetime energy exported to the grid (0.1 kWh resolution). | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3097 | Communication board temperature | Commmunicationbroadtemperature | register value; /10 | °C | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3111 | Warning code | PresentFFTValue[CHANNEL_A] | register value; /1 | — | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3115 | Inverter start delay | invstartdelaytime | register value; /1 | invstartdelay time | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3125 | Battery discharge today | Todaydischargeenergy | register value; /10 | Today discharge energy | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3126 | Battery discharge today | Energy discharged from the battery into the AC system today (0.1 kWh resolution). | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3127 | Battery discharge total | Totaldischargeenergy | register value; /10 | Total discharge energy | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3128 | Battery discharge total | Total energy discharged from the battery (0.1 kWh resolution). | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3129 | Battery charge today | Chargeenergytoday | register value; /10 | Charge energytoday | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3130 | Battery charge today | Energy charged into the battery today (0.1 kWh resolution). | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3131 | Battery charge total | Chargeenergytotal | register value; /10 | Charge energytotal | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3132 | Battery charge total | Total energy charged into the battery (0.1 kWh resolution). | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3164 | BDC presence flag | WhethertoparseBDCdataseparately | register value; /1 | 0:Don'tneed 1：need | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3169 | Battery voltage | Batteryvoltage | register value; /100 | V | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3170 | Battery current | Batterycurrent | register value; /10 | A | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3171 | Battery SOC | StateofchargeCapacity | register value; /1 | % | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3172 | VBUS1 voltage | TotalBUSvoltage | register value; /10 | V | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3173 | VBUS2 voltage | OntheBUSvoltage | register value; /10 | V | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3174 | Buck/boost current | BUCK-BOOSTCurrent | register value; /10 | A | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3175 | LLC stage current | LLCCurrent | register value; /10 | A | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3176 | Battery temperature A | TempertureA | register value; /10 | °C | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3177 | Battery temperature B | TempertureB | register value; /10 | °C | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3178 | Battery discharge power | Dischargepower | register value; /10 | W | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3179 | Battery discharge power | Real-time discharge power flowing from the battery (0.1 W resolution). | register value; /10 | W | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3180 | Battery charge power | Chargepower | register value; /10 | W | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3181 | Battery charge power | Real-time charge power flowing into the battery (0.1 W resolution). | register value; /10 | W | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3189 | BMS max cell index | BmsMaxVoltCellNo | register value; /1 | — | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3190 | BMS min cell index | BmsMinVoltCellNo | register value; /1 | — | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3191 | BMS average temperature A | BmsBatteryAvgTemp | register value; /1 | °C | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3192 | BMS max cell temperature A | BmsMaxCellTemp | register value; /10 | °C | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3193 | BMS average temperature B | BmsBatteryAvgTemp | register value; /10 | °C | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3194 | BMS max cell temperature B | BmsMaxCellTemp | register value; /1 | °C | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3195 | BMS average temperature C | BmsBatteryAvgTemp | register value; /1 | °C | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3196 | BMS max SOC | BmsMaxSOC | register value; /1 | % | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3197 | BMS min SOC | BmsMinSOC | register value; /1 | % | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3198 | Parallel battery count | ParallelBatteryNum | register value; /1 | — | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3199 | BMS derate reason | BmsDerateReason | register value; /1 | — | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3200 | BMS full charge capacity | BmsGaugeFCC（Ah） | register value; /1 | Ah | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3201 | BMS remaining capacity | BmsGaugeRM（Ah） | register value; /1 | Ah | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3202 | BMS protect flags 1 | BMSProtect1 | register value; /1 | — | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3203 | BMS warning flags 1 | BMSWarn1 | register value; /1 | — | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3204 | BMS fault flags 1 | BMSFault1 | register value; /1 | — | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3205 | BMS fault flags 2 | BMSFault2 | register value; /1 | — | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3210 | Battery insulation status | BatteryISOdetectionstatus | register value; /1 | 0：Not detected 1：Detection completed | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3211 | Battery request flags | batteryworkrequest | register value; /1 | — | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3212 | BMS status | batteryworkingstatus | register value; /1 | 0:dormancy 1:Charge 2:Discharge 3:free 4:standby 5:Softstart 6:fault 7:update | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3213 | BMS protect flags 2 | BMSProtect2 | register value; /1 | — | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3214 | BMS warning flags 2 | BMSWarn2 | register value; /1 | — | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3215 | BMS SOC | BMSSOC | register value; /1 | % | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3216 | BMS battery voltage | BMSBatteryVolt | register value; /100 | V | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3217 | BMS battery current | Positive values indicate discharge from the battery; negative values indicate charging. | register value; /100 | A | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3218 | BMS max cell temperature | batterycellmaximumtemperature | register value; /10 | °C | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3219 | BMS max charge current | Maximumchargingcurrent | register value; /100 | A | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3220 | BMS max discharge current | Maximumdischargecurrent | register value; /100 | A | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3221 | BMS cycle count | BMSCycleCnt | register value; /1 | — | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3222 | BMS state of health | BMSSOH | register value; /1 | % | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3223 | BMS charge voltage limit | Batterychargingvoltagelimitvalue | register value; /100 | V | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3224 | BMS discharge voltage limit | Batterydischargevoltagelimitvalue | register value; /1 | V | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3225 | BMS warning flags 3 | BMSWarn3 | register value; /1 | — | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3226 | BMS protect flags 3 | BMSProtect3 | register value; /1 | — | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3230 | BMS max cell voltage | BMSBatterySingleVoltMax | register value; /1 | V | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3231 | BMS min cell voltage | BMSBatterySingleVoltMin | register value; /1 | V | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |

### SPA storage

Storage family applicability comes from the graph/catalogue ranges.

| Table | Address | Name | Description | Encoding / scale | Unit | Access | Status | Evidence | Notes |
|---|---:|---|---|---|---|---|---|---|---|
| holding | 0 | Inverter Enabled | Theinvertercanbeswitched onandoff,andtheBDCcanbe switchedonandoffforthe battreadyfunction. | register value; /10 | — | R/W | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| holding | 1 | Safety function enable flags | SPI: system protection interface Bit0~3:forCEI0-21 Bit4~6:forSAA | register value | — | W | SOURCE_ONLY | source_claim | — |
| holding | 2 | Persist power-factor commands | Means these settings will be acting or not when next poweron | register value | — | W | RESOLVED | semantic_correlated, source_claim | — |
| holding | 3 | Active power limit setpoint | 255:powerisnotbelimited | register value; /1 | % | W | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| holding | 4 | Reactive power limit setpoint | 255:powerisnotbelimited | register value; /1 | % | W | SOURCE_ONLY | source_claim | — |
| holding | 5 | Power factor target | Inverter output power factor’s10000times | register value; /10000 | pf | W | SOURCE_ONLY | source_claim | — |
| holding | 6 | Rated apparent power | Normal power(high) | register value; /10 | 0.1VA | R | SOURCE_ONLY | source_claim | — |
| holding | 7 | Rated apparent power | Normal power(low) | register value; /10 | 0.1VA | R | SOURCE_ONLY | source_claim | — |
| holding | 8 | Nominal PV voltage | NormalworkPV voltage | register value; /10 | 0.1V | R | SOURCE_ONLY | source_claim | — |
| holding | 9 | Firmware | Firmwareversion (high) | firmware_version; /10 | ASCII | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| holding | 10 | Firmware | Firmwareversion (middle) | register value | ASCII | R | SOURCE_ONLY | source_claim | — |
| holding | 11 | Firmware | Firmwareversion(low) | register value | ASCII | R | SOURCE_ONLY | source_claim | — |
| holding | 12 | Firmware | ControlFirmware version(high) | register value | ASCII | R | SOURCE_ONLY | source_claim | — |
| holding | 13 | Firmware | ControlFirmware version(middle) | register value | ASCII | R | SOURCE_ONLY | source_claim | — |
| holding | 14 | Firmware | ControlFirmware version(low) | register value | ASCII | R | SOURCE_ONLY | source_claim | — |
| holding | 15 | LCD language selection | 0:Italian; 1:English; 2:German; 3:Spanish; 4:French; 5:Chinese; 6：Polish 7：Portugues 8：Hungary | register value | — | W | SOURCE_ONLY | source_claim | — |
| holding | 16 | Country profile configured | CountrySelectedor not | register value | — | W | SOURCE_ONLY | source_claim | — |
| holding | 17 | PV start voltage threshold | Inputstartvoltage | register value; /10 | 0.1V | W | SOURCE_ONLY | source_claim | — |
| holding | 18 | Start-up delay | Starttime | register value; /1 | 1s | W | SOURCE_ONLY | source_claim | — |
| holding | 19 | Restart delay | RestartDelayTime afterfaultback; | register value; /1 | 1s | W | SOURCE_ONLY | source_claim | — |
| holding | 20 | Active power ramp rate (startup) | Powerstartslope | register value; /10 | 0.1% | W | SOURCE_ONLY | source_claim | — |
| holding | 21 | Active power ramp rate (restart) | Powerrestartslope | register value; /10 | 0.1% | W | SOURCE_ONLY | source_claim | — |
| holding | 22 | Modbus RTU baud rate | Select communicationbaudrat e 0:9600bps 1:38400bps | register value | — | W | SOURCE_ONLY | source_claim | — |
| holding | 23 | Serial Number | The Home Assistant integration exposes this as the device serial number and reuses it as the unique identifier. | serial_number; /10 | ASCII | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| holding | 24 | Serial Number | The Home Assistant integration exposes this as the device serial number and reuses it as the unique identifier. | register value | ASCII | R | SOURCE_ONLY | source_claim | — |
| holding | 25 | Serial Number | The Home Assistant integration exposes this as the device serial number and reuses it as the unique identifier. | register value | ASCII | R | SOURCE_ONLY | source_claim | — |
| holding | 26 | Serial Number | The Home Assistant integration exposes this as the device serial number and reuses it as the unique identifier. | register value | ASCII | R | SOURCE_ONLY | source_claim | — |
| holding | 27 | Serial Number | The Home Assistant integration exposes this as the device serial number and reuses it as the unique identifier. | register value | ASCII | R | SOURCE_ONLY | source_claim | — |
| holding | 28 | Inverter Model | Home Assistant renders this value as the string A# B# D# T# P# U# M# S# via the integration's model() helper. Vendor spec lists value pattern `&*5`; digits appear to be stored without the leading letter codes, so treat as encoded tokens until verified on hardware. | register value; /10 | — | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| holding | 29 | Inverter Model | Home Assistant renders this value as the string A# B# D# T# P# U# M# S# via the integration's model() helper. Vendor spec lists value pattern `&*5`; digits appear to be stored without the leading letter codes, so treat as encoded tokens until verified on hardware. | register value | — | R | SOURCE_ONLY | source_claim | — |
| holding | 30 | Modbus slave address | Communicate address | register value | — | W | SOURCE_ONLY | source_claim | — |
| holding | 31 | Firmware update trigger | Updatefirmware | register value | — | W | SOURCE_ONLY | source_claim | — |
| holding | 32 | Reset user configuration | Use with caution; the inverter immediately reboots and loses provisioning data. | register value | — | W | SOURCE_ONLY | source_claim | — |
| holding | 33 | Factory reset | Equivalent to the front-panel factory reset. Requires re-commissioning afterwards. | register value | — | W | SOURCE_ONLY | source_claim | — |
| holding | 34 | Manufacturer information string | The original table lists these words as Manufacturer Info 8-1 (high/middle/low); combine them to read the full string. | register value | ASCII | R | SOURCE_ONLY | source_claim | — |
| holding | 35 | Manufacturer information string | The original table lists these words as Manufacturer Info 8-1 (high/middle/low); combine them to read the full string. | register value | ASCII | R | SOURCE_ONLY | source_claim | — |
| holding | 36 | Manufacturer information string | The original table lists these words as Manufacturer Info 8-1 (high/middle/low); combine them to read the full string. | register value | ASCII | R | SOURCE_ONLY | source_claim | — |
| holding | 37 | Manufacturer information string | The original table lists these words as Manufacturer Info 8-1 (high/middle/low); combine them to read the full string. | register value | ASCII | R | SOURCE_ONLY | source_claim | — |
| holding | 38 | Manufacturer information string | The original table lists these words as Manufacturer Info 8-1 (high/middle/low); combine them to read the full string. | register value | ASCII | R | SOURCE_ONLY | source_claim | — |
| holding | 39 | Manufacturer information string | The original table lists these words as Manufacturer Info 8-1 (high/middle/low); combine them to read the full string. | register value | ASCII | R | SOURCE_ONLY | source_claim | — |
| holding | 40 | Manufacturer information string | The original table lists these words as Manufacturer Info 8-1 (high/middle/low); combine them to read the full string. | register value | ASCII | R | SOURCE_ONLY | source_claim | — |
| holding | 41 | Manufacturer information string | The original table lists these words as Manufacturer Info 8-1 (high/middle/low); combine them to read the full string. | register value | ASCII | R | SOURCE_ONLY | source_claim | — |
| holding | 42 | G100 failsafe enable | EnglishG100failsafeset | register value | — | W | SOURCE_ONLY | source_claim | — |
| holding | 43 | Device Type Code | Vendor spec provides value pattern `&*6`; handle as encoded type/family digits with implied prefixes pending confirmation. | register value; /10 | — | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| holding | 44 | Number Of Trackers And Phases | Inputtrackernumand outputphasenum | register value; /10 | — | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| holding | 45 | System clock year | Localtime | register value | — | W | SOURCE_ONLY | source_claim | — |
| holding | 46 | System clock month | Systemtime-Month | register value | — | W | SOURCE_ONLY | source_claim | — |
| holding | 47 | System clock day | Systemtime-Day | register value | — | W | SOURCE_ONLY | source_claim | — |
| holding | 48 | System clock hour | Systemtime-Hour | register value | — | W | SOURCE_ONLY | source_claim | — |
| holding | 49 | System clock minute | Systemtime-Min | register value | — | W | SOURCE_ONLY | source_claim | — |
| holding | 50 | System clock second | Systemtime-Second | register value | — | W | SOURCE_ONLY | source_claim | — |
| holding | 51 | System clock weekday | SystemWeekly | register value | — | W | SOURCE_ONLY | source_claim | — |
| holding | 52 | Stage 1 undervoltage limit | Gridvoltagelowlimit protect | register value | 0.1V | W | SOURCE_ONLY | source_claim | — |
| holding | 53 | Stage 1 overvoltage limit | Gridvoltagehighlimit protect | register value | 0.1V | W | SOURCE_ONLY | source_claim | — |
| holding | 54 | Stage 1 underfrequency limit | Gridfrequencylow limitprotect | register value | 0.01 Hz | W | SOURCE_ONLY | source_claim | — |
| holding | 55 | Stage 1 overfrequency limit | Gridhigh frequencylimitprotect | register value | 0.01 Hz | W | SOURCE_ONLY | source_claim | — |
| holding | 56 | Stage 2 undervoltage limit | Gridvoltagelowlimit protect2 | register value | 0.1V | W | SOURCE_ONLY | source_claim | — |
| holding | 57 | Stage 2 overvoltage limit | Gridvoltagehighlimit protect2 | register value | 0.1V | W | SOURCE_ONLY | source_claim | — |
| holding | 58 | Stage 2 underfrequency limit | Gridfrequencylow limitprotect2 | register value | 0.01 Hz | W | SOURCE_ONLY | source_claim | — |
| holding | 59 | Stage 2 overfrequency limit | Gridhighfrequency limitprotect2 | register value | 0.01 Hz | W | SOURCE_ONLY | source_claim | — |
| holding | 60 | Stage 3 undervoltage limit | Grid voltage low limit protect3 | register value | 0.1V | W | SOURCE_ONLY | source_claim | — |
| holding | 61 | Stage 3 overvoltage limit | Grid voltage high limit protect3 | register value | 0.1V | W | SOURCE_ONLY | source_claim | — |
| holding | 62 | Stage 3 underfrequency limit | Grid frequency low limitprotect3 | register value | 0.01Hz | W | SOURCE_ONLY | source_claim | — |
| holding | 63 | Stage 3 overfrequency limit | Grid frequency high limitprotect3 | register value | 0.01Hz | W | SOURCE_ONLY | source_claim | — |
| holding | 64 | Reconnect undervoltage limit | Gridlowvoltagelimit connecttoGrid | register value | 0.1V | W | SOURCE_ONLY | source_claim | — |
| holding | 65 | Reconnect overvoltage limit | Gridhighvoltagelimit connecttoGrid | register value | 0.1V | W | SOURCE_ONLY | source_claim | — |
| holding | 66 | Reconnect underfrequency limit | Gridlowfrequency | register value | 0.01 | W | SOURCE_ONLY | source_claim | — |
| holding | 67 | Reconnect overfrequency limit | Gridhighfrequency limitconnecttoGrid | register value | 0.01 Hz | W | SOURCE_ONLY | source_claim | — |
| holding | 68 | Stage 1 undervoltage trip delay | Grid voltage low limit protecttime 1 | register value | Cycle | W | SOURCE_ONLY | source_claim | — |
| holding | 69 | Stage 1 overvoltage trip delay | Grid voltage high limit protecttime 1 | register value | Cycle | W | SOURCE_ONLY | source_claim | — |
| holding | 70 | Stage 2 undervoltage trip delay | Grid voltage low limit protecttime 2 | register value | Cycle | W | SOURCE_ONLY | source_claim | — |
| holding | 71 | Stage 2 overvoltage trip delay | Grid voltage high limit protecttime 2 | register value | Cycle | W | SOURCE_ONLY | source_claim | — |
| holding | 72 | Stage 1 underfrequency trip delay | Grid frequency low limitprotecttime 1 | register value | Cycle | W | SOURCE_ONLY | source_claim | — |
| holding | 73 | Modbus Version | Grid frequency high limitprotecttime 1 | register value | Cycle | W | SOURCE_ONLY | source_claim | — |
| holding | 74 | Stage 2 underfrequency trip delay | Grid frequency low limitprotecttime 2 | register value | Cycle | W | SOURCE_ONLY | source_claim | — |
| holding | 75 | Stage 2 overfrequency trip delay | Grid frequency high limitprotecttime 2 | register value | Cycle | W | SOURCE_ONLY | source_claim | — |
| holding | 76 | Stage 3 undervoltage trip delay | Grid voltage low limit protecttime 3 | register value | Cycle | W | SOURCE_ONLY | source_claim | — |
| holding | 77 | Stage 3 overvoltage trip delay | Grid voltage high limit protecttime 3 | register value | Cycle | W | SOURCE_ONLY | source_claim | — |
| holding | 78 | Stage 3 underfrequency trip delay | Grid frequency low limitprotecttime 3 | register value | Cycle | W | SOURCE_ONLY | source_claim | — |
| holding | 79 | Stage 3 overfrequency trip delay | Grid frequency high limitprotecttime 3 | register value | Cycle | W | SOURCE_ONLY | source_claim | — |
| holding | 80 | Ten-minute overvoltage limit | Voltprotectionfor10 min | register value | 0.1V | W | SOURCE_ONLY | source_claim | — |
| holding | 81 | PV input high-voltage fault | PVVoltageHigh Fault | register value | 0.1V | W | SOURCE_ONLY | source_claim | — |
| holding | 82 | Controller firmware build string | Positions: 0-1 model letters, 2-3 model variant, 4-5 DSP1 build, 6-7 DSP2/M0 build, 8-9 CPLD/AFCI build, 10-11 M3 build. | register value | ASCII | R | SOURCE_ONLY | source_claim | — |
| holding | 83 | Controller firmware build string | Positions: 0-1 model letters, 2-3 model variant, 4-5 DSP1 build, 6-7 DSP2/M0 build, 8-9 CPLD/AFCI build, 10-11 M3 build. | register value | ASCII | R | SOURCE_ONLY | source_claim | — |
| holding | 84 | Controller firmware build string | Positions: 0-1 model letters, 2-3 model variant, 4-5 DSP1 build, 6-7 DSP2/M0 build, 8-9 CPLD/AFCI build, 10-11 M3 build. | register value | ASCII | R | SOURCE_ONLY | source_claim | — |
| holding | 85 | Controller firmware build string | Positions: 0-1 model letters, 2-3 model variant, 4-5 DSP1 build, 6-7 DSP2/M0 build, 8-9 CPLD/AFCI build, 10-11 M3 build. | register value | ASCII | R | SOURCE_ONLY | source_claim | — |
| holding | 86 | Controller firmware build string | Positions: 0-1 model letters, 2-3 model variant, 4-5 DSP1 build, 6-7 DSP2/M0 build, 8-9 CPLD/AFCI build, 10-11 M3 build. | register value | ASCII | R | SOURCE_ONLY | source_claim | — |
| holding | 87 | Controller firmware build string | Positions: 0-1 model letters, 2-3 model variant, 4-5 DSP1 build, 6-7 DSP2/M0 build, 8-9 CPLD/AFCI build, 10-11 M3 build. | register value | ASCII | R | SOURCE_ONLY | source_claim | — |
| holding | 88 | Modbus Version | ModbusVersion | register value; /100 | Int(16 bits) | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| holding | 89 | Power-factor control mode | 0=Unity PF, 1=Fixed PF setpoint, 2=Default PF line, 3=User-defined PF line, 4=Under-excited reactive power, 5=Over-excited reactive power, 6=Q(V) curve, 7=Direct control, 8=Static capacitive QV, 9=Static inductive QV. | register value | — | W | SOURCE_ONLY | source_claim | — |
| holding | 90 | GPRS modem IP/status flags | Bit 0-3: 0=idle, 1=IP read requested, 2=set IP succeeded; Bit 4-7: 0=unknown, 1=modem OK, 2=no SIM, 3=no network, 4=TCP connect fail, 5=TCP connected, etc. | register value | — | W | UNKNOWN_RESERVED | source_claim | — |
| holding | 91 | Frequency derating start | Frequencyderating startpoint | register value | 0.01H Z | W | SOURCE_ONLY | source_claim | — |
| holding | 92 | Frequency derating slope | Frequency–loadlimit rate | register value | 10tim es | W | SOURCE_ONLY | source_claim | — |
| holding | 93 | CEI 0-21 Q(V) point V1S | CEI021V1SQ(v) | register value | 0.1V | W | SOURCE_ONLY | source_claim | — |
| holding | 94 | CEI 0-21 Q(V) point V2S | CEI021V2SQ(v) | register value | 0.1V | W | SOURCE_ONLY | source_claim | — |
| holding | 95 | CEI 0-21 Q(V) point V1L | CEI021V1LQ(v) | register value | 0.1V | W | SOURCE_ONLY | source_claim | — |
| holding | 96 | CEI 0-21 Q(V) point V2L | CEI021V2LQ(v) | register value | 0.1V | W | SOURCE_ONLY | source_claim | — |
| holding | 97 | Q(V) lock-in active power | Q(v)lockinactive powerofCEI021 | register value | Percen t | W | SOURCE_ONLY | source_claim | — |
| holding | 98 | Q(V) lock-out active power | Q(v)lockOutactive powerofCEI021 | register value | Percen t | W | SOURCE_ONLY | source_claim | — |
| holding | 99 | Power-factor curve lock-in voltage | Lockingirdvoltof CEI021PFline | register value | 0.1V | W | SOURCE_ONLY | source_claim | — |
| holding | 100 | Power-factor curve lock-out voltage | Lockoutgirdvoltof CEI021PFline | register value | 0.1V | W | SOURCE_ONLY | source_claim | — |
| holding | 101 | Power-factor adjust value 1 | PFadjustvalue1 | register value | — | W | SOURCE_ONLY | source_claim | — |
| holding | 102 | Power-factor adjust value 2 | PFadjustvalue2 | register value | — | W | SOURCE_ONLY | source_claim | — |
| holding | 103 | Power-factor adjust value 3 | PFadjustvalue3 | register value | — | W | SOURCE_ONLY | source_claim | — |
| holding | 104 | Power-factor adjust value 4 | PFadjustvalue4 | register value | — | W | SOURCE_ONLY | source_claim | — |
| holding | 105 | Power-factor adjust value 5 | PFadjustvalue5 | register value | — | W | SOURCE_ONLY | source_claim | — |
| holding | 106 | Power-factor adjust value 6 | PFadjustvalue6 | register value | — | W | SOURCE_ONLY | source_claim | — |
| holding | 107 | Q(V) response delay | QV Reactive Power delaytime | register value | 1S | W | SOURCE_ONLY | source_claim | — |
| holding | 108 | Over-frequency derating delay | Overfrequency derati ngdelaytime | register value | 50ms | W | SOURCE_ONLY | source_claim | — |
| holding | 109 | Maximum reactive power magnitude | QmaxforQ(V)curve | register value | 0.1% | W | SOURCE_ONLY | source_claim | — |
| holding | 110 | PF curve point 1 load | 255meansnothispoint | register value | percen t | W | SOURCE_ONLY | source_claim | — |
| holding | 111 | PF curve point 1 target | PFlimitlinepoint1 powerfactor | register value | — | W | SOURCE_ONLY | source_claim | — |
| holding | 112 | PF curve point 2 load | 255meansnothispoint | register value | percen t | W | SOURCE_ONLY | source_claim | — |
| holding | 113 | PF curve point 2 target | PFlimitlinepoint 2powerfactor | register value | — | W | SOURCE_ONLY | source_claim | — |
| holding | 114 | PF curve point 3 load | 255meansnothispoint | register value | percen t | W | SOURCE_ONLY | source_claim | — |
| holding | 115 | PF curve point 3 target | PFlimitlinepoint3 powerfactor | register value | — | W | SOURCE_ONLY | source_claim | — |
| holding | 116 | PF curve point 4 load | 255meansnothispoint | register value | percen t | W | SOURCE_ONLY | source_claim | — |
| holding | 117 | PF curve point 4 target | PFlimitlinepoint4 powerfactor | register value | — | W | SOURCE_ONLY | source_claim | — |
| holding | 118 | Module code segments | SxxBxx | register value | — | R | SOURCE_ONLY | source_claim | — |
| holding | 119 | Module code segments | DxxTxx | register value | — | R | SOURCE_ONLY | source_claim | — |
| holding | 120 | Module code segments | PxxUxx | register value | — | R | SOURCE_ONLY | source_claim | — |
| holding | 121 | Module code segments | Mxxxx Power | register value | — | R | SOURCE_ONLY | source_claim | — |
| holding | 122 | Export limit enable mode | ExportLimitenable, 0:DisableexportLimit; 1:Enable485exportLimit; 2:Enable232exportLimit; 3:EnableCTexportLimit; | register value | — | R/W | SOURCE_ONLY | source_claim | — |
| holding | 123 | Export limit power setpoint | ExportLimitPowerRate | register value | 0.1% | R/W | SOURCE_ONLY | source_claim | — |
| holding | 124 | Tracker coupling mode | 0:Independent 1:DCSource 2:Parallel | register value | — | W | SOURCE_ONLY | source_claim | — |
| holding | 1000 | Float charge current limit i | Float charge current limit i | register value | — | W | SOURCE_ONLY | source_claim | — |
| holding | 1001 | PF CMD memory state | PF CMD memory state | register value | 0or1, | W | SOURCE_ONLY | source_claim | — |
| holding | 1002 | VbatStartF orDischarg e | VbatStartF orDischarg e | register value | — | R | SOURCE_ONLY | source_claim | — |
| holding | 1003 | VbatlowWa rnClr l | VbatlowWa rnClr l | register value | — | R | SOURCE_ONLY | source_claim | — |
| holding | 1004 | Vbatstopfo rdischarge | Vbatstopfo rdischarge | register value | — | W | SOURCE_ONLY | source_claim | — |
| holding | 1005 | Vbat stop forcharge | Shouldstopcharge whenhigherthanthis voltage | register value | 0.01V | W | SOURCE_ONLY | source_claim | — |
| holding | 1006 | Vbat start for discharge | Should not discharge when lower than this voltage | register value | 0.01V | W | SOURCE_ONLY | source_claim | — |
| holding | 1007 | Vbat constant charge | CVvoltage（acid） | register value | 0.01V | W | SOURCE_ONLY | source_claim | — |
| holding | 1008 | EESysInfo.S ysSetEn | SystemEnable | register value | — | W | SOURCE_ONLY | source_claim | — |
| holding | 1009 | Battemp lower limit d | Batterytemperature lowerlimitfordischarge | register value | 0.1℃ | W | SOURCE_ONLY | source_claim | — |
| holding | 1010 | Bat temp upper limit d | Batterytemperature upperlimitfordischarge | register value | 0.1℃ | W | SOURCE_ONLY | source_claim | — |
| holding | 1011 | Bat temp lower limit c | Lowertemperaturelimit | register value | 0.1℃ | W | SOURCE_ONLY | source_claim | — |
| holding | 1012 | Bat temp upper limit c | Uppertemperaturelimit | register value | 0.1℃ | W | SOURCE_ONLY | source_claim | — |
| holding | 1013 | uwUnderFr eDischarge DelyTime | UnderFreDelayTime | register value | 50ms | R | SOURCE_ONLY | source_claim | — |
| holding | 1014 | BatMdlSeri alNum | SPH4-11Kused | register value | — | W | SOURCE_ONLY | source_claim | — |
| holding | 1015 | BatMdlPara llNum | SPH4-11Kused | register value | — | W | SOURCE_ONLY | source_claim | — |
| holding | 1016 | DRMS_EN | 0：disable 1：enable | register value | / | R | SOURCE_ONLY | source_claim | — |
| holding | 1017 | Bat First Start Time 4 | Higheight:hours Loweight:minutes | register value | — | R | SOURCE_ONLY | source_claim | — |
| holding | 1018 | Bat First Stop Time 4 | Higheight:hours Loweight:minutes | register value | — | R | SOURCE_ONLY | source_claim | — |
| holding | 1019 | BatFirst on/off Switch4 | Batterypriorityenable1 | register value | — | R | SOURCE_ONLY | source_claim | — |
| holding | 1020 | Bat First Start Time 5 | Higheight:hours Loweight:minutes | register value | — | R | SOURCE_ONLY | source_claim | — |
| holding | 1021 | BatFirst StopTime 5 | Higheight:hours Loweight:minutes | register value | — | R | SOURCE_ONLY | source_claim | — |
| holding | 1022 | BatFirst on/off Switch5 | Batterypriorityenable1 | register value | — | R | SOURCE_ONLY | source_claim | — |
| holding | 1023 | BatFirst StartTime 6 | Higheight:hours Loweight:minutes | register value | — | R | SOURCE_ONLY | source_claim | — |
| holding | 1024 | BatFirst StopTime 6 | Higheight:hours Loweight:minutes | register value | — | R | SOURCE_ONLY | source_claim | — |
| holding | 1025 | BatFirst on/off Switch6 | Batterypriorityenable1 | register value | — | R | SOURCE_ONLY | source_claim | — |
| holding | 1026 | GridFirst StartTime | Higheight:hours Loweight:minutes | register value | — | R | SOURCE_ONLY | source_claim | — |
| holding | 1027 | GridFirst StopTime 4 | Higheight:hours Loweight:minutes | register value | — | R | SOURCE_ONLY | source_claim | — |
| holding | 1028 | Grid First Stop Switch4 | Gridpriorityenable | register value | — | R | SOURCE_ONLY | source_claim | — |
| holding | 1029 | GridFirst StartTime 5 | Higheight:hours Loweight:minutes | register value | — | R | SOURCE_ONLY | source_claim | — |
| holding | 1030 | GridFirst StopTime 5 | Higheight:hours Loweight:minutes | register value | — | R | SOURCE_ONLY | source_claim | — |
| holding | 1031 | Grid First Stop Switch5 | Gridpriorityenable | register value | — | R | SOURCE_ONLY | source_claim | — |
| holding | 1032 | GridFirst StartTime 6 | Higheight:hours Loweight:minutes | register value | — | R | SOURCE_ONLY | source_claim | — |
| holding | 1033 | GridFirst StopTime 6 | Higheight:hours Loweight:minutes | register value | — | R | SOURCE_ONLY | source_claim | — |
| holding | 1034 | Grid First Stop Switch6 | Gridpriorityenable | register value | — | R | SOURCE_ONLY | source_claim | — |
| holding | 1035 | BatFirst StartTime 4 | Higheight:hours Loweight:minutes | register value | — | R | SOURCE_ONLY | source_claim | — |
| holding | 1036 | / | Reserve | register value | / | R | SOURCE_ONLY | source_claim | — |
| holding | 1037 | bCTMode | UsetheCTModeto ChooseRFCT\Cable CT\METER | register value | — | W | SOURCE_ONLY | source_claim | — |
| holding | 1038 | CTAdjust | CTAdjustenable | register value | — | W | SOURCE_ONLY | source_claim | — |
| holding | 1039 | / | Reserve | register value | / | R | SOURCE_ONLY | source_claim | — |
| holding | 1040 | / | / | register value | — | R | SOURCE_ONLY | source_claim | — |
| holding | 1041 | / | / | register value | — | R | SOURCE_ONLY | source_claim | — |
| holding | 1042 | / | / | register value | — | R | SOURCE_ONLY | source_claim | — |
| holding | 1043 | / | / | register value | — | R | SOURCE_ONLY | source_claim | — |
| holding | 1044 | Priority | ForceChrEn/ForceDischr En Load first/bat first /grid first | register value | — | R | SOURCE_ONLY | source_claim | — |
| holding | 1045 | / | / | register value | — | R | SOURCE_ONLY | source_claim | — |
| holding | 1046 | / | / | register value | — | R | SOURCE_ONLY | source_claim | — |
| holding | 1047 | AgingTestSt ep Cmd | Commandforagingtest | register value | — | R | SOURCE_ONLY | source_claim | — |
| holding | 1048 | BatteryTyp e | Batterytypechooseof buck-boostinput | register value | — | R | SOURCE_ONLY | source_claim | — |
| holding | 1049 | / | / | register value | — | R | SOURCE_ONLY | source_claim | — |
| holding | 1050 | / | / | register value | — | R | SOURCE_ONLY | source_claim | — |
| holding | 1051 | / | / | register value | — | R | SOURCE_ONLY | source_claim | — |
| holding | 1052 | / | / | register value | — | R | SOURCE_ONLY | source_claim | — |
| holding | 1053 | / | / | register value | — | R | SOURCE_ONLY | source_claim | — |
| holding | 1054 | / | / | register value | — | R | SOURCE_ONLY | source_claim | — |
| holding | 1055 | Register 1055 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| holding | 1056 | Register 1056 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| holding | 1057 | Register 1057 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| holding | 1058 | Register 1058 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| holding | 1059 | Register 1059 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| holding | 1060 | BuckUpsFunE n | 0:disable 1:enable | register value | — | R | SOURCE_ONLY | source_claim | — |
| holding | 1061 | BuckUPSVoltS et | UPSoutputvoltage | register value | — | R | SOURCE_ONLY | source_claim | — |
| holding | 1062 | UPSFreqSet | UPSoutputfrequency | register value | — | R | SOURCE_ONLY | source_claim | — |
| holding | 1063 | Register 1063 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| holding | 1064 | Register 1064 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| holding | 1065 | Register 1065 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| holding | 1066 | Register 1066 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| holding | 1067 | Register 1067 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| holding | 1068 | Register 1068 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| holding | 1069 | Register 1069 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| holding | 1070 | Grid-first discharge limit | Discharge Power Rate whenGridFirst | register value | 1% | R/W | SOURCE_ONLY | source_claim | — |
| holding | 1071 | Grid-first stop SOC | Stop Discharge soc when GridFirst | register value | 1% | R/W | SOURCE_ONLY | source_claim | — |
| holding | 1072 | / | / | register value | / | R | SOURCE_ONLY | source_claim | — |
| holding | 1073 | / | / | register value | / | R | SOURCE_ONLY | source_claim | — |
| holding | 1074 | / | / | register value | / | R | SOURCE_ONLY | source_claim | — |
| holding | 1075 | / | / | register value | / | R | SOURCE_ONLY | source_claim | — |
| holding | 1076 | / | / | register value | / | R | SOURCE_ONLY | source_claim | — |
| holding | 1077 | / | / | register value | / | R | SOURCE_ONLY | source_claim | — |
| holding | 1078 | / | / | register value | / | R | SOURCE_ONLY | source_claim | — |
| holding | 1079 | / | / | register value | / | R | SOURCE_ONLY | source_claim | — |
| holding | 1080 | Grid-first slot 1 start | High byte = hour (0-23); low byte = minute (0-59). | register value | hh:mm | R/W | SOURCE_ONLY | source_claim | — |
| holding | 1081 | Grid-first slot 1 stop | High byte = hour (0-23); low byte = minute (0-59). | register value | hh:mm | R/W | SOURCE_ONLY | source_claim | — |
| holding | 1082 | Grid-first slot 1 enable | Enable:1 Disable:0 | register value | — | R/W | SOURCE_ONLY | source_claim | — |
| holding | 1083 | Grid-first slot 2 start | High byte = hour (0-23); low byte = minute (0-59). | register value | hh:mm | R/W | SOURCE_ONLY | source_claim | — |
| holding | 1084 | Grid-first slot 2 stop | High byte = hour (0-23); low byte = minute (0-59). | register value | hh:mm | R/W | SOURCE_ONLY | source_claim | — |
| holding | 1085 | Grid-first slot 2 enable | When set from the LCD, this slot can be tied to the Force Discharge command. | register value | — | R/W | SOURCE_ONLY | source_claim | — |
| holding | 1086 | Grid-first slot 3 start | High byte = hour (0-23); low byte = minute (0-59). | register value | hh:mm | R/W | SOURCE_ONLY | source_claim | — |
| holding | 1087 | Grid-first slot 3 stop | High byte = hour (0-23); low byte = minute (0-59). | register value | hh:mm | R/W | SOURCE_ONLY | source_claim | — |
| holding | 1088 | Grid-first slot 3 enable | Enable:1 Disable:0 | register value | — | R/W | SOURCE_ONLY | source_claim | — |
| holding | 1089 | / | / | register value | / | R | SOURCE_ONLY | source_claim | — |
| holding | 1090 | Battery-first charge limit | Charge Power Rate when BatFirst | register value | 1% | R/W | SOURCE_ONLY | source_claim | — |
| holding | 1091 | Battery-first stop SOC | Stop Charge soc when Bat First | register value | 1% | R/W | SOURCE_ONLY | source_claim | — |
| holding | 1092 | Battery-first AC charge enable | WhenBatFirst Enable:1 Disable:0 | register value | — | R/W | RESOLVED | semantic_correlated, source_claim | — |
| holding | 1093 | Register 1093 | — | register value | — | R | UNKNOWN_RESERVED | source_claim | — |
| holding | 1094 | Register 1094 | — | register value | — | R | UNKNOWN_RESERVED | source_claim | — |
| holding | 1095 | Register 1095 | — | register value | — | R | UNKNOWN_RESERVED | source_claim | — |
| holding | 1096 | Register 1096 | — | register value | — | R | UNKNOWN_RESERVED | source_claim | — |
| holding | 1097 | Register 1097 | — | register value | — | R | UNKNOWN_RESERVED | source_claim | — |
| holding | 1098 | Register 1098 | — | register value | — | R | UNKNOWN_RESERVED | source_claim | — |
| holding | 1099 | Register 1099 | — | register value | — | R | UNKNOWN_RESERVED | source_claim | — |
| holding | 1100 | Battery-first slot 1 start | High byte = hour (0-23); low byte = minute (0-59). | register value | hh:mm | R/W | SOURCE_ONLY | source_claim | — |
| holding | 1101 | Battery-first slot 1 stop | High byte = hour (0-23); low byte = minute (0-59). | register value | hh:mm | R/W | SOURCE_ONLY | source_claim | — |
| holding | 1102 | Battery-first slot 1 enable | Enable:1 Disable:0 | register value | — | R/W | SOURCE_ONLY | source_claim | — |
| holding | 1103 | Battery-first slot 2 start | High byte = hour (0-23); low byte = minute (0-59). | register value | hh:mm | R/W | SOURCE_ONLY | source_claim | — |
| holding | 1104 | Battery-first slot 2 stop | High byte = hour (0-23); low byte = minute (0-59). | register value | hh:mm | R/W | SOURCE_ONLY | source_claim | — |
| holding | 1105 | Battery-first slot 2 enable | Enable:1 Disable:0 | register value | — | R/W | SOURCE_ONLY | source_claim | — |
| holding | 1106 | Battery-first slot 3 start | High byte = hour (0-23); low byte = minute (0-59). | register value | hh:mm | R/W | SOURCE_ONLY | source_claim | — |
| holding | 1107 | Battery-first slot 3 stop | High byte = hour (0-23); low byte = minute (0-59). | register value | hh:mm | R/W | SOURCE_ONLY | source_claim | — |
| holding | 1108 | Battery-first slot 3 enable | Enable:1 Disable:0 | register value | — | R/W | SOURCE_ONLY | source_claim | — |
| holding | 1109 | / | reserve | register value | / | R | SOURCE_ONLY | source_claim | — |
| holding | 1110 | Load-first slot 1 start | SPA/reserve | register value | hh:mm | R/W | SOURCE_ONLY | source_claim | — |
| holding | 1111 | Load-first slot 1 stop | SPA/reserve | register value | hh:mm | R/W | SOURCE_ONLY | source_claim | — |
| holding | 1112 | Load-first slot 1 enable | SPA/reserve | register value | — | R/W | SOURCE_ONLY | source_claim | — |
| holding | 1113 | Load-first slot 2 start | SPA/reserve | register value | hh:mm | R/W | SOURCE_ONLY | source_claim | — |
| holding | 1114 | Load-first slot 2 stop | SPA/reserve | register value | hh:mm | R/W | SOURCE_ONLY | source_claim | — |
| holding | 1115 | Load-first slot 2 enable | SPA/reserve | register value | — | R/W | SOURCE_ONLY | source_claim | — |
| holding | 1116 | Load-first slot 3 start | SPA/reserve | register value | hh:mm | R/W | SOURCE_ONLY | source_claim | — |
| holding | 1117 | Load-first slot 3 stop | SPA/reserve | register value | hh:mm | R/W | SOURCE_ONLY | source_claim | — |
| holding | 1118 | Load-first slot 3 enable | SPA/reserve | register value | — | R/W | SOURCE_ONLY | source_claim | — |
| holding | 1119 | Energy calculation formula | 0：Theoldformula 1 ： The new formula | register value | / | R/W | SOURCE_ONLY | source_claim | — |
| holding | 1120 | Backup enable | MIXUS | register value | — | R/W | SOURCE_ONLY | source_claim | — |
| holding | 1121 | SGIP enable | MIXUS | register value | — | R/W | SOURCE_ONLY | source_claim | — |
| holding | 1122 | Register 1122 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| holding | 1123 | Register 1123 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| holding | 1124 | Register 1124 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| input | 1000 | uwSysWorkMode | uwSysWorkMode | register value | — | W | SOURCE_ONLY | source_claim | — |
| input | 1001 | Systemfaultword0 | Systemfaultword0 | register value | Please refer to thefault description of Hybrid | R | SOURCE_ONLY | source_claim | — |
| input | 1002 | Systemfaultword1 | Systemfaultword1 | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 1003 | Systemfaultword2 | Systemfaultword2 | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 1004 | Systemfaultword3 | Systemfaultword3 | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 1005 | Systemfaultword4 | Systemfaultword4 | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 1006 | Systemfaultword5 | Systemfaultword5 | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 1007 | Systemfaultword6 | Systemfaultword6 | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 1008 | Systemfaultword7 | Systemfaultword7 | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 1009 | Pdischarge1H | Dischargepower(high) | register value; /10 | W | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 1010 | Pdischarge1L | Dischargepower(low) | register value; /10 | W | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 1011 | Pcharge1H | Chargepower(high) | register value; /10 | W | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 1012 | Pcharge1L | Chargepower(low) | register value; /10 | W | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 1013 | Vbat | Batteryvoltage | register value | V | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 1014 | SOC | StateofchargeCapacity | register value; /10 | lith/leadacid | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 1015 | PactouserR H | ACpowertouserH | register value | W | R | RESOLVED | semantic_correlated, source_claim | — |
| input | 1016 | PactouserR L | ACpowertouserL | register value | W | R | RESOLVED | semantic_correlated, source_claim | — |
| input | 1017 | PactouserS H | PactouserS H | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 1018 | PactouserS L | PactouserS L | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 1019 | PactouserT H | PactouserT H | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 1020 | PactouserT L | PactouserT H | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 1021 | PactouserTotalH | ACpowertousertotalH | register value; /10 | W | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 1022 | PactouserTotalL | ACpowertousertotalL | register value; /10 | W | R | RESOLVED | semantic_correlated, source_claim | — |
| input | 1023 | PactogridR H | ACpowertogridH | register value | Ac output | R | RESOLVED | semantic_correlated, source_claim | — |
| input | 1024 | PactogridR L | ACpowertogridL | register value | W | R | RESOLVED | semantic_correlated, source_claim | — |
| input | 1025 | PactogridS H | PactogridS H | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 1026 | PactogridS L | PactogridS L | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 1027 | PactogridTH | 0.1w | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 1028 | PactogridTL | 0.1w | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 1029 | pac_to_grid_total | 0.1w | register value; /10 | W | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 1030 | PactogridtotalL | 0.1w | register value; /10 | W | R | RESOLVED | semantic_correlated, source_claim | — |
| input | 1031 | PLocalLoadR H | 0.1w | register value | W | R | RESOLVED | semantic_correlated, source_claim | — |
| input | 1032 | PLocalLoadR L | 0.1w | register value | W | R | RESOLVED | semantic_correlated, source_claim | — |
| input | 1033 | PLocalLoadS H | 0.1w | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 1034 | PLocalLoadS L | 0.1w | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 1035 | PLocalLoadT H | 0.1w | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 1036 | PLocalLoadT L | 0.1w | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 1037 | PLocalLoadtotalH | 0.1w | register value | W | R | RESOLVED | semantic_correlated, source_claim | — |
| input | 1038 | PLocalLoadtotalL | 0.1w | register value | W | R | RESOLVED | semantic_correlated, source_claim | — |
| input | 1039 | IP2MTemperature | 0.1℃ | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 1040 | B2attery Temperature | 0.1℃ | register value | °C | R | RESOLVED | semantic_correlated, source_claim | — |
| input | 1041 | SPDSPStatus | SPDSPStatus | register value | — | R | RESOLVED | semantic_correlated, source_claim | — |
| input | 1042 | SPBusVolt | 0.1V | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 1043 | Register 1043 | — | register value | — | R | UNKNOWN_RESERVED | source_claim | — |
| input | 1044 | Etouser_todayH | Etouser_todayH | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 1045 | Etouser_todayL | Etouser_todayL | register value; /10 | kWh | W | RESOLVED | semantic_correlated, source_claim | — |
| input | 1046 | Etouser_totalH | Etouser_totalH | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 1047 | Etouser_totalL | Etouser_totalL | register value; /10 | kWh | R | RESOLVED | semantic_correlated, source_claim | — |
| input | 1048 | Etogrid_todayH | Etogrid_todayH | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 1049 | Etogrid_todayL | Etogrid_todayL | register value; /10 | kWh | W | RESOLVED | semantic_correlated, source_claim | — |
| input | 1050 | Etogrid_totalH | Etogrid_totalH | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 1051 | Etogrid_totalL | Etogrid_totalL | register value; /10 | kWh | R | RESOLVED | semantic_correlated, source_claim | — |
| input | 1052 | Edischarge1_toda yH | Edischarge1_toda yH | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 1053 | Edischarge1_toda yL | Edischarge1_toda yL | register value; /10 | kWh | R | RESOLVED | semantic_correlated, source_claim | — |
| input | 1054 | Edischarge1_total H | Edischarge1_total H | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 1055 | Edischarge1_total L | Edischarge1_total L | register value; /10 | kWh | W | RESOLVED | semantic_correlated, source_claim | — |
| input | 1056 | Echarge1_todayH | Echarge1_todayH | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 1057 | Echarge1_today L | Echarge1_today L | register value; /10 | kWh | R | RESOLVED | semantic_correlated, source_claim | — |
| input | 1058 | Echarge1_totalH | Echarge1_totalH | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 1059 | Echarge1_totalL | Echarge1_totalL | register value; /10 | kWh | R | RESOLVED | semantic_correlated, source_claim | — |
| input | 1060 | Register 1060 | Localloadenergytoday | register value | kWh | R | UNKNOWN_RESERVED | semantic_correlated, source_claim | — |
| input | 1061 | Register 1061 | Localloadenergytoday | register value | kWh | R | UNKNOWN_RESERVED | semantic_correlated, source_claim | — |
| input | 1062 | Register 1062 | Localloadenergytotal | register value | kWh | R | UNKNOWN_RESERVED | semantic_correlated, source_claim | — |
| input | 1063 | Register 1063 | Localloadenergytotal | register value | kWh | R | UNKNOWN_RESERVED | semantic_correlated, source_claim | — |
| input | 1064 | Register 1064 | ExportLimitApparentPowerH | register value | — | W | UNKNOWN_RESERVED | source_claim | — |
| input | 1065 | Register 1065 | ExportLimitApparentPowerL | register value | — | W | UNKNOWN_RESERVED | source_claim | — |
| input | 1066 | Register 1066 | / | register value | — | R | UNKNOWN_RESERVED | source_claim | — |
| input | 1067 | EpsFac | UPSfrequency | register value | — | R | RESOLVED | semantic_correlated, source_claim | — |
| input | 1068 | EpsVac1 | UPSphaseRoutputvoltage | register value | — | R | RESOLVED | semantic_correlated, source_claim | — |
| input | 1069 | EpsIac1 | UPSphaseRoutputcurrent | register value | — | R | RESOLVED | semantic_correlated, source_claim | — |
| input | 1070 | EpsPac1 | UPSphaseRoutputpower(H) | register value | — | R | RESOLVED | semantic_correlated, source_claim | — |
| input | 1071 | EpsPac1 | UPSphaseRoutputpower(L) | register value | — | R | RESOLVED | semantic_correlated, source_claim | — |
| input | 1072 | EpsVac2 | UPSphaseSoutputvoltage | register value | — | R | RESOLVED | semantic_correlated, source_claim | — |
| input | 1073 | EpsIac2 | UPSphaseSoutputcurrent | register value | — | R | RESOLVED | semantic_correlated, source_claim | — |
| input | 1074 | EpsPac2 | UPSphaseSoutputpower(H) | register value | — | R | RESOLVED | semantic_correlated, source_claim | — |
| input | 1075 | EpsPac2 | UPSphaseSoutputpower(L) | register value | — | R | RESOLVED | semantic_correlated, source_claim | — |
| input | 1076 | EpsVac3 | UPSphaseToutputvoltage | register value | — | R | RESOLVED | semantic_correlated, source_claim | — |
| input | 1077 | EpsIac3 | UPSphaseToutputcurrent | register value | — | R | RESOLVED | semantic_correlated, source_claim | — |
| input | 1078 | EpsPac3 | UPSphaseToutputpower(H) | register value | — | R | RESOLVED | semantic_correlated, source_claim | — |
| input | 1079 | EpsPac3 | UPSphaseToutputpower(L) | register value | — | R | RESOLVED | semantic_correlated, source_claim | — |
| input | 1080 | EpsLoadPercent | LoadpercentofUPSouput | register value | — | R | RESOLVED | semantic_correlated, source_claim | — |
| input | 1081 | EpsPF | Powerfactor | register value | — | R | RESOLVED | semantic_correlated, source_claim | — |
| input | 1082 | Register 1082 | StatusOldfromBMS | register value | — | R | UNKNOWN_RESERVED | source_claim | — |
| input | 1083 | Register 1083 | StatusfromBMS | register value | — | R | UNKNOWN_RESERVED | source_claim | — |
| input | 1084 | Register 1084 | ErrorinfoOldfromBMS | register value | — | R | UNKNOWN_RESERVED | source_claim | — |
| input | 1085 | Register 1085 | ErrorinfomationfromBMS | register value | — | R | UNKNOWN_RESERVED | source_claim | — |
| input | 1086 | Register 1086 | SOCfromBMS | register value | — | R | UNKNOWN_RESERVED | source_claim | — |
| input | 1087 | Register 1087 | BatteryvoltagefromBMS | register value | — | R | UNKNOWN_RESERVED | source_claim | — |
| input | 1088 | Register 1088 | BatterycurrentfromBMS | register value | — | R | UNKNOWN_RESERVED | source_claim | — |
| input | 1089 | Register 1089 | BatterytemperaturefromBMS | register value | — | R | UNKNOWN_RESERVED | source_claim | — |
| input | 1090 | BMS_MaxCurr | Max. charge/discharge current fromBMS(pylon) | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 1091 | BMS_GaugeRM | GaugeRMfromBMS | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 1092 | BMS_GaugeFCC | GaugeFCCfromBMS | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 1093 | BMS_FW | BMS_FW | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 1094 | BMS_DeltaVolt | DeltaVfromBMS | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 1095 | BMS_CycleCnt | CycleCountfromBMS | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 1096 | BMS_SOH | SOHfromBMS | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 1097 | BMS_ConstantV olt | CVvoltagefromBMS | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 1098 | BMS_WarnInfoO ld | WarninginfooldfromBMS | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 1099 | BMS_WarnInfo | WarninginfofromBMS | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 1100 | BMS_GaugeICCu rr | GaugeICcurrentfromBMS | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 1101 | BMS_MCUVersi on | MCUSoftwareversionfromBMS | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 1102 | BMS_GaugeVers ion | GaugeVersionfromBMS | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 1103 | BMS_wGaugeFR Version_L | GaugeFRVersionL16fromBMS | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 1104 | BMS_wGaugeFR Version_H | GaugeFRVersionH16fromBMS | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 1105 | BMS_BMSInfo | BMSInformationfromBMS | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 1106 | BMS_PackInfo | PackInformationfromBMS | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 1107 | BMS_UsingCap | UsingCapfromBMS | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 1108 | uwMaxCellVolt | Maximumsinglebatteryvoltage | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 1109 | uwMinCellVolt | Lowestsinglebatteryvoltage | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 1110 | bModuleNum | Batteryparallelnumber | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 1111 | Numberofbatteries | Numberofbatteries | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 1112 | uwMaxVoltCellN o | MaxVoltCellNo | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 1113 | uwMinVoltCellN o | MinVoltCellNo | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 1114 | uwMaxTemprCe ll_10T | MaxTemprCell_10T | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 1115 | uwMinTemprCel l_10T | MinTemprCell_10T | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 1116 | uwMaxTemprCe llNo | MaxVoltTemprCellNo | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 1117 | uwMinTemprCel | MinVoltTemprCellNo | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 1118 | ProtectpackID | FaultyBatteryAddress | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 1119 | MaxSOC | ParallelmaximumSOC | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 1120 | MinSOC | ParallelminimumSOC | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 1121 | BMS_Error2 | BatteryProtection2 | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 1122 | BMS_Error3 | BatteryProtection3 | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 1123 | BMS_WarnInfo2 | BatteryWarn2 | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 1124 | ACCharge EnergyTodayH | ACChargeEnergytoday | register value | kWh | W | RESOLVED | semantic_correlated, source_claim | — |
| input | 1125 | ACCharge EnergyTodayL | ACChargeEnergytoday | register value | kWh | W | RESOLVED | semantic_correlated, source_claim | — |
| input | 1126 | A1CCharge EnergyTotalH | A1CCharge EnergyTotalH | register value | kWh | R | RESOLVED | semantic_correlated, source_claim | — |
| input | 1127 | ACCharge EnergyTotalL | ACCharge EnergyTotalL | register value | kWh | R | RESOLVED | semantic_correlated, source_claim | — |
| input | 1128 | AC Charge Power H | ACChargePower | register value | — | W | SOURCE_ONLY | source_claim | — |
| input | 1129 | AC Charge PowerL | ACChargePower | register value | — | W | SOURCE_ONLY | source_claim | — |
| input | 1130 | 70% INV Power adjust | uwGridPower_70_AdjEE_SP | register value | — | W | SOURCE_ONLY | source_claim | — |
| input | 1131 | Extra AC Power to grid_H | ExtrainverteACPowertogrid High | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 1132 | Extra AC Power to grid_L | ExtrainverteACPowertogridLow | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 1133 | Eextra_todayH | ExtrainverterPowerTOUser_Extra today(high) | register value | 0.1kWh | R | SOURCE_ONLY | source_claim | — |
| input | 1134 | Eextra_todayL | ExtrainverterPowerTOUser_Extra today(low) | register value | 0.1kWh | R | SOURCE_ONLY | source_claim | — |
| input | 1135 | Eextra_totalH | ExtrainverterPowerTOUser_Extra total(high) | register value | 0.1kWh | R | SOURCE_ONLY | source_claim | — |
| input | 1136 | Eextra_totalL | ExtrainverterPowerTOUser_Extra total(low) | register value | 0.1kWh | R | SOURCE_ONLY | source_claim | — |
| input | 1137 | Esystem_today H | SystemelectricenergytodayH | register value | 0.1kWh | R | SOURCE_ONLY | source_claim | — |
| input | 1138 | Esystem_ today L | SystemelectricenergytodayL | register value | SPA used System electric energytodayL | R | SOURCE_ONLY | source_claim | — |
| input | 1139 | Esystem_totalH | SystemelectricenergytotalH | register value | SPA used System electric energytotalH | R | SOURCE_ONLY | source_claim | — |
| input | 1140 | Esystem_totalL | SystemelectricenergytotalL | register value | SPA used System electric energytotalL | R | SOURCE_ONLY | source_claim | — |
| input | 1141 | Eself_todayH | selfelectricenergytodayH | register value | self electric energytodayH | R | SOURCE_ONLY | source_claim | — |
| input | 1142 | Eself_todayL | selfelectricenergytodayL | register value | self electric energytodayL | R | SOURCE_ONLY | source_claim | — |
| input | 1143 | Eself_totalH | selfelectricenergytotalH | register value | self electric energytotalH | R | SOURCE_ONLY | source_claim | — |
| input | 1144 | Eself_totalL | selfelectricenergytotalL | register value | self electric energytotalL | R | SOURCE_ONLY | source_claim | — |
| input | 1145 | PSystemH | SystempowerH | register value | SystempowerH | R | SOURCE_ONLY | source_claim | — |
| input | 1146 | PSystemL | SystempowerL | register value | SystempowerL | R | SOURCE_ONLY | source_claim | — |
| input | 1147 | PSelfH | selfpowerH | register value | selfpowerH | R | SOURCE_ONLY | source_claim | — |
| input | 1148 | PSelfL | selfpowerL | register value | selfpowerL | R | SOURCE_ONLY | source_claim | — |
| input | 1149 | EPVAll_TodayH | PVelectricenergytodayH | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 1150 | EPVAll_TodayL | PVelectricenergytodayL | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 1151 | AcDischarge PackSn | Discharge power pack serial number | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 1152 | Accdischarge power_H | Cumulative discharge power high 16-bitbyte | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 1153 | Accdischarge power_L | Cumulative discharge power low 16-bitbyte | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 1154 | AccCharge PackSn | chargepowerpackserialnumber | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 1155 | AccCharge power_H | Cumulative charge power high 16-bitbyte | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 1156 | AccCharge power_L | Cumulative charge power low 16-bitbyte | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 1157 | FirstBattFaultSn | FirstBattFaultSn | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 1158 | Second BattFaultSn | Second BattFaultSn | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 1159 | Third BattFaultSn | Third BattFaultSn | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 1160 | Fourth BattFaultSn | Fourth BattFaultSn | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 1161 | Batteryhistory faultcode1 | Batteryhistoryfaultcode1 | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 1162 | Batteryhistory faultcode2 | Batteryhistoryfaultcode2 | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 1163 | Batteryhistory faultcode3 | Batteryhistoryfaultcode3 | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 1164 | Batteryhistory faultcode4 | Batteryhistoryfaultcode4 | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 1165 | Batteryhistory faultcode5 | Batteryhistoryfaultcode5 | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 1166 | Batteryhistory faultcode6 | Batteryhistoryfaultcode6 | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 1167 | Batteryhistory faultcode7 | Batteryhistoryfaultcode7 | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 1168 | Batteryhistory faultcode8 | Batteryhistoryfaultcode8 | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 1169 | Number of battery codes | Number of battery codes PACK number + BIC forward and reversecodes | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 1170 | Register 1170 | — | register value | — | R | UNKNOWN_RESERVED | source_claim | — |
| input | 1171 | Register 1171 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| input | 1172 | Register 1172 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| input | 1173 | Register 1173 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| input | 1174 | Register 1174 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| input | 1175 | Register 1175 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| input | 1176 | Register 1176 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| input | 1177 | Register 1177 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| input | 1178 | Register 1178 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| input | 1179 | Register 1179 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| input | 1180 | Register 1180 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| input | 1181 | Register 1181 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| input | 1182 | Register 1182 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| input | 1183 | Register 1183 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| input | 1184 | Register 1184 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| input | 1185 | Register 1185 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| input | 1186 | Register 1186 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| input | 1187 | Register 1187 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| input | 1188 | Register 1188 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| input | 1189 | Register 1189 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| input | 1190 | Register 1190 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| input | 1191 | Register 1191 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| input | 1192 | Register 1192 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| input | 1193 | Register 1193 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| input | 1194 | Register 1194 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| input | 1195 | Register 1195 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| input | 1196 | Register 1196 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| input | 1197 | Register 1197 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| input | 1198 | Register 1198 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| input | 1199 | NewEPowerCalc Flag | Intelligent reading is used to identify software compatibility features | register value | 0 ： Old energy calculation； 1 ： new energy calculation | R | SOURCE_ONLY | source_claim | — |
| input | 1200 | MaxCellVolt | Maximumcellvoltage | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 1201 | MinCellVolt | Minimumcellvoltage | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 1202 | ModuleNum | NumberofBatterymodules | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 1203 | TotalCellNum | Totalnumberofcells | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 1204 | MaxVoltCellNo | MaxVoltCellNo | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 1205 | MinVoltCellNo | MinVoltCellNo | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 1206 | MaxTemprCell_ 10T | MaxTemprCell_10T | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 1207 | MinTemprCell_1 0T | MinTemprCell_10T | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 1208 | MaxTemprCellN o | MaxTemprCellNo | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 1209 | MinTemprCellN o | MinTemprCellNo | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 1210 | ProtectPackID | FaultPackID | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 1211 | MaxSOC | ParallelmaximumSOC | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 1212 | MinSOC | ParallelminimumSOC | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 1213 | BatProtect1Add | BatProtect1Add | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 1214 | BatProtect2Add | BatProtect2Add | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 1215 | BatWarn1Add | BatWarn1Add | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 1216 | BMS_HighestSof tVersion | BMS_HighestSoftVersion | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 1217 | BMS_Hardware Version | BMS_HardwareVersion | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 1218 | BMS_RequestTy pe | BMS_RequestType | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 1219 | Register 1219 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| input | 1220 | Register 1220 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| input | 1221 | Register 1221 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| input | 1222 | Register 1222 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| input | 1223 | Register 1223 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| input | 1224 | Register 1224 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| input | 1225 | Register 1225 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| input | 1226 | Register 1226 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| input | 1227 | Register 1227 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| input | 1228 | Register 1228 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| input | 1229 | Register 1229 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| input | 1230 | Register 1230 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| input | 1231 | Register 1231 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| input | 1232 | Register 1232 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| input | 1233 | Register 1233 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| input | 1234 | Register 1234 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| input | 1235 | Register 1235 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| input | 1236 | Register 1236 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| input | 1237 | Register 1237 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| input | 1238 | Register 1238 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| input | 1239 | Register 1239 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| input | 1240 | Register 1240 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| input | 1241 | Register 1241 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| input | 1242 | Register 1242 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| input | 1243 | Register 1243 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| input | 1244 | Register 1244 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| input | 1245 | Register 1245 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| input | 1246 | Register 1246 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| input | 1247 | Register 1247 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| input | 1248 | bKeyAgingTestO kFlag | Success sign of key detection beforeaging | register value | 1：Finishedtest 0 ： test not completed | R | SOURCE_ONLY | source_claim | — |
| input | 1249 | / | / | register value | reversed | R | SOURCE_ONLY | source_claim | — |
| input | 2000 | InverterStatus | Inverterrunstate | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 2001 | Register 2001 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| input | 2002 | Register 2002 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| input | 2003 | Register 2003 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| input | 2004 | Register 2004 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| input | 2005 | Register 2005 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| input | 2006 | Register 2006 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| input | 2007 | Register 2007 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| input | 2008 | Register 2008 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| input | 2009 | Register 2009 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| input | 2010 | Register 2010 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| input | 2011 | Register 2011 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| input | 2012 | Register 2012 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| input | 2013 | Register 2013 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| input | 2014 | Register 2014 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| input | 2015 | Register 2015 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| input | 2016 | Register 2016 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| input | 2017 | Register 2017 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| input | 2018 | Register 2018 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| input | 2019 | Register 2019 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| input | 2020 | Register 2020 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| input | 2021 | Register 2021 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| input | 2022 | Register 2022 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| input | 2023 | Register 2023 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| input | 2024 | Register 2024 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| input | 2025 | Register 2025 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| input | 2026 | Register 2026 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| input | 2027 | Register 2027 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| input | 2028 | Register 2028 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| input | 2029 | Register 2029 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| input | 2030 | Register 2030 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| input | 2031 | Register 2031 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| input | 2032 | Register 2032 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| input | 2033 | Register 2033 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| input | 2034 | Register 2034 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| input | 2035 | PacH | Outputpower(high) | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 2036 | PacL | Outputpower(low) | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 2037 | Fac | Gridfrequency | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 2038 | Vac1 | Three/singlephasegridvoltage | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 2039 | Iac1 | Three/singlephasegridoutputcurrent | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 2040 | Pac1H | Three/single phase grid output watt VA(high) | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 2041 | Pac1L | Three/single phase grid output watt VA(low) | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 2042 | Register 2042 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| input | 2043 | Register 2043 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| input | 2044 | Register 2044 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| input | 2045 | Register 2045 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| input | 2046 | Register 2046 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| input | 2047 | Register 2047 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| input | 2048 | Register 2048 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| input | 2049 | Register 2049 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| input | 2050 | Register 2050 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| input | 2051 | Register 2051 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| input | 2052 | Register 2052 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| input | 2053 | EactodayH | Todaygenerateenergy(high) | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 2054 | EactodayL | Todaygenerateenergy(low) | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 2055 | EactotalH | Totalgenerateenergy(high) | register value | SPA | R | SOURCE_ONLY | source_claim | — |
| input | 2056 | EactotalL | Totalgenerateenergy(low) | register value | SPA | R | SOURCE_ONLY | source_claim | — |
| input | 2057 | TimetotalH | Worktimetotal(high) | register value | SPA | R | SOURCE_ONLY | source_claim | — |
| input | 2058 | TimetotalL | Worktimetotal(low) | register value | SPA | R | SOURCE_ONLY | source_claim | — |
| input | 2059 | Register 2059 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| input | 2060 | Register 2060 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| input | 2061 | Register 2061 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| input | 2062 | Register 2062 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| input | 2063 | Register 2063 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| input | 2064 | Register 2064 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| input | 2065 | Register 2065 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| input | 2066 | Register 2066 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| input | 2067 | Register 2067 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| input | 2068 | Register 2068 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| input | 2069 | Register 2069 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| input | 2070 | Register 2070 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| input | 2071 | Register 2071 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| input | 2072 | Register 2072 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| input | 2073 | Register 2073 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| input | 2074 | Register 2074 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| input | 2075 | Register 2075 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| input | 2076 | Register 2076 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| input | 2077 | Register 2077 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| input | 2078 | Register 2078 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| input | 2079 | Register 2079 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| input | 2080 | Register 2080 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| input | 2081 | Register 2081 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| input | 2082 | Register 2082 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| input | 2083 | Register 2083 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| input | 2084 | Register 2084 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| input | 2085 | Register 2085 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| input | 2086 | Register 2086 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| input | 2087 | Register 2087 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| input | 2088 | Register 2088 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| input | 2089 | Register 2089 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| input | 2090 | Register 2090 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| input | 2091 | Register 2091 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| input | 2092 | Register 2092 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| input | 2093 | Temp1 | Invertertemperature | register value | SPA | R | SOURCE_ONLY | source_claim | — |
| input | 2094 | Temp2 | TheinsideIPMininverterTemperature | register value | SPA | R | SOURCE_ONLY | source_claim | — |
| input | 2095 | Temp3 | Boosttemperature | register value | SPA | R | SOURCE_ONLY | source_claim | — |
| input | 2096 | Temp4 | Temp4 | register value | reserved | R | SOURCE_ONLY | source_claim | — |
| input | 2097 | uwBatVolt_DSP | BatVolt_DSP | register value | BatVolt(DSP) | R | SOURCE_ONLY | source_claim | — |
| input | 2098 | PBusVoltage | PBusinsideVoltage | register value | SPA | R | SOURCE_ONLY | source_claim | — |
| input | 2099 | NBusVoltage | NBusinsideVoltage | register value | SPA | R | SOURCE_ONLY | source_claim | — |
| input | 2100 | RemoteCtrlEn | / | register value | Remote setup enable | R | SOURCE_ONLY | source_claim | — |
| input | 2101 | RemoteCtrlPow er | / | register value | Remotely setpower | R | SOURCE_ONLY | source_claim | — |
| input | 2102 | Extra AC Power to grid_H | ExtrainverteACPowertogridHigh | register value | SPAused | R | SOURCE_ONLY | source_claim | — |
| input | 2103 | Extra AC Power to grid_L | ExtrainverteACPowertogridLow | register value | SPAused | R | SOURCE_ONLY | source_claim | — |
| input | 2104 | Eextra_todayH | ExtrainverterPowerTOUser_Extra today(high) | register value | SPA used | R | SOURCE_ONLY | source_claim | — |
| input | 2105 | Eextra_todayL | ExtrainverterPowerTOUser_Extra today(low) | register value | SPA used | R | SOURCE_ONLY | source_claim | — |
| input | 2106 | Eextra_totalH | Extrainverter PowerTOUser_Extratotal(high) | register value | SPA used | R | SOURCE_ONLY | source_claim | — |
| input | 2107 | Eextra_totalL | ExtrainverterPowerTOUser_Extra total(low) | register value | SPA used | R | SOURCE_ONLY | source_claim | — |
| input | 2108 | Esystem_today H | SystemelectricenergytodayH | register value | SPA used System electric energy todayH | R | SOURCE_ONLY | source_claim | — |
| input | 2109 | Esystem_ today L | SystemelectricenergytodayL | register value | SPA used System electric energy todayL | R | SOURCE_ONLY | source_claim | — |
| input | 2110 | Esystem_totalH | SystemelectricenergytotalH | register value | SPA used System | R | SOURCE_ONLY | source_claim | — |
| input | 2111 | Esystem_totalL | SystemelectricenergytotalL | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 2112 | EACharge_Today _H | ACChargeenergytoday | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 2113 | EACharge_Today _L | ACChargeenergytoday | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 2114 | EACharge_Total _H | ACChargeenergytotal | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 2115 | EACharge_Total _L | ACChargeenergytotal | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 2116 | AC charge Power_H | Gridpowertolocalload | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 2117 | AC charge Power_L | Gridpowertolocalload | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 2118 | Priority | 0:LoadFirst 1:BatteryFirst 2:GridFirst | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 2119 | BatteryType | 0：Lead-acid 1：Lithiumbattery | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 2120 | AutoProofreadC MD | Agingmode | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 2121 | Register 2121 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| input | 2122 | Register 2122 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| input | 2123 | Register 2123 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| input | 2124 | reserved | reserved | register value | — | R | UNKNOWN_RESERVED | source_claim | — |

### SPH storage

Storage family applicability comes from the graph/catalogue ranges.

| Table | Address | Name | Description | Encoding / scale | Unit | Access | Status | Evidence | Notes |
|---|---:|---|---|---|---|---|---|---|---|
| holding | 0 | Inverter Enabled | Theinvertercanbeswitched onandoff,andtheBDCcanbe switchedonandoffforthe battreadyfunction. | register value; /10 | — | R/W | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| holding | 1 | Safety function enable flags | SPI: system protection interface Bit0~3:forCEI0-21 Bit4~6:forSAA | register value | — | W | SOURCE_ONLY | source_claim | — |
| holding | 2 | Persist power-factor commands | Means these settings will be acting or not when next poweron | register value | — | W | RESOLVED | semantic_correlated, source_claim | — |
| holding | 3 | Active power limit setpoint | 255:powerisnotbelimited | register value; /1 | % | W | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| holding | 4 | Reactive power limit setpoint | 255:powerisnotbelimited | register value; /1 | % | W | SOURCE_ONLY | source_claim | — |
| holding | 5 | Power factor target | Inverter output power factor’s10000times | register value; /10000 | pf | W | SOURCE_ONLY | source_claim | — |
| holding | 6 | Rated apparent power | Normal power(high) | register value; /10 | 0.1VA | R | SOURCE_ONLY | source_claim | — |
| holding | 7 | Rated apparent power | Normal power(low) | register value; /10 | 0.1VA | R | SOURCE_ONLY | source_claim | — |
| holding | 8 | Nominal PV voltage | NormalworkPV voltage | register value; /10 | 0.1V | R | SOURCE_ONLY | source_claim | — |
| holding | 9 | Firmware | Firmwareversion (high) | firmware_version; /10 | ASCII | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| holding | 10 | Firmware | Firmwareversion (middle) | register value | ASCII | R | SOURCE_ONLY | source_claim | — |
| holding | 11 | Firmware | Firmwareversion(low) | register value | ASCII | R | SOURCE_ONLY | source_claim | — |
| holding | 12 | Firmware | ControlFirmware version(high) | register value | ASCII | R | SOURCE_ONLY | source_claim | — |
| holding | 13 | Firmware | ControlFirmware version(middle) | register value | ASCII | R | SOURCE_ONLY | source_claim | — |
| holding | 14 | Firmware | ControlFirmware version(low) | register value | ASCII | R | SOURCE_ONLY | source_claim | — |
| holding | 15 | LCD language selection | 0:Italian; 1:English; 2:German; 3:Spanish; 4:French; 5:Chinese; 6：Polish 7：Portugues 8：Hungary | register value | — | W | SOURCE_ONLY | source_claim | — |
| holding | 16 | Country profile configured | CountrySelectedor not | register value | — | W | SOURCE_ONLY | source_claim | — |
| holding | 17 | PV start voltage threshold | Inputstartvoltage | register value; /10 | 0.1V | W | SOURCE_ONLY | source_claim | — |
| holding | 18 | Start-up delay | Starttime | register value; /1 | 1s | W | SOURCE_ONLY | source_claim | — |
| holding | 19 | Restart delay | RestartDelayTime afterfaultback; | register value; /1 | 1s | W | SOURCE_ONLY | source_claim | — |
| holding | 20 | Active power ramp rate (startup) | Powerstartslope | register value; /10 | 0.1% | W | SOURCE_ONLY | source_claim | — |
| holding | 21 | Active power ramp rate (restart) | Powerrestartslope | register value; /10 | 0.1% | W | SOURCE_ONLY | source_claim | — |
| holding | 22 | Modbus RTU baud rate | Select communicationbaudrat e 0:9600bps 1:38400bps | register value | — | W | SOURCE_ONLY | source_claim | — |
| holding | 23 | Serial Number | The Home Assistant integration exposes this as the device serial number and reuses it as the unique identifier. | serial_number; /10 | ASCII | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| holding | 24 | Serial Number | The Home Assistant integration exposes this as the device serial number and reuses it as the unique identifier. | register value | ASCII | R | SOURCE_ONLY | source_claim | — |
| holding | 25 | Serial Number | The Home Assistant integration exposes this as the device serial number and reuses it as the unique identifier. | register value | ASCII | R | SOURCE_ONLY | source_claim | — |
| holding | 26 | Serial Number | The Home Assistant integration exposes this as the device serial number and reuses it as the unique identifier. | register value | ASCII | R | SOURCE_ONLY | source_claim | — |
| holding | 27 | Serial Number | The Home Assistant integration exposes this as the device serial number and reuses it as the unique identifier. | register value | ASCII | R | SOURCE_ONLY | source_claim | — |
| holding | 28 | Inverter Model | Home Assistant renders this value as the string A# B# D# T# P# U# M# S# via the integration's model() helper. Vendor spec lists value pattern `&*5`; digits appear to be stored without the leading letter codes, so treat as encoded tokens until verified on hardware. | register value; /10 | — | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| holding | 29 | Inverter Model | Home Assistant renders this value as the string A# B# D# T# P# U# M# S# via the integration's model() helper. Vendor spec lists value pattern `&*5`; digits appear to be stored without the leading letter codes, so treat as encoded tokens until verified on hardware. | register value | — | R | SOURCE_ONLY | source_claim | — |
| holding | 30 | Modbus slave address | Communicate address | register value | — | W | SOURCE_ONLY | source_claim | — |
| holding | 31 | Firmware update trigger | Updatefirmware | register value | — | W | SOURCE_ONLY | source_claim | — |
| holding | 32 | Reset user configuration | Use with caution; the inverter immediately reboots and loses provisioning data. | register value | — | W | SOURCE_ONLY | source_claim | — |
| holding | 33 | Factory reset | Equivalent to the front-panel factory reset. Requires re-commissioning afterwards. | register value | — | W | SOURCE_ONLY | source_claim | — |
| holding | 34 | Manufacturer information string | The original table lists these words as Manufacturer Info 8-1 (high/middle/low); combine them to read the full string. | register value | ASCII | R | SOURCE_ONLY | source_claim | — |
| holding | 35 | Manufacturer information string | The original table lists these words as Manufacturer Info 8-1 (high/middle/low); combine them to read the full string. | register value | ASCII | R | SOURCE_ONLY | source_claim | — |
| holding | 36 | Manufacturer information string | The original table lists these words as Manufacturer Info 8-1 (high/middle/low); combine them to read the full string. | register value | ASCII | R | SOURCE_ONLY | source_claim | — |
| holding | 37 | Manufacturer information string | The original table lists these words as Manufacturer Info 8-1 (high/middle/low); combine them to read the full string. | register value | ASCII | R | SOURCE_ONLY | source_claim | — |
| holding | 38 | Manufacturer information string | The original table lists these words as Manufacturer Info 8-1 (high/middle/low); combine them to read the full string. | register value | ASCII | R | SOURCE_ONLY | source_claim | — |
| holding | 39 | Manufacturer information string | The original table lists these words as Manufacturer Info 8-1 (high/middle/low); combine them to read the full string. | register value | ASCII | R | SOURCE_ONLY | source_claim | — |
| holding | 40 | Manufacturer information string | The original table lists these words as Manufacturer Info 8-1 (high/middle/low); combine them to read the full string. | register value | ASCII | R | SOURCE_ONLY | source_claim | — |
| holding | 41 | Manufacturer information string | The original table lists these words as Manufacturer Info 8-1 (high/middle/low); combine them to read the full string. | register value | ASCII | R | SOURCE_ONLY | source_claim | — |
| holding | 42 | G100 failsafe enable | EnglishG100failsafeset | register value | — | W | SOURCE_ONLY | source_claim | — |
| holding | 43 | Device Type Code | Vendor spec provides value pattern `&*6`; handle as encoded type/family digits with implied prefixes pending confirmation. | register value; /10 | — | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| holding | 44 | Number Of Trackers And Phases | Inputtrackernumand outputphasenum | register value; /10 | — | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| holding | 45 | System clock year | Localtime | register value | — | W | SOURCE_ONLY | source_claim | — |
| holding | 46 | System clock month | Systemtime-Month | register value | — | W | SOURCE_ONLY | source_claim | — |
| holding | 47 | System clock day | Systemtime-Day | register value | — | W | SOURCE_ONLY | source_claim | — |
| holding | 48 | System clock hour | Systemtime-Hour | register value | — | W | SOURCE_ONLY | source_claim | — |
| holding | 49 | System clock minute | Systemtime-Min | register value | — | W | SOURCE_ONLY | source_claim | — |
| holding | 50 | System clock second | Systemtime-Second | register value | — | W | SOURCE_ONLY | source_claim | — |
| holding | 51 | System clock weekday | SystemWeekly | register value | — | W | SOURCE_ONLY | source_claim | — |
| holding | 52 | Stage 1 undervoltage limit | Gridvoltagelowlimit protect | register value | 0.1V | W | SOURCE_ONLY | source_claim | — |
| holding | 53 | Stage 1 overvoltage limit | Gridvoltagehighlimit protect | register value | 0.1V | W | SOURCE_ONLY | source_claim | — |
| holding | 54 | Stage 1 underfrequency limit | Gridfrequencylow limitprotect | register value | 0.01 Hz | W | SOURCE_ONLY | source_claim | — |
| holding | 55 | Stage 1 overfrequency limit | Gridhigh frequencylimitprotect | register value | 0.01 Hz | W | SOURCE_ONLY | source_claim | — |
| holding | 56 | Stage 2 undervoltage limit | Gridvoltagelowlimit protect2 | register value | 0.1V | W | SOURCE_ONLY | source_claim | — |
| holding | 57 | Stage 2 overvoltage limit | Gridvoltagehighlimit protect2 | register value | 0.1V | W | SOURCE_ONLY | source_claim | — |
| holding | 58 | Stage 2 underfrequency limit | Gridfrequencylow limitprotect2 | register value | 0.01 Hz | W | SOURCE_ONLY | source_claim | — |
| holding | 59 | Stage 2 overfrequency limit | Gridhighfrequency limitprotect2 | register value | 0.01 Hz | W | SOURCE_ONLY | source_claim | — |
| holding | 60 | Stage 3 undervoltage limit | Grid voltage low limit protect3 | register value | 0.1V | W | SOURCE_ONLY | source_claim | — |
| holding | 61 | Stage 3 overvoltage limit | Grid voltage high limit protect3 | register value | 0.1V | W | SOURCE_ONLY | source_claim | — |
| holding | 62 | Stage 3 underfrequency limit | Grid frequency low limitprotect3 | register value | 0.01Hz | W | SOURCE_ONLY | source_claim | — |
| holding | 63 | Stage 3 overfrequency limit | Grid frequency high limitprotect3 | register value | 0.01Hz | W | SOURCE_ONLY | source_claim | — |
| holding | 64 | Reconnect undervoltage limit | Gridlowvoltagelimit connecttoGrid | register value | 0.1V | W | SOURCE_ONLY | source_claim | — |
| holding | 65 | Reconnect overvoltage limit | Gridhighvoltagelimit connecttoGrid | register value | 0.1V | W | SOURCE_ONLY | source_claim | — |
| holding | 66 | Reconnect underfrequency limit | Gridlowfrequency | register value | 0.01 | W | SOURCE_ONLY | source_claim | — |
| holding | 67 | Reconnect overfrequency limit | Gridhighfrequency limitconnecttoGrid | register value | 0.01 Hz | W | SOURCE_ONLY | source_claim | — |
| holding | 68 | Stage 1 undervoltage trip delay | Grid voltage low limit protecttime 1 | register value | Cycle | W | SOURCE_ONLY | source_claim | — |
| holding | 69 | Stage 1 overvoltage trip delay | Grid voltage high limit protecttime 1 | register value | Cycle | W | SOURCE_ONLY | source_claim | — |
| holding | 70 | Stage 2 undervoltage trip delay | Grid voltage low limit protecttime 2 | register value | Cycle | W | SOURCE_ONLY | source_claim | — |
| holding | 71 | Stage 2 overvoltage trip delay | Grid voltage high limit protecttime 2 | register value | Cycle | W | SOURCE_ONLY | source_claim | — |
| holding | 72 | Stage 1 underfrequency trip delay | Grid frequency low limitprotecttime 1 | register value | Cycle | W | SOURCE_ONLY | source_claim | — |
| holding | 73 | Modbus Version | Grid frequency high limitprotecttime 1 | register value | Cycle | W | SOURCE_ONLY | source_claim | — |
| holding | 74 | Stage 2 underfrequency trip delay | Grid frequency low limitprotecttime 2 | register value | Cycle | W | SOURCE_ONLY | source_claim | — |
| holding | 75 | Stage 2 overfrequency trip delay | Grid frequency high limitprotecttime 2 | register value | Cycle | W | SOURCE_ONLY | source_claim | — |
| holding | 76 | Stage 3 undervoltage trip delay | Grid voltage low limit protecttime 3 | register value | Cycle | W | SOURCE_ONLY | source_claim | — |
| holding | 77 | Stage 3 overvoltage trip delay | Grid voltage high limit protecttime 3 | register value | Cycle | W | SOURCE_ONLY | source_claim | — |
| holding | 78 | Stage 3 underfrequency trip delay | Grid frequency low limitprotecttime 3 | register value | Cycle | W | SOURCE_ONLY | source_claim | — |
| holding | 79 | Stage 3 overfrequency trip delay | Grid frequency high limitprotecttime 3 | register value | Cycle | W | SOURCE_ONLY | source_claim | — |
| holding | 80 | Ten-minute overvoltage limit | Voltprotectionfor10 min | register value | 0.1V | W | SOURCE_ONLY | source_claim | — |
| holding | 81 | PV input high-voltage fault | PVVoltageHigh Fault | register value | 0.1V | W | SOURCE_ONLY | source_claim | — |
| holding | 82 | Controller firmware build string | Positions: 0-1 model letters, 2-3 model variant, 4-5 DSP1 build, 6-7 DSP2/M0 build, 8-9 CPLD/AFCI build, 10-11 M3 build. | register value | ASCII | R | SOURCE_ONLY | source_claim | — |
| holding | 83 | Controller firmware build string | Positions: 0-1 model letters, 2-3 model variant, 4-5 DSP1 build, 6-7 DSP2/M0 build, 8-9 CPLD/AFCI build, 10-11 M3 build. | register value | ASCII | R | SOURCE_ONLY | source_claim | — |
| holding | 84 | Controller firmware build string | Positions: 0-1 model letters, 2-3 model variant, 4-5 DSP1 build, 6-7 DSP2/M0 build, 8-9 CPLD/AFCI build, 10-11 M3 build. | register value | ASCII | R | SOURCE_ONLY | source_claim | — |
| holding | 85 | Controller firmware build string | Positions: 0-1 model letters, 2-3 model variant, 4-5 DSP1 build, 6-7 DSP2/M0 build, 8-9 CPLD/AFCI build, 10-11 M3 build. | register value | ASCII | R | SOURCE_ONLY | source_claim | — |
| holding | 86 | Controller firmware build string | Positions: 0-1 model letters, 2-3 model variant, 4-5 DSP1 build, 6-7 DSP2/M0 build, 8-9 CPLD/AFCI build, 10-11 M3 build. | register value | ASCII | R | SOURCE_ONLY | source_claim | — |
| holding | 87 | Controller firmware build string | Positions: 0-1 model letters, 2-3 model variant, 4-5 DSP1 build, 6-7 DSP2/M0 build, 8-9 CPLD/AFCI build, 10-11 M3 build. | register value | ASCII | R | SOURCE_ONLY | source_claim | — |
| holding | 88 | Modbus Version | ModbusVersion | register value; /100 | Int(16 bits) | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| holding | 89 | Power-factor control mode | 0=Unity PF, 1=Fixed PF setpoint, 2=Default PF line, 3=User-defined PF line, 4=Under-excited reactive power, 5=Over-excited reactive power, 6=Q(V) curve, 7=Direct control, 8=Static capacitive QV, 9=Static inductive QV. | register value | — | W | SOURCE_ONLY | source_claim | — |
| holding | 90 | GPRS modem IP/status flags | Bit 0-3: 0=idle, 1=IP read requested, 2=set IP succeeded; Bit 4-7: 0=unknown, 1=modem OK, 2=no SIM, 3=no network, 4=TCP connect fail, 5=TCP connected, etc. | register value | — | W | UNKNOWN_RESERVED | source_claim | — |
| holding | 91 | Frequency derating start | Frequencyderating startpoint | register value | 0.01H Z | W | SOURCE_ONLY | source_claim | — |
| holding | 92 | Frequency derating slope | Frequency–loadlimit rate | register value | 10tim es | W | SOURCE_ONLY | source_claim | — |
| holding | 93 | CEI 0-21 Q(V) point V1S | CEI021V1SQ(v) | register value | 0.1V | W | SOURCE_ONLY | source_claim | — |
| holding | 94 | CEI 0-21 Q(V) point V2S | CEI021V2SQ(v) | register value | 0.1V | W | SOURCE_ONLY | source_claim | — |
| holding | 95 | CEI 0-21 Q(V) point V1L | CEI021V1LQ(v) | register value | 0.1V | W | SOURCE_ONLY | source_claim | — |
| holding | 96 | CEI 0-21 Q(V) point V2L | CEI021V2LQ(v) | register value | 0.1V | W | SOURCE_ONLY | source_claim | — |
| holding | 97 | Q(V) lock-in active power | Q(v)lockinactive powerofCEI021 | register value | Percen t | W | SOURCE_ONLY | source_claim | — |
| holding | 98 | Q(V) lock-out active power | Q(v)lockOutactive powerofCEI021 | register value | Percen t | W | SOURCE_ONLY | source_claim | — |
| holding | 99 | Power-factor curve lock-in voltage | Lockingirdvoltof CEI021PFline | register value | 0.1V | W | SOURCE_ONLY | source_claim | — |
| holding | 100 | Power-factor curve lock-out voltage | Lockoutgirdvoltof CEI021PFline | register value | 0.1V | W | SOURCE_ONLY | source_claim | — |
| holding | 101 | Power-factor adjust value 1 | PFadjustvalue1 | register value | — | W | SOURCE_ONLY | source_claim | — |
| holding | 102 | Power-factor adjust value 2 | PFadjustvalue2 | register value | — | W | SOURCE_ONLY | source_claim | — |
| holding | 103 | Power-factor adjust value 3 | PFadjustvalue3 | register value | — | W | SOURCE_ONLY | source_claim | — |
| holding | 104 | Power-factor adjust value 4 | PFadjustvalue4 | register value | — | W | SOURCE_ONLY | source_claim | — |
| holding | 105 | Power-factor adjust value 5 | PFadjustvalue5 | register value | — | W | SOURCE_ONLY | source_claim | — |
| holding | 106 | Power-factor adjust value 6 | PFadjustvalue6 | register value | — | W | SOURCE_ONLY | source_claim | — |
| holding | 107 | Q(V) response delay | QV Reactive Power delaytime | register value | 1S | W | SOURCE_ONLY | source_claim | — |
| holding | 108 | Over-frequency derating delay | Overfrequency derati ngdelaytime | register value | 50ms | W | SOURCE_ONLY | source_claim | — |
| holding | 109 | Maximum reactive power magnitude | QmaxforQ(V)curve | register value | 0.1% | W | SOURCE_ONLY | source_claim | — |
| holding | 110 | PF curve point 1 load | 255meansnothispoint | register value | percen t | W | SOURCE_ONLY | source_claim | — |
| holding | 111 | PF curve point 1 target | PFlimitlinepoint1 powerfactor | register value | — | W | SOURCE_ONLY | source_claim | — |
| holding | 112 | PF curve point 2 load | 255meansnothispoint | register value | percen t | W | SOURCE_ONLY | source_claim | — |
| holding | 113 | PF curve point 2 target | PFlimitlinepoint 2powerfactor | register value | — | W | SOURCE_ONLY | source_claim | — |
| holding | 114 | PF curve point 3 load | 255meansnothispoint | register value | percen t | W | SOURCE_ONLY | source_claim | — |
| holding | 115 | PF curve point 3 target | PFlimitlinepoint3 powerfactor | register value | — | W | SOURCE_ONLY | source_claim | — |
| holding | 116 | PF curve point 4 load | 255meansnothispoint | register value | percen t | W | SOURCE_ONLY | source_claim | — |
| holding | 117 | PF curve point 4 target | PFlimitlinepoint4 powerfactor | register value | — | W | SOURCE_ONLY | source_claim | — |
| holding | 118 | Module code segments | SxxBxx | register value | — | R | SOURCE_ONLY | source_claim | — |
| holding | 119 | Module code segments | DxxTxx | register value | — | R | SOURCE_ONLY | source_claim | — |
| holding | 120 | Module code segments | PxxUxx | register value | — | R | SOURCE_ONLY | source_claim | — |
| holding | 121 | Module code segments | Mxxxx Power | register value | — | R | SOURCE_ONLY | source_claim | — |
| holding | 122 | Export limit enable mode | ExportLimitenable, 0:DisableexportLimit; 1:Enable485exportLimit; 2:Enable232exportLimit; 3:EnableCTexportLimit; | register value | — | R/W | SOURCE_ONLY | source_claim | — |
| holding | 123 | Export limit power setpoint | ExportLimitPowerRate | register value | 0.1% | R/W | SOURCE_ONLY | source_claim | — |
| holding | 124 | Tracker coupling mode | 0:Independent 1:DCSource 2:Parallel | register value | — | W | SOURCE_ONLY | source_claim | — |
| holding | 1000 | Float charge current limit i | Float charge current limit i | register value | — | W | SOURCE_ONLY | source_claim | — |
| holding | 1001 | PF CMD memory state | PF CMD memory state | register value | 0or1, | W | SOURCE_ONLY | source_claim | — |
| holding | 1002 | VbatStartF orDischarg e | VbatStartF orDischarg e | register value | — | R | SOURCE_ONLY | source_claim | — |
| holding | 1003 | VbatlowWa rnClr l | VbatlowWa rnClr l | register value | — | R | SOURCE_ONLY | source_claim | — |
| holding | 1004 | Vbatstopfo rdischarge | Vbatstopfo rdischarge | register value | — | W | SOURCE_ONLY | source_claim | — |
| holding | 1005 | Vbat stop forcharge | Shouldstopcharge whenhigherthanthis voltage | register value | 0.01V | W | SOURCE_ONLY | source_claim | — |
| holding | 1006 | Vbat start for discharge | Should not discharge when lower than this voltage | register value | 0.01V | W | SOURCE_ONLY | source_claim | — |
| holding | 1007 | Vbat constant charge | CVvoltage（acid） | register value | 0.01V | W | SOURCE_ONLY | source_claim | — |
| holding | 1008 | EESysInfo.S ysSetEn | SystemEnable | register value | — | W | SOURCE_ONLY | source_claim | — |
| holding | 1009 | Battemp lower limit d | Batterytemperature lowerlimitfordischarge | register value | 0.1℃ | W | SOURCE_ONLY | source_claim | — |
| holding | 1010 | Bat temp upper limit d | Batterytemperature upperlimitfordischarge | register value | 0.1℃ | W | SOURCE_ONLY | source_claim | — |
| holding | 1011 | Bat temp lower limit c | Lowertemperaturelimit | register value | 0.1℃ | W | SOURCE_ONLY | source_claim | — |
| holding | 1012 | Bat temp upper limit c | Uppertemperaturelimit | register value | 0.1℃ | W | SOURCE_ONLY | source_claim | — |
| holding | 1013 | uwUnderFr eDischarge DelyTime | UnderFreDelayTime | register value | 50ms | R | SOURCE_ONLY | source_claim | — |
| holding | 1014 | BatMdlSeri alNum | SPH4-11Kused | register value | — | W | SOURCE_ONLY | source_claim | — |
| holding | 1015 | BatMdlPara llNum | SPH4-11Kused | register value | — | W | SOURCE_ONLY | source_claim | — |
| holding | 1016 | DRMS_EN | 0：disable 1：enable | register value | / | R | SOURCE_ONLY | source_claim | — |
| holding | 1017 | Bat First Start Time 4 | Higheight:hours Loweight:minutes | register value | — | R | SOURCE_ONLY | source_claim | — |
| holding | 1018 | Bat First Stop Time 4 | Higheight:hours Loweight:minutes | register value | — | R | SOURCE_ONLY | source_claim | — |
| holding | 1019 | BatFirst on/off Switch4 | Batterypriorityenable1 | register value | — | R | SOURCE_ONLY | source_claim | — |
| holding | 1020 | Bat First Start Time 5 | Higheight:hours Loweight:minutes | register value | — | R | SOURCE_ONLY | source_claim | — |
| holding | 1021 | BatFirst StopTime 5 | Higheight:hours Loweight:minutes | register value | — | R | SOURCE_ONLY | source_claim | — |
| holding | 1022 | BatFirst on/off Switch5 | Batterypriorityenable1 | register value | — | R | SOURCE_ONLY | source_claim | — |
| holding | 1023 | BatFirst StartTime 6 | Higheight:hours Loweight:minutes | register value | — | R | SOURCE_ONLY | source_claim | — |
| holding | 1024 | BatFirst StopTime 6 | Higheight:hours Loweight:minutes | register value | — | R | SOURCE_ONLY | source_claim | — |
| holding | 1025 | BatFirst on/off Switch6 | Batterypriorityenable1 | register value | — | R | SOURCE_ONLY | source_claim | — |
| holding | 1026 | GridFirst StartTime | Higheight:hours Loweight:minutes | register value | — | R | SOURCE_ONLY | source_claim | — |
| holding | 1027 | GridFirst StopTime 4 | Higheight:hours Loweight:minutes | register value | — | R | SOURCE_ONLY | source_claim | — |
| holding | 1028 | Grid First Stop Switch4 | Gridpriorityenable | register value | — | R | SOURCE_ONLY | source_claim | — |
| holding | 1029 | GridFirst StartTime 5 | Higheight:hours Loweight:minutes | register value | — | R | SOURCE_ONLY | source_claim | — |
| holding | 1030 | GridFirst StopTime 5 | Higheight:hours Loweight:minutes | register value | — | R | SOURCE_ONLY | source_claim | — |
| holding | 1031 | Grid First Stop Switch5 | Gridpriorityenable | register value | — | R | SOURCE_ONLY | source_claim | — |
| holding | 1032 | GridFirst StartTime 6 | Higheight:hours Loweight:minutes | register value | — | R | SOURCE_ONLY | source_claim | — |
| holding | 1033 | GridFirst StopTime 6 | Higheight:hours Loweight:minutes | register value | — | R | SOURCE_ONLY | source_claim | — |
| holding | 1034 | Grid First Stop Switch6 | Gridpriorityenable | register value | — | R | SOURCE_ONLY | source_claim | — |
| holding | 1035 | BatFirst StartTime 4 | Higheight:hours Loweight:minutes | register value | — | R | SOURCE_ONLY | source_claim | — |
| holding | 1036 | / | Reserve | register value | / | R | SOURCE_ONLY | source_claim | — |
| holding | 1037 | bCTMode | UsetheCTModeto ChooseRFCT\Cable CT\METER | register value | — | W | SOURCE_ONLY | source_claim | — |
| holding | 1038 | CTAdjust | CTAdjustenable | register value | — | W | SOURCE_ONLY | source_claim | — |
| holding | 1039 | / | Reserve | register value | / | R | SOURCE_ONLY | source_claim | — |
| holding | 1040 | / | / | register value | — | R | SOURCE_ONLY | source_claim | — |
| holding | 1041 | / | / | register value | — | R | SOURCE_ONLY | source_claim | — |
| holding | 1042 | / | / | register value | — | R | SOURCE_ONLY | source_claim | — |
| holding | 1043 | / | / | register value | — | R | SOURCE_ONLY | source_claim | — |
| holding | 1044 | Priority | ForceChrEn/ForceDischr En Load first/bat first /grid first | register value | — | R | SOURCE_ONLY | source_claim | — |
| holding | 1045 | / | / | register value | — | R | SOURCE_ONLY | source_claim | — |
| holding | 1046 | / | / | register value | — | R | SOURCE_ONLY | source_claim | — |
| holding | 1047 | AgingTestSt ep Cmd | Commandforagingtest | register value | — | R | SOURCE_ONLY | source_claim | — |
| holding | 1048 | BatteryTyp e | Batterytypechooseof buck-boostinput | register value | — | R | SOURCE_ONLY | source_claim | — |
| holding | 1049 | / | / | register value | — | R | SOURCE_ONLY | source_claim | — |
| holding | 1050 | / | / | register value | — | R | SOURCE_ONLY | source_claim | — |
| holding | 1051 | / | / | register value | — | R | SOURCE_ONLY | source_claim | — |
| holding | 1052 | / | / | register value | — | R | SOURCE_ONLY | source_claim | — |
| holding | 1053 | / | / | register value | — | R | SOURCE_ONLY | source_claim | — |
| holding | 1054 | / | / | register value | — | R | SOURCE_ONLY | source_claim | — |
| holding | 1055 | Register 1055 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| holding | 1056 | Register 1056 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| holding | 1057 | Register 1057 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| holding | 1058 | Register 1058 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| holding | 1059 | Register 1059 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| holding | 1060 | BuckUpsFunE n | 0:disable 1:enable | register value | — | R | SOURCE_ONLY | source_claim | — |
| holding | 1061 | BuckUPSVoltS et | UPSoutputvoltage | register value | — | R | SOURCE_ONLY | source_claim | — |
| holding | 1062 | UPSFreqSet | UPSoutputfrequency | register value | — | R | SOURCE_ONLY | source_claim | — |
| holding | 1063 | Register 1063 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| holding | 1064 | Register 1064 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| holding | 1065 | Register 1065 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| holding | 1066 | Register 1066 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| holding | 1067 | Register 1067 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| holding | 1068 | Register 1068 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| holding | 1069 | Register 1069 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| holding | 1070 | Grid-first discharge limit | Discharge Power Rate whenGridFirst | register value | 1% | R/W | SOURCE_ONLY | source_claim | — |
| holding | 1071 | Grid-first stop SOC | Stop Discharge soc when GridFirst | register value | 1% | R/W | SOURCE_ONLY | source_claim | — |
| holding | 1072 | / | / | register value | / | R | SOURCE_ONLY | source_claim | — |
| holding | 1073 | / | / | register value | / | R | SOURCE_ONLY | source_claim | — |
| holding | 1074 | / | / | register value | / | R | SOURCE_ONLY | source_claim | — |
| holding | 1075 | / | / | register value | / | R | SOURCE_ONLY | source_claim | — |
| holding | 1076 | / | / | register value | / | R | SOURCE_ONLY | source_claim | — |
| holding | 1077 | / | / | register value | / | R | SOURCE_ONLY | source_claim | — |
| holding | 1078 | / | / | register value | / | R | SOURCE_ONLY | source_claim | — |
| holding | 1079 | / | / | register value | / | R | SOURCE_ONLY | source_claim | — |
| holding | 1080 | Grid-first slot 1 start | High byte = hour (0-23); low byte = minute (0-59). | register value | hh:mm | R/W | SOURCE_ONLY | source_claim | — |
| holding | 1081 | Grid-first slot 1 stop | High byte = hour (0-23); low byte = minute (0-59). | register value | hh:mm | R/W | SOURCE_ONLY | source_claim | — |
| holding | 1082 | Grid-first slot 1 enable | Enable:1 Disable:0 | register value | — | R/W | SOURCE_ONLY | source_claim | — |
| holding | 1083 | Grid-first slot 2 start | High byte = hour (0-23); low byte = minute (0-59). | register value | hh:mm | R/W | SOURCE_ONLY | source_claim | — |
| holding | 1084 | Grid-first slot 2 stop | High byte = hour (0-23); low byte = minute (0-59). | register value | hh:mm | R/W | SOURCE_ONLY | source_claim | — |
| holding | 1085 | Grid-first slot 2 enable | When set from the LCD, this slot can be tied to the Force Discharge command. | register value | — | R/W | SOURCE_ONLY | source_claim | — |
| holding | 1086 | Grid-first slot 3 start | High byte = hour (0-23); low byte = minute (0-59). | register value | hh:mm | R/W | SOURCE_ONLY | source_claim | — |
| holding | 1087 | Grid-first slot 3 stop | High byte = hour (0-23); low byte = minute (0-59). | register value | hh:mm | R/W | SOURCE_ONLY | source_claim | — |
| holding | 1088 | Grid-first slot 3 enable | Enable:1 Disable:0 | register value | — | R/W | SOURCE_ONLY | source_claim | — |
| holding | 1089 | / | / | register value | / | R | SOURCE_ONLY | source_claim | — |
| holding | 1090 | Battery-first charge limit | Charge Power Rate when BatFirst | register value | 1% | R/W | SOURCE_ONLY | source_claim | — |
| holding | 1091 | Battery-first stop SOC | Stop Charge soc when Bat First | register value | 1% | R/W | SOURCE_ONLY | source_claim | — |
| holding | 1092 | Battery-first AC charge enable | WhenBatFirst Enable:1 Disable:0 | register value | — | R/W | RESOLVED | semantic_correlated, source_claim | — |
| holding | 1093 | Register 1093 | — | register value | — | R | UNKNOWN_RESERVED | source_claim | — |
| holding | 1094 | Register 1094 | — | register value | — | R | UNKNOWN_RESERVED | source_claim | — |
| holding | 1095 | Register 1095 | — | register value | — | R | UNKNOWN_RESERVED | source_claim | — |
| holding | 1096 | Register 1096 | — | register value | — | R | UNKNOWN_RESERVED | source_claim | — |
| holding | 1097 | Register 1097 | — | register value | — | R | UNKNOWN_RESERVED | source_claim | — |
| holding | 1098 | Register 1098 | — | register value | — | R | UNKNOWN_RESERVED | source_claim | — |
| holding | 1099 | Register 1099 | — | register value | — | R | UNKNOWN_RESERVED | source_claim | — |
| holding | 1100 | Battery-first slot 1 start | High byte = hour (0-23); low byte = minute (0-59). | register value | hh:mm | R/W | SOURCE_ONLY | source_claim | — |
| holding | 1101 | Battery-first slot 1 stop | High byte = hour (0-23); low byte = minute (0-59). | register value | hh:mm | R/W | SOURCE_ONLY | source_claim | — |
| holding | 1102 | Battery-first slot 1 enable | Enable:1 Disable:0 | register value | — | R/W | SOURCE_ONLY | source_claim | — |
| holding | 1103 | Battery-first slot 2 start | High byte = hour (0-23); low byte = minute (0-59). | register value | hh:mm | R/W | SOURCE_ONLY | source_claim | — |
| holding | 1104 | Battery-first slot 2 stop | High byte = hour (0-23); low byte = minute (0-59). | register value | hh:mm | R/W | SOURCE_ONLY | source_claim | — |
| holding | 1105 | Battery-first slot 2 enable | Enable:1 Disable:0 | register value | — | R/W | SOURCE_ONLY | source_claim | — |
| holding | 1106 | Battery-first slot 3 start | High byte = hour (0-23); low byte = minute (0-59). | register value | hh:mm | R/W | SOURCE_ONLY | source_claim | — |
| holding | 1107 | Battery-first slot 3 stop | High byte = hour (0-23); low byte = minute (0-59). | register value | hh:mm | R/W | SOURCE_ONLY | source_claim | — |
| holding | 1108 | Battery-first slot 3 enable | Enable:1 Disable:0 | register value | — | R/W | SOURCE_ONLY | source_claim | — |
| holding | 1109 | / | reserve | register value | / | R | SOURCE_ONLY | source_claim | — |
| holding | 1110 | Load-first slot 1 start | SPA/reserve | register value | hh:mm | R/W | SOURCE_ONLY | source_claim | — |
| holding | 1111 | Load-first slot 1 stop | SPA/reserve | register value | hh:mm | R/W | SOURCE_ONLY | source_claim | — |
| holding | 1112 | Load-first slot 1 enable | SPA/reserve | register value | — | R/W | SOURCE_ONLY | source_claim | — |
| holding | 1113 | Load-first slot 2 start | SPA/reserve | register value | hh:mm | R/W | SOURCE_ONLY | source_claim | — |
| holding | 1114 | Load-first slot 2 stop | SPA/reserve | register value | hh:mm | R/W | SOURCE_ONLY | source_claim | — |
| holding | 1115 | Load-first slot 2 enable | SPA/reserve | register value | — | R/W | SOURCE_ONLY | source_claim | — |
| holding | 1116 | Load-first slot 3 start | SPA/reserve | register value | hh:mm | R/W | SOURCE_ONLY | source_claim | — |
| holding | 1117 | Load-first slot 3 stop | SPA/reserve | register value | hh:mm | R/W | SOURCE_ONLY | source_claim | — |
| holding | 1118 | Load-first slot 3 enable | SPA/reserve | register value | — | R/W | SOURCE_ONLY | source_claim | — |
| holding | 1119 | Energy calculation formula | 0：Theoldformula 1 ： The new formula | register value | / | R/W | SOURCE_ONLY | source_claim | — |
| holding | 1120 | Backup enable | MIXUS | register value | — | R/W | SOURCE_ONLY | source_claim | — |
| holding | 1121 | SGIP enable | MIXUS | register value | — | R/W | SOURCE_ONLY | source_claim | — |
| holding | 1122 | Register 1122 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| holding | 1123 | Register 1123 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| holding | 1124 | Register 1124 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| input | 0 | Inverter status | InverterStatus | register value; /10 | — | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 1 | PV input power | PpvH | register value; /10 | 0.1W | R/W | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 2 | PV input power | PpvL | register value; /10 | 0.1W | R/W | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 3 | PV1 DC voltage | Vpv1 | register value; /10 | 0.1V | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 4 | PV1 DC current | PV1Curr | register value; /10 | 0.1A | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 5 | PV1 DC power | Ppv1H | register value; /10 | 0.1W | R/W | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 6 | PV1 DC power | Ppv1L | register value; /10 | 0.1W | R/W | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 7 | PV2 DC voltage | Vpv2 | register value; /10 | 0.1V | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 8 | PV2 DC current | PV2Curr | register value; /10 | 0.1A | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 9 | PV2 DC power | Ppv2H | register value; /10 | 0.1W | R/W | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 10 | PV2 DC power | Ppv2L | register value; /10 | 0.1W | R/W | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 11 | PV3 DC voltage | Vpv3 | register value; /10 | 0.1V | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 12 | PV3 DC current | PV3Curr | register value; /10 | 0.1A | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 13 | PV3 DC power | Ppv3H | register value; /10 | 0.1W | R/W | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 14 | PV3 DC power | Ppv3L | register value; /10 | 0.1W | R/W | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 15 | PV4 DC voltage | Vpv4 | register value; /10 | 0.1V | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 16 | PV4 DC current | PV4Curr | register value; /10 | 0.1A | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 17 | PV4 DC power | Ppv4H | register value; /10 | 0.1W | R/W | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 18 | PV4 DC power | Ppv4L | register value; /10 | 0.1W | R/W | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 19 | PV5 DC voltage | Vpv5 | register value; /10 | 0.1V | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 20 | PV5 DC current | PV5Curr | register value; /10 | 0.1A | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 21 | PV5 DC power | Ppv5H | register value; /10 | 0.1W | R/W | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 22 | PV5 DC power | Ppv5L | register value; /10 | 0.1W | R/W | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 23 | PV6 DC voltage | Vpv6 | register value; /10 | 0.1V | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 24 | PV6 DC current | PV6Curr | register value; /10 | 0.1A | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 25 | PV6 DC power | PV6inputpower(high) | register value; /10 | W | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 26 | PV6 DC power | PV6inputpower(low) | register value; /10 | W | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 27 | PV7 DC voltage | PV7voltage | register value; /10 | V | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 28 | PV7 DC current | PV7inputcurrent | register value; /10 | A | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 29 | PV7 DC power | PV7inputpower(high) | register value; /10 | W | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 30 | PV7 DC power | PV7inputpower(low) | register value; /10 | W | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 31 | PV8 DC voltage | PV8voltage | register value; /10 | V | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 32 | PV8 DC current | PV8inputcurrent | register value; /10 | A | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 33 | PV8 DC power | PV8inputpower(high) | register value; /10 | W | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 34 | PV8 DC power | PV8inputpower(low) | register value; /10 | W | R | RESOLVED | semantic_correlated, source_claim | — |
| input | 35 | AC output power | Outputpower(high) | register value; /10 | W | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 36 | AC output power | Outputpower(low) | register value; /10 | W | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 37 | Grid frequency | Gridfrequency | register value; /100 | Hz | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 38 | AC phase L1 voltage | Three/singlephasegridvoltage | register value; /10 | V | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 39 | AC phase L1 current | Three/singlephasegridoutputcurrent | register value; /10 | A | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 40 | AC phase L1 power | Three/single phase grid output watt VA(high) | register value; /10 | W | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 41 | AC phase L1 power | Three/single phase grid output watt VA(low) | register value; /10 | W | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 42 | AC phase L2 voltage | Threephasegridvoltage | register value; /10 | V | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 43 | AC phase L2 current | Threephasegridoutputcurrent | register value; /10 | A | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 44 | AC phase L2 power | Threephasegridoutputpower(high) | register value; /10 | W | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 45 | AC phase L2 power | Threephasegridoutputpower(low) | register value; /10 | W | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 46 | AC phase L3 voltage | Threephasegridvoltage | register value; /10 | V | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 47 | AC phase L3 current | Threephasegridoutputcurrent | register value; /10 | A | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 48 | AC phase L3 power | Threephasegridoutputpower(high) | register value; /10 | W | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 49 | AC phase L3 power | Threephasegridoutputpower(low) | register value; /10 | W | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 50 | Vac_RS | Threephasegridvoltage | register value | Linevoltage | R | RESOLVED | semantic_correlated, source_claim | — |
| input | 51 | Vac_ST | Threephasegridvoltage | register value | Linevoltage | R | RESOLVED | semantic_correlated, source_claim | — |
| input | 52 | Vac_TR | Threephasegridvoltage | register value | Linevoltage | R | RESOLVED | semantic_correlated, source_claim | — |
| input | 53 | Output energy today | Todaygenerateenergy(high) | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 54 | Output energy today | Todaygenerateenergy(low) | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 55 | Output energy total | Totalgenerateenergy(high) | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 56 | Output energy total | Totalgenerateenergy(low) | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 57 | Run time | Raw counter counts seconds; divide by 7200 to obtain hours. | register value; /7200 | h | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 58 | Run time | Raw counter counts seconds; divide by 7200 to obtain hours. | register value; /7200 | h | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 59 | PV1 energy today | PV1Energytoday(high) | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 60 | PV1 energy today | PV1Energytoday(low) | register value; /10 | kWh | R | RESOLVED | semantic_correlated, source_claim | — |
| input | 61 | PV1 energy total | PV1Energytotal(high) | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 62 | PV1 energy total | PV1Energytotal(low) | register value; /10 | kWh | R | RESOLVED | semantic_correlated, source_claim | — |
| input | 63 | PV2 energy today | PV2Energytoday(high) | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 64 | PV2 energy today | PV2Energytoday(low) | register value; /10 | kWh | R | RESOLVED | semantic_correlated, source_claim | — |
| input | 65 | PV2 energy total | PV2Energytotal(high) | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 66 | PV2 energy total | PV2Energytotal(low) | register value; /10 | kWh | R | RESOLVED | semantic_correlated, source_claim | — |
| input | 67 | PV3 energy today | PV3Energytoday(high) | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 68 | PV3 energy today | PV3Energytoday(low) | register value; /10 | kWh | R | RESOLVED | semantic_correlated, source_claim | — |
| input | 69 | PV3 energy total | PV3Energytotal(high) | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 70 | PV3 energy total | PV3Energytotal(low) | register value; /10 | kWh | R | RESOLVED | semantic_correlated, source_claim | — |
| input | 71 | PV4 energy today | PV4Energytoday(high) | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 72 | PV4 energy today | PV4Energytoday(low) | register value; /10 | kWh | R | RESOLVED | semantic_correlated, source_claim | — |
| input | 73 | PV4 energy total | PV4Energytotal(high) | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 74 | PV4 energy total | PV4Energytotal(low) | register value; /10 | kWh | R | RESOLVED | semantic_correlated, source_claim | — |
| input | 75 | PV5 energy today | PV5Energytoday(high) | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 76 | PV5 energy today | PV5Energytoday(low) | register value; /10 | kWh | R | RESOLVED | semantic_correlated, source_claim | — |
| input | 77 | PV5 energy total | PV5Energytotal(high) | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 78 | PV5 energy total | PV5Energytotal(low) | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 79 | PV6 energy today | PV6Energytoday(high) | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 80 | PV6 energy today | PV6Energytoday(low) | register value; /10 | kWh | R | RESOLVED | semantic_correlated, source_claim | — |
| input | 81 | PV6 energy total | PV6Energytotal(high) | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 82 | PV6 energy total | PV6Energytotal(low) | register value; /10 | kWh | R | RESOLVED | semantic_correlated, source_claim | — |
| input | 83 | PV7 energy today | PV7Energytoday(high) | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 84 | PV7 energy today | PV7Energytoday(low) | register value; /10 | kWh | R | RESOLVED | semantic_correlated, source_claim | — |
| input | 85 | PV7 energy total | PV7Energytotal(high) | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 86 | PV7 energy total | PV7Energytotal(low) | register value; /10 | kWh | R | RESOLVED | semantic_correlated, source_claim | — |
| input | 87 | PV8 energy today | PV8Energytoday(high) | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 88 | PV8 energy today | PV8Energytoday(low) | register value; /10 | kWh | R | RESOLVED | semantic_correlated, source_claim | — |
| input | 89 | PV8 energy total | PV8Energytotal(high) | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 90 | PV8 energy total | PV8Energytotal(low) | register value; /10 | kWh | R | RESOLVED | semantic_correlated, source_claim | — |
| input | 91 | PV energy total | PVEnergytotal(high) | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 92 | PV energy total | PVEnergytotal(low) | register value; /10 | kWh | R | RESOLVED | semantic_correlated, source_claim | — |
| input | 93 | Inverter temperature | Invertertemperature | register value; /10 | °C | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 94 | IPM temperature | TheinsideIPMininverterTemperature | register value; /10 | °C | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 95 | Boost temperature | Boosttemperature | register value; /10 | °C | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 96 | Temp4 | Temp4 | register value | reserved | R | SOURCE_ONLY | source_claim | — |
| input | 97 | uwBatVolt_DSP | BatVolt_DSP | register value | BatVolt(DSP) | R | SOURCE_ONLY | source_claim | — |
| input | 98 | P-bus voltage | PBusinsideVoltage | register value; /10 | V | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 99 | N-bus voltage | NBusinsideVoltage | register value; /10 | V | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 100 | IPF | InverteroutputPFnow | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 101 | Output power percentage | RealOutputpowerPercent | register value; /10 | % | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 102 | OPFullwattH | OutputMaxpowerLimitedhigh | register value | W | R | RESOLVED | semantic_correlated, source_claim | — |
| input | 103 | OPFullwattL | OutputMaxpowerLimitedlow | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 104 | Derating mode | DeratingMode | register value; /10 | — | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 105 | Fault code | Inverterfaultmaincode | register value; /10 | — | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 106 | Register 106 | — | register value | — | R | UNKNOWN_RESERVED | source_claim | — |
| input | 107 | FaultSubcode | Inverterfaultsubcode | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 108 | RemoteCtrlEn | / | register value | StoragePow er(SPA) | R | SOURCE_ONLY | source_claim | — |
| input | 109 | RemoteCtrlPow er | / | register value | StoragePow er(SPA) | R | SOURCE_ONLY | source_claim | — |
| input | 110 | Warning code | WarningbitH | register value; /10 | — | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 111 | Warning code | Inverterwarnsubcode | register value; /10 | — | R | SOURCE_ONLY | source_claim | — |
| input | 112 | WarnMaincode | Inverterwarnmaincode | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 113 | real Power Percent | realPowerPercent | register value | MAX | R | SOURCE_ONLY | source_claim | — |
| input | 114 | inv start delay time | invstartdelaytime | register value | MAX | R | SOURCE_ONLY | source_claim | — |
| input | 115 | bINVAllFaultCod e | bINVAllFaultCode | register value | MAX | R | SOURCE_ONLY | source_claim | — |
| input | 116 | AC charge Power_H | Gridpowertolocalload | register value | Storage Power | R | SOURCE_ONLY | source_claim | — |
| input | 117 | AC charge Power_L | Gridpowertolocalload | register value | Storage Power | R | SOURCE_ONLY | source_claim | — |
| input | 118 | Priority | 0:LoadFirst | register value | Storage | R | RESOLVED | semantic_correlated, source_claim | — |
| input | 119 | BatteryType | 0：Lead-acid 1：Lithiumbattery | register value | — | R | RESOLVED | semantic_correlated, source_claim | — |
| input | 120 | AutoProofreadC MD | Aging mode Auto-calibration command | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 121 | Register 121 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| input | 122 | Register 122 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| input | 123 | Register 123 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| input | 124 | reserved | reserved | register value | — | R | UNKNOWN_RESERVED | source_claim | — |
| input | 1000 | uwSysWorkMode | uwSysWorkMode | register value | — | W | SOURCE_ONLY | source_claim | — |
| input | 1001 | Systemfaultword0 | Systemfaultword0 | register value | Please refer to thefault description of Hybrid | R | SOURCE_ONLY | source_claim | — |
| input | 1002 | Systemfaultword1 | Systemfaultword1 | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 1003 | Systemfaultword2 | Systemfaultword2 | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 1004 | Systemfaultword3 | Systemfaultword3 | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 1005 | Systemfaultword4 | Systemfaultword4 | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 1006 | Systemfaultword5 | Systemfaultword5 | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 1007 | Systemfaultword6 | Systemfaultword6 | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 1008 | Systemfaultword7 | Systemfaultword7 | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 1009 | Pdischarge1H | Dischargepower(high) | register value; /10 | W | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 1010 | Pdischarge1L | Dischargepower(low) | register value; /10 | W | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 1011 | Pcharge1H | Chargepower(high) | register value; /10 | W | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 1012 | Pcharge1L | Chargepower(low) | register value; /10 | W | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 1013 | Vbat | Batteryvoltage | register value | V | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 1014 | SOC | StateofchargeCapacity | register value; /10 | lith/leadacid | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 1015 | PactouserR H | ACpowertouserH | register value | W | R | RESOLVED | semantic_correlated, source_claim | — |
| input | 1016 | PactouserR L | ACpowertouserL | register value | W | R | RESOLVED | semantic_correlated, source_claim | — |
| input | 1017 | PactouserS H | PactouserS H | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 1018 | PactouserS L | PactouserS L | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 1019 | PactouserT H | PactouserT H | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 1020 | PactouserT L | PactouserT H | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 1021 | PactouserTotalH | ACpowertousertotalH | register value; /10 | W | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 1022 | PactouserTotalL | ACpowertousertotalL | register value; /10 | W | R | RESOLVED | semantic_correlated, source_claim | — |
| input | 1023 | PactogridR H | ACpowertogridH | register value | Ac output | R | RESOLVED | semantic_correlated, source_claim | — |
| input | 1024 | PactogridR L | ACpowertogridL | register value | W | R | RESOLVED | semantic_correlated, source_claim | — |
| input | 1025 | PactogridS H | PactogridS H | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 1026 | PactogridS L | PactogridS L | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 1027 | PactogridTH | 0.1w | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 1028 | PactogridTL | 0.1w | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 1029 | pac_to_grid_total | 0.1w | register value; /10 | W | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 1030 | PactogridtotalL | 0.1w | register value; /10 | W | R | RESOLVED | semantic_correlated, source_claim | — |
| input | 1031 | PLocalLoadR H | 0.1w | register value | W | R | RESOLVED | semantic_correlated, source_claim | — |
| input | 1032 | PLocalLoadR L | 0.1w | register value | W | R | RESOLVED | semantic_correlated, source_claim | — |
| input | 1033 | PLocalLoadS H | 0.1w | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 1034 | PLocalLoadS L | 0.1w | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 1035 | PLocalLoadT H | 0.1w | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 1036 | PLocalLoadT L | 0.1w | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 1037 | PLocalLoadtotalH | 0.1w | register value | W | R | RESOLVED | semantic_correlated, source_claim | — |
| input | 1038 | PLocalLoadtotalL | 0.1w | register value | W | R | RESOLVED | semantic_correlated, source_claim | — |
| input | 1039 | IP2MTemperature | 0.1℃ | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 1040 | B2attery Temperature | 0.1℃ | register value | °C | R | RESOLVED | semantic_correlated, source_claim | — |
| input | 1041 | SPDSPStatus | SPDSPStatus | register value | — | R | RESOLVED | semantic_correlated, source_claim | — |
| input | 1042 | SPBusVolt | 0.1V | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 1043 | Register 1043 | — | register value | — | R | UNKNOWN_RESERVED | source_claim | — |
| input | 1044 | Etouser_todayH | Etouser_todayH | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 1045 | Etouser_todayL | Etouser_todayL | register value; /10 | kWh | W | RESOLVED | semantic_correlated, source_claim | — |
| input | 1046 | Etouser_totalH | Etouser_totalH | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 1047 | Etouser_totalL | Etouser_totalL | register value; /10 | kWh | R | RESOLVED | semantic_correlated, source_claim | — |
| input | 1048 | Etogrid_todayH | Etogrid_todayH | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 1049 | Etogrid_todayL | Etogrid_todayL | register value; /10 | kWh | W | RESOLVED | semantic_correlated, source_claim | — |
| input | 1050 | Etogrid_totalH | Etogrid_totalH | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 1051 | Etogrid_totalL | Etogrid_totalL | register value; /10 | kWh | R | RESOLVED | semantic_correlated, source_claim | — |
| input | 1052 | Edischarge1_toda yH | Edischarge1_toda yH | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 1053 | Edischarge1_toda yL | Edischarge1_toda yL | register value; /10 | kWh | R | RESOLVED | semantic_correlated, source_claim | — |
| input | 1054 | Edischarge1_total H | Edischarge1_total H | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 1055 | Edischarge1_total L | Edischarge1_total L | register value; /10 | kWh | W | RESOLVED | semantic_correlated, source_claim | — |
| input | 1056 | Echarge1_todayH | Echarge1_todayH | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 1057 | Echarge1_today L | Echarge1_today L | register value; /10 | kWh | R | RESOLVED | semantic_correlated, source_claim | — |
| input | 1058 | Echarge1_totalH | Echarge1_totalH | register value; /10 | kWh | R | RESOLVED_WITH_NOTES | semantic_correlated, source_claim | Source datatype catalogue contains conflicting or incomplete fields; the selected interpretation is retained with alternatives. |
| input | 1059 | Echarge1_totalL | Echarge1_totalL | register value; /10 | kWh | R | RESOLVED | semantic_correlated, source_claim | — |
| input | 1060 | Register 1060 | Localloadenergytoday | register value | kWh | R | UNKNOWN_RESERVED | semantic_correlated, source_claim | — |
| input | 1061 | Register 1061 | Localloadenergytoday | register value | kWh | R | UNKNOWN_RESERVED | semantic_correlated, source_claim | — |
| input | 1062 | Register 1062 | Localloadenergytotal | register value | kWh | R | UNKNOWN_RESERVED | semantic_correlated, source_claim | — |
| input | 1063 | Register 1063 | Localloadenergytotal | register value | kWh | R | UNKNOWN_RESERVED | semantic_correlated, source_claim | — |
| input | 1064 | Register 1064 | ExportLimitApparentPowerH | register value | — | W | UNKNOWN_RESERVED | source_claim | — |
| input | 1065 | Register 1065 | ExportLimitApparentPowerL | register value | — | W | UNKNOWN_RESERVED | source_claim | — |
| input | 1066 | Register 1066 | / | register value | — | R | UNKNOWN_RESERVED | source_claim | — |
| input | 1067 | EpsFac | UPSfrequency | register value | — | R | RESOLVED | semantic_correlated, source_claim | — |
| input | 1068 | EpsVac1 | UPSphaseRoutputvoltage | register value | — | R | RESOLVED | semantic_correlated, source_claim | — |
| input | 1069 | EpsIac1 | UPSphaseRoutputcurrent | register value | — | R | RESOLVED | semantic_correlated, source_claim | — |
| input | 1070 | EpsPac1 | UPSphaseRoutputpower(H) | register value | — | R | RESOLVED | semantic_correlated, source_claim | — |
| input | 1071 | EpsPac1 | UPSphaseRoutputpower(L) | register value | — | R | RESOLVED | semantic_correlated, source_claim | — |
| input | 1072 | EpsVac2 | UPSphaseSoutputvoltage | register value | — | R | RESOLVED | semantic_correlated, source_claim | — |
| input | 1073 | EpsIac2 | UPSphaseSoutputcurrent | register value | — | R | RESOLVED | semantic_correlated, source_claim | — |
| input | 1074 | EpsPac2 | UPSphaseSoutputpower(H) | register value | — | R | RESOLVED | semantic_correlated, source_claim | — |
| input | 1075 | EpsPac2 | UPSphaseSoutputpower(L) | register value | — | R | RESOLVED | semantic_correlated, source_claim | — |
| input | 1076 | EpsVac3 | UPSphaseToutputvoltage | register value | — | R | RESOLVED | semantic_correlated, source_claim | — |
| input | 1077 | EpsIac3 | UPSphaseToutputcurrent | register value | — | R | RESOLVED | semantic_correlated, source_claim | — |
| input | 1078 | EpsPac3 | UPSphaseToutputpower(H) | register value | — | R | RESOLVED | semantic_correlated, source_claim | — |
| input | 1079 | EpsPac3 | UPSphaseToutputpower(L) | register value | — | R | RESOLVED | semantic_correlated, source_claim | — |
| input | 1080 | EpsLoadPercent | LoadpercentofUPSouput | register value | — | R | RESOLVED | semantic_correlated, source_claim | — |
| input | 1081 | EpsPF | Powerfactor | register value | — | R | RESOLVED | semantic_correlated, source_claim | — |
| input | 1082 | Register 1082 | StatusOldfromBMS | register value | — | R | UNKNOWN_RESERVED | source_claim | — |
| input | 1083 | Register 1083 | StatusfromBMS | register value | — | R | UNKNOWN_RESERVED | source_claim | — |
| input | 1084 | Register 1084 | ErrorinfoOldfromBMS | register value | — | R | UNKNOWN_RESERVED | source_claim | — |
| input | 1085 | Register 1085 | ErrorinfomationfromBMS | register value | — | R | UNKNOWN_RESERVED | source_claim | — |
| input | 1086 | Register 1086 | SOCfromBMS | register value | — | R | UNKNOWN_RESERVED | source_claim | — |
| input | 1087 | Register 1087 | BatteryvoltagefromBMS | register value | — | R | UNKNOWN_RESERVED | source_claim | — |
| input | 1088 | Register 1088 | BatterycurrentfromBMS | register value | — | R | UNKNOWN_RESERVED | source_claim | — |
| input | 1089 | Register 1089 | BatterytemperaturefromBMS | register value | — | R | UNKNOWN_RESERVED | source_claim | — |
| input | 1090 | BMS_MaxCurr | Max. charge/discharge current fromBMS(pylon) | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 1091 | BMS_GaugeRM | GaugeRMfromBMS | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 1092 | BMS_GaugeFCC | GaugeFCCfromBMS | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 1093 | BMS_FW | BMS_FW | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 1094 | BMS_DeltaVolt | DeltaVfromBMS | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 1095 | BMS_CycleCnt | CycleCountfromBMS | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 1096 | BMS_SOH | SOHfromBMS | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 1097 | BMS_ConstantV olt | CVvoltagefromBMS | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 1098 | BMS_WarnInfoO ld | WarninginfooldfromBMS | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 1099 | BMS_WarnInfo | WarninginfofromBMS | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 1100 | BMS_GaugeICCu rr | GaugeICcurrentfromBMS | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 1101 | BMS_MCUVersi on | MCUSoftwareversionfromBMS | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 1102 | BMS_GaugeVers ion | GaugeVersionfromBMS | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 1103 | BMS_wGaugeFR Version_L | GaugeFRVersionL16fromBMS | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 1104 | BMS_wGaugeFR Version_H | GaugeFRVersionH16fromBMS | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 1105 | BMS_BMSInfo | BMSInformationfromBMS | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 1106 | BMS_PackInfo | PackInformationfromBMS | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 1107 | BMS_UsingCap | UsingCapfromBMS | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 1108 | uwMaxCellVolt | Maximumsinglebatteryvoltage | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 1109 | uwMinCellVolt | Lowestsinglebatteryvoltage | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 1110 | bModuleNum | Batteryparallelnumber | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 1111 | Numberofbatteries | Numberofbatteries | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 1112 | uwMaxVoltCellN o | MaxVoltCellNo | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 1113 | uwMinVoltCellN o | MinVoltCellNo | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 1114 | uwMaxTemprCe ll_10T | MaxTemprCell_10T | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 1115 | uwMinTemprCel l_10T | MinTemprCell_10T | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 1116 | uwMaxTemprCe llNo | MaxVoltTemprCellNo | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 1117 | uwMinTemprCel | MinVoltTemprCellNo | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 1118 | ProtectpackID | FaultyBatteryAddress | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 1119 | MaxSOC | ParallelmaximumSOC | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 1120 | MinSOC | ParallelminimumSOC | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 1121 | BMS_Error2 | BatteryProtection2 | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 1122 | BMS_Error3 | BatteryProtection3 | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 1123 | BMS_WarnInfo2 | BatteryWarn2 | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 1124 | ACCharge EnergyTodayH | ACChargeEnergytoday | register value | kWh | W | RESOLVED | semantic_correlated, source_claim | — |
| input | 1125 | ACCharge EnergyTodayL | ACChargeEnergytoday | register value | kWh | W | RESOLVED | semantic_correlated, source_claim | — |
| input | 1126 | A1CCharge EnergyTotalH | A1CCharge EnergyTotalH | register value | kWh | R | RESOLVED | semantic_correlated, source_claim | — |
| input | 1127 | ACCharge EnergyTotalL | ACCharge EnergyTotalL | register value | kWh | R | RESOLVED | semantic_correlated, source_claim | — |
| input | 1128 | AC Charge Power H | ACChargePower | register value | — | W | SOURCE_ONLY | source_claim | — |
| input | 1129 | AC Charge PowerL | ACChargePower | register value | — | W | SOURCE_ONLY | source_claim | — |
| input | 1130 | 70% INV Power adjust | uwGridPower_70_AdjEE_SP | register value | — | W | SOURCE_ONLY | source_claim | — |
| input | 1131 | Extra AC Power to grid_H | ExtrainverteACPowertogrid High | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 1132 | Extra AC Power to grid_L | ExtrainverteACPowertogridLow | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 1133 | Eextra_todayH | ExtrainverterPowerTOUser_Extra today(high) | register value | 0.1kWh | R | SOURCE_ONLY | source_claim | — |
| input | 1134 | Eextra_todayL | ExtrainverterPowerTOUser_Extra today(low) | register value | 0.1kWh | R | SOURCE_ONLY | source_claim | — |
| input | 1135 | Eextra_totalH | ExtrainverterPowerTOUser_Extra total(high) | register value | 0.1kWh | R | SOURCE_ONLY | source_claim | — |
| input | 1136 | Eextra_totalL | ExtrainverterPowerTOUser_Extra total(low) | register value | 0.1kWh | R | SOURCE_ONLY | source_claim | — |
| input | 1137 | Esystem_today H | SystemelectricenergytodayH | register value | 0.1kWh | R | SOURCE_ONLY | source_claim | — |
| input | 1138 | Esystem_ today L | SystemelectricenergytodayL | register value | SPA used System electric energytodayL | R | SOURCE_ONLY | source_claim | — |
| input | 1139 | Esystem_totalH | SystemelectricenergytotalH | register value | SPA used System electric energytotalH | R | SOURCE_ONLY | source_claim | — |
| input | 1140 | Esystem_totalL | SystemelectricenergytotalL | register value | SPA used System electric energytotalL | R | SOURCE_ONLY | source_claim | — |
| input | 1141 | Eself_todayH | selfelectricenergytodayH | register value | self electric energytodayH | R | SOURCE_ONLY | source_claim | — |
| input | 1142 | Eself_todayL | selfelectricenergytodayL | register value | self electric energytodayL | R | SOURCE_ONLY | source_claim | — |
| input | 1143 | Eself_totalH | selfelectricenergytotalH | register value | self electric energytotalH | R | SOURCE_ONLY | source_claim | — |
| input | 1144 | Eself_totalL | selfelectricenergytotalL | register value | self electric energytotalL | R | SOURCE_ONLY | source_claim | — |
| input | 1145 | PSystemH | SystempowerH | register value | SystempowerH | R | SOURCE_ONLY | source_claim | — |
| input | 1146 | PSystemL | SystempowerL | register value | SystempowerL | R | SOURCE_ONLY | source_claim | — |
| input | 1147 | PSelfH | selfpowerH | register value | selfpowerH | R | SOURCE_ONLY | source_claim | — |
| input | 1148 | PSelfL | selfpowerL | register value | selfpowerL | R | SOURCE_ONLY | source_claim | — |
| input | 1149 | EPVAll_TodayH | PVelectricenergytodayH | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 1150 | EPVAll_TodayL | PVelectricenergytodayL | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 1151 | AcDischarge PackSn | Discharge power pack serial number | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 1152 | Accdischarge power_H | Cumulative discharge power high 16-bitbyte | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 1153 | Accdischarge power_L | Cumulative discharge power low 16-bitbyte | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 1154 | AccCharge PackSn | chargepowerpackserialnumber | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 1155 | AccCharge power_H | Cumulative charge power high 16-bitbyte | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 1156 | AccCharge power_L | Cumulative charge power low 16-bitbyte | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 1157 | FirstBattFaultSn | FirstBattFaultSn | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 1158 | Second BattFaultSn | Second BattFaultSn | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 1159 | Third BattFaultSn | Third BattFaultSn | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 1160 | Fourth BattFaultSn | Fourth BattFaultSn | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 1161 | Batteryhistory faultcode1 | Batteryhistoryfaultcode1 | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 1162 | Batteryhistory faultcode2 | Batteryhistoryfaultcode2 | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 1163 | Batteryhistory faultcode3 | Batteryhistoryfaultcode3 | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 1164 | Batteryhistory faultcode4 | Batteryhistoryfaultcode4 | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 1165 | Batteryhistory faultcode5 | Batteryhistoryfaultcode5 | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 1166 | Batteryhistory faultcode6 | Batteryhistoryfaultcode6 | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 1167 | Batteryhistory faultcode7 | Batteryhistoryfaultcode7 | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 1168 | Batteryhistory faultcode8 | Batteryhistoryfaultcode8 | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 1169 | Number of battery codes | Number of battery codes PACK number + BIC forward and reversecodes | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 1170 | Register 1170 | — | register value | — | R | UNKNOWN_RESERVED | source_claim | — |
| input | 1171 | Register 1171 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| input | 1172 | Register 1172 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| input | 1173 | Register 1173 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| input | 1174 | Register 1174 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| input | 1175 | Register 1175 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| input | 1176 | Register 1176 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| input | 1177 | Register 1177 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| input | 1178 | Register 1178 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| input | 1179 | Register 1179 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| input | 1180 | Register 1180 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| input | 1181 | Register 1181 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| input | 1182 | Register 1182 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| input | 1183 | Register 1183 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| input | 1184 | Register 1184 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| input | 1185 | Register 1185 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| input | 1186 | Register 1186 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| input | 1187 | Register 1187 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| input | 1188 | Register 1188 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| input | 1189 | Register 1189 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| input | 1190 | Register 1190 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| input | 1191 | Register 1191 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| input | 1192 | Register 1192 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| input | 1193 | Register 1193 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| input | 1194 | Register 1194 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| input | 1195 | Register 1195 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| input | 1196 | Register 1196 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| input | 1197 | Register 1197 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| input | 1198 | Register 1198 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| input | 1199 | NewEPowerCalc Flag | Intelligent reading is used to identify software compatibility features | register value | 0 ： Old energy calculation； 1 ： new energy calculation | R | SOURCE_ONLY | source_claim | — |
| input | 1200 | MaxCellVolt | Maximumcellvoltage | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 1201 | MinCellVolt | Minimumcellvoltage | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 1202 | ModuleNum | NumberofBatterymodules | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 1203 | TotalCellNum | Totalnumberofcells | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 1204 | MaxVoltCellNo | MaxVoltCellNo | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 1205 | MinVoltCellNo | MinVoltCellNo | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 1206 | MaxTemprCell_ 10T | MaxTemprCell_10T | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 1207 | MinTemprCell_1 0T | MinTemprCell_10T | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 1208 | MaxTemprCellN o | MaxTemprCellNo | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 1209 | MinTemprCellN o | MinTemprCellNo | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 1210 | ProtectPackID | FaultPackID | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 1211 | MaxSOC | ParallelmaximumSOC | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 1212 | MinSOC | ParallelminimumSOC | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 1213 | BatProtect1Add | BatProtect1Add | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 1214 | BatProtect2Add | BatProtect2Add | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 1215 | BatWarn1Add | BatWarn1Add | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 1216 | BMS_HighestSof tVersion | BMS_HighestSoftVersion | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 1217 | BMS_Hardware Version | BMS_HardwareVersion | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 1218 | BMS_RequestTy pe | BMS_RequestType | register value | — | R | SOURCE_ONLY | source_claim | — |
| input | 1219 | Register 1219 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| input | 1220 | Register 1220 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| input | 1221 | Register 1221 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| input | 1222 | Register 1222 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| input | 1223 | Register 1223 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| input | 1224 | Register 1224 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| input | 1225 | Register 1225 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| input | 1226 | Register 1226 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| input | 1227 | Register 1227 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| input | 1228 | Register 1228 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| input | 1229 | Register 1229 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| input | 1230 | Register 1230 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| input | 1231 | Register 1231 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| input | 1232 | Register 1232 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| input | 1233 | Register 1233 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| input | 1234 | Register 1234 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| input | 1235 | Register 1235 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| input | 1236 | Register 1236 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| input | 1237 | Register 1237 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| input | 1238 | Register 1238 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| input | 1239 | Register 1239 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| input | 1240 | Register 1240 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| input | 1241 | Register 1241 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| input | 1242 | Register 1242 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| input | 1243 | Register 1243 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| input | 1244 | Register 1244 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| input | 1245 | Register 1245 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| input | 1246 | Register 1246 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| input | 1247 | Register 1247 | — | register value | — | R | UNKNOWN_RESERVED | — | — |
| input | 1248 | bKeyAgingTestO kFlag | Success sign of key detection beforeaging | register value | 1：Finishedtest 0 ： test not completed | R | SOURCE_ONLY | source_claim | — |
| input | 1249 | / | / | register value | reversed | R | SOURCE_ONLY | source_claim | — |

### Older inverter / 3.15 family

Source-only external layout coverage; no live hardware resolution is claimed.

| Table | Address | Name | Description | Encoding / scale | Unit | Access | Status | Evidence | Notes |
|---|---:|---|---|---|---|---|---|---|---|
| input | 0 | InverterStatus | InverterStatus | register value | — | UNKNOWN | SOURCE_ONLY | source_claim | — |
| input | 1 | DcPower | DcPower | register value | W | UNKNOWN | SOURCE_ONLY | source_claim | — |
| input | 3 | DcVoltage | DcVoltage | register value | V | UNKNOWN | SOURCE_ONLY | source_claim | — |
| input | 4 | DcInputCurrent | DcInputCurrent | register value | A | UNKNOWN | SOURCE_ONLY | source_claim | — |
| input | 13 | AcFrequency | AcFrequency | register value | Hz | UNKNOWN | SOURCE_ONLY | source_claim | — |
| input | 14 | AcVoltage | AcVoltage | register value | V | UNKNOWN | SOURCE_ONLY | source_claim | — |
| input | 15 | AcOutputCurrent | AcOutputCurrent | register value | A | UNKNOWN | SOURCE_ONLY | source_claim | — |
| input | 16 | AcPower | AcPower | register value | W | UNKNOWN | SOURCE_ONLY | source_claim | — |
| input | 26 | EnergyToday | EnergyToday | register value | kWh | UNKNOWN | SOURCE_ONLY | source_claim | — |
| input | 28 | EnergyTotal | EnergyTotal | register value | kWh | UNKNOWN | SOURCE_ONLY | source_claim | — |
| input | 30 | OperatingTime | OperatingTime | register value | s | UNKNOWN | SOURCE_ONLY | source_claim | — |
| input | 32 | Temperature | Temperature | register value | °C | UNKNOWN | SOURCE_ONLY | source_claim | — |

### SPF off-grid / hybrid

Source-only external layout coverage; no live hardware resolution is claimed.

| Table | Address | Name | Description | Encoding / scale | Unit | Access | Status | Evidence | Notes |
|---|---:|---|---|---|---|---|---|---|---|
| input | 0 | InverterStatus | InverterStatus | register value | — | UNKNOWN | SOURCE_ONLY | source_claim | — |
| input | 1 | PV1Voltage | PV1Voltage | register value | V | UNKNOWN | SOURCE_ONLY | source_claim | — |
| input | 2 | PV2Voltage | PV2Voltage | register value | V | UNKNOWN | SOURCE_ONLY | source_claim | — |
| input | 3 | PV1ChargePwr | PV1ChargePwr | register value | W | UNKNOWN | SOURCE_ONLY | source_claim | — |
| input | 5 | PV2ChargePwr | PV2ChargePwr | register value | W | UNKNOWN | SOURCE_ONLY | source_claim | — |
| input | 7 | Buck1Current | Buck1Current | register value | A | UNKNOWN | SOURCE_ONLY | source_claim | — |
| input | 8 | Buck2Current | Buck2Current | register value | A | UNKNOWN | SOURCE_ONLY | source_claim | — |
| input | 9 | OutActivePwr | OutActivePwr | register value | W | UNKNOWN | SOURCE_ONLY | source_claim | — |
| input | 11 | OutVA | OutVA | register value | VA | UNKNOWN | SOURCE_ONLY | source_claim | — |
| input | 13 | ACChargePwr | ACChargePwr | register value | W | UNKNOWN | SOURCE_ONLY | source_claim | — |
| input | 15 | ACChargeVA | ACChargeVA | register value | VA | UNKNOWN | SOURCE_ONLY | source_claim | — |
| input | 17 | BattVoltage | BattVoltage | register value | V | UNKNOWN | SOURCE_ONLY | source_claim | — |
| input | 18 | BattSOC | BattSOC | register value | % | UNKNOWN | SOURCE_ONLY | source_claim | — |
| input | 19 | BusVoltage | BusVoltage | register value | V | UNKNOWN | SOURCE_ONLY | source_claim | — |
| input | 20 | GridInVoltage | GridInVoltage | register value | V | UNKNOWN | SOURCE_ONLY | source_claim | — |
| input | 21 | LineFrequency | LineFrequency | register value | Hz | UNKNOWN | SOURCE_ONLY | source_claim | — |
| input | 22 | OutVoltage | OutVoltage | register value | V | UNKNOWN | SOURCE_ONLY | source_claim | — |
| input | 23 | OutFrequency | OutFrequency | register value | Hz | UNKNOWN | SOURCE_ONLY | source_claim | — |
| input | 24 | OutDCVoltage | OutDCVoltage | register value | V | UNKNOWN | SOURCE_ONLY | source_claim | — |
| input | 25 | InverterTemp | InverterTemp | register value | °C | UNKNOWN | SOURCE_ONLY | source_claim | — |
| input | 26 | DCDCTemp | DCDCTemp | register value | °C | UNKNOWN | SOURCE_ONLY | source_claim | — |
| input | 27 | LoadPercent | LoadPercent | register value | % | UNKNOWN | SOURCE_ONLY | source_claim | — |
| input | 32 | Buck1Temp | Buck1Temp | register value | °C | UNKNOWN | SOURCE_ONLY | source_claim | — |
| input | 33 | Buck2Temp | Buck2Temp | register value | °C | UNKNOWN | SOURCE_ONLY | source_claim | — |
| input | 36 | ACInPwr | ACInPwr | register value | W | UNKNOWN | SOURCE_ONLY | source_claim | — |
| input | 38 | ACInVA | ACInVA | register value | VA | UNKNOWN | SOURCE_ONLY | source_claim | — |
| input | 77 | BattPwr | BattPwr | register value | W | UNKNOWN | SOURCE_ONLY | source_claim | — |

## Remaining gaps

- MIN/TL-XH is materially stronger than the other families because it has model-specific live reads; the other families are primarily source/correlation based.
- No register has genuine write-accepted, write-reversible or behavior-verified evidence in this release.
- Some vendor, Grott and external layouts use different width/signedness conventions; alternatives and conflicts remain attached to the JSON records.
- Shine/proprietary protocol traffic and broker transport behavior are intentionally outside this register-reference release.

Original evidence files are retained in `doc/` and the local research checkouts; this generated reference is the recommended normal lookup.
