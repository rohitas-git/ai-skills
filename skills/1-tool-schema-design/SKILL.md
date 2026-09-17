---
name: 1-tool-schema-design
description: >
  Design or review one bounded model-facing tool contract, including arguments, external authority, effects, errors, and selection tests. Use when: creating or correcting function-calling, MCP, plugin, or agent-action schemas. Not for: general APIs (1-api-and-interface-design), complete MCP servers (1-mcp-server-building), or approval-policy design (1-human-in-the-loop). Hub: /0-agent-engineering.
disable-model-invocation: true
license: MIT
metadata:
  catalog:
    hub: 0-agent-engineering
    role: leaf
    when:
      - "creating or correcting model-facing tool schemas"
      - "a model chooses the wrong tool or invents arguments"
    not_when:
      - "general API design → 1-api-and-interface-design"
      - "complete MCP server → 1-mcp-server-building"
      - "approval workflow/policy → 1-human-in-the-loop"
    prev: [0-agent-engineering, 1-mcp-server-building, 1-human-in-the-loop, 2-prompt-injection-defense]
    next: [0-agent-engineering, 1-mcp-server-building, 1-human-in-the-loop, 1-agent-evaluation, 2-prompt-injection-defense]
    cousins: [1-api-and-interface-design, 1-mcp-server-building, 1-human-in-the-loop]
    triggers: [tool schema, function calling, function-calling schema, MCP tool, structured tool input, tool arguments]
    requires_setup: false
  vendor:
    source: seb1n/awesome-ai-agent-skills
    upstream_id: tool-schema-design
    commit: 75865a5d037a4cdaa7f409a4ec14ab9b0292920b
---

# Tool Schema Design

## Boundary

| Need | Skill |
|------|-------|
| Model-facing tool contract | **this skill** |
| General public API or module boundary | `/1-api-and-interface-design` |
| MCP server transport and implementation | `/1-mcp-server-building` |
| Human approval policy and lifecycle | `/1-human-in-the-loop` |
| Broad prompt-injection trust-boundary assessment | `/2-prompt-injection-defense` |

## Process

1. Pin caller, intent, target provider/schema dialect, neighboring tools, implementation candidate, exclusions and mode: **design-only**, **read-only review**, or **authorized edit**. A security/review caller stays read-only. For a code/PR candidate load [the shared candidate contract](../0-review/references/review-candidate.md); context outside scope establishes behavior, not permission to fix it.
2. Read [schema patterns](./references/schema-patterns.md). Define one coherent user intent and decide whether different permissions, effects, required fields or retry semantics require separate tools. Avoid mirroring every backend endpoint or adding speculative tools.
3. Design the model-facing name, selection description and smallest supported argument shape. Bound unknown fields, lengths, counts, numeric limits and distinguishable conditional branches according to the actual provider. Keep actor, tenant, credentials, authorization and approval evidence in trusted runtime state—not model arguments.
4. Specify the execution contract outside JSON Schema: allowed effect/target, server-side policy, preview/confirmation binding, idempotency, timeout/retry/status lookup, partial result and safe error/output envelope. Schema constraints improve calls; they do not enforce authorization, prevent SSRF/path escape, or make model output trusted.
5. Design-only/review returns a contract or findings without editing. For authorized edits, verify the matching repo/worktree and dirty ownership; use `/1-git-worktrees` only when isolation is needed, then return here. Do not switch branches, stash, install dependencies, reset shared services, or change backend behavior outside the approved contract.
6. If useful, run the [bundled validator](./references/validator-contract.md) on one explicit task-owned JSON file. Then use the target provider's **already-installed local/offline** validation path when available. Networked provider calls, new credentials, package installs and billable model evaluation require corresponding authority; otherwise record the limitation.
7. Test parsing and runtime policy separately. Use mocks/stubs or an authorized disposable environment for invalid/boundary/stale/denied/confirmation/retry cases, and contrast prompts for this tool, neighbors and no-tool. Never let schema validation or selection evaluation trigger the real consequential action. Return artifacts, evidence and gaps to the caller; do not automatically implement a server, publish, commit or launch another review.

## Conditional handoffs

- Approval lifecycle → `/1-human-in-the-loop`; reusable selection/behavior evaluation → `/1-agent-evaluation`; full MCP transport/server → `/1-mcp-server-building`; prompt-injection boundary → `/2-prompt-injection-defense`. Carry caller mode, candidate and allowed effects; each returns to the originating workflow. `next` is not an automatic pipeline.
- Source provenance and adaptations → [source adaptation](./references/source-adaptation.md). The upstream snapshot is historical, not a second required workflow.
