# Shared PR repair checkpoints

Load for single-PR and stack repair, with or without fresh review. These are shared
checks within the caller's loop; they do not start another repair workflow.

## Workspace and authority

Record owner/repository, PR number, head repository/ref, declared base ref, local
path/branch/SHA, remote head SHA, and dirty paths. A fork's head repository may differ
from the PR repository; never infer a push destination from the name `origin` alone.
Use `/1-git-worktrees` only when isolation is needed, then resume this caller's step.
For a stack, map each branch to its actual registered worktree and immediate parent;
serialize dependent history changes and never switch a branch out from another worker.

Each helper receives allowed files, base/head SHAs, finding IDs, verification target,
and granted actions. Helpers return evidence to this caller; commit grouping does not
start finishing, feedback assessment does not restart PR repair, and setup does not
start a second implementation loop. Preserve all unrelated staged and unstaged work.
Isolate unrelated migrations through a suitable workspace/project mechanism. If a
path-scoped stash is necessary, obtain authority for those exact paths, record the
stash identity, restore promptly, and verify original content as well as status.

Rebase/restack only when requested or required by the confirmed merge/conflict policy.
Do not rewrite history merely to repair a test or refresh an already acceptable PR.
Before a push, verify its exact destination and current expected remote SHA; a lease
limits overwrite risk but does not grant authority to rewrite remote history.

## Scope after history changes

After rebase, cherry-pick, or rebuild, compare against the PR's declared-base merge-base
(the immediate parent for a stack). Classify every changed file/material hunk:

| Diff item | Classification | Evidence | Disposition |
|---|---|---|---|
| Path / hunk | requested scope, required compatibility, or excluded | current request / contract / base diff | retain, authorized removal, follow-up, or blocked |

An older commit or stale test cannot expand the user's latest scope. Do not silently
delete excluded changes; obtain a concrete decision if they prevent the requested PR
scope. Re-review descendants whose parent or behavior changed.

## CI evidence

Record local HEAD, remote PR head, current base, check/run URL and attempt, event,
checkout revision, conclusion, and the head/base pair tested when available.
Local verification remains local evidence until its commit is published.

Distinguish a head build, a synthetic merge build, and a base-context/policy check.
A merge-check SHA can legitimately differ from the PR head: establish through the
run/event/checkout evidence that it contains the intended head and base. A different
SHA alone does not prove staleness. A policy check that never tested PR code does not
prove code correctness. Unknown provenance stays unknown; never infer it from green.

| Check | Relationship | Evidence | Owner / action |
|---|---|---|---|
| Name / run | direct root, downstream, infrastructure, policy, or unknown | log, dependency, tested revision | repair in scope, wait, or report blocker |

Classify pending, cancelled, skipped, neutral, and failed separately. Follow the actual
required-check policy; platform-accepted skipped/neutral is not evidence that tests ran.
Refresh stale evidence after the relevant head/base changes. Poll a known run with
bounded snapshots when a watcher yields no useful output; missing access or an unknown
required-check set must be reported, not treated as green.

## Repair contracts and browser checks

Before changing product behavior for a failing test, reconcile adjacent unit tests,
source/spec contracts, and current intended behavior. Repair a stale assertion when
the stronger current contract contradicts it; otherwise establish the product defect.
For repeated UI elements created by a test, verify the expected count change within
an isolated container and locate the new element by stable identity. Prove the final
locator is unique; replacing a positional locator with broad text is insufficient.
Use `/1-playwright-browser-testing` for browser verification. A runtime or service
preflight failure is a verification blocker, not a passed test or a product defect.

## Evidence return

Return the finding/scope/CI dispositions, tested revisions, final local and remote
SHAs, outstanding blockers, and restored dirty paths. Summaries/comments are optional
requested outputs; publishing them, merging, or cleanup are separate authorized actions.

## Source

GitHub's [workflow event reference](https://docs.github.com/en/actions/reference/workflows-and-actions/events-that-trigger-workflows#pull_request)
documents PR merge revisions and base-context events. Apply that distinction to the
actual workflow checkout and check/run evidence rather than assuming a fixed SHA rule.
