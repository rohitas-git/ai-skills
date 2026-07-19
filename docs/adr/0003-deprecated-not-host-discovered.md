# ADR 0003: Deprecated skills are not host-discovered

## Status

Accepted

## Context

Symlink sync previously installed `deprecated/` tombstones into agent skill directories, keeping dead names visible to hosts and competing for description budget.

## Decision

Remove `deprecated` from `DISCOVER_BUCKETS` in `scripts/sync-skills-symlinks.sh`. Tombstones remain in git for humans and butler history only.

## Consequences

Old slash names stop resolving via host skill dirs after re-sync. Successors are the live skills; tombstone text is still in-repo under `skills/deprecated/`.
