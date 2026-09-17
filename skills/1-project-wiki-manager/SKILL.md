---
name: 1-project-wiki-manager
description: >
  Build, query, or audit a grounded in-repository concept wiki from declared project sources.
  Use for project wiki pages, source-backed Q&A, and wiki health checks. Not for: code-to-doc
  synchronization governance (1-living-documentation-governor), personal Obsidian notes
  (0-rohitas-vault-wiki), or design-time domain decisions (1-domain-modeling).
  Hub: /0-improve-codebase-architecture.
disable-model-invocation: true
metadata:
  catalog:
    hub: 0-improve-codebase-architecture
    role: soft
    when:
      - "build, query, or audit a grounded in-repository concept wiki"
    not_when:
      - "code-synced documentation governance → 1-living-documentation-governor"
      - "personal Obsidian vault → 0-rohitas-vault-wiki"
      - "design-time glossary or ADR decision → 1-domain-modeling"
    prev: [0-improve-codebase-architecture]
    cousins: [1-living-documentation-governor, 0-rohitas-vault-wiki, 1-domain-modeling]
    triggers: [project wiki, project wiki manager, ingest project sources, query project wiki, audit project wiki]
    requires_setup: false
---

# Project Wiki Manager

**Atomic job:** maintain or interrogate one repository's source-grounded concept wiki without
changing its source material or silently expanding into living-doc governance.

## Boundary

| Need | Route |
|---|---|
| Concept wiki synthesis, query, or health audit | **this skill** |
| Docs whose ownership/triggers track code changes | `/1-living-documentation-governor` |
| Personal Notes/Obsidian knowledge | `/0-rohitas-vault-wiki` |
| Domain model or ADR while designing | `/1-domain-modeling` |
| Extract one long external resource | `/1-resource-summarizer` or its format specialist |

F-D1/F-D2 apply only when the destination is genuinely unclear. Clear project-wiki requests route
directly; do not ask the user to choose again or load a cousin implicitly.

## Process

1. **Pin caller, mode, and workspace.** Resolve the project root, exact current worktree/branch/HEAD,
   requested wiki/source roots, dirty-file ownership, and query/audit/write authority. This skill
   creates no worktree and switches no branch. For authorized repository edits, reuse a matching
   caller workspace; if isolation is actually required, call `/1-git-worktrees`, then return here.
2. **Discover local authority.** Read applicable repository instructions and existing documentation
   conventions. Prefer an established wiki layout. Propose `docs/raw/` plus `docs/wiki/` only when no
   convention exists, and create it only when the user's request authorizes initialization.
3. **Declare the source universe.** Default raw sources are immutable. User-named project docs,
   source code, tests, schemas, or decisions may be read when needed, but must be identified and
   cited; do not imply code access when it was not inspected. Never rewrite source material during
   synthesis. Use [workspace and source rules](./references/folder-structure-and-initialization.md).
4. **Choose one mode.** Query and audit are read-only. Ingest/update writes only the requested wiki
   surface and its existing index/log when applicable. An explicit request to ingest or update is
   sufficient authority; pause only for a material ambiguity such as competing roots, unclear source
   authority, destructive restructuring, or a high-blast page split the user has not selected.
5. **Ground and synthesize.** Separate observed source claims, agent synthesis, user-confirmed facts,
   conflicts, and unknowns. Use precise locators and the repository's page conventions. Merge into an
   existing concept when it is the same subject; do not create pages by quota. See
   [ingest](./references/ingest-workflow.md), [grounding](./references/citation-and-grounding-rules.md),
   and [page contract](./references/page-formats-and-templates.md).
6. **Verify the bounded result.** For writes, inspect the diff and validate page names, internal
   links, cited source paths/locators, index coverage, and log consistency using existing tools. Do
   not install a wiki tool, run unrelated formatters, or modify generated/vendor/source files. For a
   read-only audit, report findings without repairing them.
7. **Return to the caller.** Report mode, project/worktree/HEAD, source and wiki roots, pages read or
   changed, grounding/coverage gaps, conflicts, checks, and remaining decisions. Do not commit,
   publish, deploy, merge, or mutate remote knowledge systems.

## Load only for the selected mode

- Initialization/layout: [folder structure](./references/folder-structure-and-initialization.md)
- Ingest/update: [ingest workflow](./references/ingest-workflow.md), [page contract](./references/page-formats-and-templates.md), [grounding](./references/citation-and-grounding-rules.md)
- Query: [question answering](./references/question-answering-workflow.md)
- Audit/logging: [logging and audit](./references/logging-and-audit.md)
- Hard boundaries or unusual sources: [hard rules](./references/hard-rules-and-constraints.md), [edge cases](./references/edge-cases-and-nuances.md)
