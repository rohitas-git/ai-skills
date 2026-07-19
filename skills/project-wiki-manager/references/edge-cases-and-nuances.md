# Edge Cases and Nuances

This reference captures situations that deviate from the happy path and provides guidance for maintaining wiki quality under real-world conditions.

## Multiple Sources on One Concept
When the same concept, requirement, or decision appears in several raw documents:

- Merge the information into a single authoritative concept page.
- In the "Sources" frontmatter, list every contributing raw file.
- In the body, use headings or a "Perspectives" subsection to present differing or evolving views with citations.
- Highlight any unresolved tensions.
- Implication: The concept page becomes the "single source of truth" that reconciles history. This is one of the highest-value functions of the wiki.

## Large-Impact or Foundational Ingests
A single source (e.g., a 50-page strategy document, a comprehensive requirements spec, or a research paper) can legitimately spawn 10–15 new pages plus updates to many existing ones.

- Do not treat this as a problem; it is the expected and healthy growth pattern.
- Spend extra time on high-quality `[[wiki-links]]` and accurate categorization in `index.md`.
- After such an ingest, proactively offer an audit or a "wiki tour" of the new structure.
- User confirmation of takeaways is especially important here because the blast radius is large.

## Visuals, Diagrams, Tables, and Non-Text Content
Raw sources frequently contain images, architecture diagrams, flowcharts, or data tables.

- Describe the visual in clear prose: what it shows, the key elements, relationships, and any numbers or labels.
- Add a traceability note: "See the original diagram in `raw/architecture-overview.pdf` (page 7) for the visual representation."
- If the visual is central to understanding, consider whether a textual representation (ASCII art, Mermaid diagram if supported by user tooling, or detailed bullet breakdown) adds value in the wiki page.
- Never claim to "include" the image in the wiki; the wiki remains text-first and portable.

## Uncertainty, Ambiguity, and User Disagreement
- When the agent is unsure about categorization, page granularity, or whether something merits its own page: surface the uncertainty and ask the user.
- Example: "This topic could live as its own page or as a section inside [[user-management]]. Which would you prefer?"
- If the user later changes their mind about structure, treat it as a normal evolution: update links, move content via edit, and log the change.

## Knowledge Compounding and Self-Improvement
High-quality answers to user questions often represent syntheses that do not yet exist as first-class wiki pages.

- After delivering a strong answer that draws from multiple pages or fills a gap, always offer to persist it:
  > "This explanation connects several concepts cleanly. Would you like me to create a new wiki page (or enhance an existing one) so future questions can benefit from it?"
- Accepting these offers gradually turns the wiki into a curated, high-signal resource rather than a mere dump of source summaries.
- Over months, this compounds: each good Q&A session can improve the wiki for all future sessions.

## Scalability and Wiki Growth
As the wiki grows to dozens or hundreds of pages:

- The categorized `index.md` remains the primary navigation aid; keep categories meaningful and avoid overly fine-grained ones.
- Periodic audits (see logging-and-audit.md) become more valuable.
- Consider proposing lightweight additional structure (e.g., a `decisions/` subfolder for ADRs) only when a clear pattern emerges and the user agrees.
- The flat-by-default approach plus excellent linking scales surprisingly well; many successful wikis remain largely flat for years.

## Stale or Superseded Content
- When a raw source is revised, re-ingest it and mark affected wiki pages with "Last updated" + a note that they were reviewed against the new version.
- For obsolete pages (e.g., an old requirements version that has been fully superseded): do not delete. Instead, add a prominent note at the top: "Superseded by [[new-requirements]]. Retained for historical traceability." Update index description accordingly.
- This preserves the ability to answer "What did we believe in 2025?" — often valuable for audits, onboarding, or understanding why certain decisions were made.

## Non-Text or Binary-Heavy Sources
- For images, screenshots, or binary documents, use available tools to extract text, OCR, or descriptions.
- If text extraction is poor, describe what the user should know from the visual and cite the raw file heavily.
- The wiki's job is to make the knowledge queryable in text form; it does not need to replicate every pixel.

## Implications of Ignoring Edge Cases
- Treating every ingest the same leads to either shallow pages (for complex sources) or overly monolithic pages (for simple ones).
- Failing to offer compounding turns the wiki into a read-only archive instead of a living knowledge asset.
- Neglecting visuals leaves large parts of many sources inaccessible to text-based queries and future agents.
- The discipline of handling these cases gracefully is what separates a merely functional wiki from one that becomes indispensable over time.

## Encouraged Mindset
Approach every edge case with the question: "What would make this knowledge most useful and trustworthy for a future reader (or future version of myself) who was not present during this conversation?" That single perspective usually points to the right action.