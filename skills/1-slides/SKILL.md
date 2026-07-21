---
name: 1-slides
description: >
  Create strategic HTML presentations with Chart.js, design tokens, responsive layouts,
  copywriting formulas, and contextual slide strategies. Use when: Create strategic HTML
  presentations with Chart.js, design tokens, responsive layouts, copywriting fo. Hub:
  /0-ui-ux.
disable-model-invocation: true
argument-hint: "[topic] [slide-count]"
metadata:
  author: claudekit
  version: "1.0.0"
  catalog:
    hub: 0-ui-ux
    role: leaf
    when:
      - "Create strategic HTML presentations with Chart.js, design tokens, responsive layouts, copywriting fo"
    triggers:
      - "1-slides"
      - "slides"
    requires_setup: false
---

# Slides

## Process

1. Follow the steps and hard rules in this skill.
2. Load linked `references/` only when the branch needs them.


## Boundary

| Need | Skill |
|------|--------|
| Strategic **HTML** presentations (Chart.js / tokens) | **this skill** |
| PowerPoint `.pptx` office artifact | `/1-pptx` (office hub) |
| Design tokens for slides | `/1-design-system` |
| Domain hub | `/0-ui-ux` |

**Hub:** `/0-ui-ux` · Do not use this for Office PPTX — use `/1-pptx`.

Vendor pointer: [references/vendor-source.md](./references/vendor-source.md).

Strategic HTML presentation design with data visualization.

## When to Use

- Marketing presentations and pitch decks
- Data-driven slides with Chart.js
- Strategic slide design with layout patterns
- Copywriting-optimized presentation content

## Subcommands

| Subcommand | Description | Reference |
|------------|-------------|-----------|
| `create` | Create strategic presentation slides | `references/create.md` |

## References (Knowledge Base)

| Topic | File |
|-------|------|
| Layout Patterns | `references/layout-patterns.md` |
| HTML Template | `references/html-template.md` |
| Copywriting Formulas | `references/copywriting-formulas.md` |
| Slide Strategies | `references/slide-strategies.md` |

## Routing

1. Parse subcommand from `$ARGUMENTS` (first word)
2. Load corresponding `references/{subcommand}.md`
3. Execute with remaining arguments


## Related

**Next:** `/0-ui-ux`. Parent hub: `/0-ui-ux`.
