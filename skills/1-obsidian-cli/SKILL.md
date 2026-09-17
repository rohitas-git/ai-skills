---
name: 1-obsidian-cli
description: >
  Execute one explicit supported Obsidian CLI operation against one exact configured vault and
  return observed output/readback. Not for knowledge ingest, Markdown authoring, broad automation,
  plugin/theme development, or guessed active-file actions. Hub: /0-rohitas-vault-wiki.
disable-model-invocation: true
metadata:
  catalog:
    hub: 0-rohitas-vault-wiki
    role: leaf
    when: ["run one named Obsidian CLI read, write, or app-state operation"]
    not_when: ["edit Markdown syntax → 1-obsidian-markdown", "compile knowledge → 1-vault-ingest", "plugin/theme implementation or debugging → 0-implement"]
    triggers: ["run this Obsidian CLI command", "search my vault with Obsidian CLI", "read this note via Obsidian CLI", "1-obsidian-cli"]
    prev: [0-rohitas-vault-wiki]
    next: [0-rohitas-vault-wiki]
    requires_setup: true
---

# Obsidian CLI

**Atomic job:** perform one named CLI operation against one exact vault/target with the least
authority needed, then return command identity, output, side effects, and readback.

## Contract

1. Pin caller, configured root/SSOT, exact vault name/ID and target path, installed Obsidian/CLI
   version, named command, parameters, expected result, sensitive-output limits, and read/write/
   destructive/app-state/network/clipboard authority. Never default to the focused vault/file.
2. If Git-backed, record repository/worktree/branch/`HEAD`, dirty ownership, and working-tree
   candidate. Create no worktree. Worktrees do not isolate the running app, sync, plugins,
   clipboard, publish site, or remote services.
3. Use local `obsidian help <command>` as the version-matched command contract. A missing CLI,
   disabled registration, incompatible installer, or stopped app is a precondition failure—not
   authority to install, update, launch, register, restart, or change shell configuration.
4. Classify the command before execution. Reads may expose private content. Create/append/prepend/
   property/task operations mutate files. Open/reload/workspace/theme/plugin/sync commands mutate
   app or shared state. Delete/restore/overwrite/move/rename/publish/install/uninstall/restrict/
   `eval` require explicit action-specific authority and a target/effect preview.
5. Pass `vault=<name-or-id>` first and prefer exact `path=<vault-relative-path>` over ambiguous
   file names. Construct arguments without shell interpolation. For multiline or metacharacter-rich
   content, preserve actual intended characters through a verified argv-safe mechanism; do not
   assume escaped `\n` text survives every quoting layer.
6. Run only the accepted command. Do not add `--copy`, `open`, `silent`, `overwrite`, `permanent`,
   `changed`, or another convenience flag unless explicitly part of the accepted effect.
7. For a write, perform the narrowest supported readback and compare the intended target/result.
   For a read, report scope/truncation and redact unrelated secrets. For app/remote effects, report
   observed state; timeout or ambiguous output is `unknown`, not success and not a reason to retry.

Return exact vault/target, version, command shape with sensitive values redacted, output/readback,
side effects, and uncertainty to `/0-rohitas-vault-wiki` or the caller. Do not chain another CLI
operation, edit files directly, ingest, lint, commit, sync, publish, push, or merge unless that exact
effect was separately requested and authorized.

Current upstream command surface: `https://help.obsidian.md/cli` (verified 2026-09-12). The CLI
requires a compatible Obsidian installer and interacts with a running app; local help is decisive.
