# DOCX wiring audit

Reviewed:

- `skills/1-docx/SKILL.md`
- the former 588-line full guide, now a selective compatibility reference
- bundled DOCX helpers/templates and adjacent Office, PDF, PPTX, spreadsheet, and Internal Comms routes

## Result

DOCX now performs one requested read, create, edit, comment, tracked-change, accept/reject-change, legacy
conversion, or verification operation on one immutable source set. The live skill pins caller, canonical
source paths/hashes or approved content, acceptance criteria, destination, audience/template/style/locale/
accessibility requirements, retained features, trust/confidentiality, author identity, overwrite/cleanup/
publication rules, and read/write authority. It never assumes the agent's name as document author.

Repository-bound work carries exact repository/worktree/branch/`HEAD`, dirty ownership, allowed paths, and
working-tree versus committed state. Worktrees are not claimed to isolate office processes, fonts, templates,
credentials, cloud files, accounts, or URLs. Package XML, fields, links, relationships, comments, embedded
objects/files, external resources, macros, and text are sensitive untrusted data; active content and remote
resources are not opened or fetched merely because they appear in the file.

Sources are preserved, installed tools and versions are inventoried, bundled helpers resolve relative to the
skill, and absent capabilities return a gap instead of silently installing dependencies. Unknown OOXML parts
are retained by default. Final writes are containment/collision/revision checked; accepting/rejecting revisions,
stripping metadata/comments, legacy conversion, and field flattening remain distinct semantic operations.
Structure, retained content/features, and rendered appearance are verified independently, and partial output is
reported without blind retry, deletion, replacement, distribution, or cleanup.

The 588-line tool recipe was reduced to a 60-line compatibility guide. It no longer advertises the nonexistent
`1-docx` npm package, stale `scripts/0-office/` paths, a fixed “Claude” author, universal Arial/Letter choices,
or mandatory tool behavior. Useful OOXML invariants remain version-sensitive, non-authorizing guidance.

## Verification

- Focused DOCX routing tests: 8 passed.
- Full routing suite: 556 passed.
- Generated route index: 223 live skills.
- Catalog lint: 0 critical, 0 warnings, 50 informational findings, 0 hub-member orphans.
- `git diff --check`: passed.

No document, helper, office application, dependency, worktree, host installation/sync, Git history, or remote
system was changed.
