# PPTX wiring audit

Reviewed `1-pptx` and its complete 855-line routing, template/XML, and PptxGenJS guidance plus bundled
helpers and adjacent Office routes.

## Result

PPTX now performs one requested read, create, template-adapt, edit, reorder, or verify operation on one
immutable source/content set. It pins caller, sources/templates/hashes, slide scope/order, destination,
audience/purpose, factual sources, aspect ratio, template/brand/theme/font/accessibility/compatibility,
retained features, trust/sensitivity, author metadata, overwrite/cleanup/publication rules, and read/write/
network/app authority. Repository work carries exact worktree/branch/`HEAD` and dirty ownership, while shared
office processes, fonts, templates, assets, cloud files, accounts, and URLs remain explicitly non-isolated.

Package data and active/external content are sensitive untrusted input. The skill never silently installs,
downloads, delegates, fetches assets, opens cloud apps, or invents claims/visuals. Sources and unknown OOXML
parts are preserved; writes use fresh containment/collision/revision checks. Template adaptation, structural
changes, content edits, cleanup, and export remain separate operations. Verification separates package,
semantic, rendered, and target-viewer evidence; QA is risk-based, does not require inventing a defect, and
rerenders only affected slides after actual fixes. Partial results never trigger blind retry or cleanup.

The prior 855 lines of live guidance are now 69 lines of selective, version-sensitive compatibility notes.
Fixed palettes/fonts/margins/layout formulas, mandatory visuals/subagents, forced defect/fix cycles, stale helper
paths, and global install recipes were removed while retaining relationship-aware editing, PptxGenJS mutation,
color, list, image, chart, provenance, accessibility, and verification constraints.

## Verification

- Focused PPTX routing tests: 8 passed.
- Full routing suite: 572 passed.
- Generated route index: 223 live skills.
- Catalog lint: 0 critical, 0 warnings, 50 informational findings, 0 hub-member orphans.
- `git diff --check`: passed.

No deck, helper, app, dependency, asset, worktree, host sync, Git history, or remote system was changed.
