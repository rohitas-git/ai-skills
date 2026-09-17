---
name: 1-pr-review-and-repair
description: >
  Review one pull request, fix each in-scope finding one at a time, and repeat scoped review until none remain.
  Use when: fix all findings on a PR, repeatedly review and repair one PR, or make one PR merge-ready.
  Not for: repair-only work from known findings (1-pr-repair), review-only feedback (1-code-review), dependent PR stacks (1-stacked-pr-review-and-repair),
  or merging an approved PR (1-finish-branch). Hub: /0-git.
disable-model-invocation: true
metadata:
  catalog:
    hub: 0-git
    role: pipeline
    when:
      - "review one PR, repair each in-scope finding, and repeat until clean and green"
      - "rebase, fix, push, and verify one PR"
    not_when:
      - "repair known findings without fresh review → 1-pr-repair"
      - "review without modifying → 1-code-review"
      - "dependent PR stack → 1-stacked-pr-review-and-repair"
      - "merge a PR → 1-finish-branch"
    next: [1-pr-summarizer]
    cousins: [1-pr-repair, 1-stacked-pr-review-and-repair, 1-code-review, 1-git-worktrees, 1-atomic-git-commits, 1-resolving-merge-conflicts, 1-ci-cd-and-automation]
    triggers: [review and fix PR, fix PR findings one by one, fresh PR review and repair, review PR until green, make PR merge-ready]
    requires_setup: false
---

# PR Review and Repair

Converge one PR against its declared base: review, repair each actionable in-scope
finding, then review the updated PR again. Retain evidence for every disposition.

## Boundary

| Need | Skill |
|------|-------|
| Converge one PR through review, repair, rebase, and CI | **this skill** |
| Repair known findings without fresh review | `/1-pr-repair` |
| Review without changing the branch | `/1-code-review` |
| Converge a dependent PR stack | `/1-stacked-pr-review-and-repair` |
| Apply validated findings | `/1-receive-review` |
| Create atomic commits | `/1-atomic-git-commits` |
| Resolve rebase conflicts | `/1-resolving-merge-conflicts` |
| Diagnose CI automation | `/1-ci-cd-and-automation` |

This skill may update and push the confirmed PR branch. It never merges the PR or broadens authority to another branch.

## PR scope guard

The review boundary is the PR's declared base merge-base, its changed behavior, and its stated purpose. Inspect surrounding code only to understand those changes. Repair only a defect introduced by the PR, a regression exposed by its change, or the smallest directly required compatibility/test/conflict adjustment. Do not fix pre-existing issues, adjacent cleanup, unrelated CI debt, or newly noticed improvements; record them as follow-ups with evidence instead.

Every proposed change needs a direct entry in the finding ledger. A useful change is not
enough: if it cannot be tied to a specific PR finding and the PR's changed behavior, do
not make it. Never turn a review cycle into a refactor, feature expansion, broad test
cleanup, or opportunistic hardening pass.

## Process

Load the [shared PR repair checkpoints](../0-git/references/pr-repair-checkpoints.md) before the loop; apply them at workspace, history, contract, CI, and evidence-return steps. Specialist handoffs return here without restarting a sibling pipeline.

1. **Identify the PR.** Resolve one PR from the user's input or the current branch. Record its number, head branch, base branch, head/base SHAs, required checks, and merge status. Use **F-G4** if the target is not unique.
2. **Confirm authority and isolate.** Require permission to commit and push if the request did not grant it. Use `/1-git-worktrees` when the current workspace is dirty or belongs to other work. Never overwrite unrelated changes or operate directly on `main`, `master`, or a protected branch.
3. **Refresh and rebase.** Fetch immediately before mutation. Rebase onto the latest declared base only when requested or required by conflict/merge policy. Resolve conflicts through `/1-resolving-merge-conflicts` and rerun affected checks.
4. **Review the current PR diff.** Run `/1-code-review` against the PR's declared base merge-base. Include existing review comments when available, but verify each against current code before acting. Record every candidate in a finding ledger: finding, evidence, scope decision, repair, verification, and disposition. Keep findings inside the PR scope guard.
5. **Classify the ledger.** Mark each candidate unsupported, already fixed by a current PR commit, actionable in scope, out-of-scope follow-up, or blocked by human judgment. Cite code and commit evidence; never close a finding by assumption. Out-of-scope items are reported, never repaired in this PR.
6. **Repair findings one at a time.** For the next actionable in-scope finding, use `/1-receive-review`, fix its root cause with the smallest change, and run the focused verification that proves that finding resolved. Update its ledger row before taking the next finding. Use `/1-atomic-git-commits` for independently revertible Conventional Commits; do not combine unrelated findings merely to reduce commit count.
7. **Push safely.** Push fast-forward changes normally. After a rebase, re-check the remote SHA and use `git push --force-with-lease=refs/heads/<branch>:<expected-sha> <remote> <branch>:<branch>`. Never use bare `--force`, bypass hooks, or weaken branch protection.
8. **Check CI.** Wait for every required check to reach a terminal state. Diagnose and fix failures attributable to the PR; report infrastructure or permission failures as blockers. Never invent a pass.
9. **Repeat the scoped loop.** After all actionable ledger items are repaired and CI reaches a terminal state, review the updated PR diff again. Repeat steps 4–8 until the fresh review yields no actionable **in-scope** findings, required CI passes, the branch satisfies the confirmed base/update policy, and no technical merge blocker remains. Stop and report rather than expanding scope when a remaining item is out of scope or needs human judgment.
10. **Final sweep.** Refresh provider state and verify the final remote SHA, base relationship, review dispositions, required checks, and mergeability without merging.

## Completion report

Report the PR and final SHA, review cycles used, finding ledger dispositions
(fixed/rejected/out-of-scope/blocked), commits created, push mode, rebase result,
required CI states, and remaining blockers. Explicitly state that the PR was not merged
and that no out-of-scope changes were made.

## Fork

| Fork | When | Question | Recommended | Branches |
|------|------|----------|-------------|----------|
| **F-G4** | no unique PR is identified | Which PR should be reviewed and repaired? | the current branch's single open PR, when unique | user-named PR · unique current-branch PR · **Agent judgment** |

## Hard stops

- The PR or writable head branch is not uniquely identified.
- A protected/default or unrelated branch would be rewritten.
- The remote SHA changes unexpectedly before a history rewrite.
- A finding, conflict, or required CI failure needs product or policy judgment.
- The proposed repair is not caused by or strictly required for the PR's change boundary.
- An in-scope finding cannot be resolved without a product, policy, or scope decision.

## Related

Parent: `/0-git`. Optional next: `/1-pr-summarizer`. Merging remains an explicit `/1-finish-branch` decision.
