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
| **Children** | All domain hubs below (routing targets): 0-setup-rohitas-skills, 0-grilling, 0-implement, 0-review, 0-triage, 0-diagnosing-bugs, 0-wayfinder, 0-improve-codebase-architecture, 0-rohitas-vault-wiki, 0-skill-manager, 0-skill-creator, 0-ponytail, 0-learn, 0-office, 0-ui-ux, 0-thinking, 0-git, 0-agent-engineering, 0-devops, 0-marketing |
| **Session meta (soft)** | `1-grok-help` (local Grok evidence), `1-context-monitor` (no guessed telemetry) → `1-strategic-compact` (same-session capsule) / `1-handoff` (durable file; also Design detour), `1-response-effort-calibrator`, `1-action-first-output` (explicit, persistent action-first mode), `1-caveman` (explicit ultra-terse style), `1-bro`, `1-plow-ahead`, `1-quick-recap` · **satellite:** `1-rewind`, `1-webmcp` |
| **Project adapter (soft)** | `1-pi-agent-rust` → supplies current-checkout surface/invariants/check candidates, then routes to Diagnose, Ship, Review, or CI/CD |
| **Mutations** | **Not here** → `/0-skill-manager` |

**Pipeline:** explicit routing request → read flows/index → direct matching skill
when clear, otherwise **F7** → validate live `SKILL.md` → report owning hub +
smallest skill + first action → stop. Butler is read-only and never executes the
selected workflow. Catalog mutation routes to `0-skill-manager`; skill-body craft
routes to `0-skill-creator`.

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
| **Children** | **leaves:** `1-setup-issue-tracker`, `1-setup-domain-docs`, `1-setup-vault-root`, `1-setup-triage-labels` · **template assets:** issue-tracker, domain, vault, triage-labels |

**Pipeline:** pin the consumer repository, exact worktree, branch/HEAD, dirty-state ownership, active instructions, allowed paths, and authority → inspect current setup read-only → route an explicit request directly or ask **F-S1** once → hand exactly one child the pinned scope and current contents → child returns its draft/applied diff, verification evidence, and unresolved external setup → stop. The hub does not write, create worktrees, or mutate trackers/vaults. Worktrees isolate files and Git state, not accounts or shared services.

| Fork | Question | Recommended | Branches |
|------|----------|-------------|----------|
| **F-S1** | What should be configured now? | Issue tracker for a new repo | `1-setup-issue-tracker` · `1-setup-domain-docs` · `1-setup-vault-root` · `1-setup-triage-labels` · **Agent judgment** |

---

## Domain 2 — Design

| | |
|--|--|
| **★ Hub** | `/0-grilling` |
| **Children** | **wrapper:** `1-grill-me`, `1-grill-with-docs` · **on-ramp:** `1-brainstorm` · **pull-in:** `1-domain-modeling` · **leaf:** `1-honest-advisor` · **soft:** `1-thinking-steel-manning`, `1-anti-sycophancy`, `1-critique` · **detour:** `1-handoff` ⇄ `1-prototype` · **satellite:** `1-visual-plan` |
| **Pipeline** | pin caller + immutable candidate + evidence/authority + optional worktree → direct smallest child or material-only F-B1/F2 → one decision-changing neutral question at a time → optional separately accepted prototype/visual-plan detour returns evidence → one decision record to actual caller; no automatic downstream action |

| Fork | Question | Recommended | Branches |
|------|----------|-------------|----------|
| **F-B1** | Hard brainstorm design-gate or grill interview? | grill if product requirements; brainstorm if greenfield feature design before code | `1-brainstorm` · `1-grill-with-docs` / `1-grill-me` · **Agent judgment** |
| **F2** | Do repository facts materially govern the decision? | Yes → 1-grill-with-docs | `1-grill-with-docs` · `1-grill-me` · **Agent judgment** |
| **F3** | Need a runnable prototype answer? | No unless a runnable experiment resolves a design question | stay in grill · `1-prototype` and return · **Agent judgment** |
| **F-P1** | What question should the prototype answer? | logic/state for behavior; UI alternatives for visual layout | `1-prototype` logic/state · `1-prototype` local UI alternatives · **Agent judgment** |
| **F-B2** | Was a visual review artifact requested? | Keep conversational/text unless explicit | `1-visual-plan` · keep conversational/text result · **Agent judgment** |

**Return:** accepted/delegated decisions and separately requested prototype/visual evidence return to the actual design caller. Specification, planning, handoff, or implementation requires a separate request. Approval is not execution authority.

---

## Domain 3 — Ship

| | |
|--|--|
| **★ Hub** | `/0-implement` |
| **Children** | **pipeline members (conditional sequence below):** `1-to-spec`, `1-to-tickets`, `0-implement`, `1-tdd`, `1-code-review`, `1-atomic-git-commits` · **soft (plan path):** `1-write-plan`, `1-git-worktrees`, `1-subagent-implement`, `1-execute-plan`, `1-finish-branch` · **satellite:** `1-parallel-agents` · **soft (style/quality/docs):** `1-coding-standards`, `1-go-best-practices` (scoped Go implementation), `1-living-documentation-governor` (code↔canonical-doc obligations), `1-constraint-driven-development`, `1-code-comments` (one public contract surface), `1-inline-comments` (one internal why/constraint), `1-execution-flow-comments` (one explicitly requested function narrative), `1-stepdown-rule` (one behavior-independent file reorder); all return without automatic review · **soft (contract/module/lifecycle):** `1-api-and-interface-design`, `1-codebase-design`, `1-deprecation-and-migration` (design or phase evidence, then return to Ship) · **soft (failure behavior):** `1-error-handling` (bounded implementation; returns to Ship) · **soft (Supabase):** `1-supabase` (one product integration), `1-supabase-postgres-best-practices` (one measured Postgres concern), `1-supabase-schema-migration` (one new local schema concept), `1-pending-migration-hygiene` (rewrite only with complete observed provenance or exact human attestation); all pin local-stack ownership because worktrees do not isolate it, and none applies remotely · **soft (explicit process):** `1-karpathy-guidelines` (inherits and returns candidate/workspace/authority) · **cousin:** `2-verify-work` · **soft (Git cross-links):** `1-atomic-git-commits`, `1-pr-summarizer`, `1-resolving-merge-conflicts` · **soft:** `1-research` (one bounded answer; persistence only when requested) · **soft (delivery/UI/performance):** `1-ci-cd-and-automation` (one candidate-aware workflow/check contract; returns without remote execution), `1-observability-and-instrumentation` (one question-to-signal contract; returns without hosted telemetry), `1-shipping-and-launch` (one immutable release candidate; plan/read-only modes do not deploy), `1-frontend-ui-engineering` (one candidate-bound interaction surface; returns without redesign or publication), `1-ui-styling` (one presentation-only visual delta; preserves behavior and returns candidate/worktree/authority), `1-performance-optimization` (one measured experiment; returns its disposition without shared load) · **additions:** `1-dev-test`, `1-i18n-sync` |

| Fork | Question | Recommended | Branches |
|------|----------|-------------|----------|
| **F4** | Is the request already buildable, or does it need specification/ticket decomposition? | direct implementation for a clear bounded request | /1-to-spec → /1-to-tickets for materially unresolved or multi-session work · direct /0-implement for a clear bounded request · Agent judgment |
| **F-TDD1** | Does this slice have a settled seam, deterministic behavior, independent oracle, and edit authority for a red-green loop? | TDD only when every fit condition is established | /1-tdd for one fitting red-green slice · characterization or /0-diagnosing-bugs when the current behavior/root cause is unknown · /1-write-plan or /1-prototype when the contract or interface is unsettled · /1-agent-evaluation for probabilistic model or RAG behavior · Agent judgment |
| **F-SP** | Execute directly or use explicitly authorized delegation? | direct execution unless delegation was requested and has safe ownership boundaries | /1-subagent-implement · /1-execute-plan · Agent judgment |
| **F5** | Does the actual candidate have enough evidence to enter review reconciliation? | review after applicable claims have current evidence or labeled gaps | /1-code-review → fix verified in-scope findings → reverify/re-review → /1-atomic-git-commits when authorized · continue the current slice or next requested ticket · Agent judgment |
| **F6** | (inside 1-code-review) axes applicable? | every applicable | Spec · Standards · Maintainability · soft-skip · Agent judgment |

**Multi-session pipeline:**

```text
pin scope/worktree/authority → 1-to-spec → 1-to-tickets when needed → implement with the fitting evidence loop → 1-code-review → reconcile verified in-scope findings → reverify/re-review → optional authorized 1-atomic-git-commits
```

**Optional plan path (after design / `1-write-plan`):**

```text
existing plan (1-write-plan only if missing) → exact repo/worktree/branch/HEAD + dirty/service ownership
  → 1-git-worktrees only for protected-branch, overlapping-state, concurrent-work, or branch-specific-state isolation
  → resume Ship → F-SP direct or explicitly authorized delegation → verify → review/reconcile loop → return to caller
1-atomic-git-commits requires commit authority; 1-finish-branch only for requested integration options; no implicit remote/production effects
```

**Single-session:** clear request → pin exact workspace/authority → implement with the fitting evidence loop → `1-code-review` → repair verified in-scope findings one by one → reverify/re-review → optional authorized `1-atomic-git-commits`. Use `/1-tdd` only for known deterministic behavior at an agreed seam; specification, characterization, prototype/evaluation, or focused runtime evidence may fit better.

**Note:** Ship lands on **`/1-code-review`** (Review **sub-hub**), not domain hub `/0-review`. Open-ended “which review?” → `/0-review` F-R1.

---

## Domain 4 — Review

| | |
|--|--|
| **★ Hub** | `/0-review` |
| **Children** | **sub-hub:** `1-code-review` · **sub-hub:** `1-security-auditor` · **pipeline:** `1-complete-pr-review` (one PR: comprehensive risk-weighted review, read-only) · **leaf:** `1-agent-pr-review` (agent-generated PR risk pass) · **leaf:** `1-clean-tautological-tests` (tautological and zero-signal test audit) · **security leaves:** `2-prompt-injection-defense`, `2-skill-supply-chain-audit`, `2-dependency-security` (application dependency checks) · **soft:** `1-doubt-driven-development`, `1-receive-review` · **soft (failure behavior):** `1-error-handling` (narrow read-only review; primary Domain 8) · **soft (Go practice):** `1-go-best-practices` (narrow read-only review; primary Domain 8) · **on-ramp:** `1-codebase-review-strategy` · **cousin:** `2-verify-work`, `2-ponytail-review`, `2-thermo-nuclear-code-quality-review` · **satellite:** `1-visual-recap` · **soft (shared):** `2-security-and-hardening` · **soft (dual):** `2-software-architect` (primary Domain 8) · **additions:** `1-pre-merge`, `1-design-review` |
| **Pipeline** | honor selected mode; **F-R1** only if ambiguous → pin scope + actual candidate → sub-hub / skill → read-only report → return to caller · `1-complete-pr-review` combines code + differential security on the same pinned PR, closes material risk-triggered coverage gaps, and returns one ledger · repair, publication and integration need corresponding authority · unfamiliar/whole-repo request → `1-codebase-review-strategy` returns one coverage plan; a specialist runs only when separately/originally authorized on the same candidate · one consequential claim → `1-doubt-driven-development` → keep/revise/reject/unknown · incoming feedback → `/1-receive-review` |

| Fork | Question | Recommended | Branches |
|------|----------|-------------|----------|
| **F-R1** | What kind of review? | Multi-axis **change** review if PR/ship/diff | /1-design-review (pre-code spec/plan) · /1-code-review · /1-complete-pr-review · /1-pre-merge · /1-agent-pr-review · /1-error-handling · /1-go-best-practices · /1-security-auditor · /2-software-architect · /1-codebase-review-strategy (unfamiliar/whole repo) · /1-doubt-driven-development (one consequential claim) · /2-thermo-nuclear-code-quality-review · /2-verify-work · /1-visual-recap · Agent judgment |
| **F6** | (inside 1-code-review) axes applicable? | every applicable | every applicable axis; missing spec/standards uses labeled baseline, not a false pass · Agent judgment |
| **F-R2** | (inside 1-security-auditor) audit scope? | full project unless path/PR named | full · scoped module · differential/PR · Agent judgment |
| **F-R3** | Which focused security surface? | narrow specialist when scope matches | `2-prompt-injection-defense` · `2-skill-supply-chain-audit` · `2-dependency-security` · general security audit · **Agent judgment** |

### Sub-hub `/1-code-review`

| | |
|--|--|
| **Role** | Read-only multi-axis review of the actual diff/PR/current implementation, including task-owned staged, unstaged and untracked changes |
| **Children** | **axis:** Spec, Standards, Maintainability · **cousin:** `2-verify-work`, `2-ponytail-review`, `2-thermo-nuclear-code-quality-review` · **soft:** `2-software-architect` (bounded read-only system review; return to caller), `2-security-and-hardening` · **additions:** `1-pre-merge`, `1-design-review` |
| **Pipeline** | pin candidate + caller → applicable axes → validate findings + coverage → return to caller; no automatic repair, publication or commit |

Review and verification use [the shared candidate contract](../../0-review/references/review-candidate.md). Reading needs no new worktree; runtime isolation returns to the paused review. `2-verify-work` reports PASS/FAIL/BLOCKED for supported claims rather than owning a repair loop. Historical `code-review-v2` is not a live route; use `1-code-review`.

### Sub-hub `/1-security-auditor`

| | |
|--|--|
| **Role** | Multi-phase security/quality audit + structured findings |
| **Children** | **soft:** `2-security-and-hardening` (remediate / prevent after findings) · **leaf:** `2-prompt-injection-defense`, `2-skill-supply-chain-audit`, `2-dependency-security` (dependency vulnerability, staleness, and new-package checks) · **additions:** `1-pre-merge`, `1-design-review` |
| **Pipeline** | honor caller scope/authority → pinned candidate → applicable recon/hunt/validation → verified report + coverage limits → return to caller; files, remediation and publication only when requested |

Dependency ratchets compare issue identities under equivalent advisory data, not
aggregate counts; existing policy is not weakened by an audit. Security specialists
receive the same candidate and review-only mode when called from PR review.

`2-skill-supply-chain-audit` returns a fixed-snapshot recommendation and coverage gaps
to Security, Agent Engineering or the ingest caller. Package metadata/pattern scans
do not approve installation, executable imports, catalog promotion, edits or live
quarantine. Source reading needs no worktree; authorized dynamic tests require a
restricted disposable runtime, not merely another Git checkout.

`2-security-and-hardening` is listed under **both** sub-hubs (shared soft). It applies
only authorized scoped fixes in the caller's matching workspace and returns to that
build/repair workflow; audit findings alone do not grant remediation, rotation or
deployment authority. Architecture deepen/survey stays Domain 8; only the persona
dual-softs into Review for architecture *review*.

---

## Domain 5 — Triage

| | |
|--|--|
| **★ Hub** | `/0-triage` |
| **Children** | **leaf:** `1-triage-inbox` (one read-only attention snapshot) · **pipeline:** `1-triage-assess` (one read-only candidate assessment), `1-triage-apply` (one approved revision-checked transition) |
| **Pipeline** | pin tracker/candidate or query + revision/cutoff + privacy/authority + optional worktree identity → direct leaf or material-only F-TR1 → return evidence/proposed or actual effects to caller → separately requested ready work may enter `0-implement` |
| **Rule** | Never re-triage `1-to-tickets` output. Assessment grants no tracker-write authority; `ready-for-agent` grants no implementation authority. |

| Fork | Question | Recommended | Branches |
|---|---|---|---|
| **F-TR1** | Which one triage operation is needed? | infer from request and candidate state | `1-triage-inbox` · `1-triage-assess` · `1-triage-apply` · **Agent judgment** |

Inbox is remote-read-only unless the configured tracker is local Markdown. Assessment may return a
bounded Grilling, Diagnose, or Review handoff but starts none. Apply accepts only a still-current approved
transition, enumerates every label/comment/assignment/status/file effect, verifies readback, and reports
partial effects without blind retries. Worktrees do not isolate remote tracker state.

---

## Domain 6 — Diagnose

| | |
|--|--|
| **★ Hub** | `/0-diagnosing-bugs` |
| **Children** | `1-tdd`; optional on-ramp → `0-improve-codebase-architecture` · **soft:** `1-performance-optimization` (one repeatable measured experiment; dual Ship with caller/candidate/worktree return), `1-browser-testing-with-devtools` (one read-only candidate/server/profile-bound evidence session; returns without edits), `1-playwright-browser-testing` (one exact candidate/worktree/server-bound durable check; returns the verdict without product edits) · **soft (dual Ship):** `1-parallel-agents` (independent multi-failure) |
| **Pipeline** | pin candidate/worktree/environment/evidence/authority → choose the smallest discriminating loop → reproduce or observe honestly → localize/minimize → falsify hypotheses one variable at a time → return supported/inconclusive/blocked/not-reproduced diagnosis → separately authorized implementation/verification |

| Fork | Question | Recommended | Branches |
|---|---|---|---|
| **F-DIAG1** | Which evidence loop best distinguishes this failure? | smallest repository-native focused test, command, request, or observation | core loop · `1-performance-optimization` · `1-browser-testing-with-devtools` · `1-playwright-browser-testing` · explicitly authorized `1-parallel-agents` · known authorized fix → `0-implement` · **Agent judgment** |

---

## Domain 7 — Uncertainty map

| | |
|--|--|
| **★ Hub** | `/0-wayfinder` |
| **Children** | **leaf:** `1-wayfinder-chart` (one new map set) · **pipeline:** `1-wayfinder-advance` (one existing decision-ticket cycle) · **on-ramp:** `1-to-spec` (settled snapshot, separate request) |
| **Pipeline** | pin caller + immutable map/source candidate + evidence/authority + optional worktree identity → direct route or material-only F-W1/F-W2 → chart one map set or advance one ticket → return artifact/effects/frontier/fog → F8 only if settlement is ambiguous; no direct implementation |

| Fork | Question | Recommended | Branches |
|------|----------|-------------|----------|
| **F-W1** | Which one uncertainty-map operation is needed? | infer from the named candidate | `1-wayfinder-chart` · `1-wayfinder-advance` · settled snapshot → `1-to-spec` · **Agent judgment** |
| **F-W2** | Which frontier decision ticket should advance? | user-named or unique/declared-first eligible ticket | user-named · unique/declared-first eligible · **Agent judgment** |
| **F8** | Is the map settled enough for specification? | stay while material fog remains | stay `0-wayfinder` · separately requested `1-to-spec` · **Agent judgment** |

**Return:** Wayfinder leaves preserve exact candidate, optional repository/worktree identity, tracker/shared-resource
state, and effect ledger. Charting starts no specialist. Advancing handles exactly one ticket and either returns one
specialist handoff or records one supplied resolution packet. A worktree does not isolate tracker accounts,
databases, services, deployments, or other remote state. Decision/spec approval grants no implementation authority.

---

## Domain 8 — Architecture

| | |
|--|--|
| **★ Hub** | `/0-improve-codebase-architecture` |
| **Children** | **vocab:** `1-codebase-design` · **persona:** `2-software-architect` (bounded system decision packet; catalog depth under Review) · **satellite (explicit local graph):** `1-graphify` (pins corpus/worktree/output; never installs, hooks, strict mode, shared output, or backends itself) · **soft (principles):** `1-clean-craftsmanship` · **soft (always-on style):** `1-coding-standards`, `1-go-best-practices` (also Ship) · **soft (failure behavior):** `1-error-handling` (standalone or returns to its caller; F-EH1) · **soft (docs):** `1-project-wiki-manager` (declared sources; query/audit read-only, edits pinned to worktree), `1-living-documentation-governor` (code↔canonical-doc contract; also Ship) · **soft (vendor harvest):** `1-api-and-interface-design`, `1-deprecation-and-migration` · **additions:** `1-change-impact` |
| **Pipeline** | pin caller/mode/repository-worktree/evidence → clear request dispatches to one specialist and returns · broad improvement runs a bounded local read-only scan → Markdown or explicitly requested static HTML → F9 selected candidate · requested implementation returns to `/0-implement` |

| Fork | Question | Recommended | Branches |
|------|----------|-------------|----------|
| **F9** | Take a deepening idea to Design? | stay at the report unless the user selects a candidate | stay · /1-grill-with-docs · Agent judgment |
| **F-EH1** | Define failure behavior or diagnose an unexplained bug? | Failure behavior for handling/recovery requests | /1-error-handling · /0-diagnosing-bugs · Agent judgment |
| **F-ARCH1** | Design an API contract, a module, or the whole system? | API contract for endpoint/schema requests | /1-api-and-interface-design · /1-codebase-design · /2-software-architect · Agent judgment |
| **F-C1** | Enforce standards on code now, or discuss clean-code principles? | coding while editing | /1-coding-standards · /1-clean-craftsmanship · Agent judgment |
| **F-D1** | Concept wiki (docs/wiki) or living docs + code triggers? | wiki if raw→concepts · living if drift/triggers | /1-project-wiki-manager · /1-living-documentation-governor · Agent judgment |

**Related atoms (not merge targets):** `1-coding-standards` ↔ `1-clean-craftsmanship` (F-C1); `1-project-wiki-manager` ↔ `1-living-documentation-governor` (F-D1); personal vault is Domain 9 (F-D2).

---

## Domain 9 — Vault

| | |
|--|--|
| **★ Hub** | `/0-rohitas-vault-wiki` |
| **Children** | **setup on-ramp:** `1-setup-vault-root` · **operations:** `1-vault-inbox`, `1-vault-ingest`, `1-vault-lint` → `1-vault-repair` (one accepted finding), `1-wiki-query`, `1-vault-explain` · **soft (Learn dual):** `1-resource-summarizer` (bounded ingest evidence), `1-learning-explainer` (Concept pedagogy) · **leaf primitives:** `1-obsidian-markdown`, `1-obsidian-cli`, `1-obsidian-bases` |
| **Pipeline** | direct route from stated outcome → **F11** or **F-D2** only for material ambiguity → one leaf → evidence returns to actual caller |
| **Learn handoff** | `1-vault-explain` binds one exact Concept packet → `/1-learning-explainer` selects one Learn leaf → return to Vault/Learn caller; open-ended non-vault learning → `/0-learn` |

| Fork | Question | Recommended | Branches |
|------|----------|-------------|----------|
| **F11** | Capture / compile / query / lint / explain? | route directly from the stated outcome; ask only when two operations materially differ | inbox · ingest · query · lint · explain · **Agent judgment** |
| **F-D2** | Project repo wiki or personal Rohitas’s Notes vault? | infer from the named destination | `/0-rohitas-vault-wiki` · `/1-project-wiki-manager` (or F-D1 if living docs) · **Agent judgment** |

Vault root path from setup SSOT only.

---

## Domain 10 — Catalog facilities

| | |
|--|--|
| **★ Hub** | `/0-skill-manager` |
| **Children** | ops: create/read/update/delete/place/new-hub/ingest/organize · **pipeline:** `1-skill-linter` (read-only report), `1-skill-atomize` (one overlap cluster) · **soft:** `1-session-skill-reflect` (read-only proposal), `1-discover-skills` (read-only external discovery) · body craft → `0-skill-creator` |

Not a product feature pipeline — **mutates the catalog**.

**Lint:** `/0-skill-manager` lint op loads **`/1-skill-linter`**. Every live skill must be a hub member (ADR 0006). New place/ingest requires skill-lint Gate: PASS.

**Catalog pipeline:** pin exact catalog/worktree/revision/dirty ownership and one requested operation → assess or apply according to the request → revision-safe direct surfaces → regenerate affected projections → `1-skill-linter` → return. Explicit scoped edits need no duplicate confirmation; delete/overwrite/merge/split/install/sync/publish/external effects stay separately gated.

**Atomize:** `/0-skill-manager` atomize loads **`/1-skill-atomize`** for one pinned overlap cluster. It excludes intentional hub links, chooses the smallest boundary repair, and re-lints. Merge or split asks only when identity or retained behavior would materially change.

| Fork | Question | Recommended | Branches |
|------|----------|-------------|----------|
| **F-A1** | How far should this overlap pass extend? | named or highest-evidence cluster only | named cluster · high-overlap clusters · broader catalog · **Agent judgment** |
| **F-A2** | Should a true duplicate be bounded, merged, or split? | keep both with deterministic boundaries unless identity change is justified | boundary repair · merge/tombstone · split thinner · **Agent judgment** |

---

## Domain 11 — Author body

| | |
|--|--|
| **★ Hub** | `/0-skill-creator` |
| **Children** | **wrapper:** `1-create-skill` · **craft:** `1-writing-great-skills` · **leaf:** `1-source-backed-skill` · **optional separate handoff:** `0-skill-manager` place |

**Pipeline:** pin one exact package/worktree/revision and mode → draft/update/trigger-eval/output-eval → validate the selected evidence → return one candidate to the caller. Placement, installation, sync, commit, push, and publication do not follow unless separately requested.

---

## Domain 12 — Simplify

| | |
|--|--|
| **★ Hub** | `/0-ponytail` |
| **Children** | **satellite:** `2-ponytail-review` (one immutable diff, removable complexity only), `1-ponytail-audit` (bounded repository snapshot), `1-ponytail-debt` (read-only marker ledger), `1-ponytail-gain` (pinned benchmark with limitations), `1-ponytail-help` (catalog-accurate one-shot help) |
| **Pipeline** | explicit coding request → apply the requirement- and safety-preserving overlay and return · named review/audit/debt/gain/help request → direct one-child route → read-only result → actual caller · no automatic repair, Git, publication, child chaining, or mode change |
| **Not for** | non-coding prose/summaries/translation, extensive documentation, unresolved acceptance criteria, or any simplification that weakens requirements, correctness, security, privacy, accessibility, compatibility, or required verification |

Optional; not Ship closer.

---

## Domain 13 — Learn

| | |
|--|--|
| **★ Hub** | `/0-learn` |
| **Children** | **router:** `1-learning-explainer` → **leaves:** `1-learning-diagnostic`, `1-level-explainer`, `1-mental-model-builder`, `1-progressive-deep-dive` · **leaves:** `1-explain-with-example` (selected material), `1-tutor` (interactive practice) · **leaf (soft cross; code object):** `1-code-explainer` · **satellite router:** `1-teach` → `1-teaching-workspace`, `1-lesson-authoring`, `1-learning-progress-record`, `1-learning-glossary` · **leaf:** `1-story-teacher` · **soft:** `1-resource-summarizer` · **on-ramp (Vault primary):** `1-vault-explain` → explainer · **additions:** `1-design-rationale` |
| **Pipeline** | direct evidence route → **F-L1** only for material mode ambiguity → optional **F-L2** only for detail-versus-distillation choice → explainer router **F-L3** → load one leaf → return |

| Mode | Skill / load | Default when |
|------|----------------|--------------|
| Explain | `/1-learning-explainer` → level/model/deep-dive leaf | “what is / explain / ELI5 / levels” |
| Selected material | `/1-explain-with-example` | explain a quoted passage, error, finding, or recommendation with one grounded example and non-executing dry run |
| Tutor | `/1-tutor` | stuck on a problem, quiz, guided practice |
| Code walkthrough | `/1-code-explainer` | explain source code in editor/repo |
| Workspace course | `/1-teach` | multi-session directory lessons |
| Story | `/1-story-teacher` | one source-faithful original narrative |
| Summarize source | `/1-resource-summarizer` | distill long artifact for notes |
| Vault Concept | `/1-vault-explain` | explain `[[Note]]` from vault |

| Fork | Question | Recommended | Branches |
|------|----------|-------------|----------|
| **F-L1** | Should this be a direct explanation, interactive practice, or a reusable course? | infer from stated outcome; ask only when two modes materially differ | /1-learning-explainer · /1-explain-with-example · /1-tutor · /1-code-explainer · /1-teach · /1-story-teacher · /1-resource-summarizer · vault-explain if vault Concept · Agent judgment |
| **F-L2** | Should the selected material be explained directly or distilled first? | explain a clear selection directly; distill for source-level summary | /1-resource-summarizer first · /1-explain-with-example directly · Agent judgment |
| **F-L3** | What focused concept-learning operation is needed? | first explanation at a level | /1-learning-diagnostic · /1-level-explainer · /1-mental-model-builder · /1-progressive-deep-dive · Agent judgment |

**Not for:** product ship (`/0-implement`), catalog routing (`/0-butler`), vault compile/query (`/1-vault-ingest`, `/1-wiki-query`).

**Cross-domain:** Vault `1-vault-explain` enters `1-learning-explainer`, which routes to a focused leaf. `1-explain-with-example` covers supplied text, findings, errors, and recommendations with a grounded example plus explanatory dry run; it does not replace audience-level concept teaching or execute the described system. `1-resource-summarizer` is soft under Learn and used by 1-vault-ingest distill. `1-code-explainer` lives under `skills/1-code-explainer` as Learn child (hub membership).

---

## Domain 14 — Office

| | |
|--|--|
| **★ Hub** | `/0-office` |
| **Children** | **leaf:** `1-docx`, `1-pdf`, `1-pptx`, `1-xlsx`, `1-diagram-maker`, `1-imagine`, `1-json-canvas`, `1-defuddle`, `1-internal-comms` · **sub-hub:** `1-hatch-pet` |
| **Pipeline** | pin caller + immutable request/source/destination + sensitivity/authority + optional worktree identity → direct final-artifact route or material-only F-misc → exactly one leaf or the Pet operation sub-hub → return artifact/result provenance, verification, effects, and limits to actual caller |

| Fork | Question | Recommended | Branches |
|------|----------|-------------|----------|
| **F-misc** | Which one final artifact is required? | explicit requested output or strongest format evidence | `1-docx` · `1-pdf` · `1-pptx` · strategic HTML presentation → `1-slides` · `1-xlsx` · `1-diagram-maker` · `1-imagine` · `1-hatch-pet` · `1-json-canvas` · `1-defuddle` · `1-internal-comms` · **Agent judgment** |
| **F-PET1** | Which one pet result is needed? | explicit verb or strongest candidate-state evidence | `2-hatch-pet-build` · `2-hatch-pet-repair` · `2-hatch-pet-validate` · `2-hatch-pet-install` · **Agent judgment** |

**Return:** the hub reads no content and invokes no tool. It passes one exact artifact candidate and
effect boundary to one leaf or the Pet sub-hub; a second conversion, pet operation, publication, or catalog change is a separate request.
Worktrees isolate repository files, not desktop apps, browser profiles, cloud files, fonts, accounts, or URLs.

---

## Domain 15 — UI/UX

| | |
|--|--|
| **★ Hub** | `/0-ui-ux` |
| **Children** | **pipeline:** `1-ui-ux-pro-max` · **sub-hubs:** `1-brand` (guidelines, review, context extraction; F-BR1), `1-user-research` (study plan or completed-evidence synthesis; F-UR1) · **leaf:** `1-design-system`, `1-ui-styling`, `1-design` (one logo/icon/social/identity asset), `1-banner-design` (one promotion), `1-slides` (one self-contained HTML deck), `1-customer-experience-audit` (one read-only external-customer backlog) · **soft:** `1-frontend-ui-engineering` (Ship primary; one interaction surface with caller/candidate/worktree return) · **satellite:** `1-impeccable`, `1-visual-edit` (explicit tool workflows) |
| **Pipeline** | pin caller + immutable request/candidate + evidence/constraints/authority + optional worktree/runtime → direct route or material-only **F-UI1** → exactly one specialist → return evidence, verification, effects, assumptions, and limits to actual caller |

| Fork | Question | Recommended | Branches |
|------|----------|-------------|----------|
| **F-UI1** | What kind of UI/UX work? | Design intelligence for app/web UI → `/1-ui-ux-pro-max` | design intelligence · customer-experience audit · user research · brand · tokens · presentation-only styling · one logo/icon/social/identity asset · one banner/ad/hero image · one self-contained HTML presentation · production a11y UI · Impeccable tool workflow · live-app visual editing (`1-visual-edit`) · **Agent judgment** |

**Brand sub-hub F-BR1:** exact brand outcome → guideline authoring/update (`/2-brand-guidelines`), read-only
compliance review (`/2-brand-review`), read-only context extraction (`/2-brand-context-extract`), or **Agent judgment**.

**User Research sub-hub F-UR1:** exact research-document outcome → study-plan authoring
(`/2-user-research-plan`), completed-evidence synthesis (`/2-user-research-synthesis`), or **Agent judgment**.

**Not for:** product requirements grilling (`/0-grilling`), engineering ship work without a visual-design ask (`/0-implement`), or office file formats (`/0-office`).

---


## Domain 16 — Thinking

| | |
|--|--|
| **★ Hub** | `/0-thinking` |
| **Children** | **soft (diagnose):** `1-thinking-scientific-method`, `1-thinking-five-whys-plus`, `1-thinking-kepner-tregoe`, `1-thinking-systems`, `1-thinking-map-territory`, `1-thinking-cynefin`, `1-thinking-socratic` · **soft (decide):** `1-thinking-reversibility`, `1-thinking-opportunity-cost`, `1-thinking-probabilistic`, `1-thinking-second-order`, `1-thinking-steel-manning` (dual · primary Grilling), `1-thinking-bounded-rationality`, `1-thinking-circle-of-competence`, `1-thinking-lindy-effect` · **soft (create):** `1-thinking-first-principles`, `1-thinking-lateral`, `1-thinking-triz`, `1-thinking-via-negativa`, `1-thinking-thought-experiment`, `1-thinking-jobs-to-be-done`, `1-thinking-effectuation` · **soft (risk/response):** `1-thinking-pre-mortem`, `1-thinking-red-team`, `1-thinking-margin-of-safety`, `1-thinking-theory-of-constraints`, `1-thinking-ooda` · **leaf (perspective/strategy):** `1-perspective-analysis`, `1-thinking-ethical`, `1-strategic-analysis`, `1-competitive-analysis` · **satellite:** `1-thinking-model-combination`, `1-plan-arbiter` |
| **Pipeline** | pin caller + immutable candidate + evidence/authority + optional worktree → direct one-leaf route or material-only **F-T1/F-T2** → leaf or NONE → return artifact to actual caller; no automatic composition, diagnosis, implementation, or action |
| **Source** | Core: `archive/vendor/cc-thinking-skills/` (tjboudreaux/cc-thinking-skills MIT) · selective lateral/ethical leaves: `archive/vendor/ysskrishna-ai-agent-skills/` (MIT) · model-router folded into hub |

| Fork | Question | Recommended | Branches |
|------|----------|-------------|----------|
| **F-T1** | Right thinking frame already clear? | Yes if user named a model | invoke leaf · hub route F-T2 · NONE · **Agent judgment** |
| **F-T2** | What kind of thinking help? | Match problem type | diagnose/understand · decide · create · risk/response · perspectives/strategy · compose · compare existing plans (`1-plan-arbiter`) · **Agent judgment** |

**Not for:** house routing (`/0-butler`), plan interview (`/0-grilling`), live bug pipeline (`/0-diagnosing-bugs`), security product audit (`/1-security-auditor`), simplify mode (`/0-ponytail`).

**Cousins:** diagnose frames soft-cross Diagnose hub; red-team soft-cross Review security; via-negativa soft-cross Ponytail; socratic and steel-manning primary remain Grilling.

---

## Domain 17 — Git

| | |
|--|--|
| **★ Hub** | `/0-git` |
| **Children** | **pipeline helpers (caller-return, not an automatic sequence):** `1-git-worktrees`, `1-atomic-git-commits`, `1-finish-branch`; `1-pr-repair`; `1-pr-review-and-repair`; `1-stacked-pr-repair`; `1-stacked-pr-review-and-repair` · **leaves:** `1-git-changelog`, `1-git-text-normalization` (scoped encoding/EOL/attributes), `1-resolving-merge-conflicts`, `1-github-cli`, `1-github-pr-comment-intake` (read-only PR discussion), `1-pr-comment-drafter` (outbound prose, draft only) · **soft (Ship primary):** `1-pr-summarizer` (main PR description) |
| **Pipeline** | optional isolation → return to requesting implementation/repair workflow; implementation → authorized atomic commits → return to caller; requested branch outcome → chosen merge/PR/keep option; active conflict → resolve → resume interrupted operation; binary diff or scoped text normalization → Git text normalization → requested atomic commit groups; GitHub PR discussion → comment intake → requested assessment/repair; outbound comment → draft → explicitly authorized GitHub post/edit; one PR or PR stack → scoped repair-only or review/repair convergence |

| Fork | Question | Recommended | Branches |
|------|----------|-------------|----------|
| **F-G1** | What Git operation is needed? | infer the narrowest operation from repository state | worktree · atomic commits · changelog · text normalization · conflict resolution · GitHub CLI operation · PR comment intake · PR comment draft · PR description · single-PR repair-only · single-PR review+repair · stack repair-only · stacked review+repair · finish branch · **Agent judgment** |
| **F-G2** | How should mixed changes be grouped? | by independently revertible behavior | proposed atomic groups · user-specified grouping · leave ambiguous changes uncommitted · **Agent judgment** |
| **F-G3** | What is the intended base-to-tip PR order? | derive parent-child edges; stop if ambiguity remains | user-supplied order · provider/stack-tool order · **Agent judgment** |
| **F-G4** | Which PR should be reviewed and repaired? | current branch's unique open PR | user-named PR · unique current-branch PR · **Agent judgment** |
| **F-G5** | What PR prose is needed? | main PR description | PR description → `1-pr-summarizer` · individual comment → `1-pr-comment-drafter` · **Agent judgment** |

**Not for:** product implementation (`/0-implement`), code-quality review (`/0-review`), or release rollout (`/1-shipping-and-launch`).

## Domain 18 — Agent engineering

| | |
|--|--|
| **★ Hub** | `/0-agent-engineering` |
| **Children** | **leaf:** `1-agent-evaluation`, `1-tool-schema-design`, `1-human-in-the-loop`, `1-mcp-server-building`, `1-agent-workflow-observer` · **soft (shared):** `1-parallel-agents`, `1-observability-and-instrumentation` (bounded operational metadata; sensitive content omitted by default; no hosted operations) · **security cross-links:** `2-prompt-injection-defense`, `2-skill-supply-chain-audit` · **additions:** `1-asd-ste100`, `1-llm-cost-design`, `1-ai-suitability`, `1-context-retrieval-design` |
| **Route** | one clear concern → one leaf → candidate/evidence/effects/limits returned to the caller; workflow observation uses a fixed completed/paused snapshot and applies nothing; no mandatory lifecycle |

| Fork | Question | Recommended | Branches |
|------|----------|-------------|----------|
| **F-AE1** | Which one AI application or agent-system outcome is required? | infer the narrowest specialist; ask only when two outcomes materially differ | /1-agent-evaluation · /1-asd-ste100 · /1-tool-schema-design · /1-human-in-the-loop · /1-mcp-server-building · /1-agent-workflow-observer · /1-parallel-agents · /1-observability-and-instrumentation · /2-prompt-injection-defense · /2-skill-supply-chain-audit · /1-llm-cost-design · /1-ai-suitability · /1-context-retrieval-design · Agent judgment |

Tool-schema design receives design/read-only-review/authorized-edit mode, provider
dialect, neighboring tools, candidate and allowed effects. It returns to the hub,
MCP, oversight or security caller. Static/provider validation is separate from runtime
authorization; neither selection evaluation nor schema review exercises the real
consequential action. Source inspection needs no worktree; authorized edits use a
matching isolated checkout only when needed and return to the caller.

The hub itself reads no candidate, creates no worktree, delegates no agent, and runs no
tool. Every selected leaf receives exact system/artifact/environment and version, caller,
trust and privacy boundaries, allowed checks, exclusions, authority, and—when Git-backed—
repository/worktree/branch/`HEAD`, dirty ownership, and candidate. Worktrees do not isolate
provider accounts, credentials, MCP processes, queues, telemetry, browsers, approvals,
deployments, or other shared services.

Prompt-injection selection carries caller mode, scope, candidate and allowed checks.
`2-prompt-injection-defense` keeps assessment read-only and returns evidence to its
caller; tool/approval/evaluation handoffs are conditional, not automatic implementation
or incident containment. Source inspection needs no new worktree; authorized runtime
checks or edits use the matching isolated workspace when needed and return here.

**Not for:** ordinary product implementation (`/0-implement`) or broad application security review (`/1-security-auditor`).

## Domain 19 — DevOps

| | |
|--|--|
| **★ Hub** | `/0-devops` |
| **Children** | **leaf:** `1-infrastructure-as-code`, `1-cloud-platform-operations`, `1-container-platform-operations`, `1-database-and-storage-operations`, `1-postgres-read-only`, `1-network-and-edge-operations`, `1-server-and-fleet-operations`, `1-platform-engineering`, `1-ai-platform-operations`, `1-identity-and-secrets-management`, `1-resilience-and-disaster-recovery`, `1-compliance-engineering` · **pipeline:** `1-incident-response` · **soft (shared):** `1-ci-cd-and-automation` (one workflow/check contract), `1-observability-and-instrumentation` (one question-to-signal contract), `1-shipping-and-launch` (one immutable release candidate; explicit authority per remote stage), `2-security-and-hardening` · **additions:** `1-manual-procedure-wizard` |
| **Pipeline** | pin environment/candidate/worktree/authority → select one specialist → design/read-only diagnosis or authorized local change → verify → return; rollout/remote operations require separate authority |
| **Source** | `archive/vendor/devops-security-agent-skills/` and `archive/vendor/awesome-copilot/` — untrusted reference snapshots; live skills preserve authority boundaries |

| Fork | Question | Recommended | Branches |
|------|----------|-------------|----------|
| **F-O1** | What operational concern should we handle? | infer the narrowest evidence-backed specialist; ask only when two outcomes materially differ | infrastructure as code · cloud platform · containers and orchestration · databases and storage · network and edge · servers and fleets · platform engineering · AI platform operations · identity and secrets · incident response · resilience and disaster recovery · compliance engineering · CI/CD · observability · shipping and rollout · security hardening · Agent judgment |

**Not for:** application feature implementation (`/0-implement`), security findings (`/1-security-auditor`), or agent-system design (`/0-agent-engineering`).

## Domain 20 — Marketing

| | |
|--|--|
| **★ Hub** | `/0-marketing` |
| **Children** | **on-ramp:** `1-marketing-product-marketing` · **pipeline:** `1-marketing-marketing-loops` · **leaf:** 48 focused strategy, research, conversion, content, SEO, paid-media, measurement, growth, partnership, lifecycle, and sales skills · **additions:** `1-marketing-blog-editor`, `1-marketing-healthcare-blog-writing` |
| **Pipeline** | pin outcome, audience, evidence, jurisdiction, account state, and authority → select one narrow child → advisory or draft deliverable → separate explicit authority for any external effect |
| **Source** | `coreyhaines31/marketingskills` pinned at `5b2c0007766c6a1cf1d53fd8fc73e979e0821022`; upstream tools, installers, and plugin metadata were not promoted |

| Fork | Question | Recommended | Branches |
|------|----------|-------------|----------|
| **F-M1** | Which marketing outcome is primary? | infer the narrowest evidence-backed specialist; ask only when two categories materially differ | strategy/research · conversion/lifecycle · content/messaging · search/discovery · paid/measurement · growth/partnerships/sales · Agent judgment |

**Not for:** product or UX research (`/1-user-research`), general strategy (`/1-strategic-analysis`), brand systems (`/1-brand`), or software release work (`/1-shipping-and-launch`).


## Global entry fork

| Fork | Question | Recommended | Branches |
|------|----------|-------------|----------|
| **F7** | What kind of work? | Narrowest domain supported by the request | Design · Ship · Review · Triage · Diagnose · Fog · Architecture · Vault · UI/UX · Git · Agent engineering · DevOps · Marketing · Office/artifact · Catalog facilities · Learn · Simplify · Thinking · **Agent judgment** |

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
     ┌── explicit setup → ★ 0-setup-rohitas-skills (F-S1) → one child → stop
     ├── unsettled product intent → ★ 0-grilling → spec/plan when needed
     └── clear build request → ★ 0-implement
                              │
            fitting evidence loop (F-TDD1; 1-tdd only when suitable)
                              │
                       1-code-review
                              │
             optional authorized atomic commits

Open-ended review request → ★ 0-review (F-R1) → one review specialist.
```

## Residual — Personal

| | |
|--|--|
| **Package** | `personal/` (not a domain hub) |
| **Skills** | `1-pi-agent-rust` (project-specific) |
| **Rule** | Not promoted; hub membership optional / personal residual |
