# Plan phases a caller can verify

Plan from the accepted design. A small obvious change can have a short inline plan; do not execute
a planning-only request. For an empirical unresolved choice, propose or run a separately authorized
prototype; a product preference remains a user decision. The implementation plan does not reopen
settled scope or require a new interview by default.

Map independent units and dependencies: intended change, actual file/contract surface, immediate
parent/base, blocking prerequisites, observable result, owner, allowed effects and verification.
For multi-PR work, distinguish independent branches from genuine stacked dependencies. Do not invent
PR numbers before they exist; use provisional unit IDs and later map real PR identities.

Each unit ends at a meaningful evidence boundary. Establish a before-state for equivalence or a
red-capable oracle where appropriate. Select unit/integration/runtime/performance checks by the actual
change and repository contract; record not-applicable dimensions with reasons rather than forcing
all three on every documentation or mechanical change. Missing required evidence remains unproven.

Name review/approval gates, service/data isolation, invalidation and rollback/reconciliation conditions.
Return the plan and unknowns. Execution, commits, PRs, delegated owners and merge start only under
the caller's existing explicit task/operation scope. Never make the word plan grant those effects.

Adapted from the individually reviewed pstack 0.15.43 sources, MIT, Lauren Tan.
[Source-by-source decisions and checks](../../../guidelines/catalog/pstack-methods-review-2026-11-18.md).
