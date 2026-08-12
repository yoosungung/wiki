---
id: inbox-pm-vscode-extension-qa-gate
agent: pm
ticket_id: 556
updated: 2026-08-12
status: inbox
sources:
  - ticket:556
  - wiki/Engineering/AI-Native-Engineering/Playwright-Frontend-UI-Smoke-Pattern.md
  - wiki/Engineering/AI-Native-Engineering/Tenant-Quality-Yaml-Gate-Skip-Pattern.md
---

# VS Code extension QA gate ≠ browser base_url

- Factory QA `browser-e2e` assumes a web `base_url`. Cursor/VS Code **extension** products (e.g. codingland) need a **repo-owned Extension Host** command instead.
- Pattern: `@vscode/test-cli` + `@vscode/test-electron`, `.vscode-test.js`, smoke that extension activates / key command runs, `package.json` script e.g. `test:vscode`, and `.factory/quality.yaml` `e2e.command` pointing at that script (CI/headless-safe flags; non-zero on fail).
- QA evidence shape stays `qa: e2e pass scenario=<id> evidence=<log/url>` — criteria live in the tenant repo, not invented in the factory.
- Existing wiki Playwright frontend smoke ([[wiki/Engineering/AI-Native-Engineering/Playwright-Frontend-UI-Smoke-Pattern.md]]) is for **web** UIs; do not force Chromium against a missing base_url for extensions.
