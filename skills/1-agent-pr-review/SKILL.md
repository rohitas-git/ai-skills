---
name: 1-agent-pr-review
description: >
  Run a risk-focused review pass for an agent-generated pull request before approval. Use when reviewing
  AI-authored PRs, especially with CI, new utilities, non-trivial logic, or agent workflows. Not for:
  ordinary multi-axis PR review (1-code-review), broad security audit (1-security-auditor), or repairing
  findings (1-pr-repair). Hub: /0-review.
disable-model-invocation: true
metadata:
  catalog:
    hub: 0-review
    role: leaf
    when:
      - "review an agent-generated pull request"
      - "check AI-authored PR for CI weakening, duplicate utilities, or unsafe agent workflow"
    not_when:
      - "ordinary PR/diff review → 1-code-review"
      - "broad security audit → 1-security-auditor"
      - "implement approved PR findings → 1-pr-repair"
    next: [1-code-review, 1-pr-repair]
    cousins: [1-code-review, 1-security-auditor, 2-prompt-injection-defense, 1-pr-repair]
    triggers: [agent PR review, AI-generated PR review, review AI pull request, agent-authored PR]
    requires_setup: false
  vendor:
    source: github-blog-agent-pr-review
    source_url: https://github.blog/ai-and-ml/generative-ai/agent-pull-requests-are-everywhere-heres-how-to-review-them/
---

# Agent PR Review

**Atomic job:** surface the risks that agent-generated pull requests disproportionately hide before normal approval or repair work begins.

## Process

1. **Pin and classify the change.** Apply [the shared candidate contract](../0-review/references/review-candidate.md): exact PR/base/head, caller, scope and read-only authority. Inspect the actual diff and available intent before asking for missing context. An empty PR body or large diff is a coverage/sizing signal, not an automatic defect; review the resolvable scope and identify any specific missing decision.
2. **Check CI changes first.** Block changes that remove, skip, weaken, or conditionally suppress tests, coverage, lint, build, pull-request, or fork checks unless an explicit, reviewed justification preserves the intended protection.
3. **Search for duplicate additions.** Search for existing equivalents of new helpers, validators, middleware and modules. Verify behavioral compatibility and ownership before recommending reuse; similar names alone do not justify consolidation or cross-module coupling.
4. **Trace critical changed paths.** Start at the highest-risk input and follow transformations to output; expand to other independent high-risk paths within scope. Check relevant empty/zero/max cases, validation, authorization branches and surprising conditionals. Assess whether focused tests detect the changed contract or regression; a preserved-behavior refactor need not fail its correct pre-change tests. Do not mistake one traced path for complete coverage.
5. **Inspect agent-workflow boundaries when touched.** For LLM consumption of PR/issue/commit content or execution of model output, use a necessary `/2-prompt-injection-defense` or differential `/1-security-auditor` pass on the same candidate. Return findings here; avoid rerunning a lens the caller already covered. Validate untrusted-data flows, token permissions, executable output and secret exposure against concrete scenarios rather than declaring every pattern a blocker.
6. **Return an evidence-backed review queue.** Give each check a disposition (findings, no findings within coverage, not applicable, or blocked), with locations, evidence and PR causality. Separate pre-existing issues and unverified claims. Return to a combined review or repair caller without starting another pipeline. Standalone invocation stops at the report: `/1-code-review` is an optional broader review, and `/1-pr-repair` is only a handoff for authorized repair. Never publish comments or approve a PR implicitly.

## Boundary

| Need | Skill |
|---|---|
| Risk-focused pass for an agent-generated PR | **this skill** |
| Multi-axis review of any PR or diff | `/1-code-review` |
| Full security audit | `/1-security-auditor` |
| Agent workflow prompt-injection boundaries | `/2-prompt-injection-defense` |
| Repair approved findings on one PR | `/1-pr-repair` |

## Provenance

Adapted from [source notes](./references/vendor-source.md). It adds no hook, automated approval, shell execution, or merge authority.
