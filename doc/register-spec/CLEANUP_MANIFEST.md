# Register research cleanup manifest

HA-6D does not delete or move the research corpus. This manifest records the
intended future separation after independent review.

## Product

- `register-spec/growatt-register-spec.json`
- `register-spec/growatt-register-spec.schema.json`
- `register-spec/build_register_spec.py`
- `register-spec/README.md`, `PROTOCOLS.md`, `SEMANTIC_INDEX.md`
- generated `register-spec/families/*.md`

## Source and evidence

- vendor V1.24 and V3.14 documents and extracted tables;
- `min_6000tl_xh_live_validation.json`;
- `min_6000tl_xh_block_validation.json`;
- concise external implementation extracts under `doc/`;
- source catalogue and provenance entries in the canonical JSON.

## Research and intermediate

- graph pickle and consolidated graph exports;
- best-guess datasets and overlays;
- exploratory comparison/extraction scripts;
- web mirror and translation research;
- runtime snapshots and HA-specific audit outputs.

Future work may move source/evidence into an archive and delete obsolete
intermediates only after the canonical product has been independently reviewed.
No destructive cleanup is part of HA-6D.
