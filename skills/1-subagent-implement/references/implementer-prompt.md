# Implementer task brief

Use the host's actual delegation API and inherited model unless an available
override is requested by the user or applicable policy. One bounded task, one
writer in the confirmed checkout. Fill the fields below; do not leave placeholders.

## Inputs

- Task ID and full requirements/acceptance criteria: <brief path or text>
- Binding constraints and dependency contracts: <exact values and relationships>
- Repository/worktree: <canonical path>; expected branch/SHA: <identity>
- Allowed files: <paths>; protected/pre-existing dirty files or hunks: <baseline>
- Scope exclusions: <explicit exclusions>
- Verification: <commands, runtime/services, acceptance evidence>
- Authority: <allowed edits; commit allowed or not; no default push/merge/cleanup>
- Report destination: <new task-owned path>

## Worker instructions

Read the brief and local instructions. Verify checkout identity and baseline before
editing. Implement only the task; inspect relevant callers and dependencies when
needed to understand behavior. Do not restructure unrelated code or silently
discard existing edits. If overlapping changes make ownership unclear, stop the
affected edit and report the conflict.

Use focused checks during iteration and the required checks for the final candidate.
Use TDD only where the agreed plan specifies a known deterministic behavior;
agent-authored happy-path tests are not an independent acceptance oracle.
Do not change a product contract simply to satisfy a stale test.

Do not commit unless the authority field permits it. Never push, merge, switch
branches, rebase, start another writer, reset services or remove a workspace unless
that exact operation is separately authorized. If an instruction conflicts with
repository policy or the task needs a material product/architecture decision,
report the evidence and ask the controller. Diagnose ordinary failures in scope.

Self-review completeness, correctness, scope and test quality before reporting.
After a review repair, update the report with the amended candidate and affected
check results; do not reuse a prior green result for changed code.

## Report

Write a concise evidence record, then return its path and status:

- DONE | DONE_WITH_CONCERNS | BLOCKED | NEEDS_CONTEXT.
- What was implemented or attempted; files and meaningful behavior changed.
- Current SHA and remaining staged/unstaged/untracked task changes.
- Commits only if authorized and actually created.
- Exact verification commands, tested candidate/environment, results and limits.
- RED/GREEN evidence only when TDD was required and actually performed.
- Self-review, unresolved concerns, missing requirements and requested decisions.

DONE means ready for independent review, not “approved” or “merged.” Do not claim
tests passed when unavailable or hide warnings: distinguish task regressions from
existing environment noise and explain material warnings.
