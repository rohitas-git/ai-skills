---
name: 1-ui-ux-pro-max
description: >
  UI/UX design intelligence for web and mobile. Searchable local database with 84
  styles, 192 color palettes, 74 font pairings, 192 product types, 98 UX guidelines, 104
  icon entries, 16 GSAP motion presets, and 25 chart types across 22 stacks (React,
  Next.js, Vue, Nuxt, Svelte, Astro, SwiftUI, React Native, Flutter, Tailwind,
  shadcn/ui, Jetpack Compose, Angular, Laravel, JavaFX, WPF, WinUI, Avalonia, Uno
  Platform, UWP, Three.js, and HTML/CSS). Use when designing, building, or reviewing UI:
  pages, components, color schemes, typography, layout, accessibility, animation, or
  data visualization. Hub: /0-ui-ux.
disable-model-invocation: true
metadata:
  catalog:
    hub: 0-ui-ux
    role: pipeline
    when:
      - "designing, building, or reviewing UI: pages, components, color schemes, typography, layout, accessib"
    triggers:
      - "1-ui-ux-pro-max"
      - "ui ux pro max"
    requires_setup: false
---
# UI/UX Pro Max

Lean catalog skill. **Full body:** [references/full-guide.md](./references/full-guide.md).
Vendor pointer: [references/vendor-source.md](./references/vendor-source.md).

Searchable design-intelligence DB (styles, palettes, typography, UX, stacks).

## Boundary

| Need | Skill |
|------|--------|
| Design intelligence (styles/palettes/UX DB) | **this skill** |
| Brand voice / identity | `/1-brand` |
| Tokens / specs | `/1-design-system` |
| shadcn + Tailwind implement | `/1-ui-styling` |
| Logo / CIP / icons / creative | `/1-design` |
| Production a11y UI engineering | `/1-frontend-ui-engineering` |
| Domain hub router | `/0-ui-ux` |

**Hub:** `/0-ui-ux` · **Fork:** F-UI1 when ambiguous.

## Process

1. Extract product type, audience, style keywords, and stack from the repo/request.
2. Run design-system search first (`scripts/search.py "…" --design-system`).
3. Supplement with `--domain` / `--stack` searches as needed.
4. Persist MASTER.md when the project needs a durable design system (`--persist --output-dir`).
5. Before delivery, apply `references/pro-rules.md` pre-delivery checklist.

## Hard rules

- Prefer evidence and small reversible steps.
- Do not invent design tokens or stack defaults — detect stack or ask.
- When overlapping another skill, load the specialist (Boundary table).
- Scripts/data live under this skill directory; invoke by skill-relative path.

## Related

- Hub `/0-ui-ux` · F-UI1
- Tokens `/1-design-system` · implement `/1-ui-styling` · a11y `/1-frontend-ui-engineering`


## Progressive disclosure

Load only when the current branch needs depth:

| Load when | File |
|-----------|------|
| quick reference | [references/quick-reference.md](./references/quick-reference.md) |
