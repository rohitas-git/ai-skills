# Logging and audit

## Logging writes

Use the wiki's existing history mechanism. If it has an append-only `log.md`, add one consolidated
entry for the operation and preserve earlier entries. If it uses a sentinel, validate exactly one
sentinel remains in the expected position. Do not introduce a second logging convention during an
ordinary update.

Create a new log only when wiki initialization is in scope. A log helps explain curated wiki changes;
it does not replace Git history, cited sources, or the current diff.

## Read-only audit

Pin the exact wiki/source roots and check applicable items:

- unresolved internal links and ambiguous aliases;
- pages missing from the established index/navigation;
- missing, nonexistent, or imprecise cited sources;
- claims newer than or inconsistent with their evidence;
- unmarked conflicts, proposals, historical states, or unknowns;
- duplicate/overlapping concepts and accidental forks;
- format violations relative to local page conventions;
- log/index drift and broken sentinel/append behavior;
- unexpected files outside the authorized wiki surface.

Report location, evidence, impact, confidence, and smallest repair. Do not automatically fix an audit.
Absence of a broken link is not proof that every factual claim is correct; report coverage and skipped
checks.

## Verification after an authorized repair

Run existing wiki/link checks when available, then inspect the scoped Git diff. If no checker exists,
perform a bounded link/source/index/log validation and label it manual. Never install a linter,
rewrite the entire wiki, or normalize unrelated pages merely to complete an audit.
