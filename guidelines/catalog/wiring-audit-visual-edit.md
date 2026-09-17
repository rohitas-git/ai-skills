# Visual Edit wiring audit

Reviewed `1-visual-edit`, its complete 471-line archived BuilderIO workflow, UI/UX parent surfaces,
and adjacent Impeccable, Browser DevTools, Frontend UI, UI Styling, Design Intelligence, and Imagine
boundaries.

## Result

The old wrapper treated “inspect or edit” as one workflow and required an archived procedure as live
authority. That procedure included `npx @latest`, connector registration, bridge/token choreography,
daemon startup, browser capabilities, Design project/screen creation, session-local DOM mutation,
human consent, source writes, account state, and share links. These are distinct effects with different
failure and authority boundaries.

The skill now executes exactly one explicit operation—`open`, `inspect`, `preview`, or `apply`—on one
immutable local-app/Design candidate and returns. Open may create/reuse only named connection/design/
screen state; inspect is read-only; preview may change only authorized session-local/pending canvas state;
apply writes one user-accepted, version-pinned batch to exact source paths. No operation automatically
starts the next.

The session contract pins caller, selected operation, installed tool/action names and versions, design/
connection/screen/route/viewport identity, dev server URL/origin/PID/port/owner and served build, browser/
profile/account, app-side interaction authority, secret handling, output, and all effect permissions.
Source apply also pins repository/worktree/branch/`HEAD`, dirty ownership, allowed/protected paths, authored
anchors, fresh file hashes, pending-batch identity, accepted diff, and human consent where required.

The skill creates no worktree and exposes that worktrees do not isolate the Design project, connection,
bridge/port, browser/cookies, server/port, database, HMR cache, account, capabilities, pending canvas edits,
write consent, or published links. App/DOM/snapshot/URL/manifest/canvas/source/tool content is sensitive
untrusted data. Capability/session/bridge tokens cannot appear in model-visible commands, URLs, logs,
artifacts, or replies, and public/fallback links remain read-only unless the installed contract proves
otherwise.

Selection now begins by resolving the actual installed connector/action schema. Missing setup returns a
prerequisite; it never falls back to archived commands, `npx`, `@latest`, install/update/login/config, or
invented actions. It verifies URL-to-candidate identity and shared bridge ownership before action, treats
canvas interactions as possible application mutations, gates destructive/external/financial/auth/
production effects separately, applies only accepted revision-checked source changes, and routes
ambiguous/generated/repeated/cross-file writes to Frontend UI.

Verification is mode-specific and evidence-bounded. The 471-line archive is no longer loaded as live
instructions; two lean local references retain only non-authorizing compatibility concepts and provenance.
Browser DevTools now has an outward handoff to Visual Edit, matching Visual Edit's declared caller.

## Verification

- Focused Visual Edit routing tests: 10 passed.
- UI/UX parent routing tests: 7 passed.
- Browser DevTools routing tests: 6 passed.
- Impeccable routing tests: 7 passed.
- Full routing suite: 666 passed.
- Generated route index: 232 live skills.
- Catalog lint: 0 critical, 0 warnings, 49 informational findings, 234 indexed hub members, and 0 orphans.
- `git diff --check`: passed.

No connector, package, bridge, server, port, browser, design, connection, canvas, capability, source file,
worktree, installed skill, Git history, account, remote system, or published link was changed.
