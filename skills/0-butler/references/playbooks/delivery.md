# PRs and delivery

Use the selected section within the [playbook handoff and tool contract](../playbooks.md#handoff-and-tool-selection).

## babysit

1. Pin the PR and declare check, threads-only or drive using the [mode contract](../../../0-git/references/babysit-modes.md). Use an available authorized forge connector for status, or the existing [GitHub watcher](../../../1-pr-repair/scripts/watch-pr/watch-pr) when its GitHub and CLI prerequisites are met.
2. Apply *Fix Root Causes* by testing review claims against current code and the accepted contract. For authorized fixes select [PR Repair](../../../1-pr-repair/SKILL.md) or [Stacked PR Repair](../../../1-stacked-pr-repair/SKILL.md) for known blockers. Requests for fresh review and repair use the corresponding combined owner.
3. Return head, base, check and thread state, and any permitted work completed. A watcher observation supports status reporting. Merge policy and current-head proof remain separate checks.

## opening-a-pr

1. Use [Finish Branch](../../../1-finish-branch/SKILL.md) to pin publish target, head, base and check receipts. Apply *Prove It Works* by matching evidence to the actual candidate and reporting gaps.
2. Use [PR Summarizer](../../../1-pr-summarizer/SKILL.md) for the description. Open only when publishing is in scope, using the available authorized forge write tool or the repository's configured CLI.
3. Read back the PR, expected base and head. A prose-only request ends with the draft, and publication state belongs in the final report.

## shipping

1. Pin the requested delivery operation and prerequisites. Use [Verified Delivery](../../../1-finish-branch/references/verified-delivery.md) for branch or stack disposition and [Shipping and Launch](../../../1-shipping-and-launch/SKILL.md) for release rollout.
2. Apply [Sequence Work into Verifiable Units](../../../0-implement/references/rerunnable-changes.md) by finding the contiguous verified stack prefix. Recheck evidence invalidated by head, base or environment changes. Use [Verify Work](../../../2-verify-work/SKILL.md) for the affected claims.
3. Use the authorized forge operation only after its approval and required checks hold. Read back the provider state with the supported connector or watcher. Report queued, merged and deferred items distinctly.

## worktree-cleanup

1. Use [Git Worktrees](../../../1-git-worktrees/SKILL.md) and the [local audit](../../../1-git-worktrees/scripts/worktree-audit.py) to identify candidates. Apply [Separate Before Serializing Shared State](../../../1-parallel-agents/references/coverage-and-races.md) by preserving ownership and checking whether a worktree or service is still in use.
2. Use [Finish Branch](../../../1-finish-branch/SKILL.md) to reconcile exact paths, branch disposition, dirty and untracked files and any evidence that must survive. Local ancestry only establishes local Git relationships.
3. With exact removal authority, recheck candidates immediately before cleanup. Return the paths removed and retained, with blockers for anything unproven.
