# Lint checklist — Rohitas's Notes

Run as many checks as practical. For large vaults, sample high-traffic Registry topics + recently touched notes from Ingest Log.

## 1. Broken wikilinks

Scan `[[Target]]` in Concepts, Atlas, Guides, Projects, Queries. Flag targets with no matching `.md` (Title Case + spaces; consider aliases if present).

## 2. Orphans

Concepts with no inbound link from any Atlas MOC (and ideally weak inbound from other Concepts). Suggest MOC attachment or archive if obsolete.

## 3. Misplaced hubs

- Any `* MOC.md` or `type: hub` under `Concepts/` → move to Atlas  
- Atlas files not named `* MOC.md` that behave as hubs → rename or reclassify  

## 4. Frontmatter

Missing or invalid on permanent notes:

- Required: `type`, `status`, `tags`, `created`, `updated`  
- Valid status: `active` | `incubating` | `stable` | `archived`  
- Valid type for folder (concept/hub/guide/project/literature/query)

## 5. Near-duplicates

Similar titles or heavily overlapping scopes (e.g. two cache strategy notes that should be one + links). Suggest merge or scope boundary.

## 6. Stale / Dashboard noise

- `incubating` notes long untouched (if dates available)  
- Too many `status: active` (Dashboard sprawl) — suggest `stable`  

## 7. Missing concept stubs

Hubs or bodies mention important ideas without a Concept page. Suggest stub + open questions (ROOT).

## 8. Cross-page contradictions

For sampled related Concepts under the same topic: conflicting definitions, “always” vs “never”, outdated supersession. Report table; do not resolve.

## 9. Inbox / archive hygiene

- Non-empty Inbox backlog  
- Processed material still only in Inbox  
- Missing `(Source)` archives after known multi-page ingests (heuristic)

## 10. Registry drift

`README.md` areas without hubs, or hubs/topics not reflected in Registry status.

## 11. Invalid source references

`source:` or links to Archives that do not exist.

## 12. Template / format drift

Permanent Concepts missing useful structure vs `Guides/Note Templates.md` (soft hygiene, not always critical).

## Tooling tips

```bash
cd "$(vault_root from docs/agents/vault.md)"
ls Inbox/
rg -n '^type:|^status:' Concepts Atlas --glob '*.md' | head
rg -n '\[\[[^\]]+\]\]' Concepts Atlas --glob '*.md' | head
```

Prefer structured search over dumping entire vault into context.
