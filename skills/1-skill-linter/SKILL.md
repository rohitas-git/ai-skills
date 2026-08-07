---
name: 1-skill-linter
description: >
  Report skill/catalog health: lean SKILL.md, depth-prefix, hub membership, route surface, sprawl.
  Reports only — does not place or rewrite. Use when: after create/place/ingest, /1-skill-linter, catalog health.
  Not for: apply fixes (0-skill-manager), thin rewrite (0-skill-creator), atomize overlap (1-skill-atomize).
  Hub: /0-skill-manager.
disable-model-invocation: true
metadata:
  catalog:
    hub: 0-skill-manager
    role: pipeline
    when:
      - "lint skill or catalog health"
      - "gate after place/ingest"
    not_when:
      - "apply place/organize → 0-skill-manager"
      - "thin rewrite → 0-skill-creator"
      - "overlap reorg → 1-skill-atomize"
    prev: [0-skill-manager]
    cousins: [1-skill-atomize, 0-skill-creator]
    triggers:
      - "skill lint"
      - "1-skill-linter"
      - "catalog health"
    requires_setup: false
---

# Skill linter

**Report only.** Mutations → `/0-skill-manager` · lean craft → `/0-skill-creator` + `/1-writing-great-skills`.

**Rules:** [ADR 0006](../../docs/adr/0006-skill-linter-and-hub-membership.md) · [ADR 0009](../../docs/adr/0009-catalog-route-surface-for-butler.md) · [lean-structure](./references/lean-structure.md) · [skill-route-surface](../0-skill-manager/references/skill-route-surface.md) · theory `/1-writing-great-skills`

## Process

1. Resolve catalog root + `catalog.yaml` version + flows/hubs SSOT.  
2. Choose **mode** (default after place/ingest: **skill**).  
3. Collect targets → run [skill-lint-checklist](./references/skill-lint-checklist.md) A–F.  
4. Enforce lean shape + route surface + hub membership ([hub-membership](./references/hub-membership.md)).  
5. Sprawl/sub-domain only after thin+chain options ([sprawl-and-subdomain](./references/sprawl-and-subdomain.md)).  
6. Prefer `./scripts/lint-skills` for CI-parity.  
7. Emit report ([report-format](./references/report-format.md)). **Critical > 0** ⇒ fail place/ingest gate.  
8. Hand off fixes — do not mutate.

## Modes

| Mode | Scope |
|------|--------|
| skill | One skill dir |
| hub | Domain hub + children |
| catalog | All `skills/` |
| diff | Listed or git-changed paths |

## Pass bar (lean)

| Bar | |
|-----|--|
| Identity | `{depth}-{slug}` name == dir |
| Route | description triggers + `metadata.catalog`; no top-level route keys |
| Shape | Thin router + disclosure pointers; not a book |
| Chain | Hub member; pipeline names next |
| Size | ≤120 ideal; >180 needs map; >250 sprawl; new >180 without map → `gate-lean` critical |

Examples of lean routers: `/0-implement`, `/1-tdd`, `/1-to-spec`.

## Automation

```bash
./scripts/lint-skills           # Gate PASS = 0 critical
./scripts/generate-route-index  # after membership/frontmatter change
```

## Handoffs

| Finding | Who |
|---------|-----|
| Place / organize / new-hub | `/0-skill-manager` |
| Missing Boundary / dual job | `/1-skill-atomize` |
| Fat body / bad description | `/0-skill-creator` + `/1-writing-great-skills` |
| Which skill | `/0-butler` |

## Hard rules

1. Report only — no multi-file catalog writes.  
2. Depth-prefix + hub membership critical.  
3. Lean + progressive disclosure.  
4. No inventing skills/hubs.  
5. New place/ingest fails on any critical (incl. `gate-route`, `gate-lean`, `route-top-level`).

## Related

Parent: `/0-skill-manager`.
