---
name: 1-thinking-red-team
description: >
  For authorized security review of code, auth, or APIs you control, model the attacker, map the attack surface, and report only findings with a reproducible exploit path and verified mitigation.
  Use when: For authorized security review of code, auth, or APIs you control, model the attacker, map the attack surface, and report only findings with a reproducible exploit path and verified mitigation.
  Not for: security audit product path (1-security-auditor); hardening after findings (2-security-and-hardening).
  Hub: /0-thinking. Triggers: thinking red team, red-team.
disable-model-invocation: true
license: MIT
metadata:
  catalog:
    hub: 0-thinking
    role: soft
    when:
      - "For authorized security review of code, auth, or APIs you control, model the attacker, map the attack surface, and re…"
    not_when:
      - "security audit product path → 1-security-auditor"
      - "hardening after findings → 2-security-and-hardening"
      - "No authorization to attack the target"
      - "Speculative \"best practice\" notes without a reproducible exploit path"
    cousins:
      - "1-security-auditor"
      - "2-security-and-hardening"
    triggers:
      - "1-thinking-red-team"
      - "thinking red team"
      - "red team"
    requires_setup: false
  vendor:
    source: tjboudreaux/cc-thinking-skills
    upstream_id: thinking-red-team
    commit: 7b8fece345dfaa11773be7152ccd194589cb5437
---

# Red Team

Adversarial security review of systems you are authorized to assess. Attack before an outsider does, but report only what you can actually break: every finding needs a concrete exploit path and a check that the proposed fix closes it.

## Boundary

| Need | Skill |
|------|--------|
| Mental-model frame / which model? | `/0-thinking` (hub) |
| Red Team (this) | **1-thinking-red-team** (this) |
| security audit product path | `/1-security-auditor` |
| hardening after findings | `/2-security-and-hardening` |
| House routing (which domain) | `/0-butler` |

## When to Use

- Security review of code, authentication, authorization, APIs, data handling, or infrastructure you control and are permitted to probe.
- Pre-launch hardening of systems that handle auth, money, personal data, or privileged actions.
- Checking whether a specific vulnerability class (injection, XSS, IDOR, auth bypass, SSRF, secret exposure, etc.) is present with a real path.
- Validating that a claimed control actually blocks the attack, not only that a scanner is quiet.

## When NOT to Use

- No authorization to attack the target — stop; do not probe systems you do not own or have written leave to test.
- Speculative "best practice" notes without a reproducible exploit path — drop them; they are not findings.
- Plan, strategy, or decision stress-testing — use pre-mortem (how the plan fails) or steel-manning (strongest case against the decision).
- Architecture resilience without a security objective — use systems or pre-mortem.
- Scanner output alone as a report — patterns are leads; red-team requires an exploit path.
- Non-security root-cause or hypothesis localization — use scientific-method or five-whys-plus.

## Process

1. **Confirm authorization and objective.** State target, allowed scope, out-of-scope assets, success condition (e.g., unauthorized data read, privilege escalation), and stop rules. Refuse or narrow if authorization is unclear.
2. **Build the threat model.** Name adversary profiles (anonymous external, authenticated user, privileged insider) and their goals under realistic access. Attacks without an actor and goal are noise.
3. **Map the attack surface.** Enumerate entry points and trust boundaries: public endpoints, auth flows, APIs, uploads, admin surfaces, jobs, webhooks, secrets, and data stores. Note exposure and required privileges.
4. **Trace exploit paths.** For each high-value surface, attempt concrete abuse: input manipulation, authz gaps, token/session misuse, injection, SSRF, IDOR, mass assignment, rate-limit bypass, secret leakage. Record exact steps and observed behavior.
5. **Apply the anti-fabrication gate.** Keep a finding only if you can complete: entry point → ordered steps → realized impact on this code/config. Incomplete paths are dropped, not listed as "informational."
6. **Score severity and attempt defense bypass.** Rate impact and exploitability. For each relevant control (rate limit, validation, session check), try a realistic bypass and record held vs broken.
7. **Prescribe and verify mitigations.** For each kept finding, give a minimal concrete fix and state how to re-test that the path is closed. Prefer fixes that remove the exploit precondition. Stop when in-scope surfaces are covered or authorization/budget ends; zero findings is valid.

## Output

```text
Target/scope: <in | out | goal | authorization>
Threat model: <actors, access, goals>
Attack surface: <entry points + trust boundaries>
Findings (only complete paths):
  - Title | Severity
    Entry: <endpoint/param/file>
    Steps: <1..n>
    Impact: <realized effect>
    Bypass attempts: <control → result>
    Mitigation: <minimal fix>
    Re-test: <how to confirm closed>
Summary: <kept count; dropped speculative count>
```

## Verification

- Falsify any finding missing entry, steps, or realized impact; treat "could be vulnerable" as non-finding.
- Stop when in-scope attack surfaces are exhausted under authorization, or when re-test shows mitigations close the paths.
- Over-application guard: do not pad with best-practice laundry lists; do not use this skill for non-security plan critique; do not attack without authorization.

## Related

Soft under `/0-thinking`. Vendor: `archive/vendor/cc-thinking-skills/skills/thinking-red-team/`.
Route via hub when frame unclear; invoke this leaf when mechanism is known.
