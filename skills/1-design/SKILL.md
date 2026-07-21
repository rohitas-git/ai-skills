---
name: 1-design
description: >
  Comprehensive design skill: brand identity, design tokens, UI styling, logo generation
  (55 styles, Gemini AI), corporate identity program (50 deliverables, CIP mockups),
  HTML presentations (Chart.js), banner design (22 styles, social/ads/web/print), icon
  design (15 styles, SVG, Gemini 3.1 Pro), social photos (HTML→screenshot,
  multi-platform). Actions: design logo, create CIP, generate mockups, build slides,
  design banner, generate icon, create social photos, social media images, brand
  identity, design system. Platforms: Facebook, Twitter, LinkedIn, YouTube, Instagram,
  Pinterest, TikTok, Threads, Google Ads. Use when: Comprehensive design skill: brand
  identity, design tokens, UI styling, logo generation (55 styles, G. Hub: /0-ui-ux.
disable-model-invocation: true
argument-hint: "[design-type] [context]"
license: MIT
metadata:
  author: claudekit
  version: "2.1.0"
  catalog:
    hub: 0-ui-ux
    role: leaf
    when:
      - "Comprehensive design skill: brand identity, design tokens, UI styling, logo generation (55 styles, G"
    triggers:
      - "1-design"
      - "design"
    requires_setup: false
---
# Design (creative)

Lean catalog skill. **Full body:** [references/full-guide.md](./references/full-guide.md).
Vendor pointer: [references/vendor-source.md](./references/vendor-source.md).

Logo, CIP, icons, banners, social photos — creative package router.

## Boundary

| Need | Skill |
|------|--------|
| Logo / CIP / icons / creative package | **this skill** |
| Brand voice only | `/1-brand` |
| Design tokens only | `/1-design-system` |
| App UI intelligence DB | `/1-ui-ux-pro-max` |
| HTML pitch decks | `/1-slides` |
| Office PowerPoint | `/1-pptx` |
| Domain hub | `/0-ui-ux` |

**Hub:** `/0-ui-ux` · **Fork:** F-UI1 when ambiguous.

## Process

1. Pick sub-route: logo · CIP · icon · banner · social photo · (or defer brand/tokens/ui-styling to peers).
2. Load the matching references under this skill; run scripts under `scripts/`.
3. Keep brand voice via `/1-brand` and tokens via `/1-design-system` when needed.
4. For app UI intelligence (not logo/CIP), use `/1-ui-ux-pro-max` instead.

## Hard rules

- Prefer evidence and small reversible steps.
- Do not invent design tokens or stack defaults — detect stack or ask.
- When overlapping another skill, load the specialist (Boundary table).
- Scripts/data live under this skill directory; invoke by skill-relative path.

## Related

- Hub `/0-ui-ux` · peers `/1-brand`, `/1-design-system`, `/1-banner-design`, `/1-slides`


## Progressive disclosure

Load only when the current branch needs depth:

| Load when | File |
|-----------|------|
| banner sizes and styles | [references/banner-sizes-and-styles.md](./references/banner-sizes-and-styles.md) |
| cip deliverable guide | [references/cip-deliverable-guide.md](./references/cip-deliverable-guide.md) |
| cip design | [references/cip-design.md](./references/cip-design.md) |
| cip prompt engineering | [references/cip-prompt-engineering.md](./references/cip-prompt-engineering.md) |
| cip style guide | [references/cip-style-guide.md](./references/cip-style-guide.md) |
| design routing | [references/design-routing.md](./references/design-routing.md) |
| icon design | [references/icon-design.md](./references/icon-design.md) |
| logo color psychology | [references/logo-color-psychology.md](./references/logo-color-psychology.md) |
| logo design | [references/logo-design.md](./references/logo-design.md) |
| logo prompt engineering | [references/logo-prompt-engineering.md](./references/logo-prompt-engineering.md) |
| logo style guide | [references/logo-style-guide.md](./references/logo-style-guide.md) |
| slides copywriting formulas | [references/slides-copywriting-formulas.md](./references/slides-copywriting-formulas.md) |
| slides create | [references/slides-create.md](./references/slides-create.md) |
| slides html template | [references/slides-html-template.md](./references/slides-html-template.md) |
| slides layout patterns | [references/slides-layout-patterns.md](./references/slides-layout-patterns.md) |
| slides strategies | [references/slides-strategies.md](./references/slides-strategies.md) |
| slides | [references/slides.md](./references/slides.md) |
| social photos design | [references/social-photos-design.md](./references/social-photos-design.md) |
