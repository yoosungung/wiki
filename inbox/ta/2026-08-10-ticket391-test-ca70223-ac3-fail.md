---
id: inbox-ta-2026-08-10-ticket391-test-ca70223-ac3-fail
agent: ta
ticket_id: 391
updated: 2026-08-10
status: inbox
sources:
  - ticket:391
  - https://github.com/yoosungung/nl2sql/pull/49
  - https://github.com/yoosungung/nl2sql/actions/runs/31356127094
  - wiki/Engineering/Infrastructure-and-DevOps/Test-Overlay-vs-Release-Package-Deploy-Paths.md
---

# nl2sql #391 Deploying Test: test-ca70223 + AC3 fail

- PR #49 merge_sha `ca70223…` (shared execute SSE stash) → Test-Overlay `tag=test-ca70223` + backend image set.
- Workflow 31356127094 backend success; mcp cancelled. Live pin held through AC3.
- Smoke: `/api/health`+`/api/ready` 200.
- AC3 `ticket391-agent-smoke-test-ca70223-20260810-044153` id `019fe9fa-2c9f-7556-a04c-4a0cd44b8e68`: empty-SQL=2 · pass_rate=0.0.
  - Both instances: LangGraph BadRequest context overflow (51994 / 48777 tokens > 40960) → empty SQL.
- Bounce: In Progress/@nl2sql; QA/AA not started.
