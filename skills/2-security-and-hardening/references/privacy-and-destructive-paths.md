# Privacy and destructive-path boundaries

These are engineering constraints for an authorized change, not legal conclusions
or permission to perform deletion, credential rotation or infrastructure operations.

## Data lifecycle

Record necessary data categories, purpose, allowed readers/processors and applicable
retention/export/deletion requirements from approved project policy. Do not invent
one universal consent rule, expiry period or deletion obligation across jurisdictions.
For policy interpretation use /1-compliance-engineering; for an active exposure use
/1-incident-response with separate authority.

Minimize data and prevent accidental copies in telemetry, caches, indexes, exports
and model contexts. Identify relevant stores and backup/retention constraints;
a deletion design must account for restore behavior and legal holds where applicable.
Do not purge backups or send customer records to a new vendor merely to satisfy a
generic checklist. Verify lifecycle behavior using synthetic local records.

## Derived destructive targets

A path received from a process, payload or config is not authorization. Before a
requested delete/move/overwrite, resolve the exact target, approved root, ownership
and protected exclusions. Never let a root/home/workspace itself become a recursive
target, or fall back to a broader path when validation fails.

A marker writable by the target's author is self-attestation, not trustworthy
ownership proof. Expected ownership must come from trusted task/runtime state.
Path depth and lexical containment alone do not handle symlinks, aliases or races.
An earlier realpath check followed by a pathname operation still has a check/use gap.

Use a proven platform/project primitive with no-follow/beneath-root semantics or
an environment whose hierarchy cannot change during the operation. Do not invent a
cross-platform deletion helper during unrelated hardening. If the required safety
cannot be established, leave the target intact and request a decision.

For Git worktree cleanup, return to /1-finish-branch only when the caller requested
that lifecycle step. That owner decides branch/worktree/service provenance; this
reference does not tear down shared resources or infer cleanup from a passing test.
