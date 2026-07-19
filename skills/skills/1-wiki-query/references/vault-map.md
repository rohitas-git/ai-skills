# Rohitas vault map (for retrieval)

**Vault root:** resolve from SSOT only — consumer repo `docs/agents/vault.md` (written by `/0-setup-rohitas-skills`), or the `## Agent skills` vault pointer. Do **not** hard-code a home path in this skill. If unset, ask once and offer to write the SSOT.

```
README.md              # Knowledge Registry (start here)
My Dashboard.md        # status: active notes
Atlas/                 # * MOC.md hubs only
Concepts/              # atomic notes only
Queries/               # filed query answers (type: query)
Guides/                # methodology, templates, ops
Archives/              # literature sources + Query Log + Ingest Log
Inbox/                 # capture only
Projects/              # active work
```

## Retrieval order for a typical question

1. `README.md` → pick Area → open Atlas MOC  
2. Read linked Concepts from the MOC  
3. `rg` Concepts by keyword / `topic:` if MOC incomplete  
4. Archives only if Concepts thin  
5. File non-trivial synthesis under `Queries/`  
6. Log in `Archives/Query Log.md`

## Companion skills

| Skill | Use for |
|-------|---------|
| `1-wiki-query` | Answer + file queries |
| `0-rohitas-vault-wiki` | Ingest, structure, templates, MOCs |
| `1-resource-summarizer` | Distill long raw text before filing Concepts |
