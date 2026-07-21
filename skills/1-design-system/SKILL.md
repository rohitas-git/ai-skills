---
name: 1-design-system
description: >
  Token architecture, component specifications, and slide generation. Three-layer tokens
  (primitive→semantic→component), CSS variables, spacing/typography scales, component
  specs, strategic slide creation. Use for design tokens, systematic design,
  brand-compliant presentations. Use when: Token architecture, component specifications,
  and slide generation. Hub: /0-ui-ux.
disable-model-invocation: true
argument-hint: "[component or token]"
license: MIT
metadata:
  author: claudekit
  version: "1.0.0"
  catalog:
    hub: 0-ui-ux
    role: leaf
    when:
      - "Token architecture, component specifications, and slide generation"
    triggers:
      - "1-design-system"
      - "design system"
    requires_setup: false
---
# Design System

Lean catalog skill. **Full body:** [references/full-guide.md](./references/full-guide.md).
Vendor pointer: [references/vendor-source.md](./references/vendor-source.md).

Three-layer tokens (primitive→semantic→component), specs, slide token helpers.

## Boundary

| Need | Skill |
|------|--------|
| Tokens / component specs | **this skill** |
| Brand voice | `/1-brand` |
| Implement with shadcn/Tailwind | `/1-ui-styling` |
| Design intelligence search | `/1-ui-ux-pro-max` |
| Domain hub | `/0-ui-ux` |

**Hub:** `/0-ui-ux` · **Fork:** F-UI1 when ambiguous.

## Process

1. Clarify brand context (`/1-brand` if missing).
2. Define primitive → semantic → component tokens; prefer CSS variables.
3. Use references for architecture and Tailwind integration.
4. Hand off implementation to `/1-ui-styling` or product UI to `/1-ui-ux-pro-max`.

## Hard rules

- Prefer evidence and small reversible steps.
- Do not invent design tokens or stack defaults — detect stack or ask.
- When overlapping another skill, load the specialist (Boundary table).
- Scripts/data live under this skill directory; invoke by skill-relative path.

## Related

- Hub `/0-ui-ux` · `/1-brand` · `/1-ui-styling` · `/1-ui-ux-pro-max`


## Progressive disclosure

Load only when the current branch needs depth:

| Load when | File |
|-----------|------|
| component specs | [references/component-specs.md](./references/component-specs.md) |
| component tokens | [references/component-tokens.md](./references/component-tokens.md) |
| primitive tokens | [references/primitive-tokens.md](./references/primitive-tokens.md) |
| semantic tokens | [references/semantic-tokens.md](./references/semantic-tokens.md) |
| states and variants | [references/states-and-variants.md](./references/states-and-variants.md) |
| tailwind integration | [references/tailwind-integration.md](./references/tailwind-integration.md) |
| token architecture | [references/token-architecture.md](./references/token-architecture.md) |
