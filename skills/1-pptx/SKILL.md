---
name: 1-pptx
description: >
  Create/read/edit PowerPoint (.pptx) decks. Use when slides/deck/presentation or .pptx
  is involved. Not for: Word (1-docx), HTML design slides under UI hub (1-slides), spreadsheets (1-xlsx).
  Hub: /0-office. Triggers: pptx, slides, deck, presentation.
disable-model-invocation: true
license: Proprietary. LICENSE.txt has complete terms
metadata:
  catalog:
    hub: 0-office
    role: leaf
    when:
      - ".pptx / slide deck work"
    not_when:
      - "word → 1-docx"
      - "design HTML slides → 1-slides"
      - "sheet → 1-xlsx"
    triggers:
      - "pptx"
      - "slides"
      - "deck"
      - "presentation"
    requires_setup: false
---

# PPTX Skill

Purpose router for **`/1-pptx`**. Full procedure: [references/full-guide.md](./references/full-guide.md).

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
