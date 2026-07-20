# Severity labels and change sizing (merged from vendor)

Source: archive vendor `code-review-and-quality`. Does **not** replace multi-axis Spec/Standards/Maintainability — use labels **inside** each axis report.

## Severity (within an axis)

| Label | Meaning |
|-------|---------|
| **Critical** | Must fix before merge (wrong behavior, security, data loss, broken build) |
| **Major** | Should fix in this PR or immediate follow-up |
| **Nit** | Style/clarity; optional if timeboxed |
| **Optional** | Idea for later; not blocking |

Still **do not cross-rerank axes** into one global list.

## Structural remedies

Prefer remedies that change structure (extract, delete, move seam) over "add a comment." If the fix is large, recommend a follow-up PR rather than bloating this one.

## Change sizing

Flag PRs that mix unrelated concerns or exceed ~300–400 meaningful LOC without a clear reason. Prefer vertical slices (see `/0-implement` incremental guidance).

## Dependency upgrades

Review lockfile + changelog risk separately from feature logic; note major bumps and security advisories.
