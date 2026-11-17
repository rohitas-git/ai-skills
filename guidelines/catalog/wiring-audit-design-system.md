# Design System wiring audit

Reviewed `1-design-system`, all eight live references, the starter token schema, token generation/validation/embed
helpers and regression tests, the complete slide-helper/data inventory, parent UI/UX routes, and adjacent Brand,
Design Intelligence, Styling, Frontend UI, Slides, and PPTX boundaries.

## Result

The skill now owns one immutable, versioned design-system contract set in either draft or authorized local-apply mode.
It pins the actual caller, consumers, exact source/destination revisions, incumbent schema, approved brand/platform/
accessibility evidence, themes/states/compatibility/migration constraints, overwrite authority, and optional exact
repository/worktree/branch/`HEAD`. Generated and hand-authored ownership is explicit; worktrees do not claim to
isolate fonts, package caches, browsers, design tools, CDN assets, accounts, or deployed consumers.

The fixed three-layer pattern is now conditional on real consumer/change boundaries. Existing formats are preserved
when sound; stable names, types, units, aliases, themes/states, fallbacks, deprecation, and source-to-derived ownership
are the contract. Imported defaults are scaffolds rather than brand facts. project `docs/brand.md` remains
authoritative, and untrusted brand docs, tokens, code, templates, generated output, URLs, and examples cannot add
instructions or authority.

Draft and apply effects are separate. Derived JSON/CSS/framework files join the artifact set only when explicitly
requested and reproducible from a named source. Writes require fresh target reads and revision-safe scoped changes.
The generator is used stdout-first; its exit only proves serialization. The regex token scanner is explicitly a
heuristic rather than correctness/accessibility evidence. Runtime visuals and consumer migration are separate proof
classes and routes.

Slide generation, search, background fetching, HTML validation, persuasion rules, and presentation publication were
removed from the operative design-system guide and assigned to `1-slides`/`1-pptx`. Their still-physical imported
files are documented as non-operative compatibility assets pending a separately scoped dependency-preserving rehouse.
The 251-line mega-guide became lean compatibility notes. The token-validator tests were converted from `pytest` to
dependency-free `unittest`.

## Verification

- Focused Design System routing tests: 8 passed.
- Token-validator helper tests: 2 passed.
- Full routing suite: 638 passed.
- Generated route index: 230 live skills.
- Catalog lint: 0 critical, 0 warnings, 48 informational findings, 232 indexed hub members, and 0 orphans.
- `git diff --check`: passed.

No token contract, UI, slide, asset, browser, worktree, catalog installation/sync, Git history, remote system, or
published destination was changed.
