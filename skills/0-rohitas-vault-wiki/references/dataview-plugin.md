# Dataview compatibility note

Dataview is an optional third-party Obsidian plugin. Do not assume it is installed, enabled,
current, or authorized. Do not install/configure it or mutate `.obsidian/` from a Vault task.

When the user explicitly requests a Dataview query:

1. Confirm the installed plugin/version or label syntax as unverified.
2. Pin the requested view, folders/properties, expected result, and performance/privacy limits.
3. Use the active vault property vocabulary; avoid an unbounded whole-vault query by default.
4. Return a proposed query as text unless a separate skill has exact file-write authority.
5. Verify in the user's actual Obsidian environment only when they authorize that interaction;
   do not claim rendering or query correctness from static text alone.

For Obsidian Bases, route `/1-obsidian-bases`. For general Markdown syntax, route
`/1-obsidian-markdown`; for supported CLI execution, route `/1-obsidian-cli`.
