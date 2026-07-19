# Vault Profile — Rohitas's Notes

## Identity

| Field | Value |
|-------|--------|
| Vault name | Rohitas's Notes |
| Path | ``docs/agents/vault.md` → vault_root` |
| Model | Single PKM |
| Schema skill | `rohitas-vault-wiki` |
| Content skill | `resource-summarizer` (long/raw sources) |
| Teach skill | `vault-explain` → `learning-explainer` |
| Query skill | `wiki-query` |
| Ops skills | `vault-inbox`, `vault-ingest`, `vault-lint` |
| Skill source | `~/Development/AI-Skills/skills/rohitas-vault-wiki` |
| Grok install | `~/.grok/skills/rohitas-vault-wiki` |
| In-vault symlink | `Guides/skills/rohitas-vault-wiki` |

## Dual-skill contract (distill)

1. **wiki skill** decides *where* and *how* notes live (folders, YAML, links, archives).
2. **resource-summarizer** decides *what the permanent prose says* for long/raw inputs (80/20, Feynman, takeaways).
3. Wiki skill always wins on path, naming, and schema.
4. Do not dump full Cornell/summarizer templates into Concepts — map into normal note shape.

## Summarizer gate

| Lines / shape | Action |
|---------------|--------|
| \> ~40 lines or multi-heading dump | Full **resource-summarizer** → then file |
| ~15–40 lines | Light Feynman rewrite + bullets |
| \< ~15 lines, one idea | Place + frontmatter only |
| `* MOC` hub (links + short gloss) | Atlas hub; no body rewrite |

## Philosophy

1. Ephemeral vs persistent  
2. Atomic notes + link-first  
3. 3-sentence / own-words (via summarizer)  
4. ROOT before mass rabbit holes  
5. Knowledge Registry in `README.md`  
6. Atlas = maps only as `* MOC.md`; Concepts = atoms only (no hubs)  
7. Weekly GC → Archives  

## Naming

- Title Case + spaces  
- Archives: unique `… (Source).md`  

## Frontmatter minimal

```yaml
---
type: concept   # concept | hub | guide | project | literature | query
status: incubating  # active | incubating | stable | archived
tags: [system-design]
created: 2026-07-19
updated: 2026-07-19
topic: System Design
---
```
