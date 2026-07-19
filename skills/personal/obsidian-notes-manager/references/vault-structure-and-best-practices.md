# Vault Structure and Best Practices for Obsidian

A healthy Obsidian vault balances **structure** (folders for broad categories) with **connection** (wikilinks and MOCs for emergent relationships). There is no single perfect structure — the best one is the one you will actually maintain. The agent helps evolve your structure over time.

## Recommended Starting Folder Layout (Flexible)
Many effective vaults use variations of this pattern:

```
Your Vault/
├── Inbox/                  # Quick capture zone (new notes, imports, web clippings)
├── Notes/                  # Main atomic notes and concept notes
├── MOCs/                   # Maps of Content — hub notes that organize topics
├── Daily/                  # Daily notes (or use Periodic Notes plugin)
├── Projects/               # Active project notes and planning
├── Resources/              # Reference material, PDFs, images, templates
├── Archives/               # Old or completed notes (still linked)
└── .obsidian/              # Obsidian settings (do not edit manually)
```

Alternative popular patterns:
- Flat + heavy linking (minimal folders, rely on graph and search)
- PARA method (Projects, Areas, Resources, Archives)
- Johnny Decimal or custom numbering
- Folder-per-topic with MOCs inside

**Agent guidance**: At session start, ask about or observe your current structure and suggest incremental improvements rather than forcing a big reorganization.

## Core Concepts & Patterns

### Atomic Notes
Each note should ideally focus on **one clear idea, concept, or piece of knowledge**. Keep them concise but complete. Link liberally to related notes.

### Maps of Content (MOCs)
A MOC is a special note that acts as a table of contents / index for a topic. It contains many `[[wikilinks]]` to related notes, often with brief descriptions or groupings.

Example MOC structure:
```markdown
---
title: Knowledge Management
tags: [moc, pkm]
---

# Knowledge Management

## Core Principles
- [[Atomic Notes]]
- [[Linking is Thinking]]
- [[ Evergreen Notes ]]

## Tools & Systems
- [[Obsidian]]
- [[Zettelkasten]]
- [[PARA Method]]

## My Implementation
- [[My Daily Note Template]]
- [[How I Use Properties]]
```

MOCs are living documents — update them as you create new notes.

### Daily Notes / Periodic Notes
Use for journaling, quick capture, meeting notes, or habit tracking. Link from daily notes to permanent notes. Many users enable the Daily Notes or Periodic Notes core plugin.

### Linking Strategy (Most Important)
- Create `[[wikilinks]]` as you write — don't wait for the perfect note name.
- Use aliases `[[Long Note Name|short name]]` for readability.
- Link *to* headings and blocks when precision matters: `[[Note#^insight-42]]`
- Bidirectional linking happens automatically in Obsidian.

### Properties Best Practices
- Keep a consistent set of core properties across note types (created, updated, tags, status, type).
- Use tags for broad categorization and quick filtering (`#project/active`, `#area/health`).
- Custom properties enable powerful Bases (database views) and queries.

## Agent Best Practices When Working in Your Vault
- **Respect existing structure**: Learn your folders and naming conventions first. Suggest changes; don't impose.
- **Prefer evolution over revolution**: Small, consistent improvements (adding a few good links, creating one MOC) compound beautifully.
- **Inbox zero for notes**: Help process Inbox regularly — turn quick captures into atomic notes with proper links and properties.
- **MOC maintenance**: When you see a topic with many related notes but no hub, propose creating or updating an MOC.
- **Graph health**: Notes with few or no links are "orphans" — suggest connections. Notes with too many links may need splitting.
- **Naming**: Use clear, descriptive, kebab-case or Title Case filenames that read well as wikilinks. Avoid overly long names.

## Nuances & Edge Cases
- **Very large vaults** (thousands of notes): Folders + MOCs + good properties become essential for navigation. Search and Graph still work but benefit from curation.
- **Collaborative or shared vaults**: Be extra careful with properties and naming; document conventions in a meta note.
- **Plugins you rely on**: The agent should be aware of (or ask about) plugins like Dataview, Templater, Periodic Notes, Excalidraw, etc., as they affect workflows.
- **Mobile vs Desktop**: Structure should work reasonably on mobile (avoid extremely deep folders).

## Why Structure + Linking Matters
Folders provide initial orientation. Wikilinks + MOCs + Graph View create the emergent, associative structure that makes Obsidian magical for long-term thinking and discovery. The agent's job is to strengthen both the explicit structure *and* the implicit connections.

The agent should periodically offer light audits or suggestions to keep the vault from becoming a tangled or neglected garden.