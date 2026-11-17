---
name: 1-manual-procedure-wizard
description: >
  Author an interactive Bash wizard for a human-only manual procedure. Use when
  dashboard setup, credential entry, or a manual transition needs a repeatable guided script.
  Not for steps the agent can perform directly, executing the procedure, or applying migrations.
  Hub: /0-devops.
disable-model-invocation: true
license: MIT
metadata:
  catalog:
    hub: 0-devops
    role: leaf
    when: [author a guided script for human-only setup or manual operations]
    not_when: ["perform an operational action → 0-devops", "implement ordinary code → 0-implement"]
    prev: [0-devops]
    next: [0-devops]
    triggers: [manual setup wizard, interactive Bash wizard, guided dashboard procedure]
    requires_setup: false
  vendor:
    source: mattpocock/skills
    upstream_id: wizard
    commit: 5863806dd4e15c63174bee4e7515a4256792ecfa
---

# Manual Procedure Wizard

Author one script for the human to run. Authoring does not execute its procedure.

## Boundary

| Need | Owner |
|---|---|
| A script guiding a human through manual steps | This skill |
| Direct infrastructure, account, deployment, or migration work | `/0-devops` |
| CI/CD workflow rather than a human procedure | `/1-ci-cd-and-automation` |

## Process

1. Pin repository/worktree/branch/HEAD, dirty ownership, procedure, current/target state,
   allowed output path, and human-only steps. Read examples, configuration keys, and workflow
   references before asking. Avoid reading real secret values when names are sufficient.
2. Map stages in dependency order. For each stage record the human action, value source,
   secret/public classification, exact destination, scope/account, and reversible/irreversible effect.
   Present the concrete stage map. Resolve material choices before authoring dependent stages.
3. Verify dashboard journeys and commands against current official documentation when needed.
   Mark unknown UI paths instead of inventing clicks. Use one focused task per stage.
4. Read [authoring constraints](references/authoring.md). Create a local script at the agreed path.
   Use stage progress, explicit prompts, default-no confirmation, hidden secret entry,
   failure handling, and an accurate completion summary. Preserve existing files.
5. Inspect the generated script statically. Run `rtk bash -n <script>` and an installed shell
   linter when available. Trace every input to its destination, failure path, and output.
   Add a focused non-interactive check for any custom parsing or persistence logic using synthetic data.
6. Return the path, exact human-run command, checks performed, untested behavior, prerequisites,
   and remote/irreversible effects the human will encounter. Keep the script by default.

Do not run the wizard end to end, open dashboards, collect credentials in chat, write hosted
secrets, delete the artifact, commit, or publish as part of authoring.
The upstream template is archived evidence, not an approved executable library.
Source review: [ingest report](../../guidelines/catalog/ingest-mattpocock-2026-11-12.md).
