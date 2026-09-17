# Source notes — Complete PR Review

## Adopted review areas

The user supplied the following cross-source checklist. The live skill uses these as
review lenses, constrained by its PR scope guard:

- **Functionality and logic:** Does the change solve its intended problem, handle relevant
  edge cases, and avoid unintended side effects?
- **Architecture and design:** Are module boundaries appropriate, existing abstractions or
  libraries reused where suitable, and new patterns justified by real variation?
- **Complexity:** Is the changed logic understandable and proportionate? Would splitting a
  large or incoherent change make the behavior safer to review?
- **Security and data privacy:** Do changed trust boundaries expose credentials, sensitive
  data, or an exploitable authorization/validation weakness?
- **Testing:** Do focused tests exercise the changed contract and distinguish the new
  behavior from the pre-change failure?
- **Readability and style:** Do names, structure, and necessary documentation make the
  change maintainable without turning the review into formatting nitpicks?

## Provenance and access state

- YouTube: [The Effective Pull Request Checklist](https://www.youtube.com/watch?v=HUdmjJQg9UI&t=57s)
  — page title, description, and auto-generated caption track were accessible. It frames a
  practical checklist for reviewing many pull requests; this skill adopts only the
  review-relevant checklist areas above.
- User-provided supporting links: [video](https://www.youtube.com/watch?v=lz32biXRwdM&t=64),
  [PR reviewer practices](https://www.gustavwengel.dk/2025/02/19/pr-reviewer-practices.html),
  [security/process guide](https://medium.com/@iamprovidence/ultimate-guide-to-pr-review-process-6d75c8886763),
  and [readability checklist](https://medium.com/@dorinbaba/the-perfect-pr-review-checklist-no-one-is-talking-about-50ca213a4ac1).
- The [Google shared link](https://share.google/aimode/AzDyECjLa75p9CguE) resolved to a
  generic Google Search page during retrieval. No claimed content from that link appears in
  this skill.

These sources are prompts for evidence collection, not proof that a specific PR contains a
defect. Every reported finding still requires repository evidence and a concrete scenario.
