# ADR 0006: skill-linter, hub membership, and sub-domain hubs

## Status

Accepted

## Context

Catalog health mixed abstract “lint” ops on skill-manager with a partial CI script. Many live skills are not attached to any domain hub workflow. Oversized SKILL.md files lack a standard path to split into sub-domain hubs. New skills can land without a health check of SKILL.md and references.

## Decision

### skill-linter

- **`/skill-linter`** (`productivity/skill-linter`) is the **per-skill and catalog health-check** skill.
- Parent domain hub: **skill-manager** (Catalog facilities). Link type: ops / pipeline leaf.
- skill-linter **reports only**. skill-manager **applies** fixes (place, new-hub, organize) after human confirm.
- skill-manager **lint** op loads skill-linter. create / place / ingest require a skill-lint pass (zero **critical**) before or immediately after apply as specified in skill-manager.

### Modes

`skill` · `hub` · `catalog` · `diff` — see skill-linter SKILL.md.

### Hub membership

- Every **live** skill under `engineering/`, `productivity/`, `misc/`, `personal/` **must** appear as a child of some domain hub in:
  - `productivity/butler/references/flows.md`, and/or
  - `hubs/{hub}/workflow.json` → `children[].skills`
- **Exempt:** `deprecated/`, `vendor/`. **in-progress/** → warn until placed.
- Ops tokens that are not skills (e.g. `create`, `read` in workflow ops lists) are not membership targets.

### Matt lean SKILL.md + chaining

skill-linter enforces **Matt Pocock–style** skills as the default:

- **Main `SKILL.md` stays lean** — ordered Process/Dispatch/Steps, short hard rules, Related/chain blurb; heavy material behind context pointers (`references/` or sibling `.md`). Theory: `/writing-great-skills`.
- **Size bar:** target ≤120 lines; warn `lean` above ~180 without disclosure map; `sprawl` above ~250; **new** skills above ~180 without map → `gate-lean` **critical** (block place/ingest).
- **Chaining:** every live skill has a hub slot; pipeline skills name **next** (and often prev); hard-deps for to-spec/to-tickets/triage → `/setup-rohitas-skills`. Thin examples: `/implement`, `/tdd`, `/to-spec`.

### Sprawl → sub-domain hub

When SKILL.md is too large or multi-pipeline after lean options fail, skill-linter emits `sprawl` / `subdomain-candidate`. Remediation order:

1. **Thin** SKILL.md (progressive disclosure).
2. **Chain** place under domain hub with prev/next.
3. Prefer **split** into child skills + thin router, or
4. Create a **sub-domain hub** package `hubs/{sub-hub}/` with `hub.html` + `workflow.json`:
   - `parent` remains **butler** (house apex, ADR 0005)
   - `parent_domain_hub` names the owning domain hub (e.g. `skill-manager`)
   - Parent domain lists the sub-hub with `link_type: "sub-hub"`
5. Re-run skill-linter.

### Mandatory lint on new skills

| Op | Gate |
|----|------|
| place / ingest apply | integration test includes skill-lint; no critical findings |
| create (after body craft) | place plan includes skill-lint |
| new-hub | lint hub package + child membership |

## Consequences

- Orphans are **critical** in catalog/skill lint (report backlog; do not silent-promote).
- CI `scripts/lint-skills` automates a subset (name-dir, refs, hub-member, sprawl counts).
- Agents must not invent skills outside hub workflows.
