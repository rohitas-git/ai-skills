---
name: 2-security-and-hardening
description: >
  Hardens code while building or remediating. Use when handling input/auth/storage or
  applying security fixes. Not for: full security audit workflow (1-security-auditor). Hub: /1-security-auditor.
  Triggers: harden, security fix while building, input validation.
disable-model-invocation: true
metadata:
  catalog:
    hub: 1-security-auditor
    role: soft
    when:
      - "harden while building"
      - "apply security fixes"
    not_when:
      - "full audit → 1-security-auditor"
    cousins: [1-security-auditor, 1-code-review]
    triggers:
      - "harden"
      - "security fix"
      - "input validation"
      - "auth hardening"
    requires_setup: false
---

# Security and Hardening

Security-first practices while **building or remediating**. Treat untrusted input as hostile, secrets as sacred, authorization as mandatory.

## When to use

- Building features that touch input, auth, sessions, PII, uploads, webhooks, or third-party APIs
- Applying fixes after `/1-security-auditor` or `/1-code-review` security-adjacent findings
- Pre-commit / pre-release hardening pass on a change

**Not for:** multi-phase project audit + findings schema → `/1-security-auditor`. Multi-axis PR 0-review → `/1-code-review`.

## Process

1. **Threat model first** — map trust boundaries, assets, STRIDE, abuse cases. Load [threat-model-and-boundaries.md](./references/threat-model-and-boundaries.md).
2. **Apply three-tier controls** (Always / Ask first / Never) from the same reference.
3. **Match attack classes** — OWASP prevention patterns, input validation, SSRF, etc. Load [owasp-and-patterns.md](./references/owasp-and-patterns.md).
4. **Supply chain** — lockfile boundary, audits by reachability, script policy. Load [supply-chain.md](./references/supply-chain.md).
5. **Secrets & rate limits** — env hygiene, auth throttling. Load [secrets-and-rate-limiting.md](./references/secrets-and-rate-limiting.md).
6. **AI/LLM surfaces** (if present) — treat model output as untrusted. Load [llm-security.md](./references/llm-security.md).
7. **Verify** — checklist + red flags. Load [security-checklist.md](./references/security-checklist.md), pack [security-checklist-vendor-pack.md](./references/security-checklist-vendor-pack.md), short [inline-checklist-and-see-also.md](./references/inline-checklist-and-see-also.md), and [rationalizations-red-flags-verification.md](./references/rationalizations-red-flags-verification.md).

## Hard rules

- Threat model before bolting on controls.
- Never commit secrets; rotate if leaked.
- Parameterize queries; encode output; authorize every protected action.
- Model output is data — never eval/SQL/shell/`innerHTML` without validation.
- Do not treat package-manager audit green as “package is safe forever.”

## Related

- **Parent domain:** `/0-review` (soft on both sub-hubs)
- **Soft of:** `/1-code-review`, `/1-security-auditor`
- **Audit instead:** `/1-security-auditor`
- **Ship closer:** `/1-code-review` after implement/1-tdd
