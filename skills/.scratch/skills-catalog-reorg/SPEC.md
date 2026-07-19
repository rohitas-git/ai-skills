# Spec: Skills catalog reorg (Matt buckets + butler)

## Problem Statement

The skills catalog is a flat warehouse of ~78 skills plus a nested `agent-skills` pack. That creates:

1. **Routing fights** — dozens of model-invoked descriptions compete (~5–6k tokens always on); cousins (grill, review, TDD, learn, architecture) steal each other's triggers.
2. **No house layout** — skills are not organized like Matt Pocock's buckets (`engineering` / `productivity` / `misc` / `personal` / `in-progress` / `deprecated`), so discovery and promotion rules are ad hoc.
3. **No single steward** — `ask-matt` only routes; there is no skill that **ingests** new skills into the workflow, **lints** catalog health, or **organizes** moves/deprecations. Wiki-style stewardship exists for project wikis (`project-wiki-manager`) and the Obsidian vault, but not for the skill catalog itself.
4. **Split identities** — setup is still named for Matt; agent-skills can co-load a second meta-router; absolute vault paths are repeated; TDD philosophy is duplicated.

The user needs a durable catalog structure, one steward skill (**butler**), Rohitas naming, Matt-style chaining (`to-spec` → `to-tickets` → `implement`), and a clear rule for what (if anything) is promoted from `agent-skills`.

## Solution

Reorganize the catalog to **Matt Pocock structure and chaining**, with:

1. **Six buckets** under the catalog root, with Matt promotion rules (only `engineering|productivity|misc` in the root README).
2. **`butler`** — a user-invoked steward skill (project-wiki-manager pattern for **skills**, not wiki atoms) with four ops: **query**, **ingest**, **lint**, **organize**. Owns `flows.md` (chaining SSOT). Absorbs `ask-matt`.
3. **`setup-rohitas-skills`** — rename of `setup-rohitas-skills`; configures issue tracker, triage labels, domain docs, and vault path SSOT for consumer skills.
4. **Primary engineering path:** grill → (optional prototype via handoff) → **`to-spec` → `to-tickets` → `implement`** (drives `tdd` + `code-review`), with documented on-ramps.
5. **Selective agent-skills integration** only via butler ingest (never whole pack / never `using-agent-skills`); e.g. merge TDD material into single `tdd`.
6. Residual agent-skills under **`vendor/`** (out of discovery). Optional later: `scripts/lint-skills` mirroring butler lint.

## User Stories

1. As a catalog owner, I want skills grouped into Matt-style buckets, so that I know what is promoted daily vs personal vs deprecated.
2. As a catalog owner, I want root README to list only engineering/productivity/misc, so that agents and humans share a short promoted set.
3. As a catalog owner, I want each bucket README to link every skill with a one-line description, so that browsing is fast.
4. As a catalog owner, I want CLAUDE.md (or AGENTS.md) to state bucket rules, so that future agents do not re-flatten the tree.
5. As a user, I want a single skill named **butler** I can invoke when I am lost, so that I get a recommended skill or flow without memorizing the catalog.
6. As a user, I want butler to **query** from disk + `flows.md` only, so that it never invents skills that are not installed.
7. As a user, I want butler to explain why not to use a cousin skill, so that routing collisions are conscious.
8. As a skill author, I want butler to **ingest** a new skill folder, so that it is bucketed, indexed, and chained correctly.
9. As a skill author, I want ingest to run an integration test before promote, so that dual meta-routers and name collisions are rejected.
10. As a skill author, I want ingest to prefer merge into an existing winner over a second skill, so that the catalog stays lean.
11. As a skill author, I want human confirmation before multi-file ingest mutations, so that butler does not reorganize silently.
12. As a catalog owner, I want butler to **lint** structure, descriptions, hard deps, and README drift, so that the catalog cannot rot quietly.
13. As a catalog owner, I want lint to flag model-invoked budget and trigger collisions, so that context load stays bounded.
14. As a catalog owner, I want lint to require hard deps (`to-spec`, `to-tickets`, `triage`) to point at `/setup-rohitas-skills`, so that tracker config is explicit.
15. As a catalog owner, I want butler to **organize** (move, rename, deprecate) with tombstones, so that successors are documented.
16. As a catalog owner, I want butler **never** to create wiki/concept atoms, so that skill stewardship stays separate from knowledge wikis and the vault.
17. As a developer starting a feature, I want the main flow documented as grill → to-spec → to-tickets → implement, so that multi-session work is consistent.
18. As a developer, I want single-session work to skip to implement after grill when appropriate, so that small changes stay light.
19. As a developer, I want implement to drive tdd then code-review, so that build and review are one path.
20. As a developer, I want on-ramps (triage, diagnosing-bugs, wayfinder, architecture) to merge into the main flow by name, so that I do not invent ad hoc pipelines.
21. As a developer, I want wayfinder to exit only via to-spec → to-tickets, so that fog maps are not implemented raw.
22. As a developer, I want triage to never re-triage tickets produced by to-tickets, so that AFK tickets stay agent-ready.
23. As a developer, I want setup-rohitas-skills to configure issue tracker, triage labels, and domain docs, so that hard-dep skills have config.
24. As a vault user, I want vault root configured once (setup or rohitas-vault-wiki SSOT), so that absolute paths are not copy-pasted across skills.
25. As a catalog owner, I want setup-rohitas-skills renamed to setup-rohitas-skills everywhere, so that branding matches ownership.
26. As a catalog owner, I want ask-matt retired after butler query ships, so that there is one router.
27. As a catalog owner, I want software-architecture deprecated, so that its poison-wide triggers stop stealing work.
28. As a catalog owner, I want agent-skills parked under vendor by default, so that using-agent-skills cannot co-route.
29. As a catalog owner, I want selected agent-skills content integrated only via butler ingest, so that promotions are intentional.
30. As a catalog owner, I want test-driven-development merged into a single tdd skill, so that TDD philosophy is one source of truth.
31. As a skill author, I want create-skill to hand off to butler ingest, so that scaffolds become first-class catalog citizens.
32. As a skill author, I want writing-great-skills to remain craft reference (not replaced by butler), so that predictability theory stays separate.
33. As a skill author, I want reflect to optionally hand off to butler lint/organize, so that session learnings can trigger catalog hygiene.
34. As a catalog owner, I want skills-lock paths updated after moves, so that lock integrity holds.
35. As a multi-agent user, I want install paths documented for bucket layout, so that Grok/Claude/Codex still find skills.
36. As a catalog owner, I want optional scripts/lint-skills mirroring butler lint, so that CI can fail on catalog regressions.
37. As a developer, I want grill-me and grill-with-docs as thin wrappers over grilling, so that one interview body is maintained.
38. As a developer, I want hard vs soft setup dependencies documented (ADR-style), so that soft skills degrade gracefully without cargo-cult setup pointers.
39. As a catalog owner, I want model-invoked skill count under ~25 after the reorg, so that description load is affordable.
40. As a user, I want root README quickstart: setup-rohitas-skills then butler, so that orientation takes under two minutes.
41. As a catalog owner, I want personal/in-progress/deprecated skills excluded from root README, so that promotion is deliberate.
42. As a developer, I want vocabulary skills (domain-modeling, codebase-design, coding-standards) documented under the main flow, so that they are pulled in rather than competing as entry points.
43. As a vault user, I want the vault chain documented in butler flows, so that personal knowledge ops stay consistent with catalog style.
44. As a catalog owner, I want ingest to update flows.md when a skill is added to a chain slot, so that the map stays true.
45. As an agent implementing tickets later, I want this spec extensive enough to slice into vertical tickets via to-tickets, so that work can be AFK-grabbable.

## Implementation Decisions

### Catalog layout
- Introduce buckets at catalog root (not a nested `skills/skills/` unless tooling forces it): `engineering/`, `productivity/`, `misc/`, `personal/`, `in-progress/`, `deprecated/`, plus `vendor/agent-skills/`.
- Matt promotion rule: root README lists only engineering + productivity + misc; personal/in-progress/deprecated/vendor must not appear there.
- Each bucket has README with linked skill name + one-line blurb.
- CLAUDE.md (preferred if present, else AGENTS.md) records bucket rules in Matt’s four-bullet form.

### butler skill
- Location: `productivity/butler/`.
- User-invoked (`disable-model-invocation: true`).
- Thin SKILL.md (~80–120 lines) dispatching four ops; details in `references/`:
  - `catalog-layout.md`, `flows.md`, `ingest-workflow.md`, `lint-checklist.md`, `query-workflow.md`, `hard-rules.md`.
- **Query:** recommend skills/flows from disk + flows.md; no invented skills.
- **Ingest:** integration test → propose bucket/invoke/merge/chain → confirm → mutate indexes/lock/flows → lint.
- **Lint:** structure, README membership, description/trigger collisions, hard-dep pointers, forbidden names, sprawl, vault SSOT, deprecated successors.
- **Organize:** rehouse/rename/deprecate with tombstones.
- Hard rules: no atoms/concept pages; confirm before multi-file mutate; no dual meta-router.
- Session start: resolve catalog root, confirm layout, state paths.

### Integration test (ingest promote gate)
All must pass: (1) gap in flows, (2) no collision / prefer merge, (3) explicit prev/next, (4) hard vs soft setup correct, (5) Matt-short or progressive-disclosure plan, (6) never promote `using-agent-skills`.

### setup-rohitas-skills
- Rename from `setup-rohitas-skills` (dir, name, lock, all pointers).
- Keeps Matt setup shape: issue tracker, triage labels, domain docs → `docs/agents/*` + `## Agent skills` block.
- Adds vault root SSOT (e.g. `docs/agents/vault.md` or domain section).
- Branding: Rohitas skills.

### Hard vs soft dependencies
- **Hard** (must point at `/setup-rohitas-skills`): `to-spec`, `to-tickets`, `triage`.
- **Soft** (CONTEXT/ADR if present): `tdd`, `diagnosing-bugs`, `improve-codebase-architecture`, design vocabulary skills.

### Chaining SSOT (`butler/references/flows.md`)
- Precondition: setup-rohitas-skills.
- Main: grill-with-docs | grill-me → optional handoff⇄prototype → multi-session? to-spec → to-tickets → implement* else implement*; implement → tdd → code-review → commit.
- On-ramps: triage, diagnosing-bugs, wayfinder→to-spec…, improve-codebase-architecture, optional ship/security if ingested.
- Vocabulary and vault chains as in plan.
- Meta: create-skill → butler ingest; reflect → optional butler lint/organize.

### agent-skills policy
- Default: move pack to `vendor/agent-skills/` (out of discovery).
- Merge `test-driven-development` ideas into single **`tdd`** (no second skill).
- Promote others only via butler ingest after gap check (security, shipping, observability, performance, api, frontend, source-driven, code-simplification as candidates).
- Never promote `using-agent-skills`.
- Do not promote interview-me / spec-driven-development / planning-and-task-breakdown as peers of grill / to-spec / to-tickets.

### Deprecations / renames
- `ask-matt` → absorbed by butler query (tombstone).
- `setup-rohitas-skills` → `setup-rohitas-skills`.
- `software-architecture` → deprecated Week 1.
- Prefer one create-skill path if create-skill and skill-creator both exist.

### Craft bar (during reorg, not infinite polish)
- Target model-invoked &lt; 25; description budget ~&lt; 2k tokens for promoted set.
- User-invoke setup, butler, ponytail satellites, task-observer, rare office tools by default.
- Progressive disclosure for sprawl (task-observer, hatch-pet).
- Cousin clusters get exclusive Use when / Don’t use when (grill, review, learn, architecture).
- Vault absolute path only via SSOT.

### Phasing (implementation order)
1. Scaffold buckets + move skills + renames + butler spine + flows + vendor park + deprecate toxic.
2. Butler query + ingest + setup rewrite + hard/soft pointers + tdd merge + cousin de-conflict.
3. Butler lint + main-path craft + selective promotes + description budget + Done when checklists.
4. Optional lint script, smoke fixtures, vendor cleanup, reflect bridge, root README polish.

## Testing Decisions

What makes a good test here (catalog / agent-skill domain):

- Assert **observable catalog behavior and file contracts**, not internal prose wording of every skill body.
- Prefer the highest seam: **butler ops outputs** and **lint report**, then **filesystem/index invariants**.

Seams (in preference order):

1. **Lint report seam** — given a fixture catalog tree, lint returns structured findings (or clean). Primary automated seam for `scripts/lint-skills` if added; butler lint should match the same checklist.
2. **Catalog index seam** — after organize/ingest (or scripted move), root README membership, bucket README lines, name==dir, skills-lock paths hold.
3. **Query seam** — given fixture catalog + flows.md, query for fixed utterances returns the expected skill name(s) (smoke fixtures; can start as documented manual cases, then script).
4. **Ingest dry-run seam** — propose plan without write; integration test pass/fail is visible.

Prior art: `agent-skills` evals/scripts (structure + routing); `wiki-query`/`pr-summarizer` evals; Matt’s list-skills scripts. Prefer adapting lightweight scripts over LLM-only “tests.”

Modules under test (logical):

- butler references (checklist fidelity)
- catalog layout invariants
- hard-dep string presence on named skills
- single tdd / no ask-matt / no setup-rohitas-skills / no using-agent-skills in discovery after cutover

## Out of Scope

- Using butler as a second brain, Obsidian vault, or project wiki (existing vault/wiki skills remain separate).
- Creating concept atoms or LLM-wiki pages from butler.
- Promoting or co-loading the entire agent-skills lifecycle (`using-agent-skills`, `/spec`…`/ship` as primary stack).
- Rewriting every skill body to agent-skills-style rationalizations tables.
- Changing vault **content** schema (only path SSOT packaging).
- Publishing a new public marketplace plugin listing (optional later).
- Full multi-agent install automation for every host (document paths; deep install tooling later).
- Renaming every historical Matt skill filename beyond setup + router absorption (tdd, triage, etc. keep names unless collision forces rename).

## Further Notes

- **Issue tracker for this monorepo:** GitHub `rohitas-git/ai-skills` (remote present). `docs/agents/` was not yet configured at spec time; first implementation ticket should run **setup-rohitas-skills** (after rename) or seed docs/agents so hard deps are real.
- **Seams agreed for agent work:** (1) catalog layout/index, (2) butler four ops, (3) flows + hard-dep contract. Prefer these over new application modules.
- **Next step after this spec:** `/to-tickets` to produce vertical tracer-bullet issues with blocking edges; label ready-for-agent.
- **Local copy of this spec:** `.scratch/skills-catalog-reorg/SPEC.md` in the skills catalog repo for offline use.
