# UI Styling wiring audit

Reviewed `1-ui-styling`, all nine live Markdown references, the imported font inventory, both helper
implementations, both helper test suites and historical coverage artifact, UI/UX and Ship parent
surfaces, and adjacent Frontend UI, Design Intelligence, Design System, Brand, Design, and browser-test
boundaries.

## Result

The skill now owns one immutable presentation-only visual delta on one existing UI surface. It pins the
actual caller; before-state and requested visual result; protected behavior, semantics, content,
analytics, data, and public contracts; approved brand/tokens/components; supported viewport/input/theme/
browser matrix; exact repository/worktree/branch/`HEAD`; dirty ownership; candidate state; and effect
authority. Advice and read-only assessment create no worktree, while authorized edits reuse the caller's
matching worktree and return there.

Worktree isolation no longer implies isolation of package caches, binaries, fonts, browser profiles,
servers, ports, databases, generated assets, CDNs, design tools, accounts, or deployed UI. Source,
styles, configs, DOM, screenshots, design files, copy, URLs, package output, and embedded prompts are
sensitive untrusted data. Repository rules and installed versions outrank vendor examples, and KiloCare
`docs/brand.md` remains authoritative.

The implementation loop freezes a visual-delta/protected-contract ledger, detects the actual installed
stack, uses the smallest repository-native presentation change, preserves DOM meaning/order and runtime
contracts, and verifies the current candidate with repository and optional owned runtime evidence.
Screenshots, typechecks, helper exits, and automated accessibility scans are bounded evidence rather than
proof of visual correctness, behavior preservation, or conformance.

Library initialization, package installation/update, component-registry copying, config replacement,
font/asset installation, token-system design, interaction/semantic changes, visual-direction choices,
artwork, browser testing, Git, and publication are separate effects. The skill never runs the imported
`npx` shadcn installer or Tailwind config generator. Ship now links presentation-only work directly and
symmetrically; Frontend UI retains behavior/semantics/setup ownership, and UI/UX remains the visual-domain
parent. Every handoff preserves candidate/worktree/authority and none starts automatically.

The 331-line mixed guide was replaced by 44 compatibility lines. A reference index keeps every imported
guide reachable while labeling it version-sensitive and non-authorizing. Canvas/font assets and the old
coverage report are explicitly non-operative. The 660 lines of pytest-bound helper tests became 181 lines
of dependency-free `unittest` coverage aligned with the helper's current pinned behavior.

## Verification

- Focused UI Styling routing tests: 9 passed.
- UI/UX parent routing tests: 7 passed.
- Ship parent routing tests: 6 passed.
- Compatibility-helper regression tests: 16 passed without third-party Python packages.
- Full routing suite: 647 passed.
- Generated route index: 230 live skills.
- Catalog lint: 0 critical, 0 warnings, 49 informational findings, 232 indexed hub members, and 0 orphans.
- `git diff --check`: passed.

No product UI, package, lockfile, font, asset, browser, server, worktree, installed skill, Git history,
remote system, or published destination was changed.
