---
name: 1-ponytail-gain
description: >
  Display one pinned upstream Ponytail benchmark snapshot with methodology and limitations. Not for
  measuring this repository, predicting savings, or activating Ponytail. Hub: /0-ponytail.
disable-model-invocation: true
metadata:
  catalog:
    hub: 0-ponytail
    role: satellite
    when: ["show the pinned Ponytail benchmark result and its limitations"]
    not_when:
      - "measure or predict savings for this repository"
      - "audit code → 1-ponytail-audit or 2-ponytail-review"
    prev: [0-ponytail]
    next: [0-ponytail]
    cousins: [2-ponytail-review, 1-ponytail-audit]
    triggers: [ponytail gain, Ponytail benchmark, what does Ponytail save, show Ponytail impact]
    requires_setup: false
---

# Ponytail Gain

Display this one-shot, read-only snapshot. Do not change mode, inspect a repository, fetch new data,
write files, or persist state.

## Pinned benchmark card

Upstream agentic benchmark dated **2026-06-18**: Haiku 4.5, one pinned FastAPI + React repository,
12 feature tasks, four runs per task/arm, same headless coding agent with and without the skill. Metrics
were taken from the resulting diffs and agent runs.

```text
Ponytail vs no-skill baseline — agentic feature tasks

added LOC   -54% mean   (about 0% on irreducible work; up to -94% on an over-build trap)
tokens      -22%
cost        -20%
time        -27%

safety slice: 20/20 known adversarial checks passed
```

## Honesty boundary

- This is one upstream experiment, one model, one repository, one date, `n=4`; it is not a universal
  effect size, security proof, current-repository measurement, or prediction.
- The 20/20 result is a small deterministic safety floor, not `100% secure`.
- The older `80–94% less code`, `47–77% lower cost`, and `3–6× faster` card used a single-shot,
  chatty-baseline design. Upstream now labels that LOC range partly inflated; do not present it as the
  primary agentic result.
- Never claim this repository saved a number without a controlled counterfactual. Marker counts from
  `/1-ponytail-debt` and findings from `/1-ponytail-audit` answer different questions.

Report the snapshot date, setup, figures, and limitations together. If current figures are requested,
use a separately authorized source-verification task and label any newer source; do not silently replace
this pinned card.

## Provenance

See [pinned upstream sources](./references/vendor-source.md).
