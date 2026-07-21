---
name: 1-vault-ingest
description: >
  Ingest knowledge into Rohitas's Notes (chat/Inbox/URLs → Concepts). Use for ingest,
  process inbox, compile source into wiki. Not for: fast capture only (1-vault-inbox) or query notes
  (1-wiki-query). Hub: /0-rohitas-vault-wiki. Triggers: ingest, process inbox, put this in the wiki.
disable-model-invocation: true
metadata:
  catalog:
    hub: 0-rohitas-vault-wiki
    role: pipeline
    when:
      - "compile sources into Concepts"
      - "process inbox into vault"
    not_when:
      - "quick capture only → 1-vault-inbox"
      - "ask notes a question → 1-wiki-query"
    next: [1-vault-explain]
    prev: [1-vault-inbox]
    triggers:
      - "ingest"
      - "process inbox"
      - "put this in the wiki"
      - "1-vault-ingest"
    requires_setup: false
---

# Vault Ingest

## Process

1. Follow the steps and hard rules in this skill.
2. Load linked `references/` only when the branch needs them.

## Boundary

| Need | Skill |
|------|--------|
| Compile sources into Rohitas vault Concepts | **vault-ingest** (this) |
| Fast capture only (no Concepts) | `/1-vault-inbox` |
| Distill long source first | `/1-resource-summarizer` |
| Query vault | `/1-wiki-query` |
| Lint vault health | `/1-vault-lint` |
| Teach a Concept after ingest | `/1-vault-explain` |
| Project repo wiki (not personal vault) | `/1-project-wiki-manager` (F-D2) |


Compile source material into the living vault (LLM Wiki **Ingest** op).

**Vault root:** resolve from SSOT only — consumer repo `docs/agents/vault.md` (written by `/0-setup-rohitas-skills`), or the `## Agent skills` vault pointer. Do **not** hard-code a home path in this skill. If unset, ask once and offer to write the SSOT.
**Schema:** always load **`0-rohitas-vault-wiki`** first.  
**Distill:** long/raw → always load **`1-resource-summarizer`** (see contract).  
**Teach after:** offer **`1-vault-explain`** → `1-learning-explainer`.

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
3. **Distill** — if long: **`1-resource-summarizer`** (`references/resource-summarizer-contract.md`)  
4. **Takeaways** — 5–12 grounded bullets; **confirm** with user  
5. **Retrieve** — Registry → MOC → search Concepts (index-first)  
6. **Classify** — new | update | inconsistent per atom  
7. **Ingest plan** — show before multi-page or conflict writes  
8. **After confirm** — write/update with templates + frontmatter; archive Source; clear processed Inbox  
9. **Log** — `Archives/Ingest Log.md`  
10. **Close** — report pages; open conflicts; offer **`/1-vault-explain`**; suggest **`/1-vault-lint`** if large  

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
- Distilled with: 1-resource-summarizer | light | none
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
- Explain 1-handoff offered for new/substantially updated Concepts  

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
- Sibling schema: `0-rohitas-vault-wiki`
