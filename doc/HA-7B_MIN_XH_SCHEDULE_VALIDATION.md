# HA-7B MIN/TL-XH schedule validation

Read-only validation of the live `MIN 6000TL-XH` through broker
`192.168.1.148:5021`, unit 1, on 2026-09-06. No FC06/FC16 writes were issued.
The compact machine-readable evidence is in
[`HA-7B_MIN_XH_SCHEDULE_VALIDATION.json`](HA-7B_MIN_XH_SCHEDULE_VALIDATION.json).

## Live result

The user-stated precondition was **not true** in the live register state:
Time 2 is enabled. Therefore the requested claim “with all XH slots disabled,
I3144 reports Load First” cannot be recorded as validated.

The live observation was instead:

> With Time 2 enabled for `00:00–07:00` Battery First, and the inverter clock
> outside that interval at approximately `15:15`, I3144 repeatedly reported
> Load First.

This is a behavior/state observation, not a universal firmware fallback rule.

## Slot state

Vendor decoding: bits 0–7 minute, 8–12 hour, 13–14 priority (`0 Load First`,
`1 Battery First`, `2 Grid First`), bit 15 enable. End words use bits 0–7
minute and 8–12 hour; bits 13–15 are reserved.

| Slot | Start/control raw | Start | Priority | Enabled | End raw | End |
|---:|---:|---:|---|---:|---:|---:|
| 1 | `H3038=0x3700` | 23:00 | Battery First | no | `H3039=0x173B` | 23:59 |
| 2 | `H3040=0xA000` | 00:00 | Battery First | **yes** | `H3041=0x0700` | 07:00 |
| 3 | `H3042=0x2000` | 00:00 | Battery First | no | `H3043=0x043B` | 04:59 |
| 4 | `H3044=0x0000` | 00:00 | Load First | no | `H3045=0x0000` | 00:00 |
| 5 | `H3050=0x0000` | 00:00 | Load First | no | `H3051=0x0000` | 00:00 |
| 6 | `H3052=0x0000` | 00:00 | Load First | no | `H3053=0x0000` | 00:00 |
| 7 | `H3054=0x0000` | 00:00 | Load First | no | `H3055=0x0000` | 00:00 |
| 8 | `H3056=0x0000` | 00:00 | Load First | no | `H3057=0x0000` | 00:00 |
| 9 | `H3058=0x0000` | 00:00 | Load First | no | `H3059=0x0000` | 00:00 |

Thus 8/9 slots are disabled and Time 2 is the only enabled slot.

## Executed priority

| Timestamp UTC | I3144 raw | Decoded |
|---|---:|---|
| 13:16:08.096 | `0x0000` | Load First |
| 13:17:08.118 | `0x0000` | Load First |
| 13:18:08.141 | `0x0000` | Load First |

All three samples are stable. They were taken outside Time 2’s configured
00:00–07:00 interval, so they do not distinguish the all-disabled fallback
from ordinary outside-slot behavior.

## EMS baseline

| Register | Raw | Decoded meaning |
|---|---:|---|
| H3036 | `70` | Grid First discharge power rate: 70% |
| H3037 | `10` | Grid First stop SOC: 10% |
| H3047 | `70` | Battery First charge power rate: 70% |
| H3048 | `90` | Battery First stop SOC: 90% |
| H3049 | `0` | AC Charge disabled |
| H3082 | `0` | Load First stop SOC raw value; vendor lists 13–100, so this is retained without reinterpretation |

No baseline value was changed.

## Inverter clock

The vendor labels H45–H50 as local system time. The read returned:

```text
H45–H50 = 2026-09-06 15:15:47
```

At the H0 read response, host Europe/Amsterdam time was approximately
`2026-09-06 15:16:05.795+02:00`. The inverter clock was therefore about 19
seconds behind the host. The date and timezone basis are understood well enough
for a later short controlled test, but the test should include a safety margin
of at least one minute around its target boundary.

## Source semantics

| Question | Status | Finding |
|---|---|---|
| Slot bit layout and priority enum | DOCUMENTED | V1.24 explicitly defines the start/control and end word bits. |
| Outside-slot fallback | NOT DOCUMENTED | The vendor describes periods and priorities but does not state the fallback rule. The live result is only an outside-active-window observation. |
| Start boundary inclusion | NOT DOCUMENTED | `[Start Time ~ End Time]` is shown, but exact inclusivity and transition timing are not specified. |
| End boundary inclusion | NOT DOCUMENTED | No exact end-boundary rule is stated. |
| Overlap precedence | NOT DOCUMENTED | No precedence rule for overlapping enabled slots is stated. |
| Midnight crossing | NOT DOCUMENTED | No explicit rule states whether a start later than the end crosses midnight. |
| External implementation correlation | LIMITED | The retained inverter-to-MQTT documentation exposes priority/time controls and says Load First is a default in an SPH-specific context, but it does not validate these MIN/TL-XH H3038–H3059 semantics. |

## Dynamic-tariff implication

The proposed architecture is plausible as a design hypothesis: HA can select a
small number of windows, Growatt can store them, and I3144 can provide feedback.
It is not yet production-validated because the current live configuration is
not all-disabled and boundary, overlap, midnight, and fallback semantics remain
unresolved.

## Future reversible test plan — not executed

After explicit approval, use currently disabled Time 4 (H3044/H3045) rather than
overwriting the existing enabled Time 2:

1. Read and save the complete H3038–H3059 state, H3047–H3049, H3082, and the
   clock; require an exact byte-for-byte restoration record.
2. Confirm AC Charge remains disabled and choose a one- to two-minute future
   interval with at least a one-minute clock margin.
3. Select a stable low-power operating condition with no material PV surplus or
   battery movement. A Battery First slot with AC Charge still disabled is the
   least likely to cause grid charging, but it is not risk-free.
4. Program only H3044/H3045, observe I3144 before, at, inside, and after the
   interval, and monitor battery/grid power concurrently.
5. Use a short watchdog timeout; on any unexpected power movement, restore
   immediately.
6. Restore the exact saved H3044/H3045 words and verify them by readback. Then
   verify the complete saved schedule and EMS baseline are unchanged.

This plan is required to settle boundary behavior and actual priority
transitions. It must not be executed as part of HA-7B.

## Safety and scope

- No FC06 or FC16 writes; no schedule was enabled or altered.
- No runtime mappings, entities, polling, or dynamic-tariff code changed.
- H3125+ US-machine time structures were not read or interpreted.
- The sniff capture was temporary and is not committed; the compact evidence
  artifact retains its SHA-256 only.
