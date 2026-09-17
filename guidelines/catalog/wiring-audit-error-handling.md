# Error-handling wiring audit

Date: 2026-09-11  
Skill: `1-error-handling`  
Status: reviewed; final catalog sweep pending

## Evidence boundary

Reviewed the complete live package: `SKILL.md`, `references/failure-policy.md`,
`references/typescript-javascript.md`, and `references/sources.md`. Also reviewed the
relevant dispatch, workflow JSON, HTML, and flow surfaces for its Architecture primary
parent and its Ship and Review callers. This audit verifies skill behavior and catalog
wiring; it does not validate a particular application's runtime error policy.

## Decisions and changes

- Kept one atomic job: define, implement, or narrowly review failure representation,
  propagation, recovery, retries, public translation, and cleanup.
- Kept `0-improve-codebase-architecture` as the primary soft owner and added the missing
  parent `next` edge and direct dispatch language.
- Added explicit soft memberships from `0-implement` and `0-review`. Ship calls the leaf
  only when implementation needs failure behavior and resumes the build. Review calls it
  only for an explicitly narrow, read-only failure-behavior review and receives findings.
- Preserved the diagnosis boundary: unexplained root-cause investigation belongs to
  `0-diagnosing-bugs`; `F-EH1` exposes Agent judgment rather than silently combining jobs.
- Added the shared Review candidate contract so a narrow review cannot expand beyond its
  pinned diff/module/PR or turn itself into edits.
- Added workspace and authority behavior: advice and review create no worktree; authorized
  edits reuse a matching caller workspace, call `1-git-worktrees` only when isolation is
  needed, and return. The skill does not switch branches, stash user work, install, reset
  shared services, mutate remotes, inject failures into live systems, commit, or publish.
- Retained the source ledger's fixed-source hashes, corrections, primary documentation,
  and explicit limits; no upstream scripts, hooks, dependencies, or permissions are live.
- Added routing regression tests covering primary/dual membership, all parent `next`
  surfaces, hub HTML links, Review/worktree contracts, and both ambiguity forks.

## Verification

- `python3 -m unittest scripts/test-routing.py`: **34 tests passed**.
- `scripts/generate-route-index`: generated **215 skill rows**.
- `scripts/lint-skills`: **Gate PASS**, 0 critical, 0 warnings, 61 informational findings,
  0 hub-member orphans.
- `git diff --check`: passed.
- `SKILL.md`: 69 lines; operative references are linked and all relative links resolve.

## Remaining limits

- No application code or framework-specific middleware was exercised; callers must verify
  their actual runtime, transport, persistence, and provider behavior.
- The final catalog-wide reconciliation remains pending, and parent hubs still require
  their own complete semantic audits beyond the targeted routing changes recorded here.
