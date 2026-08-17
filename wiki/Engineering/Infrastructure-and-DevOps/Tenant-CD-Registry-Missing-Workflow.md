---
id: tenant-cd-registry-missing-workflow
title: "tenant_cd 레지스트리 workflow 부재 시 대체 CD 금지"
status: canonical
owner: km
updated: "2026-08-17"
last_updated: "2026-08-17"
review_after: "2026-11-17"
sources:
  - ticket:918
  - ticket:920
  - schedule:ta-load-weekly
tags: ["Infrastructure", "DevOps", "tenant_cd", "GitHub-Actions", "CD"]
type: "wiki"
---

# tenant_cd 레지스트리 workflow 부재 시 대체 CD 금지

테넌트 CD 레지스트리(`tenant-cd-registry` / `tenant_cd`)가 `workflow: deploy.yml` + `image_input: image_tag`를 가리키는데 제품 `main`에 해당 워크플로가 없으면, tip 경로(`build-ghcr-images` + kubectl overlay)로 **대체 디스패치하지 않는다**.

## 계약 vs tip 경로

| 축 | 내용 | TA 행동 |
| :--- | :--- | :--- |
| **Registry contract** | `workflow_dispatch` 대상 파일명·input 키·verify ns/deploy | 파일 없거나 input 불일치 → Blocked + 인간/플랫폼 |
| **Product tip path** | 예: `build-ghcr-images.yml` + `tag=test-<sha>` + `overlays/test` | 레지스트리와 **다른 축** — 계약 대체로 쓰지 않음 |
| **Publish only** | `ci.yml` / `publish-releases.yml` | 클러스터 apply 아님 — [[wiki/Engineering/Infrastructure-and-DevOps/Test-Overlay-vs-Release-Package-Deploy-Paths.md]] |

```bash
# 개념 프로브
gh workflow list --repo <owner/repo>
gh workflow run deploy.yml --repo <owner/repo> -f image_tag=test-<sha>
# → "workflow … not found on the default branch" 이면 계약 미충족
```

## 운영 규칙

1. `gh workflow run <registry.workflow>` 실패(파일 없음) → **대체 workflow를 발명하지 않음**.
2. tip 이미지 빌드/오버레이 문서가 있어도 registry `workflow`·`image_input`과 키가 다르면 **동일 CD로 취급하지 않음**.
3. 해소: (a) 제품에 registry와 맞는 `workflow_dispatch` 추가, 또는 (b) registry를 실제 존재하는 워크플로/input으로 정정 — 둘 다 인간/플랫폼 결정.
4. Deploying Test는 계약 정합 전까지 Blocked 유지. dual-loop `test_*`는 계약 수정 후에만.

## 적용 체크

1. registry의 `workflow`·`image_input`이 default branch에 존재하는가?
2. tip 경로를 “임시 CD”로 쓰고 있지 않은가?
3. Blocked 사유가 제품 버그가 아니라 **레지스트리↔레포 계약**인가?

## 🔗 관련 문서

- [[wiki/Engineering/Infrastructure-and-DevOps/Test-Overlay-vs-Release-Package-Deploy-Paths.md]]
- [[wiki/Engineering/Infrastructure-and-DevOps/In-Cluster-Kaniko-Tip-GHCR.md]]
- [[wiki/Engineering/AI-Native-Engineering/Tenant-Quality-Yaml-Gate-Skip-Pattern.md]]
- [[wiki/Engineering/AI-Native-Engineering/Wiki-Synthesis-Policy.md]]
