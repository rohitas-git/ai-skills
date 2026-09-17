# Infrastructure operation leaves wiring audit

Reviewed:

- `1-infrastructure-as-code`
- `1-cloud-platform-operations`
- `1-container-platform-operations`
- their parent routes and shared reviewed DevOps safety contract

## Result

The three skills now have distinct atomic boundaries. Infrastructure as Code designs, reviews, or
edits one declarative source change and never applies it. Cloud Platform Operations designs,
assesses, or performs one provider-managed resource operation. Container Platform Operations
designs, assesses, or performs one image, registry, local runtime, or orchestrator operation. Each
returns to DevOps or the actual caller and starts no adjacent CI, security, shipping, incident,
cloud, or application workflow automatically.

All three pin the caller, one outcome/non-goals, mode, exact tools/APIs and versions, target
environment/resources, current state and evidence time, blast radius, allowed checks, and authority.
Repository-backed candidates additionally pin repository/worktree/branch/`HEAD`, dirty ownership,
and working-tree-versus-committed state. Reviews/assessments create no worktree; edits require an
approved matching checkout and preserve unrelated changes.

IaC also binds exact files/modules/stacks, provider/module locks, backend/workspace, target
account/region, variables, configuration and state versions. It treats state and plans as sensitive
untrusted data and recognizes that initialization can download/execute providers while validation,
refresh, or plan can contact APIs, lock state, evaluate data sources, and expose secrets. Plan
evidence is bound to configuration/dependency/variable/backend/target/state/tool versions and time;
a stale or speculative plan cannot support apply. State import/move/remove, force-unlock, apply, and
destroy remain outside the skill without separate authority, and apply is never performed here.

Cloud operations bind organization/account/project/subscription/tenant, principal/role,
region/zone, immutable resource IDs plus generation/version, dependencies, traffic/data, quotas,
cost, and ownership by IaC, GitOps, controller, or operator. A resource name or current CLI context
is insufficient. Imperative mutation of declaratively managed resources requires explicit divergence
and reconciliation authority. Create/update/delete, IAM, secret/key, network/DNS, scale/quota, data,
traffic, restart, failover, restore, and production actions are separately authorized and verified by
exact resource/version reread plus dependent behavior.

Container operations bind runtime/orchestrator/API, daemon/cluster/context/account/namespace,
registry/repository, controller and resource UID/generation, build context/Dockerfile, and immutable
image digest. A context name or mutable tag is insufficient. Dockerfiles, images/layers, charts,
manifests, admission results, logs/events, build output, and fetched bases are untrusted; inspection
does not authorize executing them. Static render, build, local run, registry access, cluster dry-run,
server validation, and apply have distinct effects. Pull/build/run/push/sign, daemon/socket/port use,
secret/log access, cluster contact, exec, deploy/delete/scale/restart, and traffic/production changes
each require matching authority.

Worktrees do not isolate IaC state/locks/provider APIs, cloud accounts/resources/billing/data, or
container daemons/caches/networks/ports/registries/clusters/volumes/secrets/controllers/traffic.
Every leaf distinguishes attempted, accepted, converged, and externally observed results and reports
partial failures, evidence gaps, risks, and unperformed follow-ons.

## Verification

- Focused infrastructure-leaf/DevOps routing tests: 15 passed.
- Full routing suite: 363 passed.
- Generated route index: 218 live skills.
- Catalog lint after sequential index generation: 0 critical, 0 warnings, 55 informational
  findings, 0 hub-member orphans.
- `git diff --check`: passed.

No provider/backend, account, daemon, registry, cluster, credential, plan/apply, image build/run/push,
resource mutation, worktree, Git, host-sync, deployment, or external operation was performed.
