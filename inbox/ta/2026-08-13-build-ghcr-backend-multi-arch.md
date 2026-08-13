---
id: inbox-ta-build-ghcr-backend-multi-arch
agent: ta
ticket_id: 552
updated: 2026-08-13
status: inbox
sources:
  - ticket:552
  - https://github.com/yoosungung/nl2sql/pull/75
  - wiki/Engineering/Infrastructure-and-DevOps/In-Cluster-Kaniko-Tip-GHCR.md
  - wiki/Engineering/Infrastructure-and-DevOps/Test-Overlay-vs-Release-Package-Deploy-Paths.md
---

# build-ghcr-images backend multi-arch (Mode B)

- `build-ghcr-images.yml` tip 기본은 backend `linux/amd64`; Prod/semver는 `backend_multi_arch=true`로 `linux/amd64,linux/arm64` (QEMU on ubuntu-latest).
- mcp 이미지는 multi-arch 비목표(항상 amd64).
- Kaniko tip 경로와 분리: tip 속도는 Kaniko/amd64; Actions multi-arch는 package fallback.
