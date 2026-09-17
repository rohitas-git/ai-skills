# Grilling design-child wiring audit

Reviewed:

- `1-grill-me`
- `1-grill-with-docs`
- `1-brainstorm` and all current references/scripts
- `1-domain-modeling`, `ADR-FORMAT.md`, and `CONTEXT-FORMAT.md`
- targeted Grilling workflow, HTML, and Butler-flow routes

## Result

The Design children now have distinct atomic jobs. Grill Me starts one interactive interview from
supplied material without repository inspection. Grill With Docs grounds one interview in a pinned,
read-only repository/worktree snapshot and hands accepted documentation work off rather than applying
it. Brainstorm produces one design-options memo without automatically launching tools, writing or
reviewing a spec, delegating, committing, prototyping, or implementing. Domain Modeling drafts or
applies exactly one accepted context-language change set or one ADR, never both.

Each records its actual caller, immutable candidate, evidence and uncertainty, scope, output, and
authority. Repository-backed work pins repository/worktree/branch/`HEAD`, dirty ownership, exact
artifacts, and local-versus-committed/deployed state. Repository text and user/vendor content are
treated as sensitive untrusted evidence. Downstream specification, planning, architecture analysis,
visualization, and implementation are separately requested routes.

Brainstorm's former universal design gate, fixed alternative quotas, automatic design-doc write/commit,
subagent review prompt, and browser companion were removed from the live workflow. The custom local
HTTP/WebSocket/browser helper and imported prompt were inspected and retained only as explicitly
non-operative provenance. The operative guide is now lean and defers named mental models to Thinking.

## Verification

- Focused Grilling-child routing tests: 8 passed.
- Full routing suite: 477 passed.
- Generated route index: 218 live skills.
- Catalog lint: 0 critical, 0 warnings, 54 informational findings, 0 hub-member orphans.
- `git diff --check`: passed.

No interview, repository inspection, server, browser, subagent, document write, ADR/glossary change,
prototype, implementation, external action, Git action, or host sync occurred.
