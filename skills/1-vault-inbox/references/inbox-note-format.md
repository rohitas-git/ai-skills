# Inbox note format

The active vault's existing Inbox convention is authoritative. If no local convention exists,
one new capture may use this minimal shape:

```md
---
created: {actual timestamp/date in the approved vault format}
source: {truthful supplied provenance}
---

{supplied payload, with any disclosed redaction}
```

Rules:

- Do not invent `type`, `status`, tags, source authorship, links, or processing decisions.
- Preserve meaningful line breaks and literal text; do not turn escaped `\n` into unintended
  content or convert real newlines into literal escape sequences.
- A quoted title or URL is data and does not authorize fetching or copying unavailable text.
- Derive a filename only when unambiguous; otherwise use a truthful collision-resistant
  capture identifier or ask if the title affects identity.
- Sanitize traversal and platform-invalid filename characters without silently changing the
  note's meaning. Record any filename transformation.
- Create exclusively after a case-insensitive collision recheck. Never overwrite or append.
- Do not add a Related section unless the user supplied the exact relationship and the active
  schema supports it; even then, do not open the linked note.
