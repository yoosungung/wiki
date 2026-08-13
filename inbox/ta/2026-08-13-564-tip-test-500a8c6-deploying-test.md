---
id: inbox-ta-564-tip-test-500a8c6-deploying-test
agent: ta
ticket_id: 564
updated: 2026-08-13
status: inbox
sources:
  - ticket:564
  - https://github.com/yoosungung/nl2sql/pull/76
  - wiki/Engineering/Infrastructure-and-DevOps/In-Cluster-Kaniko-Tip-GHCR.md
  - wiki/Engineering/Infrastructure-and-DevOps/Test-Overlay-vs-Release-Package-Deploy-Paths.md
---

# #564 tip roll test-500a8c6 (Kaniko)

- Tip path: in-cluster Kaniko Jobs → GHCR (`test-<shortsha>`), not `publish-releases` / Actions tip.
- Tag `test-500a8c6` from merge_sha `500a8c6d3415b05efa7ee9ff6cdcbbed489b75a3` (nl2sql#76) · Jobs Complete ~50s backend / ~3m47s mcp.
- Roll: `kubectl set image` backend+mcp → Ready 1/1; smoke `/api/health` `/api/ready` `/health` `/ready` all HTTP 200.
- CM still luna + credential-less git-http remotes + `*_GIT_HTTP_USERNAME=git` (OPENAI_API_BASE absent).
