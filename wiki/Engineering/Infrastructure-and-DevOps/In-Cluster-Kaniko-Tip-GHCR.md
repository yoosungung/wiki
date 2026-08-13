---
id: in-cluster-kaniko-tip-ghcr
title: "In-cluster Kaniko tip → GHCR (vs Actions build-ghcr)"
status: canonical
owner: km
updated: "2026-08-13"
last_updated: "2026-08-13"
review_after: "2026-11-12"
sources:
  - ticket:551
  - ticket:552
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

스톡 스크립트가 `git clone --branch <ref>`이면 **커밋 SHA**는 실패한다. one-shot Job은 `git fetch origin <sha> && git checkout <sha>`. backend-only 델타면 MCP Kaniko Job을 생략하고 퍼블리시 바이너리 핀은 유지 — [[wiki/Engineering/Infrastructure-and-DevOps/Tip-Roll-Keep-Published-Binary.md]].

## AA 스코프

`quality.yaml`에 `security.command` 없으면 mechanical skip + Kaniko/Secret 경로 수동 리뷰. ConfigMap에 API 키 잔여는 **사전 존재 Forbidden 패턴**으로 NF follow-up — tip 게이트 fail과 분리.

## 🔗 관련 문서

- [[wiki/Engineering/Infrastructure-and-DevOps/GHCR-Actions-Package-Write-ACL.md]]
- [[wiki/Engineering/Infrastructure-and-DevOps/Test-Overlay-vs-Release-Package-Deploy-Paths.md]]
- [[wiki/Engineering/Infrastructure-and-DevOps/Tip-Roll-Keep-Published-Binary.md]]
- [[wiki/Engineering/AI-Native-Engineering/Tenant-Quality-Yaml-Gate-Skip-Pattern.md]]
