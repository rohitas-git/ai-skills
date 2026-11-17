# Frontend UI engineering wiring audit

Date: 2026-09-11  
Skill: `1-frontend-ui-engineering`  
Status: reviewed; final catalog sweep pending

## Evidence boundary

Reviewed the complete live skill and every operative reference, its Ship and UI/UX parents
across bodies/workflows/HTML/flows/generated routes, neighboring UI specialist boundaries,
candidate/worktree/service authority, and routing regressions. The archived upstream remains
source material rather than operative framework policy. This audit changed skill documentation
and routing only; it did not change or render project UI, start a browser/server, install tools,
publish a preview, or claim accessibility conformance for a product.

## Decisions and changes

- Kept one atomic job: implement or harden one bounded user-facing interaction surface in the
  repository's existing frontend stack. Advice, read-only assessment, and authorized edit modes
  preserve the caller's scope.
- Corrected primary ownership to Ship (`0-implement`) while retaining UI/UX as the shared design-
  side caller. Both parent workflows/HTML/flows now describe the same candidate/worktree/authority
  return and no-redesign/no-publication boundary.
- Narrowed triggers to concrete component/page/form/interaction implementation and state,
  accessibility, or responsive defects. Visual direction, tokens/systems, styling-only work,
  customer-journey audits, and browser-verification-only work retain their specialist owners.
- Required exact repository/worktree/branch/HEAD, route/component, role/data contract, design and
  brand rules, browser/input/viewport support, local service/port ownership, asset/dependency
  permission, and allowed effects. Advice/read-only work creates no worktree; worktrees do not
  isolate browser profiles, ports, databases, generated assets, or external design services.
- Added an applicable interaction-state contract instead of requiring every possible state. It
  records focus, inputs, announcements, navigation, persistence, recovery, and explicit non-goals.
- Made native semantics and recognized widget behavior the default while avoiding ARIA-as-a-fix.
  Accessibility criteria are selected from the declared project/legal/platform target; one-H1,
  universal heading, 44-pixel, and similar folklore are not treated as blanket conformance rules.
- Replaced fixed React/Tailwind structure, three-level prop limits, 200-line component limits,
  fixed breakpoints, mandatory skeleton/optimistic patterns, and unapproved `npx` tooling with
  repository-native, evidence-based decisions.
- Required fresh runtime evidence from the exact candidate: applicable states, input paths,
  representative viewports, focus, accessibility tree/screen reader where material, console/
  network, and reflow/content behavior. Automated scans and screenshots supplement but do not
  prove interaction or accessibility.
- Preserved product rules over generic anti-AI advice and tightened the anti-slop reference to
  candidate-bound, multi-state evidence without expanding a bounded fix into a redesign.
- Replaced the 328-line framework-heavy guide and 160-line checklist with concise operative
  adaptations while keeping the full source archived.

## Verification

- `python3 -m unittest scripts.test-routing.FrontendUiEngineeringRouteTests`: **6 tests passed**.
- `python3 -m unittest scripts/test-routing.py`: **123 tests passed**.
- `scripts/generate-route-index`: generated **215 skill rows**.
- `scripts/lint-skills`: **Gate PASS**, 0 critical, 0 warnings, 64 informational findings, and
  0 hub-member orphans.
- `git diff --check`: passed.
- Regression coverage proves two-parent membership/dispatch/returns, corrected primary ownership,
  exact candidate/worktree/service authority, bounded interaction scope, applicable accessibility
  and runtime evidence, product-rule precedence, and removal of upstream framework/numeric absolutes.

## Remaining limits

- Product accessibility and visual claims still require rendering and interaction evidence from
  the exact product candidate and supported environment.
- Other Ship and UI/UX children remain pending semantic review.
