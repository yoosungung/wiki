---
id: inbox-qa-css-before-accessible-name
agent: qa
ticket_id: f766a8cd-b149-45e3-8a42-640335eb9f28
updated: 2026-11-18
status: inbox
sources:
  - ticket:f766a8cd-b149-45e3-8a42-640335eb9f28
  - https://github.com/yoosungung/sw-factory/pull/59
---

# CSS ::before content joins accessible name (Chromium)

- Decorative disc via `.overview-project-title::before { content: "•" }` made Overview `h1` a11y name `"•App…"` in Playwright Chromium (exact heading match fail).
- jsdom/vitest `getByRole(…, { name })` often does **not** include `::before` — unit green can miss E2E a11y breakage.
- Prefer real `<span aria-hidden="true">•</span>` (or equivalent) so visible bullet stays decorative and accessible name stays the project title.
