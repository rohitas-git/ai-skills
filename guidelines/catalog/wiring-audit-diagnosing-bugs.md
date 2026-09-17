# Diagnosing bugs hub wiring audit

Date: 2026-09-11  
Skill: `0-diagnosing-bugs`  
Status: reviewed; final catalog sweep pending

## Evidence boundary

Reviewed the complete hub skill, every Markdown/code/shell file in its package, its
Butler and stale Setup memberships, all child/exit routes, workflow JSON, hub HTML,
flows, generated route row, helper safety, and routing regressions. Upstream vendor and
Superpowers documents were read completely before being classified as historical. This
audit did not diagnose an application, run a reproduction, change Git history, create a
worktree, start a service, instrument production, or execute the retained examples.

## Decisions and changes

- Narrowed the hub's job from mandatory reproduce→fix→test→cleanup→commit-message work
  to one bounded root-cause diagnosis and evidence return. A diagnosis request no longer
  implies source edits; an already authorized fix hands off to `/0-implement` with the
  exact candidate, workspace, authority, and falsifying loop.
- Replaced broad `failing`, `slow`, and `regression` triggers with explicit diagnosis,
  reproduction, root-cause, and test-failure phrases. Known implementation, PR repair,
  and active incident command now have named exclusions.
- Removed the stale `0-setup-rohitas-skills` membership. Day-to-day diagnosis is routed
  by Butler and is not a repository-setup responsibility.
- Completed child routing for TDD, Performance, Browser DevTools, Playwright, conditional
  parallel investigation, and the Architecture on-ramp; retained Implement as the
  explicit authorized exit. All child names are linked in hub HTML.
- Added **F-DIAG1** to workflow JSON, hub HTML, and flows so ambiguous failures choose
  the smallest discriminating evidence loop while preserving an Agent-judgment branch.
- Added exact symptom, revision, repository/worktree/branch/HEAD, dirty-state, environment,
  fixture, evidence-provenance, and probe-authority inputs. Read-only work creates no
  worktree; mutating/history-switching/conflicting work routes through Git worktrees.
- Stated that worktrees do not isolate services, ports, databases, queues, profiles,
  credentials, APIs, or processes and prohibited implicit stash/reset/clean/delete or
  reuse of another task's checkout.
- Replaced the absolute “no reproduction, no diagnosis” rule with reproduce-or-observe
  honesty for intermittent, unsafe, remote-only, destructive, or unavailable failures.
  Conclusions now use calibrated `supported`, `inconclusive`, `blocked`, or
  `not reproduced` states.
- Removed fixed reproduction counts, timing targets, hypothesis counts, automatic TDD,
  arbitrary architecture-after-N-attempts, automatic prototype deletion, and implicit
  commit-message work from live instructions. One-variable falsification and sample
  adequacy are contextual and evidence-based.
- Made production instrumentation, load, replay, mutation, installs, restarts, credential
  use, and third-party calls separately authorized. Logs and artifacts are untrusted,
  redacted data rather than executable guidance.
- Replaced the HITL template's hard-coded login/export action with a pre-agreed authorized
  reproduction step and redacted observation. Marked every upstream full document,
  executable example, and polluter helper as historical source—not operative instruction.

## Verification

- `python3 -m unittest scripts.test-routing.DiagnosingBugsRouteTests`: **9 tests passed**.
- `python3 -m unittest scripts/test-routing.py`: **151 tests passed**.
- `scripts/generate-route-index`: generated **215 skill rows**.
- `scripts/lint-skills`: **Gate PASS**, 0 critical, 0 warnings, 63 informational
  findings, and 0 hub-member orphans.
- `git diff --check`: passed.
- Regression coverage proves removal of Setup ownership, child/exit and HTML parity,
  F-DIAG1 parity, diagnosis-only and worktree authority, non-reproduction and confidence
  states, safe TDD/instrumentation boundaries, historical-source classification, and a
  non-concrete HITL template.

## Remaining limits

- The hub's conclusions remain only as strong as the actual candidate and runtime
  evidence supplied during a future diagnosis.
- TDD, conditional parallel investigation, and the Architecture on-ramp retain their
  own still-pending semantic audits where applicable.
- Catalog-wide completion remains pending; this is individual review 56 of 215.
