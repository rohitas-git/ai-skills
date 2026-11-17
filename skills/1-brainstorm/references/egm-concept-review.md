# Optional Elephant-Goldfish concept review

Modified adaptation of Google EGM `egm-brainstorm`, Apache-2.0.
[Source, license, and adaptations](../../1-design-review/references/source-review.md).
Use only when a caller explicitly requests Goldfish/EGM concept stress-testing or authorizes fresh
reviewers. Ordinary brainstorming retains its existing memo-only, no-delegation boundary.

1. Anchor the concept: user/problem, current workaround, outcome, constraints, non-goals, viable
   alternatives and unresolved decisions. Sustained clarification belongs to `/0-grilling`.
2. Give fresh reviewers only the anchored hypothesis and allowed sources, without earlier dialogue
   (`fork_turns="none"`). Require read-only findings; obey runtime concurrency limits. If fresh
   contexts are unavailable, report that the Goldfish pass did not run. Do not simulate independence.
3. Cover six lenses, without manufacturing risks or metrics: (a) contrarian/YAGNI and existing reuse,
   (b) cost, throughput, quota and token economics, (c) user/developer ergonomics, (d) migration,
   compatibility and rollback, (e) observability and incident diagnosis, (f) coupling, technical debt
   and long-term maintenance. One reviewer may cover several named lenses within the stated budget;
   report actual coverage and failures, not an invented six-reviewer swarm.
4. Consolidate objections with source IDs and evidence. The context-rich author returns alternatives,
   trade-offs, recommendation, constraints and unresolved risks; owner decisions remain explicit.
5. Return the concept brief as the requested memo. If a durable `concepts_brief.md` was authorized,
   use only its pinned caller-owned destination; ordinary brainstorming grants no file write.
   Record overview, goals/non-goals, alternatives weighed and rejection reasons, key decisions,
   evidence and remaining questions. Never invent a maintainer's rejection or claim user approval.
6. When settled and requested, pass that artifact to `/1-to-spec`. A later `/1-design-review` receives
   the resulting design, while the author checks the brief-to-draft decisions separately.

The [workflow map](../../1-design-review/references/workflow-and-connections.md) explains the full
development loop. This optional pass does not start drafting, implementation, publication or review.
