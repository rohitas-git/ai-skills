# Implement-hub wiring audit

Date: 2026-09-11  
Skill: `0-implement`  
Status: reviewed; final catalog sweep pending

## Evidence boundary

Reviewed the complete live hub skill, all seven references, workflow JSON, rendered hub HTML,
Domain 3 flow map, generated routing data, every declared child target, workspace/delegation/
verification/closure semantics, and regression coverage. The two retained vendor guides were read
but are historical source, not operative instructions. This audit validates the Ship control path;
it does not semantically certify each child, which remains a separate catalog requirement.

## Decisions and changes

- Kept one hub job: preserve a bounded requested outcome, candidate, workspace, and authority while
  dispatching only the implementation specialists and evidence loops the change needs.
- Made a clear request, accepted specification, ticket, or plan valid entry evidence. Small reversible
  changes no longer require a ceremonial spec/plan; material product conflicts still return to
  Grilling or `1-to-spec`.
- Added an explicit workspace contract: repository/worktree path, branch/HEAD, dirty-file ownership,
  concurrent writers, and local-service ownership. Worktrees are conditional on protected-primary
  work, overlapping state, another task owning the checkout, concurrent isolation, or branch-specific
  local state, and always return provenance to Ship.
- Required every specialist to inherit and return the same task, candidate, workspace, dirty ownership,
  exclusions, and authority. No child may silently broaden scope, create a second workspace, or turn
  design/review into edits.
- Replaced automatic orchestration with direct execution by default. Delegation requires explicit
  request/authority and disjoint ownership; concurrent writers may not share a worktree, branch, file,
  database, port, artifact, or mutable service.
- Replaced universal TDD/full-suite/per-slice-commit rules with a behavior- and risk-selected evidence
  loop. TDD is limited to known deterministic behavior at an agreed seam; completion uses a claim
  ledger with PASS/FAIL/BLOCKED/SKIPPED/NOT APPLICABLE against the actual candidate.
- Added a bounded convergence closer: `1-code-review` inspects the actual task candidate, verified
  in-scope findings are repaired one by one under existing edit authority, affected evidence is rerun,
  and the candidate is re-reviewed until clear or genuinely blocked. Broader improvements stay outside
  the change.
- Separated implementation completion from Git and external authority. Atomic commits require commit
  authority; finish-branch runs only for requested integration/PR options; remote, production, publish,
  deploy, and protected-branch effects are never inferred.
- Rewrote four operative references to lean, contextual guidance and marked both vendor guides
  historical/non-operative.
- Reconciled all parent surfaces: metadata declares 36 outward routes, workflow membership contains
  exactly those 36 plus the hub itself, and HTML now links every live child. Fixed stale
  `engineering/`/`productivity/` identities and broken chart/flow relative paths.
- Updated F4, F-SP, and F5 consistently across workflow, HTML, and `flows.md` for buildability,
  explicit-only delegation, and evidence-backed review reconciliation.

## Verification

- `python3 -m unittest scripts.test-routing.ImplementHubRouteTests`: **6 tests passed**.
- `python3 -m unittest scripts/test-routing.py`: **94 tests passed**.
- `scripts/generate-route-index`: generated **215 skill rows**.
- `scripts/lint-skills`: **Gate PASS**, 0 critical, 0 warnings, 64 informational findings, and
  0 hub-member orphans.
- `git diff --check`: passed.
- `ImplementHubRouteTests` proves metadata/workflow/HTML child parity, child existence, resolvable
  workflow artifacts, current identities, worktree conditions, explicit-only delegation, candidate
  review/repair convergence, no inferred external effects, lean operative references, and historical
  vendor boundaries.

## Remaining limits

- This parent audit proves dispatch and return contracts, not the semantic quality of the remaining
  pending children.
- Real repository policy can require broader checks or stricter completion gates; the hub preserves
  those rules rather than replacing them with a universal command list.
- Other parent hubs and **168 of 215** live skills still lack individual semantic review evidence.
