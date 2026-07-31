---
id: k8s-secret-vs-configmap-deploy-hardening
title: "K8s Secret vs ConfigMap 배포 하드닝"
status: canonical
owner: km
updated: "2026-07-31"
last_updated: "2026-07-31"
review_after: "2026-10-31"
sources:
  - ticket:61
tags: ["Infrastructure", "DevOps", "Kubernetes", "Secret", "Security", "Overlay"]
type: "wiki"
---

# K8s Secret vs ConfigMap 배포 하드닝

공유 클러스터 앱 배포에서 **토큰·바이패스 플래그를 ConfigMap에 두면** 공개 Ingress와 결합해 인증 우회가 된다. Secret-only + scrubber + 이미지 pin 패턴.

## 규칙

| 넣을 곳 | 내용 |
| :--- | :--- |
| **Secret** + `envFrom.secretRef` | 공유 토큰, 자격 증명 |
| **ConfigMap** | 비민감 설정만 |
| **금지** | CM에 `*_TOKEN`, `*_DEV_USER` 등 신원 바이패스 키 |

## Apply 후 scrubber

Strategic-merge overlay가 예전 CM 키를 남길 수 있다. `apply` 스크립트에서:

1. Secret 로테이션
2. Overlay apply
3. CM에서 금지 키(`MCP_SHARED_TOKEN`, `NL2SQL_DEV_*` 등) **명시 삭제**

```bash
# 개념: apply 직후 잔존 키 제거
kubectl -n <ns> get cm <config> -o jsonpath='{.data}' | grep -E 'TOKEN|DEV_' && echo FAIL
kubectl -n <ns> get deploy <app> -o yaml | grep -A2 secretRef
```

## AA / 스모크 체크리스트

- `/api/ready` 200
- 비인증 `POST /api/chat` · `GET /api/conversations` → **401**
- initContainer/이미지 **sha256 pin** (릴리스 바이너리)
- 공개 Ingress만으로 신원 우회되지 않음 (앱 게이트 또는 oauth2-proxy)

## 경합

보안 재검사와 라이브 리미디에이션이 동시에 돌면, 중간 스냅샷으로 FAIL이 난다. **리미디에이션 완료 후 recheck**를 게이트로 둔다.

## 🔗 관련 문서

- [[wiki/Engineering/Infrastructure-and-DevOps/Test-Overlay-vs-Release-Package-Deploy-Paths.md]]
- [[wiki/Engineering/AI-Native-Engineering/Playwright-Frontend-UI-Smoke-Pattern.md]]
