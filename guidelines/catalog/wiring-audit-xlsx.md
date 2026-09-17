# XLSX and CSV wiring audit

Reviewed `1-xlsx`, its complete 289-line guide, the complete recalculation helper and LibreOffice wrapper,
bundled OOXML utilities, and adjacent Office/live-Excel boundaries.

## Result

XLSX now performs one read, analyze, create, edit, recalculate, or verify operation on one immutable source/data
set. It pins caller, hashes/data, sheet/range/table scope, destination, schema/types/locale/timezone/units,
formula/calculation expectations, template/style/accessibility/compatibility, lineage, trust/confidentiality,
overwrite/cleanup/publication rules, authority, and exact optional worktree. Worktrees are not claimed to isolate
office processes, user profiles, add-ins/macros, links, cloud files, accounts, engines, or shared destinations.

Workbook and CSV content is sensitive untrusted data; formula/CSV injection, macros, queries, links, hidden
content, and embedded objects cannot trigger execution or refresh. Identifiers, dates, decimals, formulas, sources,
and financial conventions are not inferred. Analysis, repair, formula authoring, recalculation, styling, conversion,
and external refresh are separate operations. Verification covers structure/types/counts/keys/formulas/errors/
reconciliations/precision/time/units/links/retained features while stating sampling limits.

The former recalculation helper silently installed a macro in the global LibreOffice profile and modified the
source in place. The replacement requires separate input/output paths, target-specific overwrite, a trusted-input
or verified-sandbox assertion, an isolated disposable LibreOffice profile, fresh source hashes, and exclusive or
authorized atomic promotion. It refuses source aliases, symlink outputs, collisions, changed sources, and active/
external package features; it never writes a global macro. Its report distinguishes engine success, visible error
tokens, formula correctness, and cross-engine compatibility. The 289-line universal financial guide is now a
30-line version-sensitive compatibility reference.

## Verification

- Focused XLSX routing/helper tests: 9 passed, including hazard detection, alias/collision refusal, and
  source-preserving exclusive copy.
- Full routing suite: 581 passed.
- Generated route index: 223 live skills.
- Catalog lint: 0 critical, 0 warnings, 50 informational findings, 0 hub-member orphans.
- `git diff --check`: passed.

Tests used disposable synthetic files and never launched LibreOffice. No workbook, global profile, package,
worktree, host sync, Git history, or remote system was changed.
