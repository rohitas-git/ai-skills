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

Prepare the following report sections; write named documents only when requested in the agreed task-owned location. Preserve prior artifacts and return an in-memory report to a calling review by default.

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
- Suggested remediation direction (not permission to apply a patch, even if trivial)
- Any residual risks or related issues

Keep Low-severity items brief or summarized in the main report unless the user requests full detail.

## Phase 5 — Structured Output

When structured output is requested, emit `findings.json` conforming to [findings-schema.json](./findings-schema.json). Otherwise maintain these fields in the returned findings. Store only redacted, necessary evidence, never secret payloads or raw private records.

Rules:
- Only include findings that survived Phase 3 validation.
- Use exactly one primary category: "security", "logic", "ambiguity" or "bug". Put finer risk labels in subcategory, not unsupported category combinations.
- Include confidence (high / medium / low).
- Include status ("confirmed").
- Provide enough location information for a developer to navigate directly to the issue.
- Reuse only a user-selected prior audit matching this repository/scope; revalidate on the current candidate. Use is_new for prior-audit identity and change_relation for PR causality; those are different questions.

After writing an authorized report, run the local `scripts/validate-findings.js` with its explicit path. It checks the schema's supported structural constraints and report consistency, not exploit validity or date-time format semantics. Report unavailable validation honestly; manual inspection must not be described as a successful validator run.

The helper implements this bundled schema's structural vocabulary, not arbitrary
JSON Schema. Unsupported keywords fail closed. `format` is annotation-only as
allowed by [Draft 2020-12](https://json-schema.org/draft/2020-12/json-schema-validation);
review timestamp provenance separately. Reports lacking newly required evidence
must be revalidated/enriched from source, not silently accepted as current findings.

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
- Remove unsubstantiated findings from the confirmed queue; keep rejected/needs-more-info leads separately and visibly labeled if the user requested that ledger. Do not count them as confirmed in any summary.
- Update findings.json and the human reports accordingly.

Only after this phase is complete should the final set of findings be presented to the user.

## Final Presentation

When delivering results to the user:
- Lead with the executive summary and highest-severity verified findings.
- Provide navigation only to files actually created; otherwise reference report sections.
- Offer to generate remediation patches, deeper analysis of specific findings, or a follow-up focused audit if desired.
- Be transparent about residual risk and any areas that received lighter coverage.

Recheck candidate identity and return to the paused caller. No recursive review,
automatic hardening, issue/comment publication, approval, commit or cleanup follows
from a finding. Fresh reasoning may be local; workers are optional and require an
explicit packet and permission, not an assumption of inherited chat or isolation.
