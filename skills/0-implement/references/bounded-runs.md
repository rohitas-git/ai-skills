# Bounded unattended and multi-PR work

## One persistent task

Use the [project continuation lifecycle](./project-continuity.md): read the known task record before
broad discovery, preserve the accepted contract, and refresh it at meaningful safe boundaries.

Define done as a falsifiable predicate, with explicit scope, resource budget and stop/escalation
conditions. A duration alone is not success. Use existing event/status mechanisms when permitted;
do not install a loop, enable a schedule or spawn a watcher from an autonomy request alone.
Each iteration records a hypothesis, owned change, observation and disposition. Keep useful work
inside the accepted task; unexpected adjacent fixes are follow-ups unless separately authorized.

If no existing recipe fits a substantial task, write a short phase list in the existing task record.
Put the highest-consequence unknown first and record the observation that would settle it. Establish
the relevant baseline and check before changing behavior. Give each phase its own verification point
and record the next safe action when the result is inconclusive. Scale the record to the task's risk.

When progress stalls, revisit the premise or experiment rather than relaxing the predicate. Preserve
failed checks and return a genuine blocker or product decision. Stop promptly on an explicit user
pause/stop, reaching a safe owned boundary and retaining a continuation record. Do not infer a goal
status change or a right to commit merely from being asked to keep going.

## Independent PR queue

Use one responsible owner per independent item only when delegation is authorized. Plan requests
produce a plan and stop. Pin the queue and grant per operation: building, committing, pushing, opening,
replying, approving and merging are distinct. Operator-owned or excluded items remain outside the grant.

Independent PRs branch from their real base; dependent changes form a stack with explicit parent edges.
Record owner handles, output paths, current heads, pending dependencies, evidence, service ownership
and next action in a durable task record. A replacement first establishes that the prior writer stopped
and reconciles its partial work; never replace it while it can still mutate the same state.

Keep implementation evidence separate from verification and policy approval. Fresh verification is
valuable when available, but a matching model label is not independence and an AI countersign cannot
substitute for a required human/forge approval. Do not weaken a failed gate, raise a budget or add an
exception solely to make the queue pass. Route a needed policy change to its actual owner.

## Delivery boundary

Rebase/restack only for the requested base/conflict policy, with correct remote destination and a
verified expected SHA. A new head or changed base can invalidate evidence even if patch-id matches.
Use the Git shipping recipe to determine what must be rechecked. A no-merge queue ends with verified
current-head receipts and no further pushes after handoff unless authorized. A merge grant still
obeys repository rules requiring immediate explicit permission for protected/default branches.

Adapted from the individually reviewed pstack 0.15.43 sources, MIT, Lauren Tan.
[Source-by-source decisions and checks](../../../guidelines/catalog/pstack-methods-review-2026-11-18.md).
