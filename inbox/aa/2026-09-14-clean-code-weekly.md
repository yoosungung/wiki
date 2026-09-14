---
id: inbox-aa-2026-09-14-clean-code-weekly
agent: aa
ticket_id: 1982
updated: 2026-09-14
status: inbox
sources:
  - ticket:1982
  - ticket:1983
  - wiki/Engineering/AI-Native-Engineering/Quality-Yaml-Clean-Code-CI-Align.md
  - wiki/Engineering/AI-Native-Engineering/Tenant-Quality-Yaml-Gate-Skip-Pattern.md
  - https://github.com/kulshekhar/ts-jest/issues/3938
  - https://github.com/kulshekhar/ts-jest/issues/1648
---

# aa-clean-weekly 2026-09-14

- Tenant sync: sw-factory `20f8190`, nl2sql `401b55b`, candidate `46379de`, codingland `03e1714` under `/tmp/tenant-repos/<repo_id>`.
- Skip `clean_code` when `.factory/quality.yaml` absent (sw-factory, candidate) — same as missing-key skip pattern.
- nl2sql mechanical aligned with CI 3단 (ruff+mypy+pytest) EXIT 0 / 347 passed; prior clean-code remediations (inspect extract, WriteOp, tool_result ok, validator load Issues) still present → no new High/Med.
- codingland: `@codingland/core` `main`/`types` point at `dist/`; `ci` runs `npm test` before compile → host jest TS2307. Boy scout: compile before host test (or moduleNameMapper to src). ts-jest does not build workspace references automatically.
- Filed New #1982 (ci compile order), #1983 (gateHost test.missing) on codingland project_id=8.
