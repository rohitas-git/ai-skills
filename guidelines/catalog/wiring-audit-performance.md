# Performance optimization wiring audit

Date: 2026-09-11  
Skill: `1-performance-optimization`  
Status: reviewed; final catalog sweep pending

## Evidence boundary

Reviewed the complete live skill and every operative reference, its Diagnose and Ship
parents across bodies/workflows/HTML/flows/generated routes, neighboring performance/
telemetry/database/browser boundaries, candidate/worktree/shared-resource authority, and
routing regressions. The archived upstream remains source material rather than operative
budgets or commands. This audit did not benchmark an application, install tooling, execute
a query plan, create an index, apply a migration, run load, or inspect production metrics.

## Decisions and changes

- Kept one atomic job: run one controlled optimization experiment against one measured
  bottleneck and explicit performance claim, preserving correctness and other guards.
- Added Ship as a formal shared parent because the skill may edit code/config after Diagnose
  supplies a repeatable loop. Both parents now dispatch and receive the same loop/candidate/
  worktree/authority packet and explicit experiment disposition.
- Narrowed triggers to budgets, traces, profiles, query plans, field evidence, or repeatable
  benchmarks that identify a bottleneck. Unknown symptoms, speculative tuning, durable
  telemetry, and broad database advice retain their own owners.
- Required exact repository/worktree/branch/HEAD, workload/fixture, tool and version, machine/
  runtime/network/database identity, warm/cold state, repetitions, correctness checks, artifact
  ownership, and allowed load/schema/service effects. Worktrees do not isolate compute,
  networks, databases, caches, ports, load generators, or hosted datasets.
- Added a measurement contract with raw samples, variability, confounders, field-versus-
  synthetic distinctions, and a predeclared practical decision threshold.
- Required localization before remedies and one causal hypothesis/variable where possible.
  Caches, indexes, pools, memoization, preloads, workers, CDNs, and similar changes are
  hypotheses rather than checklist defaults.
- Added correctness/cost boundaries for cache partitioning and staleness, query-plan execution,
  migration ownership, write/lock costs, concurrency/backpressure, bounded load, and frontend
  delivery trade-offs.
- Made before/after comparison candidate- and protocol-aware, with re-baselining when the
  protocol is corrected. A delta inside noise or without practical value is not claimed as a win.
- Replaced automatic keep/revert/commit language with an explicit keep/revise/recommend-removal/
  inconclusive disposition. User work is never silently reverted, and complexity is not retained
  solely because it was written.
- Made regression guards conditional on stability and repository policy; noisy or environment-
  sensitive metrics may belong in trend monitoring instead of required CI.
- Removed hard-coded web/backend budgets, evergreen Core Web Vitals numbers, framework recipes,
  unapproved `npx` commands, and remote-load implications from the operative package while
  preserving the 496-line upstream snapshot in archive.

## Verification

- `python3 -m unittest scripts.test-routing.PerformanceOptimizationRouteTests`: **6 tests passed**.
- `python3 -m unittest scripts/test-routing.py`: **129 tests passed**.
- `scripts/generate-route-index`: generated **215 skill rows**.
- `scripts/lint-skills`: **Gate PASS**, 0 critical, 0 warnings, 65 informational findings, and
  0 hub-member orphans.
- `git diff --check`: passed.
- Regression coverage proves two-parent membership/dispatch/returns, exact candidate/worktree/
  protocol/authority identity, comparable evidence, explicit disposition, database/load safety,
  and removal of upstream numeric/tool/action absolutes.

## Remaining limits

- Any actual performance improvement remains unproven until a concrete target supplies comparable
  before/after evidence under its real workload and environment.
- Other Diagnose and Ship children remain pending semantic review.
