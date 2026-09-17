# Query workflow

Query mode is read-only unless the user separately asks to persist or repair the wiki.

## Steps

1. Pin the project/worktree, question, wiki root, declared source roots, and requested depth.
2. Read the index or search manifest if present; otherwise search page names/headings. Load only the
   pages relevant to the question.
3. Check cited sources when the answer is high-stakes, a page is stale/contradictory, or the requested
   precision exceeds the wiki summary.
4. Separate supported answer, conflicts, unknowns, and coverage limits. Never fill a gap from general
   memory while presenting it as project knowledge.
5. Return a concise answer with contributing wiki pages and direct sources. Include verbatim quotes
   only when they materially help.

## Response contract

Use the smallest structure that preserves auditability:

- answer;
- sources with useful locators;
- conflicts/unknowns/coverage limits when present.

Do not force an empty Quotes block, repetitive separators, or a “wiki gap” sales pitch into every
answer. If a durable gap is material, identify it and offer a page update only when that is a useful
next action; do not write it in query mode.

## No coverage

If neither wiki nor declared sources support the answer, say so and identify the missing evidence.
Route external research to `/1-research` when requested. Source-code questions may inspect explicitly
in-scope project code and tests; cite them and state that observed implementation may differ from
documented intent or deployed behavior.
