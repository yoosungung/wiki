---
id: inbox-codingland-test-vscode-compile-core-first
agent: codingland
ticket_id: 556
updated: 2026-08-12
status: inbox
sources:
  - ticket:556
  - inbox/qa/2026-08-12-codingland-556-vscode-test-core-first.md
---

# `test:vscode` must compile core before host

- Fresh tenant sync wipes `core/dist` + `host/out`. `test:vscode` that only runs `compile -w codingland` fails with `Cannot find module '@codingland/core'`.
- Fix: `npm run test:vscode` → `npm run compile && …` (core then host), matching workspace `compile` script.
- Pod QA also needs xvfb + gtk/nss/gbm/asound libs; prefer `VSCODE_EXECUTABLE_PATH` when CDN blocked.
