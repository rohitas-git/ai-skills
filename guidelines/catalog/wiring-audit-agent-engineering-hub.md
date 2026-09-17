# Agent Engineering hub wiring audit

Reviewed:

- `0-agent-engineering`
- `hubs/0-agent-engineering/workflow.json`
- `hubs/0-agent-engineering/hub.html`
- Agent Engineering section in Butler flows
- Butler/manifest/wiki entry surfaces
- all nine child metadata return links (targeted wiring only)

## Result

The hub is now a pure one-operation router. Metadata, dispatch, workflow JSON, HTML, and Butler
flows expose the same nine children, including the previously omitted `1-parallel-agents` metadata
route and missing HTML links. F-AE1 is used only when two outcomes would materially differ; clear
requests route directly without asking users to choose a skill name.

The former pipeline implied every request should progress through intent, tool/MCP design,
oversight, evaluation, observability, workflow observation, and adversarial verification. Those
are now independent operations, not a mandatory lifecycle. The workflow says: route one concern,
run one leaf, and return its exact candidate, evidence, effects, limits, and choices to the caller.

Every handoff preserves caller, system/repository/artifact/environment/version, mode, trust and
untrusted-input boundaries, sensitive-data limits, allowed checks, exclusions, and read/write/
execute/external/destructive authority. Git-backed candidates include repository/worktree/branch/
`HEAD`, dirty ownership, and working-tree versus committed identity. A read-only design/review
needs no new worktree; a writing leaf decides whether isolation is useful. Worktrees do not
isolate model-provider accounts, credentials, MCP processes, queues, sandboxes, telemetry,
browsers, human approval systems, deployments, or shared services.

The hub itself reads no candidate/package/transcript/code, creates no worktree, delegates no
agent, runs no tool/evaluation, edits no file, and performs no install, external call, Git, or
deployment action. Prompts, retrieved content, outputs, traces, packages, and transcripts remain
untrusted data. Assessment/design/edit/runtime/remote modes keep their original authority.

Targeted child metadata changes added the actual Agent Engineering caller and return to all nine
routes. These edits make the parent graph symmetric but do not count as semantic audits of the
still-pending Agent Evaluation, Human in the Loop, MCP Server Building, Workflow Observer, or
Parallel Agents packages. Previously audited shared/security leaves retain their primary homes.

## Verification

- Focused hub/tool-schema/prompt-defense routing tests: 14 passed.
- Full routing suite: 312 passed.
- Generated route index: 218 live skills.
- Catalog lint: 0 critical, 0 warnings, 55 informational findings, 0 hub-member orphans.
- `git diff --check`: passed.

No worktree, agent delegation, evaluation, tool/server execution, package read, external call,
installation, Git action, host sync, or deployment action was performed.
