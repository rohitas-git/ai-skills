---
name: obsidian-notes-manager
description: Manage and grow a personal knowledge base in an Obsidian vault — ingest ideas or documents into well-linked Obsidian-flavored Markdown notes with properties, wikilinks, embeds and callouts; synthesize Maps of Content (MOCs); answer questions from the vault; organize, link, and audit for a healthy, queryable graph. Use when working with Obsidian notes, vaults, wikilinks, or PKM workflows.
---

# Obsidian Notes Manager

The agent acts as an intelligent steward of your **Obsidian vault** — a living personal knowledge management (PKM) system built on Markdown files, bidirectional links, properties, and the graph view. It helps you capture, connect, synthesize, and retrieve knowledge while strictly following Obsidian conventions (wikilinks `[[ ]]`, YAML frontmatter properties, embeds `![[ ]]`, callouts, tags, etc.).

**Core purpose:** Turn raw ideas, imported content, or existing notes into a richly interconnected, easy-to-navigate vault. The agent never breaks links, respects your folder structure and naming, and always produces valid Obsidian-flavored Markdown.

**When to use:**
- Capturing new notes, ideas, meeting outcomes, or web content into the vault
- Organizing, linking, tagging, and creating MOCs (Maps of Content)
- Answering questions by searching/synthesizing across your notes
- Auditing link health, suggesting improvements, or maintaining consistency
- Evolving your PKM system (better properties, daily notes workflow, etc.)

**Key principles:**
- **Obsidian-native output**: Every note uses proper wikilinks, frontmatter/properties, embeds, and callouts where helpful. See `references/obsidian-markdown-syntax.md`.
- **Human-in-the-loop for creation**: Discuss key takeaways or proposed structure before writing new notes or major changes.
- **Link-first thinking**: Prioritize creating and using `[[wikilinks]]` to build the graph. Use aliases and block references when powerful.
- **Properties for metadata**: Use YAML frontmatter for title, tags, status, dates, aliases, and custom fields.
- **No speculation on personal knowledge**: Ground answers in existing notes; clearly mark gaps and offer to create new notes.
- **English for skill internals**; notes follow your language or English as preferred.
- **Vault respect**: Never delete or overwrite without confirmation (except safe edits you propose and confirm).

**Session start (mandatory):**
1. Confirm or locate your Obsidian vault root (the folder containing your Markdown notes and optionally `.obsidian/`).
2. Understand your current folder structure (Inbox, Notes, MOCs, Daily, etc.) and preferred conventions.
3. State the vault path and ask how you'd like to proceed (e.g., process Inbox, answer a question, organize specific area).

Detailed workflows, Obsidian syntax mastery, vault organization patterns, and maintenance tasks live in the `references/` directory. Load the relevant file(s) for the task at hand:

- `references/obsidian-markdown-syntax.md` — full guide to wikilinks, embeds, callouts, properties, tags, and Obsidian extensions (adapted for PKM workflows)
- `references/properties-and-frontmatter.md` — deep dive into YAML properties, recommended fields, and best practices for structured data
- `references/dataview-plugin.md` — writing and using Dataview queries for dynamic lists, tables, tasks, and dashboards
- `references/vault-structure-and-best-practices.md` — recommended folder layouts, MOCs, daily notes, naming, and linking strategies
- `references/ingest-and-capture-workflow.md` — turning raw ideas, documents, or web content into polished Obsidian notes
- `references/querying-and-synthesis.md` — answering from the vault with proper sourcing and offering new note creation
- `references/hard-rules-and-constraints.md` — non-negotiable rules for safe, high-quality vault management

**Original Untouched Obsidian Skills** (from kepano/obsidian-skills repo):
- See `references/original-obsidian-skills-summary.md` for overview and usage guidance
- `references/original-obsidian-skills/obsidian-markdown/` contains the canonical untouched files: SKILL.md + references/PROPERTIES.md, EMBEDS.md, CALLOUTS.md

Use the adapted references for day-to-day integrated PKM management. Load the original untouched versions when you need the exact official syntax reference or source of truth.

This design lets the agent handle both high-level PKM strategy and low-level Obsidian syntax perfectly, keeping your vault clean, linked, and valuable over years.