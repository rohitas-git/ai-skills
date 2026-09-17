# ADR boundary examples

ADR creation belongs to `/1-domain-modeling`; this skill only recognizes when changed living docs may
need a recorded decision linked.

## Likely ADR

A durable authentication trust-boundary change, datastore migration strategy, or cross-service
consistency choice may warrant an ADR when real alternatives existed and future maintainers need the
rationale/consequences to avoid accidentally reversing it.

## Usually not an ADR

A routine endpoint addition, typo fix, dependency patch, or already-settled implementation detail
normally belongs in current guides/contracts or nowhere. Reversibility is a signal, not a universal
three-condition gate.

## Existing history

Match the repository's status, numbering, filename, and supersession conventions. Never renumber,
delete, or rewrite an accepted decision merely to fit a template. If the current decision changed,
the owning workflow decides whether to supersede, amend, or record it elsewhere.

## Evidence returned to the ADR owner

Provide the changed decision, constraints, alternatives actually considered, consequences, current
docs affected, repository convention, and unknowns. Do not invent rejected alternatives or infer
acceptance from implementation alone.
