---
name: 1-security-auditor
description: >
  Multi-phase security and quality auditor for codebases. Use for security audit, OWASP
  review, scoped project audit. Not for: multi-axis PR review (1-code-review) or build-time hardening
  patterns (2-security-and-hardening). Hub: /1-security-auditor. Triggers: security audit, OWASP, vulnerability review.
disable-model-invocation: true
metadata:
  catalog:
    hub: 1-security-auditor
    role: sub-hub
    when:
      - "security/OWASP audit"
      - "vulnerability review of project"
    not_when:
      - "PR multi-axis review → 1-code-review"
      - "apply hardening while building → 2-security-and-hardening"
    cousins: [2-security-and-hardening, 1-code-review]
    triggers:
      - "security audit"
      - "OWASP"
      - "vulnerability review"
    requires_setup: false
---

# Security Auditor
## Boundary

| Need | Skill |
|------|--------|
| Multi-phase security/quality audit + findings | **security-auditor** (this) |
| Harden while coding / after findings | `/2-security-and-hardening` |
| Multi-axis PR/diff 0-review | `/1-code-review` |
| Pick 0-review mode | `/0-review` F-R1 |


## Overview

Perform structured, multi-phase audits of codebases and projects to surface security vulnerabilities, functional bugs, logical errors, race conditions, edge cases, and ambiguities. Findings must be high-signal, independently verified, and include concrete scenarios and impact. Prefer exploitable or demonstrably incorrect issues over theoretical risks.

## Core Principles

- Require concrete evidence, reproduction scenario, and real impact for every finding.
- Severity = impact × likelihood. Do not inflate severity for checklist items alone.
- Adversarial validation is mandatory — separate reasoning must try to disprove each candidate.
- Independent verification of every factual claim against source is required before finalizing.
- Runs are additive — load any existing findings.json and avoid re-reporting known issues unless they have changed.
- Scope can be full project or limited (e.g. "only auth module", "only changed files").
- Cover source code, configuration, dependencies, build/CI, architecture docs, and IaC when present.
- Surface ambiguity as a finding when it can reasonably lead to defects or security issues.

## Workflow

Execute the following phases in order. Do not skip phases. Load the referenced files when starting each phase.

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

Run multiple specialized 0-review passes (or parallel sub-agents if available). Produce candidate findings with evidence, location, scenario, and estimated impact.

For differential or PR-only audits, also load and follow `references/differential-pr-audit.md`.

### Phase 3 — Validation
Load and follow the validation section of `references/validation-and-reporting.md`.
Also load `references/false-positives.md` and actively use it to reject weak candidates.
For every candidate, actively attempt to disprove it. Reject any finding that cannot survive adversarial scrutiny or lacks a concrete scenario.

### Phase 4 — Reporting
Generate human-readable `REPORT.md` (executive summary + prioritized findings) and `FINDINGS-DETAIL.md` (deep traces for Medium+ severity).
Use `references/remediation-prioritization.md` to order findings and produce a clear remediation roadmap.

### Phase 5 — Structured Output
Emit `findings.json` conforming to `references/findings-schema.json`. Validate the file before proceeding (use `scripts/validate-findings.js` if available).

### Phase 6 — Independent Verification
Load the independent verification section of `references/validation-and-reporting.md`.
Use fresh reasoning (or a new agent context if possible) to re-verify every factual claim in the structured findings against the actual source code and project artifacts. Only verified findings remain in the final output.

## Output Requirements

Always produce (in the working directory or a user-specified audit directory):
- `architecture.md`
- `REPORT.md`
- `FINDINGS-DETAIL.md` (for Medium+ items)
- `findings.json` (schema-validated)

If prior `findings.json` exists, load it, mark previously known issues, and focus new effort on unexplored areas.

## Anti-Patterns (Never Do These)

- Report pure style, formatting, or subjective "code smell" without security, logic, or ambiguity impact.
- Accept a finding without a concrete scenario and demonstrated or highly plausible impact.
- Skip adversarial validation or independent verification.
- Invent findings or claim issues not grounded in observable code or artifacts.
- Treat every static-analysis pattern match as a confirmed vulnerability.
- Overwhelm the user with low-severity noise — prioritize and clearly rank.
- Ignore project-specific context (e.g. treating a pure library the same as a web app).

## Scope (F-R2)

If the user did not name a path or PR, ask once: **full project** (recommended) · **scoped module** · **differential/PR only**. Then proceed with the matching recon/hunt depth.

## Additional Guidance

- Prefer depth over breadth when time or context is limited. Cover high-risk areas (auth, input handling, crypto, access control, concurrency-critical paths) first.
- When the project contains AI/LLM or agent components, load the expanded guidance in `references/ai-llm-agent-risks.md`.
- For differential audits (PR or changed files only), follow `references/differential-pr-audit.md` while still performing lightweight surrounding-context recon.
- After the final verified findings, offer a concise prioritized remediation plan using the framework in `references/remediation-prioritization.md`.
- Use `references/false-positives.md` aggressively in validation to keep signal high.
- For prevention patterns while remediating → `/2-security-and-hardening`.

## Related

- **Parent domain:** `/0-review` (this skill is a **sub-hub**)
- **Soft next:** `/2-security-and-hardening` (remediate / prevent)
- **Not for:** multi-axis diff/PR closer → `/1-code-review`; large-repo plan-first → `/1-codebase-review-strategy`
