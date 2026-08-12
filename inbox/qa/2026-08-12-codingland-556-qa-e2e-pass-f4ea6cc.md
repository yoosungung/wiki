---
id: inbox-qa-codingland-556-qa-e2e-pass-f4ea6cc
agent: qa
ticket_id: 556
updated: 2026-08-12
status: inbox
sources:
  - ticket:556
  - https://github.com/yoosungung/codingland/pull/9
  - inbox/qa/2026-08-12-codingland-556-vscode-test-core-first.md
  - inbox/pm/2026-08-12-codingland-556-pr9-core-first-merge.md
---

# codingland #556 QA e2e pass on f4ea6cc

- After PR #9 merge (`f4ea6cc`), wipe `extension/core/dist` + `extension/host/out` then `npm --prefix extension run test:vscode` (quality.yaml `e2e.command`) compiles core then host and smoke passes: activate + `codingland.triggerGate` (2 passing, exit 0).
- Official VS Code CDN download may fail in Pod; runner falls back to cached VSCodium under `extension/host/.vscode-test/` (documented residual; prefer `VSCODE_EXECUTABLE_PATH`).
- tenant_cd / Deploying Test: N/A for Extension Host-only gate — PM Done after qa+aa (skip TA).
