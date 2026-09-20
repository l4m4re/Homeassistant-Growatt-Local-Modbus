# Growatt integration documentation

This directory contains documentation for the Home Assistant runtime and its
bounded validation. The integration does not keep a second copy of the broad
Growatt register research corpus.

## Register knowledge

The project-independent register authority is the
[`growatt-inverter-info`](https://github.com/l4m4re/growatt-inverter-info)
repository. Its `spec/growatt-register-spec.json` is the reviewed,
machine-readable specification. Keep the separation explicit:

- GII owns vendor material, independent implementation snapshots, live and
  portal evidence, semantic review, and the generated register specification.
- This repository owns the model-specific runtime dictionaries, decoding,
  polling plans, entity descriptions, and focused integration tests.

An entry in the GII specification is not automatically a Home Assistant
entity. Promote a register into the runtime only after checking model
applicability, decoding, entity metadata, and validation evidence.

Runtime register audits and polling-plan reviews belong with the evidence in
the GII repository, under
[`docs/consolidation/`](https://github.com/l4m4re/growatt-inverter-info/tree/main/docs/consolidation).
They are deliberately not duplicated in this integration repository.

Project-specific HIL and production-readiness records are kept in the
workspace documentation at `../../doc/home-energy/growatt/`. They are not
part of the reusable integration package.

## Reproducible integration checks

Run the focused tests from the repository root:

```bash
pytest
```

Run the focused integration tests and direct register reader as described in
[`../testing/README.md`](../testing/README.md). The simulator and fixtures are
maintained by the companion broker project and are not runtime dependencies of
the integration.

Changes to the runtime register dictionaries should include the corresponding
entity metadata, translations, polling-plan checks, and focused regression
tests. Keep entity IDs and Recorder/statistics semantics stable when changing
decoding or polling.
