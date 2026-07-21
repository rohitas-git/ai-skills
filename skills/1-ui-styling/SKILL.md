---
name: 1-ui-styling
description: >
  Create beautiful, accessible user interfaces with shadcn/ui components (built on Radix
  UI + Tailwind), Tailwind CSS utility-first styling, and canvas-based visual designs.
  Use when building user interfaces, implementing design systems, creating responsive
  layouts, adding accessible components (dialogs, dropdowns, forms, tables), customizing
  themes and colors, implementing dark mode, generating visual designs and posters, or
  establishing consistent styling patterns across applications. Hub: /0-ui-ux.
disable-model-invocation: true
argument-hint: "[component or layout]"
license: MIT
metadata:
  author: claudekit
  version: "1.0.0"
  catalog:
    hub: 0-ui-ux
    role: leaf
    when:
      - "building user interfaces, implementing design systems, creating responsive layouts, adding accessibl"
    triggers:
      - "1-ui-styling"
      - "ui styling"
    requires_setup: false
---
# UI Styling

Lean catalog skill. **Full body:** [references/full-guide.md](./references/full-guide.md).
Vendor pointer: [references/vendor-source.md](./references/vendor-source.md).

shadcn/ui + Tailwind (+ canvas design system) implementation skill.

## Boundary

| Need | Skill |
|------|--------|
| shadcn/ui + Tailwind styling | **this skill** |
| A11y / production UI engineering | `/1-frontend-ui-engineering` |
| Design intelligence | `/1-ui-ux-pro-max` |
| Tokens | `/1-design-system` |
| Domain hub | `/0-ui-ux` |

**Hub:** `/0-ui-ux` · **Fork:** F-UI1 when ambiguous.

## Process

1. Confirm stack (React/Next + Tailwind); init shadcn if needed.
2. Compose accessible primitives; utility-first Tailwind; dark mode consistently.
3. Use `references/` for components, theming, a11y, responsive, canvas.
4. For production a11y hardening beyond styling, load `/1-frontend-ui-engineering`.

## Hard rules

- Prefer evidence and small reversible steps.
- Do not invent design tokens or stack defaults — detect stack or ask.
- When overlapping another skill, load the specialist (Boundary table).
- Scripts/data live under this skill directory; invoke by skill-relative path.

## Related

- Hub `/0-ui-ux` · design intel `/1-ui-ux-pro-max` · tokens `/1-design-system`


## Progressive disclosure

Load only when the current branch needs depth:

| Load when | File |
|-----------|------|
| canvas design system | [references/canvas-design-system.md](./references/canvas-design-system.md) |
| shadcn accessibility | [references/shadcn-accessibility.md](./references/shadcn-accessibility.md) |
| shadcn components | [references/shadcn-components.md](./references/shadcn-components.md) |
| shadcn theming | [references/shadcn-theming.md](./references/shadcn-theming.md) |
| tailwind customization | [references/tailwind-customization.md](./references/tailwind-customization.md) |
| tailwind responsive | [references/tailwind-responsive.md](./references/tailwind-responsive.md) |
| tailwind utilities | [references/tailwind-utilities.md](./references/tailwind-utilities.md) |
