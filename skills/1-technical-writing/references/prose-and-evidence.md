# Prose and evidence checklist

## Shape the document

For a tutorial, name the thing the learner builds and show the observation after each meaningful step.
For a how-to, start from the reader's actual problem, assume its stated prerequisites and allow real
branches. For reference, give complete accurate facts in the order of the interface. For explanation,
show context, design constraints, mechanisms, alternatives and their evidence.

These are organizing tools, not certification rules. Preserve an established README/RFC template and
its audience. Link a long explanation from a procedure when it interrupts execution; do not force a
small document into several files. Apply repository Markdown and code-indentation conventions.

## Make a sentence carry its meaning

Use the real identifier and one stable term per concept. Put `only`, `not`, conditions and quantities
next to what they qualify. Replace a vague pronoun with its actor or object. Keep articles and verbs
needed to disambiguate. Use active voice when the actor matters, and passive voice when it does not.
Break a sentence carrying several decisions; retain a longer sentence that accurately conveys one.

## Edit generic prose without erasing facts

Cut empty introductions, praise, stock conclusions, rhetorical contrasts and decorative formatting.
Replace abstract benefits with the actual mechanism or result. Name an attribution's source or label
it unsupported. Avoid invented jargon, forced groups of three and synonym churn. Keep a needed
technical term and explain it instead of replacing it with an inaccurate everyday word.

Preserve `may`, `unknown`, confidence and scope where the evidence requires them. A rule to keep one
hedge cannot turn uncertainty into a fact. Preserve the requested voice, code punctuation, accessibility
text, legal notices and literal identifiers. Do not impose a universal blacklist on ordinary words.

## Check technical truth separately from style

Compare old and new meanings clause by clause. A command that has not run remains unrun. A model
pass remains bounded model evidence. A proposal remains a proposal. A source saying a feature may
fail does not justify writing that it always fails, that it is fixed or that no failure is possible.

For PR prose, let `/1-pr-summarizer` own candidate/evidence collection and the repository template.
Lead with the concrete problem and resulting behavior; include only decision-relevant trade-offs and
actual validation. Link long logs instead of copying them into a briefing. Drafting prose never posts it.

For product UI strings and marketing, use the product's copy/brand owner. For a plain chat restatement,
use `/1-bro`. No prose-cleanup request authorizes arbitrary source edits or data disclosure.

Adapted from pstack `technical-writing` and `unslop`, MIT. [Review](../../../guidelines/catalog/pstack-methods-review-2026-11-18.md).
