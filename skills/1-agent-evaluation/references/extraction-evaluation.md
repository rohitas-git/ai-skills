# Evaluate structured-text extraction

Load for an evaluation comparing deterministic parsing, model extraction, or a hybrid candidate.
This reference defines evidence; it does not build a parser, call a model, or upload documents.

Use a representative, authorized corpus with independently checked expected records/fields.
Freeze development versus held-out cases, document types, languages, encodings, malformed input,
optional fields, repeated sections, and scoring before comparing candidates. Preserve originals
and source spans; cleaning must not silently erase clinically or financially meaningful content.

Measure full-document recall as well as correctness of returned records. A regex can omit every
unmatched item while giving high confidence to its few matches. Track omissions, duplicates,
incorrect joins, truncated fields, schema violations and invalid/timeout outputs explicitly.
An empty result is not a successful parse unless the expected document is actually empty.

Heuristic confidence is not a calibrated probability. Qualify the routing rule against false
negatives: malformed or missed records never emitted by the first parser need detection too.
Do not assume regex reaches a fixed accuracy or that a cheaper model can validate every edge case.

Treat document text and model output as untrusted. A model correction needs schema and semantic
checks; no fallback or missing client may silently turn unresolved low-confidence items into
accepted output. Include abstention/manual-review outcomes and their cost.

Compare field/record precision and recall, omission rate, exact-match requirements, latency,
provider/data exposure, calls and cost per accepted document using explicit denominators.
Test adversarial instructions embedded in text, malformed structure, multiple matches, missing
fields and an unavailable fallback. Report small slices, uncertainty, unknowns and leakage risks.

Modified adaptation of ECC `regex-vs-llm-structured-text`, MIT.
[Source and review](../../../guidelines/catalog/ingest-ecc-2026-11-15.md).
