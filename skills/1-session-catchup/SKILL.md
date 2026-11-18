---
name: 1-session-catchup
description: >
  Summarize changes in the current conversation and every still-open user decision. Use for
  catching up since the user's last message. Not for cross-session history reconstruction,
  a one-line status signal, a PR description, or continuing the work. Hub: /0-butler.
disable-model-invocation: true
license: MIT
metadata:
  catalog:
    hub: 0-butler
    role: satellite
    when: [catch the user up on this conversation and make pending decisions self-contained]
    not_when: [cross-session recall, one-line completion status, PR description, task execution]
    prev: [0-butler]
    next: [0-butler]
    cousins: [1-working-context, 1-quick-recap, 1-handoff, 1-video-recap]
    triggers: [catch me up on this chat, session catchup, what changed while I was away, ketchup]
    requires_setup: false
  vendor:
    source: cursor/plugins
    upstream_id: pstack/skills/ketchup
    commit: e1cc03121a0e71129a4fb730d7c5528a0a3e43c8
---

# Session catchup

Return one read-only update that lets the user understand the work and decide what needs them.
Use this conversation's evidence. It authorizes no implementation, publication or state change.

## Process

1. Set the change window to the last human message before the catchup request, or the explicit
   interval. Tool notifications and agent reports do not reset that window. Include unresolved
   user decisions raised earlier too, so an old pending call does not disappear.
2. Reconcile actions, actual results and artifact evidence. Recheck material current status only
   through permitted read-only sources; otherwise label it stale or unknown. A worker's summary
   is a claim to check, not a substitute for its receipts.
3. Separate work the agent can still perform from calls only the user owns: product preference,
   approval, missing access or an irreversible choice. Do not manufacture action items for routine
   reversible work or recommendations the user has not accepted.
4. Lead with what needs the user, or say that nothing does. Briefly explain what changed for them,
   with done/running/failed/unverified distinctions. Link or embed existing relevant evidence;
   never draw a purported screenshot or invent a number to fill a summary.
5. For each user call, give the item/link, what it changes, viable options, a grounded recommendation,
   material costs/risks and prerequisites. A shared call can group items, but retain each item's
   evidence and exceptions. Unknown decision-critical facts stay explicitly unknown.
6. State agent-owned work remaining separately. Return the catchup without resuming that work,
   posting comments or creating new artifacts unless the user requested an artifact format.

Use [the decision-packet checklist](./references/decision-packet.md) for larger queues.
For a requested captioned video use `/1-video-recap`; a catchup alone does not render one.

## Boundary

`/1-working-context` rebuilds several prior threads. `/1-handoff` writes a continuation file.
`/1-quick-recap` adds an explicitly requested traffic-light line. `/1-pr-summarizer` drafts PR prose.
