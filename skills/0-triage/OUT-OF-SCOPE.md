# Rejection-record contract

A repository-local rejection record is an optional, separately authorized effect for one durable,
accepted decision that a named enhancement concept is outside the candidate's product scope. It is not
required for every `wontfix`, temporary deferral, duplicate, invalid report, or already-built behavior.

```markdown
# <Concept>

**Status:** active | superseded
**Decision owner/date:** <who accepted what, when>
**Scope:** <where this decision applies>

## Decision and rationale
<Evidence-backed reason and meaningful constraints.>

## Prior requests
- <issue/PR identity and revision or durable link>

## Supersession
<Later decision pointer when status changes; preserve history.>
```

Before create/update, pin repository/worktree/branch/`HEAD`, exact path, current content/revision, dirty
ownership, privacy, and write authority. Search only the bounded index/location configured by the project;
do not read arbitrary repository data or use semantic similarity as proof. Re-read before the smallest
conflict-safe edit and verify the diff. Never delete history merely because the decision changes—mark it
superseded and point to the newer decision. Do not commit or push.
