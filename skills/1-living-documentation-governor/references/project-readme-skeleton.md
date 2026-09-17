# README baseline

Use only when a repository has no established README convention and creating one is requested.

```markdown
# Project name

Purpose and supported audience.

## Quick start

Verified prerequisites and commands; do not invent environment values or secret setup.

## Commands

Only commands confirmed in repository tooling.

## Architecture and operations

Link canonical current guides and accepted decisions rather than copying them.

## Contributing

Link repository rules, tests, review, and documentation obligations.
```

Not every project needs every section. Verify commands from the pinned candidate, distinguish local
from deployed behavior, and do not expose secrets. Release notes/changelogs belong to their release
workflow.
