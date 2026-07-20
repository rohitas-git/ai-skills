#!/usr/bin/env bash
# Interactive setup for symlinking AI-Skills catalog to agent directories.
# Run from anywhere: detects existing clone, asks questions, writes config, symlinks skills.

set -euo pipefail

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
BLUE='\033[0;34m'
CYAN='\033[0;36m'
YELLOW='\033[1;33m'
DIM='\033[2m'
NC='\033[0m' # No Color

log() { echo -e "${BLUE}→${NC} $*"; }
ok() { echo -e "${GREEN}✓${NC} $*"; }
warn() { echo -e "${YELLOW}⚠${NC} $*"; }
err() { echo -e "${RED}✗${NC} $*" >&2; }

# Detect repo root or prepare to clone
detect_or_clone_repo() {
  # If we're in a subdirectory of the repo, find the root
  if [[ -f "skills/CLAUDE.md" ]]; then
    REPO_ROOT="$(cd . && pwd)"
    ok "Using current repo: $REPO_ROOT"
    return 0
  fi

  # Check if we're already inside the repo
  current_script_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
  if [[ -f "${current_script_dir}/../skills/CLAUDE.md" ]]; then
    REPO_ROOT="$(cd "${current_script_dir}/.." && pwd)"
    ok "Using repo root: $REPO_ROOT"
    return 0
  fi

  # Not in repo; ask user
  log "AI-Skills repo not detected in current directory."
  read -p "Path to existing clone (or blank to clone a new one): " user_path

  if [[ -n "$user_path" ]]; then
    user_path="$(cd "$user_path" 2>/dev/null && pwd)" || { err "Path not found: $user_path"; return 1; }
    if [[ ! -f "$user_path/skills/CLAUDE.md" ]]; then
      err "Not a valid AI-Skills repo (missing skills/CLAUDE.md)"
      return 1
    fi
    REPO_ROOT="$user_path"
    ok "Using repo: $REPO_ROOT"
  else
    # Clone
    default_dir="./ai-skills"
    read -p "Clone destination (default: $default_dir): " clone_dir
    clone_dir="${clone_dir:-$default_dir}"

    if [[ -e "$clone_dir" ]]; then
      err "Directory already exists: $clone_dir"
      return 1
    fi

    log "Cloning https://github.com/rohitas-git/ai-skills.git → $clone_dir"
    git clone https://github.com/rohitas-git/ai-skills.git "$clone_dir" || { err "Clone failed"; return 1; }
    REPO_ROOT="$(cd "$clone_dir" && pwd)"
    ok "Cloned to: $REPO_ROOT"
  fi
}

# Discover skills in repo
discover_skills() {
  local skills_dir="$REPO_ROOT/skills/skills"
  local inbox_dir="$REPO_ROOT/skills/inbox"
  local all_skills=()

  if [[ -d "$skills_dir" ]]; then
    while IFS= read -r -d '' skill; do
      skill=$(basename "$skill")
      all_skills+=("$skill")
    done < <(find "$skills_dir" -maxdepth 1 -type d -name '*' ! -name '.' -exec test -f "{}/SKILL.md" \; -print0 2>/dev/null)
  fi

  if [[ -d "$inbox_dir" ]]; then
    while IFS= read -r -d '' skill; do
      skill=$(basename "$skill")
      all_skills+=("$skill")
    done < <(find "$inbox_dir" -maxdepth 1 -type d -name '*' ! -name '.' -exec test -f "{}/SKILL.md" \; -print0 2>/dev/null)
  fi

  # Sort and deduplicate
  all_skills=($(printf '%s\n' "${all_skills[@]}" | sort -u))

  # Return array (bash limitation: use global)
  DISCOVERED_SKILLS=("${all_skills[@]}")
}

# Prompt for skill selection
select_skills() {
  log "Skill selection"

  discover_skills
  local count=${#DISCOVERED_SKILLS[@]}
  echo "Found $count skills."
  echo ""

  read -p "Install all skills? [Y/n]: " choice
  choice="${choice:-y}"

  if [[ "$choice" =~ ^[Yy]$ ]]; then
    SELECTED_SKILLS=()  # empty = include all
    ok "Selected: all skills"
  else
    # Show numbered list and let user choose
    for i in "${!DISCOVERED_SKILLS[@]}"; do
      echo "  $((i+1))) ${DISCOVERED_SKILLS[$i]}"
    done
    echo ""
    read -p "Enter skill numbers (comma-separated, e.g. 1,3,5) or 'all': " indices

    if [[ "$indices" == "all" ]]; then
      SELECTED_SKILLS=()
      ok "Selected: all skills"
    else
      SELECTED_SKILLS=()
      for idx in $(echo "$indices" | tr ',' '\n' | tr -d ' '); do
        if [[ "$idx" =~ ^[0-9]+$ ]] && (( idx >= 1 && idx <= count )); then
          SELECTED_SKILLS+=("${DISCOVERED_SKILLS[$((idx-1))]}")
        else
          warn "Skipped invalid index: $idx"
        fi
      done

      if [[ ${#SELECTED_SKILLS[@]} -eq 0 ]]; then
        err "No skills selected"
        return 1
      fi

      ok "Selected ${#SELECTED_SKILLS[@]} skill(s): ${SELECTED_SKILLS[*]}"
    fi
  fi
}

# Default targets (from existing symlink-targets.json)
declare -a DEFAULT_TARGETS=(
  "~/.agents/skills"
  "~/.claude/skills"
  "~/.codex/skills"
  "~/.cursor/skills"
  "~/.gemini/antigravity/skills"
  "~/.gemini/config/skills"
  "~/.gemini/skills"
  "~/.grok/skills"
  "~/.kiro/skills"
  "~/.zcode/skills"
)

# Prompt for target selection
select_targets() {
  log "Target agent directories"
  echo ""
  echo "Known targets (all preselected):"

  SELECTED_TARGETS=()
  for i in "${!DEFAULT_TARGETS[@]}"; do
    echo "  $((i+1))) ${DEFAULT_TARGETS[$i]}"
    SELECTED_TARGETS+=("${DEFAULT_TARGETS[$i]}")
  done

  echo ""
  while true; do
    read -p "Deselect targets by number (comma-separated, leave blank to keep all): " deselect

    if [[ -n "$deselect" ]]; then
      # Parse comma-separated indices into an associative set
      local deselect_set=()
      local has_invalid=0
      for idx in $(echo "$deselect" | tr ',' '\n' | tr -d ' '); do
        if [[ "$idx" =~ ^[0-9]+$ ]]; then
          if (( idx >= 1 && idx <= ${#SELECTED_TARGETS[@]} )); then
            deselect_set+=("$idx")
          else
            has_invalid=1
          fi
        else
          has_invalid=1
        fi
      done

      if [[ $has_invalid -eq 1 ]]; then
        warn "Invalid indices (valid: 1-${#SELECTED_TARGETS[@]}), try again"
        continue
      fi

      # Build new targets array, skipping deselected indices
      local new_targets=()
      for i in "${!SELECTED_TARGETS[@]}"; do
        local skip=0
        for idx in "${deselect_set[@]}"; do
          if (( idx == i+1 )); then
            skip=1
            break
          fi
        done
        if [[ $skip -eq 0 ]]; then
          new_targets+=("${SELECTED_TARGETS[$i]}")
        fi
      done

      if [[ ${#new_targets[@]} -eq 0 ]]; then
        warn "All targets deselected; nothing left to do"
        continue
      fi

      SELECTED_TARGETS=("${new_targets[@]}")
    fi
    break
  done

  echo ""
  read -p "Add custom target? (leave blank for no): " custom
  if [[ -n "$custom" ]]; then
    custom="${custom/#\~/$HOME}"
    SELECTED_TARGETS+=("$custom")
  fi

  if [[ ${#SELECTED_TARGETS[@]} -eq 0 ]]; then
    err "No targets selected"
    return 1
  fi

  ok "Selected ${#SELECTED_TARGETS[@]} target(s)"
  for target in "${SELECTED_TARGETS[@]}"; do
    echo "    → $(echo "$target" | sed "s|^$HOME|~|")"
  done
}

# Generate config JSON
write_config() {
  local config_file="$REPO_ROOT/scripts/symlink-targets.local.json"
  local include_json=""

  if [[ ${#SELECTED_SKILLS[@]} -gt 0 ]]; then
    # Build include array
    include_json='  "include": ['
    for i in "${!SELECTED_SKILLS[@]}"; do
      include_json+=$'\n    "'"${SELECTED_SKILLS[$i]}"'"'
      if [[ $((i+1)) -lt ${#SELECTED_SKILLS[@]} ]]; then
        include_json+=","
      fi
    done
    include_json+=$'\n  ],'
  fi

  # Build targets array
  local targets_json='  "targets": ['
  for i in "${!SELECTED_TARGETS[@]}"; do
    targets_json+=$'\n    "'"${SELECTED_TARGETS[$i]}"'"'
    if [[ $((i+1)) -lt ${#SELECTED_TARGETS[@]} ]]; then
      targets_json+=","
    fi
  done
  targets_json+=$'\n  ]'

  cat > "$config_file" <<EOF
{
  "source": "$REPO_ROOT/skills",
  "discoverPackages": ["skills", "inbox"],
  "neverDiscover": ["archive", "hubs", "guidelines", "wikis", "vendor", ".scratch", ".system", ".claude"],
  "nestedSkillRoots": [],
  "ingestDestination": "inbox",
$include_json$targets_json
}
EOF

  ok "Config written to: $config_file"
}

# Run sync with dry-run preview
preview_sync() {
  log "Preview (dry-run)"
  echo ""
  bash "$REPO_ROOT/scripts/sync-skills-symlinks.sh" \
    --config "$REPO_ROOT/scripts/symlink-targets.local.json" \
    --dry-run --verbose
}

# Ask for confirmation and run actual sync
confirm_and_sync() {
  echo ""
  read -p "Proceed with symlinking? [y/N]: " confirm
  confirm="${confirm:-n}"

  if [[ "$confirm" =~ ^[Yy]$ ]]; then
    log "Running symlink sync..."
    bash "$REPO_ROOT/scripts/sync-skills-symlinks.sh" \
      --config "$REPO_ROOT/scripts/symlink-targets.local.json"
    ok "Done!"
  else
    warn "Cancelled. No changes made."
  fi
}

# Print closing instructions
print_closing_note() {
  echo ""
  echo -e "${CYAN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
  echo -e "${CYAN}Setup Complete${NC}"
  echo -e "${CYAN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
  echo ""
  echo "To reconfigure your setup in the future, run:"
  echo -e "  ${DIM}cd $REPO_ROOT && ./scripts/setup.sh${NC}"
  echo ""
  echo "To resync skills (e.g., from a git hook), run:"
  echo -e "  ${DIM}./scripts/sync-skills-symlinks.sh --config ./scripts/symlink-targets.local.json${NC}"
  echo ""
}

# Main flow
main() {
  echo ""
  echo -e "${BLUE}AI-Skills Setup${NC}"
  echo ""

  detect_or_clone_repo || { err "Failed to detect/clone repo"; return 1; }
  echo ""

  select_skills || { err "Skill selection failed"; return 1; }
  echo ""

  select_targets || { err "Target selection failed"; return 1; }
  echo ""

  write_config
  echo ""

  preview_sync
  echo ""

  confirm_and_sync
  print_closing_note
}

main "$@"
