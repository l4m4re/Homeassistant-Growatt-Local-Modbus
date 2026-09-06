# Protocol and native read blocks

## V1.24 / modern 120-family

- minimum command period: 850 ms
- recommended period: 1000 ms
- maximum read/write: 125 words
- native pages and family applicability are in the machine-readable `protocols.120_v124` object.

## V3.14 / 3.15 family

- minimum command period: 850 ms
- recommended period: 1000 ms
- maximum read/write: 45 words
- vendor grouping/boundary restrictions remain family-specific.

The five MIN/TL-XH pages in `native_read_evidence` are bounded live hardware
readability evidence. They are not a Home Assistant polling prescription and
do not promote every returned register to a verified semantic interpretation.
