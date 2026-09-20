# Register knowledge workflow

This repository is a Home Assistant consumer of the project-independent
[`growatt-inverter-info`](https://github.com/l4m4re/growatt-inverter-info)
register knowledge base. New register knowledge is collected and reviewed in
that repository first. This repository records how an accepted result is
checked against the HA runtime and how it is introduced without losing entity
or Recorder continuity.

The local `doc/register-spec/` tree is currently a compatibility and migration
artifact. It is not an independent semantic authority.

## Where information belongs

| Information | Repository and location | Use |
| --- | --- | --- |
| New vendor, live, portal, cloud, or Recorder evidence | `growatt-inverter-info/sources/` | Source and review input |
| Accepted shared register semantics | `growatt-inverter-info/sources/consolidated/register-blocks.json` | Project-independent authority |
| Generated shared specification | `growatt-inverter-info/spec/` | Machine-readable consumer input |
| HA runtime declarations and decoders | `custom_components/growatt_local/` | Actual integration behaviour |
| HA compatibility and runtime audit views | `doc/` | Consumer reconciliation and review record |
| HA tests and fixtures | `tests/` | Decoder, entity, simulator and continuity checks |

Do not put new shared register semantics only in a Python map, a generated HA
Markdown file, or a Recorder export. If an observation is not yet accepted in
GII, keep it in an HA audit or evidence note with a provisional status and link
it back to the GII review work.

## Updating register knowledge

### 1. Complete the evidence review in GII

Follow GII's
[`REGISTER_KNOWLEDGE_WORKFLOW.md`](https://github.com/l4m4re/growatt-inverter-info/blob/main/docs/REGISTER_KNOWLEDGE_WORKFLOW.md)
for capture, provenance, conflict handling and human review. The accepted GII
commit must be known before changing the HA consumer.

Portal mappings and Recorder correlations need separate evidence records. A
portal label/value change establishes a UI-to-device correlation only when the
readback and operating conditions are recorded. A Recorder correlation records
behaviour over time; it does not by itself redefine a Modbus register.

### 2. Pin the GII input

In the HA change document, record all of the following:

- GII repository commit;
- specification checksum or generated artifact version;
- affected family, table and address rows;
- applicability paths and unresolved alternatives;
- the date and reason for the consumer update.

Use `(family, table, address)` as the identity. Holding and input registers
with the same numeric address are different records.

For a local HA-core checkout the GII repository is normally available at
`external/growatt-inverter-info/`. Do not copy a new generated specification
over the existing HA tree without recording the source commit and reviewing
the format and authority transition.

### 3. Reconcile with the runtime

Compare the accepted GII rows with the actual declarations selected by the
runtime, including:

- device family and model selection;
- function code and address table;
- signedness, width, scale, unit and word order;
- read/write policy and polling block;
- entity name, unique ID, state class and statistics behaviour.

Change the runtime only when the evidence and consumer impact have been
reviewed. Keep a runtime-only workaround or model-specific exception explicit
in the HA audit documentation and link it to the GII source or unresolved
conflict.

### 4. Regenerate and test

When the compatibility/reference inputs in this repository change, use the
documented pipeline and inspect the generated diff:

```bash
python3 doc/build_register_graph.py
python3 doc/generate_consolidated_ref.py --validate-schema
python3 doc/build_resolved_register_reference.py
python3 doc/validate_resolved_register_reference.py
python3 doc/register-spec/build_register_spec.py
python3 doc/register-spec/validate_register_spec.py
```

Run the focused register and runtime tests, then the relevant Home Assistant
integration tests. A register change that affects an existing entity also
needs a Recorder/statistics continuity check. Never update generated files by
hand.

### 5. Link the two commits

Commit the GII evidence/review change first. The HA consumer commit should
include the GII commit in its message or review document and should state:

- which runtime files changed;
- which entities or services can change;
- whether units, signs, cumulative counters or statistics are affected;
- which tests and live checks were run;
- which conflicts remain open.

If HA work discovers a new semantic conflict, stop the promotion of that
interpretation, add the observation to GII, and keep the HA behaviour marked as
provisional until the shared review is resolved.

## Current transition state

The integration still contains Python runtime maps under
`custom_components/growatt_local/API/device_type/`. The local generated
`doc/register-spec/` output and older `doc/*.json` files are retained for
compatibility, migration and audit. They are not a second maintained semantic
truth alongside GII.

The target architecture is:

```text
GII evidence -> human review -> GII consolidated model -> generated GII spec
                                                        |
                                                        v
                                      HA pinned consumer projection/review
                                                        |
                                                        v
                                            HA runtime maps and tests
```

Until an automated consumer projection exists, every HA synchronization must
be a deliberate, pinned, reviewable change rather than an implicit copy.

## Consumer review checklist

- [ ] The source is an accepted GII commit, not an unreviewed local finding.
- [ ] `(family, table, address)` identity and applicability are recorded.
- [ ] Holding/input, function code, width, signedness and scaling were checked.
- [ ] Runtime declarations and generated compatibility views agree or the
      difference is documented.
- [ ] Entity IDs, units, signs, state classes and Recorder continuity were
      reviewed.
- [ ] Focused tests and required generated validators pass.
- [ ] The HA commit links to the exact GII commit and records open conflicts.
