# Git workflow discipline (harvested)

Source: archive vendor `git-workflow-and-versioning` — day-to-day VCS only.  
**Winners:** this skill (messages), `/1-resolving-merge-conflicts`, `/0-implement` (commit after slice). Versioning/changelog → [`shipping-and-launch/references/versioning-changelog.md`](../../1-shipping-and-launch/references/versioning-changelog.md). Do not peer-promote full git-workflow skill.

## Trunk-based default

- Keep `main` deployable.
- Short-lived feature branches (merge in ~1–3 days).
- Prefer feature flags over long-lived branches.
- Branch/worktree cleanup follows `/1-finish-branch` only when selected and ownership is established.

## Save-point loop

```text
Implement slice → test/verify → commit → next slice
```

Not: 0-implement everything → one giant commit.  
If an increment fails, preserve the working changes and diagnose the difference from
the last verified commit. A save point does not authorize resetting or discarding work.

## Atomic commits

One logical change per commit. Apply the live skill's
[atomic grouping guide](./atomic-grouping.md), including its purpose/revert/verification tests
and mandatory split review for size pressure. Separate:

- feature vs refactor vs formatting
- behavior change vs drive-by cleanup (cleanup can be tiny in-feature at reviewer discretion)

Line and file counts are signals, not the definition. Default large proposed groups to a split;
retain one only with a concrete inseparability reason and coherent verification.

## Change summary (after multi-file work)

```text
CHANGES MADE:
- path: what

THINGS I DIDN'T TOUCH (intentionally):
- path: why out of scope

POTENTIAL CONCERNS:
- …
```

Surfaces scope discipline for reviewers and humans.

## Pre-commit hygiene

1. `git diff --staged` (know what you ship)
2. No secrets in the diff
3. Project tests / lint / typecheck as expected
4. `.gitignore` covers `node_modules/`, build output, `.env*`, keys

## Branch naming (common)

`feature/…` · `fix/…` · `chore/…` · `refactor/…`

## Parallel agents

Use `/1-git-worktrees` to establish separate checkouts for concurrent writers; different
branch names alone do not isolate a shared working directory or index. Return to the
caller after committing. Cleanup follows the owner's explicit lifecycle decision.

## Red flags

- Huge uncommitted piles
- Messages like “fix” / “update” / “misc”
- Formatting mixed with behavior
- Force-push to shared main
- Secrets or build artifacts committed
