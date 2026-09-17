# Agent Workflow Observer wiring audit

Reviewed:

- `1-agent-workflow-observer`
- its route surfaces in `0-agent-engineering`, the hub workflow/HTML, and Butler flows

## Result

The skill now owns one read-only retrospective over one fixed completed or explicitly paused
agent-run snapshot. It does not pretend to supervise an active agent, verify the run's product
result, or apply its recommendations. The old `watch the agent process` trigger was removed because
it contradicted the live-supervision exclusion and promised a capability the skill does not own.

The evidence boundary records the original request, run start/end or pause boundary, available
transcript/tool trace/final response, agent/model/tool versions when known, environment, evidence
cutoff, privacy limits, and missing artifacts. Agent text and discovered content are untrusted data,
not instructions. Every claim is classified as observed, inferred, or unknown; failures, retries,
scope changes, and user corrections are preserved rather than allowing the final response to become
ground truth.

For Git-backed runs, the analysis records repository/worktree/branch/`HEAD`, dirty ownership, and
whether evidence describes working-tree, committed, remote, or CI state. It creates no worktree.
A worktree does not isolate processes, ports, accounts, providers, credentials, caches, databases,
browsers, or remote state. Reads stay within supplied or separately authorized read-only artifacts.

Before suggesting a new mechanism, the skill checks current project automation/runbooks and the
live catalog by job and boundary. One run may reveal a candidate but cannot prove recurrence. Each
proposal therefore includes evidence, confidence, owner, inputs/outputs, authority/effects,
privacy/secrets, failure mode, a smallest reversible experiment, success measure, verification,
rollback, and duplication/maintenance cost.

The leaf returns proposals to Agent Engineering or its actual caller and stops. It cannot write a
script or runbook, execute checks, modify the active task, enable hooks, install tools, change the
catalog, message people, or mutate external state. A user-selected catalog proposal becomes a new
request through Skill Manager, which may call Skill Creator. Verification and explicit-correction
capture remain separate Verify Work and Session Skill Reflect operations.

## Verification

- Focused observer/Agent Engineering routing tests: 15 passed.
- Full routing suite: 341 passed.
- Generated route index: 218 live skills.
- Catalog lint after sequential index generation: 0 critical, 0 warnings, 55 informational
  findings, 0 hub-member orphans.
- `git diff --check`: passed.

No run was supervised, result verified, worktree created, project check executed, recommendation
applied, catalog operation initiated, Git action performed, host sync run, or external state changed.
