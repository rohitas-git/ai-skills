---
name: 0-skill-creator
description: >
  Create, edit, and evaluate agent skill bodies — draft, eval pressure, description triggers.
  Use when: authoring or improving a skill file, skill evals, optimize description.
  Not for: place/ingest (0-skill-manager), which skill (0-butler), craft theory only (1-writing-great-skills).
  Hub: /0-skill-creator.
disable-model-invocation: true
metadata:
  catalog:
    hub: 0-skill-creator
    role: hub
    when:
      - "author or improve skill body"
      - "eval skill descriptions"
    not_when:
      - "place/ingest → 0-skill-manager"
      - "which skill → 0-butler"
    next: [0-skill-manager]
    cousins: [1-create-skill, 1-writing-great-skills, 1-skill-linter]
    triggers:
      - "create skill"
      - "improve skill"
      - "skill evals"
    requires_setup: false
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
2. Draft or edit the skill body to lean shape (thin SKILL.md + `references/`). Prefer `## Process` / Dispatch / Steps.
3. **Route surface (required for this catalog)** — see [skill-route-surface.md](../0-skill-manager/references/skill-route-surface.md) · [ADR 0009](../../docs/adr/0009-catalog-route-surface-for-butler.md):
   - `description`: Use when (or Use for) + Not for (cousins) + Hub
   - `metadata.catalog`: `hub`, `role`, `when` or `triggers` (optional `not_when`, `next`, `prev`, `cousins`, `requires_setup`)
   - **Forbidden:** top-level `hub` / `when` / `not_when` / `next` / `prev` / `cousins` / `triggers` / `role`
4. **Update existing skill:** if editing description or routing intent, keep `metadata.catalog` in sync (hub/role/when/triggers/next). Do not strip unrelated `metadata` keys (`author`, `license` companions stay).
5. When ready for this catalog → `/0-skill-manager` **place** or **ingest** (Gate: PASS includes `gate-route`). Manager regenerates route-index.
6. Convention-only changes that affect the whole house → manager **release-note** (`catalog.yaml` + FEATURE-LOG), not this skill.

## Progressive disclosure

| Load when | File |
|-----------|------|
| Full create/eval loop (ops) | [references/full-guide.md](./references/full-guide.md) |
| Portable layout vs house place rules | [references/agentskills-io-specification.md](./references/agentskills-io-specification.md) |
| Designing cases / assertions / grade patterns | [references/agentskills-io-evaluating-skills.md](./references/agentskills-io-evaluating-skills.md) |
| Bundling helpers or agentic CLI scripts | [references/agentskills-io-using-scripts.md](./references/agentskills-io-using-scripts.md) |
| Description misses or false fires (trigger eval) | [references/agentskills-io-optimizing-descriptions.md](./references/agentskills-io-optimizing-descriptions.md) |
| Craft theory (predictability, prune, leading words) | `/1-writing-great-skills` |
| Route surface schema | [../0-skill-manager/references/skill-route-surface.md](../0-skill-manager/references/skill-route-surface.md) |

## Related

Parent hub: `/0-skill-creator` (Author) · next: `/0-skill-manager` place · lint: `/1-skill-linter`.
