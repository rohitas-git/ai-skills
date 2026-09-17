# TDD wiring audit

Date: 2026-09-11  
Skill: `1-tdd`  
Status: reviewed; final catalog sweep pending

## Evidence boundary

Reviewed the complete 1,711-line package, including the live skill, all focused test,
mocking, portfolio, browser, reproduction, and pattern references, both full upstream
TDD snapshots, the upstream anti-pattern reference, metadata, agent descriptor, three
callers, parent workflows/HTML/flows, generated routing, and routing regressions. No
project test, application code, browser, database, service, worktree, dependency, or
remote system was changed or executed during this catalog audit.

## Decisions and changes

- Kept one atomic job: one agreed deterministic behavior slice from discriminating red
  evidence to minimal green implementation, then return the same candidate to its caller.
- Preserved Ship as primary owner and Diagnose as a conditional parent. Removed the stale
  Setup-hub membership and formalized the existing `1-execute-plan` caller. Each caller
  now dispatches to TDD and TDD returns its candidate rather than silently starting review,
  branch finishing, commits, or remote operations.
- Added **F-TDD1** to Ship workflow JSON, HTML, and flows. TDD is selected only when the
  seam and behavior are settled, an independent oracle exists, the outcome is deterministic,
  and both test and implementation edits are authorized. Characterization/Diagnose,
  planning/prototyping, and agent evaluation are explicit alternatives.
- Replaced generic `tdd`, `red green`, and `prove it` triggers with explicit TDD/test-first/
  bug-reproduction phrases and added exclusions for exploratory, probabilistic, unknown-
  cause, and already-green review work.
- Added exact task/acceptance source, allowed/excluded scope, repository/worktree/branch/
  HEAD, dirty ownership, toolchain, before candidate, fixture/state, local-service authority,
  and return-route identity.
- Made worktree creation conditional through `/1-git-worktrees`; documented that a worktree
  does not isolate ports, databases, queues, browsers, credentials, external services, or
  processes. Concurrent writers and implicit stash/reset/deletion of user work are forbidden.
- Required red to fail for the predicted behavioral reason, distinguished harness/fixture/
  unrelated/flaky failure, prohibited manufactured red and green-by-weakened-assertion,
  and made broader verification proportionate to policy and risk rather than universally
  running the full suite after each micro-step.
- Rejected the echo-chamber claim that agent-authored tests independently prove agent-authored
  implementation. A separate agent is also not independent when given the same unverified
  premise; the oracle must come from a contract, confirmed bug, or independently derived result.
- Prohibited deleting or hiding pre-existing implementation to reenact TDD. Existing work uses
  a real before revision, characterization, or diagnose-first evidence instead.
- Replaced fixed pyramid percentages and universal mock rules with behavior/risk/resource-
  based seam selection. Tightened browser candidate identity, state ownership, snapshots,
  coverage, conditional regression retention, and test-double contract limits.
- Marked full vendor/Superpowers bodies, language-specific pattern examples, and the upstream
  anti-pattern guide as historical source—not operative instructions. Live focused references
  were reduced to 20–44 lines each and explicitly supersede conflicting absolutes.

## Verification

- `python3 -m unittest scripts.test-routing.TddRouteTests`: **10 tests passed**.
- `python3 -m unittest scripts/test-routing.py`: **161 tests passed**.
- `scripts/generate-route-index`: generated **215 skill rows**.
- `scripts/lint-skills`: **Gate PASS**, 0 critical, 0 warnings, 63 informational findings,
  and 0 hub-member orphans.
- `git diff --check`: passed.
- Regression coverage proves dual-parent/caller return wiring, removal from Setup, F-TDD1
  parity, fit/oracle boundaries, exact candidate/worktree/service ownership, honest red/green
  dispositions, proportional verification, lean contextual references, and historical-source
  isolation from live behavior.

## Remaining limits

- A future TDD run still needs an actual independently grounded oracle and exact candidate;
  catalog wording cannot prove a project behavior.
- Caller-specific implementation and review semantics remain governed by their own skills.
- Catalog-wide completion remains pending; this is individual review 57 of 215.
