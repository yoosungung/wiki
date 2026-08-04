---
id: test-overlay-vs-release-package-deploy-paths
title: "Test Overlay vs Release Package 배포 축 분리"
status: canonical
owner: km
updated: "2026-08-04"
last_updated: "2026-08-04"
review_after: "2026-11-04"
sources:
  - ticket:59
  - ticket:61
  - ticket:116
  - ticket:60
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

## GHCR publish ACL

Actions `packages: write`만으로 부족할 수 있다 — [[wiki/Engineering/Infrastructure-and-DevOps/GHCR-Actions-Package-Write-ACL.md]].

## Doc smoke

배포 문서 마커 + `kubectl` client dry-run을 스크립트로 고정한다 (예: `verify-deploy-docs.sh`).

## 🔗 관련 문서

- [[wiki/Engineering/Infrastructure-and-DevOps/K8s-Secret-vs-ConfigMap-Deploy-Hardening.md]]
- [[wiki/Engineering/Infrastructure-and-DevOps/GHCR-Actions-Package-Write-ACL.md]]
- [[wiki/Engineering/AI-Native-Engineering/Playwright-Frontend-UI-Smoke-Pattern.md]]
- [[wiki/Engineering/AI-Native-Engineering/In-Process-ASGI-Load-Harness-Pattern.md]]
- [[wiki/Models/Optimization-and-Serving/SGLang-gemma4-llm-serving-cluster-ops.md]]
