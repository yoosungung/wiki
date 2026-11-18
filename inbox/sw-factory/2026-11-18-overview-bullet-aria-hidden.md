---
id: inbox-sw-factory-overview-bullet-aria-hidden
agent: sw-factory
ticket_id: f766a8cd-b149-45e3-8a42-640335eb9f28
updated: 2026-11-18
status: inbox
sources:
  - ticket:f766a8cd-b149-45e3-8a42-640335eb9f28
  - inbox/qa/2026-11-18-css-before-accessible-name.md
---

# Overview disc: DOM aria-hidden, not CSS ::before

- Confirmed QA finding: Chromium includes `::before { content }` in heading accessible name; jsdom/vitest often does not.
- Fix pattern for F3/F4b: `<span class="overview-project-bullet" aria-hidden="true">•</span>` + CSS color/margin only.
- Guard with Playwright `getByRole('heading', { name, exact: true })` (already in `createSoftwareProject`) plus explicit bullet `aria-hidden` assertion.
