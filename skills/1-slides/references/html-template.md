# Safe self-contained HTML notes

Prefer semantic, dependency-free HTML/CSS/JavaScript with artifact-local styles. Each slide should be a labeled section;
navigation buttons need accessible names and disabled/end behavior; arrow keys must not trap normal controls. Provide
visible focus, reduced-motion handling, sufficient contrast, responsive overflow, and print rules when required.

External CDNs, fonts, analytics, remote images, and chart libraries require explicit network/runtime/licensing consent.
For supplied numeric data, local SVG or accessible HTML is often sufficient. Never interpolate untrusted source text
into HTML without escaping/sanitizing it. Verify in an authorized browser when available; structural inspection alone
is not rendered proof.
