# Original Obsidian Skills (Untouched)

This folder contains the **original, unmodified skills** from the official [kepano/obsidian-skills](https://github.com/kepano/obsidian-skills) repository. They are included here for reference and direct use when you need the canonical, low-level instructions for Obsidian syntax and features.

## Why Include the Originals?

- My adapted references (`obsidian-markdown-syntax.md`, `properties-and-frontmatter.md`, `dataview-plugin.md`, etc.) are **customized** for the high-level PKM management workflows in this skill (ingest, MOC creation, querying, synthesis, vault health).
- The original skills are more **foundational and syntax-focused**. They are excellent when you want the exact, official guidance without any adaptation.
- Keeping them "untouched" ensures you always have access to the authoritative source.

## Included Original Skills

### obsidian-markdown (Primary)
**Location:** `original-obsidian-skills/1-obsidian-markdown/`

- `SKILL.md` — Core instructions for creating/editing Obsidian-flavored Markdown
- `references/PROPERTIES.md` — Detailed property/frontmatter reference
- `references/EMBEDS.md` — Embed syntax for notes, images, PDFs, audio, etc.
- `references/CALLOUTS.md` — All callout types, folding, nesting, and customization

**When to load the original instead of my adapted version:**
- You want the exact official examples and tables.
- You are doing very low-level syntax work.
- You want to compare or see the source of truth.

### Other Skills in the Official Repo (Not Yet Copied)
The full repo also contains:
- `1-obsidian-bases` — For Obsidian Bases (database views)
- `1-json-canvas` — For JSON Canvas files (visual whiteboards)
- `1-obsidian-cli` — CLI interactions with Obsidian
- `1-defuddle` — Clean web page extraction to Markdown

If you need any of these added in untouched form, let me know and I can include them.

## How to Use

When the agent is working on your vault, it will primarily use the **adapted** references in the parent `references/` folder because they are integrated with the full manager workflows.

However, you (or the agent) can explicitly ask to "use the original obsidian-markdown skill" or "consult the untouched PROPERTIES.md" when you want the canonical version.

## Recommendation

For most day-to-day use with this `obsidian-notes-manager` skill, the adapted files (`properties-and-frontmatter.md` + `dataview-plugin.md` + `obsidian-markdown-syntax.md`) will be more practical because they are tailored to PKM tasks like ingestion, MOC maintenance, and synthesis.

The original files are here as your **source of truth** and for advanced or precise syntax needs.