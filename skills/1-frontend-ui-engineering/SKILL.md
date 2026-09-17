---
name: 1-frontend-ui-engineering
description: >
  Implement or harden one bounded user-facing interaction in the repository's frontend
  stack, including applicable states, accessibility, responsiveness, and runtime evidence.
  Use for UI components, pages, forms, or interaction defects. Not for visual direction,
  token systems, copy/brand definition, or review-only customer journeys. Primary hub:
  /0-implement; shared with /0-ui-ux.
disable-model-invocation: true
metadata:
  catalog:
    hub: 0-implement
    role: soft
    when:
      - "implementing or hardening one bounded user-facing component, page, form, or interaction"
      - "repairing applicable UI states, semantics, focus, keyboard, responsive, or runtime behavior"
    not_when:
      - "choose visual direction or UX patterns → 1-ui-ux-pro-max"
      - "define tokens or component-system contracts → 1-design-system"
      - "apply styling only within an established system → 1-ui-styling"
      - "audit an existing customer journey without editing → 1-customer-experience-audit"
      - "runtime browser verification only → 1-browser-testing-with-devtools / 1-playwright-browser-testing"
    prev: [0-implement, 0-ui-ux]
    next: [0-implement, 0-ui-ux, 1-ui-ux-pro-max, 1-design-system, 1-ui-styling, 1-brand, 1-browser-testing-with-devtools, 1-playwright-browser-testing, 1-visual-edit, 1-performance-optimization]
    cousins: [1-ui-ux-pro-max, 1-design-system, 1-ui-styling, 1-customer-experience-audit]
    triggers:
      - "1-frontend-ui-engineering"
      - "implement this UI interaction"
      - "build this accessible form"
      - "fix this responsive component"
      - "harden these loading error or empty states"
    requires_setup: false
---

# Frontend UI Engineering

Implement **one bounded interaction surface** in the repository's existing stack and visual
language. Modes are advice, read-only assessment, or authorized repository edit. Design-system
and brand decisions remain inputs or explicit specialist handoffs, not inventions by this skill.

## Boundary

| Need | Route |
|---|---|
| Build or harden concrete frontend behavior | **this skill** |
| Choose UX direction, visual style, or patterns | `/1-ui-ux-pro-max` |
| Define tokens/components as a reusable system | `/1-design-system` |
| Apply styling to an already-defined surface | `/1-ui-styling` |
| Inspect runtime behavior without editing | `/1-browser-testing-with-devtools` or `/1-playwright-browser-testing` |
| Audit the end-to-end customer experience | `/1-customer-experience-audit` |

## Input and workspace contract

Inherit caller, mode, requested user outcome and exclusions; exact repository/worktree/branch/
HEAD; owned and protected files; route/component and user role; content/data contract; existing
design/brand/accessibility/browser support rules; viewport/input matrix; local service and port
ownership; permitted dependencies/assets; and allowed local, Git, remote, and production effects.

Advice and read-only assessment create no worktree. Authorized edits reuse the caller's matching
owned worktree. Use `/1-git-worktrees` only when isolation is independently required, then return
to the original caller. A worktree does not isolate a shared browser profile, dev server, port,
database, generated asset, or external design service.

## Process

1. **Pin the surface.** State the user task, route/component, entry and exit, affected roles,
   acceptance behavior, explicit non-goals, exact candidate, and applicable browser/input/viewport
   support. Do not turn a component fix into a page or product redesign.
2. **Inspect before designing.** Read repository instructions, nearby implementations, primitives,
   tokens, content/brand rules, data/API contract, tests, and current rendered behavior when
   available. Reuse established semantics and components when they fit; do not add a framework,
   UI kit, state library, font, icon pack, or testing tool without authority.
3. **Write the interaction-state contract.** Cover only applicable default, loading/pending,
   empty, partial, success, validation/error, disabled, permission/auth, offline/retry, and
   destructive-confirmation states. Record focus, keyboard/pointer/touch, announcement, navigation,
   persistence, and recovery behavior; do not invent unavailable product requirements.
4. **Implement semantics first.** Prefer native elements and platform behavior. Preserve accessible
   names, relationships, landmarks/headings appropriate to context, focus order/visibility/return,
   input purpose, error association, status announcements, and non-color cues. Custom widgets must
   implement the relevant interaction pattern, not merely add an ARIA role.
5. **Fit the codebase.** Put state at the narrowest stable owner, preserve server/client and data-
   fetching boundaries, avoid duplicate sources of truth and accidental request waterfalls, and
   keep component seams cohesive. No numeric prop-depth or line-count rule replaces evidence.
6. **Fit content and layout.** Use real representative content and project tokens; preserve logical
   reading order, zoom/reflow, localization/long text, reduced motion, media proportions, and
   target sizes appropriate to the applicable standard and platform. Choose representative
   viewports from support evidence rather than a universal breakpoint list.
7. **Verify the actual candidate.** Run repository checks, then render the affected states and
   exercise supported keyboard/pointer/touch paths at representative viewports. Inspect console/
   network, focus, accessibility tree or screen-reader behavior where material, and screenshots
   or DOM/runtime evidence. Automated accessibility checks supplement—not prove—conformance.
   Browser/service starts require owned ports/state; report unavailable checks honestly.
8. **Return.** Provide caller, candidate/worktree, changed paths, interaction-state disposition,
   checks with PASS/FAIL/BLOCKED/SKIPPED and evidence identity, rendered defects repaired, residual
   accessibility/visual/runtime risk, and any narrowly scoped specialist follow-up.

## Hard rules

- Repository and product brand/design rules outrank generic style advice.
- Never claim accessibility conformance from markup inspection or an automated scan alone.
- Do not commit, push, merge, install tools, start unowned shared services, upload assets/data,
  publish previews, deploy, or mutate remote/production state without separate authority.

## References

- Operative: [implementation guide](./references/full-guide.md), [accessibility checklist](./references/accessibility-checklist.md), [anti-slop scope guard](./references/anti-ui-slop.md)
- Provenance: [vendor source](./references/vendor-source.md)
