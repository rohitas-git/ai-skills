# Interface detail checks

Use only for a requested presentation change on an existing surface. Check the actual design system, behavior, accessibility, and viewport evidence before adopting a suggestion. No value below is universal.

- **Nested surfaces:** Compare outer and inner corner radii with their spacing. Adjust only when the relationship visibly clashes with the approved system.
- **Optical alignment:** Inspect asymmetric icons and icon-plus-label controls at their rendered size. A small visual offset may be more balanced than mathematical centering; preserve hit areas and focus visibility.
- **Depth and edges:** Choose borders, shadows, and image outlines to match the current theme and contrast. Avoid replacing borders wholesale or prescribing one opacity or color for all surfaces.
- **Typography:** Check heading wraps, orphaned short words, and changing numeral widths. Use `text-wrap` or tabular numerals when browser support and actual content make them useful.
- **Motion:** Prefer interruptible transitions for interactive state. Animate only needed properties, keep entry and exit movement restrained, honor reduced-motion preferences, and avoid permanent `will-change` hints without measured benefit.
- **Touch targets:** Check control size, spacing, and overlap at supported inputs and zoom levels. Do not treat a visual polish pass as authority to change interaction semantics.

Paraphrased from `danielabar/meblog` `.claude/skills/make-interfaces-feel-better/` at commit `0d3962332b7c07b0cb4d025d170e9f6e5c1ae292` (five-file source snapshot reviewed statically). The source credits `jakubkrehel/make-interfaces-feel-better`. Its fixed numeric and library-specific prescriptions were intentionally turned into context-dependent checks.
