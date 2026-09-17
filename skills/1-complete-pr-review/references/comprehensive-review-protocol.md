# Comprehensive PR review protocol

Use this protocol to make coverage explicit without turning review into mechanical checklist theater. Review the fixed PR candidate, not an imagined final system. Start broad enough to find changed risk, then go deep on the paths whose failure would matter.

## Coverage dispositions

Every area below receives exactly one disposition in the final report:

- **finding** — at least one validated, PR-caused defect survives adversarial review.
- **no finding within reviewed coverage** — the inspected evidence produced no surviving issue; name the actual paths and checks.
- **not applicable** — the PR does not touch this area; give the short reason.
- **blocked** — intended evidence could not be obtained because of a concrete permission, environment, identity, or tool constraint.
- **coverage gap** — the area applies, but available evidence is insufficient for a responsible conclusion.

Do not use “passed” for source inspection alone. Do not turn missing evidence into a defect unless the missing evidence itself violates an applicable contract.

## Coverage matrix

| Area | Inspect when changed or plausibly affected | Evidence questions |
|---|---|---|
| **Intent and change shape** | Always | Does the diff match the PR's stated problem and acceptance criteria? Are unrelated or generated changes explained? Is the size coherent enough to review? |
| **Behavior and correctness** | Always | Do happy paths, boundaries, empty/zero/max cases, state transitions, side effects, and failure paths preserve the intended contract? |
| **Interfaces and compatibility** | Public APIs, schemas, events, commands, config, persistence, migrations | Are callers/consumers compatible? Are defaults, versioning, migrations, serialization, downgrade, rollback, and deprecation behavior safe? |
| **Architecture and maintainability** | New modules, responsibilities, dependencies, abstractions, or cross-layer changes | Does the change preserve ownership and cohesion, reuse fitting project code, avoid speculative indirection, and remain understandable? |
| **Security, privacy, and abuse** | Inputs, authn/authz, secrets, sensitive data, network, dependencies, CI, agents | Can an attacker cross a changed trust boundary, gain privilege, disclose/retain data, inject instructions, poison dependencies, or abuse resources? |
| **Reliability and concurrency** | Async work, queues, retries, locks, caching, distributed state, cleanup | Are idempotency, ordering, atomicity, races, timeouts, retry budgets, partial failure, cancellation, and cleanup handled? |
| **Performance and resource use** | Hot paths, queries, loops, large payloads, rendering, allocation, I/O | Is complexity proportionate? Are batching, limits, indexes, caching, backpressure, and memory/CPU/network costs safe at realistic scale? |
| **Dependencies, build, and delivery** | Manifests, lockfiles, toolchains, CI, containers, flags, deployment config | Is the dependency necessary and compatible? Are provenance and lock changes coherent? Are checks, rollout gates, flags, and artifacts preserved rather than weakened? |
| **Tests and verification** | Always | Do tests exercise the changed contract and relevant failure modes? Would they catch the pre-change defect or regression? What exact candidate and environment ran? |
| **Operability and observability** | Services, jobs, integrations, migrations, behavior operators must diagnose | Are logs, metrics, traces, alerts, diagnostics, runbooks, rollout, rollback, and failure visibility sufficient without leaking sensitive data? |
| **User experience and accessibility** | User-facing UI, CLI, API errors, workflows, content | Are states, keyboard/focus, semantics, contrast, responsive behavior, localization, error recovery, latency feedback, and compatibility preserved where applicable? |
| **Documentation and release impact** | User/developer-visible behavior, setup, config, API, operational change | Are docs, examples, changelog/release notes, migration instructions, ownership, and follow-up work accurate and proportionate? |

Adjacent code may be read to prove a call path, contract, or impact. It does not become review scope merely because it is nearby.

## Risk weighting

Prioritize depth using concrete change signals:

1. irreversible data loss, authorization, privacy, secrets, money, safety, or production availability;
2. externally consumed contracts, migrations, concurrency, distributed state, and recovery paths;
3. broad fan-out, critical workflows, dependency/build/CI changes, and hard-to-observe behavior;
4. ordinary local logic and maintainability;
5. optional style or alternative design.

High risk means deeper causal tracing and stronger evidence, not automatic high severity. Large diffs and missing descriptions are coverage signals, not findings by themselves.

## Finding acceptance test

A final finding must contain all of the following:

1. **Location** — exact file and tight line/range on the reviewed candidate.
2. **Observation** — what the changed code or artifact actually does.
3. **Trigger** — a concrete input, state, sequence, actor, scale, or failure condition.
4. **Impact** — the incorrect or unsafe externally meaningful result.
5. **PR causality** — how this PR introduces, exposes, or materially worsens the issue.
6. **Evidence** — code trace, contract, test, command output, or authoritative project rule.
7. **Counterevidence** — what was checked in an attempt to disprove or downgrade it.
8. **Severity** — Critical, Major/Important, Nit, or Optional, based on consequence and likelihood.
9. **Direction** — the smallest in-scope remediation and the verification that would close the finding.

Reject candidates that depend on an impossible path, ignore an existing guard, cite only preference, lack PR causality, or merely request unrelated cleanup. Do not expose secrets or unnecessary sensitive records in evidence.

## Specialist use

The required combined review is `/1-code-review` plus differential `/1-security-auditor` on the same candidate. Add a focused pass only when changed risk demands evidence those two passes cannot provide efficiently, for example:

- `/1-agent-pr-review` or `/2-prompt-injection-defense` for a changed AI/agent trust boundary;
- `/2-dependency-security` for a consequential dependency or lockfile change;
- `/2-software-architect` for a consequential system-boundary decision;
- `/1-error-handling` for complex recovery/retry/cleanup behavior;
- `/1-go-best-practices` for material Go-specific API or concurrency mechanics.

Do not invoke every specialist for every PR. Record why each was used, skipped, or unnecessary. A specialist returns evidence here and never starts repair or a sibling review pipeline.

## Verification evidence

For every command or CI result used as evidence, record:

- command/check name and relevant configuration;
- repository, candidate SHA or dirty-state identity, and environment;
- exit/status and the behavior it actually exercises;
- whether the result is fresh, cached, head-only, or a synthetic merge build;
- blocked, flaky, skipped, or unverified portions.

Static inspection can validate many findings without execution. Runtime checks must be permitted, non-destructive, relevant, and safe for the current environment. Never install tools, use production credentials, weaken checks, or mutate shared services to make a review appear complete.

## Report schema

Return sections in this order:

1. **Candidate** — repository, PR, base/head SHAs, merge-base, dirty/published state, stability recheck, intent, exclusions.
2. **Findings** — severity-ordered accepted findings using every acceptance-test field; say “none” when none survive.
3. **Coverage matrix** — all twelve areas with disposition, evidence inspected, and limits.
4. **Verification** — commands and CI evidence with relevance and status.
5. **Rejected leads** — plausible candidates rejected after counterevidence, briefly stated.
6. **Follow-ups** — pre-existing issues and optional improvements outside this PR's required scope.
7. **Human decisions and blockers** — unresolved product, policy, permission, environment, or ownership choices.
8. **Bottom line** — highest remaining risk and what was not verified; never silently convert this into approval or merge readiness.

Keep the report concise relative to evidence. Zero findings does not justify filler, praise, an approval action, or a claim of exhaustive security.
