---
id: inbox-ta-ticket391-ac3-empty-sql-partial
agent: ta
ticket_id: 391
updated: 2026-08-10
status: inbox
sources:
  - ticket:391
  - wiki/Engineering/Infrastructure-and-DevOps/Test-Overlay-vs-Release-Package-Deploy-Paths.md
  - wiki/Agents/Text-to-SQL/Spider2-Quality-Gate-nl2sql.md
  - https://github.com/yoosungung/nl2sql/actions/runs/31349192148
---

# #391 AC3 agent smoke after test-f4218d3

- registry `deploy.yml` absent → Test overlay path: `publish-releases` tag `test-f4218d3` + `kubectl set image` backend-only (mcp build still running; wiki allows backend-only delta).
- Live image `ghcr.io/yoosungung/nl2sql-backend:test-f4218d3` · merge_sha `f4218d36…` · `/api/health`+`/api/ready` 200.
- AC3 `spider2-opik run --task agent --instance-ids local008,local022` experiment `ticket391-agent-smoke-20260810-022554` id `019fe97d-af17-7dcb-a076-f810941fd49f`:
  - local008: reason `empty SQL` (output "")
  - local022: non-empty SQL but wrong relation (`baseball_batting` on ipl question) → exec fail
  - pass_rate **0.0** · empty-SQL count **1** (AC3 hard fail)
- hermes needed `GRANT USAGE/SELECT` on spider2db schemas (owned by postgres) before check OK.
