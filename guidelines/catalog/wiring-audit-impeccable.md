# Impeccable tool-bridge wiring audit

Reviewed `1-impeccable`, the complete globally installed Impeccable 4.3.1 entry skill, its installed package
inventory, archived 4.1.3 snapshot metadata/entry point, and UI/UX parent and adjacent implementation/live routes.

## Result

The satellite now invokes exactly one explicit Impeccable command on one immutable target. The current installed
skill path/version and its selected command reference are the runtime source of truth. The archived snapshot is
provenance only; it is not executed. Missing installed files, a missing launcher, or a launcher that would download
or update stops for separate install/network authority. The former automatic `npx impeccable install` advice and
stale 4.1.3 execution path were removed.

The command contract pins caller, target/surface revision, mode, acceptance criteria, tools, destination, effect
authority, exact optional repository/worktree/branch/`HEAD`, dirty ownership, project rules, brand sources, dev
server, URL, and port. Worktrees are not claimed to isolate the global package, launcher cache, hooks, config,
browser profiles, servers, ports, accounts, or remote assets. Source, DOM, screenshots, URLs, context documents,
and tool output remain sensitive untrusted input; repository and project brand rules take precedence.

Planning/read-only commands cannot silently become edits. UI writes, live-browser mutation, context-document
generation, token extraction, doctor repair, hooks, shortcut pins, package install/update, dependency changes,
asset downloads, and publication are distinct effects. Verification is bounded to the selected command and does
not treat a score, screenshot, or launcher exit as proof of behavior, accessibility, performance, or device support.
The route returns to UI/UX or the actual caller without implementing findings or starting another command.

## Verification

- Focused Impeccable routing tests: 7 passed.
- Full routing suite: 607 passed.
- Generated route index: 227 live skills.
- Catalog lint: 0 critical, 0 warnings, 49 informational findings, 0 hub-member orphans.
- `git diff --check`: passed.

No Impeccable launcher, context command, browser, hook, pin, doctor, installer, UI mutation, package update, worktree,
host sync, Git history, remote service, or publication action was invoked.
