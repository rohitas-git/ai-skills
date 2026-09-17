# Action-First Output wiring audit

Date: 2026-09-11  
Skill: `1-action-first-output`  
Status: reviewed; final catalog sweep pending

## Evidence boundary

Reviewed the complete live skill, retained upstream attribution, Butler
membership, workflow/HTML/flows projections, metadata, generated-route inputs,
and focused regressions. No chat mode was activated for the user, and no file,
tool, worktree, task state, external system, commit, or publication was changed
except this catalog's authorized skill/audit artifacts.

## Decisions and changes

- Kept one atomic job: shape output for the current chat after explicit user
  activation. Added bidirectional Butler/caller wiring without turning the mode
  into a task pipeline.
- Clarified that presentation cannot change task scope, tool selection, authority,
  evidence standards, rigor, or required response structure and must never infer
  a medical condition.
- Replaced the fixed five-item/off-screen rule with readable grouping that cannot
  hide safety conditions, evidence limits, choices, or deliverables.
- Made persistence honest: the mode remains active in observable chat state, but
  compacted/restarted/stateless hosts may lose it and must not claim otherwise.
- Explicitly made worktrees and tools inapplicable. Activation/deactivation cannot
  edit files or task state, and the skill returns mode state plus the next action
  to its caller without starting work.
- Ensured the latest user formatting request and higher-priority response rules
  override the mode, including immediate deactivation requests.

## Verification

- `python3 -m unittest scripts.test-routing.ActionFirstOutputRouteTests`:
  **5 tests passed**.
- `python3 -m unittest scripts/test-routing.py`: **183 tests passed**.
- `scripts/generate-route-index`: generated **215 skill rows**.
- `scripts/lint-skills`: **Gate PASS**, 0 critical, 0 warnings, 61 informational
  findings, and 0 hub-member orphans.
- `git diff --check`: passed.

## Remaining limits

- Mode persistence depends on visible host/session state; wording cannot create
  durable memory in a stateless client.
- Catalog-wide completion remains pending; this is individual review 63 of 215.
