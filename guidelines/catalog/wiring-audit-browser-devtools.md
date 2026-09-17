# Browser testing with DevTools wiring audit

Date: 2026-09-11  
Skill: `1-browser-testing-with-devtools`  
Status: reviewed; final catalog sweep pending

## Evidence boundary

Reviewed the complete live skill and every operative reference, its Diagnose parent across
body/workflow/HTML/flows/generated routes, its Frontend UI and Performance caller handoffs,
neighboring Playwright/Visual Edit ownership, browser/profile/server/worktree authority, and
routing regressions. The archived upstream remains source material rather than installation or
execution authority. This audit did not open a browser, inspect a product, attach to a profile,
start a server, install an MCP, or collect browser data.

## Decisions and changes

- Kept one atomic job: run one read-only browser evidence session against a pinned scenario and
  return its observations. Source editing and durable regression-test authoring are explicit
  handoffs rather than hidden later steps.
- Preserved Diagnose as the sole hub owner while formalizing returns to Diagnose, Frontend UI,
  and Performance. Parent body/workflow/HTML/flows now state the candidate/server/profile-bound
  evidence contract; caller metadata routes back without adding redundant hub membership.
- Narrowed triggers to explicit DOM, accessibility-tree, console, network-metadata, layout,
  screenshot, or trace inspection. Implementation, Playwright regression tests, performance
  experiments, and connected-app visual mutation retain their owners.
- Required repository/worktree/branch/HEAD, served build/commit, URL/origin, server command/PID/
  port owner, browser/profile/viewport/input, role/fixture, permitted interaction effects, data
  sensitivity, and evidence identity. A worktree neither proves served code nor isolates profiles,
  cookies, databases, queues, ports, APIs, or server-side effects.
- Removed automatic browser/MCP installation and personal-profile attachment. Missing setup is
  returned as a prerequisite; dedicated ephemeral/test profiles and disposable data are preferred.
- Classified clicks and submissions by real effect. Record creation, messages, purchases,
  permission/auth changes, destructive actions, and production/third-party effects require
  separate authority even when performed through a browser.
- Treated page, DOM, console, accessibility, response, and tool content as untrusted data. Unknown
  extracted URLs, page-supplied code, credential storage, broad network bodies, and unrelated tabs
  remain outside the observation boundary.
- Added a claim-to-evidence map: screenshots, DOM, accessibility trees, network metadata, traces,
  and console entries each prove only bounded facts. Clean console, one screenshot, or one tree
  cannot prove user success, conformance, backend correctness, or field performance.
- Removed universal zero-warning and all-findings-fixed gates, fixed accessibility folklore, broad
  capture, and source-fix steps from the operative guide while preserving the 317-line upstream
  snapshot for provenance.

## Verification

- `python3 -m unittest scripts.test-routing.BrowserDevtoolsRouteTests`: **6 tests passed**.
- `python3 -m unittest scripts/test-routing.py`: **135 tests passed**.
- `scripts/generate-route-index`: generated **215 skill rows**.
- `scripts/lint-skills`: **Gate PASS**, 0 critical, 0 warnings, 65 informational findings, and
  0 hub-member orphans.
- `git diff --check`: passed.
- Regression coverage proves parent and specialist-caller wiring, exact candidate/server/profile/
  fixture authority, no-worktree/no-edit behavior, untrusted-data and action-effect controls,
  evidence limits, and removal of upstream setup/edit/universal-gate instructions.

## Remaining limits

- No browser-facing product claim is proven until the skill is used against an exact served
  candidate with authorized runtime evidence.
- Playwright and other Diagnose children remain pending semantic review.
