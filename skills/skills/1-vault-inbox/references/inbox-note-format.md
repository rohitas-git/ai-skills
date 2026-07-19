# Inbox note format

## Location

`{vault}/Inbox/<Title Case Name>.md`

## Minimal frontmatter

```yaml
---
created: YYYY-MM-DD
source: chat | url | agent | paste
tags: []   # optional
---
```

No required `type`/`status` until ingest promotes the note.

## Body

- Prefer user text as-is
- Keep URLs and quotes intact
- Optional trailing `## Related` only when user named targets

## Naming

| Situation | Filename |
|-----------|----------|
| Clear title | `Title Case.md` |
| URL article title known | That title Title Case |
| Pure dump | `2026-07-19 1430 Capture.md` |

Avoid characters unsafe in filenames (`/ \ :`). Collapse internal slashes.
