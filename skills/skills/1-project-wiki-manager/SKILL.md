---
name: 1-project-wiki-manager
description: >
  Karpathy-style in-repo project wiki: docs/raw/ → docs/wiki/ concept pages,
  grounded Q&A, audit, compound knowledge. English-only wiki content. Not
  code↔docs trigger governance (/1-living-documentation-governor) or personal
  Obsidian Notes (/0-rohitas-vault-wiki). Soft under Architecture domain.
disable-model-invocation: true
---

# Project Wiki Manager

**Atomic job:** sole editor of a queryable **project** Markdown wiki at `docs/wiki/`, synthesized from `docs/raw/`.

## Boundary

| Need | Skill |
|------|--------|
| In-repo concept wiki (`docs/raw` → `docs/wiki`) | **project-wiki-manager** (this) |
| Code-synced living docs + trigger maps | `/1-living-documentation-governor` |
| Personal Rohitas’s Notes vault | `/0-rohitas-vault-wiki` |
| Domain glossary / ADRs while designing | `/1-domain-modeling` |

## Hard redirect / forks

| Fork | Question | Recommended | Branches |
|------|----------|-------------|----------|
| **F-D1** | Concept wiki from sources, or living docs tied to code paths/triggers? | wiki if raw→concepts | this · `/1-living-documentation-governor` |
| **F-D2** | Project repo wiki or personal Notes vault? | vault if Concepts/Atlas/my notes | this · `/0-rohitas-vault-wiki` |

Ask once (recommended first), wait — never silent-load the cousin.

**Core purpose:** compounding knowledge with full source auditability. Human supplies materials and confirms writes; agent never invents facts or modifies originals in `docs/raw/`.

**When to activate:**
- User adds or updates files in `docs/raw/`
- User asks questions about **project** wiki knowledge
- Wiki audits, consistency checks, gap analysis
- Synthesize new wiki pages from existing wiki or strong Q&A

**Key principles (always follow):**
- Ground every factual statement in explicit sources; mark unsourced claims clearly.
- All wiki pages, index, log entries, and internal reasoning: **English only**.
- Never modify, delete, or invent content in `docs/raw/` or any original sources.
- Human confirmation required before creating or significantly updating wiki pages during ingestion.
- Use precise wiki-links `[[page-name]]` to interconnect concepts.
- Prefer merging and highlighting differences over duplication.
- Keep answers clear, complete, and structured; offer to persist high-value syntheses as new wiki pages.

**Session start (mandatory):**
1. Locate or confirm the project root (parent directory containing `docs/`).
2. Verify or initialize `docs/raw/` and `docs/wiki/` structure if missing.
3. Confirm with user before any wiki modifications.
4. State the resolved paths clearly.

Detailed instructions for each major workflow are maintained in the `references/` directory. Load the relevant file(s) when performing specific tasks:

- `references/folder-structure-and-initialization.md` — layout, paths, and session setup
- `references/ingest-workflow.md` — processing new or updated raw sources
- `references/page-formats-and-templates.md` — standard page and index structure
- `references/citation-and-grounding-rules.md` — quotes, citations, handling contradictions
- `references/question-answering-workflow.md` — how to answer from wiki or raw, mandatory response format, wiki gaps
- `references/logging-and-audit.md` — append-only log, lint/audit commands
- `references/hard-rules-and-constraints.md` — immutability, naming, no-speculation, and forbidden actions
- `references/edge-cases-and-nuances.md` — multiple sources, large ingests, visuals, uncertainty, knowledge compounding, scalability

This modular design keeps the core skill lightweight while providing comprehensive, on-demand depth for reliable long-term wiki stewardship.