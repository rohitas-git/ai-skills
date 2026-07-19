# Skills catalog rules

This directory is the **skills catalog** (not an application). Agents editing skills must respect bucket layout.

## Bucket rules

1. **Promoted set** — only skills under `engineering/`, `productivity/`, and `misc/` appear on the root README and are the default daily catalog.
2. **Personal / in-progress / deprecated / vendor** — never list on the root README; they are offline from promotion until intentionally moved.
3. **One skill = one directory** named after frontmatter `name`, containing `SKILL.md` (plus optional references/scripts).
4. **Stewardship** — catalog health, routing, ingest, and rehousing go through **`butler`** (user-invoked). Do not flatten buckets or invent a second meta-router.

## Layout

```text
skills/
  engineering/   # promoted
  productivity/  # promoted
  misc/          # promoted
  personal/      # not promoted
  in-progress/   # not promoted
  deprecated/    # not promoted
  vendor/        # not promoted; packs only
  CLAUDE.md
  README.md
  skills-lock.json
```

## Install / discovery

Hosts that only scan one level deep should use the repo symlink sync (`scripts/sync-skills-symlinks.sh`), which flattens bucket children to top-level skill names in agent skill dirs. Do not re-flatten this tree into a single directory of skills.

## Deprecated

Skills under `deprecated/` are tombstones only. They are **not** installed into agent skill directories by `scripts/sync-skills-symlinks.sh`. Do not re-add `deprecated` to discovery without an ADR.

