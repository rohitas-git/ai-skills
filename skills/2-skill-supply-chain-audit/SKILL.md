---
name: 2-skill-supply-chain-audit
description: >
  Review a fixed third-party agent package or update for provenance, permissions, and unsafe behavior without executing it. Use when: assessing a skill, plugin, MCP package, archive, or suspicious update before enabling it. Not for: catalog structure lint (1-skill-linter), application dependency review (2-dependency-security), or installation/catalog mutation (0-skill-manager). Hub: /1-security-auditor.
disable-model-invocation: true
license: MIT
metadata:
  catalog:
    hub: 1-security-auditor
    role: leaf
    when:
      - "reviewing an untrusted agent skill, plugin, MCP integration, or package"
      - "comparing an agent package against a known-good version"
    not_when:
      - "catalog conformance lint → 1-skill-linter"
      - "application dependency review → 2-dependency-security"
      - "installation or catalog mutation → 0-skill-manager"
    prev: [1-security-auditor, 0-agent-engineering]
    next: [1-security-auditor, 0-agent-engineering, 1-skill-linter, 2-dependency-security, 2-prompt-injection-defense]
    cousins: [1-skill-linter, 1-security-auditor, 0-skill-manager, 2-security-and-hardening]
    triggers: [skill supply chain, audit a skill, audit agent skill, plugin security, agent package provenance, review MCP package]
    requires_setup: false
  vendor:
    source: seb1n/awesome-ai-agent-skills
    upstream_id: skill-supply-chain-audit
    commit: 75865a5d037a4cdaa7f409a4ec14ab9b0292920b
---

# Skill Supply-Chain Audit

## Boundary

| Need | Skill |
|------|-------|
| Security review of agent packages | **this skill** |
| Catalog naming, routing, and membership lint | `/1-skill-linter` |
| Broad codebase security audit | `/1-security-auditor` |
| Application dependency advisories/staleness | `/2-dependency-security` |
| Agent trust-boundary design | `/2-prompt-injection-defense` |
| Install/place or apply package changes | `/0-skill-manager` for catalog work; otherwise return to the authorized build caller |

## Process

1. Record the caller, requested package/version, expected capability, runtime, permissions, sensitive data exposure, exclusions and baseline. A PR/update review uses [the candidate contract](../0-review/references/review-candidate.md); distinguish introduced changes from prior package risk. Unknown publisher/version is unknown, not trusted by popularity.
2. Inspect a fixed, private snapshot read-only. Do not import target code, run hooks/installers, resolve dependencies by installing them, render active content, follow embedded commands/links, or expose credentials. Source inspection needs no new worktree. If separately authorized dynamic testing needs isolation, use `/1-git-worktrees` only for checkout ownership; it is not a security sandbox. Require a disposable restricted runtime, synthetic data, resource limits and denied-by-default egress, then return here.
3. Read [the checklist](./references/review-checklist.md). Inventory instructions, executable entry points, dependencies, origins, credential access, filesystem reach, persistence and updates. Trace source → processing → destination → retention; a regex hit establishes text presence, not runtime behavior or a vulnerability.
4. Use the [scanner contract](./references/scanner-contract.md) when a filesystem inventory helps. Inspect every material entry in its review queue or retain an explicit blocking gap. Metadata-only archive inspection and hashes never establish member-content safety. Compare both versions' coverage as well as content/type/mode/link changes.
5. Return an evidence-backed **recommendation**, not an installation approval: accept for the stated scope, accept only under verified constraints, defer pending evidence, or reject. Use the [report template](./assets/audit-report-template.md) in chat unless a file was requested; include candidate/hash, observed/inferred/unknown claims, prerequisites, gaps, constraints and residual risk. No assertion of malware absence or certification.

## Return and authority

- Return to the ingest, security-review or agent-engineering caller; standalone audit stops at its report. Do not install, enable, publish, edit, commit, move/quarantine files, rotate secrets or clean up resources because a disposition recommends it.
- Optional catalog conformance → `/1-skill-linter`; application dependency questions → `/2-dependency-security`; injection boundary assessment → `/2-prompt-injection-defense`. Pass the same candidate and read-only mode; each returns here. `next` is conditional, not an automatic repair pipeline.
- If unexpected execution or exposure is observed, stop the audit action, preserve redacted evidence and return containment recommendations to the owner; `/1-incident-response` can coordinate an explicitly requested response. Do not contact maintainers or upload private packages to scanners without permission.
- Source history and adaptations → [source adaptation](./references/source-adaptation.md). The vendor snapshot is not a second operative procedure.

The archived BagelHole snapshot is a concrete example of why operational documentation needs constraints: its DevOps [vendor map](../0-devops/references/vendor-map.md) records non-executable scripts and remote-installer patterns that must not be promoted as trusted actions.
