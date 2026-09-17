# Differential / PR-Focused Audit Guidance

Use this when the user requests a review of changed files only, a pull request, a commit range, or a differential audit. The goal is high signal on the delta while still catching issues that the change introduces or exposes.

## Scope Rules
- Primary focus: the changed files and the new/modified code paths.
- Always perform a lightweight recon of the surrounding context (callers, callees, shared utilities, configuration that the change touches).
- Apply [the shared candidate contract](../../0-review/references/review-candidate.md) before any phase. Preserve the caller, exact candidate, comparison semantics, scope and read-only authority, including dirty-state ownership for current-work reviews.
- Do **not** re-audit the entire unchanged codebase unless the user explicitly expands scope. High risk changes inspection depth along relevant paths, not the authorization boundary.
- Load prior findings only when explicitly supplied/selected and verified to concern this repository and audit scope. Revalidate them on this candidate; an unrelated findings.json is not an audit baseline.

## Adapted Workflow

### Phase 1 — Lightweight Recon
- Identify the exact diff (git show, git diff, PR files).
- Map how the changed code fits into the existing architecture (who calls it, what it calls, data it touches).
- Note any new entry points, new dependencies, new configuration, or new trust boundaries introduced by the change.
- Flag high-risk change patterns early: auth logic, crypto, input handling, concurrency, deserialization, new external calls, permission changes.

### Phase 2 — Focused Hunting
- Apply the relevant attack classes **to the changed code and its immediate interactions**.
- Pay special attention to:
  - New or modified authorization checks (or missing ones).
  - Changes in input validation or sanitization.
  - New uses of dangerous APIs.
  - Concurrency changes (new shared state, removed locks, etc.).
  - Dependency additions or version bumps.
  - Error-handling changes that might leak information or fail open.
  - Ambiguities introduced by the change (unclear contracts, inconsistent naming with existing code).
- For each candidate, ask: “Does this issue exist because of the PR, or was it pre-existing and merely touched?”

### Phase 3–6
- Validation and independent verification remain mandatory and just as strict.
- In reporting, clearly separate:
  - Issues **introduced** by the PR.
  - Pre-existing issues that the PR happens to touch or that become more severe because of the PR.
  - Issues the PR appears to **fix**.
- Prefer findings that a human reviewer of this PR would care about right now.
- Retain the six phases' reasoning, validation and independent factual checks without automatically emitting their full-audit artifacts. Return an in-memory ledger to a combined-review caller; serialize/schema-validate only when that output was requested. Use fresh reasoning locally when delegation is unavailable or not permitted.

## Special Considerations
- **Security-sensitive PRs** (auth, crypto, payments, admin, data deletion): raise effort and consider a slightly broader context scan.
- **Large refactors**: focus on whether security properties were preserved; look for accidental removal of checks.
- **Dependency-only changes**: apply the supply-chain guidance heavily.
- **Test-only changes**: still check that tests do not introduce new attack surface (e.g., test helpers left in production paths) and that security-relevant behavior is actually tested.
- **Documentation / config-only changes**: look for secrets, insecure defaults, or policy weakenings.

## Output Adjustments
- Title the report clearly as a differential / PR audit.
- Include the commit range or PR identifier in audit_metadata.
- In findings, mark whether each issue is “introduced”, “pre-existing”, or “fixed-by-this-change”.
- Keep the report concise — reviewers of PRs have limited attention.
- Default to chat/caller output, not architecture.md, REPORT.md or findings.json files. If files are requested, use an agreed task-owned location and preserve existing artifacts.
- Distinguish introduced/worsened findings from unchanged pre-existing issues, fixed issues, rejected leads and unverified coverage. A pre-existing weakness newly exposed by the PR needs causal evidence to count as a PR finding.
- Recheck candidate identity before reporting. Return to the calling complete-review/repair workflow; do not initiate hardening, another full review, publication, approval, commit or cleanup.

## When to Recommend Expanding Scope
- The change touches a central security control and the surrounding code looks risky.
- Multiple related findings suggest a systemic problem beyond the diff.
- The PR is very large or touches many modules (consider splitting or doing a full audit later).

Always respect the user’s declared scope while giving them a clear signal if the differential 0-review has important blind spots.
