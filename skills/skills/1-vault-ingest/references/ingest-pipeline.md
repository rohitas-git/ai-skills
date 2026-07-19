# Ingest pipeline (vault-ingest)

## 1. Orient

1. Confirm vault root from SSOT (`docs/agents/vault.md`)
2. Load `0-rohitas-vault-wiki` → `vault-profile.md`, folder map, hard rules
3. Skim `README.md` (Registry) for areas

## 2. Materialize source

- **Text:** use as-is  
- **Inbox:** read file(s); if “process Inbox”, list all and process one-by-one or batch with one plan  
- **URL:** see `url-ingest.md`

If source is huge, summarize structure first and ask whether to full-ingest or focus sections.

## 3. Distill

Apply `resource-summarizer-contract.md`. Map distill output into:

- Short summary (1–3 sentences, own words)
- Key bullets / takeaways
- Gaps / open questions
- Candidate concept titles + related links

**No Cornell chrome** in permanent Concepts.

## 4. Key takeaways (human confirm)

Present 5–12 takeaways grounded in the source. Ask:

> Confirm, edit, or drop takeaways before I write vault pages?

Proceed only after approval (or explicit “proceed with all”).

## 5. Retrieve related vault knowledge

```
README Registry → Atlas MOC(s) → search Concepts/ (title, topic, tags, keywords)
         → read 3–10 candidate notes
```

Prefer existing Concepts over creating near-duplicates.

## 6. Classify each atom

| Class | Action |
|-------|--------|
| **New** | Propose `Concepts/<Title>.md` + hub link |
| **Update** | Propose delta merge into existing note |
| **Inconsistent** | Conflict table; wait |
| **Ephemeral** | Do not vault; suggest browser bookmark |

## 7. Ingest plan

Show plan template from SKILL.md. Wait if any of: >2 pages, any conflict, Registry change, new hub.

Single short atom with no conflict and user already said “ingest this as X” may proceed after stating the one-line plan.

## 8. Apply (after confirm)

1. Follow `Guides/Note Templates.md` shapes  
2. Frontmatter: `type`, `status`, `tags`, `created`, `updated` (+ `topic`, `source`)  
3. Status default for new concepts: `incubating` unless user wants `active`  
4. Update Atlas MOC links  
5. New area → Registry row in `README.md`  
6. Archive: `Archives/<Unique Name> (Source).md` with `type: literature`, `status: archived`  
7. Remove or empty processed Inbox files  

## 9. Log

Append to `Archives/Ingest Log.md`:

```markdown
## YYYY-MM-DD | source-id | Created: [[A]], [[B]] | Updated: [[C]] | Conflicts open: …
<!-- END OF LOG -->
```

If sentinel missing, add it once after the new entry.

## 10. Close report

```markdown
## Ingest complete
- Created: …
- Updated: …
- Archived: …
- Open conflicts: …
- Next: `/1-vault-explain` on [[…]]?  `/1-vault-lint`?
```
