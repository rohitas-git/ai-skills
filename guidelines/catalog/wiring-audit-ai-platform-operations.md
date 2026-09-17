# AI Platform Operations wiring audit

Reviewed:

- `1-ai-platform-operations`
- its dispatch and return surfaces in the reviewed `0-devops` hub

## Result

The skill now owns one bounded AI-platform operation in exactly one mode: design-only, read-only
assessment, or authorized operation. Its boundary distinguishes agent/tool design, formal model or
agent quality evaluation, generic container/cloud administration, telemetry design, and active
incident work. It returns to DevOps or the actual caller after the selected operation and starts no
adjacent specialist automatically.

The target identity covers the exact provider/account/project/tenant/region/environment,
endpoint/cluster/registry/index/cache/queue/GPU resources, state and evidence time, users/traffic,
blast radius, SLOs, budget, data classes, allowed checks, and authority. The served candidate pins
model/provider/version or artifact digest, tokenizer/runtime/driver, serving/config version,
prompt/tool/retrieval contract when relevant, dataset/corpus/index snapshot, embedding/reranker
versions, cache namespace/key/TTL policy, and compatibility constraints. Unmatched candidates may
not be compared or rolled between.

Repository-backed configuration carries repository/worktree/branch/`HEAD`, dirty ownership, and
working-tree-versus-committed identity. Assessment creates no worktree, and edits require an
approved matching checkout. Worktrees do not isolate endpoints, accelerators, ports, accounts,
credentials, registries, data/indexes, caches, queues, quotas, spend, or traffic.

Prompts, outputs, retrieved documents, datasets, manifests, logs, traces, metrics, registry
metadata, and provider/tool output are sensitive untrusted data. Provenance, license, consent,
retention, and tenant isolation are checked before ingesting, embedding, training, caching, logging,
or exporting data. Platform configuration, health, capacity, and cost evidence does not establish
model or retrieval quality; a formal quality evaluation remains a separately selected Agent
Evaluation operation with no invented gate.

Downloads/publication, deploy/restart, traffic shifts, autoscaling/GPU/quota changes, cache purge,
corpus ingestion, index rebuild, registry mutation, credential access, and production/customer-data
effects require separate exact authority. The operation defines capacity/concurrency, spend/egress,
success/abort, compatibility, traffic, and recovery controls first. Verification rereads the exact
resource and representative serving path, distinguishes attempted from accepted/converged state,
and states which quality, privacy, isolation, performance, error, and cost claims were actually
tested.

The skill cannot install a runtime or driver, acquire a model/dataset, access customer data, mutate
a platform resource, scale GPUs, shift traffic, deploy, publish, restart, alter production, roll
back, commit, push, or merge without action-specific authority.

## Verification

- Focused AI-platform/DevOps routing tests: 14 passed.
- Full routing suite: 355 passed.
- Generated route index: 218 live skills.
- Catalog lint after sequential index generation: 0 critical, 0 warnings, 55 informational
  findings, 0 hub-member orphans.
- `git diff --check`: passed.

No model/provider, dataset, index, cache, registry, endpoint, GPU, credential, account, network,
deployment, worktree, Git, host-sync, or other external operation was performed.
