# HA-GII-5 controlled development Home Assistant deployment

Disposition: **`HA_GII_DEV_DEPLOYMENT_ACCEPTED_WITH_FOLLOW_UP`**

This was a read-side development deployment only. It did not write to the
inverter, modify the production HA instance, modify the production database,
or change the broker configuration.

## Exact baselines

| Component | Baseline |
| --- | --- |
| HA Core | branch `research/ha-dev-2-transport-20260906`, version `2026.9.0`, SHA `1f3748d9310fad0a9b22ceec17654fcb8d42069f` |
| Python | `3.14.5` |
| PyModbus | `3.13.1` |
| Consumer | `integration/register-spec-consolidation-20260911`, SHA `969553f03c7f78ad624d5362b89b2065c620b4bd` |
| Canonical GII | `main`, SHA `f061c4aeeadeb06246aac6d4d0732da36fc6996d` |
| Broker source | SHA `ef325f00f6eb3ab3cc8b88b97844a7237fea02e4` |
| Broker runtime | `growatt-rtu-broker:ha-dev-3d-predictive-20260911c` |
| HA endpoint | DEV `:5021`, unit 1 |

Only DEV `:5021` was used. The production endpoint `:5020` was not used by
the development HA. The integration was loaded from the checked-out consumer
repository through the existing `config/custom_components/growatt_local`
symlink. For the clean validation run, a temporary config copied only the
existing DEV config-entry and linked that checked-out component; it had no
production database or serial-device access.

The compact evidence is in
[`doc/data/HA-GII-5_DEV_DEPLOYMENT_EVIDENCE.json`](data/HA-GII-5_DEV_DEPLOYMENT_EVIDENCE.json).

## Startup and entity surface

The clean development instance started successfully and set up the existing
Growatt config-entry. Polling produced successful coordinator updates and the
process remained alive throughout the bounded run. The standard HA warning
that this is an untested custom integration was present; no Growatt setup
exception or repeated HA integration error occurred.

The clean registry contains 95 Growatt entities. The production registry
contains 94. Ninety-three unique-ID suffixes are shared. The difference is a
configuration/surface difference: development exposes the read-side
`current_priority` and `xh_schedule` entities, while the production registry
contains the legacy `power_control` surface. Development had
`inverter_power_control` disabled, and no writable control was exercised.

Shared unique-ID semantics and physical quantities are preserved; the entity
ID prefix differs because the development entry name is different. No entity
rename or migration was performed.

The development Recorder created 27 statistics metadata records. Cumulative
energy metadata uses kWh and `total_increasing`; instantaneous power metadata
uses W and `measurement`. Two short-term samples were present for each of the
27 records at the end of the bounded run. Long-term rows were not yet present,
because this run was minutes rather than an hour-scale statistics soak.

## HA-GII-3 presentation checks

The clean registry/database confirms the reconciled presentation inside real
Home Assistant:

| Check | Development result |
| --- | --- |
| I3021 reactive power | `0.0 var`, device class `reactive_power`, state class `measurement` |
| I3101 real output percentage | `10 %`, no `power_factor` device class |
| I3230 cell voltage max | `3.300 V` |
| I3231 cell voltage min | `3.279 V` |

The I3021 numeric value was not converted; only its HA presentation changed.
Cell voltage precision is meaningful and is not frontend-rounded to whole
volts.

## Polling and broker behavior

A three-minute sniff was captured during normal clean development polling.
The development HA issued the following recurring read set:

| Function | Start/count | Role |
| ---: | --- | --- |
| FC03 | 3000/125 | holding-side compatibility/read set |
| FC04 | 3000/125 | native inverter telemetry page |
| FC04 | 3125/125 | native battery/BMS page |

The HA client opened repeated short TCP sessions and requested three complete
125-word blocks per update cycle. This is transaction-efficient at the
application level and aligns with the broker cache; it did not regress into
one-register-per-entity polling. The FC04 3250 page was not requested because
the active consumer did not select fields from that page. The broker provided
the repeated requests predominantly from cache, while background prefetch
refreshed physical data opportunistically.

The existing broker analyzer reported:

| Event | Count/result |
| --- | ---: |
| Shine request/response pairs | 145/145 |
| Shine timeouts | 0 |
| Shine CRC errors | 0 |
| Cache hits | 232 |
| FC20 refreshes | 18 |
| Async frames observed/forwarded | 7/7 |
| Writes | 0 |
| Background prefetch refresh failures | 1 |
| Downstream timeout | 1 |
| Automatic inverter serial reopen | 1 |

The single failure occurred at 18:33:21 UTC during a background FC04
3000/125 prefetch physical refresh. The broker reopened the inverter serial
port after repeated timeouts; subsequent refreshes and HA updates continued.
The Shine path had no timeout or CRC error in this capture. This validates
continued operation under one recovered transport disturbance, but it is a
follow-up transport observation rather than a claim of zero-failure
operation.

## Representative live values

The following values were read by the development HA entity layer near the
end of the run and agree with the HA-GII-4 DEV evidence within normal timing
differences:

| Quantity | Source | Development value |
| --- | --- | ---: |
| AC output power | I3023 | 647.1 W |
| Reactive power | I3021 | 0.0 var |
| Grid import/export | I3041/I3043 | 0.0/0.0 W |
| House/load power | I3045 | 682.0 W |
| SOC | I3171 | 66% |
| Battery voltage | I3169 | 211.58 V |
| I3170 battery current | I3170 | +3.1 A |
| BMS current | I3217 | −3.2 A |
| Discharge/charge power | I3178/I3180 | 679.0/0.0 W |
| Total produced energy | I55 | 19623.3 kWh |
| Energy to grid/user total | I3073/I3069 | 11169.8/7866.5 kWh |
| Battery discharged/charged total | I3127/I3131 | 3245.4/3389.1 kWh |
| Cell voltage max/min | I3230/I3231 | 3.300/3.279 V |

The state represents natural battery discharge. No charging or near-idle state
occurred, so HA-GII-5 adds no new I3170 sign conclusion. The development
I3170 value remains positive while I3217 remains negative in this condition,
consistent with HA-GII-4's unresolved measurement-point/sign distinction.

The cumulative values were non-negative and did not show an artificial jump
within the development state history. `battery_discharged_total` advanced
normally by 0.1 kWh during the observed run. No counter reset or rollover was
observed.

## Production coexistence

Read-only inspection of the production container during the development run
showed recent successful Growatt fetches and no new failure burst. The
production broker and production HA container were not restarted or
reconfigured. The development connection used only the broker's DEV port.

## Recorder continuity and production anomaly classification

The clean development instance confirms that the reconciled entity metadata
and short-term Recorder path are internally coherent. It is not long enough
to generate long-term statistics rows, so long-term continuity remains a
deployment gate.

The first restart against the existing Frodo dev database exposed the exact
migration hazard anticipated by HA-GII-4: the old I3021 statistics identity
was compiled as `W`, while the reconciled entity is `var`, and HA suppressed
long-term statistics for that entity. The clean bounded config removed the
historical database and loaded the new metadata correctly. A production
upgrade must therefore include a deliberate statistics migration/continuity
plan; silently reusing the old statistics identity is not acceptable.

The production database was queried read-only. Its evidence classifies the
known anomalies as follows:

1. `total_energy_produced` has one historical `-0.1` state step, from
   19501.1 to 19501.0 over approximately four minutes on 2026-09-05. The
   current total counter history is otherwise monotonic in the inspected
   range. This is a historical state/rounding or old-integration outlier,
   not evidence of an ongoing HA-GII-2 decoder regression; keep it visible in
   the production readiness checklist.
2. `battery_discharged_today` has a statistics aggregate sum of approximately
   144,776,728 while its current daily state is single-digit kWh and the
   lifetime counter is normal and monotonic. This cannot be raw inverter
   behavior. It is best classified as an old Recorder/integration aggregation
   artifact or database outlier. No database correction was attempted.

## Tests and warnings

The relevant existing tests were run against the reconciled consumer:

- HA-GII-2 decoder regressions: **8 passed**.
- Full consumer suite: **81 passed, 1 failed, 1 error, 1 warning**.
- The failure and error are the known broker-simulator/PyModbus 3.13.1
  harness incompatibility: it constructs `SimData(address=-1)`. They occur
  in `test_growatt_api_read_write` and the `test_sensor_setup` fixture before
  integration behavior is exercised.

The clean deployment itself had no Growatt setup error. Unrelated inherited
dev-config warnings about missing local devices were not treated as Growatt
failures. No protocol or register code was changed in HA-GII-5.

## Decision and next gate

The development deployment is broadly successful and safe for continued
read-side development through DEV `:5021`. It is not yet a production-upgrade
approval because of the I3021 statistics-unit migration issue, the limited
long-term statistics window, the recovered background transport timeout, and
the already-known I3170/BMS evidence gaps.

Next, separately perform a production-upgrade readiness gate covering:

- backup and rollback;
- an explicit I3021 statistics migration/identity decision;
- before/after entity, unique-ID, unit, state-class, and counter checks;
- longer Recorder validation;
- broker transport recovery review;
- production cutover only after those checks pass.
