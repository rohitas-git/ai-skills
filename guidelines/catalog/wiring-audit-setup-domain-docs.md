# Setup Domain Docs wiring audit

Date: 2026-09-11  
Skill: `1-setup-domain-docs`  
Status: reviewed; final catalog sweep pending

## Evidence boundary

Reviewed the complete live skill, shared domain template, parent route, metadata,
generated-route inputs, and focused regressions. No consumer repository, domain
document, ADR, worktree, application source, commit, push, or merge was changed.

## Decisions and changes

- Kept one job: configure domain-document discovery in one local SSOT plus one
  relative instructions pointer. Authoring domain vocabulary, context maps, ADRs,
  architecture decisions, or application code is excluded and routes to the
  relevant domain-modeling/design workflow.
- Added exact repository/worktree/branch/HEAD, dirty ownership, instruction
  hierarchy, allowed paths, observed layout, and write authority. Read-only
  inspection creates no worktree; authorized isolation returns through Setup and
  `/1-git-worktrees` before resuming the same task.
- Made layout selection evidence-based. Existing layouts are described as found;
  a root context plus `docs/adr/` is a new-convention default, while directory
  count alone cannot justify a multi-context model.
- Required claimed paths to resolve and future/conventional paths to be labelled
  honestly. Verification re-reads both outputs, resolves the pointer, inspects
  only the scoped diff, and checks idempotence.
- Added explicit parent/caller return and stopped automatic continuation into
  other setup work, Git operations, or remote effects.

## Verification

- Covered by `SetupRohitasSkillsRouteTests`: **16 focused setup tests passed**.
- `python3 -m unittest scripts/test-routing.py`: **178 tests passed**.
- `scripts/generate-route-index`: generated **215 skill rows**.
- `scripts/lint-skills`: **Gate PASS**, 0 critical, 0 warnings, 61 informational
  findings, and 0 hub-member orphans.
- `git diff --check`: passed.

## Remaining limits

- Future domain content still requires project evidence and its owning skill.
- Catalog-wide completion remains pending; this is individual review 60 of 215.
