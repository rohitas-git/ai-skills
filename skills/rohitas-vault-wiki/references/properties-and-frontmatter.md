# Properties Schema — Rohitas's Notes

Keep the schema **minimal** so every note stays easy to write and the Dashboard stays reliable.

## Required fields

| Property | Values / format | Purpose |
|----------|-----------------|---------|
| `type` | `concept` \| `hub` \| `guide` \| `project` \| `literature` | Note kind |
| `status` | `active` \| `incubating` \| `stable` \| `archived` | Lifecycle; Dashboard uses `active` |
| `tags` | YAML list | Broad filters (e.g. `system-design`, `pkm`) |
| `created` | `YYYY-MM-DD` | Birth date |
| `updated` | `YYYY-MM-DD` | Last meaningful edit |

## Optional fields

| Property | Purpose |
|----------|---------|
| `topic` | Human label for Dashboard column (e.g. System Design, PKM) |
| `source` | URL or citation for literature-derived notes |
| `aliases` | Alternate link names |

## Status meanings

| status | Meaning | Dashboard? |
|--------|---------|------------|
| `active` | Currently studying or using | Yes |
| `incubating` | Draft / thin / needs ROOT loops | No |
| `stable` | Good enough evergreen | No |
| `archived` | Cold / superseded / literature dump | No |

## Examples

### Concept

```yaml
---
type: concept
status: incubating
tags:
  - system-design
created: 2026-07-19
updated: 2026-07-19
topic: System Design
source: "https://www.youtube.com/watch?v=F2FmTdLtb_4"
---
```

### Guide

```yaml
---
type: guide
status: stable
tags:
  - pkm
  - methodology
created: 2026-06-21
updated: 2026-07-19
topic: PKM
---
```

### Literature (archived source)

```yaml
---
type: literature
status: archived
tags:
  - system-design
  - source
created: 2026-06-21
updated: 2026-07-19
topic: System Design
source: "https://www.youtube.com/watch?v=F2FmTdLtb_4"
---
```

## Agent rules

- Always write required fields on **new** notes
- When editing older notes missing frontmatter, add the minimal block
- Bump `updated` on meaningful content changes
- Do not invent new required property keys without user approval (breaks queries)
