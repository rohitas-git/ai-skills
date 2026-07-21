---
name: 1-docx
description: >
  Create/read/edit Word documents (.docx). Use when the deliverable or input is a Word
  doc, report, memo, letter, or .docx. Not for: PDFs, spreadsheets (1-xlsx), presentations (1-pptx).
  Hub: /0-office. Triggers: word doc, .docx, memo, letterhead.
disable-model-invocation: true
license: Proprietary. LICENSE.txt has complete terms
metadata:
  catalog:
    hub: 0-office
    role: leaf
    when:
      - ".docx / Word document work"
    not_when:
      - "spreadsheet → 1-xlsx"
      - "slides → 1-pptx"
    triggers:
      - "word"
      - "docx"
      - "memo"
      - "letter"
    requires_setup: false
---

# DOCX creation, editing, and analysis

Purpose router for **`/1-docx`**. Full procedure: [references/full-guide.md](./references/full-guide.md).

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
