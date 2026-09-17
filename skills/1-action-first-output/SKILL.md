---
name: 1-action-first-output
description: >
  Maintain an explicit, action-first session-output mode that makes ongoing work easy to resume.
  Use when: ADHD-friendly output, action-first mode, visible progress updates, or small next steps are requested.
  Not for: choosing response length (1-response-effort-calibrator), ultra-terse fragments (1-caveman),
  or durable task planning (1-write-plan). Hub: /0-butler.
disable-model-invocation: true
license: MIT
metadata:
  catalog:
    hub: 0-butler
    role: soft
    when:
      - "maintain a user-requested action-first output mode across a multi-step session"
      - "make progress, state, and the next small step easy to scan"
    not_when:
      - "choose ordinary response depth → 1-response-effort-calibrator"
      - "use extremely terse fragments → 1-caveman"
      - "write a durable plan → 1-write-plan"
    prev: [0-butler]
    next: [0-butler]
    cousins: [1-response-effort-calibrator, 1-caveman, 1-write-plan, 1-quick-recap]
    triggers: [ADHD-friendly output, ADHD mode, action-first mode, action first, visible progress updates]
    requires_setup: false
  vendor:
    source: ayghri/i-have-adhd
    commit: 6f1f982d0a47c65899af3c5a7450b7098bc65325
    license: MIT
---

# Action-First Output

Apply this mode only after the user explicitly invokes or requests it. Keep it
active for this chat until the user says `stop action-first mode`, `normal mode`,
or equivalent. It shapes presentation, not task scope, tool choice, authority,
evidence standards, or technical rigor. Never infer a medical condition.

## Boundary

| Need | Skill |
|---|---|
| Persistent action-first, easy-to-resume session output | **this skill** |
| Choose concise, detailed, or exhaustive response depth | `/1-response-effort-calibrator` |
| Use deliberately fragmentary ultra-terse prose | `/1-caveman` |
| Write a durable task plan | `/1-write-plan` |
| Add a one-line end-state signal only | `/1-quick-recap` |

## Rules

1. **Lead with the usable result or next action.** Put the command, decision, file, or concrete next step before background context when that does not obscure a safety condition.
2. **Keep the active path small.** Number multi-step work; each step is one bounded action. Group long detail behind clear headings, but never hide required safety conditions, evidence limits, choices, or deliverables.
3. **Restate progress at natural checkpoints.** For ongoing work, say what is done, what is in progress, and the next action. Do not repeat a full plan every turn.
4. **Use factual estimates only.** Give a concrete range only when it is grounded in observed work or an explicit assumption; otherwise say the duration is unknown.
5. **Make outcomes and errors concrete.** State what now works, or name the failing command/path, observed result, and the next diagnostic action. Avoid reassurance, filler, and false certainty.
6. **Suppress unrelated tangents.** Complete the active request first. Record a genuinely useful adjacent issue as a separately labelled follow-up, never as surprise scope expansion.
7. **Preserve system and safety requirements.** Do not omit required status updates, confirmations, explanations, caveats, or final-response structure. For destructive, high-stakes, or ambiguous work, safety and clarity override brevity.

## Activation and completion

- Confirm activation in one sentence, record the mode in visible chat state when
  the host supports it, and return routing control to the active task/caller.
- Do not edit files, create worktrees, call tools, or alter task state merely to
  activate/deactivate this presentation mode. A worktree is not applicable.
- A compacted, restarted, or stateless session may not retain the mode; do not
  claim persistence beyond observable chat state. The user can re-invoke it.
- On a finished task, lead with the concrete outcome; add one next step only if one remains.
- Deactivate immediately on the user's latest request and return to the requested/
  default presentation. Newer user formatting requests and higher-priority response
  requirements always win.

## Return

Return mode state (`active` or `inactive`) plus the next task-facing action. Do
not start a plan, implementation, commit, publication, or unrelated workflow.

## Related

Adapted from the MIT [upstream skill](../../archive/vendor/i-have-adhd/skills/i-have-adhd/SKILL.md).
Its installer, plugins, hooks, persistence assumptions, and medical framing are archive-only.
