# Eval pressure on skill output (agentskills.io harvest)

> **Source:** [agentskills.io/skill-creation/evaluating-skills](https://agentskills.io/skill-creation/evaluating-skills) · fetched 2026-08-05  
> **Load when:** designing cases, writing assertions, grading, or deciding what to change after a run.  
> **House ops (SSOT):** [full-guide.md](./full-guide.md) — candidate identity, proportional evidence, and authority boundaries.  
> **Cousins:** [optimizing-descriptions](./agentskills-io-optimizing-descriptions.md) (trigger, not output) · [using-scripts](./agentskills-io-using-scripts.md) (bundle repeated helpers).

**Eval pressure** = checkable cases plus honest comparison where useful. Baselines, fresh contexts, viewers, and human review are optional instruments, not automatic gates.

## Steps — one iteration

Each step ends when its criterion holds. Full automation choreography lives in full-guide; this file is the *method*.

### 1. Cases (hand-author)

When a persistent harness is justified, store `evals/evals.json`: `prompt` · `expected_output` · optional `files`. Start with the smallest representative set.

**Completion criterion:** prompts are realistic (paths, columns, casual speech); ≥1 edge; varied formality. Assertions empty until after first run.

### 2. Run with **baseline**

Compare **with_skill** to **without_skill** or an **old_skill** snapshot only when that baseline answers a real question. Otherwise run the selected candidate directly and label the missing comparison.

Workspace pattern (sibling to skill):

```text
skill-workspace/iteration-N/eval-<name>/{with_skill,without_skill}/{outputs,timing.json,grading.json}
skill-workspace/iteration-N/benchmark.json
```

Capture **timing** at completion (`total_tokens`, `duration_ms`) — often only in the notification.

**Completion criterion:** every selected case records its input, immutable skill revision, output, runtime, and available timing; paired outputs exist only for selected comparisons.

### 3. Assertions (after seeing outputs)

Objective and observable. Style/feel → human review, not forced pass/fail.

| Strong | Weak |
|--------|------|
| “Bar chart image present; exactly 3 months; axes labeled” | “Output is good” / exact brittle phrase |

**Completion criterion:** each case has assertions you can grade with evidence.

### 4. Grade

PASS/FAIL + **concrete evidence** (quote path, field, screenshot detail). Scripts for mechanical checks; LLM for checkable qualitative claims. Require substance — a “Summary” heading alone fails “includes a summary.”

While grading, **prune the assertions**: always-pass both configs (no-op), always-fail (broken), unverifiable → fix before next iteration.

Optional blind comparison requires an available, authorized fresh-context mechanism; it is not implied by this reference.

### 5. Aggregate + pattern-read

`benchmark.json`: pass_rate, time, tokens per config + **delta** (what the skill costs vs buys). Early: raw pass counts matter more than stddev.

| Pattern | Action |
|---------|--------|
| Pass with skill, fail without | Skill value — keep / reinforce the instruction or script that did it |
| High variance | Ambiguous skill → examples / sharper steps |
| Time outlier | Read **transcript** for thrash |
| Always pass both | Drop assertion |

### 6. Human review

Actionable notes per case (`feedback.json`). Empty = fine. Improve only where feedback is specific.

### 7. Revise skill (generalize)

| Signal | Move |
|--------|------|
| Failed assertion | Missing step, unclear instruction, unhandled case |
| Human feedback | Wrong approach or unhelpful structure |
| Transcript | Agent ignored or thrashed — reword or cut dead steps |

Rules of revision (house craft):

- **Generalize** — one eval is not the product  
- **Lean** — cut transcript-proven waste (**no-op** / **sediment**)  
- **Why over MUST** — purpose steers better than caps  
- **Bundle** repeated helpers → `scripts/`  

**Loop completion:** stop at the selected evidence bar—affected cases pass, uncertainty is reported, or additional runs no longer justify their cost.

## Related

| Need | Where |
|------|--------|
| Spawn, grade, viewer, schemas | [full-guide.md](./full-guide.md) |
| Trigger accuracy | [agentskills-io-optimizing-descriptions.md](./agentskills-io-optimizing-descriptions.md) |
| Agentic scripts | [agentskills-io-using-scripts.md](./agentskills-io-using-scripts.md) |
