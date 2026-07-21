---
name: 1-create-skill
description: >
  Thin entry for authoring skills. Loads 0-skill-creator (body craft/eval), then
  0-skill-manager for catalog place/ingest. Use when scaffolding a skill or
  /1-create-skill. Hub: /0-skill-creator.
disable-model-invocation: true
metadata:
  catalog:
    hub: 0-skill-creator
    role: wrapper
    when:
      - "scaffolding a skill or /1-create-skill"
    triggers:
      - "1-create-skill"
      - "create skill"
    requires_setup: false
---

# Create Skill

## Process

1. Follow the steps and hard rules in this skill.
2. Load linked `references/` only when the branch needs them.

## Boundary

| Need | Skill |
|------|--------|
| Scaffold / entry to author a skill | **create-skill** (this thin wrapper) |
| Craft body, evals, description quality | `/0-skill-creator` |
| Place / ingest into catalog | `/0-skill-manager` |
| Writing principles only | `/1-writing-great-skills` |
| Discover installable skills | `/1-discover-skills` |
| Which skill to use | `/0-butler` |


Thin wrapper.

1. Load **`/0-skill-creator`** for create/edit/eval of the skill body.
2. **Name with depth prefix (hard):** plan `{depth}-{kebab-slug}` for dir + frontmatter `name` (★ hub → `0-`; hub child → `1-`; deeper → `2+`). See `0-skill-manager/references/depth-prefix-names.md`.
3. **Route surface before place:** description contract + `metadata.catalog` (`hub`, `role`, `when`|`triggers`); never top-level route keys — [skill-route-surface.md](../0-skill-manager/references/skill-route-surface.md) (ADR 0009).
4. When ready for this catalog, load **`/0-skill-manager`** place or ingest (hub slot + **gate-route** + lint Gate: PASS; regenerates route-index).
5. Craft theory → `/1-writing-great-skills`. Routing → `/0-butler`. Catalog version / feature log → root `catalog.yaml` + `docs/FEATURE-LOG.md` (manager **release-note** only when house rules change).

## Don't use when

- Which skill should I use? → `/0-butler`
- Lint/rehouse only → `/0-skill-manager`
- Install from public ecosystem → `/1-discover-skills`
