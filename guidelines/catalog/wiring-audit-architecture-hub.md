# Architecture hub wiring audit

Date: 2026-09-11  
Skill: `0-improve-codebase-architecture`  
Status: reviewed; final catalog sweep pending

## Evidence boundary

Reviewed the complete hub skill, HTML-report guide, agent metadata, workflow JSON, hub HTML,
Domain 8 flow surface, every declared live child edge, and caller/worktree behavior. This
verifies routing and scan/report safety; it does not substitute for semantic audits of every
remaining child or for an architecture review of a particular repository.

## Decisions and changes

- Reframed the hub as a router first and bounded read-only deepening scan second. Clear API,
  module, system, failure, retirement, principles/standards, Go, graph, and documentation
  requests dispatch directly to one specialist and return to the caller.
- Made `metadata.catalog.next` enumerate every live declared child. Updated workflow JSON,
  Domain 8 flows, and hub HTML so route, pipeline, fork, and visible-link surfaces agree.
- Added an evidence boundary for broad scans: repository/worktree/branch, caller, requested
  paths, comparison/base, dirty-state ownership, excluded areas, and partial-coverage labels.
  Read-only scans create no worktree and never switch branches or stash user work.
- Removed automatic Agent-tool exploration. Local read-only exploration is the default;
  sub-agents are available only when explicitly requested and their scopes are independent.
- Replaced mandatory HTML with Markdown by default. Requested HTML is a unique local static file
  with inline CSS/SVG only—no Tailwind/Mermaid CDN, scripts, analytics, remote assets, browser
  opening, or unescaped repository text.
- Removed automatic `CONTEXT.md` and ADR mutation. Durable documentation changes route through
  `1-domain-modeling` only with separate write authority.
- Clarified F9 and workflow return: the report is terminal until a candidate is selected;
  design may continue through `1-grill-with-docs`, while requested implementation returns to
  `0-implement`, which owns workspace isolation, edits, verification, review, and commits.
- Repaired stale/broken hub HTML paths for the flows chart, flows SSOT, and live skill locations;
  added all missing live child links plus F-C1/F-D1/F-ARCH1/F-EH1/F9 visibility.
- Added regression checks for child discovery across metadata/body/HTML, local-link resolution,
  every fork's Agent judgment branch, no automatic delegation/docs mutation, scan worktree rules,
  and script/network-free HTML guidance.

## Verification

- `python3 -m unittest scripts/test-routing.py`: **52 tests passed**.
- `scripts/generate-route-index`: generated **215 skill rows**.
- `scripts/lint-skills`: **Gate PASS**, 0 critical, 0 warnings, 63 informational findings,
  and 0 hub-member orphans.
- `git diff --check`: passed.
- Main hub remains below the 120-line lean target; its only operative supporting guide was read
  completely and rewritten to a bounded static-output contract.

## Remaining limits

- No repository was scanned and no report artifact was rendered in this audit; the checks cover
  instructions, routes, and local-link/static-report invariants.
- Several Architecture children remain semantically pending even though their structural routes
  are now complete.
