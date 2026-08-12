---
id: inbox-ta-nl2sql-backend-multi-arch-intake
agent: ta
ticket_id: 552
updated: 2026-08-12
status: inbox
sources:
  - ticket:552
  - ticket:549
  - wiki/Engineering/Infrastructure-and-DevOps/Test-Overlay-vs-Release-Package-Deploy-Paths.md
  - wiki/Engineering/Infrastructure-and-DevOps/GHCR-Actions-Package-Write-ACL.md
  - https://docs.docker.com/build/ci/github-actions/multi-platform/
---

# nl2sql: backend GHCR multi-arch follow-up (#552)

- #549 lands `build-ghcr-images` backend as `linux/amd64` only; #552 extends backend to amd64+arm64 manifest (mcp stays amd64).
- Prefer opt-in `workflow_dispatch` multi-arch for Prod/Apple Silicon; keep tip amd64-default to avoid QEMU tip latency (alt: always-on QEMU or native arm matrix).
- Manifest evidence: `docker buildx imagetools inspect ghcr.io/yoosungung/nl2sql-backend:<tag>`; GHCR ACL still [[wiki/Engineering/Infrastructure-and-DevOps/GHCR-Actions-Package-Write-ACL.md]].
