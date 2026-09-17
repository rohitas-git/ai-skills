# Setup Issue Tracker wiring audit

Date: 2026-09-11  
Skill: `1-setup-issue-tracker`  
Status: reviewed; final catalog sweep pending

## Evidence boundary

Reviewed the complete live skill, its parent route and four tracker templates,
metadata, generated route inputs, and focused regressions. No consumer repository,
instructions file, worktree, tracker account/project, issue, PR/MR, credential,
commit, push, or merge was read or changed beyond this catalog's local files.

## Decisions and changes

- Kept one atomic job: configure one repository-local issue-tracker SSOT and
  exactly one relative pointer. Remote tracker operation is explicitly excluded.
- Added a parent/caller return in both directions with
  `/0-setup-rohitas-skills`; adjacent setup concerns remain cousins, not an
  automatic sequence.
- Required exact repository root, worktree, branch/detached state, `HEAD`, dirty
  ownership, applicable instructions, allowed paths, requested tracker, and write
  authority. Read-only inspection creates no worktree; isolation returns through
  the parent to `/1-git-worktrees` and resumes the same task.
- Documented that a worktree does not isolate tracker accounts/projects,
  credentials, issues, labels, or PRs/MRs and prohibited implicit stash, reset,
  clean, branch switching, or overwrite of user work.
- Made tracker choice evidence-based: honor an explicit choice; otherwise accept
  only an unambiguous remote or repository convention and ask once on conflict.
  The skill does not authenticate or query a tracker just to select a template.
- Separated command documentation from action authority. Templates may record
  future command shapes, but setup cannot create/edit/label/assign/comment/close
  remote work, authenticate, commit, push, or merge.
- Replaced unconditional preview gates with direct authorized writes when the
  request is clear, while retaining a preview for explicit requests or ambiguity.
  Output verification re-reads files, resolves the pointer, inspects the scoped
  diff, and proves a second application would not duplicate content.

## Verification

- `python3 -m unittest scripts.test-routing.SetupRohitasSkillsRouteTests`:
  **10 tests passed**.
- `python3 -m unittest scripts/test-routing.py`: **172 tests passed**.
- `scripts/generate-route-index`: generated **215 skill rows**.
- `scripts/lint-skills`: **Gate PASS**, 0 critical, 0 warnings, 61 informational
  findings, and 0 hub-member orphans.
- `git diff --check`: passed.

## Remaining limits

- A future setup run must still resolve the actual repository's instruction-file
  hierarchy and tracker convention from current evidence.
- This local SSOT cannot prove that future authenticated tracker operations target
  the right account or project; the operational skill must re-pin those values.
- Catalog-wide completion remains pending; this is individual review 59 of 215.
