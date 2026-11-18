# Project continuity implementation plan

Status: applied, serially reviewed and verified locally; execution results below.
Source: the user's request to plan deeply, polish and implement the project-continuity gaps identified
in this conversation. Revision context: `codex/generalize-skill-catalog`, HEAD
`163b03982c510345a06a0ab1ed784e1440d3956d`, dirty working tree with earlier adoption/Butler work.
Those existing edits are protected; a pre-task hash inventory and target copies are retained locally.

## Goal and acceptance contract

A cold session given the project and task can find one current continuation record, understand the
accepted goal and scope, identify completed versus pending work and existing evidence, detect changed
workspace inputs, and resume the first genuinely unfinished step under current instructions. The
active execution owner maintains the record at meaningful boundaries, without making Butler an
executor or treating a saved instruction as fresh authority.

| ID | Required outcome | Acceptance oracle |
|---|---|---|
| C1 | Discoverable local task state | Default `.scratch/<task>/continuation.json`, one record per task; existing adequate project progress records take precedence. No global active-task pointer or private history scan. |
| C2 | Complete, bounded contract | Goal, phase/status, accepted scope/exclusions, decisions, operation/authority limits, owned/protected paths, artifact/evidence locators, remaining work, services and exact next action. Observed identity/timestamp/revision are generated. |
| C3 | Safe refresh | Explicit create versus digest-checked update; serialized cooperating writers, atomic publication, private files, bounded regular-file JSON, no symlink traversal or overwrite of corrupt/mismatched state. Pre-publication failure preserves prior bytes; interruption around publication leaves an old or new complete record. |
| C4 | Honest pickup | Current project/branch/HEAD/status plus declared source-file fingerprints compared with saved state. Change means reconcile, not automatic restart or false pass. A matching workspace is still not runtime proof or execution authority. |
| C5 | Continuous execution lifecycle | Start/resume → work → checkpoint after a meaningful verified unit, decision, blocker, safe pause or finish. One-step work stays proportional; read-only/plan-only requests remain read-only/plan-only. |
| C6 | Durable handoff | Known project/task uses a non-overwriting project handoff file referencing the canonical record. Unknown project identity retains the temporary-file fallback. Handoff never updates a record or resumes code implicitly. |
| C7 | Actual local cold-start check | Save a checkpoint in a disposable repository; a fresh process inspects it and returns the next action; changed source/HEAD/task and competing writes are rejected or classified. No model trial is implied. |
| C8 | Catalog integrity | Existing route ownership/invocation unchanged, lean main bodies, links/projections valid, provenance current, unrelated dirty work byte-preserved. |

## Design decisions and polished trade-offs

- Reuse the current execution, handoff, context and planning owners. Add one conditional lifecycle
  reference and one standard-library checkpoint helper, not a new hub, orchestration service or hook.
- Use one canonical JSON record rather than parallel JSON/Markdown copies. Existing Markdown plans,
  tickets, ADRs and append-only decision logs remain authoritative for their jobs and are linked.
  The JSON is human-readable and the helper's inspection output is readable; no generated second state.
- Keep one task record per project. Multiple tasks do not race a global “current task” file. If the
  task identity is ambiguous, inspect only the project's known task locations and resolve the actual
  ambiguity; do not pick the newest unrelated record by timestamp.
- The helper supports Git project roots/worktrees and captures branch/HEAD/status plus explicitly
  declared source files. It does not claim a filesystem-wide atomic snapshot, inspect every dependency,
  fingerprint databases, prove receipts, or retrieve inaccessible transcripts. Other projects can use
  the same contract in an existing manually maintained progress record.
- Writes need the active workflow's artifact/edit authority. A user request to implement a nontrivial
  project change normally includes its scoped progress artifact; explicit no-write instructions win.
  Historical permission notes are context, not grants. No installation, scheduling, model call, Git
  state change, external message, automatic WIP commit or checkpoint publication is introduced.
- Reuse evidence whose source/environment still matches. Recheck changed or missing claims, rather
  than rerunning everything or accepting an old checkbox. In-flight work waits for a safe boundary;
  interruption leaves an older record that pickup must reconcile.

The first design considered a second Markdown projection, whole-repository content hashing and a
global active pointer. Review removed all three: duplicate state drifts, whole-tree reads add cost
without proving external state, and a global pointer conflicts across independent tasks. A narrow
file list plus explicit fingerprint scope makes limitations visible.

## Task 1: Specify lifecycle and record contract

- Depends on: none. Covers C1, C2, C4–C6.
- New: `skills/0-implement/references/project-continuity.md` and the helper's schema/example documentation.
- Define field meanings, status vocabulary, default path, checkpoints, authority and stale-evidence
  handling, and ownership of creation/update versus non-overwriting handoff.
- Verify the contract against existing Handoff safe-boundary rules and local `.scratch/<task>` tracking.

## Task 2: Implement the bounded checkpoint helper

- Depends on: Task 1. Covers C2–C4, C7.
- New: `skills/0-implement/scripts/project-checkpoint.py`, `scripts/test-project-continuity.py`.
- CLI: `save --project ROOT --task SLUG --input JSON (--create | --expect SHA256)` and
  `inspect --project ROOT --task SLUG`. No task execution or broad discovery operation.
- Save validates input, checks record identity and expected digest under a lock, captures the observed
  workspace, writes a complete private temporary file and atomically replaces the canonical record.
- Inspect is read-only. It returns the saved data/digest, current declared workspace and a matching
  versus reconciliation-required disposition. Missing, corrupt and unsupported state remains an error.
- Use deterministic tests for cold pickup, stale source/HEAD/status, saved task/root mismatch,
  competing writers, symlinks/nonregular files/path traversal, private modes, bounded input and atomic
  publication failure. Source/data commands must never be executed.

## Task 3: Wire existing owners and surfaces

- Depends on: Tasks 1–2. Covers C1, C5, C6, C8.
- Implement and Execute Plan maintain checkpoints; Write Plan names the record/next dependency.
- Handoff chooses a project-local non-overwriting path when identity is known; its pickup reference
  uses the canonical record and never silently starts work. Working Context and Strategic Compact
  reuse the record or point to its owner, preserving their read-only boundaries.
- Butler routes an explicit project-task resume to the active execution owner; context reconstruction
  and chat catchup remain distinct. It does not write/checkpoint/execute the project.
- Update existing hub/flow projections and docs without inventing new skill names. Root catalog
  conventions, runtime invocation policy and installation configuration remain unchanged.

## Task 4: Apply to this task and verify cold pickup

- Depends on: Task 3. Covers C7–C8.
- Use the helper for this task's own `.scratch/project-continuity/continuation.json`, with the plan,
  verification report, declared file scope and exact next action. This is local state, not a commit.
- Inspect through a fresh process; demonstrate stale inputs and compare-and-swap failures only in
  disposable repositories. Preserve every pre-existing project file and record actual command exits.
- Run the focused helper tests, routing/continuity regressions, lint, projection freshness, previous
  source/tooling integrity and whitespace checks. Reconcile Spec, Standards and Maintainability findings.
- Update source locks and authorized adopted hashes without changing pinned upstream archives or
  retroactively rewriting historical test claims. Report local-runtime evidence separately from
  provider-agent behavior, host restart discovery and external-service state, which remain unrun.

## Plan review disposition

Ready for the stated scope after the simplifications above. Requirements map to concrete artifacts
and tests; serial execution avoids shared writers. No unresolved product decision prevents progress.
The script is a local artifact manager, not a permission engine or resume scheduler. Stop only for a
material collision/concurrent change or an effect outside the existing request, preserving prior state.

## Execution and final evidence

| Task | Disposition and observed evidence |
|---|---|
| 1 — lifecycle/contract | Complete. Existing records take precedence; the canonical default, authority boundary, declared fingerprint scope and safe publication semantics are documented. |
| 2 — helper | Complete. **22 executable tests passed**, including fresh-process pickup and negative drift/concurrency/path-safety/schema/publication controls. |
| 3 — integration | Complete. Existing owners and hub/flow surfaces linked; **754 routing/contract tests passed**; lint PASS with zero critical and four unchanged inbox warnings. |
| 4 — application/evidence | Complete. This task's real checkpoint was created and read through a fresh process with `workspace_matches` during integration; the canonical record is refreshed at closure. Eight prior method tests pass, all 80 source entries/149 current adopted-file hashes match, and all 440 earlier tooling files remain intact. |

The [verification report](../../../guidelines/catalog/project-continuity-2026-11-18.md) records scope,
checks and limitations. Of 2,463 pre-task file snapshots, 2,438 remain byte-identical; all 25 changed
existing files are declared task-owned paths. No missing/unexpected change or broken owned local link.
No commit, push, merge, installation, global hook, provider-agent trial or external effect was performed.
