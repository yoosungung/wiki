---
id: inbox-pm-1982-ci-compile-merge
agent: pm
ticket_id: 1982
updated: 2026-09-14
status: inbox
sources:
  - ticket:1982
  - https://github.com/yoosungung/codingland/pull/18
  - wiki/Engineering/AI-Native-Engineering/Quality-Yaml-Clean-Code-CI-Align.md
---

# #1982 merge — compile before host Jest

- intent: pass — PR #18 `merge_sha=c08dfdd16c164c261d6fa259fac4cc1b2214abb9`
- Diff: `ci` = `npm run compile && npm test && npm run test:vscode`; `packageScripts.test.cjs` locks order + gate keys; DESIGN Commands note.
- Evidence: dist-deleted host jest fails (Cannot find module); `compile && npm test` → core 90 + host 4 + scripts node:test pass. GH checks: none configured.
- Closeout: VSIX dogfood → tenant_cd N/A (no Deploying Test/@ta). Done.
