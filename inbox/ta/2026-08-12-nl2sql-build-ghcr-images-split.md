---
id: inbox-ta-nl2sql-build-ghcr-images-split
agent: ta
ticket_id: 549
updated: 2026-08-12
status: inbox
sources:
  - ticket:549
  - wiki/Engineering/Infrastructure-and-DevOps/Test-Overlay-vs-Release-Package-Deploy-Paths.md
---

# nl2sql: Test tip GHCR vs Release publish 워크플로 분리

- Test tip 이미지는 `build-ghcr-images.yml` (`workflow_dispatch` + `tag=test-<sha>`)만 사용 → GHCR → kubectl tip roll.
- `publish-releases.yml`은 `test-*` 태그를 즉시 fail; Docker 재빌드 없이 사전 GHCR 검증 후 Release asset/README만 처리.
- Prod 패키지: `build-ghcr-images` (semver tag) → `publish-releases` 순. 기존 [[wiki/Engineering/Infrastructure-and-DevOps/Test-Overlay-vs-Release-Package-Deploy-Paths.md]] 축과 정합.
