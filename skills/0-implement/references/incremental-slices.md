# Incremental slices

Slice a change when doing so creates an independently understandable, verifiable checkpoint without
breaking required invariants.

## Choose by dependency and risk

- **Vertical/tracer slice:** one thin end-to-end path when it can be safe and testable.
- **Contract-first:** stabilize a consumer/provider seam when parallel or staged work depends on it.
- **Risk-first experiment:** falsify a load-bearing unknown before building around it.
- **Compatibility phase:** expand → migrate → contract when consumers or stored data cannot move at
  once.
- **Atomic local change:** keep a small cohesive change together when splitting would create a broken
  or misleading intermediate state.

No strategy is universally preferred. Do not split schema from the code required to keep the branch
safe merely for line-count purity; database-specific migration rules still govern file boundaries and
deployment order.

## Per-slice contract

Record outcome, acceptance evidence, dependencies, allowed paths, worktree/service ownership, and
rollback/next-state assumptions. Keep unrelated cleanup out. Verify the narrowest relevant claims
before expanding; a slice may remain uncommitted unless commit authority and granularity justify it.

Stop and re-slice when ownership overlaps, the candidate cannot be reviewed independently, the
intermediate state would expose unsafe behavior, or one slice has acquired a second unrelated outcome.
