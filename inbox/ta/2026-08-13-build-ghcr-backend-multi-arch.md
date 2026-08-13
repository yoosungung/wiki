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

# build-ghcr-images backend multi-arch (Mode B) — Done

- `build-ghcr-images.yml` tip 기본 backend `linux/amd64`; Prod/semver는 `backend_multi_arch=true` → `linux/amd64,linux/arm64` (QEMU on ubuntu-latest).
- mcp 이미지는 multi-arch 비목표(항상 amd64).
- Merged: PR#75 @ `cc9d95d20b15fa185b2c1ed2262280da28750130` (2026-08-13).
- tenant_cd Deploying Test/QA/AA/Prod = N/A (workflow/docs/manifest only; no tip/prod roll).
- Feature Done on Review→Done axis when tenant_cd path absent (Test-Overlay wiki).
