# Interview-intent calibration

This is the only operative reference for `/0-grilling`. The main skill owns scope, authority, routing,
and return behavior.

## Ask only what changes the outcome

Before a question, state:

- the fixed candidate and current interpretation;
- the unresolved decision;
- which materially different outcome depends on the answer;
- what evidence is already known or missing.

If the answer cannot change the requested artifact, do not ask. If a repository fact can settle the
question, return the needed read to `/1-grill-with-docs`. If external research is required, request
separate authority rather than turning it into a preference question.

## Question shape

Ask one neutral question per turn. Give a recommendation only when evidence supports it, and state the
trade-off behind it. Do not use a guess to anchor the user, manufacture disagreement, diagnose motives,
or ask the user to justify a preference they are entitled to choose.

Record responses as one of:

- accepted decision;
- explicit delegation to the agent;
- deferred decision with owner/condition;
- rejected option;
- reversible assumption accepted for now;
- unresolved blocker.

Delegation is a valid decision. “Sounds good,” “go ahead,” or similar wording may be adequate approval
when its referent is clear from context; ask again only when scope or authority is genuinely ambiguous.

## Stop and return

Stop when the requested result is decision-ready, the remaining unknowns are immaterial, evidence is
unavailable, another workflow owns the next fact/action, or the user asks to stop. Do not require an
arbitrary confidence threshold or claim you can predict the user.

Return a compact record:

```text
candidate/version:
outcome and success evidence:
accepted/delegated decisions:
constraints and assumptions:
non-goals:
open issues and owners:
evidence/cutoff and provenance:
next route requested (if any):
```

The record is not permission to write a spec, create a prototype, change documentation, or implement.
