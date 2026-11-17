# Reviewer rubrics

Modified adaptation of Google EGM personas and document standards, Apache-2.0.
Use with [the protocol](./review-protocol.md); [source and license](./source-review.md).

Give each fresh reviewer its lens, pinned artifact/scope, allowed evidence, and read-only contract.
Require precise evidence and severity, not a quota of findings. Missing evidence stays unknown.

## Skeptical architect: zoom out

Can the reader identify what problem is being solved and why? Does the design address the root
problem in the right layer? Check project alignment, YAGNI, unnecessary data hops, speculative
abstractions and premature optimization. Search allowed source for equivalent utilities and stable
platform features before claiming reuse. Prefer simple boundaries that permit change without
building hypothetical features. Feature sections describe components, contracts and data flow;
implementation minutiae belong in the plan. Re-check mitigations for new coupling and complexity.

## Naive reader: comprehension

Read only the target document. Start with **What this proposes** and **How the existing system
works, per this document**, two to five sentences each. Inability to paraphrase a material section
is a Blocker. A wrong paraphrase exposes missing connections even when terms are defined.
Check project-specific terms, prerequisites, workflow order, unstated state and side effects.
Search the rest of the target before calling a definition missing. General software terms do not
need a glossary. A link can establish that a definition exists, but its content is not available
in this comprehension test. Never apply a code-reconstruction standard to high-level design prose.

## Design critic: feature standard

Check the problem, intended users, goals/non-goals, architecture/data flow, external contracts,
failure behavior, security/privacy, load assumptions, costs/quotas, integration and operability
where applicable. Require evidence for feasibility claims; don't invent traffic or performance.
Evaluate viable alternatives and technical rejection reasons, including author decisions recorded
in the brief. Do not invent alternatives just to satisfy a template, or attribute a rejection to
a maintainer without evidence. Identify missing decisions and unmitigated risks concretely.

## Structure and style

Structure: use the selected project standard; check required sections, heading nesting, coherent
scope split, working links, valid tables and closed code fences. A differently named heading is
not a defect when it serves the same contract. Style: prefer precise, plain, factual prose; strip
flattery, hyperbole, redundancy and unexplained project jargon without losing technical substance.
Calibrate claims of existing/tested behavior to evidence. For a caveat ask what reader decision it
changes: drop irrelevant caveats, narrow unsupported claims, or move guidance to the affected step.

## Implementation readiness and codebase details

Could a new implementer execute the plan without choosing architecture, schemas, APIs, dependencies,
or failure policy? Mechanical coding choices may remain. Check exact Create/Modify/Delete paths and
rationales, bounded write scope, signatures/data/state changes, dependency order, stable buildable
phases, happy/edge/failure acceptance checks, and applicable migration/rollout/rollback.
Verify claimed **existing** files and symbols against permitted source. A clearly proposed new file
is not a missing-reference defect. If Create/Modify/Delete is unclear, report the ambiguity once.
Check existing reuse, observable defaults, errors/retries, configuration, side effects and shared
test helpers as relevant to the changed contract; avoid demanding every private helper be documented.
Inspect tests when relevant; reading a test is not running it. Missing source access limits codebase
claims, and a spec without a plan cannot pass implementation readiness.

## Optional standards for a custom pass

**Heilmeier proposal:** what is being attempted in plain language; current practice and its limits;
what changes and why it could succeed; who benefits; risks/payoffs; cost; timeline; intermediate and
final success checks. Apply only to a proposal that needs those answers.

**Re-implementation contract:** can a reader reproduce the scoped observable behavior without
guessing APIs, formats, state transitions, defaults, errors, side effects, configuration or limits?
Document significant contracts, not syntax/private layout. Use for documentation of an existing
component, not to force code-level detail into the feature design or comprehension stage.
