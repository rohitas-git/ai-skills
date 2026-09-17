# Safe Helper Scripts

> Adapted from agentskills.io. House authority and supply-chain rules control execution.

Load only when a skill repeatedly needs deterministic helper behavior.

## Choose

| Evidence | Choice |
|---|---|
| One-off operation | use an existing repository command; do not add a permanent helper |
| Repeated fragile command | add one reviewed, tested script |
| Existing owner fits | reuse or improve it |
| Third-party runner/package required | stop until source, version, network, install, and execution are separately authorized |

## Contract

A bundled helper has:

- one bounded job and explicit input/output paths;
- non-interactive flags or stdin;
- closed/validated inputs and safe path resolution;
- useful stderr, structured/bounded stdout, and meaningful exit codes;
- idempotent behavior where retries are plausible;
- explicit dry-run or recovery for destructive effects;
- pinned dependencies already available in the authorized environment;
- tests for success, invalid input, partial failure, and unsafe paths.

Point to the script with an exact command relative to the skill root. State whether the agent should read or execute it.

## Safety

Never rely on `npx`, `uvx`, `bunx`, remote imports, self-installing dependency blocks, lifecycle hooks, or package-manager auto-install as an implicit convenience. They download or execute code and require separate authority plus a fixed-source review.

Do not embed secrets in argv, logs, examples, or fixtures. A worktree isolates files, not package caches, credentials, global runtimes, or network effects.

## Completion

Record script revision, runtime/dependency versions, command, exit status, output truncation, and verification result. The script is an implementation aid, not proof of semantic correctness.

