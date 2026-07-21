---
name: 1-skill-linter
description: >
  Health-check agent skills for lean SKILL.md, chaining, hub membership, route surface,
  and sprawl. Reports only — skill-manager applies fixes. Use when linting a skill or catalog after
  create/place/ingest. Not for: rewriting skills (0-skill-creator), placing (0-skill-manager).
  Hub: /0-skill-manager. Triggers: skill lint, /1-skill-linter, catalog health.
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
    prev: [0-skill-manager]
    triggers:
      - "skill lint"
      - "1-skill-linter"
      - "catalog health"
    requires_setup: false
---

# Skill Linter

Report catalog and skill health. You **do not** rehouse, place, or rewrite skills — hand mutations to **`/0-skill-manager`** / **`/0-skill-creator`**.

**Parent hub:** `/0-skill-manager` · **Rules:** [ADR 0006](../../../docs/adr/0006-skill-linter-and-hub-membership.md) · [ADR 0009](../../../docs/adr/0009-catalog-route-surface-for-butler.md) · lean bar: [lean-structure.md](./references/lean-structure.md) · route surface: [skill-route-surface.md](../0-skill-manager/references/skill-route-surface.md) · theory: `/1-writing-great-skills` · version: root `catalog.yaml`

## Session start

1. Resolve **catalog root** (six folders: `skills/`, `inbox/`, `archive/`, `hubs/`, `guidelines/`, `wikis/`).
2. Note hub SSOT: `skills/0-butler/references/flows.md` and packages under `hubs/`; catalog version from `catalog.yaml`.
3. Choose **mode** (ask if unclear). Default after create/place/ingest/**update**: **skill**.
4. Load checklists under `references/` as needed — always apply **lean + chaining + route surface**.
5. Prefer also running `scripts/lint-skills` for CI-parity (prints catalog version).
6. Emit report per [report-format.md](./references/report-format.md).

## Modes

| Mode | Scope |
|------|--------|
| **skill** | One skill directory (`bucket/name` or path) |
| **hub** | One domain hub + skills listed in its workflow/flows children |
| **catalog** | All live skills under `skills/` |
| **diff** | Paths the user lists or git-changed skill dirs |

## Dispatch

1. Collect targets for the mode.
2. Run checks from [skill-lint-checklist.md](./references/skill-lint-checklist.md) groups **A–F** (includes route codes).
3. Enforce **lean main SKILL.md** + **lean shape** via [lean-structure.md](./references/lean-structure.md).
4. Enforce **route surface** (ADR 0009): `description-triggers`, `route-top-level`, `route-hub`, `gate-route` on new place/update of frontmatter.
5. Resolve hub membership + chain slot via [hub-membership.md](./references/hub-membership.md).
6. Apply sprawl / sub-domain rules from [sprawl-and-subdomain.md](./references/sprawl-and-subdomain.md) only after thin+chain options.
7. Print structured report. **Critical > 0** ⇒ fail gate for 0-skill-manager apply.
8. If fixes needed: hand off **`/0-skill-creator`** (thin body / catalog fields), **`/0-skill-manager`** (place / new-hub / organize / regen route-index), and/or **`/1-skill-atomize`** — do not mutate yourself.

## What “pass” looks like (lean default)

- **Depth-prefix name (hard):** dir + frontmatter `name` = `{depth}-{kebab-slug}` (`0-` hub, `1-` child, …). Codes: `depth-prefix`, `depth-hub`. Rule: `0-skill-manager/references/depth-prefix-names.md`.
- **Route surface:** description when-to-use signal + `metadata.catalog` (`hub`, `role`, when/triggers); **no** top-level route keys.
- `SKILL.md` is a **thin router**: frontmatter, short purpose, ordered Process/Dispatch/Steps, hard rules bullets, Related/next chain.
- Heavy templates, rubrics, glossaries live in **sibling `.md` or `references/`** with context pointers.
- Skill sits on a **chain**: parent hub + link type; pipeline skills name **next** (and often prev); hard-deps call `/0-setup-rohitas-skills` when required.
- Size targets: **≤120 lines** ideal; **>180** needs disclosure map; **>250** is sprawl; **new** skills **>180** without map → `gate-lean` critical.

Good examples: `/0-implement`, `/1-tdd`, `/1-to-spec`, `/1-grill-with-docs`.

## Automation

```bash
# from catalog root
./scripts/lint-skills              # prints catalog.yaml version; Gate PASS = 0 critical
./scripts/generate-route-index     # after place/update of catalog membership
```

Script covers name-dir, ref-exists, hub-member, lean/sprawl, depth-prefix, route-top-level, description-triggers, route-index staleness. Full lean-shape, chain-next judgment, and gate-route for “new” place stay with this skill + skill-manager.

## Handoffs

| Need | Skill |
|------|--------|
| Apply place / new-hub / organize | `/0-skill-manager` |
| Content overlap / one-job + Boundary + forks | `/1-skill-atomize` |
| Thin / rewrite SKILL.md to lean | `/0-skill-creator` (+ `/1-writing-great-skills`) |
| Which skill to use | `/0-butler` |

When report flags missing Boundary, cousin trigger collision, or dual full procedures for the same job, prefer **`/1-skill-atomize`** over ad-hoc edits.

## Hard rules

1. **Report only** — no multi-file catalog writes.
2. **Depth-prefix names** — live skills must be `{depth}-{slug}` for full hub-tree depth `max(parent+1)` through max tree depth, including **3- / 4- / 5- / 6-** when the tree reaches them (`depth-prefix` / `depth-hub` / `depth-graph` / `gate-depth-prefix`).
3. **Lean SKILL.md** — main file stays lean; progressive disclosure, not inlined books.
4. **Chain** — live skills have hub membership + chain slot; pipeline skills expose next steps.
5. **Hub membership** — orphans are critical (ADR 0006).
6. **No invent** — do not invent skills or hubs; only report gaps.
7. **Sprawl** — prefer thin + chain + split; sub-domain hub last (sub-hub packages are `1-`).
8. **New skill gate** — 0-skill-manager must not place/ingest/update-frontmatter with skill-lint criticals (`depth-prefix`, `gate-lean`, `gate-route`, `route-top-level` included).
