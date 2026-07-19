---
name: create-skill
description: >
  Thin entry for authoring skills. Loads skill-creator (body craft/eval), then
  skill-manager for catalog place/ingest. Use when scaffolding a skill or /create-skill.
disable-model-invocation: true
---

# Create Skill

Thin wrapper.

1. Load **`/skill-creator`** for create/edit/eval of the skill body.
2. When ready for this catalog, load **`/skill-manager`** place or ingest (hub slot required).
3. Craft theory → `/writing-great-skills`. Routing → `/butler`.

## Don't use when

- Which skill should I use? → `/butler`
- Lint/rehouse only → `/skill-manager`
- Install from public ecosystem → `/find-skills`
