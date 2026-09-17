# Accessibility evidence checklist

Apply the project's declared accessibility target and platform conventions to the bounded surface.
This is a risk checklist, not a claim of WCAG conformance; mark non-applicable items explicitly.

## Structure and names

- [ ] Native elements and DOM order express the intended semantics where possible.
- [ ] Interactive elements have an accurate accessible name; visible labels are associated.
- [ ] Instructions, descriptions, required state, validation, and errors are programmatically related.
- [ ] Headings, landmarks, lists, tables, and regions describe the actual context without redundant roles.
- [ ] Meaningful images/media have equivalent alternatives; decorative imagery is ignored appropriately.
- [ ] Document language/title and navigation aids are correct when this surface owns them.

## Input and focus

- [ ] Supported actions work by keyboard without requiring pointer gestures.
- [ ] Focus order follows task/reading order and focus indication is visible at supported zoom/contrast.
- [ ] No unintended keyboard trap; composite widgets implement the applicable recognized pattern.
- [ ] Dialogs, popovers, menus, route changes, and inserted/removed content manage and return focus
      according to task context rather than an unconditional rule.
- [ ] Pointer/touch targets and alternatives meet the declared standard/platform requirements.
- [ ] Timeouts, drag/motion, shortcuts, or repeated input have alternatives where applicable.

## Dynamic states and forms

- [ ] Loading/pending, empty, partial, success, validation/error, disabled, permission/auth, and
      offline/retry states are covered where the interaction can reach them.
- [ ] Status or alert announcements are timely and concise without duplicating visible content.
- [ ] Error identification and recovery do not rely only on color, position, or placeholder text.
- [ ] Input purpose, format, autocomplete, and constraints match the actual data contract.
- [ ] Destructive actions expose consequence and recovery/confirmation appropriate to risk.

## Visual, content, and media

- [ ] Text/non-text contrast is measured against the applicable criterion and component state.
- [ ] Color is not the sole carrier of meaning.
- [ ] Content remains usable at required zoom/reflow/text-spacing settings and representative widths.
- [ ] Long/localized text and user content do not clip, overlap, or hide essential actions.
- [ ] Animation respects reduced-motion preference; flashing, autoplay, audio, captions, and controls
      meet applicable requirements.

## Runtime evidence

- [ ] Candidate, route, role/fixture, viewport, input method, browser/assistive technology, and run
      identity are recorded.
- [ ] Primary and error/recovery paths were exercised, not inferred from source.
- [ ] Relevant accessibility tree or screen-reader output was inspected when names, relationships,
      announcements, or custom widgets changed.
- [ ] Existing automated checks were run and findings assessed; a clean scan is not treated as proof.
- [ ] Unavailable browser, device, assistive technology, credentials, fixtures, or services are
      reported as BLOCKED/SKIPPED rather than silently assumed.

Do not install scanners, launch an unowned service, upload user data, publish a preview, or change
remote environments merely to complete this checklist.
