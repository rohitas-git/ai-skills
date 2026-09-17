# Coding-standards wiring audit

Date: 2026-09-11  
Skill: `1-coding-standards`  
Status: reviewed; final catalog sweep pending

## Evidence boundary

Reviewed the complete live skill, both declared parent routes, Architecture and Ship hub bodies,
HTML/workflow surfaces, generated route membership, and routing regression coverage. The package
has no operative reference files. This audit verifies how the skill constrains scoped code changes;
it does not impose one repository's conventions on another.

## Decisions and changes

- Kept one atomic job: apply repository-aligned naming, cohesion, and comment conventions inside an
  already selected candidate. Failure policy, principle explanation, file layout, public/API docs,
  and module design retain their specialist owners.
- Kept this as the catalog's intentional model-invoked coding aid while narrowing its activation to
  maintainability conventions. Clear specialist requests still bypass it.
- Formalized Architecture as primary owner and Ship as a soft caller; both expose the child in their
  `next`, body, HTML, and workflow/flow surfaces and receive its result back.
- Added the caller contract: inherit repository, worktree, branch, requested paths or diff, dirty-file
  ownership, authority mode, and acceptance criteria. The skill creates no worktree, switches no
  branch, and never converts read-only review into edits.
- Made repository instructions, formatter/linter configuration, nearby vocabulary, language idioms,
  and compatibility constraints authoritative over generic preferences.
- Removed mechanical style rules. Function length, argument count, extraction, comments, and
  abbreviations are evidence-dependent signals rather than universal thresholds.
- Prevented Boy Scout scope expansion: only task-owned code and the minimum surrounding lines may be
  changed; unrelated cleanup is proposed separately, and generated/vendor/snapshot/lockfile/
  migration/public-contract ownership is preserved.
- Added proportional verification in the caller's existing workspace and prohibited installation,
  shared-state reset, unrelated formatting, commit, publication, deployment, and merge side effects.
- Preserved F-C1 for genuinely ambiguous “clean this code” requests without forcing a craftsmanship
  essay or standards edit when the user's intent is already clear.

## Verification

- `python3 -m unittest scripts.test-routing.CodingStandardsRouteTests`: **4 tests passed**.
- `scripts/lint-skills`: **Gate PASS**, 0 critical, 0 warnings, 62 informational findings, and
  0 hub-member orphans.
- `git diff --check`: passed.
- Parent membership, dispatch text, HTML links, worktree boundaries, caller scope, and lean size are
  covered by `CodingStandardsRouteTests`.

## Remaining limits

- Repository-local standards remain authoritative, so this skill cannot prove a specific codebase's
  conventions without an actual caller and candidate.
- Other Architecture and Ship children remain semantically pending.
