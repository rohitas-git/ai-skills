---
name: 0-skill-creator
description: >
  Create, edit, and evaluate agent skills (body craft, evals, description
  optimization). Use when authoring a skill from scratch or improving one.
  Not catalog place (/0-skill-manager) or thin entry (/1-create-skill).
disable-model-invocation: true
---

# Skill Creator

## Boundary

| Need | Skill |
|------|--------|
| Craft/eval skill body | **skill-creator** (this) |
| Thin catalog entry wrapper | `/1-create-skill` |
| Place / ingest into this catalog | `/0-skill-manager` |
| Writing principles | `/1-writing-great-skills` |
| Lint only | `/1-skill-linter` |
| Discover ecosystem skills | `/1-discover-skills` |

## Process

1. Load full craft/eval procedure: [references/full-guide.md](./references/full-guide.md).
2. Draft or edit the skill body to Matt-lean shape (thin SKILL.md + `references/`).
3. When ready for this catalog → `/0-skill-manager` place or ingest (skill-lint Gate: PASS).

## Progressive disclosure

| Load when | File |
|-----------|------|
| Full create/eval loop | [references/full-guide.md](./references/full-guide.md) |

## Related

Parent hub: `/0-skill-creator` (Author) · next: `/0-skill-manager` place.
