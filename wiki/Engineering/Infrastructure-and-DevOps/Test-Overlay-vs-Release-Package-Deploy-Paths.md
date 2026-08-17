---
id: test-overlay-vs-release-package-deploy-paths
title: "Test Overlay vs Release Package 배포 축 분리"
status: canonical
owner: km
updated: "2026-08-17"
last_updated: "2026-08-17"
review_after: "2026-11-17"
sources:
  - ticket:59
  - ticket:61
  - ticket:116
  - ticket:60
  - ticket:172
  - ticket:176
  - ticket:551
  - ticket:552
tags: ["Infrastructure", "DevOps", "Kubernetes", "GHCR", "CD", "RBAC"]
type: "wiki"
---

# Test Overlay vs Release Package 배포 축 분리

“Prod”를 런타임 클러스터와 동일시하면 스코프가 꼬인다. **테스트 오버레이**와 **릴리스 패키지 퍼블리시**를 축으로 분리한다.

## 두 축

| 축 | 의미 | 전형 산출 |
| :--- | :--- | :--- |
| **Test** | 공유 클러스터 NS + kustomize/helm overlay | Ingress host, in-cluster health/ready, QA e2e |
| **Prod package** | Release assets + GHCR 이미지/바이너리 publish | `publish-releases` workflow, 패키지 레포 — **반드시 클러스터 apply는 아님** |

테넌트 레지스트리(`tenant_cd`)가 비어 있으면 workflow_dispatch CD 경로가 없다 → 해당 티켓의 **prod_* = N/A**가 정상이다.

레지스트리가 `deploy.yml` 등을 가리키는데 제품 default branch에 파일이 없으면 tip 경로로 대체하지 않는다 — [[wiki/Engineering/Infrastructure-and-DevOps/Tenant-CD-Registry-Missing-Workflow.md]].

팩토리 **플러그인-only** 테스트 배포는 `tenant_cd`가 아니라 install 스크립트(예: ConfigMap + initContainer + `rollout restart deploy/…`)일 수 있다. 재설치 시 live `bridge.json`(에이전트 user id)을 **샘플로 덮지 말고** 기존 CM에서 보존한다. 스모크는 in-cluster Service FQDN(예: `favicon.ico` 200)을 쓰고, 외부 Host 302와 혼동하지 않는다.

## GHCR private → releases 바이너리

익명 `docker pull ghcr.io/...`가 401이면:

- 런타임 이미지를 공개 base(예: `ubuntu:24.04`) + **Release 바이너리 initContainer**로 구성
- 구형 base(bookworm 등)는 GLIBC 부족으로 바이너리 실행 실패 가능 → OS 매트릭스를 맞춘다

## 에이전트 SA RBAC 갭

SA가 NS/CM/Deploy만 만들고 **Service / PVC / Ingress / Secret create 불가**면 Pod가 Pending(볼륨·엔드포인트 없음)으로 남는다. Overlay 적용 전 SA verb 표를 점검한다.

```bash
# 개념 프로브
kubectl auth can-i create pvc -n <ns> --as=system:serviceaccount:<ns>:<sa>
kubectl auth can-i create secret -n <ns> --as=system:serviceaccount:<ns>:<sa>
kubectl auth can-i create ingress -n <ns> --as=system:serviceaccount:<ns>:<sa>
```

## Overlay 재적용 함정 (공유 Secret)

`apply.sh`가 Secret을 **재생성**하면 기존 `MCP_SHARED_TOKEN`(또는 동등 shared secret)이 바뀌어 backend↔mcp가 깨질 수 있다. 토큰이 이미 있으면 **보존**하고 idempotent `-k` apply만 한다. Service 스모크 포트는 문서의 containerPort(예: 8080/8800)를 쓴다 — `80` 가정 금지.

레지스트리 `…/healthz` 호스트가 DNS에 없으면 **in-cluster Service FQDN**(예: `backend.ns.svc.cluster.local:8080`의 `/api/health`·`/api/ready`)으로 검증한다. backend-only 델타면 mcp deploy·MDL PVC reseed를 생략할 수 있다.

## GHCR publish ACL

Actions `packages: write`만으로 부족할 수 있다 — [[wiki/Engineering/Infrastructure-and-DevOps/GHCR-Actions-Package-Write-ACL.md]].

## Tip 이미지 공급 (Kaniko)

빈번한 `test-<sha>` tip은 in-cluster Kaniko → GHCR을 1차로 두고, `build-ghcr-images`는 Prod/semver·opt-in multi-arch fallback으로 둔다. tip 태그를 `publish-releases`에 넣지 않는다 — [[wiki/Engineering/Infrastructure-and-DevOps/In-Cluster-Kaniko-Tip-GHCR.md]]. initContainer 바이너리 URL을 `test-*`로 바꾸면 404 — [[wiki/Engineering/Infrastructure-and-DevOps/Tip-Roll-Keep-Published-Binary.md]]. RWO 메타데이터 PVC는 Recreate — [[wiki/Engineering/Infrastructure-and-DevOps/RWO-PVC-Recreate-Deploy-Strategy.md]].

## Doc smoke

배포 문서 마커 + `kubectl` client dry-run을 스크립트로 고정한다 (예: `verify-deploy-docs.sh`).

## Live pin ↔ Git overlay sha drift

수동 upload 후 `publish-releases`가 **같은 tag asset을 덮어쓰면** live initContainer sha와 overlay `patch-*-binary.yaml` pin이 어긋난다. Live Host-200이어도 git↔live 정합용 re-pin PR이 필요할 수 있다 — 라이브 블로커와 혼동하지 않는다.

MCP Host allowlist 롤아웃 순서는 [[wiki/Engineering/Infrastructure-and-DevOps/MCP-Host-Allowlist-DNS-Rebinding.md]].

## 🔗 관련 문서

- [[wiki/Engineering/Infrastructure-and-DevOps/Tenant-CD-Registry-Missing-Workflow.md]]
- [[wiki/Engineering/Infrastructure-and-DevOps/K8s-Secret-vs-ConfigMap-Deploy-Hardening.md]]
- [[wiki/Engineering/Infrastructure-and-DevOps/GHCR-Actions-Package-Write-ACL.md]]
- [[wiki/Engineering/Infrastructure-and-DevOps/MCP-Host-Allowlist-DNS-Rebinding.md]]
- [[wiki/Engineering/AI-Native-Engineering/Playwright-Frontend-UI-Smoke-Pattern.md]]
- [[wiki/Engineering/AI-Native-Engineering/In-Process-ASGI-Load-Harness-Pattern.md]]
- [[wiki/Models/Optimization-and-Serving/SGLang-gemma4-llm-serving-cluster-ops.md]]
