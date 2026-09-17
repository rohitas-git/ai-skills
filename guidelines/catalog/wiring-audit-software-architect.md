# Software-architect wiring audit

Date: 2026-09-11  
Skill: `2-software-architect`  
Status: reviewed; final catalog sweep pending

## Evidence boundary

Reviewed the complete live skill, all three formal parent bodies/HTML/workflows/flows/generated
routes, catalog descriptions, depth/ownership semantics, caller/worktree behavior, and regressions.
The package has no operative references. This audit validates bounded decision analysis; it does not
choose an architecture for an external system.

## Decisions and changes

- Kept one atomic job: evaluate one consequential system-design/refactoring decision and return a
  defensible choice, conditions, migration/rollback, and verification implications. Opportunity
  scanning, module/API design, fixed-diff review, ADR recording, and implementation retain their
  specialist owners.
- Reconciled the apparent parent conflict without a disruptive rename. Catalog depth/metadata remains
  under the `1-code-review` sub-hub; Architecture is the domain entry for design/strategy, while
  Review and Code Review supply a pinned read-only candidate. No parent is falsely called dual-primary.
- Added `2-software-architect` to the Code Review sub-hub's `next`, body, linked HTML, workflow note,
  and flow description. Architecture and Review surfaces now describe the same bounded return.
- Added explicit caller provenance: decision question, system boundary, repository and exact
  worktree/branch/HEAD, review base/candidate, dirty ownership, business/operational constraints,
  and read-only authority. The skill creates no worktree, switches no branch, and cannot turn review
  into edits or an unrequested redesign.
- Replaced the mandatory pillar-score report with decision-relevant drivers only. Repository state,
  documented intent, deployed evidence, and inference remain distinct; missing inputs and assumptions
  are visible.
- Replaced the forced “2–4 alternatives” ritual with the smallest viable choice set, including keeping
  the current design when credible. Pattern names apply only when their mechanics do.
- Prevented fabricated precision: percentages, SLOs, latency/cost improvements, and other quantitative
  claims require measurements or labeled assumptions/ranges.
- Made recommendations conditional and falsifiable through assumptions, disconfirming evidence,
  reversible first steps, verification signals, and stop/reconsider criteria. Neither big-bang nor
  phased migration is an automatic default.
- Review returns findings inside the pinned candidate and labels broader redesign optional. Design
  returns a decision packet; public-contract detail, module design, ADR/domain recording, and
  implementation route only after an explicit next request.
- Tables and diagrams are conditional on explanatory value rather than mandatory output decoration.
- Prohibited code/doc/infrastructure/database mutation, installs, services, fetches, commits,
  publication, deployment, and merge.

## Verification

- `python3 -m unittest scripts/test-routing.py`: **88 tests passed**.
- `scripts/generate-route-index`: generated **215 skill rows**.
- `scripts/lint-skills`: **Gate PASS**, 0 critical, 0 warnings, 64 informational findings, and
  0 hub-member orphans.
- `git diff --check`: passed.
- `SoftwareArchitectRouteTests` covers three-parent membership and linked surfaces, depth-owner
  explanation, read-only candidate/worktree behavior, optional follow-up boundaries, viable-current
  option, non-forced alternatives, non-fabricated numbers, and conditional visuals.

## Remaining limits

- A real decision still requires system-specific evidence and stakeholders; this workflow deliberately
  cannot manufacture missing constraints.
- Other Review and Ship children remain semantically pending.
