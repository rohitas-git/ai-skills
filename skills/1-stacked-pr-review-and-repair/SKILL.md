---
name: 1-stacked-pr-review-and-repair
description: >
  Review, repair, rebase, and verify every pull request in a dependent stack from base to tip.
  Use when: harden a stacked PR chain, repeatedly review and fix every PR, or make an entire PR stack green.
  Not for: repairing a stack without fresh review (1-stacked-pr-repair), reviewing and repairing one PR only (1-pr-review-and-repair),
  or merging approved PRs (1-finish-branch). Hub: /0-git.
disable-model-invocation: true
metadata:
  catalog:
    hub: 0-git
    role: pipeline
    when:
      - "review and repair every PR in a dependent stack"
      - "rebase, restack, and make a PR stack green"
    not_when:
      - "repair stack without fresh review → 1-stacked-pr-repair"
      - "review and repair one PR only → 1-pr-review-and-repair"
      - "commit ordinary local changes → 1-atomic-git-commits"
      - "merge PRs → 1-finish-branch"
    next: [1-pr-summarizer]
    cousins: [1-stacked-pr-repair, 1-pr-review-and-repair, 1-git-worktrees, 1-code-review, 1-atomic-git-commits, 1-resolving-merge-conflicts, 1-ci-cd-and-automation]
    triggers: [review PR stack, fresh review of PR stack, review stack until green, restack PRs]
    requires_setup: false
---

# Stacked PR Review and Repair

Converge a dependent PR stack from base to tip. Delegate specialist work; keep one stack-wide ledger of evidence.

## Boundary

| Need | Skill |
|------|-------|
| Converge every PR in a dependent stack | **this skill** |
| Repair known stack findings without fresh review | `/1-stacked-pr-repair` |
| Converge one PR only | `/1-pr-review-and-repair` |
| Isolate branch work from a dirty workspace | `/1-git-worktrees` |
| Review one fixed diff | `/1-code-review` |
| Validate and apply findings | `/1-receive-review` |
| Group fixes into commits | `/1-atomic-git-commits` |
| Resolve an active rebase conflict | `/1-resolving-merge-conflicts` |
| Diagnose CI automation | `/1-ci-cd-and-automation` |
| Merge, retain, or clean a completed branch | `/1-finish-branch` |

This skill may update and push named stack branches. It never merges PRs or broadens authority beyond the confirmed stack.

## Stack scope guard

The confirmed stack is the outer boundary; each PR's immediate-parent merge-base, changed behavior, and stated purpose is its inner boundary. Review each PR only in that inner boundary. Place a repair in an earlier stack PR only when that PR introduced the defect and the move is necessary to preserve stack correctness. Do not sweep pre-existing issues, adjacent cleanup, unrelated CI debt, or improvements outside the named stack into this work; record them as follow-ups.

## Process

Load the [shared PR repair checkpoints](../0-git/references/pr-repair-checkpoints.md) before the loop; apply them at workspace, history, contract, CI, and evidence-return steps. Specialist handoffs return here without restarting a sibling pipeline.

1. **Discover the stack.** Use the repository's configured stack tool or PR-provider metadata. Record each PR, head branch, immediate base, head SHA, and required checks. Order the dependency graph base-to-tip. At ambiguity use **F-G3**; reject cycles.
2. **Confirm scope and authority.** Name the exact PRs and branches. Require permission to commit and push if the request did not already grant it. Use `/1-git-worktrees` when isolation is needed; never overwrite unrelated local changes. Never operate on `main`, `master`, protected, or unrelated branches.
3. **Refresh state.** Fetch immediately before work. Re-check remote SHAs before every rebase and push; stop if an unexpected actor changed a branch.
4. **Plan each history rewrite.** Before an interactive rebase or restack, record a dependency map: branch, immediate parent, current/target SHA, and base-to-tip order. For commits whose treatment is not the default **KEEP**, create a disposition row: `REWORD`, `DROP`, `SQUASH`, or `EMPTY` → exact SHA(s), evidence, rationale, expected outcome, and user authority. `KEEP` is the default. Never reword, drop, squash, or skip an empty commit merely for neatness; obtain explicit authorization for each history-altering disposition.
5. **Process one PR.** Restack onto its updated immediate parent when required; retain history already satisfying the confirmed base policy. Resolve conflicts through `/1-resolving-merge-conflicts`, preserving both intents and rerunning affected checks. If actual state differs from the plan, stop, inspect `git status`, the graph/log, and reflog, then ask before any recovery that discards work.
6. **Review the correct diff.** Run `/1-code-review` against the PR's immediate parent merge-base, not automatically against the default branch. Keep findings inside that PR's inner boundary.
7. **Classify every finding.** Check the entire stack, then mark it unsupported, already fixed here, fixed in another stack PR, actionable here, out-of-scope follow-up, or blocked by a human decision. Cite code or a specific PR and commit; never defer on assumption.
8. **Place fixes at the earliest valid layer.** A descendant fix normally moves or is reproduced in the earliest PR that introduces the defect. Defer only when the affected behavior genuinely begins in the descendant. After moving a fix downward, restack every descendant.
9. **Repair and verify.** Use `/1-receive-review` for actionable findings. Run the smallest relevant lint, typecheck, tests, and build. Use `/1-atomic-git-commits` for independently revertible Conventional Commits.
10. **Push safely.** Push fast-forward changes normally. After history rewrites, verify the expected remote SHA and use `git push --force-with-lease=refs/heads/<branch>:<expected-sha> <remote> <branch>:<branch>`. Never use bare `--force`, bypass hooks, or weaken branch protection.
11. **Check CI.** Wait for every required check to reach a terminal state. Fix failures attributable to the PR, then repeat review. Report infrastructure or permission failures as blockers; do not invent a pass.
12. **Converge, bounded.** Run at most three full review/repair passes per PR. Stop early when no actionable findings remain, every downstream deferral is evidenced and legitimate, CI passes, and no technical merge blocker remains. After pass three, stop and report unresolved items.
13. **Advance base-to-tip.** Any changed parent invalidates descendant bases: rebase, safely force-sync, retest, and re-review each materially changed descendant before moving on. After each rebase, show a short `git log --oneline --graph` anchored at the expected parent; do not run garbage collection or delete tags as routine cleanup.
14. **Sweep the stack.** Refresh provider state once more and verify every PR is based on the latest parent SHA, conflict-free, review-clean under the rules above, and green.

## Completion report

For each PR report: final SHA, passes used, findings fixed/deferred/out-of-scope/rejected, commits created, push mode, rebase result, and required CI states. Then list unresolved blockers and explicitly state that no PR was merged.

## Fork

| Fork | When | Question | Recommended | Branches |
|------|------|----------|-------------|----------|
| **F-G3** | provider metadata does not establish one stack order | What is the intended base-to-tip PR order? | derive parent-child edges, then stop if still ambiguous | user-supplied order · provider/stack-tool order · **Agent judgment** |

## Hard stops

- A protected/default branch would be rewritten.
- The remote SHA changed unexpectedly before a history rewrite.
- Stack topology is cyclic or remains ambiguous after F-G3.
- A finding, conflict, or required CI failure needs product or policy judgment.
- A proposed repair is outside the confirmed stack or not required by the affected PR's change boundary.
- Three passes leave actionable findings or failing required CI.

## Related

Parent: `/0-git`. Optional next: `/1-pr-summarizer`. Merging remains an explicit `/1-finish-branch` decision. Adapted safety-compatible guidance: [vendor source](../../archive/vendor/ai-agent-rules/VENDOR-SOURCE.md).
