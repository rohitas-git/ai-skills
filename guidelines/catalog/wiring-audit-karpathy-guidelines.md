# Karpathy-guidelines wiring audit

Date: 2026-09-11  
Skill: `1-karpathy-guidelines`  
Status: reviewed; final catalog sweep pending

## Evidence boundary

Reviewed the complete live skill, its sole Ship parent across body/workflow/HTML/flows/generated
routes, cousin collisions, caller/worktree/authority behavior, and regressions. The package has no
local references or executable assets. This audit validates the adapted process checklist; it does
not independently validate the linked social-media source or any implementation to which the
checklist may later be applied.

## Decisions and changes

- Kept one atomic job: apply four process checks inside one already-scoped implementation and return
  the unchanged task/candidate/workspace/authority packet to Ship.
- Narrowed triggering from generic writing/reviewing/refactoring and broad “simplicity first” language
  to explicit Karpathy, assumption-surfacing, surgical-diff, or goal-driven implementation requests.
  Ordinary implementation remains `0-implement`; review and verification retain their own skills.
- Added explicit `prev` and `next` returns to `0-implement`. The parent body, workflow note, HTML,
  and Domain 3 flow map now identify the leaf as an opt-in checklist rather than an implicit
  always-on pipeline.
- Required inheritance of caller, outcome/exclusions, exact repository/worktree/branch/HEAD,
  dirty-file and service ownership, allowed paths/effects, and acceptance evidence. The skill creates
  no workspace and grants no authority.
- Limited clarification to load-bearing decisions. Small reversible assumptions use repository
  evidence and remain visible instead of causing unnecessary pauses.
- Replaced speculative-minimalism absolutes with an evidence boundary: reuse local/platform capability
  where appropriate, but never simplify away validation, authorization, accessibility, data integrity,
  recovery, observability, or compatibility. “Impossible” scenarios require an enforced invariant.
- Replaced arbitrary 200-versus-50 line targets and senior-engineer intuition tests with a scope ledger:
  requested, required compatibility/cleanup, or excluded.
- Replaced forced test-first examples with falsifying evidence chosen for the behavior: tests,
  characterization, runtime inspection, static/type checks, or another fitting loop. Exploratory and
  probabilistic work does not inherit a mechanical TDD requirement.
- Prohibited advice/review mutations, branch/worktree/stash actions, installs, shared-service starts,
  commits, push/publication/deploy/merge, remote/production mutation, and unbounded looping.

## Verification

- `python3 -m unittest scripts.test-routing.KarpathyGuidelinesRouteTests`: **5 tests passed**.
- `python3 -m unittest scripts/test-routing.py`: **99 tests passed**.
- `scripts/generate-route-index`: generated **215 skill rows**.
- `scripts/lint-skills`: **Gate PASS**, 0 critical, 0 warnings, 64 informational findings, and
  0 hub-member orphans.
- `git diff --check`: passed.
- Regression coverage proves sole-parent membership, explicit parent dispatch, return wiring,
  non-generic triggers, candidate/worktree/authority preservation, scope classification, evidence-loop
  choice, external-effect prohibitions, and removal of numeric/safety-shortcut guidance.

## Remaining limits

- The checklist intentionally does not implement, review, or verify work by itself; its value depends
  on receiving a concrete Ship task and returning its decisions to that caller.
- Other Ship children remain pending semantic review.
