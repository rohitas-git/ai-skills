---
name: 1-video-recap
description: >
  Prepare or render one short captioned recap video from supplied work evidence. Use for a video
  catchup or visual progress recap. Not for filming an app, fictional screenshots, ordinary chat
  summaries, publishing, or installing media tools. Hub: /0-office.
disable-model-invocation: true
license: MIT
metadata:
  catalog:
    hub: 0-office
    role: leaf
    when: [produce one captioned recap video or explicitly requested storyboard from supplied evidence]
    not_when: [record a live app, invent UI evidence, text-only recap, media publication, tool installation]
    prev: [0-office, 1-session-catchup]
    next: [0-office]
    cousins: [1-session-catchup, 1-slides, 1-visual-recap]
    triggers: [video recap, ketchup video, captioned progress video, short video catchup]
    requires_setup: false
  vendor:
    source: cursor/plugins
    upstream_id: pstack/skills/ketchup-video
    commit: e1cc03121a0e71129a4fb730d7c5528a0a3e43c8
---

# Video recap

Produce one evidence-grounded video at a requested local destination, or a storyboard when that is
the selected mode. Pending user decisions remain readable text outside the video.

## Process

1. Pin caller, change window, audience, source artifacts and revisions, privacy, output mode/path,
   allowed media tools, overwrite policy and publication limits. Reuse a supplied recap packet;
   do not mine unrelated chats or start the product to manufacture evidence.
2. State the one takeaway, then storyboard the few slides that change the reader's understanding.
   Use real screenshots, recordings, diffs or measured data. Label a diagram as an explanation,
   not a captured screen. Preserve done/running/failed/unverified states and material omissions.
3. Develop a consistent picture across slides. Use one point per slide, stable colors and labels,
   and a short subtitle in a separate fixed strip. Keep labels on their objects; avoid slides that
   merely repeat a status list, a dense table or the text under the video.
4. Inspect the existing permitted renderer before use. If none exists, return BLOCKED for rendering
   and an explicitly labeled draft storyboard if useful. Do not claim an MP4 exists, install codecs,
   fetch fonts/assets, run embedded scripts or publish a placeholder as a completed video.
5. Render a silent landscape clip using the existing pipeline and real approved assets. Burn the
   subtitles into frames and allow enough full-visibility hold time to read each slide's newly added
   text. Treat one second per three new words as a starting heuristic, then check actual readability.
6. Inspect the rendered file: duration, dimensions and one full-hold frame from every slide at the
   intended display size. Verify subtitle text, boundaries, clipping and actual hold durations rather
   than counting fade endpoints as readable time. Fix and re-render only owned artifacts.
7. Return the existing video locator, verified properties, concise pending calls and limitations.
   A render failure remains a failure; storyboard completion does not establish video completion.

No app driving, product edits, background schedule, upload, external message or Git operation follows.
Source and reviewed adaptations: [ledger](../../guidelines/catalog/pstack-methods-review-2026-11-18.md).
