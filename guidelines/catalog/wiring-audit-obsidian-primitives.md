# Obsidian primitive wiring audit

Reviewed complete operative packages:

- `1-obsidian-markdown` and its three syntax references
- `1-obsidian-cli`
- `1-obsidian-bases` and its two Bases references

## Result

Obsidian Markdown now changes one exact `.md` syntax hunk. It resolves the configured root and
optional Git repository/worktree/branch/`HEAD`/dirty candidate, preserves active schemas and
unknown plugin syntax, and does not add default properties/links/tags/embeds. Notes and supplied
text are private untrusted data; links, embeds, URLs, attachments, and code are not followed.
Static/literal checks are separated from unobserved app rendering.

Obsidian CLI now executes one named operation against an exact vault and target. This matters
because the [current official CLI](https://help.obsidian.md/cli) can otherwise use the vault from
the terminal's directory or the active vault, and file-taking commands can otherwise default to
the active file. The skill uses local version-matched help, classifies read/file/app/remote effects,
passes the vault explicitly first, prefers exact paths, protects multiline/metacharacter arguments,
adds no convenience flags, and requires targeted readback. Overwrite/delete/restore/move/rename,
publish, plugin/theme/sync changes, clipboard effects, and `eval` keep explicit action authority.
Plugin/theme implementation/debugging returns to the implementation domain instead of remaining a
second hidden CLI job. Missing prerequisites do not authorize installation, registration, launch,
restart, or shell edits. Official documentation currently notes the CLI requires a compatible
Obsidian installer and interacts with a running app; local installed help/runtime is decisive.

Obsidian Bases now edits one exact `.base` candidate or named view. The [official Bases syntax](https://help.obsidian.md/bases/syntax)
defines `.base` files as YAML with views, filters, and formulas, but the skill treats every detailed
function/view rule as version-sensitive. It minimizes the query population, preserves unknown
fields, changes no source notes, installs no plugin, validates only the exact candidate, and makes
runtime CLI verification a separate authorized operation. The former 498-line guide and 173-line
function table were reduced to a minimal procedure plus a non-exhaustive version note.

All three require configured-root setup, create no worktree, and explicitly state that worktrees
do not isolate the Obsidian app, sync, plugins, accounts, clipboard, publication, or remote state.
Parent dispatch and metadata now describe the same atomic objects and returns.

## Verification

- Focused primitive/parent routing and contract tests: 16 passed.
- Full routing suite: 304 passed.
- Generated route index: 218 live skills.
- Catalog lint: 0 critical, 0 warnings, 55 informational findings, 0 hub-member orphans.
- `git diff --check`: passed.

No vault/app/CLI operation, worktree action, installation, plugin/sync action, Git action, host
sync, publication, or external write was performed. Official Obsidian documentation was read-only.
