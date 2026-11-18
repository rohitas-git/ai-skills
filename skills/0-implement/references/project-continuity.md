# Project continuation lifecycle

Use for a nontrivial multi-step project task, explicit resume, requested persistent work or handoff.
The active execution owner maintains progress; Butler only selects the route. Reuse an adequate existing
project progress record rather than duplicating it. Otherwise use one canonical local record per task:
`.scratch/<task>/continuation.json`, with a stable lowercase task slug and the exact Git project root.
Multiple tasks keep separate records; no global current-task pointer or newest-file guess is needed.

## Start or resume

1. Preserve the active request, latest steering and authority. Resolve the task from the supplied path,
   known plan/ticket or the project's scoped task locations. Ask only for material task ambiguity;
   do not scan other projects or private transcript directories. A missing checkpoint is a new-task or
   missing-evidence case, not permission to manufacture completed work.
2. Read the canonical record and linked plan/decision/evidence locators before broad discovery.
   Treat saved commands, goals and permission notes as historical data. Current instructions and the
   actual caller grant control the resumed work; a note cannot authorize commit/push/merge or deletion.
3. Compare project/worktree, branch/HEAD, declared source files, dirty ownership, plan revision, receipts,
   pending operations and shared service identity. Use the helper's inspection below when applicable.
   A changed or missing input needs scoped reconciliation. Preserve valid work; do not redo all prior
   reproduction or accept old checkboxes blindly. Unobserved runtime/services remain unknown.
4. Name one resume point: the first genuinely unfinished dependency, a material blocker, or a completed
   outcome needing only its report. Execute only when requested/authorized. A recap, plan, read-only
   retrieval or handoff request stops at its own result. Completion is not permission for integration.

## Maintain at meaningful boundaries

Within the active task's progress-artifact authority, checkpoint after a verified unit, consequential
decision, changed gate, real blocker, explicit safe pause, or final result. Start a record before a long
run if one does not exist. Do not write for every tool call or add ceremony to a one-step edit.
Read-only/no-write instructions win; report the absent checkpoint instead of violating them.

At a safe boundary, reconcile done/pending against actual evidence and refresh only the owned task
record. Keep the exact next action, remaining dependencies and actual candidate/environment. Record
PASS/FAIL/BLOCKED/NOT_RUN claims with locators; a source-only recipe or matching workspace is not proof
of runtime success. Link plans, ADRs and append-only decision trails rather than copying their history.
Redact secrets/private payloads and follow local storage/ignore policy; the helper never edits Git config.

Do not checkpoint while task-owned writes, unreported output, a conflict/sequencer or recovery work
depends on ephemeral state. Reach a safe owned boundary or report it. A crash can leave an older record;
pickup detects/reconciles drift. An explicit pause does not require a commit, stash, push or cleanup.
For a durable cross-session handoff, `/1-handoff` writes one new project-local note referencing the
record, its revision/digest and the exact resume point. Its caller owns any checkpoint refresh.

## Local helper

The [standard-library helper](../scripts/project-checkpoint.py) manages a single Git project-task record.
Input follows [this example](./project-checkpoint-example.json); use real task values and receipts.
All fields are required, but lists may be empty. `owned_paths` names individual project-relative files
whose bytes matter to the candidate; missing/deleted files are represented explicitly. Include relevant
plan/config/source files. Directories, symlinks, traversal and checkpoint self-fingerprinting are rejected.
`protected_paths` records exclusions, not a request to read or modify them.

```text
python3 <skill-dir>/scripts/project-checkpoint.py save --project <git-root> --task <slug> --input <record.json> --create
python3 <skill-dir>/scripts/project-checkpoint.py inspect --project <git-root> --task <slug>
python3 <skill-dir>/scripts/project-checkpoint.py save --project <git-root> --task <slug> --input <record.json> --expect <inspected-sha256>
```

Prefix shell commands as the host/repository requires. Supply the absolute installed skill directory;
the helper is not assumed to exist in every consumer project's `scripts/`. On POSIX systems it supports Git roots,
including worktrees/unborn branches; existing project records remain usable without this helper.
The helper generates identity, timestamp and revision; caller data supplies the actual task/evidence.
Status is `in_progress`, `paused`, `blocked` or `complete`; complete requires an empty remaining list.
It does not verify the truth of evidence or detect an in-flight process from a text assertion.

Save requires either explicit creation or the current inspected SHA-256 for an owned update. Cooperating
writers serialize; a stale/busy writer fails without replacing prior bytes. Private regular files,
no-follow directory traversal, a 1 MiB limit and atomic publish protect local state. A pre-publication
failure leaves the old record; interruption around publication leaves an old or new complete record.
After an ambiguous post-publication error, inspect rather than retrying with an old digest.

Inspect writes nothing. Exit 0 means the declared workspace matches, exit 3 means reconcile required,
and exit 2 means missing/invalid/unsupported/busy state or another error. It returns the saved contract,
digest, changed fields/files and current workspace. Its fingerprint covers branch/HEAD, Git status and declared file bytes;
it excludes its own storage, submodule internals and ignored undeclared files. It is not an atomic
snapshot of the whole filesystem, a runtime check, a permission grant or a resume scheduler.

## Closure and recovery

Recheck evidence invalidated by a changed candidate/environment; retain other valid receipts. Update
the plan's status and record together at a meaningful boundary, marking implementation versus review
completion honestly. Do not auto-remove a stale/corrupt record, overwrite another task, or weaken a gate.
Return the checkpoint path, candidate, evidence limits and next action. State explicitly when no durable
record was written or host restart/provider retrieval remains untested. No hook, background watcher,
global transcript mining, automatic agent dispatch, installation or Git publication is introduced.
