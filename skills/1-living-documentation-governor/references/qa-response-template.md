# Read-only Q&A contract

Use when answering a project-documentation question without editing.

Return only what the evidence supports:

1. concise answer in the user's requested language;
2. contributing living docs and precise locations;
3. code/config/spec/runtime evidence directly inspected, separated by evidence class;
4. conflicts, staleness, trigger obligations, and coverage limits when present;
5. one bounded doc-update suggestion only when a material gap exists.

Do not require empty headings, a quote block, or every possible source category. Quote sparingly when
exact wording matters. A code observation describes the pinned repository candidate, not necessarily
deployed behavior or intended policy.

Query mode never edits docs, source, triggers, index, or logs. If the user asks to repair a gap, return
the pinned evidence and requested scope to the main update workflow.
