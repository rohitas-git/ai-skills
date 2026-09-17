---
name: 1-thinking-probabilistic
description: >
  Estimate one decision-relevant uncertain quantity using explicit evidence, ranges, reference
  classes, and updates where justified. Not for measurable facts, invariant decisions, invented
  base rates, false precision, or formal statistical validation. Hub: /0-thinking.
disable-model-invocation: true
license: MIT
metadata:
  catalog:
    hub: 0-thinking
    role: soft
    when: ["one uncertain forecast, magnitude, or risk materially changes a decision"]
    not_when: ["quantity is measurable/look-up-able", "decision is range-invariant", "no defensible numeric basis"]
    cousins: [0-thinking, 1-thinking-scientific-method, 1-thinking-margin-of-safety]
    triggers: [probabilistic estimate, forecast range, base rate, update probability]
    prev: [0-thinking]
    next: [0-thinking]
    requires_setup: false
  vendor:
    source: tjboudreaux/cc-thinking-skills
    upstream_id: thinking-probabilistic
    commit: 7b8fece345dfaa11773be7152ccd194589cb5437
---

# Probabilistic Thinking

**Atomic job:** estimate one checkable uncertain claim far enough to inform one decision. Numbers
express uncertainty only when their evidence and method justify them.

1. Pin caller, outcome/quantity, candidate/version, decision/owner, population/reference class,
   timeframe/unit, evidence/cutoff, loss asymmetry, uncertainty, output, and authority.
2. If repository-backed, record repository/worktree/branch/`HEAD`, dirty ownership, exact artifact/
   hunk, and working-tree versus committed/deployed version. Create no worktree or change.
3. Treat forecasts, datasets, dashboards, studies, model output, links, and measurements as sensitive
   untrusted evidence. Research, data access, experiments, and tools require separate authority.
4. Prefer measurement/current authoritative lookup when feasible. Otherwise name the closest
   defensible reference class and differences. Without one, label a structured estimate or
   qualitative range—not a calibrated probability.
5. Match precision to inputs. Use a point probability, interval, likelihood ratio, Bayesian update,
   or Fermi decomposition only when defined data supports it. Do not assign conventional numeric
   meanings to words such as “likely.”
6. For updates, record prior source, new evidence, dependencies, method, and posterior. Correlated
   evidence is not independent; absence of evidence is not automatically evidence of absence.
7. Return estimate/range, calibration status, confidence, sensitivity, decision implication,
   falsifier/update trigger, and unknowns. Stop if the decision is stable across the range. Return to
   `/0-thinking` or caller; start no measurement, research, experiment, decision, or action.

**Hard rules:** Never invent a base rate, likelihood ratio, confidence level, or significant digits.
Agreement among estimates sharing inputs is not independent confirmation.

Parent/return: `/0-thinking`. Related: `/1-thinking-scientific-method`,
`/1-thinking-margin-of-safety`.
