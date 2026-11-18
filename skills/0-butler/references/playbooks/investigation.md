# Investigate and improve

Use the selected section within the [playbook handoff and tool contract](../playbooks.md#handoff-and-tool-selection).

## investigation

1. Use [Code Explainer](../../../1-code-explainer/SKILL.md) to trace entry points, state and effects. Apply [Model the Domain](../../../1-codebase-design/references/data-shapes-and-ownership.md) to identify what owns data and decisions.
2. Use [Design Rationale](../../../1-design-rationale/SKILL.md) if the reason behind an existing choice matters and relevant evidence is available. Cite source and observed outputs, and label inferred behavior.
3. Return the mechanism, evidence and unknowns. A request to explain a concrete failure uses [Runtime Forensics](#runtime-forensics) or [Trace Forensics](#trace-forensics) as appropriate.

## bug-fix

1. Establish a failing observation on the actual affected surface. Use a permitted project harness or [runtime feature verification](../../../0-implement/references/verification-workflows.md#w-ps1--runtime-feature-verification) where a mapped user action reproduces it.
2. Apply [Attack the Premise and Fix Root Causes](../../../0-diagnosing-bugs/references/premises-and-forensics.md) to discriminate plausible causes. Carry the observed mechanism and smallest authorized fix into [Implement](../../../0-implement/SKILL.md).
3. If a stable independent oracle exists, use [TDD](../../../1-tdd/SKILL.md) for the regression. Run the same failing check after the fix and verify affected neighboring behavior. Return baseline, result and coverage gaps.

## runtime-forensics

1. Pin the served build, instance, time and permitted surface. Use the project's existing log, browser or CLI observations. For a real user journey with a mapped path, use [runtime feature verification](../../../0-implement/references/verification-workflows.md#w-ps1--runtime-feature-verification).
2. Apply [Attack the Premise](../../../0-diagnosing-bugs/references/premises-and-forensics.md). Write what each candidate cause predicts, capture the smallest discriminating observation and preserve evidence before effects disappear.
3. Return the observed mechanism or unresolved alternatives with the actual build and artifacts. Record missing prerequisites as blocked. Instrumentation that changes runtime state follows the caller's edit and execution scope.

## trace-forensics

1. Identify format, revision, capture conditions and time window. Read the relevant span with the project's existing trace reader. Apply [Guard the Context Window](../../../1-context-monitor/references/bulk-evidence.md) by preserving short cited excerpts plus the trace locator.
2. Compare event order with the mechanism each hypothesis predicts. Use [Code Explainer](../../../1-code-explainer/SKILL.md) if source is needed to interpret events. Report observed sequence, causal inference and missing signals distinctly.
3. Return a cited finding or the next discriminating observation. A live replay is a separate authorized phase under [Runtime Forensics](#runtime-forensics).

## perf-issue

1. Use [Performance Optimization](../../../1-performance-optimization/SKILL.md) for a measured path. Apply [Explain the Number](../../../1-performance-optimization/references/measurement-integrity.md) to match workload, output correctness, error counts and measurement conditions.
2. Use the existing profiler, browser trace, query plan or benchmark suited to the bottleneck. Compare a baseline with one justified change under like conditions. Preserve raw counts and variation.
3. Return the limiter, effect size and correctness evidence. A noisy, unmatched or failed measurement leaves the improvement unverified.

## hillclimb

1. Agree on target, workload, correctness gate and budget. Apply [Build the Lever](../../../0-implement/references/rerunnable-changes.md) by reusing a repeatable benchmark and showing it detects a known change before freezing it.
2. Apply [Explain the Number](../../../1-performance-optimization/references/measurement-integrity.md) to each result. Keep one change per attempt and record the hypothesis, paired measurements and disposition. Use the local [decision logger](../../../0-implement/scripts/log-decision.py) when an append-only trail is needed.
3. Run the same correctness and measurement checks before the next attempt. Stop at the requested target, budget or evidence limit. Report kept changes, misses, variation and the final correctness result.
