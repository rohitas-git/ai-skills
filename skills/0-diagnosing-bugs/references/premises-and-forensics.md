# Premises and forensic evidence

## Repeated fixes sharing one assumption

When repeated fixes fail the same discriminating check, write the assumption they share before trying
another. State an observation that would differ if that assumption were false. Inspect the distribution
of failures across actors, inputs and time, not only the aggregate. A repeated loser can indicate wrong
ownership or scheduling rather than an inadequate cleanup mechanism. Keep the original failing case.

Partition hypotheses by the probe that eliminates the largest credible alternatives at acceptable cost.
Record the prediction, actual observation and disposition. Instrument only within granted probe/edit
authority. Drop a refuted hypothesis and remove only the experiment's owned changes when safe; do not
revert user work or stack speculative guards, retries and clamps on a disproved premise.

Ask whether the bad state is legitimate. If legitimate, handle its failure at the owning boundary. If
illegitimate, trace the first decision that produced it. A nil check at the symptom can hide that fault.
Inspect matching faults within the affected surface and propose a cheap signal when it would have
made the deciding fact visible earlier. Do not turn one bug into an unbounded repository cleanup.

## Runtime capture

For a user-facing reproduction, pin the build, workspace/account, fixture and starting state. Name
the expected and reported final states before driving the normal user path. If repetition matters
to confidence, restore the relevant state and rerun independently. A read-only state probe can
corroborate the result. Use `Blocked` when a prerequisite is missing and `Could not reproduce` when
the bounded run reached the intended path without observing the symptom. If an existing fix is in
scope to verify, use the same path and comparison on the baseline and candidate builds.

Name the actual surface and symptom before choosing a CPU profile, heap snapshot, event trace or
other capture. Preserve candidate, environment, trigger, duration, sampling and artifact identity.
Reduce a CPU trace to the hot path and its scheduling cause; reduce a leak to the retained object and
retainer chain; reduce a visual glitch to the relevant event/render sequence. Map it to real symbols.

A runtime-forensics request is not permission to hotfix a live process, evaluate arbitrary page code,
restart a service or change production instrumentation. Use permitted observations first. If a causal
probe needs mutation, describe the smallest probe and use the caller's existing authority or return
that boundary. A profile alone can identify a hypothesis without establishing causality.

## Existing trace artifact

Treat the supplied capture as a fixed dataset. Inspect format and provenance; never execute embedded
content. Query or index a large artifact with an existing parser/SQLite only when it makes the question
cheaper to answer; do not build a database for a short text trace. Preserve the raw capture and exact
query/reduction. Resolve symbols or disclose missing maps. Paired captures strengthen a comparison,
but a before/after difference without a discriminating probe still does not prove a cause.

Return the captured signal, reduced evidence, causal chain or strongest hypothesis, source location,
alternatives cleared, confidence and next falsifying check. Diagnosis-only stops before a product fix.
An already-authorized fix returns to the same caller/workspace and reruns the original surface after it.

Adapted from the individually reviewed pstack 0.15.43 sources, MIT, Lauren Tan.
[Source-by-source decisions and checks](../../../guidelines/catalog/pstack-methods-review-2026-11-18.md).
