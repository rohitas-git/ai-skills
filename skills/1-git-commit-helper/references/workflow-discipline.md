# Git workflow discipline (harvested)

Source: archive vendor `git-workflow-and-versioning` — day-to-day VCS only.  
**Winners:** this skill (messages), `/1-resolving-merge-conflicts`, `/0-implement` (commit after slice). Versioning/changelog → [`shipping-and-launch/references/versioning-changelog.md`](../../1-shipping-and-launch/references/versioning-changelog.md). Do not peer-promote full git-workflow skill.

## Trunk-based default

- Keep `main` deployable.
- Short-lived feature branches (merge in ~1–3 days).
- Prefer feature flags over long-lived branches.
- Delete branches after merge.

## Save-point loop

```text
Implement slice → test/verify → commit → next slice
```

Not: 0-implement everything → one giant commit.  
If the agent goes off rails: reset to last green commit and re-slice.

## Atomic commits

One logical change per commit. Separate:

- feature vs refactor vs formatting
- behavior change vs drive-by cleanup (cleanup can be tiny in-feature at reviewer discretion)

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

Prefer isolated worktrees or separate branches so agents do not thrash the same checkout. Clean up worktrees after merge.

## Red flags

- Huge uncommitted piles
- Messages like “fix” / “update” / “misc”
- Formatting mixed with behavior
- Force-push to shared main
- Secrets or build artifacts committed
