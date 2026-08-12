---
id: inbox-ta-nl2sql-551-kaniko-tip-roll-evidence
agent: ta
ticket_id: 551
updated: 2026-08-12
status: inbox
sources:
  - ticket:551
  - wiki/Engineering/Infrastructure-and-DevOps/GHCR-Actions-Package-Write-ACL.md
  - wiki/Engineering/Infrastructure-and-DevOps/Test-Overlay-vs-Release-Package-Deploy-Paths.md
---

# nl2sql #551 Kaniko tip → GHCR → backend tip roll

- After classic PAT with `write:packages` in `nl2sql-ghcr-build`, Kaniko Jobs `nl2sql-kaniko-{backend,mcp}-test-52d0b76` Complete and push `ghcr.io/yoosungung/nl2sql-{backend,mcp}:test-52d0b76`.
- Test tip roll for backend: live `deploy/nl2sql-backend` → `:test-52d0b76`; `/api/health`+`/api/ready` HTTP 200.
- mcp GHCR tip tag exists, but live mcp stays ubuntu+releases binary (overlay private-GHCR path); do not `publish-releases` for `test-*`.
- Fine-grained PAT without packages write fails Kaniko blob upload even when git clone OK — classic/`write:packages` required for Secret.
