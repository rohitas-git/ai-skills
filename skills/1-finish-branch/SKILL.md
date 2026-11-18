---
name: 1-finish-branch
description: >
  Present branch-outcome options after implementation is complete and the relevant tests pass:
  merge locally, open a PR, or keep the branch. Execute only the user’s chosen option.
  Not for: creating commits (1-atomic-git-commits), resolving conflicts (1-resolving-merge-conflicts),
  or merging a PR without permission. Hub: /0-git.
disable-model-invocation: true
metadata:
  catalog:
    hub: 0-git
    role: pipeline
    when:
      - "implementation is complete and relevant tests pass; choose a branch outcome"
    triggers:
      - "finish branch"
      - "complete development"
      - "prepare merge"
      - "PR options"
      - "1-finish-branch"
    not_when:
      - "group and create commits → 1-atomic-git-commits"
      - "resolve active merge or rebase conflict → 1-resolving-merge-conflicts"
      - "merge a remote PR without explicit permission → stop"
    prev: [1-atomic-git-commits]
    next: [1-pr-summarizer]
    cousins: [1-atomic-git-commits, 1-pr-summarizer, 1-resolving-merge-conflicts, 1-git-worktrees]
    requires_setup: false
---

# Finish branch

**Core:** verify tests → detect environment → present options → execute → cleanup.

## Boundary

| Need | Skill |
|------|--------|
| Post-green merge/PR/cleanup choices | **finish-branch** (this) |
| Evidence before “done” claims | `/2-verify-work` |
| Multi-axis review closer | `/1-code-review` |
| Atomic commit groups | `/1-atomic-git-commits` |
| PR description | `/1-pr-summarizer` |
| Verify workspace provenance and service ownership | `/1-git-worktrees` |

## Process

1. **Verify evidence** — inspect checks required by the repository for the exact tree being integrated. Run missing or invalidated checks; do not repeat unchanged verified work. A failing or unavailable required check blocks a ready/merge claim; preserve the branch and report it.
2. Detect the forge, actual base, registered worktrees, detached state, and workspace/service ownership carried from `/1-git-worktrees`.
3. Honor an already selected, authorized outcome. Otherwise offer merge locally, open a PR, or keep the branch; detached HEAD gets only PR-from-a-named-feature-branch or keep. Discard is never a menu item.
4. Execute only the user's chosen option; clean a temporary worktree only after a successful merge or an explicitly confirmed discard.

## Hard safety rules

- Required verification must cover the tree being integrated; earlier evidence is reusable only when that tree and relevant environment are unchanged.
- Confirm the actual base branch before a merge. A merge into `main` or `master` still requires explicit user permission.
- Do not offer or perform discard unless the user expressly asks; require the exact word `discard` before deleting anything.
- Preserve a worktree for PR creation and “keep” choices. Never force-remove a worktree with uncommitted or untracked files.
- A path under `.worktrees/` or `worktrees/` does not prove ownership. Require creation/ownership evidence and a scoped cleanup decision; preserve host-managed workspaces and shared services.

## Progressive disclosure

| Load when | File |
|-----------|------|
| Full option matrix + commands | [references/full-guide.md](./references/full-guide.md) |

## Related

- Git pipeline under `/0-git`; Ship cross-link after 1-tdd / 1-code-review green
- Upstream: `archive/vendor/superpowers` (`finishing-a-development-branch`)
- Additional safety adaptation: [great_cto source](./references/great-cto-source.md)

## Conditional methods

Load only for the requested phase, within this skill’s authority: [Verified delivery and scoped cleanup](./references/verified-delivery.md).
