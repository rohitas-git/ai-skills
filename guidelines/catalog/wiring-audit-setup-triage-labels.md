# Setup Triage Labels wiring audit

Date: 2026-09-11  
Skill: `1-setup-triage-labels`  
Status: reviewed; final catalog sweep pending

## Evidence boundary

Reviewed the complete live skill, shared label template, parent and triage routes,
metadata, generated-route inputs, and focused regressions. No consumer repository,
tracker, remote labels, issue/PR/MR, worktree, commit, push, or merge was queried or
changed.

## Decisions and changes

- Kept one job: map five canonical triage roles to local tracker-label strings in
  one SSOT plus one relative pointer. Creating/applying remote labels and triaging
  issues are separate authority and separate skills/work.
- Added exact repository/worktree/branch/HEAD, dirty ownership, instructions,
  issue-tracker SSOT, allowed paths, mapping, and write authority. Read-only setup
  does not query a remote tracker; worktrees do not isolate tracker state.
- Treated an explicit configure/enable request as opt-in instead of asking a
  redundant confirmation. Each role must appear exactly once with a non-empty
  target; duplicate targets that collapse states need explicit acceptance.
- Prohibited claims that remote labels exist without current evidence and return
  unknown existence as an evidence gap rather than performing an implicit query.
- Required idempotent mapping/pointer verification, scoped diff evidence, explicit
  parent/caller return, and no continuation into tracker or Git actions.

## Verification

- Covered by `SetupRohitasSkillsRouteTests`: **16 focused setup tests passed**.
- `python3 -m unittest scripts/test-routing.py`: **178 tests passed**.
- `scripts/generate-route-index`: generated **215 skill rows**.
- `scripts/lint-skills`: **Gate PASS**, 0 critical, 0 warnings, 61 informational
  findings, and 0 hub-member orphans.
- `git diff --check`: passed.

## Remaining limits

- A valid local mapping does not prove the corresponding remote labels exist.
- Catalog-wide completion remains pending; this is individual review 62 of 215.
