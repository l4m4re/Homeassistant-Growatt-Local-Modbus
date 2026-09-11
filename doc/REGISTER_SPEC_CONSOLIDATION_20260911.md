# Register specification consolidation — 2026-09-11

## Disposition

```text
REGISTER_SPEC_LINES_CONSOLIDATED_WITH_FOLLOW_UP
```

The HA-8D development line and the complete resolved-register research line
are now preserved together on:

```text
integration/register-spec-consolidation-20260911
```

The canonical register specification regenerates and validates cleanly. One
bounded, non-blocking test-environment issue remains: two simulator-dependent
tests use an address-zero data block that the installed PyModbus version
rejects. No register-spec or HA runtime failure was found, and that unrelated
compatibility issue was not changed in this consolidation.

## Source history

| Item | Value |
| --- | --- |
| HA source branch | `feature/ha-8d-shadow-ems-planner-20260906` |
| HA source head | `b72ddef4c5e5a85e156c54baf2cf96bee2241515` |
| Register source branch | `research/resolved-register-reference-20260906` |
| Register source head | `a3a75e2068a14026f1fd558035c47f2c6deb75da` |
| Common merge base | `4127e33144e2c5c8efe3d0427f43174a47b94fa0` |
| Consolidation merge commit | `e0386ac` — `Merge resolved register specification research` |

The new branch was created from the exact HA-8D head and the research branch
was merged with `--no-ff`. Neither source branch was rewritten or updated.
Git reported no textual conflicts. The potentially overlapping HA runtime and
register-reference files were checked after the merge; the HA-7A/7C, HA-8A/B/C
and HA-8D runtime changes remain present, while the register research pipeline
and generated products are present in full.

The local untracked `doc/growatt_web/` research directory was preserved. No
`git clean`, reset, credential/capture/log staging, or unrelated cleanup was
performed.

## Pipeline and generated artefacts

The merged repository contains the complete generation route:

```text
source/vendor/HA/external corpus
        -> doc/build_register_graph.py
        -> doc/register_graph.gpickle
        -> doc/generate_consolidated_ref.py
        -> doc/consolidated_register_ref.json
        -> doc/build_resolved_register_reference.py
        -> doc/growatt_register_reference.json
        -> doc/register-spec/build_register_spec.py
        -> doc/register-spec/growatt-register-spec.json
        -> doc/register-spec/*.md
```

The generated family and human-readable outputs include:

```text
doc/register-spec/README.md
doc/register-spec/PROTOCOLS.md
doc/register-spec/SEMANTIC_INDEX.md
doc/register-spec/CLEANUP_MANIFEST.md
doc/register-spec/families/*.md
doc/register-spec/growatt-register-spec.json
doc/register-spec/growatt-register-spec.schema.json
```

The authority model is intentionally layered:

- `doc/consolidated_register_ref.json` is the graph-derived audit and
  consolidation layer, retaining source payloads and alternatives.
- `doc/growatt_register_reference.json` is the resolved compatibility/reference
  layer and bounded migration input.
- `doc/register-spec/growatt-register-spec.json` is the canonical,
  project-independent consumer specification.
- `doc/register-spec/*.md` are generated human-readable views of that
  canonical specification.

The earlier layers are provenance, audit, and compatibility material; they are
not competing semantic truths.

The graph command has a path detail worth retaining: a relative `--output`
value is resolved below `doc/` by the current script. The reproducible
repository invocation is therefore:

```sh
python3 doc/build_register_graph.py
```

or an absolute output path. Passing `--output doc/register_graph.gpickle`
would incorrectly create `doc/doc/register_graph.gpickle`.

## Regeneration and validation

The complete pipeline was run twice after the merge using:

```sh
python3 doc/build_register_graph.py
python3 doc/generate_consolidated_ref.py --validate-schema
python3 doc/build_resolved_register_reference.py
python3 doc/validate_resolved_register_reference.py
python3 doc/register-spec/build_register_spec.py
python3 doc/register-spec/validate_register_spec.py
```

Both runs reported:

```text
graph:                 6843 nodes, 53629 edges
resolved records:      4048
holding/input:         1805 / 2243
resolved conflicts:    0
live-read verified:    60
write verified:        0
canonical semantics:   962 unique semantic quantities
human documents:       11
```

The second run produced no unexplained generated changes. Expected generated
metadata differences are the `generated_at` timestamp and graph fingerprint;
the graph pickle is treated as an intermediate rather than compared by byte
identity alone. Generated Markdown and canonical JSON content remained stable
between runs. The graph-regenerated audit layer also records its current
datatype alternatives; the resolved compatibility layer and final canonical
specification retain the curated MIN interpretations below.

## MIN/TL-XH preservation check

The final generated canonical specification retains holding/input identity and
the required corrections:

```text
holding 3047  Battery-first charge power rate
holding 3048  Battery-first stop SOC
holding 3049  AC charging enabled
holding 3081  UPS/EPS frequency selection
holding 3082  Load-first stop SOC

input 3047    Inverter runtime
input 3081    PV4 energy total
```

The two battery-current locations remain distinct physical measurement points:

```text
input 3170 -> battery.current, storage_device, s16/10
              implementation-correlated signedness; no negative live sample

input 3217 -> battery.current, BMS, s16/100
              signedness regression/live-value validated
```

The compatibility reference also preserves the semantic relationship between
the alternate/preferred battery-SOC registers and the validated native MIN
read plans. No writes were performed as part of this consolidation.

## Verification results

Passed:

```text
python3 doc/validate_resolved_register_reference.py       PASS
python3 doc/register-spec/validate_register_spec.py      PASS
register/resolved tests:                                 17 passed
HA-5 regression tests:                                    7 passed
full HA integration suite:                               73 passed
python3 -m compileall -q doc custom_components tests    PASS
git diff --check                                         PASS
```

The full suite collected 75 tests. Two simulator-dependent tests did not
complete under the installed PyModbus version:

```text
test_growatt_api_read_write         FAILED during simulator startup
test_sensor::test_sensor_setup       ERROR during simulator fixture setup
```

Both fail because the existing simulator constructs a sequential data block at
register zero, which this PyModbus version converts to `address=-1` and rejects.
This is outside the register-spec merge and does not affect the 24 passing
register/HA-5 checks or the 73 other integration tests. It is the bounded
follow-up for this checkpoint.

The initial pytest invocation from the integration checkout also encountered
the repository's minimal local `homeassistant` stub and an auto-loaded plugin.
The HA tests were rerun from the HA-core parent with `--import-mode=importlib`,
which loads the actual HA-core package and gives the results above.

## Deliberately deferred

This consolidation does not:

- perform the broad semantic cleanup of questionable BMS/BDC/temperature/
  warning fields;
- change HA entities, `entity_id`, `unique_id`, units, state classes, sign
  conventions, Recorder/LTS semantics, or cumulative counters;
- rewrite runtime register mappings or enable TCP writes;
- claim additional semantic verification from native block-read evidence;
- change HA-7C native polling or HA-8D shadow EMS behavior; or
- fix unrelated PyModbus simulator compatibility or repository lint debt.

The next recommended task is a bounded semantic cleanup/reconciliation of the
canonical MIN/TL-XH specification, with sensor/statistics continuity review
before any production entity migration.
