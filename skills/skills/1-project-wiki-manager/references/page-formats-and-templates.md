# Page Formats and Templates

## Rationale
Consistent page structure makes the wiki predictable for both the agent and human readers. Every page answers the same basic questions ("What is this?", "Where did this come from?", "When was it last touched?") and provides clear navigation via related links. This reduces cognitive load and enables reliable automated linting or future tooling.

## Standard Wiki Page Template (Every .md file except index.md and log.md)

```markdown
# Page Title

**Summary**: One or two sentences capturing the essence of this concept or source.

**Sources**: 
- `exact-raw-filename.ext` (sections X–Y or pages p. A–B)
- `another-source.md` (if merged)

**Last updated**: YYYY-MM-DD

---

## Overview
(Short prose introduction. Use headings liberally for scannability.)

## Key Concepts / Details
(Use bullet lists, numbered steps, or sub-headings. Include inline `[[wiki-links]]` to related pages.)

## Known Issues or Open Questions
(Explicitly call out contradictions, uncertainties, or items needing verification.)

## Related Pages
- [[related-concept-1]] — brief reason for connection
- [[related-concept-2]] — brief reason for connection
```

### Required Elements Explained
- **Summary**: Forces the author (agent) to distill. Readers get instant orientation.
- **Sources**: Non-negotiable for traceability. Use exact original filenames from `docs/raw/`.
- **Last updated**: Simple date stamp; update on every meaningful change.
- **Wiki-links**: Use the exact `[[kebab-case-page-name]]` syntax (no .md extension). These create the graph of knowledge.
- **Headings**: Start with `##` after the frontmatter block. Use `###` for subsections. Avoid `####` unless truly necessary for very complex pages.

## Index Page Format (`docs/wiki/index.md`)

The index is a categorized Markdown table that serves as the primary discovery mechanism.

```markdown
# Wiki Index

## Project Overview
| Page | Description | Sources |
|------|-------------|---------|
| [[project-vision]] | Core goals and success criteria for the initiative | vision-deck-2026.pdf |
| [[stakeholder-requirements]] | Consolidated needs from all parties | requirements-v2.pdf, stakeholder-interviews.md |

## Core Concepts
| Page | Description | Sources |
|------|-------------|---------|
| [[knowledge-compounding]] | How the wiki itself grows and maintains signal over time | (synthesized) |

## Sources
| Page | Description | Sources |
|------|-------------|---------|
| [[requirements-v2]] | Summary and extraction from the v2 requirements document | requirements-v2.pdf |
```

### Index Rules
- Use clear, alphabetical category headings (## Category Name).
- Keep descriptions to one line.
- The "Sources" column lists the primary raw file(s) that feed the page.
- For purely synthesized pages (no single raw source), note "(synthesized from multiple wiki pages)" or similar.
- Rebuild or update the table after every ingest or significant edit. Sort rows alphabetically within each category.
- Add new categories only when the number of pages in an existing category becomes unwieldy (roughly >12–15 pages).

## Log Page Format (`docs/wiki/log.md`)

Append-only history. Never edit past entries.

```
# Wiki Operation Log

## 2026-07-19 | requirements-v2.pdf | Added source summary + 7 concept pages (user confirmed takeaways) | Updated index and log
<!-- END OF LOG -->
```

- Always append **above** the sentinel `<!-- END OF LOG -->`.
- Use the exact format: `## YYYY-MM-DD | source-or-action | summary of changes | pages affected`
- The sentinel enables reliable mechanical appends without parsing the entire file.

## Nuances and Quality Guidelines
- **Page naming**: Always `lowercase-with-hyphens.md`. Never use spaces, underscores, or camelCase. Source-derived pages should closely match the raw filename slug.
- **Length**: Aim for focused pages. If a page grows beyond ~800–1000 words, consider splitting into sub-concepts and linking.
- **Tone**: Plain, precise English. Avoid jargon unless the source uses it; then define on first use or link to a glossary-style page.
- **Visuals**: When a source contains diagrams, tables, or screenshots, describe their content and purpose in prose. Add a note: "Key visual elements from original: ... (see raw/filename.ext for the diagram itself)".
- **Empty sections**: Omit "Known Issues" or "Related Pages" if genuinely empty, but prefer to include at least 1–2 related links for connectivity.
- **Implications of inconsistent formatting**: Inconsistent pages make the wiki feel unprofessional, break future automation (e.g., link checkers), and increase reader friction. Strict adherence compounds into a high-quality corpus over months and years.

## Template Usage During Creation
When creating a new page, copy the template exactly, fill in the frontmatter first, then write content, then add related links last (after you know what other pages exist or were just created). This order prevents dangling or incorrect links.