---
id: inbox-codingland-1982-ci-compile-before-host-test
agent: codingland
ticket_id: 1982
updated: 2026-09-14
status: inbox
sources:
  - ticket:1982
  - wiki/Engineering/AI-Native-Engineering/Quality-Yaml-Clean-Code-CI-Align.md
  - https://github.com/npm/cli/issues/4139
---

# #1982 — ci compile before host Jest

- npm workspaces do not topo-sort scripts; host Jest needs `@codingland/core` `main`/`types` → `dist/`.
- Fix: `extension/package.json` `"ci": "npm run compile && npm test && npm run test:vscode"`; keep `ci`/`test:vscode` keys (CI-align).
- Guard: `scripts/packageScripts.test.cjs` asserts compile precedes `npm test` in `ci`.
