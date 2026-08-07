# Optimize description triggers (agentskills.io harvest)

> **Source:** [agentskills.io/skill-creation/optimizing-descriptions](https://agentskills.io/skill-creation/optimizing-descriptions) · fetched 2026-08-05  
> **Load when:** improving trigger accuracy (misses or false fires); designing a trigger-eval set.  
> **House ops:** [full-guide.md](./full-guide.md) § Description Optimization (`run_loop`, eval review HTML).  
> **Craft:** `/1-writing-great-skills` § Writing the description (**leading word**, one trigger per **branch**).  
> **This catalog:** every description change → sync ADR 0009 [route surface](../../0-skill-manager/references/skill-route-surface.md) (`Use when` / `Not for` / `Hub` + `metadata.catalog`).

The **description** is the always-on **context pointer** for a model-invoked skill: name + description load at startup; body loads only after a match. Trigger quality *is* invocation **predictability**.

**Nuance:** agents often skip skills for one-step tool work they can do alone. Write eval prompts that *need* specialized procedure — otherwise you measure nothing.

## Description craft (before measuring)

| Lever | Do |
|-------|----|
| Framing | “Use when…” (agent decides to act) |
| Match surface | User intent and **leading words**, not internal mechanics |
| Coverage | Explicit contexts, including when the user never names the domain |
| Budget | Spec max **1024** chars; prune hard — description is permanent **context load** |
| House | **Not for** cousins + **Hub**; mirror in `metadata.catalog` |

## Steps — trigger eval

**Completion criterion (set ready):** ~20 realistic queries, ~half should-trigger / half should-not, frozen train/val split, labels you trust.

### 1. Author queries

```json
[
  {"query": "…realistic user message with path/columns/backstory…", "should_trigger": true},
  {"query": "…near-miss cousin task…", "should_trigger": false}
]
```

| Class | Goal |
|-------|------|
| **Should-trigger** | Scope coverage: phrasing mix, casual/typos, implicit domain, multi-step burial. Best cases: skill would help but the link is **not obvious**. |
| **Near-miss** (should-not) | Shared keywords, different job. Easy irrelevants (“fibonacci”) are **no-op** tests — they never fail. |

### 2. Measure **trigger rate**

Per query, run ≥3 times. Rate = fraction of runs that load the skill body.

| Label | Pass |
|-------|------|
| should_trigger | rate ≥ threshold (default **0.5**) |
| should_not | rate **below** threshold |

Automate when possible (`run_loop` in full-guide). Early-stop a run once the skill was or wasn’t consulted.

### 3. Split once, freeze

~**60% train** / **40% val**, balanced positives/negatives. **Only train failures** drive rewrites. Pick the winner by **validation** pass rate (may not be the last train-friendly draft).

### 4. Revise for generalization

| Train failure | Move |
|---------------|------|
| Missed should-trigger | Broaden *when* / intent (not keyword-stuff the failed query) |
| False trigger | Sharpen boundary / **Not for** cousins |
| Stuck | New sentence structure, not micro-edits |
| Plateau | Re-label or replace **queries** — the set may be broken |

Stay ≤1024 chars.

### 5. Apply

1. Write `description` (+ house catalog fields).  
2. Spot-check; optional **5–10 fresh** queries never used in optimization.  
3. Done when val pass rate is acceptable or iterations stop gaining (~5).

**Shape (illustrative):**

```yaml
# weak
description: Process CSV files.

# stronger — intent + when + pushy coverage
description: >
  Analyze CSV/TSV/Excel — stats, derived columns, charts, clean messy data.
  Use when the user has tabular data to explore, transform, or visualize,
  even without saying "CSV" or "analysis."
```

## Related

| Need | Where |
|------|--------|
| Ops + scripts | [full-guide.md](./full-guide.md) § Description Optimization |
| Output quality evals | [agentskills-io-evaluating-skills.md](./agentskills-io-evaluating-skills.md) |
| Spec + house name rules | [agentskills-io-specification.md](./agentskills-io-specification.md) |
