---
id: in-cluster-kaniko-tip-ghcr
title: "In-cluster Kaniko tip → GHCR (vs Actions build-ghcr)"
status: canonical
owner: km
updated: "2026-08-25"
last_updated: "2026-08-25"
review_after: "2026-11-19"
sources:
  - ticket:551
  - ticket:552
  - ticket:1050
  - https://github.com/GoogleContainerTools/kaniko
tags: ["Infrastructure", "DevOps", "Kaniko", "GHCR", "Kubernetes", "CD"]
type: "wiki"
---

# In-cluster Kaniko tip → GHCR (vs Actions build-ghcr)

공유 클러스터에서 **test tip 이미지**(`test-<sha>`)를 자주 돌릴 때, hosted runner `build-ghcr-images`만 두면 Actions 비용·대기·main-auto 압력이 커진다. tip 공급의 1차 경로는 **in-cluster Kaniko Job → GHCR**, Actions는 `workflow_dispatch` fallback.

## 축 분리

| 경로 | 용도 | 금지 |
| :--- | :--- | :--- |
| Kaniko tip | `test-<sha>` overlay/재스모크 | tip 태그를 Prod package/`publish-releases`로 쓰지 않음 |
| `build-ghcr-images` | semver/Prod 패키지·(옵션) multi-arch | tip 전용 자동 `push:main`을 기본으로 두지 말 것(비용) |
| `publish-releases` | Release asset/README | `test-*` 태그 즉시 fail; Docker 재빌드 없이 사전 GHCR 검증 |

Prod package ≠ 공유 클러스터 apply — [[wiki/Engineering/Infrastructure-and-DevOps/Test-Overlay-vs-Release-Package-Deploy-Paths.md]]. Feature Done 증거에 `prod_* = N/A (package out of scope)`가 정상일 수 있다.

## 클러스터 전제

```bash
# 개념
# Secret: github-token + Docker config.json → /kaniko/.docker/
# SA: batch/jobs create·delete in app NS
./build-tip-images-kaniko.sh <test-sha> <ref>
```

- Executor 핀 예: `gcr.io/kaniko-project/executor:v1.23.2` (upstream archive → Chainguard/self-build 기술부채).
- context는 `dir://` 등 tar extract 면이 좁은 방식 선호.
- GHCR: PAT Contents OK ≠ Packages Write; Actions `packages:write` ≠ 패키지 Manage ACL — [[wiki/Engineering/Infrastructure-and-DevOps/GHCR-Actions-Package-Write-ACL.md]], [[wiki/Engineering/Infrastructure-and-DevOps/GitHub-Fine-Grained-PAT-Contents-Write-Probe.md]].

## Multi-arch

Prod/Apple Silicon용 backend `amd64+arm64`는 **opt-in** (`backend_multi_arch=true` → `linux/amd64,linux/arm64`, QEMU on ubuntu-latest). tip 기본은 `linux/amd64`. sidecar/MCP 이미지는 multi-arch 비목표(amd64). 증거: `docker buildx imagetools inspect ghcr.io/<owner>/<img>:<tag>`.

## SHA ref 체크아웃

스톡 스크립트가 `git clone --branch <ref>`이면 **커밋 SHA를 `--branch`에 넣으면 Init:Error**다. tip Job의 git-ref는 **브랜치명**(예: `main`)을 쓰고, 태그만 `test-<short_sha>`로 맞춘다. one-shot이 특정 커밋을 강제해야 하면 `git fetch origin <sha> && git checkout <sha>`. backend-only 델타면 MCP Kaniko Job을 생략하고 퍼블리시 바이너리 핀은 유지 — [[wiki/Engineering/Infrastructure-and-DevOps/Tip-Roll-Keep-Published-Binary.md]].

## AA 스코프

`quality.yaml`에 `security.command` 없으면 mechanical skip + Kaniko/Secret 경로 수동 리뷰. ConfigMap에 API 키 잔여는 **사전 존재 Forbidden 패턴**으로 NF follow-up — tip 게이트 fail과 분리.

## Backend tip_roll 배포 및 RBAC

테넌트 환경에서 백엔드 변경 사양을 클러스터에 반영할 때, Deployment 패치와 권한 분리에 관한 규칙.

1. **Kaniko 빌드 및 롤 권한**:
   - TA SA (`cursor-agent-test-ns-write` 등) 권한은 `nl2sql` 네임스페이스 내에서 Jobs를 생성/삭제하고 Deployments를 패치할 수 있는 RBAC 권한이 필요하다.
   - 동기화된 테넌트 체크아웃에서 `./deploy/scripts/build-tip-images-kaniko.sh test-<short> main` 을 실행하여 `test-<short>` 이미지 빌드를 수행한다.
2. **`tip_roll` 제한 (mcp 핀 보호)**:
   - 빌드가 완료되면 **백엔드만** 해당 `ghcr.io/yoosungung/nl2sql-backend:test-<short>` 이미지로 롤링 업데이트를 수행한다.
   - **mcp Deployment는 `test-*` 이미지로 덮어쓰지 말 것** (Init:Error 위험 및 verify.md 오동작 방지). mcp는 이전의 안정적인 팁 핀(prior tip pin) 상태로 둔다.
3. **완료 게이트 (Done Gate)**:
   - 해당 기능 구현(Done)의 배포 게이트 완료 조건은 제품의 팁 이미지 SHA가 병합 커밋(예: PR #115의 `53a45e1`)을 포함하는 상태여야 한다. (메타데이터 git head의 SHA와는 무관함)
   - `/api/ready` 가 200 성공 응답을 주어야 배포 완료로 판단한다.

## 🔗 관련 문서

- [[wiki/Engineering/Infrastructure-and-DevOps/GHCR-Actions-Package-Write-ACL.md]]
- [[wiki/Engineering/Infrastructure-and-DevOps/Test-Overlay-vs-Release-Package-Deploy-Paths.md]]
- [[wiki/Engineering/Infrastructure-and-DevOps/Tip-Roll-Keep-Published-Binary.md]]
- [[wiki/Engineering/AI-Native-Engineering/Tenant-Quality-Yaml-Gate-Skip-Pattern.md]]
