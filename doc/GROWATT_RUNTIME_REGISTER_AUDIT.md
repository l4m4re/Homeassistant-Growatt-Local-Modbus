# Growatt runtime register audit

This is an audit of the current `growatt_local` read path. It does not change
the polling engine. The public semantic reference and its read plans separate
bus blocks, local decoding, semantic selection and HA entities.

## Current implementation

`GrowattDevice.update()` in `custom_components/growatt_local/API/growatt.py`
does not issue one request per entity. It converts the requested physical keys
to sequences with `register_sequences()` / `keys_sequences()` in
`custom_components/growatt_local/API/utils.py`, then reads each holding and
input sequence separately. Holding and input sequences are always separate
function codes. The sequence cache is keyed by the requested key set.

For the TL-XH runtime, the current `MAXIMUM_DATA_LENGTH_120` is 100 words.
`keys_sequences()` may include gaps inside a sequence, but its split heuristic
can divide a logical vendor page at large gaps. Entity selection therefore does
affect the blocks: the normal coordinator key set is assembled from the
selected HA sensors/switches/numbers, while the optional power scan uses the
smaller `p_keys` set. Decoding only exposes mapped values; returned gap words
are not entities.

## Derived current MIN/TL-XH transaction budget

Using the current `HYBRID_120_TL_XH` register definitions and all currently
declared inverter/storage/control keys, the cached sequences are:

```text
Holding: H0+2, H3049+1                         2 FC03 transactions
Input:   I3000+100, I3101+32, I3164+68          3 FC04 transactions
Total:                                             5 transactions
```

At the vendor-recommended 1-second command period, this is approximately a
5-second minimum cycle before connection/processing overhead. The optional
power scan is currently derived as:

```text
Input: I3001+46, I3171+11                       2 FC04 transactions
```

There are no duplicate/overlapping blocks within either derived update. The
normal full update and power scan use different key sets, so they are separate
polling modes rather than a merged transaction budget.

## Vendor-native and proposed MIN plan

The V1.24 document declares a minimum command period of 850 ms, recommends
1 second, permits up to 125 read words, and defines 125-word register pages.
The current broker's 1-second period therefore follows the vendor recommendation;
it is not merely an empirically chosen broker throttle.

The bounded HIL validation in `min_6000tl_xh_block_validation.json` repeated all
five applicable candidate pages twice through broker `:5021`, with sniff
analysis from `:5700`. All ten requests returned the requested 125 words, with
zero exceptions, timeouts, drops, retries or bad CRCs.

For the high-value MIN/TL-XH runtime set, the preferred plan is:

```text
FAST telemetry:  FC04 I3000+125 (3000–3124)  one transaction
                 FC04 I3125+125 (3125–3249)  one transaction
                 minimum at 1 s/command:      approximately 2 s

FAST controls:   FC03 H3000+125 (3000–3124)  one transaction
                 combined telemetry/control:  3 transactions, approximately 3 s

NORMAL/SLOW:     FC03 H0+125 (identity)       +1 transaction
                 FC04 I3250+125 (diagnostics)  +1 transaction where applicable
```

The input 3000–3124 page contains status, PV power, grid import/export and load
semantics. The input 3125–3249 page contains the preferred battery telemetry
and BMS values. The holding 3000–3124 page contains the dynamic-tariff control
registers. Unused or reserved words are fetched but decoded locally only when
their physical definitions are known; they are not promoted to HA entities.

The 125-word page is preferred over smaller ranges because transaction count is
the limiting resource. The page boundaries are family/protocol metadata, not a
global assumption: the older 3.15/V3.14 family is modelled separately with its
45-word maximum and 45-word boundary restrictions, and SPF limits are not
inherited without evidence.

## Separation of concerns

```text
vendor-safe FC03/FC04 block
        -> local register decoder
        -> selected semantic keys
        -> selected HA entities
```

Adding more register knowledge must therefore not imply one more Modbus
transaction or one more Home Assistant entity. A future runtime implementation
should consume the generated `read_plans` metadata and retain the polling-class
distinction rather than rebuilding blocks from entity names.

The current runtime was intentionally not rewritten in HA-6B.
