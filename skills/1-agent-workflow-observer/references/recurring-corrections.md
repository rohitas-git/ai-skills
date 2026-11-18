# Repeated corrections and enforceable lessons

Load when the fixed completed/paused snapshot contains repeated user corrections or established
mistake classes. Use supplied evidence; do not mine unrelated chat history or private repositories.
A single run may suggest a candidate without establishing recurrence across runs.

For each class, propose the highest fitting prevention mechanism, not a mandatory rewrite:

1. Architecture/data ownership or one authoritative representation that removes the bad path.
2. Types or boundary validation that reject the invalid state.
3. A targeted lint/CI rule with an actionable message and scoped adoption.
4. A behavioral check that detects the actual failure.
5. Documentation for context and judgment that cannot be mechanically enforced.

Record correction/evidence → failure mechanism → existing rule → proposed enforcement → owner →
negative control and clean control → exceptions/rollout cost. Prefer preventing new occurrences
over expanding into a broad cleanup; legitimate exceptions require their actual policy owner.

Name the existing authoring path that should use the proposed guard. If its canonical examples would
still teach the failing pattern, include the smallest correction to those examples in the proposal.

A mechanism can enforce a syntactic rule without guaranteeing the product outcome. Existing
documentation still preserves rationale even when a check exists; do not delete it automatically.
Do not claim a mistake is impossible from one passing example or one regex rule.

Return proposals only. Implementation, CI changes, skill edits, exception approval, deletion,
commits and live automation remain separately scoped actions with their existing owners.

Modified from pstack correct and encode-lessons-in-structure guidance, MIT.
[Source and review](../../../guidelines/catalog/ingest-pstack-2026-11-15.md).
