# Observability and instrumentation wiring audit

Date: 2026-09-11  
Skill: `1-observability-and-instrumentation`  
Status: reviewed; final catalog sweep pending

## Evidence boundary

Reviewed the complete live skill and every operative reference, its Ship, DevOps, and
Agent Engineering parents across bodies/workflows/HTML/flows/generated routes, neighboring
specialist boundaries, candidate/worktree/authority behavior, and routing regressions. The
archived upstream and agent-observability files remain source material rather than operative
authority. This audit does not claim that any uninspected hosted collector, dashboard, alert,
runbook, SLO, or production signal currently behaves as intended.

## Decisions and changes

- Kept one atomic job: make one bounded behavior answer a stated operator question. Its
  modes are design/advice, read-only assessment, or an already-authorized repository edit.
- Narrowed triggers to explicit telemetry objects and operator questions. Active diagnosis,
  incident response, performance optimization, rollout, and broad security/privacy review
  retain their own owners.
- Formalized all three actual parents—Ship, DevOps, and Agent Engineering—with explicit
  caller returns. Their body/workflow/HTML/flow surfaces now describe the same bounded
  telemetry contract and remote-operation boundary.
- Required exact repository/worktree/branch/HEAD where files are involved, plus service/
  environment, evidence time, data classification, retention, owned paths/services, and
  allowed effects. Design/read-only assessment creates no worktree; edits reuse caller
  provenance or conditionally obtain isolation.
- Added a question-to-signal ledger for signal type, stable name, source boundary, fields/
  labels, propagation, sampling/aggregation, privacy/retention, ownership, and falsification.
- Made RED/USE, structured JSON, OpenTelemetry, correlation, tracing, dashboards, alerts,
  and runbooks conditional choices rather than universal requirements. Existing repository
  and platform conventions win when fit.
- Added bounded-cardinality reasoning and clarified that combined label products drive
  series cost. Unknown SLOs and thresholds remain proposals rather than invented facts.
- Added agent-specific privacy boundaries: operational metadata is separated from prompts,
  completions, retrieved content, memory, tool payloads/results, and feedback; sensitive
  content is omitted by default and traces do not prove behavioral correctness.
- Separated local/disposable verification from hosted evidence. Installation, shared-service
  starts, hosted queries/changes, fault injection, alert firing, deployment, and remote or
  production mutation require separate authority and are reported blocked/skipped otherwise.
- Replaced the 238-line absolute-heavy guide and 92-line universal checklist with concise
  operative adaptations; the full upstream remains archived for provenance.

## Verification

- `python3 -m unittest scripts.test-routing.ObservabilityRouteTests`: **6 tests passed**.
- `python3 -m unittest scripts/test-routing.py`: **111 tests passed**.
- `scripts/generate-route-index`: generated **215 skill rows**.
- `scripts/lint-skills`: **Gate PASS**, 0 critical, 0 warnings, 64 informational findings,
  and 0 hub-member orphans.
- `git diff --check`: passed.
- Regression coverage proves three-parent membership and dispatch, caller returns, exact
  candidate/worktree/environment/authority behavior, the one-question contract, privacy and
  remote-evidence rules, and removal of upstream absolutes.

## Remaining limits

- Hosted telemetry and production claims still require exact environment evidence and
  separately authorized operations.
- Other Ship, DevOps, and Agent Engineering children remain pending semantic review.
