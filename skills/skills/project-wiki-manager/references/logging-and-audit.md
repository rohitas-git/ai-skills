# Logging and Audit

## Purpose of the Log
`docs/wiki/log.md` is the single source of truth for all changes to the wiki. It enables:
- Quick understanding of recent activity
- Accountability and rollback context
- Detection of patterns (e.g., frequent updates to certain concepts)
- Future automation or reporting

Because it is append-only and uses a sentinel, it can be updated mechanically without risk of corrupting history.

## Log Entry Format (Strict)
```
## YYYY-MM-DD | source-or-trigger | summary of what was done | pages created/updated count and highlights
<!-- END OF LOG -->
```

- Date in ISO format.
- Trigger is usually the raw filename or "user request: Q&A synthesis".
- Summary should be concise but informative.
- Always replace the sentinel line with the new entry + new sentinel.

Example after several operations:
```
# Wiki Operation Log

## 2026-07-18 | architecture-decisions.pdf | Added source summary page + 4 concept pages (user confirmed) | Updated index
## 2026-07-19 | stakeholder-interviews.md | Merged new requirements into [[user-authentication]] and created [[gdpr-compliance]] | Updated 2 pages + index + log
<!-- END OF LOG -->
```

## Creating the Log on First Use
If `log.md` does not exist when needed:
1. Create it with a header and initial sentinel.
2. Add an entry noting the initialization.
3. Confirm with user that logging has begun.

## Audit and Lint Commands (When Requested by User)
When the user asks for a health check, run through this checklist and report findings as a numbered list with suggested fixes only. Do **not** auto-apply fixes unless explicitly instructed.

1. **Broken wiki-links**: Scan all pages for `[[page-name]]` that have no corresponding `.md` file.
2. **Orphan pages**: Pages that exist but are not referenced from index.md or from any other page's "Related Pages" section.
3. **Missing concept pages**: Major ideas mentioned in source summaries but lacking dedicated pages.
4. **Outdated claims**: Pages whose "Last updated" date is older than the most recent raw source they cite.
5. **Format violations**: Pages missing Summary, Sources, or Last updated frontmatter; or using inconsistent heading levels.
6. **Duplicate or near-duplicate pages**: Two pages covering almost identical ground without clear differentiation.
7. **Invalid source references**: Citations pointing to non-existent files in `docs/raw/`.
8. **Contradictions without resolution**: Concept pages that quote conflicting sources but have no "Conflicting Information" section or user decision recorded.
9. **Log sentinel missing or corrupted**: Ensure `<!-- END OF LOG -->` is present and at the end.

Report format example:
```
1. Broken link: [[user-onboarding]] in onboarding-flow.md — no such page exists. Suggested fix: create the page or remove the link.
2. Orphan page: legacy-requirements.md is not listed in index.md and has no incoming links. Suggested fix: add to Sources category or archive if obsolete.
...
```

## Nuances
- **Log as single source of truth**: Never rely on git history alone for wiki changes; the log is human-readable and self-contained.
- **Batch updates**: When one ingest touches many pages, produce one consolidated log entry rather than many tiny ones.
- **Audit frequency**: Encourage users to request audits after large ingests or quarterly. Regular audits prevent quality drift.
- **Implications of neglected logging**: Without a clear history, it becomes impossible to answer "When did we decide X?" or "What changed after the new compliance doc arrived?" — defeating a primary purpose of the wiki.

## Future-Proofing
The sentinel pattern and strict format make it straightforward to later add scripts that parse the log for metrics (pages per month, most-edited concepts, etc.) without fragile string matching.