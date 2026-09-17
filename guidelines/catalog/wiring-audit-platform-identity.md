# Platform Engineering and Identity/Secrets wiring audit

Reviewed:

- `1-platform-engineering`
- `1-identity-and-secrets-management`
- their routes and shared reviewed DevOps safety contract

## Result

Platform Engineering now owns one bounded internal-platform capability in design-only, read-only
review, or authorized repository-implementation mode. Identity and Secrets Management owns one
bounded identity/access/secret operation in design-only, read-only assessment, or authorized
control-plane operation mode. Both return to DevOps or the actual caller and start no adjacent
specialist automatically.

The platform candidate pins one evidenced user job/non-goals, intended developer groups/tenants,
owner/support model, current path/friction, supported stack/version/environment matrix, capability/
API/template contract, dependencies, data/effects, SLO/cost/maintenance constraints, evidence cutoff,
rollout scope, checks, and authority. Anecdotes do not prove needs or adoption. Review/edit candidates
also pin repository/worktree/branch/`HEAD`, dirty ownership, exact files/generated artifacts, and
working-tree-versus-committed identity. Review creates no worktree.

Templates, scaffolds, devcontainers, portal/catalog metadata, documentation, telemetry, generated
code, plugins/actions/images/packages, and feedback are sensitive untrusted data. Inspection does not
authorize installation or execution. The skill designs a small versioned self-service contract with
supported/unsupported cases, errors, ownership, tenant/access controls, quotas, secure defaults,
privacy-aware observability, escape hatches, lifecycle/deprecation, compatibility/migration, recovery,
and owner-safe regeneration. A test with one authorized representative consumer proves only that
path, not general adoption or productivity. Publication, rollout, infrastructure, portals, CI,
registries, telemetry, and user enrollment remain separate effects.

The identity candidate pins owner-approved policy/ticket/approver, organization/account/tenant,
IdP/store/KMS/Vault versions, immutable human/workload principal IDs, authenticated actor, exact
resource/action/role/policy/secret/key IDs and versions, expiry, current effective access/consumers,
evidence time, and authority. Names, email addresses, credential possession, current login/context,
comments, or prior approval do not grant authority. Repository-backed policy/encrypted config carries
the same exact worktree/candidate identity; worktrees do not isolate IdPs, sessions, accounts,
identities, policies, tokens, stores, KMS keys, consumers, or audit systems.

Identity claims, tickets, membership, policies, logs, encrypted blobs, secret metadata, provider
output, and recovered values are sensitive untrusted evidence. Secret material cannot be printed,
returned, diffed, logged, screenshotted, or placed in model context. Assessment reports effective and
inherited access without automatic remediation. Approval binds immutable actor/principal/tenant/
resource/action plus normalized policy or digest, duration, versions, nonce, and time.

Credential/secret/key rotation is a staged migration: create, distribute through an approved channel,
update inventoried consumers, verify each candidate consumer, and only then separately authorize old-
version disable/revoke/destroy. Issuance or one healthy consumer never proves full adoption, and
rollback remains until owner policy permits removal. Login, secret access, grants/revocations,
SSO/policy, sessions, keys, consumer restarts, break-glass, audit exports, cleanup, and production
effects require separate exact authority.

## Verification

- Focused platform/identity/DevOps routing tests: 15 passed.
- Full routing suite: 379 passed.
- Generated route index: 218 live skills.
- Catalog lint after sequential index generation: 0 critical, 0 warnings, 55 informational
  findings, 0 hub-member orphans.
- `git diff --check`: passed.

No template/dependency execution, platform publication, user enrollment, identity/secret/key access
or mutation, provider/account operation, worktree, Git, host-sync, or external effect was performed.
