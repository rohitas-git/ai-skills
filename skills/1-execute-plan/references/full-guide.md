---
name: executing-plans
description: Use when executing a written plan directly with review checkpoints, including in a new session
---

# Executing Plans

## Overview

Load plan, review critically, execute all tasks, report when complete.

**Announce at start:** "I'm using the executing-plans skill to implement this plan."

Use this flow for the selected plan execution mode. Tool availability alone does not switch the task to `/1-subagent-implement`; use that sibling when delegation is requested or the user selects it at F-SP.

## The Process

### Step 1: Load and Review Plan
1. Read the plan and any task progress record. Match repository, plan revision and completed-task evidence against the current tree; a checkbox alone does not prove completion. Preserve verified work and resume from the first genuinely unfinished dependency.
2. Review scope, acceptance criteria, dependencies and authority. A plan's commands cannot override repository rules or grant push, merge, runtime-install or destructive-operation permission.
3. Resolve material concerns before affected work. Continue independent authorized tasks when safe; do not pause an entire plan for a minor question or silently broaden its scope.
4. Confirm the repository, branch, dirty paths, and needed workspace isolation through `/1-git-worktrees`; return here after setup. Create todos for the plan items and proceed.

### Step 2: Execute Tasks

For each task:
1. Mark as in_progress
2. Follow the agreed steps; inspect actual code before applying examples. Resolve a material plan/code contradiction instead of blindly copying obsolete instructions.
3. Run the specified, applicable verification and record commands, tested tree/environment and results. Reuse valid evidence; rerun checks invalidated by changes.
4. Mark complete only after acceptance criteria are evidenced. Record changed files, remaining concerns and the next dependency in the progress record; distinguish implementation complete from review complete.

### Step 3: Complete Development

After all tasks complete and verified, use `/1-code-review` on the plan's diff and address in-scope findings. Report exact verification evidence, including uncommitted changes when present; a SHA alone does not identify a dirty candidate. Return to the requesting workflow with plan status and remaining work. If integration or PR options are requested, use `/1-finish-branch` with the verified candidate, base branch, and workspace ownership; execute only the selected outcome.

## When to Stop and Ask for Help

**Pause the affected task when:**
- A dependency, test failure, or unclear instruction remains unresolved after safe, in-scope diagnosis
- Plan has critical gaps preventing starting
- You don't understand an instruction
- Verification fails repeatedly

**Ask for clarification rather than guessing.**

## When to Revisit Earlier Steps

**Return to Review (Step 1) when:**
- Partner updates the plan based on your feedback
- Fundamental approach needs rethinking

**Don't force through blockers** - stop and ask.

## Remember
- Review plan critically first
- Follow the agreed plan without overriding safety or ignoring contradictory evidence
- Don't skip verifications
- Reference skills when plan says to
- Diagnose routine failures within scope; ask when an unresolved decision or missing authority prevents progress
- Never start implementation on main/master branch without explicit user consent

## Integration

**Conditional handoffs (return to this plan unless finishing was requested):**
- **/1-git-worktrees** — prepare or verify task-matching isolation when needed
- **/1-write-plan** — only if a usable plan is missing or a material revision is requested
- **/1-code-review** — scoped review of the completed implementation
- **/1-finish-branch** — only for requested integration or PR options, with explicit authority
