# Trigger Enforcement Reference

This document explains the exact mechanics of documentation trigger checking, generalized from production implementation.

## Glob Matching Logic

A path pattern supports `**` (any directories) and `*` (any characters within a segment).

Example implementation (JavaScript-style, adaptable to other languages):

```js
function matchGlob(pattern, filePath) {
  const normalizedPattern = pattern.replace(/\\/g, "/");
  const normalizedFile = filePath.replace(/\\/g, "/");
  const regexSource = normalizedPattern
    .split("**")
    .map((segment) =>
      segment
        .split("*")
        .map((part) => part.replace(/[.+^${}()|[\]\\]/g, "\\$&"))
        .join("[^/]*"),
    )
    .join(".*");
  return new RegExp(`^${regexSource}$`).test(normalizedFile);
}
```

- `src/auth/**` matches `src/auth/middleware.js`, `src/auth/providers/*.js`, etc.
- `src/middlewares/auth.js` matches only that exact file.
- Renames are handled by including both source and destination paths.

## Change Detection

- **Base comparison**: `git diff --name-status --find-renames baseRef...HEAD`
- **Local development**: Also include working tree (`git diff HEAD`), staged (`git diff --cached`), and untracked files so a documentation fix can satisfy the check before commit.
- **CI**: Usually commit-range only (respect `GITHUB_BASE_REF`).
- Override base with `DOCS_CHECK_BASE` env var.

## Validation Rules (Fail Fast)

Before checking changes, the map itself is validated:

- Must be valid JSON object with `rules` array.
- Every rule must have:
  - Non-empty string `id` (unique across map)
  - Non-empty `paths` array of safe relative paths (no `..`, no absolute)
  - Non-empty `docs` array of safe relative paths
- No `docs` entry may start with `docs/archive/`
- Every doc path in `docs` must exist on disk

Failures are reported with clear messages and the process exits non-zero.

## Failure Output Format

When triggered rules have no matching doc changes:

```
docs:check: code changed without acknowledging mapped docs.

Rule: langgraph
  Code:
    - src/graph/aceGraph.js
    - graph/nodes/planner.js
  Update (or banner needs-update on) at least one of:
    - docs/guides/langgraph.md
    - docs/architecture.md

Fix: edit the listed doc(s), or set DOCS_CHECK_SKIP=1 / commit with [docs-skip] intentionally.
Guide: read docs/doc-governance.md (or equivalent) for trigger rules and placement guidance.
```

## Skip Mechanisms (Intentional Only)

- Environment: `DOCS_CHECK_SKIP=1`
- Commit message contains `[docs-skip]`

These should be used rarely and only when the documentation impact has been deliberately judged irrelevant.

## Self-Protection

The "documentation-governance" rule watches:
- `docs/doc-triggers.json`
- The check script itself
- Git hook scripts
- The manager documentation files

Any change to the governance machinery must update at least one of its mapped docs.

## Recommendations for New Projects

1. Start with a minimal trigger map covering the highest-risk areas (auth, core graph, data models, API routes).
2. Add the check to CI and optionally a local pre-commit hook.
3. Keep the number of rules modest — too many noisy docs reduce signal.
4. Evolve the map as canonical ownership becomes clearer.