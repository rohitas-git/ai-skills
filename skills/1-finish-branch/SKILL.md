---
name: 1-finish-branch
description: >
  After implementation is complete and tests pass: present structured options to merge,
  open a PR, or cleanup the branch, then execute the choice. Triggers: finish branch,
  complete development, merge or PR options, /1-finish-branch. Use when: After
  implementation is complete and tests pass: present structured options to merge, open a
  PR, or. Hub: /0-implement.
disable-model-invocation: true
metadata:
  catalog:
    hub: 0-implement
    role: soft
    when:
      - "After implementation is complete and tests pass: present structured options to merge, open a PR, or"
    triggers:
      - "finish branch"
      - "complete development"
      - "merge"
      - "PR options"
      - "1-finish-branch"
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
| Commit message | `/1-git-commit-helper` |
| PR description | `/1-pr-summarizer` |

## Process

1. **Verify tests** — full suite must pass; stop if red.
2. Detect env (local-only, Graphite, gh, etc.).
3. Present options (merge local, open PR, keep branch, cleanup) with recommendation.
4. Execute choice; clean temporary worktrees if created via `/1-git-worktrees`.

## Progressive disclosure

| Load when | File |
|-----------|------|
| Full option matrix + commands | [references/full-guide.md](./references/full-guide.md) |

## Related

- Ship soft under `/0-implement` (after 1-tdd / 1-code-review green)
- Upstream: `archive/vendor/superpowers` (`finishing-a-development-branch`)
