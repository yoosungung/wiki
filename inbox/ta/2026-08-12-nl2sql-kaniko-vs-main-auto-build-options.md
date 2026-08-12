---
id: inbox-ta-nl2sql-kaniko-vs-main-auto-build-options
agent: ta
ticket_id: 551
updated: 2026-08-12
status: inbox
sources:
  - ticket:551
  - ticket:549
  - wiki/Engineering/Infrastructure-and-DevOps/Test-Overlay-vs-Release-Package-Deploy-Paths.md
  - wiki/Engineering/Infrastructure-and-DevOps/GHCR-Actions-Package-Write-ACL.md
  - https://oneuptime.com/blog/post/2026-02-08-how-to-choose-between-kaniko-and-docker-build-in-cicd/view
  - https://computingforgeeks.com/build-container-images-using-kaniko-in-kubernetes/
---

# nl2sql tip 이미지: Kaniko vs main auto build-ghcr

- #551 후속: Test tip 경로를 hosted runner-only에 두지 않으려면 (A) `build-ghcr-images`에 `push:main` 자동 트리거 또는 (B) in-cluster Kaniko Job → GHCR/노드. #549 SoT 워크플로가 먼저 존재해야 문서·구현 가능.
- Actions 환경에서는 Buildx/BuildKit이 기본 권장; Kaniko는 Docker daemon/privileged 불가한 클러스터 빌드용. Google Kaniko upstream 2025-06 archive → Chainguard fork 추적 필요(k8s-test `gcr.io/kaniko-project/executor` 패턴 재검토).
- GHCR push는 `packages:write`만으로 부족할 수 있음 — Manage Actions access Write ([[wiki/Engineering/Infrastructure-and-DevOps/GHCR-Actions-Package-Write-ACL.md]]).
