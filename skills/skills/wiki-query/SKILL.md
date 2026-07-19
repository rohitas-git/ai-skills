---
name: wiki-query
description: >
  Answer questions against a personal LLM wiki / Obsidian vault using Karpathy-style
  query workflow (index first, read compiled pages, synthesize with citations, file
  valuable answers back). Use whenever the user asks a question about their notes,
  wiki, vault knowledge, second brain, MOCs, Concepts, "what do my notes say",
  "query the wiki", "answer from the vault", comparison from notes, or /wiki-query —
  even if they do not say "query". Prefer this skill over raw RAG-style guessing
  when a vault or wiki is available. Pairs with rohitas-vault-wiki for vault layout.
---

# Wiki Query

Run **LLM Wiki Query**: answer from a **compiled** knowledge base (wiki/vault pages), not by re-deriving everything from raw sources every time.

Primary sources for this skill:
- [Karpathy LLM Wiki gist](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f) — Query as a core operation; file good answers back
- Community implementations (index-first retrieval, `queries/` filing, log append)
- This vault’s `rohitas-vault-wiki` layout when the user is in Rohitas’s Notes

## Core idea (why this exists)

Classic RAG re-discovers fragments on every question. An LLM wiki **compiles** knowledge into interlinked pages. Query means:

1. Find the right **already-compiled** pages  
2. Synthesize an answer **with citations**  
3. Optionally **file** the answer so exploration compounds  

You are the disciplined wiki reader, not a generic chatbot inventing facts.

## Default vault (Rohitas)

If the user is working on Rohitas’s Notes (or path unset):

**Vault root:** resolve from SSOT only — consumer repo `docs/agents/vault.md` (written by `/setup-rohitas-skills`), or the `## Agent skills` vault pointer. Do **not** hard-code a home path in this skill. If unset, ask once and offer to write the SSOT.

| LLM Wiki concept | This vault |
|------------------|------------|
| `index.md` | `README.md` (Knowledge Registry) + Atlas `* MOC.md` |
| Wiki pages | `Concepts/` (atoms), `Atlas/* MOC.md` (hubs only) |
| `queries/` | `Queries/` (filed answers) |
| `log.md` | `Archives/Query Log.md` (and optionally mention in Ingest Log) |
| Raw sources | `Archives/* (Source).md`, `Inbox/` (prefer Concepts over raw) |
| Schema | `rohitas-vault-wiki` + `Guides/Note Templates.md` |

If another wiki path is configured (`WIKI_PATH` or user states a path), map that wiki’s `index.md` / `wiki/` / `queries/` instead.

## When to activate

- User asks a domain question that should be grounded in notes  
- “What do my notes say about…”, “compare X and Y from the vault”  
- Explicit `/wiki-query` or “query the wiki”  
- After ingest, user wants synthesis across multiple Concepts  

**Do not use** for pure vault maintenance (folder moves, bulk structure) — use `rohitas-vault-wiki`.  
**Do not use** as a substitute for ingesting a new source — use **`vault-ingest`** first, then query.  
**Do not use** for single-Concept teaching — use **`vault-explain`** → `learning-explainer`.

## Mandatory orientation (every session / every query)

Before answering:

1. Read **`README.md`** (Registry) — which areas exist  
2. Open the **most relevant Atlas MOC(s)** for the topic  
3. Optionally skim last ~15 lines of **`Archives/Query Log.md`** so you don’t re-file duplicates  
4. For large vaults (100+ pages) or thin MOCs: **search** `Concepts/` (and tags/`topic:`) for keywords  

Do **not** dump the whole vault into context. Index → few pages → synthesize.

## Query workflow

### 1. Clarify (only if needed)

If the question is ambiguous, ask one tight clarifying question. Otherwise proceed.

### 2. Retrieve (index-first, not full-scan)

```
Registry / MOC  →  candidate Concept titles
        ↓
keyword/topic search if needed
        ↓
read 3–10 best pages (prefer Concepts over Archives)
        ↓
follow [[wikilinks]] one hop if gaps remain
```

Prefer **compiled Concepts** over Archives `(Source)` dumps. Use Archives only when Concepts are thin or missing.

### 3. Synthesize

- Answer in clear prose (or table if comparison)  
- Cite wiki pages: `Based on [[Write-Through Cache]] and [[Write-Back (Write-Behind) Cache]]…`  
- Call out contradictions and **open questions** from notes  
- Mark confidence: **high** (multiple solid Concepts), **medium** (single thin note), **low** (mostly gap)  

### 4. Response format (always for non-trivial answers)

```markdown
## Answer
{synthesis with [[wikilinks]]}

## Sources
- [[Note A]] — why used
- [[Note B]] — …

## Gaps
- {what the vault does not contain}

## File back?
{yes/no recommendation} → proposed title under Queries/ or Concepts/
```

### 5. File valuable answers (compound)

**File** when the answer is a comparison, decision framework, multi-note synthesis, or something painful to re-derive.

**Do not file** trivial lookups already answered by a single Concept’s first paragraph.

#### Filing rules (this vault)

1. Create `Queries/{Title Case Name}.md` using template in `references/query-page-format.md`  
2. `type: query` (allowed for Queries only — not a Concept hub)  
3. Link parent Atlas MOC + source Concepts in `## Related`  
4. Optionally add one bullet on the relevant **Atlas MOC** under a “Filed queries” section  
5. Append to `Archives/Query Log.md`:

```markdown
## [YYYY-MM-DD] query | short question
- Filed: [[Query Page Title]]  OR  not filed
- Sources: [[A]], [[B]]
```

6. If the answer should become permanent teaching knowledge, also propose promoting key points into a **Concept** via **`vault-ingest`** / `rohitas-vault-wiki` (don’t skip frontmatter / templates). To *learn* an existing Concept, offer **`vault-explain`**.

Human-in-the-loop: if filing would create 5+ new pages or rewrite MOCs heavily, propose first and wait for approval. Single query page + log is OK to write when the user asked to “query and file” or previously approved auto-file.

### 6. Vault gap protocol

If the vault cannot answer:

```markdown
## Vault gap
Not found in compiled notes (checked: README, [MOCs], search for …).

**Options:**
1. Answer from general knowledge (label as *not from vault*)
2. Ingest a source with **vault-ingest** (schema: rohitas-vault-wiki) first
3. Create a stub Concept + open questions for ROOT study
4. Health-check related area with **vault-lint** if structure looks broken
```

Never present invented personal/project facts as vault knowledge.

## Answer shapes

| Question type | Prefer |
|---------------|--------|
| Definition | Short synthesis + link main Concept |
| Comparison | Table + `Queries/` page often worth filing |
| Decision “when should I…” | Criteria list + cite strategy notes |
| “What do I know about X?” | MOC walk + bullet map of Concepts |
| Deep dive | Multi-section answer; file if novel |

Optional outputs (if user asks): Marp outline, checklist, Dataview snippet for related notes.

## Search tips (agent tools)

```bash
# By topic property
rg -n '^topic: System Design' Concepts --glob '*.md'

# By content
rg -n -i 'write-through|write-back' Concepts Atlas --glob '*.md'

# Filed queries
ls Queries/
rg -n 'query \|' Archives/Query\ Log.md | tail -20
```

At larger scale, hybrid search (FTS/embeddings) is optional; until then index + ripgrep is the default (Karpathy: index first; search when the wiki grows).

## Hard rules

1. Orient via Registry + MOC before deep reads  
2. Cite `[[pages]]`; don’t claim vault support without pages  
3. Prefer Concepts over Archives for answers  
4. File only non-trivial answers; log every query attempt when writing files  
5. Hubs stay in Atlas as `* MOC.md` — never create hubs in Concepts  
6. Query pages live in `Queries/` with `type: query`  
7. Coordinate layout with `rohitas-vault-wiki`; this skill owns **query + file-back**  
8. Sibling ops: `vault-inbox` (capture), `vault-ingest` (compile), `vault-lint` (health), `vault-explain` (teach Concept)  

## References

- `references/karpathy-query-principles.md` — gist-aligned theory  
- `references/query-page-format.md` — frontmatter + body for filed queries  
- `references/vault-map.md` — Rohitas folder map for retrieval  
- Schema: `rohitas-vault-wiki`  
- Ingest: `vault-ingest` · Lint: `vault-lint` · Explain: `vault-explain` · Capture: `vault-inbox`  

