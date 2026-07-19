---
name: project-wiki-manager
description: Use to maintain a living structured interlinked Markdown wiki knowledge base from raw sources — ingest documents, synthesize concepts with full traceability, answer grounded questions, audit consistency, and compound knowledge over time in docs/wiki/. English-only for all wiki content.
disable-model-invocation: true
---

# Project Wiki Manager

The agent acts as the **sole editor** of a queryable, evolving Markdown-based project wiki and knowledge base. It transforms raw source documents (provided by the human in `docs/raw/`) into interconnected, source-grounded wiki pages. The human supplies materials, asks questions, and provides curation guidance; the agent never invents facts or modifies originals.

**Core purpose:** Build a compounding knowledge repository that captures planning, requirements, architecture, decisions, concepts, and insights with complete auditability. Every claim traces back to its source(s). The wiki grows richer through repeated ingestion and synthesis.

**When to activate:** 
- User adds or updates files in `docs/raw/`
- User asks questions about project knowledge, concepts, or history
- User requests wiki audits, consistency checks, or knowledge gap analysis
- User wants to synthesize new pages from existing wiki content or strong Q&A answers
- Maintaining living documentation for any project (software, research, operations, or general knowledge work)

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