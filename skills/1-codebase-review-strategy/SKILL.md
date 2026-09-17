---
name: 1-codebase-review-strategy
description: >
  Produce a bounded, size-aware coverage strategy for reviewing an unfamiliar codebase or
  whole repository. Use to select review scope, evidence, sampling, and specialist handoffs.
  Not for: executing the review (1-code-review or a specialist), a fixed PR/diff review
  (1-code-review), or changing code. Hub: /0-review.
disable-model-invocation: true
metadata:
  catalog:
    hub: 0-review
    role: on-ramp
    when:
      - "plan evidence and coverage for an unfamiliar or whole-codebase review"
      - "choose review scope, depth, sampling, and specialist handoffs under constraints"
    not_when:
      - "execute a fixed PR, branch, or diff review → 1-code-review"
      - "execute a security audit → 1-security-auditor"
      - "review one architecture decision → 2-software-architect"
      - "implement findings → 0-implement"
    prev: [0-review]
    next: [0-review, 1-code-review, 1-security-auditor, 2-software-architect, 0-improve-codebase-architecture]
    cousins: [1-code-review, 1-security-auditor, 2-software-architect, 0-improve-codebase-architecture]
    triggers: [1-codebase-review-strategy, codebase review strategy, plan whole repository review, codebase audit plan, review coverage plan, unfamiliar repository review]
    requires_setup: false
---
# Codebase Review Strategy

**Atomic job:** return one read-only coverage and evidence plan for one immutable repository candidate. Do not run the
specialist review or change the repository.

## Contract

1. Pin caller, review decision/use, repository root, exact worktree/branch/`HEAD`, comparison baseline if any, dirty
   paths and owners, allowed/excluded paths, generated/vendor/build exclusions, time and tool budget, evidence cutoff,
   required axes, and output format. Record whether working-tree changes are included. A worktree does not isolate
   shared services, caches, databases, scanners, credentials, or remote state.
2. Inspect only enough read-only repository evidence to design coverage: instructions, manifests, topology, language
   mix, ownership/boundaries, tests, CI, risk surfaces, churn or dependency signals when locally available. Never
   install a counter/scanner, execute repository code, start services, fetch remotes, or widen from a named subtree
   without separate authority.
3. Choose depth from risk, heterogeneity, critical paths, and decision need—not fixed LOC tiers or arbitrary sample
   quotas. Define deterministic inclusions plus explicit risk-based sampling, blind spots, stop conditions, and the
   evidence required to support each review claim.
4. Map each review slice to exactly one owner: change quality `/1-code-review`; security `/1-security-auditor`;
   architecture decision `/2-software-architect`; architecture-deepening survey `/0-improve-codebase-architecture`.
   Handoffs are recommendations only and inherit the exact candidate and exclusions.
5. Return candidate identity, measured facts, proposed slices/order, axis-to-evidence map, exclusions, sampling logic,
   estimated effort as a range/assumption, specialist handoffs, unknowns, and coverage limits to `/0-review` or the
   actual caller. Do not claim the codebase was reviewed.

## References

Load [measurement guidance](./references/measurement-commands.md) only for safe local inspection and
[prompt templates](./references/prompt-templates.md) only as adaptable handoff schemas. Apply the
[clarification boundary](./references/interactive-clarification.md); the longer upstream process is
kept as [provenance notes](./references/full-guide.md); it does not override this contract.
