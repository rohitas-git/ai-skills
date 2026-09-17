# Setup Vault Root wiring audit

Date: 2026-09-11  
Skill: `1-setup-vault-root`  
Status: reviewed; final catalog sweep pending

## Evidence boundary

Reviewed the complete live skill, shared vault template, parent/vault-hub routes,
metadata, generated-route inputs, and focused regressions. No consumer repository,
vault path, vault content, worktree, commit, push, or publication was accessed or
changed.

## Decisions and changes

- Kept one job: record one user-supplied absolute vault root in one approved SSOT
  plus one pointer. The skill cannot discover, enumerate, move, sync, or edit a vault.
- Added exact repository/worktree/branch/HEAD, dirty ownership, instruction file,
  allowed paths, and authority. Read-only validation checks only whether the
  supplied path is absolute and resolves to a directory; future paths are labelled.
- Made the cross-worktree boundary explicit: every worktree may point at the same
  vault, so Git isolation provides no vault-content isolation.
- Added a privacy gate because an absolute path is host-specific and may expose a
  username or directory layout. A tracked/shared destination requires informed
  authorization; setup itself cannot commit, push, or publish the path.
- Required idempotent pointer/diff verification and a caller return containing
  path-validity plus tracking/privacy disposition.

## Verification

- Covered by `SetupRohitasSkillsRouteTests`: **16 focused setup tests passed**.
- `python3 -m unittest scripts/test-routing.py`: **178 tests passed**.
- `scripts/generate-route-index`: generated **215 skill rows**.
- `scripts/lint-skills`: **Gate PASS**, 0 critical, 0 warnings, 61 informational
  findings, and 0 hub-member orphans.
- `git diff --check`: passed.

## Remaining limits

- Path validity does not authorize reading the vault or establish its intended scope.
- Catalog-wide completion remains pending; this is individual review 61 of 215.
