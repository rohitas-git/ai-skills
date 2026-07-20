# Remediation Prioritization Framework

After findings are verified, use this framework to help the user decide what to fix first. Present prioritization clearly in REPORT.md and offer a concise remediation roadmap if requested.

## Primary Scoring Dimensions

For each confirmed finding, consider:

1. **Impact** (what can go wrong)
   - Critical: RCE, full account takeover, mass data breach, complete auth bypass, financial loss at scale.
   - High: Privilege escalation, significant data leak, widespread DoS, bypass of major security control.
   - Medium: Limited data exposure, single-user impact, moderate availability issues, defense-in-depth gaps.
   - Low: Minor information disclosure, hard-to-exploit issues, cosmetic or non-security correctness problems.

2. **Likelihood / Exploitability**
   - High: Easily reachable by unauthenticated or low-privilege attackers, reliable, no special conditions.
   - Medium: Requires authentication, specific configuration, or moderate attacker skill.
   - Low: Requires multiple unlikely conditions, high privileges already, or is theoretical.

3. **Exposure**
   - Internet-facing vs internal-only.
   - Number of users / tenants affected.
   - Presence in critical business flows.

4. **Ease of Remediation**
   - Trivial (config change, one-line fix, library bump).
   - Moderate (localized code change, well-understood pattern).
   - Hard (architectural change, data migration, large refactor).

5. **Compensating Controls Already Present**
   - Strong mitigations reduce effective priority even if the root issue remains.

## Suggested Priority Order (Default)

1. **Critical impact + High exploitability** — fix immediately.
2. **High impact + High/Medium exploitability**, especially if internet-facing.
3. **Critical/High impact that are easy to fix** (quick wins).
4. **Medium impact that enable or amplify other issues** (chained risks).
5. **Supply-chain issues** that affect many downstream components.
6. Everything else, ordered by Impact × Likelihood, then by ease of fix.

## Presentation Guidance

In REPORT.md:
- Group findings into Immediate / Next Sprint / Backlog (or similar time-based buckets).
- For the top 5–10 items, give a one-sentence “why first” rationale.
- Call out any “easy high-impact” wins separately.
- Note dependencies between fixes (e.g., “Fix authz check before exposing new endpoint”).

In findings.json (optional enrichment):
- Add a `priority_score` or `remediation_priority` field if useful (e.g., “P0”, “P1”, “P2”).
- Or keep prioritization only in the human report.

## Additional Advice to Offer the User
- Suggest creating tickets with clear acceptance criteria derived from the finding scenario.
- Recommend regression tests for the fixed paths.
- For systemic issues (many similar findings), propose a broader hardening effort rather than one-off patches.
- Offer to generate concrete patch suggestions for the highest-priority items if the user wants them.

Never present prioritization as absolute truth — it is a reasoned recommendation based on the dimensions above. Invite the user to adjust based on business context.
