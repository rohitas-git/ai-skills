# Catalog layout

```text
<catalog-root>/
  engineering/     # promoted
  productivity/    # promoted
  misc/            # promoted
  personal/        # not promoted
  in-progress/     # not promoted
  deprecated/      # not promoted
  vendor/          # packs; out of discovery
  README.md        # promoted skills only
  CLAUDE.md        # bucket rules
  skills-lock.json
```

**Promotion rule:** root README lists only engineering + productivity + misc.

**Skill path:** `<bucket>/<skill-name>/SKILL.md` with frontmatter `name` matching directory name.

**Discovery for hosts:** `scripts/sync-skills-symlinks.sh` flattens bucket children to top-level symlinks. `vendor/` is never auto-scanned.
