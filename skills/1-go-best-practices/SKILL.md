---
name: 1-go-best-practices
description: >
  Apply idiomatic Go design, error, concurrency, API, and testing practices to a Go change or
  review. Use when: writing, reviewing, or refactoring Go packages, interfaces, errors, goroutines,
  or performance-sensitive paths. Not for: generic project standards or a broad architecture review.
  Hub: /0-improve-codebase-architecture.
disable-model-invocation: true
metadata:
  catalog:
    hub: 0-improve-codebase-architecture
    role: soft
    when:
      - "write, review, or refactor Go code"
      - "choose Go error, interface, concurrency, or package patterns"
    not_when:
      - "language-neutral standards → 1-coding-standards"
      - "module boundaries across a system → 1-codebase-design"
    prev: [0-improve-codebase-architecture, 0-implement, 0-review]
    cousins: [1-coding-standards, 1-codebase-design, 1-code-review, 1-error-handling, 1-performance-optimization]
    triggers: [Go best practices, idiomatic Go, golang review, Go concurrency]
    requires_setup: false
---

# Go Best Practices

**Atomic job:** apply Go-specific design, implementation, or review judgment inside the caller's
selected candidate. Repository instructions and the declared Go/tool versions are authoritative.

## Boundary

| Need | Route |
|---|---|
| Go-specific implementation or narrow review | **this skill** |
| Cross-language conventions | `/1-coding-standards` |
| Public contract evolution | `/1-api-and-interface-design` |
| Cross-module/system design | `/1-codebase-design` or `/2-software-architect` |
| Failure policy beyond Go mechanics | `/1-error-handling` |
| Measured performance diagnosis | `/1-performance-optimization` |

## Process

1. **Inherit the caller.** Preserve repository, worktree and branch, requested paths/diff, base and
   candidate when reviewing, dirty-file ownership, acceptance criteria, and advice/read-only/edit
   authority. This skill creates no worktree, switches no branch, and never turns review into edits.
2. **Read local authority.** Inspect applicable repository instructions, `go.mod`/`go.work`, toolchain
   directives, affected packages, callers, tests, generated-code markers, and configured formatter,
   vet, linter, race, fuzz, or benchmark commands. Do not silently upgrade Go or add tooling.
3. **Apply only relevant Go judgment.** Prefer clear standard-library idioms, cohesive packages,
   small exported surfaces, and interfaces owned near consumers when they improve substitution or
   testing. One implementation can still justify a seam; do not manufacture interfaces by quota.
4. **Preserve error contracts.** Add useful operation context. Use `%w` only when callers should
   inspect or match the cause; avoid accidental compatibility commitments. Panic is for genuinely
   unrecoverable programmer/runtime invariants, not expected request or dependency failures.
5. **Prove concurrent ownership.** Identify who starts/stops goroutines, closes channels, cancels
   contexts, bounds fan-out/queues, and observes failures. Never copy synchronization-bearing values
   casually or retain caller-owned buffers without an explicit lifetime contract.
6. **Stay scoped.** Do not redesign unrelated packages, rename public symbols, edit generated/vendor
   code, replace dependencies, or optimize from intuition. Escalate public compatibility, broader
   architecture, failure policy, security, or measured performance to its owner and return afterward.
7. **Verify proportionally in the existing workspace.** Format changed Go files with the repository's
   command and run the narrowest relevant tests/checks. Add `go vet`, race, fuzz, integration, or
   benchmarks only when applicable and supported; do not imply full coverage from a focused check.
8. **Return evidence.** Report candidate/workspace identity, changed paths or read-only findings,
   commands/results, skipped checks, compatibility effects, and residual concurrency/error risks to
   the caller. Do not commit, publish, deploy, merge, install, or mutate remote/shared services.
