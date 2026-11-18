# Replay, partial progress and boundaries

List the operation's observable success, expected rejection, cancellation and ambiguous outcome.
At an external boundary, parse enough to establish the accepted domain value and translate errors
into the caller's documented convention. Keep internal causes for diagnosis without exposing secrets.
Do not revalidate an unchanged trusted value merely to repeat a guard, but identify when mutation,
authorization, another process or persisted data invalidates that trust.

An idempotent operation converges on the intended state across duplicate calls and interrupted runs.
Inspect the state that exists now, compare it with the goal and apply the required difference. A retry
after an ambiguous write needs an idempotency/reconciliation strategy, not an assumption that the write
failed. Specify ownership and crash evidence for locks, claimed jobs, temporary files and partial rows.

For file publication, write an owned temporary artifact and publish with the appropriate atomic or
exclusive operation; a rename alone does not establish database/network atomicity or durable storage.
For shared writes, first ask whether each actor can publish its own fact. Use a real lock, transaction,
compare-and-swap or single writer when shared mutation is a true invariant; prose is not a lock.

Select representative crash points: before the effect, after the effect before acknowledgement, and
after partial progress. Invoke again and inspect the user-visible result and side effects. Also invoke
again after clean completion and check that no business effect repeats, including downstream writes
or notifications. A per-attempt metric or diagnostic record may still be expected. Use authorized
disposable state for both controls. Do not inject faults into
production or replay real payments/messages merely to follow this procedure.

Adapted from the individually reviewed pstack 0.15.43 sources, MIT, Lauren Tan.
[Source-by-source decisions and checks](../../../guidelines/catalog/pstack-methods-review-2026-11-18.md).
