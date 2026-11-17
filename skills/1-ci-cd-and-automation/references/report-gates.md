# Scanner report gates

Load when implementing or reviewing a scanner-backed quality threshold. Reuse the project's
verified integration first. This guide installs no scanner, hook, dependency, or helper.

Keep three claims separate: the scanner ran successfully, its report covers the intended candidate,
and its findings satisfy the agreed policy. Report generation alone proves none of the other two.

## Contract

1. Pin scanner/version/config, input paths or URL/role/state, exact candidate, severity mapping,
   and accepted exceptions. Use the actual installed tool's documented schema and exit semantics.
2. Preserve scanner failure before evaluating a report. Start with a fresh task-owned output;
   an old JSON file must not survive a failed scan and become evidence for the new candidate.
3. Validate report shape, scanner errors, nonempty intended coverage, and required finding fields.
   Unknown severity/schema, missing or malformed input, and incomplete scans are unavailable checks.
   Empty findings are valid only when a complete scan of the intended scope is established.
4. Apply the project's threshold explicitly. For Semgrep, account for the version/config's legacy
   and current severity labels; for axe, preserve impact levels and inspect incomplete checks.
   Do not silently copy the source helper's fixed high/serious thresholds or reject/accept unfamiliar
   values without explaining what evidence is missing.
5. For a browser scan, verify successful navigation and the expected page, user role, and application
   state. An HTTP URL alone cannot distinguish the intended screen from a login/error page.
6. Keep pass, policy violation, and unavailable distinct. If the integration uses exit codes such as
   0/1/2, ensure CI blocks both violation and unavailable while reporting their different causes.
   Emit rule/location/count evidence without secret values, sensitive page text, or raw report dumps.

## Verification

Exercise the actual required-check invocation, not only a JSON parser:

| Control | Expected result |
|---|---|
| Complete intended scan, no findings | Pass |
| Finding at the agreed blocking threshold | Violation |
| Complete scan with only below-threshold findings | Pass under the agreed policy |
| Tool failure, timeout, or partial/error report | Unavailable; blocks CI |
| Missing, stale, malformed, or unsupported report | Unavailable; blocks CI |
| Empty/wrong target coverage or browser login/error page | Unavailable for the intended claim |

Record candidate, tool/config, controls, results, and untested provider behavior. Synthetic reports
can verify parsing but cannot establish that the real scanner invocation produces those reports.
Return to the caller without enabling or running hosted automation implicitly.

Modified adaptation of Addy Osmani et al., MIT: [source and static review](../../../guidelines/catalog/ingest-addyosmani-2026-11-15.md).
The upstream JavaScript helper is archived as text for provenance; it is not adopted executable code.
