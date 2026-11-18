---
name: 1-typescript-best-practices
description: >
  Design, implement, or review one bounded TypeScript type/data contract. Use for discriminated
  unions, boundary parsing, brands, exhaustive variants, schema-derived types or unsafe assertions.
  Not for generic naming, a whole API design, or changing repository toolchains. Hub: /0-implement.
disable-model-invocation: true
license: MIT
metadata:
  catalog:
    hub: 0-implement
    role: soft
    when: [apply TypeScript type and boundary discipline to scoped code]
    not_when: [generic maintainability conventions, whole public API design, compiler or dependency upgrades]
    prev: [0-implement, 1-codebase-design, 1-coding-standards]
    next: [0-implement]
    cousins: [1-coding-standards, 1-codebase-design, 1-error-handling, 1-api-and-interface-design]
    triggers: [TypeScript best practices, discriminated union, branded types, unsafe type assertion, schema-derived types]
    requires_setup: false
  vendor:
    source: cursor/plugins
    upstream_id: pstack/skills/typescript-best-practices
    commit: e1cc03121a0e71129a4fb730d7c5528a0a3e43c8
---

# TypeScript contracts

Make the type express the operation's actual guarantees while keeping runtime boundaries honest.
Inherit the caller's candidate, review/edit mode and permitted paths; use the repository's compiler,
schemas, branding conventions, logger and test stack. Install or upgrade nothing implicitly.

## Boundary

| Need | Owner |
|---|---|
| Scoped TypeScript representation, parsing and narrowing | This skill |
| General naming and cohesion | `/1-coding-standards` |
| Module ownership/interface design | `/1-codebase-design` |
| Error propagation or recovery policy | `/1-error-handling` |
| Whole public API and compatibility | `/1-api-and-interface-design` |

## Process

1. Trace producers and consumers, units, lifecycle variants, empty cases, mutation and external inputs.
   State which wrong combinations or argument substitutions the representation should reject.
2. Use discriminated unions for exclusive variants. Keep ordinary arrays where empty input is valid;
   use a nonempty tuple or an optional result only where the operation requires that distinction.
   Prefer derived values over fields that must remain synchronized.
3. Parse external `unknown` with existing schemas or complete guards, then pass named domain values
   internally. Derive types from authoritative schemas/generated definitions. Do not add a validation
   dependency for one guard, or revalidate trusted immutable values without a real boundary reason.
4. Use semantic brands only for a demonstrated mixing risk. A constructor must check the runtime
   invariant; a predicate annotation is a promise the compiler does not verify. Preserve live checks
   for authorization, shared/mutable state, persistence, untyped callers and invalidated invariants.
5. Prefer real narrowing and exhaustive handling over `any`, unchecked assertions or non-null `!`.
   `satisfies` checks compatibility; literal inference still depends on context. `as const` and justified
   boundary assertions are different from claiming unvalidated JSON has a domain type.
6. Verify with the existing strict compiler and focused behavior tests. Include a rejected invalid
   shape and a valid control when a type invariant is the point; include runtime invalid inputs for
   checks that types cannot enforce. A successful typecheck is not runtime or security proof.
7. Return the representation, actual guarantees, evidence, justified exceptions and unrun checks.
   Preserve public contracts and caller authority; no automatic broad rewrite, commit or publication.

Load [patterns and source corrections](./references/patterns.md) for examples and exceptions.
