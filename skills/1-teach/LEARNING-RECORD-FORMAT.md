# Learning-record schema

Learning records are append-only, decision-grade evidence under `learning-records/`.
Create the directory only for the first qualifying record. A record describes one event
that changes a future teaching decision; it is not an activity log or a mastery score.

```md
---
record_id: LR-{stable identifier}
evidence_kind: demonstrated | self-reported | corrected | tutor-supplied
status: active
observed_at: {date or bounded session reference when known}
---

# {Short evidence claim}

## Observation
{What was actually observed or explicitly reported. Do not merge inference into fact.}

## Teaching implication
{The one future teaching decision this evidence changes.}

## Provenance
{Exercise, learner statement, artifact, or other exact source.}

## Supersedes
{Earlier record IDs contradicted by this new evidence, or `None`.}
```

Evidence rules:

- **Demonstrated** means the learner performed or explained something without the answer
  being supplied in the same attempt.
- **Self-reported** records an explicit claim, not demonstrated competence.
- **Tutor-supplied** records exposure or assisted completion and must not be treated as
  independent mastery.
- **Corrected** identifies a misconception and the evidence that changed it.
- Mere coverage, praise, a copied answer, and an unobserved assumption do not justify a
  demonstrated-learning record.

Numbering and history:

- Follow the workspace's established identifiers. Otherwise choose the next unused
  identifier after scanning existing records, then re-scan immediately before writing.
- Append one new file. Never overwrite, renumber, edit, or delete an earlier record.
- Express supersession from the new record. The prior record remains historical evidence.
- Omit sensitive personal detail that is unnecessary for the teaching decision.
