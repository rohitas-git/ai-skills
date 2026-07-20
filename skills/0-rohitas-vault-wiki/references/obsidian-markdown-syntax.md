# Obsidian Flavored Markdown Syntax Guide

This reference teaches the agent to create and edit notes using **Obsidian Flavored Markdown** — the extended syntax that makes Obsidian powerful for PKM. It covers wikilinks, embeds, callouts, properties (frontmatter), tags, and other extensions. Standard Markdown (headings, lists, bold, tables, code blocks, etc.) is assumed knowledge.

**Core Workflow for Any New or Edited Note**
1. Start with YAML frontmatter (properties) for metadata.
2. Write clear, structured content.
3. Add `[[wikilinks]]` liberally to connect ideas.
4. Use embeds `![[ ]]` for inline inclusion of other notes or media.
5. Use callouts `> [!type]` for highlighted/important information.
6. Verify it renders beautifully in Obsidian's Reading view and supports the Graph view.

**Important rule**: Use `[[wikilinks]]` for notes *inside* the vault (Obsidian auto-updates them on rename). Use regular Markdown links `[text](url)` only for external websites.

## Wikilinks (Internal Links)

Wikilinks are the heart of Obsidian's bidirectional linking and graph.

```markdown
[[Note Name]]                          # Basic link to a note
[[Note Name|Display Text]]             # Custom display text (alias)
[[Note Name#Heading]]                  # Link to a specific heading
[[Note Name#^block-id]]                # Link to a specific block
[[#Heading in current note]]           # Link to heading in same note
```

**Block references** — append `^block-id` to a paragraph or after a block:

```markdown
This important paragraph can be referenced from elsewhere. ^key-insight

> A quoted insight worth linking to.
^quote-block
```

Then link with `[[Source Note#^key-insight]]`.

## Embeds

Prefix any wikilink with `!` to embed (inline) its content:

```markdown
![[Note Name]]                         # Embed entire note
![[Note Name#Heading]]                 # Embed just a section
![[image.png]]                         # Embed image from vault
![[image.png|300]]                     # Embed with custom width (pixels)
![[document.pdf]]                      # Embed PDF (first page)
![[document.pdf#page=3]]               # Specific page of PDF
![[audio.mp3]]                         # Embed audio player
![[video.mp4]]                         # Embed video player
```

Embeds are powerful for transclusion — e.g., embedding a "Key Definitions" section into many notes.

## Callouts (Admonitions / Highlight Boxes)

Use for warnings, tips, important notes, FAQs, etc. They support nesting and custom titles.

Basic:
```markdown
> [!note]
> This is a note callout.
```

With custom title and collapsed state:
```markdown
> [!warning] Important Security Update
> All users must enable MFA before next week.

> [!faq]- What is a Map of Content?
> A Map of Content (MOC) is a note that links to and organizes related notes.
> (The `-` makes it collapsed by default; use `+` for expanded.)
```

Common types: `note`, `abstract`, `info`, `tip`, `success`, `question`, `warning`, `danger`, `bug`, `example`, `quote`, `todo`.

You can nest callouts and combine with other syntax.

## Properties (YAML Frontmatter)

Always place at the very top of the note (between `---` delimiters). Properties power search, Bases (databases), templates, and queries.

```yaml
---
title: My Note Title
aliases:
  - Alternative Name
  - Another Alias
tags:
  - project/alpha
  - active
  - #idea
status: in-progress
created: 2026-07-19
updated: 2026-07-19
priority: high
related:
  - [[Another Note]]
cssclasses:
  - wide
---
```

**Key properties**:
- `title`: Explicit title (useful when filename differs).
- `aliases`: Alternative names for link autocomplete and renaming.
- `tags`: Array or comma-separated; support nested tags with `/` (e.g., `project/alpha`).
- `created` / `updated`: ISO dates for sorting and queries.
- `status`, `priority`, `type`, `project`: Custom fields you define for your system.
- `cssclasses`: For custom styling.

Tags can also be written inline in the note body with `#tag` or `#nested/tag`.

## Other Useful Obsidian Syntax

- **Highlights**: `==highlighted text==`
- **Comments** (hidden in Reading view): `%% hidden comment %%` or block comments.
- **Math (LaTeX)**: Inline `$E = mc^2$` or display `$$ ... $$`
- **Mermaid diagrams**:
  ```mermaid
  graph TD
      A --> B
  ```
  Add `class NodeName internal-link;` to make nodes clickable to notes.
- **Footnotes**: `Text with footnote[^1]` and `[^1]: Definition.`
- **Inline footnotes**: `Text.^[Inline note here.]`

## Complete Example Note

```markdown
---
title: Project Phoenix Planning
aliases:
  - Phoenix Initiative
tags:
  - project/phoenix
  - planning
  - active
status: in-progress
created: 2026-07-10
updated: 2026-07-19
priority: high
---

# Project Phoenix Planning

## Overview
This initiative aims to [[improve-knowledge-workflow]] by adopting modern PKM practices in [[Obsidian]].

> [!important] Key Milestone
> First working 1-prototype due ==August 15th==.

## Goals
- [x] Define core principles
- [ ] Build initial MOC structure
- [ ] Migrate key notes from old system

## Key Insights
The biggest win comes from consistent [[wikilinks]] and well-maintained [[Maps of Content]].

See detailed architecture in ![[System Architecture#Core Components]].

Reviewed during [[2026-07-18 Meeting Notes#Decisions]].

%% Internal note: Check with team on resource allocation %%
```

## Best Practices & Nuances
- **Link early and often**: Even if a target note doesn't exist yet, create the `[[wikilink]]` — Obsidian will offer to create it.
- **Use aliases** for long or technical note names to keep prose readable.
- **Block IDs** are excellent for referencing specific paragraphs or quotes across notes.
- **Properties first**: Always define frontmatter before writing body content.
- **Callouts for signal**: Use them to make important information stand out in Reading view and Graph.
- **Embeds for DRY**: Embed shared sections (definitions, templates, checklists) instead of copying.
- **Test in Obsidian**: After editing, open the note in Obsidian to confirm rendering, link resolution, and graph appearance.

This syntax mastery ensures every note you create or edit integrates seamlessly with Obsidian's powerful features (Graph View, Backlinks, Search, Bases, Canvas, etc.). 

For even more detail on specific areas, dedicated sub-references (Properties, Embeds, Callouts) can be added later from official sources.