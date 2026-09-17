# Ticket-set decomposition guidance

## Boundary test

A ticket is well bounded when it has one observable outcome, a coherent verification story, and can be
reviewed and reverted without silently requiring unrelated scope. File count, elapsed time, token budget,
title conjunctions, and architectural layer count are warning signals at most—never sizing laws.

Split when outcomes, owners, rollout/rollback decisions, acceptance evidence, or shared-resource authority
are independently meaningful. Keep work together when separation would leave an unverifiable half-state or
break compatibility.

## Shape selection

- Prefer a thin end-to-end behavior slice when it can land safely and remain green.
- For incompatible contract changes, use explicit expand → migrate callers/data → contract tickets.
- Keep schema and data/backfill work separate when failure and rollback boundaries differ.
- Put slow or operationally risky work behind its own authority and verification gate.
- Represent a true shared contract once; dependent tickets reference it rather than restating it.

## Dependencies and concurrency

Dependencies must form a directed acyclic graph justified by real inputs or state transitions. The ready
frontier contains tickets whose recorded blockers are satisfied; it is informational until an execution
workflow selects work. Tickets are parallel-eligible only when they do not share files, generated outputs,
databases, local service instances, tracker mutations, deployment targets, locks, or other mutable resources—
or when explicit coordination makes that sharing safe. A Git worktree alone does not isolate those resources.

## Evidence checkpoint

Each ticket names the smallest evidence that demonstrates its own outcome. Cross-ticket checkpoints belong
only where an integration, compatibility, migration, or release invariant cannot be proved inside one ticket.
Do not create ceremonial checkpoints by fixed ticket counts.
