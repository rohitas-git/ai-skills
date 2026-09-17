---
name: 1-security-auditor
description: >
  Multi-phase security and quality auditor for codebases. Use for security audit, OWASP
  review, scoped project audit, or differential PR security review. Not for: multi-axis PR review (1-code-review) or build-time hardening
  patterns (2-security-and-hardening). Hub: /1-security-auditor. Triggers: security audit, OWASP, vulnerability review.
disable-model-invocation: true
metadata:
  catalog:
    hub: 1-security-auditor
    role: sub-hub
    when:
      - "security/OWASP audit"
      - "vulnerability review of project"
      - "differential security review of a pinned PR or change"
    not_when:
      - "PR multi-axis review → 1-code-review"
      - "apply hardening while building → 2-security-and-hardening"
    next: [2-security-and-hardening, 2-prompt-injection-defense, 2-skill-supply-chain-audit, 2-dependency-security]
    cousins: [2-security-and-hardening, 1-code-review]
    triggers: [security audit, OWASP, vulnerability review, audit authentication, security assessment, find security issues, PR security review, differential security audit]
    requires_setup: false
---

# Security Auditor
## Boundary

| Need | Skill |
|------|--------|
| Multi-phase security/quality audit + findings | **security-auditor** (this) |
| Harden while coding / after findings | `/2-security-and-hardening` |
| Test agent boundaries against prompt injection | `/2-prompt-injection-defense` |
| Audit third-party agent skills or packages | `/2-skill-supply-chain-audit` |
| Review application dependency vulnerabilities, staleness, or new packages | `/2-dependency-security` |
| Multi-axis PR/diff 0-review | `/1-code-review` |
| Pick 0-review mode | `/0-review` F-R1 |


## Overview

Perform structured, multi-phase audits of codebases and projects to surface security vulnerabilities, functional bugs, logical errors, race conditions, edge cases, and ambiguities. Findings must be high-signal, independently verified, and include concrete scenarios and impact. Prefer exploitable or demonstrably incorrect issues over theoretical risks.

## Core Principles

- Require concrete evidence, reproduction scenario, and real impact for every finding.
- Severity = impact × likelihood. Do not inflate severity for checklist items alone.
- Adversarial validation is mandatory — separate reasoning must try to disprove each candidate.
- Independent verification of every factual claim against source is required before finalizing.
- Runs are additive only when continuing the same explicitly identified audit; verify prior findings' repository, scope and revision before reuse. Do not ingest an arbitrary findings.json from the working directory.
- Scope can be full project or limited (e.g. "only auth module", "only changed files").
- Cover source code, configuration, dependencies, build/CI, architecture docs, and IaC when present.
- Surface ambiguity as a finding when it can reasonably lead to defects or security issues.

## Workflow

**Dispatch first:** establish caller, scope and inspection-only authority with [the candidate contract](../0-review/references/review-candidate.md). Honor an already-selected specialist or audit scope; use F-R2/F-R3 only for unresolved choices. For a PR, changed files or a commit range, load [differential-pr-audit.md](./references/differential-pr-audit.md) before reconnaissance. High risk warrants deeper causal tracing, not an unrequested whole-repository audit. Each child receives the same scope/candidate and returns findings here without starting remediation or another full audit.

Source inspection needs no new worktree. Runtime checks may use an existing matching isolated workspace through `/1-git-worktrees`, then resume this audit. Do not change the caller's branch, install scanners, execute third-party code, rotate credentials, reset shared services or run production probes. Use only permitted non-destructive checks; document blocked evidence. Delegation is optional, permission-bound and does not imply filesystem isolation.

Execute the following phases in order. Do not skip phases. Load the referenced files when starting each phase. Named artifacts below describe report content; write files only when requested in an agreed location, otherwise retain that content in the returned report.

### Phase 1 — Reconnaissance
Load and follow `references/recon.md`.
Also consult `references/supply-chain.md` for dependency and build-pipeline mapping.
Map architecture, trust boundaries, entry points, data flows, auth model, dependencies, configs, and documentation. Produce `architecture.md`. Identify project type and languages to select relevant attack classes.

### Phase 2 — Hunting
Load and follow:
- `references/attack-classes.md` (core classes)
- `references/owasp-and-secure-coding.md`
- `references/language-stack-patterns.md` (for the languages/stacks in use)
- `references/concurrency-races.md` (when concurrency is present)
- `references/ai-llm-agent-risks.md` (when AI/LLM/agent components exist)
- `references/supply-chain.md` (dependencies, CI, containers)

Run the relevant specialized review passes locally, or with independent agents only when permitted and the candidate is stable. Use focused child skills instead of duplicating their full workflows. Produce candidate findings with evidence, location, scenario, and estimated impact.

For differential or PR-only audits, also load and follow `references/differential-pr-audit.md`.

### Phase 3 — Validation
Load and follow the validation section of `references/validation-and-reporting.md`.
Also load `references/false-positives.md` and actively use it to reject weak candidates.
For every candidate, actively attempt to disprove it. Reject any finding that cannot survive adversarial scrutiny or lacks a concrete scenario.

### Phase 4 — Reporting
Generate human-readable `REPORT.md` (executive summary + prioritized findings) and `FINDINGS-DETAIL.md` (deep traces for Medium+ severity).
Use `references/remediation-prioritization.md` to order findings and produce a clear remediation roadmap.

### Phase 5 — Structured Output
When JSON output is requested, use [findings-schema.json](./references/findings-schema.json) and run `node scripts/validate-findings.js /absolute/path/to/findings.json` from this skill directory. The dependency-free validator checks schema structure and report consistency, not exploit validity; date-time format remains an annotation. Missing Node or invalid input is a verification gap, not a pass. For chat/caller output keep the same evidence fields without creating a file.

### Phase 6 — Independent Verification
Load the independent verification section of `references/validation-and-reporting.md`.
Use fresh reasoning (or a new agent context if possible) to re-verify every factual claim in the structured findings against the actual source code and project artifacts. Only verified findings remain in the final output.

## Output Requirements

For a full audit with report files requested, produce in the agreed audit directory without overwriting unrelated artifacts:
- `architecture.md`
- `REPORT.md`
- `FINDINGS-DETAIL.md` (for Medium+ items)
- `findings.json` (schema-validated)

Otherwise return the report in chat or to the calling review workflow. Reuse prior `findings.json` only when its identity matches this audit and the user supplied or selected it. A review never authorizes remediation, comment publication, approval or a recursive review pipeline.

## Anti-Patterns (Never Do These)

- Report pure style, formatting, or subjective "code smell" without security, logic, or ambiguity impact.
- Accept a finding without a concrete scenario and demonstrated or highly plausible impact.
- Skip adversarial validation or independent verification.
- Invent findings or claim issues not grounded in observable code or artifacts.
- Treat every static-analysis pattern match as a confirmed vulnerability.
- Overwhelm the user with low-severity noise — prioritize and clearly rank.
- Ignore project-specific context (e.g. treating a pure library the same as a web app).

## Scope (F-R2)

If scope is unresolved, ask once: **full project** (recommended) · **scoped module** · **differential/PR only** · **Agent judgment**. Honor a caller's already-selected scope; do not ask the same fork again.

## Agent security focus (F-R3)

When the specialist is ambiguous, ask once: **prompt-injection boundaries** · **third-party agent/package provenance** · **application dependency checks** · **general security audit** (recommended when multiple surfaces are in scope) · **Agent judgment**. Otherwise route directly to the matching child in review-only mode, with the original caller as return target.

## Additional Guidance

- Prefer depth over breadth when time or context is limited. Cover high-risk areas (auth, input handling, crypto, access control, concurrency-critical paths) first.
- When the project contains AI/LLM or agent components, load the expanded guidance in `references/ai-llm-agent-risks.md`.
- For differential audits (PR or changed files only), follow `references/differential-pr-audit.md` while still performing lightweight surrounding-context recon.
- After the final verified findings, offer a concise prioritized remediation plan using the framework in `references/remediation-prioritization.md`.
- Use `references/false-positives.md` aggressively in validation to keep signal high.
- For prevention patterns while remediating → `/2-security-and-hardening`.
- Infrastructure-security taxonomies from the BagelHole snapshot are indexed in the DevOps [vendor map](../0-devops/references/vendor-map.md); treat scanner and command examples as leads, not findings.

## Related

- **Parent domain:** `/0-review` (this skill is a **sub-hub**)
- **Soft next:** `/2-security-and-hardening` (remediate / prevent)
- **Not for:** multi-axis diff/PR closer → `/1-code-review`; large-repo plan-first → `/1-codebase-review-strategy`
