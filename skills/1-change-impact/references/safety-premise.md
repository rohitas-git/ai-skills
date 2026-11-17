# Check the safety premise

Load when a change looks safe only because a specific condition is believed to hold. Name that
condition explicitly and trace how each important downstream risk depends on it.

Look beyond symbol callers: serialization, database columns, event order, microtasks/teardown,
feature flags, dependency versions/local patches, generated artifacts and other-language consumers.
Distinguish evidence levels: assumption, source location, feasible-path analysis, actual check result,
and runtime reproduction. They answer different questions and are not interchangeable guarantees.

For each material premise, record claim → supporting/contradictory evidence → affected consumer →
smallest falsifying check → current confidence. A search with no hits leaves dynamic/external
consumers uncertain. Do not invent probabilities or downgrade a plausible untested risk to “cleared.”

This owner remains read-only. Recommend a discriminating test or runtime probe, but do not run code,
write a test, spawn competing reviewers, or repair the product as part of impact analysis. Supplied
execution evidence must identify the same candidate. “Unproven” is a valid conclusion.

Modified from pstack blast-radius guidance, MIT.
[Source and review](../../../guidelines/catalog/ingest-pstack-2026-11-15.md).
