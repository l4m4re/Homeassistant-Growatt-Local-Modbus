# HA-7C MIN/TL-XH native block polling

Date: 2026-09-06
Device: MIN 6000TL-XH, unit 1
Endpoint: `192.168.1.148:5021`
Access: read-only

## Result

MIN/TL-XH runtime reads now select complete vendor-native 125-word pages. The
optimization is family-specific; legacy families continue to use their
existing limits. Register decoding and entity mappings are unchanged.

The implementation keeps physical page reads separate from local decoding:
unused words in a fetched page are not exposed as entities.

## Transport and page model

For the V1.24/MIN family, the runtime page model is:

| Class | Function | Start | Count | Current use |
| --- | --- | ---: | ---: | --- |
| FAST | FC04 | 3000 | 125 | PV, output, battery and EMS telemetry |
| FAST | FC04 | 3125 | 125 | battery energy and BMS telemetry |
| CONTROL | FC03 | 3000 | 125 | current holding/control mappings |
| STATIC | FC03 | 0 | 125 | inverter enable and static/base mappings |
| DIAGNOSTIC | FC04 | 3250 | 125 | optional future diagnostic coverage |

The vendor-declared limit is 125 words. The vendor timing evidence remains a
minimum command period of 850 ms and a recommended period of approximately one
second. These are protocol characteristics, not a newly selected integration
throttle.

The existing coordinator cadence is retained: its power-scan key set uses the
two FAST input pages, while its normal/full key set also fetches the applicable
CONTROL and STATIC pages. The DIAGNOSTIC page is not read for the current
entity surface because no current mapping requires it.

## Old and new read plans

The pre-HA-7C MIN/TL-XH operational plan was fragmented as follows:

```text
FC03 H0 +2
FC03 H3049 +1
FC04 I3000 +100
FC04 I3101 +32
FC04 I3164 +68
```

That is five physical transactions for a full operational update.

The new native plan is:

```text
FAST
  FC04 I3000 +125
  FC04 I3125 +125

FULL / control and static refresh
  FC03 H0 +125
  FC03 H3000 +125
  FC04 I3000 +125
  FC04 I3125 +125

optional diagnostic
  FC04 I3250 +125
```

Therefore the power-scan FAST path is two transactions rather than five. A
full refresh is four transactions, with control and static data retained at
the existing normal/full cadence. At the vendor-recommended one-second
command period this is approximately 2 seconds minimum for FAST and 4 seconds
minimum for a full refresh, compared with approximately 5 seconds for the old
fragmented full plan.

The effective plan is available as runtime data through
`min_tlxh_read_plan()` and is covered by deterministic tests.

## HIL evidence

Fresh bounded sniff capture:

```text
/tmp/growatt-ha7c-hil-20260906-134337.jsonl
sha256 c3e4fae61d94ff69e8dfdf8131201ecc318c630667b03b648801c682022df6b7
```

The existing broker analyzer was run against this capture. For the HIL client
(`TCP:192.168.1.139:51354`) it reported 10 requests and 10 responses, with no
timeouts, drops, CRC failures or unknown functions. Four unrelated requests
from another broker client were also present and were not included in the
HIL count.

The HIL client requests were:

```text
FAST cycle 1: FC04 I3000 +125, FC04 I3125 +125
FAST cycle 2: FC04 I3000 +125, FC04 I3125 +125
FAST cycle 3: FC04 I3000 +125, FC04 I3125 +125
FULL cycle:   FC03 H3000 +125, FC03 H0 +125,
              FC04 I3125 +125, FC04 I3000 +125
```

All ten responses had the expected 125-word payload (`len=251` in the sniff
records, including function/byte-count/data/CRC framing) and `crc_ok=true`.
The direct runtime calls completed in approximately 1.182–1.192 seconds for
each FAST cycle and 3.373 seconds for the full cycle. The decoded values
included status `1`, SOC `35`, and changing BMS current values; no decode
exception occurred.

No writes were performed. No schedule register was changed or tested. The
capture showed no late/orphan/TID warning event; any warnings outside this
bounded capture remain transport follow-up work.

## Coverage and regressions

All currently mapped MIN/TL-XH holding registers fit in H0/H3000 native pages,
and all currently mapped input registers fit in I3000/I3125 native pages.
Boundary and multiword tests verify that a value crossing I3124/I3125 causes
both complete native pages to be selected rather than an undocumented
cross-page read.

The HA-5 semantics remain unchanged:

- `I3170` remains unsigned and scaled by 10;
- `I3217` remains signed int16 and scaled by 100 (`0xFEB6` → `-3.30 A`);
- holding and input address spaces remain distinct;
- PV power, PV1/PV2 power, battery SOC/voltage/current, BMS current and
  inverter state retain their existing decoding and entity names.

The legacy v3.15 planner remains bounded at 45 words and is not routed through
the 125-word MIN plan.

## Scope

This branch contains only the runtime page planner, deterministic tests and
this bounded report. It does not change semantic mappings, add entities,
implement dynamic tariffs, add Peblar/Zoe/EMS behavior, modify schedule state,
or update the HA-core parent gitlink.
