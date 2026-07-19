# Dataview Plugin for Obsidian

Dataview is a powerful community plugin that turns your Obsidian vault into a queryable database. It reads frontmatter properties, inline fields (`Key:: Value`), and note content to generate dynamic lists, tables, task views, and more — all inside regular Markdown notes.

**Important for the agent**: You cannot execute Dataview queries yourself. Instead, you help the user by:
- Writing correct, ready-to-paste Dataview queries.
- Recommending properties and inline fields that make future queries powerful.
- Suggesting Dataview-powered views (in MOCs, dashboards, or daily notes) that improve organization and insight.
- Helping maintain data quality so queries remain reliable.

## Basic Query Syntax

Dataview uses a simple, SQL-like language called DQL.

### Common Query Types

**LIST** — Simple bullet list of matching notes
```dataview
LIST
FROM "Notes" 
WHERE type = "concept" 
SORT updated DESC
```

**TABLE** — Tabular view with chosen columns
```dataview
TABLE created, status, project
FROM "Projects"
WHERE status != "done"
SORT due ASC
```

**TASK** — Aggregate tasks from across notes
```dataview
TASK 
FROM "Inbox" OR "Projects"
WHERE !completed 
SORT due ASC
```

**CALENDAR** — Visual calendar view (great for daily/periodic notes)
```dataview
CALENDAR created
FROM "Daily"
```

## Very Useful Query Patterns for PKM

### 1. MOC / Topic Overview
Show all notes linked to a concept or project:

```dataview
LIST 
FROM [[]] 
SORT updated DESC
```

Or more advanced (notes that link to current note or have it in a property):

```dataview
TABLE created, status
FROM ""
WHERE contains(project, [[]]) OR contains(area, [[]])
SORT updated DESC
```

### 2. Active Projects Dashboard
```dataview
TABLE 
  status AS Status, 
  due AS "Due Date",
  length(rows) AS "Related Notes"
FROM "Projects"
WHERE status = "in-progress"
GROUP BY project
```

### 3. Recent Notes / Activity Feed
```dataview
LIST 
FROM ""
WHERE updated >= date(today) - dur(7 days)
SORT updated DESC
LIMIT 20
```

### 4. Tasks by Status or Due Date
```dataview
TASK 
WHERE !completed 
AND (due <= date(today) OR !due)
SORT due ASC
```

### 5. Notes by Type + Area (Great for MOCs)
```dataview
TABLE created, updated
FROM ""
WHERE type = "concept" 
AND contains(area, [[Knowledge Management]])
SORT updated DESC
```

### 6. Literature / Source Tracking
```dataview
TABLE source, created
FROM ""
WHERE type = "literature"
SORT created DESC
```

## Inline Fields vs Frontmatter

Both work with Dataview:

- **Frontmatter** (top of note): Best for structured, consistent metadata.
- **Inline fields** (`Key:: Value` in the body): Great for values that appear naturally in prose or for quick capture.

Example inline:
```markdown
The meeting happened on [date:: 2026-07-18]. 
Decision status is [status:: approved].
Related project: [project:: [[Project Phoenix]]]
```

Dataview can query both.

## Advanced / Powerful Features

- **GROUP BY** + aggregation (count, sum, etc.)
- **FLATTEN** for handling list properties
- **FROM** with folder paths, tags (`#tag`), or outgoing links
- **WHERE** with date math, string functions, list operations (`contains()`, `econtains()`)
- **SORT** and **LIMIT**
- **EMBED** or rendering queries inside callouts for clean dashboards

## Best Practices When Working with Dataview

- **Design properties for querying**: Think about how you will want to filter and display data *before* you create hundreds of notes.
- **Use consistent values**: "in-progress" vs "In Progress" vs "active" — pick one and stick to it.
- **Combine with MOCs**: Put useful Dataview queries directly inside your Maps of Content. They become living dashboards.
- **Performance**: On very large vaults, avoid extremely broad `FROM ""` queries without limits or good `WHERE` clauses.
- **Readability**: Format queries nicely with indentation. Use comments (`// comment`) inside queries when helpful.
- **Mobile**: Dataview queries render on mobile, but complex ones can be slower.

## How the Agent Should Use This Knowledge

During **ingest**:
- Suggest relevant properties and inline fields so the new note will appear correctly in existing Dataview views.
- Offer to add a small Dataview query to a related MOC that will surface the new note.

During **organization & MOC work**:
- Propose adding or improving Dataview queries inside MOCs to create dynamic overviews.
- Help standardize properties across a folder or note type so one query works everywhere.

During **querying & synthesis**:
- When the user asks a question that could benefit from an overview ("show me all active projects"), write a ready-to-use Dataview query they can paste into a note.
- Offer both a synthesized prose answer *and* a dynamic query view.

During **maintenance**:
- Spot inconsistent property usage that would break queries.
- Suggest cleanup or migration steps.

## Example: Adding a Dashboard Section to an MOC

```markdown
## Active Projects

```dataview
TABLE status, due, priority
FROM "Projects"
WHERE status = "in-progress"
SORT due ASC
```
```

This turns a static MOC into a living command center.

## Limitations & Realistic Expectations

- Dataview is read-only from the agent's perspective. We propose queries; the user pastes and refreshes them in Obsidian.
- It depends on the user having the Dataview plugin installed and enabled.
- Very complex queries can impact performance — keep them focused.

Mastering Dataview (combined with good frontmatter discipline) is one of the highest-leverage skills for long-term Obsidian power users. The agent should actively help the user build this capability into their vault over time.