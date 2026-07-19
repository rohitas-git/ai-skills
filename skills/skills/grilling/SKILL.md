---
name: grilling
description: Grill the user relentlessly about a plan, decision, or idea. Use when the user wants to stress-test their thinking, or uses any 'grill' trigger phrases.
disable-model-invocation: true
---
## Boundary

| Need | Skill |
|------|--------|
| Interview / stress-test a plan (body) | **grilling** (this) |
| Same interview, no docs | `/grill-me` (thin wrapper → this) |
| Interview + ADRs/glossary as you go | `/grill-with-docs` (wrapper + `/domain-modeling`) |
| Raw / vague idea — expand options first | [references/divergent-lenses.md](./references/divergent-lenses.md) · full [vendor-idea-refine-full.md](./references/vendor-idea-refine-full.md) · [idea-frameworks.md](./references/idea-frameworks.md) · [idea-refinement-criteria.md](./references/idea-refinement-criteria.md) · [idea-examples.md](./references/idea-examples.md) |
| Underspecified intent (who/why/success) | [references/interview-intent.md](./references/interview-intent.md) (vendor interview-me harvest) then this skill |
| Steel-man before reject/agree | `/thinking-steel-manning` |
| Multi-session fog map | `/wayfinder` |
| Spec from already-decided thread | `/to-spec` |
| Which skill? | `/butler` |

**Fork F2:** Codebase present? → prefer `/grill-with-docs` if yes, `/grill-me` if no.

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

- The user wants a **huge multi-session fog map** → `/wayfinder`
- They only want a **spec written from an already-decided thread** → `/to-spec`
- They want **catalog routing** ("which skill?") → `/butler`
