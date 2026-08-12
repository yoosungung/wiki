---
id: inbox-ta-ticket391-test-42c2eb1-ac3-fail
agent: ta
ticket_id: 391
updated: 2026-08-12
status: inbox
sources:
  - ticket:391
  - https://github.com/yoosungung/nl2sql/pull/67
  - wiki/Engineering/Infrastructure-and-DevOps/Test-Overlay-vs-Release-Package-Deploy-Paths.md
---

# #391 AC3 fail on tip test-42c2eb1

- Tip live via Kaniko (`test-42c2eb1` / merge `42c2eb1`); smoke health+ready 200.
- AC3 experiment `ticket391-agent-smoke-test-42c2eb1-20260812-050159` — ~112s · empty SQL residual · pass_rate **0**.
- PR #67 model-message sanitize did not clear AC3 empty-SQL gate on local008/local022.
