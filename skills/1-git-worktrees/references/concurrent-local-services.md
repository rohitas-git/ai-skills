# Concurrent local Supabase worktrees

Use this reference only after a worktree exists and the project uses local Supabase.

## Choose the topology first

| Worktree state | Topology | Guardrail |
|---|---|---|
| Frontend-only or schema-compatible work | One shared local stack | No reset, seed, or local migration application from either branch while shared. |
| Different migrations, schema, seed data, auth state, or DB-dependent tests | One stack per active worktree | Use unique project identity and host ports for every stack. |
| No safe local-only configuration mechanism | Do not start a second stack yet | Ask for the repository's override/launcher convention; do not commit a port change. |

## Isolated-stack checklist

1. Allocate a documented, non-overlapping port block per worktree. Inspect the current `supabase/config.toml`; change every enabled host-exposed service port, not only API, database, Studio, and Inbucket.
2. Give each stack a unique `project_id`. Supabase uses it to distinguish local projects on the same host.
3. Keep those overrides local. Prefer a repository-provided untracked config/launcher. Do not commit worktree-specific `project_id`, ports, local URLs, or keys. Do not assume `--workdir` is a config overlay: it selects the full Supabase project directory, including migrations and functions.
4. Start and inspect only the local stack from its verified worktree/config: `rtk supabase start`, then `rtk supabase status`. Confirm the intended local endpoints before connecting the app. Inspect keys privately; preserve an existing environment file and change only the agreed local fields, never blindly copy another worktree's secrets or overwrite unrelated settings.
5. Run each web app on a separate local port. Align `auth.site_url` and allowed redirect URLs with that app instance when Auth flows are tested.
6. Workspace setup alone does not authorize applying migrations, seeding or resetting data. For requested local migration work, hand off to `/1-supabase-schema-migration` and return here with verification evidence. Use only the permitted local command (`rtk supabase db push --local` or local psql under the active policy); verify the intended local target first. Never reset as routine setup, and never use linked, remote, repair, or production commands; CI applies migrations on merge.

## Completion check

For every active worktree, record privately: worktree path, branch, Supabase `project_id`, actual exposed ports, app port, status-derived URL, and service owner. Confirm each app points to its intended stack and that task-local configuration is absent from the tracked diff and index. A port block is a planning convention, not evidence that ports are available. Preserve any pre-existing tracked changes; report conflicts instead of silently restoring them.

## Sources

Supabase documents `project_id` as the local-host project discriminator, config ports as local-project settings, Auth redirect configuration, and `--workdir`/`SUPABASE_WORKDIR` as the project-directory selector: <https://supabase.com/docs/guides/local-development/cli/config> and <https://supabase.com/docs/reference/cli/supabase-start>.
