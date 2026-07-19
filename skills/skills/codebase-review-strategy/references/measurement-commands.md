# Repository Measurement Commands

Use these portable or enhanced commands to gather sizing metrics quickly. Run them via the bash tool or equivalent in your environment.

## Quick Portable Metrics (no external tools required)

```bash
# Approximate number of source files (customize extensions for your languages)
find . -type f \( \
  -name "*.py" -o -name "*.js" -o -name "*.ts" -o -name "*.tsx" -o \
  -name "*.java" -o -name "*.go" -o -name "*.rs" -o -name "*.cpp" -o -name "*.c" -o \
  -name "*.rb" -o -name "*.php" -o -name "*.cs" -o -name "*.swift" -o -name "*.kt" \
\) ! -path "*/node_modules/*" ! -path "*/venv/*" ! -path "*/__pycache__/*" ! -path "*/target/*" ! -path "*/dist/*" ! -path "*/build/*" | wc -l

# Rough total lines in those files
find . -type f \( same extensions as above \) ! -path "*/node_modules/*" ... -exec wc -l {} + | tail -1

# Tracked files via git (good proxy for human-maintained code)
git ls-files | wc -l

# Directory depth and structure snapshot
tree -L 3 --dirsfirst -I 'node_modules|__pycache__|venv|target|dist|build|.git' | head -80

# Recent activity (last 30 days or so)
git log --since="30 days ago" --oneline | wc -l
git log --since="30 days ago" --name-only --pretty=format: | sort | uniq -c | sort -nr | head -20
```

## Enhanced Metrics (if tools available)

```bash
# Install cloc if missing (Debian/Ubuntu example)
# sudo apt-get update && sudo apt-get install -y cloc

cloc --quiet --report-file=cloc-report.txt .   # or without report for stdout
# Then inspect cloc-report.txt for per-language LOC, files, etc.

# Alternative: tokei (faster, similar output)
# cargo install tokei  (or use pre-built)

# Dependency count examples
ls package.json && cat package.json | grep -o '"dependencies"' -A 20 | wc -l   # rough
ls requirements.txt && wc -l requirements.txt
ls go.mod && grep require go.mod | wc -l
```

## Test & Documentation Indicators

```bash
# Test files count
find . -type f \( -name "*_test.*" -o -name "test_*.py" -o -path "*/tests/*" -o -path "*/test/*" \) ! -path "*/node_modules/*" | wc -l

# Documentation files
find . -type f \( -name "README*" -o -name "*.md" -o -name "*.rst" \) ! -path "*/node_modules/*" | wc -l
```

## Monorepo / Workspace Detection

```bash
ls -1 package.json pnpm-workspace.yaml lerna.json nx.json yarn.lock Cargo.toml go.work 2>/dev/null | head -5
# Or count top-level directories that look like packages
ls -d */ 2>/dev/null | wc -l
```

**Tip:** After running metrics, summarize in a small table:
- Source files: X
- Approx source LOC: Y
- Main languages: ...
- Tests present: Yes/No + rough count
- Tier classification: ...

These measurements feed directly into the tier classification table in the main skill.