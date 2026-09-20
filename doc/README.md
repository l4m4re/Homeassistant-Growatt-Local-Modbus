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
private Home Energy Manager project at
`../../home-energy-manager/docs/growatt/`. They are not part of the reusable
integration package.

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

The current MIN/TL-XH comparison uses GII commit `4d1feaa` and
`spec/growatt-register-spec.json` SHA-256
`c7a6919222a453b5657b783c8d584c0a325b52547c5f7453663acb380bd4c8bc`. It
decodes the bidirectional AC output pair I3023–I3024 as signed int32 `/10`
and I3101 as signed int16 percentage values. It keeps the reviewed runtime overlay in
`sources/evidence/min-6000tl-xh-register-map.json` as the promotion boundary:
reserved words are excluded, while the reviewed PV4 energy rows at I3079 and
I3081 are represented by the existing input-energy attributes. The reviewed
FC03 UPS/EPS rows H3079-H3081 are retained as API map entries without creating
new HA entities or write services.
