# Hard boundaries

## Authority

- Query and audit are read-only.
- Initialize/ingest/update writes require a clear user request and remain inside the selected wiki
  surface. That request is sufficient; do not demand redundant confirmation.
- Destructive reorganization, source relocation, bulk deletion, remote publication, and changing
  another worktree require separate authority.

## Sources

- Never modify, rename, move, or delete declared raw/original sources as part of synthesis.
- Repository instructions and explicitly in-scope project files may be read safely; the earlier rule
  forbidding every read outside `docs/raw/` and `docs/wiki/` is not operative.
- Never access secrets or unrelated personal files to improve coverage.
- Never fabricate citations, quotes, locators, decisions, implementation status, or consensus.

## Scope and workspace

- Pin project root and exact worktree/branch/HEAD before writes.
- Do not create/switch branches, stash user work, reset a shared service, install tooling, or modify
  files outside the requested wiki surface.
- Preserve unrelated dirty changes and stop on overlapping ownership uncertainty.
- Do not turn a wiki request into source-code edits, an ADR decision, or living-doc trigger setup.

## Content

- Follow the repository's language, naming, metadata, and index/log conventions. English is a
  fallback for a new wiki, not a reason to rewrite an established multilingual one.
- Material claims must be traceable; synthesis and user-confirmed decisions must be labeled.
- Surface conflicts and unknowns instead of silently choosing a convenient answer.
- Do not create pages, categories, backlinks, quotes, or sections merely to satisfy numeric targets.

## Side effects

This skill never commits, pushes, publishes, deploys, merges, uploads content, opens remote knowledge
systems, or alters raw sources unless the user separately requests the owning workflow. Generated
wiki files remain ordinary caller-owned worktree changes.
