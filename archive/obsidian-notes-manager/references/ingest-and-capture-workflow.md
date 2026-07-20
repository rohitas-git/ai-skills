# Ingest and Capture Workflow for Obsidian

Ingestion turns raw ideas, meeting notes, web articles, PDFs, or quick thoughts into high-quality, linked Obsidian notes that integrate into your knowledge graph.

## General Principles
- Capture fast, refine thoughtfully.
- Always add wikilinks to existing relevant notes.
- Use properties for metadata from day one.
- Prefer creating atomic notes over monolithic long notes.
- Human confirmation before major new notes or restructuring.

## Step-by-Step Ingest Process

### 1. Receive Raw Material
- Pasted text, email, meeting transcript, web page content, PDF text, voice note transcription, etc.
- Or a new file dropped into `Inbox/` (or wherever you capture).

### 2. Understand & Extract Key Takeaways
- Read/summarize the source.
- Identify main concepts, decisions, facts, action items, and relationships.
- Note any existing notes this should connect to (`[[Existing Note]]`).

### 3. Propose Structure to User (Confirmation)
Present a clear plan:
- Suggested note title(s)
- Key properties (tags, status, type, etc.)
- Main sections / headings
- Important wikilinks to create or use
- Whether to split into multiple atomic notes + one MOC update

Wait for explicit approval or edits before writing files.

### 4. Create / Update Notes with Proper Obsidian Formatting
- Create new `.md` file(s) in appropriate folder (Inbox → later moved, or directly to Notes/).
- Start with clean YAML frontmatter.
- Write content using full Obsidian syntax (wikilinks, embeds if useful, callouts for key points).
- Add block IDs `^id` for important paragraphs worth referencing later.
- At the end or in a "Related" section, list outgoing links.

### 5. Update Related Notes and MOCs
- Add backlinks or mentions in relevant existing notes where natural.
- Update or create MOC(s) that should include the new note.
- This is where the graph grows stronger.

### 6. Log the Action (Lightly)
- Optionally append to a "Changelog" note or your Daily Note: "Created [[New Note Title]] from [source description] and linked to X, Y, Z."

### 7. Post-Ingest Review
- Offer a summary of what was created/linked.
- Suggest next actions (e.g., "Would you like me to create a MOC for this topic?" or "Process the rest of Inbox?").

## Special Cases

**Web content / Articles**:
- Clean the content first (remove ads, navigation — similar to Defuddle approach).
- Extract title, author, date, key quotes.
- Create a literature note or concept note with proper citation in properties or a Sources section.
- Embed or link to original if saved as PDF/webarchive.

**Meeting notes / Conversations**:
- Use a consistent template with properties (date, participants, decisions, action items).
- Link to people notes (if you have them) and topic notes.
- Extract action items into their own notes or a dedicated section with `> [!todo]` callouts.

**Quick capture from mobile or fleeting thoughts**:
- Often land in Inbox or Daily Note.
- The agent can help "process Inbox" by turning bullet points into proper linked notes.

**PDFs / Books / Papers**:
- Extract text or key passages.
- Create literature notes with bibliographic properties.
- Link concepts to your own developing ideas.

## Nuances & Quality Focus
- **Don't over-link on first pass**: Start with the most obvious and important connections. More links can be added later during review or Q&A.
- **Atomic vs. composite**: If the source covers multiple distinct ideas, propose splitting into several notes + one synthesizing MOC.
- **Properties consistency**: Try to use the same core property keys across similar note types so your future Bases and queries work reliably.
- **Confirmation is key**: Especially for new MOCs or when moving notes between folders. The user owns the mental model.
- **Large sources**: For very long documents, focus on high-signal extraction rather than transcribing everything. Offer to create multiple targeted notes.

## Why Good Ingestion Matters
Poor ingestion creates "note debt" — unlinked, untagged, poorly titled notes that are hard to find later. Excellent ingestion compounds: each new note makes the entire vault smarter and more discoverable through the graph and search.

The agent should treat every ingest as an opportunity to strengthen the overall knowledge network, not just dump content.