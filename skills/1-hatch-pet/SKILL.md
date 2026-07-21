---
name: 1-hatch-pet
description: >
  Create, repair, validate, visually QA, and package Codex-compatible v2 animated pets
  from character art, generated images, company or prospect brand cues, or visual
  references. Use for any new Codex pet, custom mascot, non-pixel pet style,
  brand-inspired pet, existing-pet repair, or 8x11 spritesheet workflow requiring all 9
  standard animation rows, 16 look directions, deterministic assembly, QA artifacts, and
  spriteVersionNumber 2 packaging. Use when: Create, repair, validate, visually QA, and
  package Codex-compatible v2 animated pets from character. Hub: /0-office.
disable-model-invocation: true
metadata:
  catalog:
    hub: 0-office
    role: leaf
    when:
      - "Create, repair, validate, visually QA, and package Codex-compatible v2 animated pets from character"
    triggers:
      - "1-hatch-pet"
      - "hatch pet"
    requires_setup: false
---

# Hatch Pet

Purpose router for **`/1-hatch-pet`**. Full procedure: [references/full-guide.md](./references/full-guide.md).

## Process

1. Read [references/full-guide.md](./references/full-guide.md) for full steps, templates, and detail.
2. Execute the procedure from that guide.
3. Stay within this skill's Boundary (above or in guide).

## Progressive disclosure

| Load when | File |
|-----------|------|
| Full workflow / detail | [references/full-guide.md](./references/full-guide.md) |
| Detail | [references/animation-rows.md](./references/animation-rows.md) |
| Detail | [references/qa-rubric.md](./references/qa-rubric.md) |
| Detail | [references/codex-pet-contract.md](./references/codex-pet-contract.md) |

## Related

See Boundary table and hub membership in `skills/0-butler/references/flows.md`.
