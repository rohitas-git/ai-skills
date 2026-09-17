---
name: 1-stacked-pr-repair
description: >
  Repair, rebase, push, and verify every pull request in a dependent stack without performing a fresh code review.
  Use when: apply existing PR findings across a stack, fix stack CI failures, or clear conflicts and merge blockers base-to-tip.
  Not for: discovering new review findings (1-stacked-pr-review-and-repair), repairing one PR (1-pr-repair),
  or merging approved PRs (1-finish-branch). Hub: /0-git.
disable-model-invocation: true
metadata:
  catalog:
    hub: 0-git
    role: pipeline
    when:
      - "repair an existing queue of findings and blockers across a dependent PR stack"
      - "rebase, restack, fix CI, and make a PR stack green without reviewing it"
    not_when:
      - "discover new findings → 1-stacked-pr-review-and-repair"
      - "repair one PR → 1-pr-repair"
      - "merge PRs → 1-finish-branch"
    next: [1-pr-summarizer]
    cousins: [1-stacked-pr-review-and-repair, 1-pr-repair, 1-pr-review-and-repair, 1-git-worktrees, 1-atomic-git-commits, 1-resolving-merge-conflicts, 1-ci-cd-and-automation]
    triggers: [repair PR stack, fix stacked PRs without review, resolve stack findings, make existing PR stack green]
    requires_setup: false
---

# Stacked PR Repair

Converge known findings and technical blockers across a dependent PR stack from base to tip. Do not initiate a code review.

## Boundary

| Need | Skill |
|------|-------|
| Repair known findings, conflicts, or CI failures across a stack | **this skill** |
| Discover and repair new findings across a stack | `/1-stacked-pr-review-and-repair` |
| Repair known findings on one PR without fresh review | `/1-pr-repair` |
| Validate and apply existing review feedback | `/1-receive-review` |
| Group fixes into commits | `/1-atomic-git-commits` |
| Resolve rebase conflicts | `/1-resolving-merge-conflicts` |
| Diagnose CI automation | `/1-ci-cd-and-automation` |

Repair inputs are existing review findings, user-provided findings, failing required CI, conflicts, and provider-reported merge blockers. Do not run `/1-code-review`, invent findings, or broaden into unrelated cleanup.

## Stack scope guard

The confirmed stack is the outer boundary; each PR's immediate-parent merge-base, changed behavior, and repair inputs are its inner boundary. Repair only defects introduced or exposed by that PR, or the smallest required compatibility/test/conflict adjustment. Move work to an earlier stack PR only when it introduced the defect and that move is necessary for stack correctness. Record pre-existing issues, adjacent cleanup, unrelated CI debt, and improvements outside the named stack as follow-ups.

## Process

Load the [shared PR repair checkpoints](../0-git/references/pr-repair-checkpoints.md) before the loop; apply them at workspace, history, contract, CI, and evidence-return steps. Specialist handoffs return here without restarting a sibling pipeline.

1. **Discover the stack.** Use the configured stack tool or PR-provider metadata. Record each PR, head branch, immediate base, head SHA, open known findings, required checks, and merge blockers. Order base-to-tip; use **F-G3** if ambiguous and reject cycles.
2. **Confirm scope and authority.** Name the exact PRs, branches, and repair inputs. Require permission to commit and push if not already granted. Use `/1-git-worktrees` when isolation is needed. Never overwrite unrelated changes or operate on `main`, `master`, protected, or unrelated branches.
3. **Refresh state.** Fetch before work. Re-check remote SHAs before every rebase and push; stop when an unexpected actor changes a branch.
4. **Plan each history rewrite.** Before an interactive rebase or restack, record a dependency map: branch, immediate parent, current/target SHA, and base-to-tip order. For commits whose treatment is not the default **KEEP**, create a disposition row: `REWORD`, `DROP`, `SQUASH`, or `EMPTY` → exact SHA(s), evidence, rationale, expected outcome, and user authority. `KEEP` is the default. Never reword, drop, squash, or skip an empty commit merely for neatness; obtain explicit authorization for each history-altering disposition.
5. **Process base-to-tip.** Restack onto the updated immediate parent when needed; avoid rewriting a branch already satisfying the confirmed base policy. Resolve conflicts through `/1-resolving-merge-conflicts`, preserve both intents, and add resulting breakage to the repair queue. If the actual state differs from the recorded plan, stop, inspect `git status`, the graph/log, and reflog, then ask before any recovery that discards work.
6. **Reconcile known findings.** Verify each input against current code. Mark it obsolete, already fixed, fixed in another stack PR, actionable here, out-of-scope follow-up, or blocked by human judgment. Cite the exact code, PR, commit, check, or conflict; never close an item by assumption.
7. **Place fixes at the earliest valid layer.** Move or reproduce a fix in the earliest PR that introduces the problem. Defer only when the affected behavior begins in a descendant. Restack every descendant after changing a parent.
8. **Repair and verify.** Use `/1-receive-review` for review feedback and `/1-ci-cd-and-automation` for pipeline failures. Fix root causes, run the smallest relevant lint, typecheck, tests, and build, then use `/1-atomic-git-commits` for independently revertible Conventional Commits.
9. **Push safely.** Push fast-forward changes normally. After history rewrites, verify the expected remote SHA and use `git push --force-with-lease=refs/heads/<branch>:<expected-sha> <remote> <branch>:<branch>`. Never use bare `--force`, bypass hooks, or weaken branch protection.
10. **Check CI and blockers.** Wait for all required checks to finish. Repair attributable failures and refresh provider mergeability. Report infrastructure, permission, approval, or policy failures; never invent a pass or bypass a gate.
11. **Converge, bounded.** Repeat repair through CI for at most three passes per PR. Stop early when its known repair queue is empty, required CI passes, and no technical merge blocker remains. After pass three, report unresolved items.
12. **Sweep the stack.** Verify every PR uses the latest parent SHA, all known findings have evidence-backed dispositions, required CI is green, and no technical merge blocker remains. Reprocess materially changed descendants. After each rebased branch, show a short `git log --oneline --graph` anchored at its expected parent; do not run garbage collection or delete tags as routine cleanup.

## Completion report

For each PR report: final SHA, passes used, known findings fixed/deferred/obsolete/out-of-scope/blocked, commits, push mode, rebase result, required CI, and merge blockers. State that no fresh code review was performed and no PR was merged.

## Hard stops

- No concrete repair input exists; route review discovery to `/1-stacked-pr-review-and-repair`.
- A protected/default branch would be rewritten.
- The remote SHA changes unexpectedly before a history rewrite.
- Stack topology remains ambiguous after F-G3 or is cyclic.
- A proposed repair is outside the confirmed stack or not required by the affected PR's change boundary.
- Three passes leave known findings, failing CI, or technical merge blockers.

## Related

Parent: `/0-git`. Review-first sibling: `/1-stacked-pr-review-and-repair`. Optional next: `/1-pr-summarizer`. Adapted safety-compatible guidance: [vendor source](../../archive/vendor/ai-agent-rules/VENDOR-SOURCE.md).
