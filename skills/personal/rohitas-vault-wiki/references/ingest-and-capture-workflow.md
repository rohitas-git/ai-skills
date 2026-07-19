# Ingest & Capture — Rohitas's Notes

Ops skills: **`vault-inbox`** (capture), **`vault-ingest`** (compile). This doc is the schema-side pipeline.

## Pipeline

### 1. Capture
Drop into `Inbox/` via **`vault-inbox`** or manual drop. Low friction — no takeaway debate.

### 2. Classify (wiki / vault-ingest)
- ephemeral → discard/bookmark  
- hub/MOC → `Atlas/{Topic} MOC.md` only (never Concepts)  
- single concept → Concepts (`type: concept` only)  
- multi-topic → split atoms + update Atlas MOC  

### 3. Distill (**resource-summarizer** when needed)
Load **resource-summarizer** for long/raw multi-heading sources:

1. Scan structure  
2. 80/20 core extract  
3. Feynman plain-language explanations  
4. Key takeaways (5–10)  
5. Gaps / related concept names  

Map into vault shape (summary + bullets + Related). **No** full Cornell template in permanent notes.

### 4. Index-first retrieve
Before create: `README.md` → relevant Atlas MOC → search `Concepts/` (title, tags, `topic`, keywords).

### 5. Plan & confirm (vault-ingest)
Present key takeaways + Ingest plan (create / update / conflicts / archive). Wait for confirm on multi-page or conflict work.

### 6. Write / update
- New atoms or **merge** richer content into existing Concepts  
- Required frontmatter; bump `updated` on edits  
- `[[wikilinks]]`; Atlas MOC TOC updates  
- Registry row if new area  

### 7. Contradictions
Report inconsistencies in a table; do **not** silent-resolve. Options: keep old / prefer new / both with context.

### 8. Archive
Inbox originals → `Archives/Name (Source).md` with `type: literature`, `status: archived` when content was rewritten/split. Treat Source notes as immutable afterward (errata append only).

### 9. Log
Append `Archives/Ingest Log.md` (prefer dated entry + `<!-- END OF LOG -->` sentinel).

### 10. Close
Inbox empty for processed items; offer **`vault-explain`** on new/updated Concepts; optional **`vault-lint`**.

## Collision rule
Existing Concepts title wins; merge richer content via summarizer; archive Inbox copy.

## URL / online
Fetch clean page content, then same pipeline. Record URL + fetch date on Source archive note.
