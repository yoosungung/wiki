---
id: inbox-pm-nl2sql-552-backend-multi-arch-intake
agent: pm
ticket_id: 552
updated: 2026-08-12
status: inbox
sources:
  - ticket:552
  - ticket:549
  - https://github.com/yoosungung/nl2sql/pull/62
  - wiki/Engineering/Infrastructure-and-DevOps/Test-Overlay-vs-Release-Package-Deploy-Paths.md
  - wiki/Engineering/Infrastructure-and-DevOps/GHCR-Actions-Package-Write-ACL.md
---

# nl2sql #552 backend multi-arch PM intake

- Decide **opt-in** (`backend_platforms` / `backend_multi_arch`, default off) for `build-ghcr-images` backend so tip `test-*` stays amd64-fast; Prod turns multi-arch on when needed.
- Do **not** stack #552 on #549 while PR #62 is changes-requested / not on main; unblock → In Progress only after #549 Done (workflow on main).
- Multi-arch push reuses same GHCR package ACL (wiki GHCR-Actions-Package-Write-ACL); tip vs Release package axes unchanged (Test-Overlay-vs-Release-Package).
