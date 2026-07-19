---
name: vault-ingest
description: >
  Ingest knowledge into Rohitas's Notes: process chat text, Inbox files, or URLs;
  create or update Concepts; report inconsistencies; log; offer vault-explain.
  Uses resource-summarizer for long sources and rohitas-vault-wiki for schema.
  Use when the user says ingest, process inbox, update vault with, put this in
  the wiki, compile this source, or /vault-ingest.
---

# Vault Ingest

Compile source material into the living vault (LLM Wiki **Ingest** op).

**Vault root:** `/Users/rohitasbansal/Development/Obsidian/Rohitas-Notes`  
**Schema:** always load **`rohitas-vault-wiki`** first.  
**Distill:** long/raw → always load **`resource-summarizer`** (see contract).  
**Teach after:** offer **`vault-explain`** → `learning-explainer`.

## Inputs

| Input | Action |
|-------|--------|
| Chat / paste | Treat as source material |
| `Inbox/*` or “process Inbox” | Read capture(s) |
| URL | Fetch clean content (prefer **defuddle** / page fetch), then ingest |

## Mandatory workflow

Load full steps from `references/ingest-pipeline.md`. Summary:

1. **Orient** — vault-profile, path, Registry glance  
2. **Materialize** — text / Inbox / URL body  
3. **Distill** — if long: **`resource-summarizer`** (`references/resource-summarizer-contract.md`)  
4. **Takeaways** — 5–12 grounded bullets; **confirm** with user  
5. **Retrieve** — Registry → MOC → search Concepts (index-first)  
6. **Classify** — new | update | inconsistent per atom  
7. **Ingest plan** — show before multi-page or conflict writes  
8. **After confirm** — write/update with templates + frontmatter; archive Source; clear processed Inbox  
9. **Log** — `Archives/Ingest Log.md`  
10. **Close** — report pages; open conflicts; offer **`/vault-explain`**; suggest **`/vault-lint`** if large  

## Ingest plan template

```markdown
## Ingest plan
- Source: …
- Takeaways (confirmed): …
- Related: [[A]], [[B]]
- Create: …
- Update: … (delta)
- Conflicts: … (need your call)
- Archive: → Archives/… (Source).md ?
- Distilled with: resource-summarizer | light | none
```

## Inconsistencies (required when found)

```markdown
## Inconsistencies
| Claim (new) | Existing note | Existing claim | Options |
|-------------|----------------|----------------|---------|
| … | [[Note]] | … | keep old / prefer new / both with context |
```

Do **not** silent-resolve. Details: `references/merge-and-contradiction.md`.

## Completion criterion

- Plan shown; after approval, every planned create/update applied with valid frontmatter  
- Conflicts resolved per user or listed open  
- Summarizer used when gate fires  
- Ingest Log entry written  
- Explain handoff offered for new/substantially updated Concepts  

## Hard rules

1. Ground claims; no invented personal facts  
2. Confirm multi-page/conflict plans  
3. Merge over duplicate  
4. Wiki skill owns path/schema; summarizer owns long prose quality  
5. Sources in Archives are immutable after write (errata append only)  
6. English permanent notes unless user overrides  

## References

- `references/ingest-pipeline.md`
- `references/merge-and-contradiction.md`
- `references/url-ingest.md`
- `references/resource-summarizer-contract.md`
- `references/karpathy-and-wiki-principles.md`
- Sibling schema: `rohitas-vault-wiki`
