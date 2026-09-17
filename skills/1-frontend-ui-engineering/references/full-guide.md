# Frontend UI engineering operative guide

Use only after the main skill fixes the surface, candidate, user/task, support matrix, repository
rules, and authority. The complete upstream snapshot remains at
`archive/vendor/agent-skills/skills/frontend-ui-engineering/SKILL.md`. Its React/Tailwind examples,
fixed file layout, prop-depth and component-line thresholds, fixed breakpoints, and mandatory state/
tool choices are examples or historical source material, not portable instructions.

## Surface contract

Record a compact ledger before editing:

| Concern | Current evidence | Required behavior | Verification |
|---|---|---|---|
| user task and boundary | route/component + caller | exact entry, action, result, recovery | focused runtime path |
| states | current UI/API contract | applicable state transitions | deterministic fixtures or controlled responses |
| accessibility | product/legal target + semantics | criteria affected by this surface | keyboard, tree/screen reader, automated supplement |
| layout/content | support matrix + real content | reflow, hierarchy, localization, motion | representative viewport/state renders |
| performance | measured issue or budget | bounded rendering/network claim | trace/profile/network evidence |

## Architecture and state

- Follow the framework and directory conventions already present. Colocation, containers,
  presentation splits, hooks, stores, and server components are contextual patterns.
- Prefer one source of truth. Derive values instead of synchronizing duplicate state; persist in
  URL, server, form, or client state only when the user behavior requires it.
- Keep data loading, cancellation, retry, optimistic updates, and error recovery consistent with
  the repository. Optimism is appropriate only when failure can be reversed and communicated.
- Split a component when responsibilities, ownership, testing seams, reuse, or change patterns
  justify it—not at a universal line count. Passing props through several levels is not by itself
  proof that global context or a store is better.
- Avoid accidental client waterfalls and blocking work; measure before adding memoization,
  virtualization, caches, or complex state machinery.

## Interaction and accessibility

- Start with native elements and DOM order. Accessible names, labels, descriptions, states,
  errors, and relationships must survive the actual framework rendering.
- Keyboard behavior follows the element or recognized widget pattern. Focus moves only for a
  user/task reason, remains visible, is not trapped unintentionally, and returns appropriately
  after transient UI closes.
- Announce asynchronous changes when they are not otherwise exposed; avoid noisy live regions.
- Images need a text alternative when meaningful and an empty alternative when decorative.
  Names need not always be visible, but visible labels usually improve usability and should be
  programmatically associated when present.
- Heading and landmark structure should describe the document or embedded surface. Neither
  “exactly one H1” nor “never skip a visual level” is a universal conformance rule.
- Contrast, reflow/zoom, target size, timing, motion, media, and error requirements depend on the
  declared WCAG/platform/project target. Use the applicable criterion, not copied folklore.

## Visual and responsive fit

- Product content hierarchy, brand rules, tokens, primitives, and established spacing/type scales
  outrank generic anti-AI aesthetics.
- Use representative short, long, localized, empty, error, and permission-constrained content.
- Preserve logical order when layout changes. Test where the composition actually changes and at
  supported extremes; fixed 320/768/1024/1440 checks are not inherently sufficient.
- Avoid clipping, overlap, unreadable density, distorted media, invisible focus, hover-only
  disclosure, and motion that ignores user preference.
- A new visual direction, token, reusable primitive, or broad polish pass is a specialist decision,
  not incidental cleanup in a bounded implementation.

## Verification

Pin evidence to repository/worktree/HEAD, route, user role/data fixture, viewport/input, and fresh
run. Start with existing local checks, then use the narrowest authorized runtime path:

- render every changed/applicable state, including a safe error/recovery path;
- traverse primary and destructive actions with keyboard and pointer/touch where supported;
- inspect focus order/return/visibility and relevant accessibility tree or screen-reader output;
- inspect console errors, failed/duplicate requests, hydration/state warnings, and actual navigation;
- check reflow/zoom, long/localized content, reduced motion, and representative widths;
- use repository-installed automated accessibility tooling as a supplement and review each result.

Do not install tools or start a shared service just to satisfy the checklist. If runtime access,
credentials, fixtures, browser permissions, or an owned port are unavailable, report the exact
check as BLOCKED/SKIPPED. A screenshot proves appearance at one state and viewport; it does not
prove interaction or accessibility.

Return to Ship or UI/UX with the same scope, candidate, workspace, and authority. Do not continue
into redesign, design-system creation, publishing, or deployment automatically.
