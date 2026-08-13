---
id: rwo-pvc-recreate-deploy-strategy
title: "RWO PVC 워크로드는 Recreate 전략"
status: canonical
owner: km
updated: "2026-08-13"
last_updated: "2026-08-13"
review_after: "2026-11-13"
sources:
  - ticket:590
tags: ["Infrastructure", "DevOps", "Kubernetes", "PVC"]
type: "wiki"
---

# RWO PVC 워크로드는 Recreate 전략

ReadWriteOnce PVC를 마운트한 Deployment에 **RollingUpdate**를 쓰면 surge Pod가 같은 볼륨을 이중 마운트하려다 Pending/Timeout이 난다. MCP 메타데이터·Git worktree처럼 **단일 writer**가 전제인 워크로드는 `strategy: Recreate`가 기본이다.

```yaml
spec:
  strategy:
    type: Recreate
```

롤아웃 중 Available=0이 잠깐 생긴다. 구 Ready replica를 남긴 채 새 RS만 Error로 두면 서비스는 살아 있어도 **새 핀은 영원히 안 뜬다** — Init 404·auth replay와 별도로 RS 상태를 본다.

## 관련

- [[wiki/Engineering/Infrastructure-and-DevOps/Tip-Roll-Keep-Published-Binary.md]]
- [[wiki/Engineering/Infrastructure-and-DevOps/Metadata-Git-PVC-Resync.md]]
- [[wiki/Engineering/Infrastructure-and-DevOps/Test-Overlay-vs-Release-Package-Deploy-Paths.md]]
