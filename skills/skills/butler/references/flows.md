# Flows — hub map + pipelines + forks (SSOT)

**Butler** reads this map to route. **skill-manager** writes hub slots when placing skills.

## Patterns

### Hub

Each **workflow domain** has exactly one **★ top skill (hub)**. Children link by type: `wrapper` · `hard` · `soft` · `pipeline` · `on-ramp` · `leaf` · `axis` · `satellite` · `sub-hub`.

### Fork (◆)

Any branch in a pipeline is a **fork**. Agents **must ask the user** one question (recommended option first) and wait — never silent branch.

**Every fork’s options must include:**

| Option | Meaning |
|--------|---------|
| **Agent judgment** | The agent chooses the best branch (using the recommended default when unsure) and **proceeds without further fork questions** for this decision. User can still interrupt later. |

Concrete branches still appear first; **Agent judgment** is always listed last among choices so the user can hand full control to the agent. Do not invent a different name for this option.

---

## Domain 0 — House (hub of hubs)

| | |
|--|--|
| **★ Hub** | `/butler` |
| **Children** | All domain hubs below (routing targets): setup-rohitas-skills, grilling, implement, review, triage, diagnosing-bugs, wayfinder, improve-codebase-architecture, rohitas-vault-wiki, skill-manager, skill-creator, ponytail, learn, misc |
| **Session meta (soft)** | `grok-help`, `context-monitor`, `strategic-compact`, `response-effort-calibrator`, `handoff` (dual design) |
| **Mutations** | **Not here** → `/skill-manager` |

**Pipeline:** orient → query → domain hub (or delegate skill-manager).

**Artifacts (ADR 0005):** every domain hub (including butler) has a **flat package dir** (flat package under catalog `hubs/`):

```text
hubs/{hub}/
  hub.html          # non-butler pages parent-link butler; butler lists every hub
  workflow.json     # parent → butler (null only for butler)
```

Also: `hubs/index.html`, `hubs/manifest.json`, `hubs/flows-chart.html`.

flows.md remains SSOT for pipelines/forks; HTML/JSON are projections. **new-hub** must create the package via `/skill-manager`. Live skills stay in flat `skills/` leaves (`skills/`, …). Flat browse: `skills/<name>`. Index: `wikis/index.md`.

---

## Domain 1 — Setup

| | |
|--|--|
| **★ Hub** | `/setup-rohitas-skills` |
| **Children** | **hard:** `to-spec`, `to-tickets`, `triage` · **soft:** `tdd`, `diagnosing-bugs`, `improve-codebase-architecture`, vocabulary skills · **SSOT:** issue-tracker, triage-labels, domain, vault |

**Pipeline:** run once per consumer repo.

| Fork | Question | Recommended | Branches |
|------|----------|-------------|----------|
| **F1** | Setup already done (`docs/agents/` present)? | Skip if present | run setup · skip → Design/Ship · **Agent judgment** |

---

## Domain 2 — Design

| | |
|--|--|
| **★ Hub** | `/grilling` |
| **Children** | **wrapper:** `grill-me`, `grill-with-docs` · **pull-in:** `domain-modeling` · **soft:** `thinking-steel-manning` · **detour:** `handoff` ⇄ `prototype` |

| Fork | Question | Recommended | Branches |
|------|----------|-------------|----------|
| **F2** | Codebase present? | Yes → grill-with-docs | `grill-with-docs` · `grill-me` · **Agent judgment** |
| **F3** | Need a runnable prototype answer? | No | stay in grill · handoff⇄prototype · **Agent judgment** |
| **F4** | Multi-session build? | Yes if >1 implement slice | yes → Ship multi · no → Ship single · **Agent judgment** |

**Merge out:** → Domain 3 Ship.

---

## Domain 3 — Ship

| | |
|--|--|
| **★ Hub** | `/implement` |
| **Children** | **pipeline:** `to-spec` → `to-tickets` → `implement` → `tdd` → `code-review` → commit · **soft (style):** `coding-standards`, `code-comments`, `inline-comments`, `execution-flow-comments`, `stepdown-rule` · **cousin:** `verify-work` · **soft (git/PR):** `git-commit-helper`, `pr-summarizer`, `resolving-merge-conflicts` · **soft:** `research` · **soft (vendor harvest):** `shipping-and-launch`, `observability-and-instrumentation`, `ci-cd-and-automation`, `frontend-ui-engineering` |

| Fork | Question | Recommended | Branches |
|------|----------|-------------|----------|
| **F4** | (entry) multi-session? | as Design | to-spec path · direct implement · **Agent judgment** |
| **F5** | This slice done? | run closer | tdd→code-review→commit · more tickets · **Agent judgment** |
| **F6** | (inside code-review sub-hub) axes applicable? | every applicable | Spec / Standards / Maintainability on or soft-skip · **Agent judgment** |

**Multi-session pipeline:**

```text
to-spec → to-tickets → implement* → tdd → code-review (multi-axis) → commit
```

**Single-session:** `implement*` → tdd → code-review → commit.

**Note:** Ship lands on **`/code-review`** (Review **sub-hub**), not domain hub `/review`. Open-ended “which review?” → `/review` F-R1.

---

## Domain 4 — Review

| | |
|--|--|
| **★ Hub** | `/review` |
| **Children** | **sub-hub:** `code-review` · **sub-hub:** `security-auditor` · **soft:** `doubt-driven-development` · **on-ramp:** `codebase-review-strategy` · **soft (shared):** `security-and-hardening` · **soft (dual):** `software-architect` (primary Domain 8) |
| **Pipeline** | orient → **F-R1** pick mode → sub-hub / skill → optional remediation via `/security-and-hardening` |

| Fork | Question | Recommended | Branches |
|------|----------|-------------|----------|
| **F-R1** | What kind of review? | Multi-axis **change** review if PR/ship/diff | `/code-review` · `/security-auditor` · `/software-architect` · `/codebase-review-strategy` first · **Agent judgment** |
| **F6** | (inside `/code-review`) axes applicable? | every applicable | Spec / Standards / Maintainability on or soft-skip · **Agent judgment** |
| **F-R2** | (inside `/security-auditor`) audit scope? | full project unless path/PR named | full · scoped module · differential/PR · **Agent judgment** |

### Sub-hub `/code-review`

| | |
|--|--|
| **Role** | Multi-axis diff/PR closer (Ship + branch review) |
| **Children** | **axis:** Spec, Standards, Maintainability · **cousin:** `verify-work`, `ponytail-review` · **soft:** `software-architect`, `security-and-hardening` · **†** `code-review-v2` |

### Sub-hub `/security-auditor`

| | |
|--|--|
| **Role** | Multi-phase security/quality audit + structured findings |
| **Children** | **soft:** `security-and-hardening` (remediate / prevent after findings) |

`security-and-hardening` is listed under **both** sub-hubs (shared soft). Architecture deepen/survey stays Domain 8; only the persona dual-softs into Review for architecture *review*.

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
| **Children** | `tdd`; optional on-ramp → `improve-codebase-architecture` · **soft (vendor harvest):** `performance-optimization`, `browser-testing-with-devtools` |

---

## Domain 7 — Fog map

| | |
|--|--|
| **★ Hub** | `/wayfinder` |
| **Children** | exit **only** → `to-spec` (then Ship) |

| Fork | Question | Recommended | Branches |
|------|----------|-------------|----------|
| **F8** | Fog clear enough to build? | only when buildable | stay wayfinder · → to-spec · **Agent judgment** |

---

## Domain 8 — Architecture

| | |
|--|--|
| **★ Hub** | `/improve-codebase-architecture` |
| **Children** | **vocab:** `codebase-design` · **persona:** `software-architect` · **soft (principles):** `clean-craftsmanship` · **soft (always-on style):** `coding-standards` (also Ship) · **soft (docs):** `project-wiki-manager`, `living-documentation-governor` · **soft (vendor harvest):** `api-and-interface-design`, `deprecation-and-migration` · **†** `software-architecture` |

| Fork | Question | Recommended | Branches |
|------|----------|-------------|----------|
| **F9** | Take a deepening idea to Design? | if user picks one | stay · → grill-with-docs · **Agent judgment** |
| **F-C1** | Enforce standards on code now, or discuss clean-code principles? | coding while editing | `/coding-standards` · `/clean-craftsmanship` · **Agent judgment** |
| **F-D1** | Concept wiki (`docs/wiki`) or living docs + code triggers? | wiki if raw→concepts · living if drift/triggers | `/project-wiki-manager` · `/living-documentation-governor` · **Agent judgment** |

**Related atoms (not merge targets):** `coding-standards` ↔ `clean-craftsmanship` (F-C1); `project-wiki-manager` ↔ `living-documentation-governor` (F-D1); personal vault is Domain 9 (F-D2).

---

## Domain 9 — Vault

| | |
|--|--|
| **★ Hub** | `/rohitas-vault-wiki` |
| **Children** | **pipeline/ops:** `vault-inbox` → `vault-ingest` → `vault-lint` / `wiki-query` / `vault-explain` · **soft (Learn dual):** `resource-summarizer` (ingest distill) · **leaf primitives:** `obsidian-markdown`, `obsidian-cli`, `obsidian-bases` · **†** `obsidian-notes-manager` |
| **Learn handoff** | `vault-explain` → hard-load `/learning-explainer` (Learn domain); open-ended non-vault learning → `/learn` |

| Fork | Question | Recommended | Branches |
|------|----------|-------------|----------|
| **F11** | Capture / compile / query / lint / explain? | match utterance | inbox · ingest · query · lint · explain · **Agent judgment** |
| **F-D2** | Project repo wiki or personal Rohitas’s Notes vault? | vault if Concepts/Atlas/my notes | `/rohitas-vault-wiki` · `/project-wiki-manager` (or F-D1 if living docs) · **Agent judgment** |

Vault root path from setup SSOT only.

---

## Domain 10 — Catalog facilities

| | |
|--|--|
| **★ Hub** | `/skill-manager` |
| **Children** | ops: create/read/update/delete/place/new-hub/ingest/organize/lint/atomize · **pipeline:** `skill-linter` · **pipeline:** `skill-atomize` · **soft:** `session-skill-reflect`, `discover-skills` · handoff body craft → `skill-creator` |

Not a product feature pipeline — **mutates the catalog**.

**Lint:** `/skill-manager` lint op loads **`/skill-linter`**. Every live skill must be a hub member (ADR 0006). New place/ingest requires skill-lint Gate: PASS.

**Atomize:** `/skill-manager` atomize op loads **`/skill-atomize`**. Detect content overlap (exclude intentional hub links), dry-run Boundary + F# forks, confirm, apply, re-lint. Default resolution: keep both peers + hard redirects (not silent merge).

| Fork | Question | Recommended | Branches |
|------|----------|-------------|----------|
| **F-A1** | (inside skill-atomize) How far this pass? | high-overlap only | high · high+medium · full · **Agent judgment** |
| **F-A2** | Collision resolution? | keep both + Boundary + forks | keep-both · merge · split · **Agent judgment** |
| **F-A3** | Apply multi-file writes? | dry-run then confirm | dry-run · apply · **Agent judgment** |

---

## Domain 11 — Author body

| | |
|--|--|
| **★ Hub** | `/skill-creator` |
| **Children** | **wrapper:** `create-skill` · craft: `writing-great-skills` · next: skill-manager place |

| Fork | Question | Recommended | Branches |
|------|----------|-------------|----------|
| **F10** | Ingest/place into catalog now? | yes when ready | stay crafting · skill-manager place/ingest · **Agent judgment** |

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
| **Children** | **leaf:** `learning-explainer` (structured explain SSOT) · **leaf (soft cross (code object)):** `code-explainer` · **satellite:** `teach` (multi-session workspace) · **leaf:** `story-teacher` · **soft:** `resource-summarizer` · **on-ramp (Vault primary):** `vault-explain` → explainer · **tutor mode:** `learn/references/tutor-mode.md` (not a separate skill) |
| **Pipeline** | orient → **F-L1** pick mode → optional **F-L2** if long source → load one mode |

| Mode | Skill / load | Default when |
|------|----------------|--------------|
| Explain | `/learning-explainer` | “what is / explain / ELI5 / levels” |
| Tutor | tutor-mode refs under `/learn` | stuck on a problem, quiz, walk-through |
| Code walkthrough | `/code-explainer` | explain source code in editor/repo |
| Workspace course | `/teach` | multi-session directory lessons |
| Story | `/story-teacher` | teach via fiction |
| Summarize source | `/resource-summarizer` | distill long artifact for notes |
| Vault Concept | `/vault-explain` | explain `[[Note]]` from vault |

| Fork | Question | Recommended | Branches |
|------|----------|-------------|----------|
| **F-L1** | What kind of learning help? | Structured **explain** for concepts; **code-explainer** if object is code | explainer · tutor · code-explainer · teach · story · summarizer · vault-explain · **Agent judgment** |
| **F-L2** | Long source — summarize first? | Yes if raw blob is huge | summarizer first · skip to explain/tutor/story · **Agent judgment** |

**Not for:** product ship (`/implement`), catalog routing (`/butler`), vault compile/query (`/vault-ingest`, `/wiki-query`).

**Cross-domain:** Vault `vault-explain` hard-loads `learning-explainer`. `resource-summarizer` is soft under Learn and used by vault-ingest distill. `code-explainer` lives under `skills/code-explainer` as Learn child (hub membership).

---

## Domain 14 — Office

| | |
|--|--|
| **★ Hub** | `/office` |
| **Children** | **leaf:** `docx`, `pptx`, `xlsx`, `diagram-maker`, `imagine`, `hatch-pet`, `json-canvas`, `defuddle` |

| Fork | Question | Recommended | Branches |
|------|----------|-------------|----------|
| **F-misc** | What artifact type? | from extension/context | document · slides · sheet · diagram · image · canvas · web · pet · **Agent judgment** |

**Tree:** hub → leaf (not a long chain).

---

## Global entry fork

| Fork | Question | Recommended | Branches |
|------|----------|-------------|----------|
| **F7** | What kind of work? | feature → Design | Design · Triage · Diagnose · Fog · Architecture · Vault · Misc · Catalog facilities · Learn · Simplify · **Agent judgment** |

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
        ★ implement → tdd → code-review (F6; Review sub-hub) → commit
               │
        open-ended “review?” → ★ /review (F-R1) → code-review | security-auditor | software-architect | strategy
```

## Residual — Personal

| | |
|--|--|
| **Package** | `personal/` (not a domain hub) |
| **Skills** | `pi-agent-rust` (project-specific) |
| **Rule** | Not promoted; hub membership optional / personal residual |
