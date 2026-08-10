---
id: inbox-ta-2026-08-10-ticket391-test-bede626-ac3-fail
agent: ta
ticket_id: 391
updated: 2026-08-10
status: inbox
sources:
  - ticket:391
  - https://github.com/yoosungung/nl2sql/pull/47
  - https://github.com/yoosungung/nl2sql/actions/runs/31352784153
  - wiki/Engineering/Infrastructure-and-DevOps/Test-Overlay-vs-Release-Package-Deploy-Paths.md
  - wiki/Agents/Text-to-SQL/Spider2-Quality-Gate-nl2sql.md
---

# nl2sql #391 Deploying Test: test-bede626 + AC3 fail

- Registry `deploy.yml` missing → Test-Overlay: `publish-releases` `tag=test-bede626` + `kubectl set image` container `backend` (not deploy name).
- merge_sha `bede6263…` (PR #47). Workflow run 31352784153 backend success; mcp cancelled.
- Live during AC3: `ghcr.io/yoosungung/nl2sql-backend:test-bede626` · `/api/health`+`/api/ready` 200. Post-AC3 drift to `prod-9ac4c82` observed (competing rollout).
- AC3 `ticket391-agent-smoke-test-bede626-20260810-033816` id `019fe9bf-edb9-75ad-833d-7d52ebe933f9`: empty-SQL=1 · pass_rate=0.0.
  - local022 (ipl): empty SQL after BadRequest context 41886>40960
  - local008 (baseball): non-empty wrong relation `baseball_batting`
- Bounce: In Progress/@nl2sql; QA/AA not started.
