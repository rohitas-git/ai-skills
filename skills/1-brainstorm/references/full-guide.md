# Brainstorm design calibration

This is the only operative reference for `/1-brainstorm`. The main skill owns scope, provenance,
authority, and return behavior; this guide only helps calibrate alternative generation and comparison.

## Frame the decision

- State the user/outcome, decision, fixed candidate version, constraints, success evidence, and non-goals.
- Separate supplied or observed facts from assumptions and generated possibilities.
- If purpose, owner, or success is still materially unclear, return to `/0-grilling` rather than running
  a second requirements interview inside Brainstorm.

## Generate alternatives

Use two or three options when genuine alternatives exist. One strong option plus `status quo` is valid;
do not manufacture novelty to fill a quota. A useful set differs in mechanism or trade-off, not wording.

Possible lenses, used only when relevant:

- subtraction or simplification;
- reuse of an existing repository pattern;
- a different boundary, sequence, or ownership model;
- a reversible experiment versus a committed design;
- an alternate affected-user or operational perspective.

Named mental models belong to their `/0-thinking` leaves. Do not duplicate a full SCAMPER, JTBD,
pre-mortem, First Principles, or Via Negativa workflow here.

## Compare consistently

Use owner-supplied criteria and one evidence standard across options. Consider only relevant dimensions:

- user value and evidence;
- compatibility with current contracts and architecture;
- implementation and operational complexity;
- security, privacy, accessibility, and affected-party cost;
- reversibility, failure containment, and validation cost;
- dependencies, unknowns, and evidence freshness.

Do not invent adoption, revenue, cost, market, competitor, or expert claims. If evidence cannot rank the
options, name the smallest discriminating question instead of forcing a recommendation.

## Return artifact

Return a conversational memo unless another operation was explicitly requested:

```text
Decision: <one decision>
Evidence and constraints: <observed/supplied, with cutoff>
Options: <2–3 mechanisms and trade-offs, or explain why only one is viable>
Recommendation: <one, conditional, or open>
Assumptions to test: <decision-changing only>
Non-goals: <explicit exclusions>
Approval state: proposed | accepted | changes requested | unknown
```

Do not write, publish, review, commit, prototype, or implement the memo automatically.

## Non-operative provenance

The imported [visual companion](./visual-companion.md) and
[spec-review prompt](./spec-document-reviewer-prompt.md) are retained only to explain dormant vendor
assets. Their contents do not add live steps or authority to Brainstorm.
