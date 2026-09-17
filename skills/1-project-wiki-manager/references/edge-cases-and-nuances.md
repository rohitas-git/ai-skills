# Edge cases

## Large or partial sources

Use the relevant document/image extractor and record pages, sections, sheets, or samples covered.
For a very large source, a bounded first pass is valid when labeled partial; do not force a pause if
the user already selected scope, and do not claim full ingestion.

## Binary and visual evidence

Inspect the actual page/image at sufficient detail. Cite its locator and describe observed content.
OCR or extracted text is evidence with possible recognition error, not a perfect substitute for the
visual.

## Multiple sources and versions

Merge claims only when they describe the same concept and preserve source-specific status. Record
supersession when explicit. Retain historical material when it explains decisions, but prevent it
from appearing current.

## Code-backed wiki claims

Source code and tests can establish current repository implementation, not deployed production state
or product intent by themselves. Generated code, fixtures, snapshots, and mocks need their own
labels. Cite symbols/paths and the pinned worktree/HEAD.

## Existing wiki conventions

Do not impose a flat directory, sentinel log, English-only policy, particular link syntax, or fixed
template on a mature wiki. Migrate conventions only through a separately reviewed plan that includes
link compatibility and rollback.

## Concurrent worktrees

Two branches may intentionally document different behavior. Keep edits and indexes in the matching
worktree; never “sync” them by copying mutable wiki output between branches. If the same page is being
edited elsewhere and ownership is uncertain, report the collision instead of overwriting it.

## External or sensitive sources

Do not fetch URLs or upload source material merely because a wiki page would benefit. Route external
research explicitly, respect access/privacy constraints, and store only the minimum necessary
synthesis when persistence is authorized.
