---
id: inbox-pm-1749-xvfb-soft-skip-intake
agent: pm
ticket_id: 1749
updated: 2026-09-07
status: inbox
sources:
  - ticket:1749
  - https://code.visualstudio.com/api/working-with-extensions/continuous-integration
  - wiki/Engineering/AI-Native-Engineering/Tenant-Quality-Yaml-Gate-Skip-Pattern.md
---

# codingland EH smoke xvfb coupling (NF intake)

- Smell `test.coupled`: `extension/scripts/run-vscode-test.cjs` always `spawnSync('xvfb-run')` on headless Linux; missing binary → ENOENT fails `npm --prefix extension run ci` after unit pass.
- Prefixed boy-scout: soft-skip `test:vscode` when `xvfb-run` absent + document in `.factory/quality.yaml`; keep `npm test` as always-on clean_code floor. Optional: install xvfb in NF image (platform follow-up).
- VS Code Extension CI docs require xvfb (or Xvfb+DISPLAY) for Linux EH; soft-skip is gate-noise reduction, not EH coverage replacement.
