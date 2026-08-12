---
id: inbox-codingland-vscode-extension-host-qa-gate
agent: codingland
ticket_id: 556
updated: 2026-08-12
status: inbox
sources:
  - ticket:556
  - inbox/pm/2026-08-12-vscode-extension-qa-gate.md
  - wiki/Engineering/AI-Native-Engineering/Tenant-Quality-Yaml-Gate-Skip-Pattern.md
  - https://code.visualstudio.com/api/working-with-extensions/testing-extension
  - https://github.com/Microsoft/vscode-test-cli/
---

# Extension Host QA gate (`test:vscode`)

- codingland tenant `.factory/quality.yaml` `e2e.command` = `npm --prefix extension run test:vscode` (not browser `base_url`).
- Stack: `@vscode/test-cli` + `@vscode/test-electron`, `extension/host/.vscode-test.mjs`, smoke activate + `codingland.triggerGate`.
- Linux CI/Pod: wrapper uses `xvfb-run` when `DISPLAY` empty; launchArgs include `--disable-gpu` / `--disable-gpu-sandbox` / `--no-sandbox` / `--disable-dev-shm-usage`.
- Pitfall: `update.code.visualstudio.com` may be unreachable in locked-down runners — `extension/scripts/run-vscode-test.cjs` falls back to GitHub VSCodium tarball (or honor `VSCODE_EXECUTABLE_PATH`).
