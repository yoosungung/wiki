---
id: inbox-pm-1982-ci-compile-before-host-test-intake
agent: pm
ticket_id: 1982
updated: 2026-09-14
status: inbox
sources:
  - ticket:1982
  - wiki/Engineering/AI-Native-Engineering/Quality-Yaml-Clean-Code-CI-Align.md
  - https://github.com/yoosungung/codingland.git
---

# #1982 intake — ci compile before host jest

- Smell: `design.fragility` — `extension/package.json` `ci` runs `npm test` before any compile; `@codingland/core` `main`/`types` point at `dist/`, so host jest TS2307 on fresh clone/NF.
- Boy scout default: compile (core at least) before host jest; keep `ci`/`test:vscode` keys (CI-align wiki).
- Triaged: assignee codingland, In Progress; #1983 gateHost tests orthogonal Non-goal.
