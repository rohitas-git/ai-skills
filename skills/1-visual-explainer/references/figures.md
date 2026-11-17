# Figure patterns

Load when planning the page. Choose figures by the claim, not by an available widget.

| Claim | Useful figure |
|---|---|
| How a request or data moves | Labeled flow or sequence with actors and boundaries |
| What changes between two cases | Same-coordinate before/after panels or an accessible toggle |
| Which responsibilities belong together | Module/ownership map with actual relationships |
| How a state changes | State/event drawing with guards and failure paths |
| How scenarios differ | Small multiples with the same coordinates and scale |
| When something happened | Source-backed timeline grouped by theme |
| Many criteria differ | Semantic comparison table with short evidence and labeled status |
| Counts, rank, or magnitude | Labeled bars; zero baseline unless a different scale is explicitly justified |
| Trend, distribution, relationship | Line, histogram, or scatter with actual data and units |
| Where time or size is spent | Dimension lines beside the measured span |

## Drawing layout

Prefer inline SVG or HTML/CSS. Sketch the reading order first, then position nodes on a grid.
Use consistent geometry and enough space for labels. Route edges without crossing labels.
SVG text needs explicit line breaks with `<tspan>`; it does not wrap like HTML.
For sequence diagrams, one column per actor and time downward is a useful default.
Use dashed boundaries for an explicitly defined scope or trust zone, not as decoration.

Keep an overview separate from detailed paths when the drawing becomes dense.
Put annotations at the feature they explain. Label every important arrow.
Use shapes consistently, and include a legend when a convention is not obvious.
Hand-drawn styling is optional; exact relationships and readable text are required.

## Honest comparison and charts

Use shared axes, units, layout, initial conditions, and time windows across options.
Do not imply that pixel distance is measured latency unless it is scaled from actual data.
Do not infer risk, performance, adoption, or activity from file counts alone.
Distinguish unavailable values from zero. Identify denominators and sources for percentages.
Do not draw a plausible line through missing measurements without labeling interpolation.

## Source-backed state diagrams

Read the named reducer/configuration or supplied transition table without executing it.
Map state → event → guard → action → next state, citing relevant code or source rows.
Include self-loops, terminal/failure states, and omitted conditions when they matter.
Do not call a hand-copied model exhaustive, formally verified, or equivalent to production code.
If simulation is useful, label assumptions and exclusions. Actual model execution is a separate
authorized engineering task, not part of rendering this explanation.

## Teaching comparison and project context

For a comparison: draw the actual difference, show meaningful scenarios, explain trade-offs,
and recommend only when the supplied criteria support it. An unselected default is not a decision.
For a project context page: identify purpose, bounded architecture, relevant recent activity,
current state, and useful entry points. Cite the chosen revision/window. Keep dirty local changes,
open branches, verified blockers, and published state distinct. Never invent momentum or urgency.
