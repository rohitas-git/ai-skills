# Phases 3–6 — Validation, Reporting, Structured Output, Independent Verification

## Phase 3 — Validation (Adversarial)

For every candidate finding from Phase 2:

1. Attempt to disprove it.
   - Is the scenario actually reachable given the architecture and controls?
   - Are there mitigating controls the hunter missed?
   - Does the claimed impact hold under realistic conditions?
   - Can you construct a counter-example or safer interpretation of the code?

2. Require a concrete, actionable scenario.
   - Reject pure theoretical risks without a plausible path.
   - Reject findings that rely on unrealistic attacker capabilities unless the project context justifies them.

3. Adjust severity and confidence based on the validation outcome.
   - Only promote findings that survive scrutiny.
   - Clearly mark rejected candidates (they can be kept in an internal list for transparency but must not appear in final outputs as confirmed).

4. Prefer fewer high-quality findings over many weak ones.

## Phase 4 — Reporting

Produce two human-readable documents:

### REPORT.md
Structure:
- Executive summary (overall risk posture, number of verified findings by severity, top 3–5 issues).
- Scope of the audit (what was examined, any limitations).
- Prioritized findings list (Critical → High → Medium → Low) with short titles, locations, and one-sentence impact.
- Notable positive observations (strong patterns worth preserving).
- Recommended next steps or remediation priorities.
- Methodology note (phases followed, any deviations).

### FINDINGS-DETAIL.md
For every Medium, High, or Critical finding:
- Full description
- Location(s)
- Detailed scenario / reproduction
- Impact analysis
- Evidence (code references or reasoning)
- Suggested remediation direction (high-level, not a full patch unless trivial)
- Any residual risks or related issues

Keep Low-severity items brief or summarized in the main report unless the user requests full detail.

## Phase 5 — Structured Output

Emit `findings.json` that strictly conforms to `references/findings-schema.json`.

Rules:
- Only include findings that survived Phase 3 validation.
- Use consistent category values: "security", "logic", "ambiguity", "bug", or combinations if needed (prefer primary category).
- Include confidence (high / medium / low).
- Include status ("confirmed").
- Provide enough location information for a developer to navigate directly to the issue.
- If prior findings.json exists, include a note or field indicating which findings are new vs previously known.

After writing the file, validate it against the schema (use the script in scripts/ if available, or manual structural checks).

## Phase 6 — Independent Verification

This phase must use fresh reasoning, ideally as if a new agent is examining the claims without the hunting history.

For every finding in findings.json:
1. Re-read the cited source code and surrounding context.
2. Verify that the location is accurate.
3. Verify that the described scenario is possible.
4. Verify that the claimed impact is realistic.
5. Check for any mitigating factors that were missed.

Actions:
- Keep the finding if it still holds.
- Demote severity or confidence if partially weakened.
- Reject (remove or mark rejected) if the claim does not hold under re-examination.
- Update findings.json and the human reports accordingly.

Only after this phase is complete should the final set of findings be presented to the user.

## Final Presentation

When delivering results to the user:
- Lead with the executive summary and highest-severity verified findings.
- Provide clear navigation to the detailed files.
- Offer to generate remediation patches, deeper analysis of specific findings, or a follow-up focused audit if desired.
- Be transparent about residual risk and any areas that received lighter coverage.
