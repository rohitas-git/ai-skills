# Butler wiring audit

Date: 2026-09-11  
Skill: `0-butler`  
Status: reviewed; final catalog sweep pending

## Evidence boundary

Reviewed Butler's complete live package, domain flow map, generated route index,
hub workflow/HTML, hub manifest, all declared child groups, shortcut/fork behavior,
route-index generator, and routing regressions. Child skill behavior remains
subject to each child's individual audit. No selected workflow, consumer repo,
worktree, external service, catalog installation/sync, commit, push, or merge was
executed during this audit.

## Decisions and changes

- Narrowed Butler to explicit catalog routing plus requests that are ambiguous,
  cross-domain, or lack one obvious direct skill. A clear direct-skill request now
  bypasses Butler and, within Butler, bypasses parent-hub invocation while still
  reporting the owning domain.
- Expanded `metadata.catalog.next` from three entries to the complete 32-skill
  union of workflow children. Manifest domain hubs, workflow routing children,
  domain_hubs_routed, metadata exits, HTML links, and flows now have regression
  parity.
- Made F7 conditional on a material remaining domain choice and removed the
  arbitrary “Feature → Design” default. The recommendation must follow request
  evidence; direct matches and non-material forks do not ask.
- Removed the obsolete Setup F1 detour. Missing optional `docs/agents/` files no
  longer override a direct task route; Setup is selected only for configuration work.
- Required validation against the live selected `SKILL.md`, which outranks stale
  projections. When no reusable skill is necessary, Butler says so; a missing
  capability is not created or ingested automatically.
- Declared routing read-only and worktree-inapplicable. Optional repository evidence
  is pinned and read-only; Butler never executes the selected skill or performs
  catalog writes, lint, install, sync, external calls, planning, or task mutation.
- Preserved the exact `??` versus `???` boundary and made explicit orientation opt-in
  rather than an automatic session-start action.
- Corrected Butler hub and manifest relative paths, current skill identity, F7 and
  product-path projections, and missing action-first/caveman/personal child entries.
- Hardened route-index truncation to stop at readable token boundaries instead of
  creating fake handoffs such as `1-session-skil`.

## Verification

- `python3 -m unittest scripts.test-routing.RoutingTests scripts.test-routing.ButlerRouteTests`:
  **14 tests passed**.
- `python3 -m unittest scripts/test-routing.py`: **192 tests passed**.
- `scripts/generate-route-index`: generated **215 skill rows**.
- `scripts/lint-skills`: **Gate PASS**, 0 critical, 0 warnings, 61 informational
  findings, and 0 hub-member orphans.
- `git diff --check`: passed.

## Remaining limits

- Butler route parity does not prove every child route is semantically correct;
  those remaining individual audits and final cross-catalog reconciliation continue.
- A generated index can become stale after later edits, so selected live skill files
  remain authoritative by design.
- Catalog-wide completion remains pending; this is individual review 64 of 215.
