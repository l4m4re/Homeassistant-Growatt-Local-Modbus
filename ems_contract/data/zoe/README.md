# Zoe replay data

The replay data was curated from local PyCanZE poller captures. The
`ems_contract.curate_zoe_replay` tool keeps charging state, SoC, measured
current, and power; it downsamples to at most one sample per five minutes and
assigns synthetic dates while preserving time gaps within each session.
Vehicle identifiers, original timestamps, odometer, and diagnostic fields are
not included. The parser reads `state=charging` from the current PyCanZE CSV
format when a separate boolean `charging` column is absent.

`charge_replay_training.csv` contains 3,004 samples across 123 usable charge
sessions. A separate source capture is reserved for
`tests/fixtures/zoe_charge_holdout.csv`, which contains eight charge sessions
ending at or below the MVP's 80% target. The regression test checks each held
out duration and requires less than 15% relative error. Keep that source
capture out of training when refreshing the data.

The 13 A model has 48 middle-SoC training sessions over 67.1 hours and 74
sessions over 125.1 hours across all SoC bands. Those estimates meet the
model's high-confidence sample thresholds. This confidence applies to the
measured 13 A charging pattern; other current settings have less training and
may retain medium or low confidence. Dates in both CSV files are synthetic and
must not be treated as real charge times.

To recreate the training file from a local log directory, exclude the entire
capture reserved for holdout:

```sh
python3 -m ems_contract.curate_zoe_replay \
  --inputs ../CanZE/PyCanZE/Testing/logs \
  --exclude ../CanZE/PyCanZE/Testing/logs/<held-out-capture>.csv \
  --output ems_contract/data/zoe/charge_replay_training.csv
```

Curate the holdout separately, filtering sessions to the forecast target range:

```sh
python3 -m ems_contract.curate_zoe_replay \
  --inputs ../CanZE/PyCanZE/Testing/logs/<held-out-capture>.csv \
  --maximum-session-soc 80 \
  --output tests/fixtures/zoe_charge_holdout.csv
```
