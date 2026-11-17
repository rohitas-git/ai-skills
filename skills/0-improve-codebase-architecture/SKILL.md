---
name: 0-improve-codebase-architecture
description: 'Route architecture requests or run a bounded, read-only deepening scan. Use when: designing an API/module/system, finding architecture improvements, or requesting an architecture candidate report. Not for: hard bug diagnosis (0-diagnosing-bugs), fixed-diff review (1-code-review), or implementation without a design question (0-implement). Hub: /0-improve-codebase-architecture.

  '
disable-model-invocation: true
metadata:
  catalog:
    hub: 0-improve-codebase-architecture
    role: hub
    when: ['route API, module, system, failure, retirement, or architecture-improvement work', run a bounded architecture deepening scan or candidate report]
    not_when: [debug hard bug → 0-diagnosing-bugs, fixed PR/diff review → 1-code-review, implement a settled design → 0-implement]
    next: [1-change-impact, 0-grilling, 1-api-and-interface-design, 1-clean-craftsmanship, 1-codebase-design, 1-coding-standards, 1-deprecation-and-migration, 1-error-handling, 1-go-best-practices, 1-graphify, 1-living-documentation-governor, 1-project-wiki-manager, 2-software-architect]
    cousins: [0-diagnosing-bugs, 0-implement, 0-review]
    triggers: [improve architecture, architecture scan, architecture report, API architecture, module design, system design, gRPC contract design]
    requires_setup: false
---


# Improve Codebase Architecture

**Hub job:** dispatch a specific architecture request; only broad improvement requests run the
scan below. Selected children return their contract, decision, or findings to the caller.

## Boundary and dispatch

| Need | Route |
|---|---|
| Discover bounded deepening candidates | **this hub's scan** |
| Public API/GraphQL/gRPC contract | `/1-api-and-interface-design` |
| One internal module interface or seam | `/1-codebase-design` |
| Whole-system alternatives or trade-offs | `/2-software-architect` |
| Failure behavior or recovery design | `/1-error-handling` (F-EH1 if diagnosis is plausible) |
| Consumer cutover or old-path retirement | `/1-deprecation-and-migration` |
| Principles discussion versus enforceable coding rules | `/1-clean-craftsmanship` versus `/1-coding-standards` (F-C1) |
| Go-specific design/code practice | `/1-go-best-practices` |
| Explicit local code graph | `/1-graphify` |
| Project concept wiki versus code-synced docs | `/1-project-wiki-manager` versus `/1-living-documentation-governor` (F-D1) |

Use F-ARCH1 only when API/module/system scope is genuinely unclear. Clear requests route directly.
Do not combine children automatically. A child may recommend another specialist, but the caller's
mode, scope, candidate, workspace, and authority remain unchanged.

## Bounded scan

1. **Pin evidence and scope.** Record caller, repository and current worktree/branch, requested paths
   or subsystem, comparison/base when relevant, existing dirty-state ownership, and whether output
   is Markdown or explicitly requested static HTML. A scan is read-only and creates no worktree.
2. **Read local constraints.** Inspect applicable repository instructions, domain vocabulary, ADRs,
   ownership, tests, and architecture docs if present. Bound broad scans to the changed/hot area or
   a stated sample; report excluded areas rather than implying whole-repository coverage.
3. **Explore locally by default.** Trace callers, dependencies, effects, tests, and recent change
   evidence with read-only tools. Use `/1-codebase-design` heuristics without forcing its vocabulary
   over established terms. Delegate read-only exploration only when the user explicitly requests
   sub-agents and scopes are independent.
4. **Rank evidence-backed candidates.** For each, state files, observed friction, proposed module or
   system change, expected leverage/locality, compatibility/migration cost, verification plan,
   confidence, and contradictory evidence. Do not infer a refactor solely from file size, adapter
   count, method count, or the deletion test.
5. **Present the report.** Markdown is the default. If static HTML was requested, follow
   [HTML-REPORT.md](./HTML-REPORT.md), write only to an approved output path or unique OS-temp file,
   and return the path. Do not open an app or load remote scripts/assets without separate authority.
6. **Return or deepen.** Stop at the report unless the user selects a candidate or already requested
   a design. F9 routes a selected candidate to `/1-grill-with-docs` or Agent judgment. Durable domain
   or ADR edits go through `/1-domain-modeling` only when separately authorized; never create or
   modify project docs as a scan side effect.
7. **Implement only when requested.** Send an agreed design and evidence to `/0-implement`. It owns
   workspace isolation, edits, verification, review, and any authorized commit. This hub never
   switches branches, stashes work, installs tools, starts services, publishes, deploys, or merges.

## Output contract

Return scope/worktree identity, evidence sources, ranked candidates or routed child result,
assumptions, excluded areas, conflicts with existing decisions, and the next user-owned decision.
Label scans partial whenever evidence does not cover the whole requested repository.

## Available specialist additions

- `/1-change-impact` — use for its scoped contract; return to this hub.
