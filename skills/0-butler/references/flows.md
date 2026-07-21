# Flows — hub map + pipelines + forks (SSOT)

**Butler** reads this map to route. **skill-manager** writes hub slots when placing skills.

## Patterns

### Hub

Each **workflow domain** has exactly one **★ top skill (hub)**. Children link by type: `wrapper` · `hard` · `soft` · `pipeline` · `on-ramp` · `leaf` · `axis` · `satellite` · `sub-hub`.

### Depth-prefix names (hard)

Live skill id = **`{depth}-{kebab-slug}`** (dir, frontmatter `name`, slash, hub package) for **full hub-tree depth** (0 … max).

| Depth | Role |
|------:|------|
| **0-** | ★ domain hubs + hub-of-hubs (`0-butler`) — hub identity always |
| **1-** | Children of a domain hub; sub-hubs at parent+1 (today `1-code-review`) |
| **2-** | Children of depth-1 hubs — e.g. under a sub-hub → `2-verify-work`, `2-security-and-hardening` |
| **3-** | Children of depth-2 parents / nested sub-hubs |
| **4- / 5- / 6-** | Same recurrence: `max(parent_depth + 1)` (no artificial cap; 7+ continues) |

**Dual domain:** depth uses the **deepest** hub parent; `"primary": true` is ownership/docs only. SSOT: `skills/0-skill-manager/references/depth-prefix-names.md`. Lint: `depth-prefix` / `depth-hub` / `depth-graph` critical.

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
| **★ Hub** | `/0-butler` |
| **Children** | All domain hubs below (routing targets): 0-setup-rohitas-skills, 0-grilling, 0-implement, 0-review, 0-triage, 0-diagnosing-bugs, 0-wayfinder, 0-improve-codebase-architecture, 0-rohitas-vault-wiki, 0-skill-manager, 0-skill-creator, 0-ponytail, 0-learn, misc |
| **Session meta (soft)** | `1-grok-help`, `1-context-monitor`, `1-strategic-compact`, `1-response-effort-calibrator`, `1-handoff` (dual design) |
| **Mutations** | **Not here** → `/0-skill-manager` |

**Pipeline:** orient → query → domain hub (or delegate 0-skill-manager).

**Artifacts (ADR 0005):** every domain hub (including 0-butler) has a **flat package dir** (flat package under catalog `hubs/`):

```text
hubs/{hub}/
  hub.html          # non-butler pages parent-link 0-butler; 0-butler lists every hub
  workflow.json     # parent → 0-butler (null only for butler)
```

Also: `hubs/index.html`, `hubs/manifest.json`, `hubs/flows-chart.html`.

flows.md remains SSOT for pipelines/forks; HTML/JSON are projections. **new-hub** must create the package via `/0-skill-manager`. Live skills stay in flat `skills/` leaves (`skills/`, …). Flat browse: `skills/<name>`. Index: `wikis/index.md`.

---

## Domain 1 — Setup

| | |
|--|--|
| **★ Hub** | `/0-setup-rohitas-skills` |
| **Children** | **hard:** `1-to-spec`, `1-to-tickets` · **soft:** `1-tdd`, `0-diagnosing-bugs`, `0-improve-codebase-architecture`, vocabulary skills · **on-ramp (opt-in):** `0-triage` · **SSOT:** issue-tracker, domain, vault · **SSOT (opt-in):** triage-labels |

**Pipeline:** run once per consumer repo. Core path = issue tracker → domain → optional vault. **Do not** configure triage unless F2 = Yes.

| Fork | Question | Recommended | Branches |
|------|----------|-------------|----------|
| **F1** | Setup already done (`docs/agents/` present)? | Skip if present | run setup · skip → Design/Ship · **Agent judgment** |
| **F2** | Configure `/0-triage` labels? (intake for *incoming* issues/PRs — not grill→tickets→ship) | **No** | No · Yes → labels · **Agent judgment** |

---

## Domain 2 — Design

| | |
|--|--|
| **★ Hub** | `/0-grilling` |
| **Children** | **wrapper:** `1-grill-me`, `1-grill-with-docs` · **on-ramp:** `1-brainstorm` · **pull-in:** `1-domain-modeling` · **soft:** `1-thinking-steel-manning` · **detour:** `1-handoff` ⇄ `1-prototype` |

| Fork | Question | Recommended | Branches |
|------|----------|-------------|----------|
| **F-B1** | Hard brainstorm design-gate or grill interview? | grill if product requirements; brainstorm if greenfield feature design before code | `1-brainstorm` · `1-grill-with-docs` / `1-grill-me` · **Agent judgment** |
| **F2** | Codebase present? | Yes → 1-grill-with-docs | `1-grill-with-docs` · `1-grill-me` · **Agent judgment** |
| **F3** | Need a runnable 1-prototype answer? | No | stay in grill · handoff⇄prototype · **Agent judgment** |
| **F4** | Multi-session build? | Yes if >1 0-implement slice | yes → Ship multi · no → Ship single · **Agent judgment** |

**Merge out:** → Domain 3 Ship (after design: optional `/1-write-plan`).

---

## Domain 3 — Ship

| | |
|--|--|
| **★ Hub** | `/0-implement` |
| **Children** | **pipeline:** `1-to-spec` → `1-to-tickets` → `0-implement` → `1-tdd` → `1-code-review` → commit · **soft (plan path):** `1-write-plan`, `1-git-worktrees`, `1-subagent-implement`, `1-execute-plan`, `1-finish-branch` · **satellite:** `1-parallel-agents` · **soft (style):** `1-coding-standards`, `1-code-comments`, `1-inline-comments`, `1-execution-flow-comments`, `1-stepdown-rule` · **cousin:** `2-verify-work` · **soft (git/PR):** `1-git-commit-helper`, `1-pr-summarizer`, `1-resolving-merge-conflicts` · **soft:** `1-research` · **soft (vendor harvest):** `1-shipping-and-launch`, `1-observability-and-instrumentation`, `1-ci-cd-and-automation`, `1-frontend-ui-engineering` |

| Fork | Question | Recommended | Branches |
|------|----------|-------------|----------|
| **F4** | (entry) multi-session? | as Design | 1-to-spec path · direct 0-implement · **Agent judgment** |
| **F-SP** | Execute plan same session or new session? | same if subagents available | `1-subagent-implement` · `1-execute-plan` · **Agent judgment** |
| **F5** | This slice done? | run closer | tdd→code-review→commit (optional `/1-finish-branch`) · more tickets · **Agent judgment** |
| **F6** | (inside 1-code-review sub-hub) axes applicable? | every applicable | Spec / Standards / Maintainability on or soft-skip · **Agent judgment** |

**Multi-session pipeline:**

```text
1-to-spec → 1-to-tickets → implement* → 1-tdd → 1-code-review (multi-axis) → commit
```

**Optional plan path (after design / `1-write-plan`):**

```text
1-write-plan → 1-git-worktrees? → F-SP → 1-subagent-implement | 1-execute-plan → 1-tdd / closer → 1-finish-branch
```

**Single-session:** `implement*` → 1-tdd → 1-code-review → commit.

**Note:** Ship lands on **`/1-code-review`** (Review **sub-hub**), not domain hub `/0-review`. Open-ended “which review?” → `/0-review` F-R1.

---

## Domain 4 — Review

| | |
|--|--|
| **★ Hub** | `/0-review` |
| **Children** | **sub-hub:** `1-code-review` · **sub-hub:** `1-security-auditor` · **soft:** `1-doubt-driven-development`, `1-receive-review` · **on-ramp:** `1-codebase-review-strategy` · **soft (shared):** `2-security-and-hardening` · **soft (dual):** `2-software-architect` (primary Domain 8) |
| **Pipeline** | orient → **F-R1** pick mode → sub-hub / skill → optional remediation via `/2-security-and-hardening` · incoming feedback → `/1-receive-review` |

| Fork | Question | Recommended | Branches |
|------|----------|-------------|----------|
| **F-R1** | What kind of review? | Multi-axis **change** 0-review if PR/ship/diff | `/1-code-review` · `/1-security-auditor` · `/2-software-architect` · `/1-codebase-review-strategy` first · **Agent judgment** |
| **F6** | (inside `/1-code-review`) axes applicable? | every applicable | Spec / Standards / Maintainability on or soft-skip · **Agent judgment** |
| **F-R2** | (inside `/1-security-auditor`) audit scope? | full project unless path/PR named | full · scoped module · differential/PR · **Agent judgment** |

### Sub-hub `/1-code-review`

| | |
|--|--|
| **Role** | Multi-axis diff/PR closer (Ship + branch 0-review) |
| **Children** | **axis:** Spec, Standards, Maintainability · **cousin:** `2-verify-work`, `2-ponytail-review` · **soft:** `2-software-architect`, `2-security-and-hardening` · **†** `code-review-v2` |

### Sub-hub `/1-security-auditor`

| | |
|--|--|
| **Role** | Multi-phase security/quality audit + structured findings |
| **Children** | **soft:** `2-security-and-hardening` (remediate / prevent after findings) |

`2-security-and-hardening` is listed under **both** sub-hubs (shared soft). Architecture deepen/survey stays Domain 8; only the persona dual-softs into Review for architecture *review*.

---

## Domain 5 — Triage

| | |
|--|--|
| **★ Hub** | `/0-triage` |
| **Children** | merge → `0-implement` |
| **Rule** | Never re-triage `1-to-tickets` output |

---

## Domain 6 — Diagnose

| | |
|--|--|
| **★ Hub** | `/0-diagnosing-bugs` |
| **Children** | `1-tdd`; optional on-ramp → `0-improve-codebase-architecture` · **soft (vendor harvest):** `1-performance-optimization`, `1-browser-testing-with-devtools` · **soft (dual Ship):** `1-parallel-agents` (independent multi-failure) |

---

## Domain 7 — Fog map

| | |
|--|--|
| **★ Hub** | `/0-wayfinder` |
| **Children** | exit **only** → `1-to-spec` (then Ship) |

| Fork | Question | Recommended | Branches |
|------|----------|-------------|----------|
| **F8** | Fog clear enough to build? | only when buildable | stay 0-wayfinder · → 1-to-spec · **Agent judgment** |

---

## Domain 8 — Architecture

| | |
|--|--|
| **★ Hub** | `/0-improve-codebase-architecture` |
| **Children** | **vocab:** `1-codebase-design` · **persona:** `2-software-architect` · **soft (principles):** `1-clean-craftsmanship` · **soft (always-on style):** `1-coding-standards` (also Ship) · **soft (docs):** `1-project-wiki-manager`, `1-living-documentation-governor` · **soft (vendor harvest):** `1-api-and-interface-design`, `1-deprecation-and-migration` · **†** `software-architecture` |

| Fork | Question | Recommended | Branches |
|------|----------|-------------|----------|
| **F9** | Take a deepening idea to Design? | if user picks one | stay · → 1-grill-with-docs · **Agent judgment** |
| **F-C1** | Enforce standards on code now, or discuss clean-code principles? | coding while editing | `/1-coding-standards` · `/1-clean-craftsmanship` · **Agent judgment** |
| **F-D1** | Concept wiki (`docs/wiki`) or living docs + code triggers? | wiki if raw→concepts · living if drift/triggers | `/1-project-wiki-manager` · `/1-living-documentation-governor` · **Agent judgment** |

**Related atoms (not merge targets):** `1-coding-standards` ↔ `1-clean-craftsmanship` (F-C1); `1-project-wiki-manager` ↔ `1-living-documentation-governor` (F-D1); personal vault is Domain 9 (F-D2).

---

## Domain 9 — Vault

| | |
|--|--|
| **★ Hub** | `/0-rohitas-vault-wiki` |
| **Children** | **pipeline/ops:** `1-vault-inbox` → `1-vault-ingest` → `1-vault-lint` / `1-wiki-query` / `1-vault-explain` · **soft (Learn dual):** `1-resource-summarizer` (ingest distill) · **leaf primitives:** `1-obsidian-markdown`, `1-obsidian-cli`, `1-obsidian-bases` · **†** `obsidian-notes-manager` |
| **Learn handoff** | `1-vault-explain` → hard-load `/1-learning-explainer` (Learn domain); open-ended non-vault learning → `/0-learn` |

| Fork | Question | Recommended | Branches |
|------|----------|-------------|----------|
| **F11** | Capture / compile / query / lint / explain? | match utterance | inbox · ingest · query · lint · explain · **Agent judgment** |
| **F-D2** | Project repo wiki or personal Rohitas’s Notes vault? | vault if Concepts/Atlas/my notes | `/0-rohitas-vault-wiki` · `/1-project-wiki-manager` (or F-D1 if living docs) · **Agent judgment** |

Vault root path from setup SSOT only.

---

## Domain 10 — Catalog facilities

| | |
|--|--|
| **★ Hub** | `/0-skill-manager` |
| **Children** | ops: create/read/update/delete/place/new-hub/ingest/organize/lint/atomize · **pipeline:** `1-skill-linter` · **pipeline:** `1-skill-atomize` · **soft:** `1-session-skill-reflect`, `1-discover-skills` · 1-handoff body craft → `0-skill-creator` |

Not a product feature pipeline — **mutates the catalog**.

**Lint:** `/0-skill-manager` lint op loads **`/1-skill-linter`**. Every live skill must be a hub member (ADR 0006). New place/ingest requires skill-lint Gate: PASS.

**Atomize:** `/0-skill-manager` atomize op loads **`/1-skill-atomize`**. Detect content overlap (exclude intentional hub links), dry-run Boundary + F# forks, confirm, apply, re-lint. Default resolution: keep both peers + hard redirects (not silent merge).

| Fork | Question | Recommended | Branches |
|------|----------|-------------|----------|
| **F-A1** | (inside 1-skill-atomize) How far this pass? | high-overlap only | high · high+medium · full · **Agent judgment** |
| **F-A2** | Collision resolution? | keep both + Boundary + forks | keep-both · merge · split · **Agent judgment** |
| **F-A3** | Apply multi-file writes? | dry-run then confirm | dry-run · apply · **Agent judgment** |

---

## Domain 11 — Author body

| | |
|--|--|
| **★ Hub** | `/0-skill-creator` |
| **Children** | **wrapper:** `1-create-skill` · craft: `1-writing-great-skills` · next: 0-skill-manager place |

| Fork | Question | Recommended | Branches |
|------|----------|-------------|----------|
| **F10** | Ingest/place into catalog now? | yes when ready | stay crafting · 0-skill-manager place/ingest · **Agent judgment** |

---

## Domain 12 — Simplify

| | |
|--|--|
| **★ Hub** | `/0-ponytail` |
| **Children** | **satellite:** `2-ponytail-review`, `1-ponytail-audit`, `1-ponytail-debt`, `1-ponytail-gain`, `1-ponytail-help` |

Optional; not Ship closer.

---

## Domain 13 — Learn

| | |
|--|--|
| **★ Hub** | `/0-learn` |
| **Children** | **leaf:** `1-learning-explainer` (structured explain SSOT) · **leaf (soft cross (code object)):** `1-code-explainer` · **satellite:** `1-teach` (multi-session workspace) · **leaf:** `1-story-teacher` · **soft:** `1-resource-summarizer` · **on-ramp (Vault primary):** `1-vault-explain` → explainer · **tutor mode:** `learn/references/tutor-mode.md` (not a separate skill) |
| **Pipeline** | orient → **F-L1** pick mode → optional **F-L2** if long source → load one mode |

| Mode | Skill / load | Default when |
|------|----------------|--------------|
| Explain | `/1-learning-explainer` | “what is / explain / ELI5 / levels” |
| Tutor | tutor-mode refs under `/0-learn` | stuck on a problem, quiz, walk-through |
| Code walkthrough | `/1-code-explainer` | explain source code in editor/repo |
| Workspace course | `/1-teach` | multi-session directory lessons |
| Story | `/1-story-teacher` | 1-teach via fiction |
| Summarize source | `/1-resource-summarizer` | distill long artifact for notes |
| Vault Concept | `/1-vault-explain` | explain `[[Note]]` from vault |

| Fork | Question | Recommended | Branches |
|------|----------|-------------|----------|
| **F-L1** | What kind of learning help? | Structured **explain** for concepts; **code-explainer** if object is code | explainer · tutor · 1-code-explainer · 1-teach · story · summarizer · 1-vault-explain · **Agent judgment** |
| **F-L2** | Long source — summarize first? | Yes if raw blob is huge | summarizer first · skip to explain/tutor/story · **Agent judgment** |

**Not for:** product ship (`/0-implement`), catalog routing (`/0-butler`), vault compile/query (`/1-vault-ingest`, `/1-wiki-query`).

**Cross-domain:** Vault `1-vault-explain` hard-loads `1-learning-explainer`. `1-resource-summarizer` is soft under Learn and used by 1-vault-ingest distill. `1-code-explainer` lives under `skills/1-code-explainer` as Learn child (hub membership).

---

## Domain 14 — Office

| | |
|--|--|
| **★ Hub** | `/0-office` |
| **Children** | **leaf:** `1-docx`, `1-pptx`, `1-xlsx`, `1-diagram-maker`, `1-imagine`, `1-hatch-pet`, `1-json-canvas`, `1-defuddle` |

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
| ask-matt | 0-butler |
| code-review-v2 | 1-code-review |
| software-architecture | 0-improve-codebase-architecture / 1-codebase-design |
| obsidian-notes-manager | 0-rohitas-vault-wiki |
| task-observer | reflect + 0-skill-manager |
| continuous-learning-v2 | reflect |

---

## ASCII — main product path

```text
        ★ 0-butler (route only)
               │
        ★ 0-setup-rohitas-skills  (F1)
               │
        ★ 0-grilling  (F2 wrappers · F3 proto · F4 multi?)
               │
     ┌─────────┴─────────┐
   multi               single
     │                   │
  1-to-spec                │
  1-to-tickets             │
     └─────────┬─────────┘
               ▼
        ★ 0-implement → 1-tdd → 1-code-review (F6; Review sub-hub) → commit
               │
        open-ended “review?” → ★ /0-review (F-R1) → 1-code-review | 1-security-auditor | 2-software-architect | strategy
```

## Residual — Personal

| | |
|--|--|
| **Package** | `personal/` (not a domain hub) |
| **Skills** | `1-pi-agent-rust` (project-specific) |
| **Rule** | Not promoted; hub membership optional / personal residual |
