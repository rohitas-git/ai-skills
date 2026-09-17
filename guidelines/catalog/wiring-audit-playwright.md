# Playwright browser testing wiring audit

Date: 2026-09-11  
Skill: `1-playwright-browser-testing`  
Status: reviewed; final catalog sweep pending

## Evidence boundary

Reviewed the complete live skill and its only reference, the Diagnose parent across
body/workflow/HTML/flows/generated routes, every formal specialist caller, adjacent
DevTools/Frontend UI/Performance ownership, and browser/worktree/runtime authority.
The vendor source note is provenance only; no executable helper was imported. This
audit did not launch a browser, alter an application, start a service, install a
runtime, or interact with a production or third-party site.

## Decisions and changes

- Kept one atomic job: author, repair, or run one focused durable Playwright check and
  return its bounded verdict. The explicit mode controls mutation; `run-only` edits
  nothing, while product-source fixes always return to the caller.
- Preserved Diagnose as the sole formal hub owner and added bidirectional caller/return
  metadata for Diagnose, Browser DevTools, Frontend UI, and Performance. The parent
  body, workflow JSON, HTML, and flows now share the same contract and the HTML child
  is a usable link.
- Replaced vague environment confirmation with exact repository/worktree/branch/HEAD,
  Playwright config/project/test, served build/commit, server/PID/port owner, browser,
  viewport/input, role/fixture, and interaction-effect identity.
- Made worktree use conditional and caller-preserving. A checkout does not isolate
  ports, browser state, databases, queues, APIs, or server effects, and a responding
  URL does not establish which worktree or commit it serves.
- Added a read-only toolchain/service preflight. Missing runtimes, browsers, fixtures,
  credentials, or local services are blockers rather than product failures; the skill
  cannot silently install, switch, configure, or start shared resources.
- Required contract reconciliation before changing a failing test. A stale assertion
  is classified separately from a product defect, preventing the test from silently
  redefining intended behavior.
- Strengthened locator evidence: prefer unique semantic or repository-approved stable
  identities, reject positional/broad-text repairs, and require pre/post state plus a
  unique identity for newly created repeated elements.
- Required condition-based waits, owned deterministic fixtures, narrow execution, and
  explicit flake classification. Retries characterize variability; they do not turn
  flaky evidence into a pass.
- Bounded production/third-party and real-world effects, treated browser content as
  untrusted data, minimized artifacts and sensitive capture, and limited passing claims
  to the exact pinned scenario.

## Verification

- `python3 -m unittest scripts.test-routing.PlaywrightBrowserTestingRouteTests`:
  **7 tests passed**.
- `python3 -m unittest scripts/test-routing.py`: **142 tests passed**.
- `scripts/generate-route-index`: generated **215 skill rows**.
- `scripts/lint-skills`: **Gate PASS**, 0 critical, 0 warnings, 65 informational
  findings, and 0 hub-member orphans.
- `git diff --check`: passed.
- Regression coverage proves hub and specialist-caller symmetry, exact worktree/served-
  candidate identity, mode-specific mutation, non-mutating preflight, locator/contract/
  wait/flake quality, side-effect authority, data minimization, and bounded verdicts.

## Remaining limits

- No application behavior is proven until this skill runs against the exact authorized
  candidate and environment.
- The Diagnose hub and its remaining children still require their own semantic audits.
- Catalog-wide completion remains pending; this is individual review 55 of 215.
