# Confusion and lightweight execution notes

Do not silently choose between contradictory authoritative inputs.

## Material conflict

State the smallest useful conflict packet:

```text
Conflict: requested/spec behavior X; current contract/code/policy Y.
Evidence: exact sources and candidate.
Impact: what changes under each interpretation.
Decision needed: the load-bearing user/product choice.
```

Ask only when the choice changes product behavior, compatibility, external effects, destructive scope,
or another material outcome. For small reversible implementation details, follow repository precedent
or the safest narrow assumption, state it, and continue.

## Planning while implementing

Use a short execution note when sequencing, shared state, or verification dependencies would otherwise
be unclear. Do not emit a ceremonial plan for a one-step change, rewrite an adequate existing plan, or
pause after announcing a plan unless a real user decision is required.

When evidence invalidates the plan, update the affected next step and preserve completed evidence;
do not restart the whole workflow or hide the changed assumption.
