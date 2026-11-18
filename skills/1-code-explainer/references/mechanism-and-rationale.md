# Explain mechanics and reasons together

Begin with what the named subsystem is and what task the reader wants to perform. Trace the concrete
input→state→effect path, including failure/teardown where material. Show where the relevant ownership
and seams live so a new maintainer can orient without reading an implementation inventory.

When the question includes why, use supplied decision records or the bounded `/1-design-rationale`
owner within the caller's read scope. Preserve its confidence language: a plausible purpose inferred
from code is not the author's recorded reason. Inaccessible history remains an unanswered question.
Do not substitute a bug diagnosis, redesign or automatic code change for the requested explanation.

Start with the smallest complete account and add depth where the actual question needs it. Explain
mechanisms, not stock framing labels. A short sequence of progressively expanded diagrams can help
when several interacting parts would overload a single picture; a simple point needs no diagram.
Do not force image generation, a fixed number of diagrams, an interview or a quiz. For non-code
concept teaching use the existing Learn leaf matching the learner's request.

Present verified source references, the observable path, recorded trade-offs, limitations and useful
gotchas. A walkthrough can explain behavior without claiming it was exercised or proven correct.

Adapted from the individually reviewed pstack 0.15.43 sources, MIT, Lauren Tan.
[Source-by-source decisions and checks](../../../guidelines/catalog/pstack-methods-review-2026-11-18.md).
