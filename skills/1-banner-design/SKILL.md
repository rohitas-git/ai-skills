---
name: 1-banner-design
description: >
  Design banners for social media, ads, website heroes, creative assets, and print.
  Multiple art direction options with AI-generated visuals. Actions: design, create,
  generate banner. Platforms: Facebook, Twitter/X, LinkedIn, YouTube, Instagram, Google
  Display, website hero, print. Styles: minimalist, gradient, bold typography,
  photo-based, illustrated, geometric, retro, glassmorphism, 3D, neon, duotone,
  editorial, collage. Uses ui-ux-pro-max, frontend-design, ai-artist, ai-multimodal
  skills. Use when: Design banners for social media, ads, website heroes, creative
  assets, and print. Hub: /0-ui-ux.
disable-model-invocation: true
argument-hint: "[platform] [style] [dimensions]"
license: MIT
metadata:
  author: claudekit
  version: "1.0.0"
  catalog:
    hub: 0-ui-ux
    role: leaf
    when:
      - "Design banners for social media, ads, website heroes, creative assets, and print"
    triggers:
      - "1-banner-design"
      - "banner design"
    requires_setup: false
---
# Banner Design

Lean catalog skill. **Full body:** [references/full-guide.md](./references/full-guide.md).
Vendor pointer: [references/vendor-source.md](./references/vendor-source.md).

Social, ads, web heroes, print banners with multi-style art direction.

## Boundary

| Need | Skill |
|------|--------|
| Social/ads/web/print banners | **this skill** |
| Broader creative (logo/CIP) | `/1-design` |
| Brand context | `/1-brand` |
| Domain hub | `/0-ui-ux` |

**Hub:** `/0-ui-ux` · **Fork:** F-UI1 when ambiguous.

## Process

1. Gather purpose, platform, content, brand, style, quantity.
2. Use size/style reference; design HTML/CSS then export at exact px.
3. Present options side-by-side; iterate once.

## Hard rules

- Prefer evidence and small reversible steps.
- Do not invent design tokens or stack defaults — detect stack or ask.
- When overlapping another skill, load the specialist (Boundary table).
- Scripts/data live under this skill directory; invoke by skill-relative path.

## Related

- Hub `/0-ui-ux` · creative `/1-design` · brand `/1-brand`


## Progressive disclosure

Load only when the current branch needs depth:

| Load when | File |
|-----------|------|
| banner sizes and styles | [references/banner-sizes-and-styles.md](./references/banner-sizes-and-styles.md) |
