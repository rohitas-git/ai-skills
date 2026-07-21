---
name: 0-grilling
description: >
  Grill the user relentlessly about a plan, decision, or idea. Use when stress-testing
  thinking or any grill trigger. Not for: synthesizing an already-decided thread into a spec (1-to-spec),
  multi-session fog maps (0-wayfinder). Hub: /0-grilling. Triggers: grill me, stress-test, interview my plan.
disable-model-invocation: true
metadata:
  catalog:
    hub: 0-grilling
    role: hub
    when:
      - "stress-test a plan or idea"
      - "grill / interview intent"
    not_when:
      - "write spec from settled thread → 1-to-spec"
      - "fog map multi-session → 0-wayfinder"
    next: [1-to-spec, 0-implement]
    cousins: [1-grill-me, 1-grill-with-docs, 1-thinking-steel-manning]
    triggers:
      - "grill me"
      - "stress-test"
      - "interview my plan"
    requires_setup: false
---
## Process

1. Follow this skill's procedure.

## Boundary

| Need | Skill |
|------|--------|
| Interview / stress-test a plan (body) | **grilling** (this) |
| Same interview, no docs | `/1-grill-me` (thin wrapper → this) |
| Interview + ADRs/glossary as you go | `/1-grill-with-docs` (wrapper + `/1-domain-modeling`) |
| Raw / vague idea — expand options first | [references/divergent-lenses.md](./references/divergent-lenses.md) · full [vendor-idea-refine-full.md](./references/vendor-idea-refine-full.md) · [idea-frameworks.md](./references/idea-frameworks.md) · [idea-refinement-criteria.md](./references/idea-refinement-criteria.md) · [idea-examples.md](./references/idea-examples.md) |
| Underspecified intent (who/why/success) | [references/interview-intent.md](./references/interview-intent.md) (vendor interview-me harvest) then this skill |
| Steel-man before reject/agree | `/1-thinking-steel-manning` |
| Multi-session fog map | `/0-wayfinder` |
| Spec from already-decided thread | `/1-to-spec` |
| Which skill? | `/0-butler` |

**Fork F2:** Codebase present? → prefer `/1-grill-with-docs` if yes, `/1-grill-me` if no.

## Progressive disclosure

| Load when | File |
|-----------|------|
| Hypothesis + Q/GUESS intent interview | [references/interview-intent.md](./references/interview-intent.md) |
| Divergent expand before grill | [references/divergent-lenses.md](./references/divergent-lenses.md) |
| Ideation frameworks (SCAMPER, HMW, …) | [references/idea-frameworks.md](./references/idea-frameworks.md) |
| Value / feasibility / differentiation rubric | [references/idea-refinement-criteria.md](./references/idea-refinement-criteria.md) |
| Worked ideation sessions | [references/idea-examples.md](./references/idea-examples.md) |
| Full idea-refine body | [references/vendor-idea-refine-full.md](./references/vendor-idea-refine-full.md) |

Interview me relentlessly about every aspect of this until we reach a shared understanding. Walk down each branch of the decision tree, resolving dependencies between decisions one-by-one. For each question, provide your recommended answer.

Ask the questions one at a time, waiting for feedback on each question before continuing. Asking multiple questions at once is bewildering.

If a *fact* can be found by exploring the environment (filesystem, tools, etc.), look it up rather than asking me. The *decisions*, though, are mine — put each one to me and wait for my answer.

Do not act on it until I confirm we have reached a shared understanding.

## Don't use when

- The user wants a **huge multi-session fog map** → `/0-wayfinder`
- They only want a **spec written from an already-decided thread** → `/1-to-spec`
- They want **catalog routing** ("which skill?") → `/0-butler`
