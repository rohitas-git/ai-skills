---
name: 1-api-and-interface-design
description: >
  Design stable public APIs and cross-module contracts (REST, GraphQL, gRPC, types). Use when:
  defining or evolving a consumer-visible interface, compatibility policy, or trust-boundary schema.
  Not for: internal module shape (1-codebase-design), failure-policy mechanics (1-error-handling),
  model-facing tool schemas (1-tool-schema-design), or complete MCP servers (1-mcp-server-building).
  Hub: /0-improve-codebase-architecture.
disable-model-invocation: true
metadata:
  catalog:
    hub: 0-improve-codebase-architecture
    role: soft
    when:
      - "designing public interfaces, versioning contracts, or validating at trust boundaries"
    not_when:
      - "internal module shape → 1-codebase-design"
      - "failure-policy mechanics → 1-error-handling"
      - "model-facing tool schema → 1-tool-schema-design"
      - "complete MCP server → 1-mcp-server-building"
    next: [0-implement, 1-error-handling, 1-deprecation-and-migration, 1-code-review]
    prev: [0-improve-codebase-architecture, 0-implement]
    cousins: [1-codebase-design, 1-error-handling, 1-tool-schema-design, 1-mcp-server-building, 1-deprecation-and-migration]
    triggers:
      - "1-api-and-interface-design"
      - "api and interface design"
      - "API contract"
      - "version this API"
      - "gRPC API"
    requires_setup: false
---

# API and Interface Design

**Atomic job:** produce or assess one consumer-visible contract and its evolution rules.
Load the [adapted operative guide](./references/full-guide.md) for protocol patterns and
the [source map](./references/vendor-source.md) for provenance and exclusions.

## Boundary

| Need | Skill |
|------|-------|
| Design stable public APIs or module interfaces | **`/1-api-and-interface-design` (this)** |
| Design a module’s internal shape and seam | `/1-codebase-design` |
| Make a whole-system architecture decision | `/2-software-architect` |
| Define detailed failure, retry, or cleanup behavior | `/1-error-handling` |
| Retire an already-consumed contract | `/1-deprecation-and-migration` |
| Design a model-facing tool schema or complete MCP server | `/1-tool-schema-design` or `/1-mcp-server-building` |
| Change database schema | `/1-supabase-schema-migration` when Supabase owns it; otherwise the project's migration workflow |

## Process

1. **Pin mode and scope.** Record caller, design/advice versus read-only assessment versus authorized implementation, repository/worktree when applicable, consumers, owners, and stability promise. Do not turn design or review into edits.
2. **Inspect evidence.** Read existing routes, schemas/types, compatibility tests, consumers, repository conventions, and relevant runtime versions. Mark unknown consumers or operational constraints; do not invent them.
3. **Write the contract matrix.** For each operation capture authentication and object authorization, input/output schema, effects, error/failure outcomes, pagination or streaming, retry/idempotency behavior, limits, and compatibility expectations. Delegate detailed recovery mechanics to `/1-error-handling` and schema mutation to its database owner.
4. **Choose the narrowest fitting protocol and evolution rule.** Define the actual OpenAPI/type/schema/protobuf artifact when requested. Treat additions as compatible only after checking consumer behavior; reserve or deprecate fields deliberately and plan migration through `/1-deprecation-and-migration` when consumers must move.
5. **Verify and return.** Check representative positive, negative, authorization, compatibility, retry/duplicate, and limit cases that apply. Return the contract, decisions, evidence, assumptions, unresolved questions, and skipped checks to the caller.

## Hard rules

- Contract advice and read-only assessment create no worktree. Authorized edits reuse the caller's matching workspace after confirming repository, branch, worktree path, dirty-state ownership, and scope. Use `/1-git-worktrees` only when isolation is needed, then resume and return to that caller.
- `/0-implement` is the conditional implementation handoff; `/1-code-review` follows only an implemented change. Neither is automatic permission to edit, commit, publish, deploy, or inspect unrelated code.
- Prefer evidence and small reversible steps.
- Do not invent APIs, metrics, or CI status — verify in the repo/env.
- When overlapping another skill, load the specialist (see Related).

## Related

For an AI feature's consumer boundary, load [AI integration contract](./references/ai-integration-contract.md).

- **Primary:** Architecture soft. **Conditional caller:** Ship (`/0-implement`).
- **Returns:** contract/advice to the requester; implemented diff to Ship, then its normal review path.
