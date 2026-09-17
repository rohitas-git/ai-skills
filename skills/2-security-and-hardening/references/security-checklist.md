# Security verification checklist

Use only rows relevant to the approved change; record evidence or a coverage limit,
not a blanket “all secure” claim. Follow the parent's candidate/workspace contract.
The checklist complements tests and source inspection; it does not authorize fixes
outside scope or changes to production configuration.

## Candidate and scope

- Caller, approved feature/finding, repository, branch/base and candidate recorded.
- Task-owned committed/staged/unstaged/new files distinguished from unrelated work.
- Changed controls traced to concrete threats; legitimate behavior preserved.
- Required decisions are resolved; no invented policy, vendor or permission grant.

## Identity, authorization and state

- Protected effects enforce authenticated actor, resource/tenant and action policy.
- Public endpoints remain intentionally public; login status alone is not ownership.
- Tests cover allowed access, unauthenticated/unauthorized access, cross-tenant IDs,
  denied fields, missing resources, stale state and relevant concurrent transitions.
- Credential/session validation uses the project's provider and flow, including
  expiry/revocation and appropriate issuer/audience checks where applicable.
- Password code, if owned here, uses a supported adaptive algorithm and parameters
  appropriate to the deployment; use [current storage guidance](https://cheatsheetseries.owasp.org/cheatsheets/Password_Storage_Cheat_Sheet.html),
  not one “salt rounds” number applied to unrelated algorithms.
- Cookie/CSRF/callback behavior is tested; SameSite alone is not a universal CSRF test.

## Input, output and files

- Normalized values satisfy boundary constraints; resource limits precede expensive
  parsing or processing, and update fields are explicitly permitted.
- Queries are parameterized and authorized; public projections select intended fields.
- Output is encoded for its sink; rich HTML uses a maintained, appropriate sanitizer.
- Error paths avoid secret/record leakage and fail safely without swallowing context.
- URL-fetch policy constrains the actual connection and any redirects, with bounded
  time/response size; a separate DNS check followed by ordinary fetch is insufficient.
- Upload tests cover forged type/extension, oversized/hostile content, safe names,
  storage/execution behavior, access checks and deletion/overwrite boundaries.
- Requested destructive paths have trusted ownership and race-safe containment;
  no parent/root fallback or cleanup of another task's data.

Details: [prevention patterns](./owasp-and-patterns.md) and
[privacy/destructive paths](./privacy-and-destructive-paths.md).

## Deployment-facing controls

- Headers, CORS and transport match actual browser/credential use and deployment.
- CSP/framing/Permissions-Policy preserve required integrations, camera/microphone
  and embedding behavior where applicable. HSTS changes have appropriate rollout
  authority; localhost testing does not establish production TLS behavior.
- Rate limits use trusted keys and hold across the actual worker topology; tests
  cover allowed bursts, denied requests and backing-store failures.
- No unrequested runtime store, provider, role, production setting or migration.

## Secrets, dependencies and privacy

- Changed files inspected privately; reports include redacted locations, not raw
  secret matches. Do not claim all Git history is clear from a scoped diff check.
- Templates use placeholders; ignore rules protect real local secrets without
  hiding arbitrary future tool-state artifacts.
- Dependency root/manager/version and scoped lockfile policy verified; scripts
  reviewed before any permitted execution and no automatic fix/approval flags.
- Advisory evidence is comparable and scoped; unknown or deferred risk is explicit.
- Sensitive data minimization, sharing and lifecycle follow approved requirements;
  tests use synthetic local data, not live records or automatic backup deletion.

Details: [secrets/rate limits](./secrets-and-rate-limiting.md) and
[dependency hardening](./supply-chain.md).

## AI surfaces, when changed

- Model input/output provenance is recorded; trusted code authorizes effects.
- Tool arguments are shape-checked and authorized independently; retrieval enforces
  the current principal's document/chunk access.
- Secrets stay out of prompts/logs; legitimate authorized context is minimized.
- Retries, loops, concurrency and consumption are bounded; uncertain writes are
  reconciled rather than blindly replayed.
- Inert adversarial tests exercise relevant direct/indirect/stored/cross-agent paths.

Details: [LLM controls](./llm-security.md).

## Evidence and return

For each relevant control record source, command/test, actual result and candidate.
Reused evidence must still match relevant code/config/environment. An unavailable
check is not a pass. Use /2-verify-work for a requested evidence pass, then return
to the implementation or PR-repair caller with remaining risks and workspace state.
No automatic commit, publication, deployment or cleanup follows.

Taxonomy reference, not a pass/fail gate: the Security Auditor's
[OWASP 2025 guide](../../1-security-auditor/references/owasp-and-secure-coding.md).
Historical 2021 ordering and package-manager snapshots are not current instructions.
