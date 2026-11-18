# Verified delivery and scoped cleanup

## Prepare a PR

An implementation or investigation does not automatically open a PR. For an authorized PR operation,
use the actual base/head, task-owned work and repository checks. Group changes through the existing
atomic-commit owner when commits are requested. Do not rebase, squash or require a new worktree just
for presentation if the current candidate already meets its contract.

Let `/1-pr-summarizer` own the evidence-backed briefing and repository template. A compact fallback
can cover problem, resulting behavior, scope, material trade-offs, affected consumers and validation;
link long evidence rather than imposing an absolute line cap. Respect requested draft/ready state.
Read back the created PR and actual base/head. Opening does not start repair, merge or monitoring.

## Land a verified dependent run

First obtain the required explicit merge authority. Pin the exact PR queue, immediate bases/current
heads, verification receipts, required CI/policy and a fixed ceiling. Independent verification is useful
when authorized/available; do not substitute author intent, green CI or a bot approval for the real
behavior evidence the repository requires. An AI countersign cannot grant a human/forge approval.

Walk from the bottom and stop at the first missing/stale/failed required verdict. A verified PR above
that gap cannot make the missing dependency verified. A PR made independent by rebasing to trunk is
a changed candidate requiring appropriate fresh checks.

Recheck candidate/base immediately before each merge. Patch-id can help inspect changes but does
not prove equivalent behavior after a changed dependency, conflict resolution, configuration or base.
Reuse receipts only when exact evidence and relevant environment still cover what lands. Inspect the
actual merge result when base drift can affect the patch; otherwise report the invalidated lane.

Use the actual approved forge operation and read back its result. Queued/auto-merge armed is not
merged. Confirm merged state and intended base/result. Retargeting, restacking and pushing the next
PR require the corresponding authority and expected remote SHA. Do not rewrite other branches or
extend the ceiling while the approved run lands. A no-merge request stops at current-head evidence.

## Worktree and other state cleanup

Inventory actual registered worktrees with the local-only audit and explicit base, then establish
ownership, active/pinned use, dirty/untracked/ignored data, local services and recoverability. Ancestry,
age, a safe-looking directory name or a script bucket is not permission to delete. Treat untracked
files as work to preserve, not throwaway scratch.

Return a concrete candidate set for the required user decision when deletion is not already explicitly
authorized. Apply only the exact authorized paths under repository policy, without force-discarding
dirty work. Preserve host-managed workspaces and artifacts. Simulator runtimes, app state, databases,
build caches and package caches are separate resources, never routine extensions of worktree cleanup.
Verify the scoped result and retained evidence; never pipe an inventory directly into deletion.

Adapted from the individually reviewed pstack 0.15.43 sources, MIT, Lauren Tan.
[Source-by-source decisions and checks](../../../guidelines/catalog/pstack-methods-review-2026-11-18.md).
