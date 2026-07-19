---
name: rohitas-vault-wiki
description: >
  Steward Rohitas's Notes Obsidian vault — Atlas hubs, Concepts atoms, Inbox capture,
  Guides/Projects/Archives, Dashboard-aligned frontmatter, Title Case notes, ROOT +
  Knowledge Engineering. Schema source for vault-inbox, vault-ingest, vault-lint,
  vault-explain, and wiki-query. Orchestrates resource-summarizer for long/raw sources.
  Use for Rohitas's Notes, vault structure, Atlas MOCs, Concepts, or /rohitas-vault-wiki.
disable-model-invocation: true
---

# Rohitas Vault Wiki

**Vault root:** resolve from SSOT only — consumer repo `docs/agents/vault.md` (written by `/setup-rohitas-skills`), or the `## Agent skills` vault pointer. Do **not** hard-code a home path in this skill. If unset, ask once and offer to write the SSOT.

Single-PKM steward and **schema source of truth**. Do **not** use Notes/MOCs/Resources defaults or dual `raw/`/`wiki/` unless the user reopens that decision.

## Skill family (ops)

| Skill | Role | Slash |
|-------|------|-------|
| **rohitas-vault-wiki** (this) | Schema, folders, frontmatter, templates | `/rohitas-vault-wiki` |
| **vault-inbox** | Fast capture → `Inbox/` only | `/vault-inbox` |
| **vault-ingest** | Compile sources → create/update Concepts; report conflicts | `/vault-ingest` |
| **vault-lint** | Health check (report-only by default) | `/vault-lint` |
| **vault-explain** | Teach a Concept → **`learning-explainer`** | `/vault-explain` |
| **wiki-query** | Query + file answers | `/wiki-query` |
| **resource-summarizer** | Long/raw distill (80/20, Feynman) — do not fork | (invoked by ingest) |
| **learning-explainer** | Pedagogy for explain — do not fork | (invoked by vault-explain) |

**Route by intent:** clear capture → `vault-inbox`; process knowledge → `vault-ingest`; health → `vault-lint`; teach concept → `vault-explain`; Q&A → `wiki-query`. Load this skill’s profile for path/schema whenever any sibling runs.

## Dual-skill distill

| Skill | Role |
|-------|------|
| **rohitas-vault-wiki** (this) | Classify, place, frontmatter, links, archives, registry |
| **resource-summarizer** | Distill long/raw: 80/20, Feynman own-words, takeaways, gaps |

**Rule:** For notes roughly **>40 lines** or multi-heading dumps, load **resource-summarizer** before writing Concepts. Map summary → Concept body (**no Cornell chrome**). Short atoms: frontmatter + place only. Wiki skill wins on path, naming, and schema.

## Shared policy (all ops)

1. **Grounding** — permanent claims grounded in source, user statement, or existing notes; mark thin claims `[needs verification]`.
2. **No invention** of personal/project facts.
3. **Merge over duplicate** — prefer update + highlight differences.
4. **Ingest confirm** — key takeaways + plan before multi-page/conflict writes.
5. **Conflicts wait** — never silent-resolve contradictions.
6. **Lint report-only** unless user says fix.
7. **Inbox** — low friction; no takeaway debate on capture.
8. **Index-first** — Registry + MOC + search before create.
9. **Log** — append `Archives/Ingest Log.md` (sentinel-friendly).
10. **Sources immutable** — do not casually rewrite `Archives/* (Source).md`.
11. **English** permanent notes (unless user overrides).
12. **No new top-level folders** without asking.
13. After new/updated Concepts, offer **`/vault-explain`**.

## Session start

1. Confirm vault root above.
2. Load `references/vault-profile.md`.
3. Check `README.md`, `Inbox/`, `Atlas/`.
4. If intent is inbox/ingest/lint/explain/query → **delegate** to that skill (keep this profile loaded).
5. Otherwise state path and ask how to proceed.

## Folder map

| Folder | Purpose | type |
|--------|---------|------|
| `Inbox/` | Capture only | process out |
| `Atlas/` | **Only hubs** — `* MOC.md` | `hub` |
| `Concepts/` | **Atoms only** — never `type: hub` | `concept` |
| `Guides/` | Methodology + ops + templates | `guide` |
| `Projects/` | Active work | `project` |
| `Archives/` | Literature sources (unique names) | `literature` |
| `Queries/` | Filed answers (`wiki-query`) | `query` |
| `README.md` | Knowledge Registry | hub |
| `My Dashboard.md` | `status: active` Dataview | hub |

## Naming & frontmatter

- Title Case with spaces: `Computer Memory.md`
- **Hubs:** `Atlas/{Topic} MOC.md` only. Use `aliases` for short link names.
- **Never** put hubs or MOCs in `Concepts/`
- Required: `type`, `status`, `tags`, `created`, `updated`
- Optional: `topic`, `source`, `aliases`
- status: `active` | `incubating` | `stable` | `archived`

## Ingest pipeline (schema view)

1. Capture → Inbox (`vault-inbox`) or direct material  
2. Classify: hub | concept | multi | ephemeral  
3. **If long/multi → resource-summarizer**  
4. Write/update Atlas hubs / Concepts atoms (`vault-ingest`)  
5. Archive sources as `Name (Source).md`  
6. Update Registry + links + Ingest Log  
7. Inbox empty for processed items  
8. Offer `vault-explain` / `vault-lint` as needed  

## Note templates

Follow vault guide **`Guides/Note Templates.md`**. Prefer named templates (concept-core, strategy, glossary, hub-moc, etc.).

## References

- `references/vault-profile.md`
- `references/vault-structure-and-best-practices.md`
- `references/properties-and-frontmatter.md`
- `references/ingest-and-capture-workflow.md`
- `references/hard-rules-and-constraints.md`
- `references/seed-concept-map.md`
- `references/obsidian-markdown-syntax.md`
- `references/dataview-plugin.md`
- `references/querying-and-synthesis.md`

## Boundary (project vs personal knowledge)

| Need | Skill |
|------|--------|
| Personal Rohitas’s Notes (Atlas/Concepts/Inbox) | **rohitas-vault-wiki** (this) + vault-* ops |
| In-repo project concept wiki | `/project-wiki-manager` |
| Code-synced living docs / triggers | `/living-documentation-governor` |

### Fork F-D2

**Project repo wiki or personal Rohitas’s Notes vault?**

- **Vault** (this) — **recommended** if user says notes, Concepts, Atlas, Inbox, “my wiki”
- **Project wiki** → `/project-wiki-manager`
- **Living docs / triggers** → `/living-documentation-governor`

Ask once; never silent-redirect. Do not implement project `docs/wiki` or doc-triggers here.

## Out of scope

- Editing `.obsidian/` unless asked (except ignore filters for skill symlink)
- Overwriting generic `obsidian-notes-manager`
- Replacing `resource-summarizer` or `learning-explainer` (invoke, do not fork)
- Project-repo wiki or living-docs governor jobs (F-D2 / F-D1)
