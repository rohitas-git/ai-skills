---
name: 1-pr-repair
description: >
  Repair, rebase, push, and verify one pull request from known findings and technical blockers without performing a fresh code review.
  Use when: apply existing PR findings, fix a PR's CI failures, or clear conflicts and merge blockers on one PR.
  Not for: discovering new review findings (1-pr-review-and-repair), repairing a dependent PR stack (1-stacked-pr-repair),
  or merging an approved PR (1-finish-branch). Hub: /0-git.
disable-model-invocation: true
metadata:
  catalog:
    hub: 0-git
    role: pipeline
    when:
      - "repair known findings, CI failures, conflicts, or blockers on one PR"
      - "make an existing PR green without a fresh review pass"
    not_when:
      - "discover new findings → 1-pr-review-and-repair"
      - "repair dependent stack → 1-stacked-pr-repair"
      - "merge PR → 1-finish-branch"
    next: [1-pr-summarizer]
    cousins: [1-pr-review-and-repair, 1-stacked-pr-repair, 1-git-worktrees, 1-atomic-git-commits, 1-resolving-merge-conflicts, 1-ci-cd-and-automation]
    triggers: [repair PR, fix PR without review, resolve PR findings, fix PR CI]
    requires_setup: false
---

# PR Repair

Converge known findings and technical blockers on one PR. Do not initiate a code review.

## Boundary

| Need | Skill |
|------|-------|
| Repair known findings, conflicts, CI failures, or blockers on one PR | **this skill** |
| Discover and repair new findings on one PR | `/1-pr-review-and-repair` |
| Repair known findings across a dependent stack | `/1-stacked-pr-repair` |
| Validate and apply review feedback | `/1-receive-review` |
| Group fixes into commits | `/1-atomic-git-commits` |
| Resolve rebase conflicts | `/1-resolving-merge-conflicts` |
| Diagnose CI automation | `/1-ci-cd-and-automation` |

Repair inputs are existing review findings, user-provided findings, failing required CI, conflicts, and provider-reported merge blockers. Do not run `/1-code-review`, invent findings, or broaden into unrelated cleanup.

## PR scope guard

The repair queue is bounded by the confirmed PR's declared base merge-base, changed behavior, and known inputs. Repair only a defect introduced by the PR, a regression exposed by its change, or the smallest directly required compatibility/test/conflict adjustment. Pre-existing defects, adjacent cleanup, unrelated CI debt, and newly noticed improvements are follow-ups, not repair work in this PR.

## Dirty-worktree isolation

Before schema-sensitive checks, inspect the full worktree status. An unrelated untracked
migration can alter migration inventory or push-hook results even when it is outside the
PR. Preserve it exactly:

- Prefer a project-native isolation mechanism when one exists.
- Otherwise ask before changing Git state, then isolate only the exact named path with a
  reversible path-scoped stash. Never use a broad stash for this purpose.
- Record the pre-check status, restore the path immediately after the sensitive check,
  and verify that the final status contains the same unrelated file. Never add, edit,
  delete, or commit it as part of the repair.

## Process

Load the [shared PR repair checkpoints](../0-git/references/pr-repair-checkpoints.md) before the loop; apply them at workspace, history, contract, CI, and evidence-return steps. Specialist handoffs return here without restarting a sibling pipeline.

1. **Identify the PR.** Resolve one PR from user input or the current branch. Record its number, head/base branches, head/base SHAs, known repair inputs, required checks, and merge blockers. Keep a PR-state record throughout the run: local `HEAD`, remote head SHA, current base SHA, and the SHA evaluated by each required check. Local verification is not remote CI evidence; associate each check with its tested head/base or policy context through the shared checkpoints. Use **F-G4** if it is not unique.
2. **Confirm scope and authority.** Require permission to commit and push if not already granted. Use `/1-git-worktrees` when isolation is needed. Never overwrite unrelated changes or operate on `main`, `master`, protected, or unrelated branches.
3. **Refresh and rebase.** Fetch before mutation. Rebase onto the latest declared base only when requested or required by the confirmed conflict/merge policy; otherwise retain history. Resolve conflicts through `/1-resolving-merge-conflicts`, preserve intent, and add resulting breakage to the repair queue.
4. **Reconstruct scope after history changes.** After any rebase, cherry-pick, or history rebuild—and before the first push—compare the current PR diff with its confirmed merge-base. Build a scope ledger that classifies every changed file or material hunk:

   | Diff item | Classification | Evidence | Disposition |
   |---|---|---|---|
   | Path / hunk | requested scope, directly required compatibility, or excluded scope | request/PR intent/base diff/contract | retain, seek removal authority, or report follow-up |

   Re-read the user's latest scope correction and the PR purpose; an older commit or test does not expand scope. An excluded item is never silently deleted or rewritten: report it, seek explicit authority for a removal, or leave it untouched and stop before pushing if the PR would remain out of scope.
5. **Triage CI before editing.** Build a disposition table for every failing or blocked check:

   | Check | Relationship | Evidence | Owner / action |
   |---|---|---|---|
   | Name | direct root failure, downstream consequence, infrastructure, policy, or unknown | failing job/log/dependency evidence | repair, wait, escalate, or report |

   Do not count a downstream failure as another root cause. Update the table when new
   evidence changes the dependency relationship.
6. **Reconcile findings and contracts.** Verify each input against current code. Mark it obsolete, already fixed, actionable in scope, out-of-scope follow-up, or blocked by human judgment. Before changing product behavior to satisfy a test—especially UI copy, visibility, or DOM structure—search adjacent unit tests, source contracts, specifications, and current behavior. If a stale test contradicts the stronger current contract, repair the stale expectation rather than regress the product. Cite the exact evidence; never close an item by assumption.
7. **Repair and verify.** Use `/1-receive-review` for feedback and `/1-ci-cd-and-automation` for pipeline failures. Fix root causes, run the smallest relevant lint, typecheck, tests, and build, then use `/1-atomic-git-commits` for independently revertible Conventional Commits. When repairing a browser test for a newly created repeated element, assert the exact count before and after creation and target the new element through a stable test attribute or an identity derived from pre-action state. Do not use a positional selector or an unconstrained text matcher that can match multiple elements.
8. **Push safely.** Push fast-forward changes normally. After history rewrites, verify the expected remote SHA and use `git push --force-with-lease=refs/heads/<branch>:<expected-sha> <remote> <branch>:<branch>`. Never use bare `--force`, bypass hooks, or weaken branch protection.
9. **Check CI and blockers.** Wait for all required checks to finish. Establish whether each check tested the intended head, a merge containing that head and base, or policy only; label stale and unknown evidence accurately. Repair attributable failures and refresh provider mergeability. Prefer bounded status snapshots when a watcher produces no useful incremental output. Report infrastructure, permission, approval, or policy failures; never invent a pass or bypass a gate.
10. **Converge, bounded.** Repeat repair through CI for at most three passes. Stop early when the known repair queue is empty, required CI passes, and no technical merge blocker remains. After pass three, report unresolved items.
11. **Final sweep.** Verify the remote SHA, base relationship, evidence-backed disposition of every repair input, scope ledger, CI disposition table, required CI, restored dirty-worktree state, and mergeability without merging.

## Completion report

Report the PR and final SHA, passes used, scope ledger, CI disposition table, known findings
fixed/obsolete/out-of-scope/blocked, contracts reconciled, commits, push mode, rebase
result, required CI, merge blockers, restored unrelated paths, and remaining blockers.
State that no fresh code review was performed and the PR was not merged.

## Hard stops

- No concrete repair input exists; route review discovery to `/1-pr-review-and-repair`.
- The PR or writable head branch is not uniquely identified.
- A protected/default or unrelated branch would be rewritten.
- The remote SHA changes unexpectedly before a history rewrite.
- Required CI cannot be associated with the intended published head/base or its actual policy context.
- An excluded-scope item remains in the diff and the user has not authorized its removal or retention.
- A proposed repair is not caused by or strictly required for the PR's change boundary.
- Three passes leave known findings, failing CI, or technical merge blockers.

## Related

Optional read-only `scripts/watch-pr/watch-pr`: [usage and limits](../../guidelines/catalog/pstack-tooling.md#pr-status).
The shared checkpoints expose it to the other PR workflows without duplicating its policy.

Parent: `/0-git`. Review-first sibling: `/1-pr-review-and-repair`. Optional next: `/1-pr-summarizer`.
