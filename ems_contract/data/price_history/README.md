# Curated historical price examples

`curated_examples.json` contains small, machine-readable selections copied from
the local `external/HistorischeStroomPrijzen/` archive. They are for EMS,
chart, and educational development only; they are not live provider data or a
complete price history.

The selections cover an hourly volatile week, an hourly negative-price day,
and two quarter-hour examples. Each sample records its source file, source
file hash, date range, resolution, and reason for selection. The original
`datum_nl`, `datum_utc`, and `prijs_excl_belastingen` strings are preserved.

`tests/test_historical_price_backtest.py` feeds the quarter-hour examples
through the current EMS planner and checks its choices against the recorded
negative-price and high-volatility patterns. The hourly examples are retained
for later history/trend analysis; the current planner accepts quarter-hour
intervals only.

The archive currently does not document its original source, currency, unit,
or exact tax/charge composition. Its timestamp fields are timezone-naive. The
JSON therefore leaves currency and unit unset and warns that provenance and
time interpretation need validation. Do not label or use these values as a
specific customer tariff until those details are verified. Check the source
and its license before redistribution beyond this development repository.

The structural audit found hourly records in the 2013–2024 files, with one
two-hour timestamp step in each annual file. The 2025 file has a complete
quarter-hour sequence; the 2026 file is quarter-hourly through 2026-09-09 and
does not cover the following eight days. The `datum_utc` name suggests UTC,
but its values have no offset, so the two-hour steps may involve timezone or
collection gaps. The price field is a decimal-comma string named
`prijs_excl_belastingen`; that establishes the stated tax basis, but not its
currency or price unit. Keep archive data out of all-in planning until these
details are resolved. Do not interpolate the timestamp gaps.

When refreshing a selection, copy records from the source archive without
interpolation, recompute its source-file hash and record count, and review the
changed selection before use. The long-term package location will be decided
as part of the planned EMS cleanup and restructuring.
