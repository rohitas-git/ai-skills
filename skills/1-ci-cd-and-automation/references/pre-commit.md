# Local pre-commit checks

Use when the selected check contract is a local pre-commit hook, including Husky and lint-staged.
This is an adaptation of Matt Pocock's setup-pre-commit workflow, not a new CI/CD owner.

1. Inspect existing hooks, `core.hooksPath`, package scripts, CI checks, formatter configuration,
   workspace layout, package-manager declaration, and lockfile. Preserve existing hooks and
   `prepare` behavior. Honor monorepo boundaries and non-JavaScript repositories.
2. Prefer existing native or installed tooling. For a requested Husky setup, confirm the actual
   installed version and its initialization contract. Add missing development dependencies only
   within package-edit authority. Do not invoke an unpinned remote initializer incidentally.
3. Configure staged-file formatting with the existing formatter. For a Prettier repository,
   `prettier --ignore-unknown --write` can serve supported staged files. Preserve ignore rules
   and existing formatting decisions rather than adding arbitrary new style defaults.
4. Add only real non-interactive typecheck/test commands. If absent, report the omission instead
   of inventing scripts. Keep expensive checks in CI when a full local run is impractical.
   Hooks supplement CI; they cannot enforce a protected-branch required check.
5. Validate shell/config syntax and command resolution. Before running a staged formatter,
   inspect ownership and partial staging: it may modify files, stage fixes, or create a stash.
   Do not use unrelated staged work as a smoke test. Use an isolated synthetic fixture when needed.
6. Return configuration changes, actual checks, skip/failure behavior, remaining gaps, and
   rollback instructions. Never create a commit just to test the hook or bypass hooks with
   `--no-verify`. Installing hooks in global runtime settings is a separate explicit effect.

Source review: [ingest report](../../../guidelines/catalog/ingest-mattpocock-2026-11-12.md).
