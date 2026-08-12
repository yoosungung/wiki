---
id: inbox-aa-codingland-556-aa-security-vscode-gate
agent: aa
ticket_id: 556
updated: 2026-08-12
status: inbox
sources:
  - ticket:556
  - wiki/Engineering/AI-Native-Engineering/Tenant-Quality-Yaml-Gate-Skip-Pattern.md
  - inbox/codingland/2026-08-12-vscode-extension-host-qa-gate.md
  - https://github.com/yoosungung/codingland/pull/8
  - https://code.visualstudio.com/api/working-with-extensions/testing-extension
---

# codingland #556 AA security — Extension Host QA gate

- `.factory/quality.yaml` has `e2e` only — no `security.command` → mechanical skip; scoped manual review (auth/Host/secret/transport).
- Candidate: master `4aa67fb` (PR #8). Delta is CI Extension Host harness + quality.yaml pointer — not a Deploying Test/prod Host surface.
- Runner `extension/scripts/run-vscode-test.cjs`: `spawnSync`/`execFileSync` fixed argv, `shell:false`; HTTPS download + redirect cap; VSCodium GitHub fallback is CI-only supply-chain residual (prefer `VSCODE_EXECUTABLE_PATH` pin).
- LaunchArgs `--no-sandbox` / gpu flags confined to `.vscode-test.mjs` (matches `@vscode/test-electron` CI defaults) — not product activation path.
- Product residual (not this gate fail): cloud Mirror opt-in default false + sanitize stub (no network); webview CSP `script-src 'unsafe-inline'` with scoped `localResourceRoots`.
