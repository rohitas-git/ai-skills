# Divergent lenses before grill (harvested)

Source: archive vendor `idea-refine` — high-value only.  
**Winner for stress-test interview:** `/grilling`. Do not peer-promote `idea-refine`.

Use when the idea is still **raw** (vague direction, many options) — expand once, then grill to converge. Skip if the user already has a sharp plan ready for decision tree walk.

## Phase shape (optional pre-grill)

1. **Restate** as a crisp “How Might We …” problem statement.
2. **Ask 3–5 sharpening questions** (who, success, constraints, prior art, why now) — still one at a time if already in grill mode.
3. **Generate 5–8 variations** (quality over 20 shallow ideas) with lenses:

| Lens | Prompt |
|------|--------|
| Inversion | What if we did the opposite? |
| Constraint removal | Budget/time/tech unlimited? |
| Audience shift | Different primary user? |
| Combination | Merge with adjacent idea/product? |
| Simplification | 10× simpler version? |
| 10× scale | Massive scale shape? |
| Expert | What would domain experts find obvious? |

In a codebase: ground variations in real architecture (`Glob`/`Grep`/`Read`); cite patterns.

Optional frameworks (pick one, don't run all): SCAMPER, first principles, JTBD, deliberate constraints, pre-mortem — see archive vendor `idea-refine/frameworks.md` if needed.

## Converge (before long grill)

Cluster resonating ideas into **2–3 distinct directions**. Stress-test each on:

1. **User value** — painkiller vs vitamin; name real users and current workaround  
2. **Feasibility** — hardest part, MVP time-to-value  
3. **Differentiation** — different, not just “better”

**Surface hidden assumptions** with how to validate. Be honest, not a yes-machine.

## Sharpen artifact (optional)

If useful before `/to-spec` or continued grill, a short one-pager:

- Problem statement (HMW)
- Recommended direction + why
- Key assumptions to validate (with tests)
- MVP scope
- **Not Doing (and why)** — often the highest-value section
- Open questions

Save only if the user wants a file (`docs/ideas/…` or their path). Default stays conversational → grill → `/to-spec`.

## Boundary

| Need | Skill |
|------|--------|
| Expand vague idea | this ref under `/grilling` |
| Decision-tree interview | `/grilling` body |
| ADRs / glossary while deciding | `/grill-with-docs` |
| Multi-session fog | `/wayfinder` |
| Spec from decided thread | `/to-spec` |
