# JSON Canvas wiring audit

Reviewed:

- `skills/1-json-canvas/SKILL.md`
- complete former 243-line guide and 329-line example set, now lean compatibility references
- Office, Diagram Maker, Vault, Obsidian CLI, and architecture boundaries

## Result

JSON Canvas now owns one exact create or bounded-edit operation on one immutable `.canvas` candidate. It pins
caller, canonical source/destination and revision/hash, consumer/spec version, requested elements/layout,
evidence versus assumptions, vault-relative path rules, sensitivity, overwrite/publication/app authority, and
acceptance criteria. Repository/vault work carries exact repository/worktree/branch/`HEAD`, dirty ownership,
allowed paths, and working-tree versus committed state; worktrees are not claimed to isolate Obsidian, plugins,
sync, collaboration, cloud files, accounts, or URLs.

Canvas content, paths, URLs, labels, unknown fields, and imported JSON are sensitive untrusted data. File/link
nodes store inert references rather than granting access, fetching, preview, plugin, or neighbor-reading rights.
Edits preserve unknown fields, z-order, stable IDs, geometry, and untouched data; targets require exact IDs plus
expected properties, new IDs must be collision-free, and relationships are labeled by evidence status rather
than invented as facts. A fresh-read concurrency fence stops ambiguous or stale writes, and JSON newlines are
serialized once rather than double escaped.

Validation covers structure, IDs, edge integrity, types, paths/URLs, finite geometry, and order without claiming
visual proof. App rendering is separately authorized and cannot activate linked content. Results return to the
actual caller before rendering, app operation, vault edits, link repair, sharing, or publication. The former
572 lines of guides/examples are now 75 lines of version-sensitive, non-authorizing compatibility material.

## Verification

- Focused JSON Canvas routing tests: 8 passed.
- Full routing suite: 564 passed.
- Generated route index: 223 live skills.
- Catalog lint: 0 critical, 0 warnings, 50 informational findings, 0 hub-member orphans.
- `git diff --check`: passed.

No canvas, vault file, worktree, Obsidian app/plugin, URL, cloud file, host installation/sync, Git history, or
remote system was changed.
