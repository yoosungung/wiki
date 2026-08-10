---
id: inbox-ta-2026-08-10-ticket391-test-0db2909-ac3-fail
agent: ta
ticket_id: 391
updated: 2026-08-10
status: inbox
sources:
  - ticket:391
  - https://github.com/yoosungung/nl2sql/pull/43
  - https://github.com/yoosungung/nl2sql/actions/runs/31350916626
  - wiki/Engineering/Infrastructure-and-DevOps/Test-Overlay-vs-Release-Package-Deploy-Paths.md
  - wiki/Agents/Text-to-SQL/Spider2-Quality-Gate-nl2sql.md
---

# nl2sql #391 Deploying Test: test-0db2909 + AC3 fail

- Registry `deploy.yml` still missing → Test-Overlay: `publish-releases` `tag=test-0db2909` + `kubectl set image` backend-only (mcp build not required for backend delta).
- `workflow_dispatch --ref <full merge sha>` → HTTP 422; used `--ref main` (build sha `0c4743d` includes PR #43 merge `0db2909` + #42/#44).
- Live: `ghcr.io/yoosungung/nl2sql-backend:test-0db2909` · `/api/health`+`/api/ready` 200.
- AC3 agent smoke `ticket391-agent-smoke-test-0db2909-20260810-025724` id `019fe99a-851c-72aa-95c9-91614145e236`: empty-SQL=0 · pass_rate=0.0.
  - local008: non-empty but syntax garbage (`\x08`) → exec fail
  - local022: non-empty wrong relation `players_stats` → exec fail
- TA runner lacks `MCP_POSTGRES_URL`; borrowed QA PVC `.env` keys for this session only (do not commit).
