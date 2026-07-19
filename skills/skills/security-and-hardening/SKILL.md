---
name: security-and-hardening
description: >
  Hardens code against vulnerabilities while building or remediating. Use when
  handling user input, auth, data storage, external integrations, or after a
  security audit when applying fixes. Not a full audit workflow (use
  /security-auditor). Soft under Review sub-hubs /code-review and /security-auditor.
disable-model-invocation: true
---

# Security and Hardening

Security-first practices while **building or remediating**. Treat untrusted input as hostile, secrets as sacred, authorization as mandatory.

## When to use

- Building features that touch input, auth, sessions, PII, uploads, webhooks, or third-party APIs
- Applying fixes after `/security-auditor` or `/code-review` security-adjacent findings
- Pre-commit / pre-release hardening pass on a change

**Not for:** multi-phase project audit + findings schema → `/security-auditor`. Multi-axis PR review → `/code-review`.

## Process

1. **Threat model first** — map trust boundaries, assets, STRIDE, abuse cases. Load [threat-model-and-boundaries.md](./references/threat-model-and-boundaries.md).
2. **Apply three-tier controls** (Always / Ask first / Never) from the same reference.
3. **Match attack classes** — OWASP prevention patterns, input validation, SSRF, etc. Load [owasp-and-patterns.md](./references/owasp-and-patterns.md).
4. **Supply chain** — lockfile boundary, audits by reachability, script policy. Load [supply-chain.md](./references/supply-chain.md).
5. **Secrets & rate limits** — env hygiene, auth throttling. Load [secrets-and-rate-limiting.md](./references/secrets-and-rate-limiting.md).
6. **AI/LLM surfaces** (if present) — treat model output as untrusted. Load [llm-security.md](./references/llm-security.md).
7. **Verify** — checklist + red flags. Load [security-checklist.md](./references/security-checklist.md), short [inline-checklist-and-see-also.md](./references/inline-checklist-and-see-also.md), and [rationalizations-red-flags-verification.md](./references/rationalizations-red-flags-verification.md).

## Hard rules

- Threat model before bolting on controls.
- Never commit secrets; rotate if leaked.
- Parameterize queries; encode output; authorize every protected action.
- Model output is data — never eval/SQL/shell/`innerHTML` without validation.
- Do not treat package-manager audit green as “package is safe forever.”

## Related

- **Parent domain:** `/review` (soft on both sub-hubs)
- **Soft of:** `/code-review`, `/security-auditor`
- **Audit instead:** `/security-auditor`
- **Ship closer:** `/code-review` after implement/tdd
