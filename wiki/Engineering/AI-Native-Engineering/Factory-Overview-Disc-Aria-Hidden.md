---
id: factory-overview-disc-aria-hidden
title: "Factory Overview disc: aria-hidden not CSS ::before"
status: canonical
owner: km
updated: "2026-11-19"
last_updated: "2026-11-19"
review_after: "2027-02-19"
sources:
  - inbox/qa/2026-11-18-css-before-accessible-name.md
  - ticket:f766a8cd-b149-45e3-8a42-640335eb9f28
  - inbox/sw-factory/2026-11-18-overview-bullet-aria-hidden.md
tags: ["Engineering", "Factory", "a11y", "SPA"]
type: wiki
---

# Factory Overview disc: aria-hidden not CSS ::before

## Overview disc accessible name

- - Decorative disc via `.overview-project-title::before { content: "•" }` made Overview `h1` a11y name `"•App…"` in Playwright Chromium (exact heading match fail).
- - jsdom/vitest `getByRole(…, { name })` often does **not** include `::before` — unit green can miss E2E a11y breakage.
- - Prefer real `<span aria-hidden="true">•</span>` (or equivalent) so visible bullet stays decorative and accessible name stays the project title.
- - Confirmed QA finding: Chromium includes `::before { content }` in heading accessible name; jsdom/vitest often does not.
- - Fix pattern for F3/F4b: `<span class="overview-project-bullet" aria-hidden="true">•</span>` + CSS color/margin only.
- - Guard with Playwright `getByRole('heading', { name, exact: true })` (already in `createSoftwareProject`) plus explicit bullet `aria-hidden` assertion.

- Prefer DOM `aria-hidden="true"` on decorative disc; CSS `::before` content is joined into Chromium accessible name (qa trap).
