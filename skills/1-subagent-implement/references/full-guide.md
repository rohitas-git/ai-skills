# Subagent plan execution

Use after the user selects `/1-subagent-implement`: one bounded implementer at a
time, a task-scoped review, then a review of the complete requested change.
Context isolation is not filesystem isolation. Subagents sharing a checkout also
share its files and Git state.

## Entry and workspace

1. Read the agreed plan and constraints. Resolve contradictions that affect scope,
   correctness or authority before dependent work; do not let example code override
   repository rules. No plan: hand back to `/1-write-plan`.
2. Record the caller, repository, task branch, original diff boundary, current SHA,
   dirty paths, runtime requirements and workspace/service ownership. For a stack,
   use the immediate parent rather than including ancestor PRs in the task diff.
3. Use `/1-git-worktrees` only for needed isolation, then resume here. Do not create
   one worktree per sequential worker or treat a branch name as isolation.
4. Confirm the host has a delegation tool. Use its documented API, not imaginary
   subagent types or model names. Inherit the current model unless the user or
   applicable task policy requests an available override; do not claim a cheaper
   model is faster or a stronger one guarantees correctness.
5. Keep one writer per checkout, including the controller. Reviews happen after
   the writer stops; read-only reviewers must not race a changing candidate.
   Shared contracts, migrations, generated artifacts and lockfiles stay serial.
   Concurrent independent workstreams are `/1-parallel-agents`, not this loop.

## Durable task state

Use an existing project-native progress mechanism or an agreed local artifact
directory. Do not overwrite another run's ledger or automatically commit scratch
files. The optional [workspace helper](./scripts/sdd-workspace) resolves a local
ignored directory; [task-brief](./scripts/task-brief) supports numbered
`# Task N` Markdown headings. For other plan formats, supply a brief manually
rather than pretending the extractor succeeded.

Record plan identity/revision, task IDs/dependencies, before/after candidate
identity, files, verification commands/results and both review verdicts.
On resume, reconcile that record with actual code and Git state. A “complete”
marker is a claim to verify, not authority to skip missing work; missing memory
is not reason to repeat work already evidenced. Rebase, plan changes or edits
invalidate affected evidence; recheck those portions, not every completed task.

## Per-task loop

1. **Brief:** use [implementer-prompt.md](./implementer-prompt.md). Supply one task's
   full requirements, exact binding values, dependency contracts, allowed/protected
   files, canonical checkout path/branch/SHA, baseline dirty changes, verification,
   authority limits, and report destination. A short brief must not omit acceptance
   criteria. Include enough surrounding code context to understand the task.
2. **Implement:** dispatch a fresh worker and answer material questions. Focused
   checks during iteration; use TDD only for an agreed deterministic seam with a
   known oracle. Commit only if explicitly included in the worker's authority.
   No worker push, merge, rebase, branch switch or workspace cleanup by default.
3. **Inspect status:** DONE is a claim ready for review, not completion.
   DONE_WITH_CONCERNS carries unresolved risks; distinguish substantive blockers
   from observations. NEEDS_CONTEXT gets targeted context. BLOCKED gets safe,
   in-scope diagnosis, a narrower task or a user decision when necessary.
   Do not redispatch the same failed attempt without new evidence or changed inputs.
4. **Prepare evidence:** stop the writer, inspect actual changes and reconcile
   them with the brief and pre-task baseline. Include all task changes, not just
   the last commit. Separate unrelated dirty work without moving or stashing it
   implicitly. A task's starting SHA alone cannot distinguish pre-existing
   uncommitted work: retain the baseline diff/path evidence too.
5. **Review:** use [task-reviewer-prompt.md](./task-reviewer-prompt.md), with brief,
   implementer report and candidate evidence. Require two verdicts: spec compliance
   and code quality. Allow focused dependency/caller inspection to resolve a named
   risk; do not constrain a reviewer to an insufficient hunk or pre-rate findings.
6. **Repair and re-review:** adjudicate evidence-backed findings against the
   requested scope. Fix in-scope blockers and refresh affected verification and
   review evidence. A plan-mandated defect is a conflict to resolve, not permission
   to ignore a finding or silently change the plan. Record minor/nonblocking
   suggestions separately; do not turn them into automatic scope expansion.
7. **Accept:** mark the task reviewed only when required criteria and both verdicts
   are supported. Resolve “cannot verify” items or carry them as explicit blockers;
   never convert uncertainty into approval. Continue in dependency order.

If a worker becomes unavailable, inspect its actual files and Git state before
replacement. The controller may perform an authorized bounded repair itself when
appropriate, then obtain independent review; “context purity” is not a reason to
leave recoverable work blocked. Never duplicate an active writer.

## Evidence packaging

Run helpers **from the target checkout**, using their absolute installed paths,
not from the skills catalog:

```text
bash <skill-dir>/references/scripts/task-brief <plan-path> <task-number>
bash <skill-dir>/references/scripts/review-package <before-sha> <after-sha>
```

Use the host-required command wrapper. Both helpers print the artifact path.
Their default artifacts are private, unique files; an explicit output must be new.

The review helper supports **clean, committed ranges only** and rejects a dirty
checkout. It resolves commit IDs and captures every commit in the supplied range,
not just HEAD~1. For dirty work, provide a task-scoped evidence package manually:
baseline and current tracked diffs (staged and unstaged), exact task-owned
untracked files, candidate identity and known omissions. Read new-file content;
`git diff` alone omits untracked files. Do not stage, commit, clean, or stash user
files just to make the helper run. Do not include secrets in a review package.

Verify package coverage against the actual checkout. After any fix, produce fresh
evidence; do not pass an old package with a new SHA label. The controller must
inspect evidence rather than forwarding a worker's success summary as proof.

## Final review and return

After all task gates, review the entire requested change through `/1-code-review`.
This catches cross-task integration defects, not unrelated repository debt.
Use the recorded scope boundary and current candidate, include deferred concerns,
and run missing integration checks. Avoid rerunning unchanged tests merely for
ceremony, but invalidate stale results and run checks that address new risks.

Return plan/task completion, final candidate (SHA plus dirty-state evidence),
changed files, checks, review outcomes, outstanding findings and workspace/service
ownership to the caller. `/1-finish-branch` is conditional on requested branch
integration/PR options; `/1-atomic-git-commits` requires commit authority.
No automatic publication or cleanup follows a green review.
