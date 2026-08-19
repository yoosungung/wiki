---
id: tip-roll-keep-published-binary
title: "Tip 롤에서 퍼블리시 바이너리 핀을 유지한다"
status: canonical
owner: km
updated: "2026-08-19"
last_updated: "2026-08-19"
review_after: "2026-11-19"
sources:
  - ticket:590
  - ticket:796
tags: ["Infrastructure", "DevOps", "Kubernetes", "GHCR", "CD", "MCP"]
type: "wiki"
---

# Tip 롤에서 퍼블리시 바이너리 핀을 유지한다

공유 클러스터에서 **앱 이미지 tip**(`test-<sha>`)과 **initContainer가 curl하는 Release 바이너리**는 축이 다르다. tip 태그를 바이너리 URL에 넣으면 `publish-releases`가 `test-*`를 거부해 **HTTP 404 → Init:Error / ProgressDeadlineExceeded**가 난다. 구 Ready replica가 ClusterIP를 계속 서빙하면 “서비스는 산다”처럼 보여 탐지가 늦다.

## 축 분리

| 면 | 허용 태그 | 금지 |
| :--- | :--- | :--- |
| 앱/사이드카 이미지 | `test-<sha>` (Kaniko tip) | tip을 `publish-releases`에 넣기 |
| init fetch URL (`…/v*/binary`, `prod-<sha>`) | semver / `prod-*` + sha256 | `test-*`로 rewrite |

## 절차

```bash
# 개념: tip은 이미지 태그만. 바이너리 핀은 overlay git 값 유지
# set image 대상은 **container 이름**(예: backend) — Deployment 이름과 혼동 금지
kubectl set image deploy/<deploy> <container>=ghcr.io/<org>/<img>:test-<sha>
# mcp-binary / patch-*-binary.yaml 은 v* 핀 그대로
# 복구: overlay 재적용 (git pin이 이미 vX.Y.Z면 URL만 되돌림)
```

backend-only 델타면 sidecar/MCP 이미지·바이너리를 같이 돌리지 않는다(퍼블리시 바이너리 URL을 tip으로 rewrite하면 Init:Error). `apply -k` 전량은 live tip 태그를 overlay 기본값으로 덮을 수 있다. Recreate 롤아웃 중 구 Pod terminating이면 ClusterIP 스모크가 잠깐 실패할 수 있으니 podIP/`/healthz`로 재시도한다.

카탈로그 PUT만으로 EX가 안 바뀌는 수정(식별자 인용 등)은 **퍼블리시된 MCP 바이너리**가 실려야 한다. live test mcp는 published semver를 쓰고 `test-*`를 핀하지 않는다 — [[wiki/Agents/Text-to-SQL/RefSql-Unparser-Identifier-Quoting.md]].

## 관련

- [[wiki/Engineering/Infrastructure-and-DevOps/In-Cluster-Kaniko-Tip-GHCR.md]]
- [[wiki/Engineering/Infrastructure-and-DevOps/Test-Overlay-vs-Release-Package-Deploy-Paths.md]]
- [[wiki/Engineering/Infrastructure-and-DevOps/RWO-PVC-Recreate-Deploy-Strategy.md]]
