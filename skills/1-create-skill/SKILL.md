---
name: 1-create-skill
description: >
  Thin entry to author a skill: craft/eval via 0-skill-creator, then place via 0-skill-manager.
  Use when: scaffolding a new skill, /1-create-skill, or "create a skill for X".
  Not for: which skill to use (0-butler), lint-only (1-skill-linter), ecosystem install (1-discover-skills).
  Hub: /0-skill-creator.
disable-model-invocation: true
metadata:
  catalog:
    hub: 0-skill-creator
    role: wrapper
    when:
      - "scaffold or create a new skill"
      - "/1-create-skill"
    not_when:
      - "which skill → 0-butler"
      - "install public skill → 1-discover-skills"
      - "lint only → 1-skill-linter"
    next: [0-skill-creator, 0-skill-manager]
    cousins: [1-writing-great-skills, 1-discover-skills]
    triggers:
      - "create skill"
      - "1-create-skill"
      - "scaffold skill"
    requires_setup: false
---

# Create skill (wrapper)

## Boundary

| Need | Skill |
|------|--------|
| Entry / scaffold path | **this** |
| Body craft + evals | `/0-skill-creator` |
| Craft vocabulary only | `/1-writing-great-skills` |
| Place / ingest | `/0-skill-manager` |
| Discover installable skills | `/1-discover-skills` |
| Which local skill | `/0-butler` |

## Process

1. Load **`/0-skill-creator`** (full loop: intent → draft → eval → revise).  
   **Done when:** body is lean and job is clear.
2. Plan live identity: dir + `name` = `{depth}-{kebab-slug}` ([depth-prefix-names](../0-skill-manager/references/depth-prefix-names.md)).  
   **Done when:** depth matches planned hub parent.
3. Write **route surface** before place: description contract + `metadata.catalog` — [skill-route-surface](../0-skill-manager/references/skill-route-surface.md).  
   **Done when:** no top-level route keys; `hub` / `role` / `when`|`triggers` set.
4. When ready for this catalog → **`/0-skill-manager` place or ingest** (integration test + lint Gate PASS + route-index).  
   **Done when:** Gate PASS.
5. Theory-only questions → `/1-writing-great-skills`. Routing → `/0-butler`. House convention bumps → manager **release-note** only.

## Related

Parent: `/0-skill-creator` · F10 place fork in flows.
