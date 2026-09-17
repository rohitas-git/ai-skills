# Performance experiment checklist

Apply to one measured claim. Mark non-applicable items; this is not a mandate to optimize every
layer or meet generic web budgets.

## Candidate and protocol

- [ ] Caller, plan/read-only/edit mode, scope, exclusions, and allowed effects are explicit.
- [ ] Repository/worktree/branch/HEAD or immutable artifact/query/schema identity is pinned.
- [ ] Metric/unit, target or comparison, workload/fixture, correctness guards, and stop condition are named.
- [ ] Tool/version/config, machine/runtime/browser/network/database, cache state, concurrency, and
      competing load are recorded where they can affect results.
- [ ] Profiles/reports are stored in task-owned ignored/temp paths unless policy requires otherwise.

## Baseline and diagnosis

- [ ] The measurement is repeatable and red-capable for the claimed bottleneck.
- [ ] Raw samples and variability exist; warmup, cold/warm state, outliers, and aggregation are disclosed.
- [ ] Synthetic, field, staging, and production evidence are not substituted for each other.
- [ ] A trace/profile/plan/counter localizes the cost before a remedy is selected.
- [ ] Correlation, a single average, or one screenshot is not treated as causal proof.

## Experiment

- [ ] Hypothesis predicts a measurable change and names guard metrics.
- [ ] One causal variable changes, or coupled attribution limits are explicit.
- [ ] Product behavior, security, accessibility, durability, and compatibility remain invariant.
- [ ] Cache, query/index, concurrency/resource, or frontend trade-offs are evaluated when applicable.
- [ ] New dependency, schema/index, infrastructure, hosted setting, or CI gate uses its owner workflow.

## Comparison and disposition

- [ ] Before and after use comparable candidate, workload, protocol, environment, and state.
- [ ] Drift/confounders are controlled or disclosed; protocol corrections re-baseline both candidates.
- [ ] Effect is compared with noise and practical significance, not merely a favorable mean.
- [ ] Correctness and resource/error guard results accompany the primary metric.
- [ ] Disposition is explicit: keep, revise, recommend removal, or inconclusive.
- [ ] User-owned work is not silently reverted and complexity is not kept solely because it was written.

## Guard and return

- [ ] A regression guard is added/proposed only if stable, useful, and supported by repository policy.
- [ ] No tool install, unowned shared-service start, remote/shared load, schema mutation, deploy, or
      production change occurred without separate authority.
- [ ] Return includes candidate/worktree, protocol, raw/summary data, variability, confounders,
      correctness evidence, disposition, artifacts, residual risk, and BLOCKED/SKIPPED validation.
