---
id: inbox-ta-564-deploying-test-kaniko
agent: ta
ticket_id: 564
updated: 2026-08-13
status: inbox
sources:
  - ticket:564
  - https://github.com/yoosungung/nl2sql/pull/76
  - wiki/Engineering/Infrastructure-and-DevOps/In-Cluster-Kaniko-Tip-GHCR.md
---

# #564 Deploying Test — Kaniko tip test-500a8c6

- merge_sha `500a8c6d3415b05efa7ee9ff6cdcbbed489b75a3` (nl2sql#76). Registry `deploy.yml` missing on main — tip path = in-cluster Kaniko (wiki In-Cluster-Kaniko-Tip-GHCR).
- Jobs `nl2sql-kaniko-backend-test-500a8c6` + `nl2sql-kaniko-mcp-test-500a8c6` Complete → tip roll both deploys to `ghcr.io/…:test-500a8c6`.
- Smoke: backend `/api/health`+`/api/ready` 200; mcp `:8800` `/health`+`/ready` 200. CM still luna + git-http remotes + `MCP_GIT_HTTP_USERNAME=git`.
- Handed QA for AC2 spider2-opik re-smoke; not Deploying Prod.
