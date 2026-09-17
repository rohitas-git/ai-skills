# Page contract

Prefer the repository's existing wiki format. Use this baseline only where no stronger convention
exists.

## Concept/source page baseline

```markdown
# Page title

Summary of the concept and its project relevance.

## Evidence

- `path/to/source.ext`, section/page/lines — contribution

## Details

Grounded synthesis with links to related project concepts.

## Conflicts and unknowns

Only when present; distinguish unresolved evidence from decisions.

## Related

- [[related-page]] — relationship
```

Dates, frontmatter, status markers, link syntax, and headings follow local conventions. Add fields
only when they carry information the repository uses; do not cargo-cult metadata.

## Names and links

- Follow existing filename and link conventions. If none exist, prefer stable lowercase hyphenated
  Markdown names and links without redundant extensions.
- Resolve naming collisions deliberately; do not overwrite a same-named page with different meaning.
- Link concepts when the relationship helps navigation, not to maximize graph density.
- Preserve redirects/aliases if renaming an established page is separately authorized.

## Index

An existing index should make changed pages discoverable. Preserve its category and ordering rules.
Create an index only when initialization is in scope. Do not rebuild the whole index for a local edit
unless validation shows it is required.

## Source fidelity

- Use exact project-relative paths and useful locators.
- Quote only when exact wording matters; otherwise paraphrase faithfully.
- For visual evidence, cite the file/page and describe only what was actually inspected.
- Synthesized relationships must name their contributing sources and be labeled as synthesis when
  they are not stated directly.

## Size

Prefer one coherent concept per page. Split based on distinct purpose, ownership, or change cadence;
there is no universal page count or word threshold. Keep source summaries separate from durable
concept pages when that improves provenance.
