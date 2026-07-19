# URL ingest

## When

User pastes a URL with ingest intent, or Inbox note is primarily a URL.

## Steps

1. Fetch clean main content:
   - Prefer **defuddle** skill / CLI when available  
   - Else page-fetch / browse tools  
2. Capture metadata: final URL, title, fetch date  
3. If body long → **resource-summarizer** per contract  
4. Continue standard ingest pipeline (takeaways → related → plan → write)

## Archive the source

Create `Archives/<Title> (Source).md`:

```yaml
---
type: literature
status: archived
tags: []
created: YYYY-MM-DD
updated: YYYY-MM-DD
source: "https://…"
---
```

Body: link + short fetch note + optional excerpt (not full illegal copy of paywalled content; prefer summary + link).

## Concepts

Compiled Concepts cite the Source archive and/or `source:` URL in frontmatter. Prefer own-words Feynman distill over paste dumps.

## Failures

If fetch fails: report error; offer Inbox capture of user-provided paste instead.
