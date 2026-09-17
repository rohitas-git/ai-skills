---
name: 1-complete-pr-review
description: >
  Produce one comprehensive, evidence-backed, risk-weighted review of a single pull request without changing it.
  Use when: comprehensive PR review, complete pull request review, code and security review, or final review before repair.
  Not for: code-only review (1-code-review), a full-project security audit (1-security-auditor),
  agent-specific PR preflight (1-agent-pr-review), or fixing findings (1-pr-repair). Hub: /0-review.
disable-model-invocation: true
metadata:
  catalog:
    hub: 0-review
    role: pipeline
    when:
      - "perform a comprehensive risk-weighted review of one pull request"
      - "produce a PR-scoped code, security, testing, reliability, delivery, and operability report before repair or approval"
    not_when:
      - "code/quality review only → 1-code-review"
      - "full-project or module security audit → 1-security-auditor"
      - "AI-authored PR risk preflight only → 1-agent-pr-review"
      - "repair known findings → 1-pr-repair"
    next: [1-receive-review, 1-pr-repair]
    cousins: [1-code-review, 1-security-auditor, 1-agent-pr-review, 1-pr-review-and-repair]
    triggers: [comprehensive PR review, complete PR review, full PR review, code and security review, pull request audit]
    requires_setup: false
  sources:
    - url: https://www.youtube.com/watch?v=HUdmjJQg9UI&t=57s
      note: "Effective Pull Request Checklist; public page and auto-generated caption track retrieved."
    - url: https://www.youtube.com/watch?v=lz32biXRwdM&t=64
      note: "User-supplied review-area reference."
    - url: https://www.gustavwengel.dk/2025/02/19/pr-reviewer-practices.html
      note: "User-supplied review-area reference."
    - url: https://medium.com/@iamprovidence/ultimate-guide-to-pr-review-process-6d75c8886763
      note: "User-supplied review-area reference."
    - url: https://medium.com/@dorinbaba/the-perfect-pr-review-checklist-no-one-is-talking-about-50ca213a4ac1
      note: "User-supplied review-area reference."
    - url: https://share.google/aimode/AzDyECjLa75p9CguE
      note: "User-supplied link; it resolved to generic Google Search content at authoring, so no unverified material was adopted."
---

# Comprehensive PR Review

Perform one comprehensive, risk-weighted review of one PR's fixed diff, then return one
verified finding ledger. It is review-only: it does not edit, commit, push, publish comments, approve, or merge.

## Boundary

| Need | Skill |
|---|---|
| Comprehensive, PR-scoped review across every applicable risk area | **this skill** |
| Code quality, spec, standards, and maintainability only | `/1-code-review` |
| Full-project or module security audit | `/1-security-auditor` |
| AI-authored PR risk preflight | `/1-agent-pr-review` |
| Repair validated PR findings | `/1-pr-repair` |
| Review and repair repeatedly | `/1-pr-review-and-repair` |

## PR scope guard

The boundary is the declared base merge-base, the PR diff, and behavior changed by that
diff. Read adjacent code only to establish context or a concrete exploit/regression path.
Report pre-existing defects, unrelated cleanup, and broad hardening opportunities as
follow-ups; promote a pre-existing weakness to a change finding only with evidence
that the PR newly exposes or materially worsens it. This skill never changes code.

## Process

1. **Pin the PR.** Apply [the shared candidate contract](../0-review/references/review-candidate.md). Resolve one repository, PR, declared base, base/head SHAs, merge-base, changed files, stated intent, required checks, and review exclusions. Review the published head; stop if identity is not unique or changes during review.
2. **Build the change and risk map.** Load [the comprehensive protocol](./references/comprehensive-review-protocol.md). Trace changed entry points, contracts, callers, data and trust boundaries, persistence, concurrency, dependencies, CI/release paths, user surfaces, tests, and operations impact. Every coverage area receives a disposition. Do not equate exhaustive checklist traversal with review completeness; depth follows changed risk and evidence.
3. **Run the code and contract pass.** Invoke `/1-code-review` on the same pinned PR candidate and return here. Cover every applicable Spec, Standards, and Maintainability axis, including behavior, edge cases, interfaces, compatibility, architecture, error paths, and proportionate complexity. Child passes never repair or start another complete review.
4. **Run the differential security pass.** Invoke `/1-security-auditor` in differential/PR mode on the same pinned PR candidate. Keep output in memory unless files were explicitly requested. Cover changed authorization, validation, privacy, secrets, dependencies, CI, supply chain, and abuse paths without claiming a repository-wide audit.
5. **Close material coverage gaps.** Inspect testing, reliability/concurrency, performance/resources, build/delivery, operability/observability, accessibility/user impact, documentation, migrations, and rollback implications when touched. Use a focused specialist only when the risk map demonstrates a material gap; preserve the candidate and return target, and never launch a checklist-driven swarm.
6. **Verify proportionately.** Run only authorized, non-destructive checks that can distinguish the changed behavior or claim. Record exact commands, candidate/config/environment, exit status, and relevance. A green but irrelevant test, stale CI result, or tool success is not evidence for an uncovered contract.
7. **Validate and deduplicate.** Admit a finding only with location, concrete trigger, impact, PR causality, severity, evidence, and a failed attempt to disprove it. Merge duplicates while retaining all lenses. Keep rejected leads, pre-existing issues, optional improvements, human decisions, and blocked evidence separate.
8. **Return one ledger.** Order actionable findings by severity, then report per-area dispositions, verification evidence, rejected leads, follow-ups, and limits. State the pinned SHAs and whether the candidate stayed stable. A chat report is not a GitHub review; repair, comments, approval, merge, or release require separate authority.

## Completion

The review is complete only when every applicable protocol area has a disposition, material
changed paths were traced deeply enough for their risk, each remaining finding is evidence-backed
and PR-caused, and limitations are explicit. “No findings” means none survived within recorded
coverage; it is not approval, merge readiness, or proof that the repository is defect-free or secure.

## Progressive disclosure

| Load when | File |
|---|---|
| Coverage, evidence acceptance, dispositions, and report schema | [comprehensive review protocol](./references/comprehensive-review-protocol.md) |
| Source provenance for adopted review areas | [source notes](./references/source-notes.md) |

## Related

Use `/1-receive-review` to evaluate incoming feedback or `/1-pr-repair` to apply an approved queue.
