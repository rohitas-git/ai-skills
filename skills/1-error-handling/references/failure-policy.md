# Failure policy

Use before adding catches, retries, or fallback values. Preserve an established project contract unless the requested change includes its migration.

## Classify by what the caller can do

| Failure | Caller contract | Recovery decision |
|---|---|---|
| Invalid input, conflict, ordinary absence | Existing tagged outcome or known exception with a stable code | Correct input or take a documented alternative |
| Temporary dependency failure | Explicit unavailable/timeout outcome or propagated error | Retry only after transient classification and replay-safety checks |
| Caller cancellation | Preserve cancellation semantics | Stop work; no automatic retry or error alert for routine cancellation |
| Broken invariant or programming bug | Fail the operation and retain diagnostic context | Fix the defect; do not substitute empty success |
| Uncertain write outcome | State uncertainty; record an operation identifier | Reconcile status or reuse supported idempotency semantics |

Exceptions and Result types are both valid conventions. Tagged results help callers enumerate ordinary negative outcomes; exceptions fit existing exception-based APIs and unexpected faults. Absence alone may use an optional value; an outage is not absence. Recoverability depends on context, not the exception class alone. These choices synthesize [the upstream patterns](./sources.md#requested-sources); they are not a demand to retrofit Result types everywhere.

## Propagation and ownership

- Validate external input before effects. Keep domain failures independent of HTTP status codes where practical; map them at the transport boundary.
- A catch must change the outcome meaningfully. Otherwise allow propagation. Wrap only when adding useful operation context, retaining the original cause.
- Assign one owner for reporting each failed operation. Lower layers may add context; they should not all log the same exception before rethrowing. Required security/audit events have their own purpose and remain intact.
- Return success only after the operation's promised work succeeds. A database rollback cannot undo an external payment or email; handle such partial completion explicitly using the project's existing reconciliation approach.

## Retry and timeout contract

First inspect SDK retries so application retries do not multiply them. Specify retryable conditions, total attempts including the first call, per-attempt timeout, total elapsed budget, backoff cap with jitter, and cancellation behavior. Retry at one selected layer. Honor applicable server retry delays within the remaining budget. Never assume every HTTP error is transient.

A timeout does not prove a remote write failed. Retry writes only with a verified idempotency/reconciliation contract; retain the same operation key for the same logical request. Do not retry unchanged validation/authentication failures or caller cancellation. Release attempt resources before the next call. A circuit breaker is optional and needs evidence of cascading failures plus tested recovery behavior; reuse a supported implementation if needed. See [AWS retry guidance](https://d1.awsstatic.com/builderslibrary/pdfs/timeouts-retries-and-backoff-with-jitter.pdf).

## Public output and diagnostics

Map known failures to an allowlisted code and actionable, non-sensitive message. Map unknown failures to a generic message plus an opaque support identifier. Never copy arbitrary `error.message`, stack, cause, provider response, SQL, path, or request payload into public output. Error shape and status must follow the documented API contract; do not signal a failed operation as ordinary success. See [OWASP error handling](https://cheatsheetseries.owasp.org/cheatsheets/Error_Handling_Cheat_Sheet.html) and the [requested skill-development guide](https://owasp.github.io/www-project-agentic-skills-top-10/skill-development-guide).

Use structured, bounded diagnostic fields: operation, approved code, correlation identifier, and safe context. Apply redaction to nested causes and stack/message text before a logging sink; internal logs are not permission to capture secrets. Exclude credentials, tokens, unnecessary personal data, and raw prompts or tool output. Sanitize untrusted event fields against log injection, restrict log access/retention, and verify logger failure behavior. Preserve required audit semantics without making ordinary telemetry outages masquerade as business success or erase the original fault. See [OWASP logging](https://cheatsheetseries.owasp.org/cheatsheets/Logging_Cheat_Sheet.html).

## Degradation and cleanup

Fallbacks must preserve correctness, authorization, and freshness requirements. An explicitly optional recommendation panel may degrade; a failed permission check must never grant access. Label partial or stale data when consumers need that distinction. Never turn persistence failure into a success notification.

Release files, streams, locks, timers, and subscriptions through the existing resource lifecycle. Roll back only work within the transaction's actual boundary. If operation and cleanup both fail, retain both with the operation's failure identifiable; do not mask it with a cleanup exception. Stop retrying after the request is cancelled or the budget is exhausted.

## Review evidence

Write a small failure matrix: **trigger → observable result → effects → recovery → diagnostic owner → check**. Use controllable stubs for deadlines and dependency errors. Include malformed data, a negative business outcome, and an unexpected exception where relevant. For writes, exercise ambiguous completion; for concurrency, exercise partial completion. Test the public response and log sink with a seeded secret. Report what the checks establish and what still depends on the real provider or runtime.
