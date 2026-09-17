# Security hardening source adaptation

Historical source bodies, retained for provenance only:
- [Full vendor workflow](./vendor-security-full.md).
- [Duplicate vendor checklist](./security-checklist-vendor-pack.md).

They are not live execution instructions. The local main and focused references
govern authority, scope, workspace handling, commands and verification.

Retained and adapted: threat boundaries (including locally delivered untrusted
values), least privilege, input/output checks, dependency root/script provenance,
multi-instance rate-limit concerns, data minimization and destructive-path ownership.

Corrected or excluded:
- Automatic credential rotation/revocation, history purges, policy commits, installs
  and production-facing hardening inferred from a generic checklist.
- Raw secret-match output and universal claim that a diff proves history clean.
- Denylist-based public record projection and unrestricted request-body updates.
- A DNS precheck followed by independent fetch presented as a complete SSRF defense.
- MIME/extension-only upload checks and unconstrained response/error data.
- Blanket camera/microphone/CORS/session/header defaults that ignore valid use cases.
- Static package-manager version/default matrices as operational truth; verify the
  actual pinned client and use its current official documentation instead.
- Universal legal consent/retention/deletion claims. Use approved policy and the
  dedicated compliance/incident workflows, not incidental legal advice here.
- Unsupported numeric generalizations about breach origins or security retrofit cost.
- Duplicate full checklists and impossible advice to keep a model's system prompt
  outside its own context. Keep secrets/authority outside prompts instead.

The SQL and projection illustrations in the local patterns are deliberately partial
contracts, not tested production endpoint implementations. No dependency, shell
installer, runtime service or production operation is bundled or activated.
