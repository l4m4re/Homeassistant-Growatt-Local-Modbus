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

## Runtime and validation reports

- [`GROWATT_RUNTIME_REGISTER_AUDIT.md`](GROWATT_RUNTIME_REGISTER_AUDIT.md)
  explains the current transaction plan and the boundary between Modbus
  blocks, decoding, and entities.
- [`HA-7A_MIN_RUNTIME_AUDIT.md`](HA-7A_MIN_RUNTIME_AUDIT.md) records the
  evidence-gated MIN/TL-XH mapping review.
- [`HA-7C_MIN_NATIVE_BLOCK_POLLING.md`](HA-7C_MIN_NATIVE_BLOCK_POLLING.md)
  records the family-specific native page polling implementation.

Project-specific HIL and production-readiness records are kept in the
workspace documentation at `../../doc/home-energy/growatt/`. They are not
part of the reusable integration package.

## Reproducible integration checks

Run the focused tests from the repository root:

```bash
pytest
```

Run the deterministic Modbus simulator and its helper tools as described in
[`../testing/README.md`](../testing/README.md). The simulator and fixtures are
test infrastructure; they are not runtime dependencies of the integration.

Changes to the runtime register dictionaries should include the corresponding
entity metadata, translations, polling-plan checks, and focused regression
tests. Keep entity IDs and Recorder/statistics semantics stable when changing
decoding or polling.
