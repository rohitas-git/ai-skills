# Citation and Grounding Rules

## Core Principle
**No claim without a source.** The wiki's value derives entirely from its trustworthiness. Every factual assertion, decision, requirement, or relationship must be traceable to one or more raw sources. Speculation, inference beyond the evidence, or "common knowledge" assertions are forbidden.

## How to Cite
1. **Inline attribution** for important facts:
   - "The authentication flow requires MFA for all admin roles (source: requirements-v2.pdf, section 4.2)."
2. **Verbatim quotes** for key passages, definitions, or decisions:
   ```
   > "All user data must be encrypted at rest using AES-256." (source: security-policy.md, paragraph 3)
   ```
   Follow the quote immediately with an English prose explanation or implication if the original language is technical or dense.
3. **Multiple sources**: List all contributing raw files. When they disagree, surface the disagreement rather than picking a winner.

## Handling Contradictions and Evolution
- When two sources conflict on the same fact:
  - Create or update the concept page with a dedicated subsection: `## Conflicting Information`
  - Quote both sides with citations.
  - Note any resolution, open question, or user decision.
  - Example: "Source A states X; Source B states Y. As of 2026-07-19 no reconciliation has been recorded."
- When a later source supersedes an earlier one, update the concept page, change "Last updated", add the new source, and optionally add a note: "Supersedes earlier guidance in legacy-requirements.pdf".

## Marking Uncertainty
- Use the explicit marker `[needs verification]` for any statement that cannot be fully grounded yet.
- Example: "The new compliance module will be delivered in Q3 [needs verification — see roadmap discussion in planning-meeting-2026-06.md]."
- Never remove the marker until a source is provided or user confirms the fact.

## Source Filename Rules
- Always use the **exact original filename** as it appears in `docs/raw/`, including extension.
- For multi-page or sectioned documents, add precise locators: `(source: filename.ext, section 3.1)` or `(p. 12–14)`.
- Never invent shorter names or omit the extension.

## Quotes Block in Question-Answering Responses
When answering user questions, the mandatory response format includes a `**Quotes**` section only when verbatim material was used inline. This keeps answers readable while still offering full traceability.

## Nuances and Implications
- **Over-citation vs. under-citation**: Cite every non-obvious or decision-relevant fact. Do not cite every sentence; that produces unreadable pages. Exercise judgment: if a reader would reasonably ask "Where did that come from?", add a citation.
- **Synthesized pages**: Even pages that combine many sources must still cite the originating raw files in the frontmatter "Sources" list and inline where specific claims appear.
- **Raw sources in non-English**: Translate key passages into clear English for the wiki body, but retain the original verbatim quote when it contains precise terminology, legal language, or numbers. This preserves fidelity.
- **Implications of weak grounding**: A wiki that tolerates unsourced claims quickly loses user trust. Once trust erodes, the entire knowledge base becomes shelfware. Strict citation discipline is the single most important quality guarantee.
- **Future tooling**: These citation conventions also enable future automated link checkers, source-coverage reports, or "what changed since last quarter" diff views.

## Anti-Patterns to Avoid
- Writing "as we discussed" or "per previous decisions" without linking to the actual raw source or wiki page that recorded it.
- Using "obviously", "clearly", or similar subjective qualifiers instead of evidence.
- Updating a page's content without also updating its "Sources" list and "Last updated" date.