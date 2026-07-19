# Properties and Frontmatter in Obsidian

YAML frontmatter (properties) is one of the most powerful features in Obsidian for structured data, search, linking, and especially when combined with the Dataview plugin. Consistent, well-chosen properties turn your vault from a collection of notes into a queryable personal database.

## Purpose
- Store structured metadata about each note (dates, status, relationships, categorization).
- Enable powerful search, filtering, and views via Dataview, Bases (core plugin), and other tools.
- Support automation, templates, and consistent PKM workflows.
- Make MOCs, dashboards, and task management much more effective.

## YAML Frontmatter Syntax

Always placed at the very top of the note, between `---` delimiters.

```yaml
---
title: Note Title
aliases:
  - Alternative Name
tags:
  - project/alpha
  - area/knowledge
created: 2026-07-19
updated: 2026-07-19
status: in-progress
type: concept
priority: high
project: [[Project Phoenix]]
area: [[Knowledge Management]]
---
```

**Rules**:
- Use valid YAML.
- Strings with special characters or starting with numbers should be quoted.
- Lists use `- ` or `[item1, item2]`.
- Dates in `YYYY-MM-DD` format are best for sorting and Dataview.
- Nested objects are supported but keep them simple for readability and querying.

## Recommended Core Properties for a PKM Vault

Adopt a consistent set across note types. This makes Dataview queries reliable.

| Property     | Type          | Purpose                                      | Example                  | Recommended for |
|--------------|---------------|----------------------------------------------|--------------------------|-----------------|
| `title`      | string        | Explicit title (when filename is not ideal) | "Project Phoenix"       | All notes      |
| `aliases`    | list          | Alternative names for linking & search      | ["Phoenix Initiative"]  | Important notes|
| `tags`       | list          | Broad categorization & quick filtering      | ["project/active"]      | Most notes     |
| `created`    | date          | Creation date                               | 2026-07-19              | All notes      |
| `updated`    | date          | Last meaningful update                      | 2026-07-19              | All notes      |
| `status`     | string/list   | Lifecycle state                             | "in-progress", "done"   | Projects, tasks|
| `type`       | string        | Note category                               | "concept", "meeting", "literature" | All notes |
| `priority`   | string        | Urgency/importance                          | "high", "medium", "low" | Actionable notes |
| `project`    | link or list  | Related project(s)                          | "[[Project Phoenix]]"   | Most notes     |
| `area`       | link or list  | Life/project area                           | "[[Knowledge Management]]" | Most notes |
| `source`     | string/link   | Origin of information                       | "[[Book Title]]" or URL | Literature, imported |
| `due`        | date          | Deadline                                    | 2026-08-15              | Tasks, projects|

**Additional useful properties**:
- `cssclasses` — for custom styling
- `publish` / `draft` — for publishing workflows
- Custom fields like `effort`, `impact`, `confidence`, `related-people`, etc.

## Inline Fields (Dataview Style)

You can also define fields directly in the note body using `Key:: Value` syntax. These are picked up by Dataview even without frontmatter.

```markdown
Status:: In Progress
Due:: 2026-08-15
Related:: [[Another Note]]
```

Inline fields are great for quick capture or when the value belongs naturally in the prose.

## Best Practices

- **Consistency is king**: Decide on your core properties once and stick to them. Inconsistent keys break queries.
- **Use links in properties**: `project: [[Project Name]]` creates a real wikilink that Dataview and the graph understand.
- **Date format**: Always `YYYY-MM-DD`. Dataview parses this reliably.
- **Tags vs Properties**: Use `tags` for broad, searchable categories. Use dedicated properties for structured data you want to query or display in tables.
- **Keep frontmatter clean**: Don't put long prose in properties. Use them for metadata only.
- **Update `updated` date** on meaningful changes (not every tiny edit).
- **Aliases**: Add common misspellings or shorter names so `[[wikilinks]]` autocomplete works better.

## How Properties Enable Better PKM

- **MOCs and Dashboards**: Filter notes by `type: concept` + `area: [[X]]`
- **Task Management**: `status: in-progress` + `due < today`
- **Review workflows**: Notes updated in the last 7 days
- **Project overviews**: All notes where `project: [[This Project]]`
- **Literature notes**: Track sources, key ideas, and connections systematically

## Nuances & Edge Cases

- **Changing property keys later**: Use Dataview or a script to migrate if needed. Avoid frequent renaming of core keys.
- **Multi-value properties**: Use lists (`- item`) rather than comma-separated strings when you want to query individual values easily.
- **Empty values**: Dataview treats missing or empty properties gracefully in most queries.
- **Performance**: On very large vaults, keep the number of properties reasonable and avoid extremely complex nested structures.
- **Mobile editing**: YAML frontmatter is fully supported on mobile.

## Agent Guidance

When creating or editing notes:
- Always include a minimal set of core properties (created, updated, tags, type at minimum).
- Suggest additional relevant properties based on note content (e.g., `project`, `status`, `due`).
- When user asks for organization help, propose standardizing properties across note types.
- In synthesis or Q&A, offer Dataview-powered views that leverage these properties.

Well-maintained properties are one of the highest-leverage improvements you can make to an Obsidian vault. They compound over time as your note count grows.