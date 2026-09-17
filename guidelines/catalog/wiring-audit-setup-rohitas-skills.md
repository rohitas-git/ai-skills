# Setup Rohitas Skills hub wiring audit

Date: 2026-09-11  
Skill: `0-setup-rohitas-skills`  
Status: reviewed; final catalog sweep pending

## Evidence boundary

Reviewed the complete hub package: its live skill, four shared setup-template
assets, agent descriptor, Butler membership, child routes, workflow JSON, hub
HTML, flows projection, and routing regressions. The four child skills were
inspected to establish the handoff boundary but retain their own pending semantic
audits. No consumer repository, worktree, tracker, vault, remote account, commit,
push, or installation was changed during this audit.

## Decisions and changes

- Kept one atomic hub job: inspect a pinned consumer repository read-only and
  route exactly one configuration request to one of four setup leaves. Removed
  stale `1-to-spec`, `1-to-tickets`, `0-triage`, and architecture memberships.
- Replaced the implied multi-step fresh-repository sequence with direct routing
  for an explicit request and one **F-S1** question only when the requested setup
  target is ambiguous. Removed obsolete F1/F2 forks from JSON, HTML, and flows.
- Added the exact consumer repository, worktree, branch/detached state, `HEAD`,
  dirty-state ownership, active instructions, allowed paths, and write-authority
  handoff contract. Read-only inventory creates no worktree; required isolation
  routes through `/1-git-worktrees` and resumes the setup route.
- Stated that worktrees isolate files and Git state, not tracker accounts,
  vaults, credentials, ports, databases, or shared services. The hub cannot
  stash, reset, clean, switch branches, commit, push, or mutate external systems.
- Required the selected child to receive current contents and return its proposed
  or applied diff, verification evidence, and unresolved external setup, then stop.
  A fresh repo may need several setup tasks, but each remains a separate invocation.
- Marked shared files as inactive starting templates rather than permissions.
  GitHub/GitLab templates now pin account and repository authority and reject
  JSON-escaped `\n` bodies; GitHub multiline Markdown uses reviewed body files.
- Corrected the agent display name and repaired broken flows/chart paths in both
  this hub and the already-reviewed Diagnose hub. Added link-resolution regression
  checks so those projections cannot silently drift again.

## Verification

- `python3 -m unittest scripts.test-routing.SetupRohitasSkillsRouteTests scripts.test-routing.DiagnosingBugsRouteTests`: **17 tests passed**.
- `python3 -m unittest scripts/test-routing.py`: **169 tests passed**.
- `scripts/generate-route-index`: generated **215 skill rows**.
- `scripts/lint-skills`: **Gate PASS**, 0 critical, 0 warnings, 61 informational
  findings, and 0 hub-member orphans.
- `git diff --check`: passed.
- Regression coverage proves exact child parity, F-S1-only behavior, workspace/
  authority/return constraints, current agent identity, resolvable hub artifacts,
  and safe local/remote tracker-template boundaries.

## Remaining limits

- The hub can prove routing consistency, not whether a future consumer repository's
  tracker, domain docs, vault pointer, or labels are correct.
- Each of the four selected child skills still requires its own full semantic audit.
- Catalog-wide completion remains pending; this is individual review 58 of 215.
