# Spreadsheet compatibility guide

Version-sensitive guidance only; `../SKILL.md` is operative. This reference grants no source read, installation,
execution, destination write/overwrite, office-profile mutation, macro/query/link refresh, app/cloud access,
cleanup, or publication authority. Confirm installed tool/engine behavior and the target consumer.

| Need | Candidate capability when already available | Main risk |
|---|---|---|
| Table analysis/CSV | typed dataframe/CSV library | silent type/date/identifier coercion |
| XLSX structure/formulas/styles | OOXML library such as openpyxl | unsupported features lost on save |
| Formula recalculation | isolated trusted Excel-compatible engine | engine differences, external refresh, source mutation |
| Visual verification | trusted spreadsheet renderer/app | macros, links, add-ins, font/layout drift |

Preserve raw values and declared types before transforming. Explicitly define headers, missing-value semantics,
identifiers, decimals, locale, dates/timezones, units, keys, duplicates, ordering, and formulas versus cached values.
CSV has no types, formulas, sheets, styles, or canonical dialect; delimiter, quote, encoding, newline, and injection
handling are part of its contract.

Formula choices follow the user's maintenance need. Dynamic formulas are useful when consumers must recalculate;
verified fixed values can be correct for immutable exports. Never impose formulas, assumption sheets, font/color
codes, number formats, or financial conventions universally. Preserve formulas when loading/saving; opening with
cached-value-only modes and then saving can destroy them in some libraries.

For models, trace hardcoded inputs to supplied sources and dates, reconcile roll-forwards/totals, inspect range
boundaries, and test material edge cases. “Zero visible error tokens” is necessary where required but insufficient:
wrong references, stale caches, hidden errors, circularity, unit mistakes, and plausible-but-wrong formulas may remain.

Recalculation must use a copy, an isolated disposable profile, disabled/unrefreshed external content, and the
declared engine/version. Compare formulas before/after and verify cached outputs independently. Different engines
can calculate, format, and support functions differently; report that compatibility boundary.
