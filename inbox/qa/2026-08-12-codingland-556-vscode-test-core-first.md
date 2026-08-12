---
id: inbox-qa-codingland-556-vscode-test-core-first
agent: qa
ticket_id: 556
updated: 2026-08-12
status: inbox
sources:
  - ticket:556
  - inbox/codingland/2026-08-12-vscode-extension-host-qa-gate.md
  - inbox/pm/2026-08-12-vscode-extension-qa-gate.md
---

# codingland `test:vscode` must compile core first

- Tenant gate `.factory/quality.yaml` `e2e.command` = `npm --prefix extension run test:vscode`.
- Script currently runs only `npm run compile -w codingland` then vscode-test. On a fresh sync (no `extension/core/dist`), host `tsc` fails: `Cannot find module '@codingland/core'` (exit 2).
- Fix shape: make `test:vscode` / root `compile` order include `@codingland/core` before host (same as `extension` package `"compile"` script), so QA ephemeral clone passes without manual precompile.
- Pod headless notes (env, not product AC): need `xvfb-run` + GTK/`libnss3`/`libgbm` for VSCodium; CDN may be blocked → VSCodium GitHub fallback already in `run-vscode-test.cjs`.
