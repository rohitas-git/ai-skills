# Local UI alternatives

Use for a visual/information-hierarchy question, not an API or production feature.
The parent [skill](./SKILL.md) controls scope, workspace and handoff.

## 1. Define the experiment

Name the user task and what the alternatives should reveal. Two or three materially
different layouts are usually enough; follow an explicit user count. Match the
project's brand, component system and accessibility requirements. Read the
applicable project brand/design guide before UI changes.

## 2. Choose a local-only surface

Use an existing preview/story environment when available. Otherwise build a
clearly marked local prototype route or a gated experiment in the task's isolated
checkout. Preserve the normal page and use synthetic or authorized read-only data;
realistic density does not require real customer records.

An existing page can provide valuable shell/context, but do not silently replace
its production rendering or trigger its real mutations. If comparing variants on
a route, guard the **entire experiment**, not merely a switcher bar. Verify that
production rendering cannot select prototype components through query parameters
or direct URLs. A non-production check is not access control for deployed previews.

## 3. Build and compare

Give variants distinct structure or interaction hierarchy, not arbitrary color
changes. Reuse appropriate components without forcing all variants into one layout.
A small URL-driven switcher is useful only when it helps comparison:

- Validate the variant key and provide a predictable fallback.
- Preserve unrelated query parameters.
- Use labeled, keyboard-accessible controls that do not obscure content.
- Do not globally hijack arrow keys used by form controls, menus, sliders or other
  widgets; scoped controls are sufficient.
- Mutating actions use stubs or explicit disposable state, never production APIs.

Keep the experiment within its requested files; do not add a general component
framework, new runtime or shared global configuration solely for a throwaway view.

## 4. Verify and return

Run the local page at an available task-owned port. Inspect every variant at the
relevant viewport and interaction state; check console/network failures that could
invalidate the comparison. Preserve Auth/security rules. If browser verification
is unavailable, report the unverified aspects rather than claiming visual success.

Return local URL/run command, variant keys, observed trade-offs, screenshots when
available, and the question still requiring user judgment. Record the user's
chosen direction without automatically promoting it. Production changes,
publication, losing-variant deletion and service/worktree cleanup are separate
authorized actions, not part of finishing a prototype.
