---
id: inbox-ta-nl2sql-551-kaniko-ghcr-packages-write
agent: ta
ticket_id: 551
updated: 2026-08-12
status: inbox
sources:
  - ticket:551
  - wiki/Engineering/Infrastructure-and-DevOps/GHCR-Actions-Package-Write-ACL.md
  - wiki/Engineering/Infrastructure-and-DevOps/GitHub-Fine-Grained-PAT-Contents-Write-Probe.md
---

# #551 Kaniko live: Job RBAC OK, GHCR packages:write missing on Pod token

- After Eric RBAC grant, TA SA can create/delete `batch/jobs` in `nl2sql`; Secret `nl2sql-ghcr-build` created from Pod `GH_TOKEN`.
- Kaniko Jobs `nl2sql-kaniko-{backend,mcp}-test-52d0b76` applied then Failed: GHCR blob upload `DENIED: permission_denied: token does not match expected scopes`.
- Pod fine-grained PAT returns 403 on Packages API (`Resource not accessible by personal access token`) — Contents/git OK ≠ Packages Write (wiki Fine-Grained + GHCR ACL axes).
- Unblock: human puts packages:write-capable token into `nl2sql-ghcr-build` (`github-token` + `config.json`), then re-run `build-tip-images-kaniko.sh test-52d0b76 main`.
