---
id: inbox-ta-nl2sql-kaniko-tip-path
agent: ta
ticket_id: 551
updated: 2026-08-12
status: inbox
sources:
  - ticket:551
  - wiki/Engineering/Infrastructure-and-DevOps/Test-Overlay-vs-Release-Package-Deploy-Paths.md
  - wiki/Engineering/Infrastructure-and-DevOps/GHCR-Actions-Package-Write-ACL.md
---

# nl2sql Test tip: Kaniko primary (Actions dispatch fallback)

- Tip supply primary path is in-cluster Kaniko Jobs (`deploy/k8s/kaniko/` + `build-tip-images-kaniko.sh`) → GHCR; `build-ghcr-images` stays `workflow_dispatch` fallback (no main-auto; Actions cost).
- Secret `nl2sql-ghcr-build` needs `github-token` + Docker `config.json` for private clone + GHCR push; apply SA needs `batch/jobs` create in `nl2sql`.
- Executor pin currently `gcr.io/kaniko-project/executor:v1.23.2` (archived upstream); migrate to Chainguard/self-built later.
