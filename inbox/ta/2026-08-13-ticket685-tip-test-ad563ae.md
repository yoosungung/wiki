---
id: inbox-ta-685-tip-test-ad563ae
agent: ta
ticket_id: 685
updated: 2026-08-13
status: inbox
sources:
  - ticket:685
  - https://github.com/yoosungung/nl2sql/pull/79
  - wiki/Engineering/Infrastructure-and-DevOps/In-Cluster-Kaniko-Tip-GHCR.md
  - wiki/Engineering/Infrastructure-and-DevOps/Test-Overlay-vs-Release-Package-Deploy-Paths.md
---

# #685 tip roll test-ad563ae (Kaniko)

- merge_sha `ad563aebf62a7860cd93bab93ada713895087c38` (nl2sql#79). Registry `deploy.yml` missing on main — tip path = in-cluster Kaniko (wiki In-Cluster-Kaniko-Tip-GHCR).
- Jobs `nl2sql-kaniko-backend-test-ad563ae` + `nl2sql-kaniko-mcp-test-ad563ae` Complete → tip roll both deploys to `ghcr.io/…:test-ad563ae`.
- Smoke: backend `/api/health`+`/api/ready` 200; mcp `:8800` `/health`+`/ready` 200.
- Handed QA for AC3 `spider2-opik run --task agent --instance-ids local008,local022` (need pass_rate>0); AA re-gate on new tip. Not Deploying Prod.
