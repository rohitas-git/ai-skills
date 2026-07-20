# Git Hooks Setup for Documentation Governance

Git hooks provide local enforcement so that documentation obligations are met before code is committed.

## Recommended Pre-Commit Hook

Create or update `.git/hooks/pre-commit` (or use the tracked version in `scripts/git-hooks/pre-commit`):

```bash
#!/bin/sh
set -eu

repo_root="$(git rev-parse --show-toplevel)"
cd "$repo_root"

echo "pre-commit: running documentation governance check"
npm run docs:check || {
  echo "Documentation check failed. Please update the required living docs or adjust the trigger map."
  exit 1
}
```

Make it executable: `chmod +x .git/hooks/pre-commit`

## Installation Script (Generic)

A simple installer (`scripts/install-git-hooks.sh` or equivalent):

```bash
#!/bin/sh
set -eu

repo_root="$(git rev-parse --show-toplevel)"
hooks_dir="$repo_root/.git/hooks"
source_hook="$repo_root/scripts/git-hooks/pre-commit"
target_hook="$hooks_dir/pre-commit"

if [ ! -f "$source_hook" ]; then
  echo "install-git-hooks: missing $source_hook — using inline hook instead" >&2
  # Fallback: create a basic one that calls your docs check command
  cat > "$target_hook" << 'EOF'
#!/bin/sh
set -eu
cd "$(git rev-parse --show-toplevel)"
echo "pre-commit: running documentation check"
npm run docs:check || exit 1
EOF
else
  mkdir -p "$hooks_dir"
  cp "$source_hook" "$target_hook"
fi

chmod +x "$target_hook"
echo "install-git-hooks: pre-commit hook installed (local to this clone)"
```

Run it once per clone: `bash scripts/install-git-hooks.sh`

## CI Integration (Generic)

Add to your CI pipeline (GitHub Actions example):

```yaml
- name: Documentation Governance Check
  run: npm run docs:check
  env:
    DOCS_CHECK_BASE: origin/${{ github.base_ref || 'main' }}
```

Or use a Makefile target:

```makefile
docs-check:
	npm run docs:check || (echo "Update living docs for changed code paths" && exit 1)
```

## Best Practices

- Keep the hook **local** (in `.git/hooks`) — never commit the installed hook itself.
- Use `[docs-skip]` in commit messages or `DOCS_CHECK_SKIP=1` only for intentional, well-reasoned exceptions.
- Combine with other hooks (lint, tests) but run docs check early.
- For monorepos: Scope the check to the relevant package or add path filters.
- If no Node/npm: Implement the checker in your primary language (Python, Go, shell + git + grep/glob) or use a lightweight Make/Python script that performs the same glob + diff logic.

## When to Introduce Hooks

- Early in a project: Low friction, prevents drift from day one.
- Existing projects: Start with the check in CI only, then add local hook after the team is comfortable with the trigger map.

The governor skill can help you design the initial `doc-triggers.json` and the check command for your stack.