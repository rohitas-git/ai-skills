# Butler help and session-continuity wiring audit

Date: 2026-09-11  
Skills: `1-grok-help`, `1-context-monitor`, `1-strategic-compact`, `1-handoff`  
Status: reviewed; final catalog sweep pending

## Evidence boundary

Reviewed all four live skill bodies, Strategic Compact's complete curated and vendor
references, Handoff's agent metadata, Butler and Grilling memberships, workflow JSON,
HTML, flow-map projections, metadata handoffs, and focused regressions. No Grok host
file, consumer repository, worktree, temporary handoff, external service, catalog
install/sync, commit, push, or merge was touched.

## Decisions and changes

- Narrowed Grok Help to one explicitly Grok-specific question, smallest relevant
  local evidence, secret-minimized current-config inspection, and an explicit edit
  authority boundary. Catalog mutations return to Skill Manager; host configuration
  is correctly treated as shared beyond worktrees.
- Replaced Context Monitor's guessed percentages, fixed warning counts, and generic
  token tips with an evidence-backed continue/compact/handoff disposition. Context,
  quota, goal-budget, time, cost, and response depth are kept distinct.
- Rebuilt Strategic Compact as a host-neutral same-session continuation capsule. It
  no longer advertises a missing hook script, assumes `/compact`, installs Claude
  settings, or inherits numerical thresholds from its now-labeled historical source.
- Made Handoff's primary owner Butler while preserving its Grilling detour. It writes
  one new non-overwriting, redacted artifact at a safe boundary, records exact
  candidate/worktree/ownership/evidence/authority, verifies the file, returns it to
  its actual caller, and never resumes the suggested workflow automatically.
- Added safe-boundary gates so neither compaction nor handoff loses in-flight state,
  conflict/sequencer details, unreported tool output, or recovery information.

## Verification

- `python3 -m unittest scripts.test-routing.SessionContinuityRouteTests`: **7 passed**.
- `python3 -m unittest scripts/test-routing.py`: **206 passed**.
- `scripts/generate-route-index`: regenerated **215 skill rows**.
- `scripts/lint-skills`: **Gate PASS**, 0 critical, 0 warnings, 60 informational
  findings, and 0 hub-member orphans.
- `git diff --check`: passed.

Individual catalog reviews represented by this document are 69–72 of 215.

## Remaining limits

- Grok's local documentation/configuration was intentionally not read because this
  audit validates the skill contract, not a live Grok question.
- The host controls actual compaction and context telemetry; these skills cannot
  prove or mutate that state.
- Catalog-wide semantic reconciliation remains pending.
