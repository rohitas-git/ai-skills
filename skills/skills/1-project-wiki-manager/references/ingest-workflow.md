# Ingest Workflow

## Purpose
Ingestion is the primary mechanism by which the wiki grows. When a human places a new or revised document in `docs/raw/`, the agent transforms it from unstructured (or semi-structured) raw material into structured, interlinked, source-grounded knowledge pages. A single rich source can legitimately affect 8–15 wiki pages; this is expected and desirable for thorough knowledge extraction.

The workflow enforces human-in-the-loop confirmation at key decision points to prevent hallucinated structure or premature commitment.

## Step-by-Step Ingest Process

### 1. Detect and Read the Source
- Identify the new or changed file in `docs/raw/`.
- Use `read_file` (or appropriate document reader for PDF/images) to obtain the **full content**.
- If the file is extremely large (> ~50k tokens), first extract and present:
  - Title / metadata
  - Table of contents or major sections
  - Executive summary or abstract (if present)
  - Key entities, decisions, data models, or processes mentioned
- Then ask the user: "Shall I proceed with full detailed analysis of this source, or focus on specific sections first?"

### 2. Extract and Discuss Key Takeaways (Human Confirmation Required)
- Identify the 5–12 most important concepts, facts, decisions, requirements, or entities.
- For each, draft a one-sentence takeaway grounded in the source.
- Present these to the user in a clear list.
- **Explicitly ask for confirmation or edits** before creating any wiki pages:
  > "Here are the key takeaways I propose to capture. Do these look accurate? Would you like to add, remove, merge, or rephrase any before I create wiki pages?"
- Only proceed after the user signals approval (e.g., "yes", "proceed with these", or provides a revised list).

### 3. Create or Update the Source Summary Page
- Create (or update) a page in `docs/wiki/` named after the source file, slugified to lowercase-hyphen.md (e.g., `requirements-v2.md` → `requirements-v2.md`, `architecture-decisions-2025.pdf` → `architecture-decisions-2025.md`).
- The page must follow the standard Page Format (see `page-formats-and-templates.md`).
- Include a "Sources" section pointing back to the exact raw filename.
- Extract major sections into headed content with inline `[[wiki-links]]` to concept pages you will create or update.
- After writing, update `index.md` and append to `log.md`.

### 4. Extract and Create/Update Concept Pages
For every significant idea, entity, process, decision, schema, requirement, or relationship:

- **Check `index.md` first** to see if a page already exists for that concept.
  - If yes: merge new information, highlight any contradictions or evolutions, and update the "Last updated" date and Sources list.
  - If no: create a new page using the standard template.
- Decide category:
  - Project-level or high-level concepts → `docs/wiki/concept-name.md`
  - More technical/implementation-oriented (even without code) → consider proposing `docs/wiki/implementation/` or similar subfolder only after user approval. By default keep flat unless complexity justifies hierarchy.
- Always include `[[wiki-links]]` to related pages.
- After creating/updating several pages, batch-update `index.md` and `log.md` once.

### 5. Update Index and Log
- Add or update rows in the categorized table in `index.md`.
- Append a single consolidated entry to `log.md` using the sentinel pattern.
- Example log entry:
  ```
  ## 2026-07-19 | requirements-v2.pdf | Added source summary page + 7 concept pages (user-confirmed takeaways) | Updated 2 existing pages
  ```

### 6. Handle Post-Ingest Review
- Offer the user a summary: "Ingestion complete. Created/updated X pages. Here are the most important new connections: ..."
- Ask whether any of the new syntheses should be expanded into deeper pages or linked from existing high-traffic pages.

## Handling Multiple Sources and Evolution
- When the same concept appears in several raw files, the concept page becomes the single source of truth that merges perspectives.
- Always note the differing viewpoints with citations.
- If a raw source is revised later, re-ingest it: mark affected wiki pages as "needs review", update dates, and log the delta.

## Nuances, Edge Cases, and Best Practices
- **Very large impact ingests (10+ pages):** This is normal for foundational documents (e.g., system requirements, 1-research papers, strategy decks). Do not rush; thorough linking in step 4 is what makes the wiki valuable.
- **Ambiguous or overlapping concepts:** When in doubt, create slightly narrower pages and link them (e.g., `user-authentication.md` and `session-management.md` rather than one giant page). User can request merges later.
- **Visuals, diagrams, tables in source:** Describe them in prose in the wiki page. For critical diagrams, note "See original diagram in raw/filename.ext, page X" and describe key elements so the wiki remains self-contained for text-based querying.
- **Contradictions within one source or across sources:** Surface them explicitly in the concept page under a "Known Issues / Open Questions" heading. Never silently resolve.
- **Source contains future plans or speculative content:** Label clearly as "Proposed / Not yet implemented (source: ...)" so readers understand status.
- **User rejects some takeaways:** Respect the decision, log the rejection reason if provided, and do not create those pages. The source summary page can still reference the raw file.
- **Incremental vs. full re-ingest:** For minor updates to a raw file, focus only on changed sections. For major rewrites, consider a full re-ingest with user confirmation.
- **Implications of skipping confirmation:** Creating pages without user 0-review risks polluting the wiki with misinterpretations or unwanted granularity. The confirmation step protects wiki quality and user agency.

## Why Strict Process Matters
Rushing ingestion without discussion leads to shallow or incorrect pages that later require costly cleanup. The human-in-the-loop design ensures the wiki reflects the user's actual mental model and priorities, not the agent's assumptions. Over time this produces a high-trust, high-signal knowledge base that accelerates onboarding, decision-making, and continuity.