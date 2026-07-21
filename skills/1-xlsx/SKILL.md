---
name: 1-xlsx
description: >
  Create/read/edit spreadsheets (.xlsx/.csv). Use when spreadsheet is primary input/output.
  Not for: Word (1-docx), slides (1-pptx), databases/pipelines. Hub: /0-office.
  Triggers: xlsx, spreadsheet, csv, tabular data file.
disable-model-invocation: true
license: Proprietary. LICENSE.txt has complete terms
metadata:
  catalog:
    hub: 0-office
    role: leaf
    when:
      - "spreadsheet primary deliverable"
      - ".xlsx/.csv work"
    not_when:
      - "word → 1-docx"
      - "pptx → 1-pptx"
    triggers:
      - "xlsx"
      - "spreadsheet"
      - "csv"
    requires_setup: false
---

# Requirements for Outputs

Purpose router for **`/1-xlsx`**. Full procedure: [references/full-guide.md](./references/full-guide.md).

## Process

1. Read [references/full-guide.md](./references/full-guide.md) for full steps, templates, and detail.
2. Execute the procedure from that guide.
3. Stay within this skill's Boundary (above or in guide).

## Progressive disclosure

| Load when | File |
|-----------|------|
| Full workflow / detail | [references/full-guide.md](./references/full-guide.md) |

## Related

See Boundary table and hub membership in `skills/0-butler/references/flows.md`.
