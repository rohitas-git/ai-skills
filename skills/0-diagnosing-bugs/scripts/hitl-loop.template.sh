#!/usr/bin/env bash
# Human-in-the-loop reproduction loop for an already authorized scenario.
# Copy this file into the task's allowed workspace, edit the placeholders below,
# inspect the final script, and run it only after the target/action is agreed.
# The agent runs the script; the user follows prompts in their terminal.
#
# Usage:
#   bash hitl-loop.template.sh
#
# Two helpers:
#   step "<instruction>"          → show instruction, wait for Enter
#   capture VAR "<question>"      → show question, read response into VAR
#
# At the end, captured values are printed as KEY=VALUE. Do not paste credentials,
# tokens, personal data, or unredacted production content into a capture.

set -euo pipefail

step() {
  printf '\n>>> %s\n' "$1"
  read -r -p "    [Enter when done] " _
}

capture() {
  local var="$1" question="$2" answer
  printf '\n>>> %s\n' "$question"
  read -r -p "    > " answer
  printf -v "$var" '%s' "$answer"
}

# --- edit below ---------------------------------------------------------

step "Perform the pre-agreed reproduction step in the authorized environment."

capture REPRODUCED "Did the exact reported symptom occur? (y/n/unknown)"

capture OBSERVATION "Describe the result briefly, with sensitive values redacted:"

# --- edit above ---------------------------------------------------------

printf '\n--- Captured ---\n'
printf 'REPRODUCED=%s\n' "$REPRODUCED"
printf 'OBSERVATION=%s\n' "$OBSERVATION"
