---
name: skill-linter
description: >
  Health-check agent skills for Matt-style lean SKILL.md, chaining (prev/next/hub),
  references, hub membership, and sprawl. Reports only — skill-manager applies fixes.
  Use after create/place/ingest, for catalog lint, or /skill-linter. Parent hub:
  skill-manager.
disable-model-invocation: true
---

# Skill Linter

Report catalog and skill health. You **do not** rehouse, place, or rewrite skills — hand mutations to **`/skill-manager`** / **`/skill-creator`**.

**Parent hub:** `/skill-manager` · **Rules:** [ADR 0006](../../../docs/adr/0006-skill-linter-and-hub-membership.md) · lean bar: [matt-lean-structure.md](./references/matt-lean-structure.md) · theory: `/writing-great-skills`

## Session start

1. Resolve **catalog root** (six folders: `skills/`, `inbox/`, `archive/`, `hubs/`, `guidelines/`, `wikis/`).
2. Note hub SSOT: `skills/butler/references/flows.md` and packages under `hubs/`.
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
6. Print structured report. **Critical > 0** ⇒ fail gate for skill-manager apply.
7. If fixes needed: hand off **`/skill-creator`** (thin body), **`/skill-manager`** (place / new-hub / organize), and/or **`/skill-atomize`** (overlap → Boundary + forks) — do not mutate yourself.

## What “pass” looks like (Matt default)

- `SKILL.md` is a **thin router**: frontmatter, short purpose, ordered Process/Dispatch/Steps, hard rules bullets, Related/next chain.
- Heavy templates, rubrics, glossaries live in **sibling `.md` or `references/`** with context pointers.
- Skill sits on a **chain**: parent hub + link type; pipeline skills name **next** (and often prev); hard-deps call `/setup-rohitas-skills` when required.
- Size targets: **≤120 lines** ideal; **>180** needs disclosure map; **>250** is sprawl; **new** skills **>180** without map → `gate-lean` critical.

Good examples: `/implement`, `/tdd`, `/to-spec`, `/grill-with-docs`.

## Automation

```bash
# from AI-Skills monorepo root
./scripts/lint-skills
```

Script covers name-dir, ref-exists, hub-member, lean/sprawl line counts. Full Matt-shape, chain-next, and disclosure judgment stay with this skill (agent).

## Handoffs

| Need | Skill |
|------|--------|
| Apply place / new-hub / organize | `/skill-manager` |
| Content overlap / one-job + Boundary + forks | `/skill-atomize` |
| Thin / rewrite SKILL.md to Matt lean | `/skill-creator` (+ `/writing-great-skills`) |
| Which skill to use | `/butler` |

When report flags missing Boundary, cousin trigger collision, or dual full procedures for the same job, prefer **`/skill-atomize`** over ad-hoc edits.

## Hard rules

1. **Report only** — no multi-file catalog writes.
2. **Lean SKILL.md** — main file stays Matt-thin; depth is disclosed, not inlined.
3. **Chain** — live skills have hub membership + chain slot; pipeline skills expose next steps.
4. **Hub membership** — orphans are critical (ADR 0006).
5. **No invent** — do not invent skills or hubs; only report gaps.
6. **Sprawl** — prefer thin + chain + split; sub-domain hub last.
7. **New skill gate** — skill-manager must not place/ingest with skill-lint criticals (`gate-lean` included).
