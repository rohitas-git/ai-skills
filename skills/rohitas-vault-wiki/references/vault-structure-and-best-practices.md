# Vault Structure — Rohitas's Notes

## Layout

```
Rohitas's Notes/
├── README.md              # Knowledge Registry
├── My Dashboard.md
├── Index.base             # optional Bases
├── Inbox/                 # capture only
├── Atlas/                 # HUBS / MOCs only
├── Concepts/              # atoms
├── Guides/                # ROOT, KE, Vault Operations, Note Templates, skills/
├── Projects/
├── Archives/              # literature sources
└── .obsidian/
```

## Atlas vs Concepts

| Atlas (hub) | Concepts (atom) |
|-------------|-----------------|
| Topic map / MOC **only** | One idea |
| Lists `[[links]]` + short intro | Definition, principles, examples |
| `type: hub` | `type: concept` |
| Filename **must** be `… MOC.md` | Title Case idea name — **never** `* MOC.md` |

**Hard rule:** No hubs in `Concepts/`. If a note is a map, it lives in Atlas as `Name MOC.md` (add `aliases` for old short titles).

## Agent practices

- Prefer evolution of hubs after ingest batches  
- Fix broken `[[wikilinks]]`  
- Unique archive titles  
- Ignore `Guides/skills/` in Obsidian graph  
