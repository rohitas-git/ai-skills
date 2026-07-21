---
name: 0-ui-ux
description: >
  Domain hub for UI/UX design intelligence, brand, tokens, styling, creative assets,
  banners, slides. Use when routing visual design / UI craft (F-UI1). Not for: implement feature tickets
  (0-implement), office file formats (0-office). Hub: /0-ui-ux. Triggers: UI, UX, design system, brand, banner.
disable-model-invocation: true
metadata:
  catalog:
    hub: 0-ui-ux
    role: hub
    when:
      - "UI/UX design routing"
      - "brand/tokens/styling/creative"
    not_when:
      - "ship tickets → 0-implement"
      - "docx/xlsx files → 0-office"
    next: [1-ui-ux-pro-max, 1-design, 1-frontend-ui-engineering]
    triggers:
      - "UI"
      - "UX"
      - "design system"
      - "brand"
      - "banner"
      - "F-UI1"
    requires_setup: false
---

# UI/UX (hub)

★ **Domain hub** for visual design and UI craft. You **route** to a leaf skill; you do not replace it.

## Boundary

| Need | Skill |
|------|--------|
| Route UI/UX work | **this hub** (`/0-ui-ux`) |
| Design intelligence (styles, palettes, UX DB) | `/1-ui-ux-pro-max` |
| Brand voice / identity | `/1-brand` |
| Design tokens / specs | `/1-design-system` |
| shadcn + Tailwind implement | `/1-ui-styling` |
| Logo / CIP / icons / social creative | `/1-design` |
| Banners / ads / heroes | `/1-banner-design` |
| Strategic HTML presentations | `/1-slides` |
| Production a11y UI engineering | `/1-frontend-ui-engineering` (Ship dual) |
| Product requirements grilling | `/0-grilling` (not this hub) |
| Office PowerPoint | `/1-pptx` (office) |

## Leaves

| Intent | Skill |
|--------|--------|
| Styles, colors, typography, UX guidelines, stack UI rules | `/1-ui-ux-pro-max` |
| Brand voice, visual identity, messaging | `/1-brand` |
| Primitive → semantic → component tokens | `/1-design-system` |
| shadcn/ui + Tailwind UI code | `/1-ui-styling` |
| Logo, CIP, icons, social photos | `/1-design` |
| Platform banners | `/1-banner-design` |
| HTML pitch decks / Chart.js slides | `/1-slides` |
| A11y-first production UI hardening | `/1-frontend-ui-engineering` |

## Process

1. Infer leaf from utterance (palette, brand, tokens, shadcn, logo, banner, HTML deck, a11y).
2. If **ambiguous** → **F-UI1** (ask once):

   > What kind of UI/UX work?  
   > **Recommended:** design intelligence for app/web UI → `/1-ui-ux-pro-max`  
   > Options: design intelligence · brand · tokens · shadcn/tailwind · creative (logo/CIP/icons) · banners · HTML slides · production a11y UI · **Agent judgment**

3. Load the **leaf** skill and follow it end-to-end.
4. After design system exists, implement via `/1-ui-styling` or Ship `/0-implement` + `/1-frontend-ui-engineering` as needed.
5. Catalog placement of new UI/UX tools → `/0-skill-manager` place under hub `0-ui-ux`.

## Don't use when

- Product plan / requirements stress-test → `/0-grilling`  
- Engineering ship path without visual design ask → `/0-implement`  
- Office Word/PPTX/xlsx only → `/0-office`  
- “Which skill for coding?” → `/0-butler`
