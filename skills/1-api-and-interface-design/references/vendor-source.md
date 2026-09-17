# Source map and adaptation limits

**Upstream (archive, not host-discovered):** `archive/vendor/agent-skills/skills/api-and-interface-design/SKILL.md`

The archived Addy Osmani `agent-skills` snapshot is MIT-licensed and remains reference
material, not operative instructions. The live main file is the route/authority contract;
`full-guide.md` is a locally adapted guide. No upstream installation commands, plugins,
hooks, permissions, dependencies, or automatic activation behavior are adopted.

Promoted as a **lean** catalog skill. For depth, read the upstream sections:

- Overview
- When to Use
- Core Principles
- REST API Patterns
- TypeScript Interface Patterns
- Common Rationalizations
- Red Flags
- Verification

Local corrections include conditional rather than universal validation, compatibility checks
for additive changes, protocol-dependent pagination/update semantics, and an explicit warning
that the idempotency example is incomplete. Do not re-promote a second peer skill with the
same job from vendor.
