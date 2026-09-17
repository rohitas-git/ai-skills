# Butler autonomy, retrieval, app, and project-adapter wiring audit

Date: 2026-09-11  
Skills: `1-plow-ahead`, `1-rewind`, `1-webmcp`, `1-pi-agent-rust`  
Status: reviewed; final catalog sweep pending

## Evidence boundary

Reviewed all four live bodies, complete Pi Agent Rust references, complete linked
BuilderIO vendor sources, Butler membership/workflow/HTML/flow projections, metadata
handoffs, and focused regressions. Vendor material is historical. No screen memory,
browser app, external account, pi_agent_rust checkout, consumer worktree, catalog
install/sync, commit, push, or merge was touched.

## Decisions and changes

- Made Plow Ahead an explicit overlay on an already-authorized workflow. It inherits
  exact scope/candidate/worktree/dirty-state/resource authority, handles only routine
  reversible choices, and cannot turn persistence into permission, delegation, goal
  state, or destructive/external/Git action.
- Narrowed Rewind to one bounded, local, read-only memory question. Retrieval is
  privacy-minimized, screen content is untrusted evidence, multiple workstreams stay
  separate, setup/capture/upload is never implicit, and worktrees correctly provide no
  isolation for screen memory.
- Added a WebMCP operation checkout and explicit external-state boundary. Open-only,
  read, ordinary write, sign-in, high-impact effects, UI fallback, uncertain writes,
  and targeted readback now have distinct authority/evidence rules.
- Converted Pi Agent Rust from a 205-line second engineering workflow into a lean
  repository adapter. It validates the current checkout, returns surface/invariant/
  command candidates, and routes to Diagnose, Ship, Review, or CI/CD. Its recipes are
  explicitly snapshot candidates; destructive installer examples and shared absolute
  cache setup were removed.
- Marked all three BuilderIO sources historical and added Pi Agent Rust to Butler's
  flow map as the project adapter already present in workflow and HTML surfaces.

## Verification

- `python3 -m unittest scripts.test-routing.ButlerSatelliteRouteTests`: **8 passed**.
- `python3 -m unittest scripts/test-routing.py`: **214 passed**.
- `scripts/generate-route-index`: regenerated **215 skill rows**.
- `scripts/lint-skills`: **Gate PASS**, 0 critical, 0 warnings, 59 informational
  findings, and 0 hub-member orphans.
- `git diff --check`: passed.

Individual catalog reviews represented by this document are 73–76 of 215.

## Remaining limits

- No runtime connector or target repository was in scope, so operational behavior was
  not exercised; the skills require fresh target evidence when actually invoked.
- Catalog-wide semantic reconciliation remains pending.
