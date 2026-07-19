# Question Answering Workflow

## Purpose
The wiki exists to be queried. High-quality answers reinforce the wiki's value and often surface opportunities to grow it further. Every answer must be transparent about its sources and honest about gaps.

## Step-by-Step Answering Process

### 1. Consult the Index First
- Read `docs/wiki/index.md` to identify candidate pages.
- If the question is broad, note several potentially relevant categories and pages.
- If ambiguity exists in the question, ask a clarifying question before deep reading.

### 2. Read Relevant Wiki Pages
- Load only the pages that appear directly relevant (progressive disclosure).
- Extract grounded facts, quotes, and relationships.
- Note any `[needs verification]` markers or open questions.

### 3. Decide Answer Sufficiency
- **If wiki content is sufficient**: Answer directly from the wiki pages, using inline citations and the mandatory response format below.
- **If partial coverage exists**: Answer what can be answered from the wiki, then clearly state what is missing. Offer to research the gap in raw sources.
- **If no relevant wiki coverage**: Proceed to raw sources (step 4).

### 4. Search Raw Sources When Wiki Is Insufficient
- Use available tools to search or read files in `docs/raw/`.
- Prioritize files already referenced in the wiki index.
- Label any information drawn directly from raw (not yet in wiki) with clear attribution.
- After answering, propose creating or updating wiki pages to close the gap (see Wiki Gap block).

### 5. Apply the Mandatory Response Format
Every answer — regardless of source — **must** follow this exact structure:

```
{Answer prose in clear English. Use inline citations such as (source: filename.ext, section X). Include [[wiki-links]] where they help navigation.}

---
**Quotes**
> "Verbatim key passage" (source: exact-filename.ext, location)
> "Another important excerpt" (source: ...)

---
**Sources**
*Wiki pages consulted:*
- [[page-name]] — reason this page contributed
- [[another-page]] — reason

*Raw sources linked from wiki:*
- `filename.ext` — reason

*Raw sources directly read for this answer:*
- `filename.ext` — reason (e.g., gap in wiki coverage)

[Wiki Gap block — include only when applicable]
```

- The **Sources** section is always required.
- Only list items that actually contributed to the answer.
- The **Quotes** block appears only when verbatim material was used in the prose.
- Keep the prose readable; the structured blocks provide full auditability.

### Wiki Gap Block (When Information Came from Raw or Was Synthesized)
```
---
📥 **Wiki Gap detected**
This answer drew on raw sources or synthesis not yet captured in dedicated wiki pages.

**Suggested new page**: `concept-name.md`
**Suggested category in index**: Core Concepts (or other)
**Content to add**: Brief outline of what should be persisted (key facts, links, citations).

Would you like me to create this page now (after your 0-review of the draft)?
```

If the entire answer had no wiki coverage at all, use a variant:
```
---
📥 **Wiki Gap detected**
No existing wiki pages covered this topic. The answer above is sourced directly from raw files.

**Suggested first page**: `new-concept.md`
**Suggested category**: ...
Would you like me to draft and add it to the wiki?
```

### 6. Offer to Compound Knowledge
After any strong, well-sourced answer that fills a gap or provides a useful synthesis:
- Explicitly ask: "This synthesis seems valuable for future questions. Shall I create a dedicated wiki page for it (or update an existing one)?"
- If yes, follow the normal page creation process with user confirmation of the draft.

## Nuances and Best Practices
- **Do not speculate**: If neither wiki nor raw sources contain the answer, state clearly: "I could not find coverage of this in the current wiki or raw sources. Would you like to provide a source document, or shall we note this as an open question?"
- **Partial answers are acceptable**: It is better to say "The wiki currently covers A and B but not C" than to guess at C.
- **Cross-page synthesis**: When an answer naturally draws from 3+ pages, consider whether a new "overview" or "relationship" page would be useful; offer it via the gap mechanism.
- **Language of answers**: While the wiki itself remains English-only, if the user asks in another language the agent may respond in that language for the prose section while keeping the structured blocks and all wiki links in English. (However, new wiki content created from the answer must be English.)
- **Implications of skipping the format**: Inconsistent answers erode user confidence in the wiki's reliability. The rigid format trains users to trust every citation and makes it easy to audit or improve answers later.
- **Long-term effect**: Consistently offering to persist good answers turns the wiki from a static archive into a living, self-improving knowledge graph.

## When to Decline or Redirect
- If the question is about implementation details inside source code and no raw design docs cover it: state that the wiki focuses on documented knowledge and suggest the user add the relevant design document to raw/.
- Never attempt to reverse-engineer or infer from code (this skill has no codebase access by design).