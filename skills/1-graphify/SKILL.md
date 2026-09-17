---
name: 1-graphify
description: >
  Build or query an explicitly requested local Graphify codebase graph, keeping graph evidence
  distinct from source verification. Use when: Graphify, codebase knowledge graph, graphify query,
  graphify path, or graphify explain is explicitly requested. Not for: general codebase review
  (1-codebase-review-strategy), architecture decisions (2-software-architect), or project wiki work
  (1-project-wiki-manager). Hub: /0-improve-codebase-architecture.
disable-model-invocation: true
argument-hint: "[extract|query|path|explain] <approved local target or question>"
metadata:
  catalog:
    hub: 0-improve-codebase-architecture
    role: satellite
    when:
      - "explicit Graphify local codebase graph or graph query"
      - "query, trace, or explain an existing Graphify graph"
    not_when:
      - "general codebase review planning → 1-codebase-review-strategy"
      - "architecture strategy or decision → 2-software-architect"
      - "grounded project wiki creation or query → 1-project-wiki-manager"
    prev: [0-improve-codebase-architecture]
    cousins: [1-codebase-review-strategy, 2-software-architect, 1-project-wiki-manager, 1-diagram-maker]
    triggers: [graphify, "codebase knowledge graph", "graphify query", "graphify path", "graphify explain"]
    requires_setup: false
  vendor:
    source: Graphify-Labs/graphify
    commit: 23f2ffaa43fd12f25d9eabe91e6d184b5d89b474
    license: Apache-2.0 AND MIT
---

# Graphify

**Atomic job:** build or interrogate one explicitly requested local code graph while keeping its
artifact, worktree, freshness, and inference limits visible. The full upstream workflow is
[archived](../../archive/vendor/graphify/VENDOR-SOURCE.md); it is not operative or installed here.

## Boundary

| Need | Skill |
|---|---|
| Explicit, approved local Graphify extract/query/path/explain | **this skill** |
| Scope and plan a codebase review | `/1-codebase-review-strategy` |
| Evaluate architecture direction or trade-offs | `/2-software-architect` |
| Build or query a grounded project wiki | `/1-project-wiki-manager` |
| Draw a hand-authored architecture diagram | `/1-diagram-maker` |

## Process

1. **Pin caller and target.** Preserve the caller's mode and question. Resolve the corpus and graph
   paths explicitly; when the corpus is a Git repository, record its repository root, exact
   worktree/branch/HEAD, and dirty-state ownership. This skill never creates or switches worktrees.
2. **Classify the operation.** `query`, `path`, and `explain` read an existing `graph.json`; `extract`
   writes an artifact set. Do not translate conceptual “build” into a nonexistent `graphify build`
   subcommand. Use an explicit `--graph` path for reads and an explicit output directory for writes.
3. **Validate ownership and freshness.** Confirm an existing graph's root marker/metadata points to
   the approved corpus and report whether it predates the candidate HEAD or dirty files. Before an
   extract, inspect the output path and Git status. Do not overwrite an unknown/user-owned artifact,
   share one mutable output across worktrees, or use `--force`/`--allow-partial` without separate,
   evidence-based authorization.
4. **Use the installed local tool only.** Verify the executable and version. If absent, stop with the
   exact missing prerequisite; installation is a separate `/1-discover-skills` or package-management
   decision. Do not use `uvx`, `pip`, or another implicit downloader as a fallback.
5. **Default to code-only extraction.** For an explicitly requested build, use
   `graphify extract <absolute-corpus> --code-only --out <approved-output>` (or the installed version's
   equivalent after checking help). This avoids semantic/model backends. Do not disable repository
   ignore rules unless the user explicitly includes ignored material and its privacy implications.
6. **Keep reads local and non-persistent.** Run the smallest requested `query`, `path`, or `explain`
   against the pinned graph and disable optional query logging for that invocation. Do not start a
   server, MCP process, watcher, browser, or background task.
7. **Verify claims at source.** `EXTRACTED` means source-derived and `INFERRED` means resolver-derived;
   neither proves runtime behavior, correctness, security, or architectural intent. Inspect the cited
   source and tests before returning any such claim; label stale, ambiguous, missing, and conflicting
   evidence.
8. **Return evidence and ownership.** Report operation, corpus/worktree/HEAD, graph and output paths,
   CLI version, artifact mutation state, useful results, source checks, freshness, exclusions, and
   uncertainty to the caller. Graph artifacts are not committed or published unless separately asked.

## Hard limits

- Never run `graphify install`, `graphify codex install`, hook setup, strict mode, `--watch`, or any other persistent instruction/configuration change unless the user separately requests and authorizes that exact change.
- Never install Graphify or its extras as a side effect of an extract/query request.
- Never clone a repository, use URLs as corpus input, start MCP, or launch background work without separate authorization.
- Never enable a remote/API/LLM backend, read provider keys, push to Neo4j/FalkorDB/Postgres, or perform live database introspection without separate explicit authorization.
- Do not include docs, PDFs, images, audio, video, or semantic extraction by default: those can invoke model/backend processing and need an explicit target, privacy discussion, and authorization.
- Do not modify source files, stage/commit graph artifacts, or make Graphify an always-on instruction
  for an agent as a consequence of this skill.

## Related

Use this only through explicit invocation such as `$1-graphify extract /approved/project` or
`$1-graphify query "what calls X?"`. Its upstream installer, hook policy, autonomous
subagent extraction, remote backends, and persistence behavior remain archive-only.
