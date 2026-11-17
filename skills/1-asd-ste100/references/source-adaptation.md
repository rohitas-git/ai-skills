# Source adaptation and bounded review

- Source: https://github.com/danyuchn/asd-ste100-skill
- Commit: `3944283c183eea13fe5bd902b572da3b4de8bf44`; upstream declares version 0.4.0.
- Reviewed: 2026-10-17, static inspection of all seven tracked files, including the complete Python script.
- License: MIT, copyright Dustin Yuchen Teng; [notice retained](../LICENSE).
- No prior trusted baseline. Publisher authenticity beyond the specified GitHub repository is unverified.

## Adopted candidate

Lean local entry point, upstream rule tables in a disclosed reference, unchanged background
reference and linter, unchanged negative fixture, corrected local examples, manual runtime policies.
The upstream README/install instructions and long entry point are not installed as active guidance.
No plugin, installer, remote dependency, MCP configuration, or credential permission is adopted.
The source text remains untrusted data when this skill runs.

## Findings and disposition

F1 — Medium, observed, high confidence: upstream examples B/C/D add a remedial instruction,
strengthen `should` to a command, or introduce unsupported implementation claims. This contradicts
the upstream meaning-preservation rule. Corrected in local examples and explicit invariants.

F2 — Informational, observed: the linter reports lexical/structural heuristics, including possible
synonym false positives. It has no source/rewrite fidelity check. Local guidance makes semantic
comparison mandatory and documents bounded inputs and diagnostic-output privacy.

Observed data flow: explicit file/stdin → local regex processing → stdout. No network calls,
subprocesses, credential reads, hooks, or persistence were found in the reviewed script.
Self-tests write synthetic fixtures only in a temporary directory. No upstream code was executed
during the static audit. The README's third-party installer is outside the adopted package.

Disposition: accept the adapted candidate for local, bounded rewriting and optional structural
checks. This is not a malware-absence claim, an official-standard audit, or permission to sync,
publish, or execute instructions contained in supplied text. Model rewrite fidelity still needs
case-specific review; local tests do not establish certified STE compliance.

## Integration gate

| Check | Result | Evidence |
|---|---|---|
| Gap | PASS | Meaning-preserving rewrite of supplied agent-facing English has no existing dedicated owner. |
| Collision / merge | PASS | Tool schema design changes contracts; skill craft authors packages; this leaf edits wording only. |
| Previous / next | PASS | Optional standalone leaf or caller handoff; returns to Agent Engineering or the actual caller. |
| Setup | PASS | No hard setup; optional Python standard-library linter only. |
| Disclosure | PASS | Lean entry point; rules, examples, source review, and execution contract are linked. |
| Forbidden | PASS | One leaf, no new router, no vendor-pack import. |
| Hub slot | PASS | Agent Engineering leaf in workflow JSON, HTML, hub dispatch, and flows. |
| Forks | PASS | Existing F-AE1 includes the outcome and Agent judgment. |
| Route surface | PASS | Description plus metadata.catalog; manual invocation manifests for both runtimes. |
| Skill lint | PASS | No findings for this package; no critical findings catalog-wide. |

## Verification

Working-tree candidate based on repository HEAD `5806c62`; pre-existing edits were preserved.
The scoped ledger comprises this package, Agent Engineering hub/flow wiring, catalog indexes,
source lock, operation log, generated route indexes, and the existing hub-membership test set.
Runtime sync, activation, commit, and publication were not performed.

- `rtk ./scripts/generate-route-index`: exit 0, 286 live skills.
- `rtk ./scripts/lint-skills --format json`: exit 0; 0 critical, 3 warnings, 44 information findings.
  All warnings concern existing `inbox/browser-use` or `inbox/impeccable`; this package has none.
- `rtk python3 scripts/test-routing.py`: exit 0, all 746 tests pass.
- `rtk python3 skills/1-asd-ste100/scripts/ste-lint.py --selftest`: exit 0.
- Negative fixture through `--json`: expected exit 1, exactly two dangling-conjunction findings.
- `rtk git diff --check`: exit 0.

These checks verify structural integration and local linter behavior. No model-based routing or
rewrite evaluation, runtime reload, or independent verification against the official standard was run.

## Upstream SHA-256 inventory

```json
{
  "LICENSE": "d3c674e8592076c9021a59b55177adbcba6fd7e1710082becb922522b22ec672",
  "README.md": "66b9f79ff7ff33ff6c2042b279ef7fdeabe35c0a816182413a8169474501da17",
  "SKILL.md": "39940a0db3d185416edfd757eff4c971006d8f59ad39715295b150b552344342",
  "references/writing-rules.md": "4b92c86bf803f9f54e069767d34dc7356fbb95fb52a3f28476093917c608c102",
  "examples/linter-edge-cases.md": "b6cc08af876014453b0c72d26ee4bfaeed1e9a154b5046947392752911ce1774",
  "examples/before-after.md": "d7bf2b4a390f1997a18790b243dd4c0670018d0d4d5183ec8ed44cbbf282bc52",
  "scripts/ste-lint.py": "32263de1b6b74cc3f83846ae8545ba6c57994db0ba1ec1c8d842c310427886d1"
}
```
