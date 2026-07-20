# Hard Rules and Constraints

These rules are non-negotiable. They protect the integrity, trustworthiness, and long-term viability of the wiki.

## Immutability of Sources
- **Never** read from or write to any file outside `docs/raw/` and `docs/wiki/`.
- **Never** modify, rename, delete, or move files inside `docs/raw/`.
- **Never** touch source code, build artifacts, configuration files, or any other project folders (this skill has no codebase scope by design).
- If a user requests an action on raw sources, politely decline and explain that the wiki treats raw/ as the immutable ground truth.

## English-Only Policy for Wiki Content
- All wiki pages (`*.md` in `docs/wiki/`), `index.md`, and `log.md` must be written in clear, professional English.
- Internal reasoning and log entries are also English-only.
- User questions may arrive in any language; the agent may respond in the query language for the prose portion of answers, but any new or updated wiki content created as a result must be English.
- Key original terms from non-English sources may be retained in parentheses or quotes for traceability, followed by English explanation.

## No Speculation or Invention
- Every sentence that asserts a fact, decision, requirement, relationship, or status must be directly supported by at least one raw source.
- If no source exists, the agent must either:
  - State the gap explicitly, or
  - Ask the user to provide a source document.
- Phrases such as "it is obvious that...", "we can assume...", or "in practice this usually means..." are forbidden unless backed by a cited source.

## Page Naming and Organization
- All page filenames: lowercase letters, digits, and single hyphens only. Must end with `.md`.
- No spaces, underscores, camelCase, or special characters.
- Source summary pages should be named to closely match the slug of their raw filename.
- Concept pages use descriptive English names (e.g., `user-authentication-flow.md`).
- By default, keep all pages in the flat `docs/wiki/` directory. Propose subdirectories (e.g., `implementation/`, `decisions/`) only when page count in a category exceeds ~15–20 and the user explicitly approves the new structure.

## Human-in-the-Loop Confirmation
- During ingestion: present key takeaways and obtain explicit confirmation before writing any new pages or making substantial updates.
- For Q&A synthesis that proposes new pages: always show a draft outline and wait for approval.
- Never auto-create or auto-update pages on the basis of inference alone.

## Index and Log Discipline
- After every creation or meaningful update of wiki pages, the `index.md` table **must** be updated.
- After every change, a log entry **must** be appended using the sentinel pattern.
- These two updates are not optional; they are what keep the wiki discoverable and auditable.

## Forbidden Actions
- Do not create `README.md`, `CHANGELOG.md`, or other human-facing files inside the skill or wiki unless explicitly part of the documented workflow.
- Do not nest references inside references (for the skill itself).
- Do not exceed reasonable page length without splitting (see page formats guidance).
- Do not silently resolve contradictions; always surface them.

## Why These Rules Exist
Each constraint addresses a specific failure mode observed in long-lived knowledge bases:
- Immutability prevents the "telephone game" where synthesized pages drift from reality.
- English-only ensures a single consistent language for search, linking, and future agents or humans.
- No-speculation preserves trust; users quickly 0-learn they can rely on every statement.
- Confirmation steps protect against over-eager or misaligned automation.
- Strict index/log updates prevent the wiki from becoming a collection of orphaned or invisible pages.

Violating any of these rules, even once, risks compounding errors that become expensive to unwind later. The agent must internalize these as hard boundaries, not suggestions.