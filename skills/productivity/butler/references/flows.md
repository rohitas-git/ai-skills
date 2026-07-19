# Flows — hub map + pipelines + forks (SSOT)

**Butler** reads this map to route. **skill-manager** writes hub slots when placing skills.

## Patterns

### Hub

Each **workflow domain** has exactly one **★ top skill (hub)**. Children link by type: `wrapper` · `hard` · `soft` · `pipeline` · `on-ramp` · `leaf` · `axis` · `satellite`.

### Fork (◆)

Any branch in a pipeline is a **fork**. Agents **must ask the user** one question (recommended option first) and wait — never silent branch.

---

## Domain 0 — House (hub of hubs)

| | |
|--|--|
| **★ Hub** | `/butler` |
| **Children** | All domain hubs below (routing targets) |
| **Mutations** | **Not here** → `/skill-manager` |

**Pipeline:** orient → query → domain hub (or delegate skill-manager).

---

## Domain 1 — Setup

| | |
|--|--|
| **★ Hub** | `/setup-rohitas-skills` |
| **Children** | **hard:** `to-spec`, `to-tickets`, `triage` · **soft:** `tdd`, `diagnosing-bugs`, `improve-codebase-architecture`, vocabulary skills · **SSOT:** issue-tracker, triage-labels, domain, vault |

**Pipeline:** run once per consumer repo.

| Fork | Question | Recommended | Branches |
|------|----------|-------------|----------|
| **F1** | Setup already done (`docs/agents/` present)? | Skip if present | run setup · skip → Design/Ship |

---

## Domain 2 — Design

| | |
|--|--|
| **★ Hub** | `/grilling` |
| **Children** | **wrapper:** `grill-me`, `grill-with-docs` · **pull-in:** `domain-modeling` · **detour:** `handoff` ⇄ `prototype` |

| Fork | Question | Recommended | Branches |
|------|----------|-------------|----------|
| **F2** | Codebase present? | Yes → grill-with-docs | `grill-with-docs` · `grill-me` |
| **F3** | Need a runnable prototype answer? | No | stay in grill · handoff⇄prototype |
| **F4** | Multi-session build? | Yes if >1 implement slice | yes → Ship multi · no → Ship single |

**Merge out:** → Domain 3 Ship.

---

## Domain 3 — Ship

| | |
|--|--|
| **★ Hub** | `/implement` |
| **Children** | **pipeline:** `to-spec` → `to-tickets` → `implement` → `tdd` → `code-review` → commit · **cousin:** `check-work` (mid-build only) |

| Fork | Question | Recommended | Branches |
|------|----------|-------------|----------|
| **F4** | (entry) multi-session? | as Design | to-spec path · direct implement |
| **F5** | This slice done? | run closer | tdd→code-review→commit · more tickets |
| **F6** | (inside code-review) axes applicable? | every applicable | Spec / Standards / Maintainability on or soft-skip |

**Multi-session pipeline:**

```text
to-spec → to-tickets → implement* → tdd → code-review (multi-axis) → commit
```

**Single-session:** `implement*` → tdd → code-review → commit.

---

## Domain 4 — Review

| | |
|--|--|
| **★ Hub** | `/code-review` |
| **Children** | **axis:** Spec, Standards, Maintainability · **cousin:** `check-work`, `ponytail-review`, `codebase-review-strategy` · **†** `code-review-v2` |

Fork **F6** — ask only to force/skip axes when user wants override; default = scan and run applicable.

---

## Domain 5 — Triage

| | |
|--|--|
| **★ Hub** | `/triage` |
| **Children** | merge → `implement` |
| **Rule** | Never re-triage `to-tickets` output |

---

## Domain 6 — Diagnose

| | |
|--|--|
| **★ Hub** | `/diagnosing-bugs` |
| **Children** | `tdd`; optional on-ramp → `improve-codebase-architecture` |

---

## Domain 7 — Fog map

| | |
|--|--|
| **★ Hub** | `/wayfinder` |
| **Children** | exit **only** → `to-spec` (then Ship) |

| Fork | Question | Recommended | Branches |
|------|----------|-------------|----------|
| **F8** | Fog clear enough to build? | only when buildable | stay wayfinder · → to-spec |

---

## Domain 8 — Architecture

| | |
|--|--|
| **★ Hub** | `/improve-codebase-architecture` |
| **Children** | **vocab:** `codebase-design` · **persona:** `software-architect` · **†** `software-architecture` |

| Fork | Question | Recommended | Branches |
|------|----------|-------------|----------|
| **F9** | Take a deepening idea to Design? | if user picks one | stay · → grill-with-docs |

---

## Domain 9 — Vault

| | |
|--|--|
| **★ Hub** | `/rohitas-vault-wiki` |
| **Children** | **pipeline/ops:** `vault-inbox` → `vault-ingest` → `vault-lint` / `wiki-query` / `vault-explain` · **leaf primitives:** `obsidian-markdown`, `obsidian-cli`, `obsidian-bases` · **†** `obsidian-notes-manager` |

| Fork | Question | Recommended | Branches |
|------|----------|-------------|----------|
| **F11** | Capture / compile / query / lint / explain? | match utterance | inbox · ingest · query · lint · explain |

Vault root path from setup SSOT only.

---

## Domain 10 — Catalog facilities

| | |
|--|--|
| **★ Hub** | `/skill-manager` |
| **Children** | ops: create/read/update/delete/place/new-hub/ingest/organize/lint · handoff body craft → `skill-creator` |

Not a product feature pipeline — **mutates the catalog**.

---

## Domain 11 — Author body

| | |
|--|--|
| **★ Hub** | `/skill-creator` |
| **Children** | **wrapper:** `create-skill` · craft: `writing-great-skills` · next: skill-manager place |

| Fork | Question | Recommended | Branches |
|------|----------|-------------|----------|
| **F10** | Ingest/place into catalog now? | yes when ready | stay crafting · skill-manager place/ingest |

---

## Domain 12 — Simplify

| | |
|--|--|
| **★ Hub** | `/ponytail` |
| **Children** | **satellite:** ponytail-review, audit, debt, gain, help |

Optional; not Ship closer.

---

## Domain 13 — Learn

| | |
|--|--|
| **★ Hub** | `/learn` |
| **Children** | `learning-explainer`, `teach`, `story-teacher`, `resource-summarizer` |

---

## Domain 14 — Misc / office

| | |
|--|--|
| **★ Hub** | `/misc` |
| **Children** | **leaf:** `docx`, `pptx`, `xlsx`, `diagram-maker`, `imagine`, `hatch-pet`, `json-canvas`, `defuddle` |

| Fork | Question | Recommended | Branches |
|------|----------|-------------|----------|
| **F-misc** | What artifact type? | from extension/context | document · slides · sheet · diagram · image · canvas · web · pet |

**Tree:** hub → leaf (not a long chain).

---

## Global entry fork

| Fork | Question | Recommended | Branches |
|------|----------|-------------|----------|
| **F7** | What kind of work? | feature → Design | Design · Triage · Diagnose · Fog · Architecture · Vault · Misc · Catalog facilities · Learn · Simplify |

Butler asks **F7** when intent is unclear.

---

## Deprecated (†)

| Tombstone | Successor hub / skill |
|-----------|------------------------|
| ask-matt | butler |
| code-review-v2 | code-review |
| software-architecture | improve-codebase-architecture / codebase-design |
| obsidian-notes-manager | rohitas-vault-wiki |
| task-observer | reflect + skill-manager |
| continuous-learning-v2 | reflect |

---

## ASCII — main product path

```text
        ★ butler (route only)
               │
        ★ setup-rohitas-skills  (F1)
               │
        ★ grilling  (F2 wrappers · F3 proto · F4 multi?)
               │
     ┌─────────┴─────────┐
   multi               single
     │                   │
  to-spec                │
  to-tickets             │
     └─────────┬─────────┘
               ▼
        ★ implement → tdd → ★ code-review (F6 axes) → commit
```
