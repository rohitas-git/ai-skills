# Security hardening audit — 2026-09-11

Reviewed: `2-security-and-hardening`. Catalog-wide reconciliation remains pending.

## Sources inspected

Read the main, all ten original reference files including the complete vendor body
and checklist, and the shared DevOps vendor map. Compared actual parent membership
under Security/Code Review/DevOps and their relevant flow/handoff wording. Inspected
the linter's reference algorithm and surrounding call site after it reported false
orphans for the new progressive-disclosure structure.

Used primary technical references linked in the revised guides: OWASP authorization,
CSRF, SSRF, file-upload, HTTP-header and password-storage guidance; MDN CORS; OWASP
LLM taxonomy. No package-manager version snapshot, compliance claim or example code
was accepted as proof of current runtime behavior.

## Workflow and reference corrections

- Separate inspection-only callers from authorized implementation. Carry approved
  finding/feature, exclusions, repository/worktree and actual candidate throughout.
- Reuse the matching workspace; isolate when needed, return after setup, protect
  unrelated edits and shared database/service state. No automatic branch switch,
  stash, remote migration, credential rotation, production operation or cleanup.
- Return to the paused build/repair caller instead of automatically running a new
  review/commit loop. Do not ask again for the exact fix already authorized.
- Consolidated overlapping live checklists. Full vendor body/checklist stay clearly
  historical and reachable through source adaptation, not mandatory runtime inputs.
- Preserved unique source value: provenance of locally supplied input, dependency
  installation boundaries and script review, multi-worker rate-limit concerns,
  data minimization and trusted destructive-path ownership.
- Replaced raw-body updates with a scoped, parameterized mutation illustration and
  explicit field/actor/state constraints; replaced denylist-based public output with
  explicit projection. Illustrations are partial contracts, not full tested endpoints.
- Removed the misleading DNS-precheck-plus-fetch “safe” example; the guide requires
  enforcement on the actual connection/redirects and appropriate local verification.
- Upload guidance no longer equates claimed MIME/extension/magic bytes with safety.
- Cookie/CORS/header/password/rate policies follow the actual use case, not blanket
  settings that could break public assets, login callbacks, camera/microphone or
  required integrations. No unsupported cost/breach-origin numeric claims remain live.
- Replaced raw secret-match logging with private inspection/redacted evidence and
  separated exposure reporting from credential/history operations requiring authority.
- Replaced volatile package-manager default/version matrices with a procedure to
  inspect the actual pinned manager before any authorized installation. No automatic
  script-policy commits, forced audit fixes or unrequested new stores/vendors.
- Privacy/deletion requirements come from approved project policy; no universal
  consent/retention obligations or incidental deletion of backups. Prompt guidance
  distinguishes instruction content from externally enforced permissions.

## Reference-linter repair

The old orphan check considered direct SKILL.md text and basenames only. It warned
about correctly chained sources and could hide an unlinked file behind another file
with the same basename. The replacement follows package-local Markdown links and
explicit backticked file pointers, resolving by full path with cycle protection.
It does not fetch remote URLs, traverse sibling/vendor packages through links,
execute assets, or parse non-Markdown assets as guides. It handles space/title/
anchor paths and skips unreadable or invalid navigation without broadening scope.

This is a targeted linter improvement, not its complete semantic audit. It establishes
reachability, not whether linked content is safe or should be executed.

## Verification and limits

- `python3 scripts/test-routing.py`: 23 passing tests. Four new disposable fixtures
  cover reference chains/cycles and file pointers, duplicate basenames, external and
  symlink escapes, and spaces/titles/non-Markdown assets. Hardening's live links,
  parent identity and historical-source routing are also checked.
- Initial new fixture failures were macOS /var versus /private/var path aliases;
  canonicalized expected fixture roots and reran successfully. No implementation
  behavior was weakened to accept an incorrect traversal.
- Catalog index regenerated: 214 skills. Lint: 0 critical, 0 warnings, 60 info.
- `git diff --check` passed. Source/route scenario review is not an end-to-end agent
  benchmark, application security test, package install or browser rendering test.
- No added runtime dependency, application edits, external mutation, host sync,
  commit, push, merge or production access. Historical source retained, not deleted.

Scenario review covered audit-only handoff, approved auth fix, unrelated PR debt,
dirty/shared worktree, denied and allowed effects, equal-name refs, DNS rebinding,
raw-field output growth, spoofed upload types, public versus credentialed CORS,
multi-instance throttling, exposed credential response and destructive-path races.
