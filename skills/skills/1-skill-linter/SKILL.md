---
name: 1-skill-linter
description: >
  Health-check agent skills for Matt-style lean SKILL.md, chaining (prev/next/hub),
  references, hub membership, and sprawl. Reports only — 0-skill-manager applies fixes.
  Use after create/place/ingest, for catalog lint, or /1-skill-linter. Parent hub:
  skill-manager.
disable-model-invocation: true
---

# Skill Linter

Report catalog and skill health. You **do not** rehouse, place, or rewrite skills — hand mutations to **`/0-skill-manager`** / **`/0-skill-creator`**.

**Parent hub:** `/0-skill-manager` · **Rules:** [ADR 0006](../../../docs/adr/0006-skill-linter-and-hub-membership.md) · lean bar: [matt-lean-structure.md](./references/matt-lean-structure.md) · theory: `/1-writing-great-skills`

## Session start

1. Resolve **catalog root** (six folders: `skills/`, `inbox/`, `archive/`, `hubs/`, `guidelines/`, `wikis/`).
2. Note hub SSOT: `skills/0-butler/references/flows.md` and packages under `hubs/`.
3. Choose **mode** (ask if unclear). Default after create/place/ingest: **skill**.
4. Load checklists under `references/` as needed — always apply **Matt lean + chaining**.
5. Emit report per [report-format.md](./references/report-format.md).

## Modes

| Mode | Scope |
|------|--------|
| **skill** | One skill directory (`bucket/name` or path) |
| **hub** | One domain hub + skills listed in its workflow/flows children |
| **catalog** | All live skills under `skills/` |
| **diff** | Paths the user lists or git-changed skill dirs |

## Dispatch

1. Collect targets for the mode.
2. Run checks from [skill-lint-checklist.md](./references/skill-lint-checklist.md) groups **A–F**.
3. Enforce **lean main SKILL.md** + **Matt shape** via [matt-lean-structure.md](./references/matt-lean-structure.md).
4. Resolve hub membership + chain slot via [hub-membership.md](./references/hub-membership.md).
5. Apply sprawl / sub-domain rules from [sprawl-and-subdomain.md](./references/sprawl-and-subdomain.md) only after thin+chain options.
6. Print structured report. **Critical > 0** ⇒ fail gate for 0-skill-manager apply.
7. If fixes needed: hand off **`/0-skill-creator`** (thin body), **`/0-skill-manager`** (place / new-hub / organize), and/or **`/1-skill-atomize`** (overlap → Boundary + forks) — do not mutate yourself.

## What “pass” looks like (Matt default)

- `SKILL.md` is a **thin router**: frontmatter, short purpose, ordered Process/Dispatch/Steps, hard rules bullets, Related/next chain.
- Heavy templates, rubrics, glossaries live in **sibling `.md` or `references/`** with context pointers.
- Skill sits on a **chain**: parent hub + link type; pipeline skills name **next** (and often prev); hard-deps call `/0-setup-rohitas-skills` when required.
- Size targets: **≤120 lines** ideal; **>180** needs disclosure map; **>250** is sprawl; **new** skills **>180** without map → `gate-lean` critical.

Good examples: `/0-implement`, `/1-tdd`, `/1-to-spec`, `/1-grill-with-docs`.

## Automation

```bash
# from AI-Skills monorepo root
./scripts/lint-skills
```

Script covers name-dir, ref-exists, hub-member, lean/sprawl line counts. Full Matt-shape, chain-next, and disclosure judgment stay with this skill (agent).

## Handoffs

| Need | Skill |
|------|--------|
| Apply place / new-hub / organize | `/0-skill-manager` |
| Content overlap / one-job + Boundary + forks | `/1-skill-atomize` |
| Thin / rewrite SKILL.md to Matt lean | `/0-skill-creator` (+ `/1-writing-great-skills`) |
| Which skill to use | `/0-butler` |

When report flags missing Boundary, cousin trigger collision, or dual full procedures for the same job, prefer **`/1-skill-atomize`** over ad-hoc edits.

## Hard rules

1. **Report only** — no multi-file catalog writes.
2. **Lean SKILL.md** — main file stays Matt-thin; depth is disclosed, not inlined.
3. **Chain** — live skills have hub membership + chain slot; pipeline skills expose next steps.
4. **Hub membership** — orphans are critical (ADR 0006).
5. **No invent** — do not invent skills or hubs; only report gaps.
6. **Sprawl** — prefer thin + chain + split; sub-domain hub last.
7. **New skill gate** — 0-skill-manager must not place/ingest with skill-lint criticals (`gate-lean` included).
