---
id: sglang-gemma4-llm-serving-cluster-ops
title: "SGLang Gemma4 llm-serving 클러스터 운영 (12b/31b)"
status: canonical
owner: km
updated: "2026-07-30"
last_updated: "2026-07-30"
review_after: "2026-08-30"
sources:
  - ticket:42
  - kubectl:llm-serving
tags: ["Models", "Serving", "SGLang", "Kubernetes", "Gemma4", "GPU"]
type: "wiki"
---

# SGLang Gemma4 llm-serving 클러스터 운영

티켓 #42 — `didim-gpu` 노드의 SGLang Gemma4 12b/31b 배치·삭제·GPU 경합 기록.

## 노드·용량

- Node `didim-gpu` Ready; DiskPressure=False; allocatable `nvidia.com/gpu=2`.
- `sglang-gemma4-12b` ×2 Running(각 1 GPU)이 기본 점유 → 31b(요청 GPU=2)는 Pending 가능.

## 31b 삭제 closeout (2026-07-30)

Eric 지시: 클러스터에서 31b 제거, **레포 소스 유지** (`manifests/apps/sglang-gemma4-31b.yaml`).

```bash
kubectl delete deployment sglang-gemma4-31b -n llm-serving
# 초기 leftover: Service sglang-gemma4-31b (empty endpoints)
# SA sw-factory:cursor-agent 는 services 삭제 Forbidden → Eric/RBAC로 Service 정리
```

- Closeout 확인: `llm-serving`에 `sglang-gemma4-31b` Deploy/Svc/Pod/Ingress/PVC 없음(Eric이 leftover Service 삭제).
- 12b는 2/2 Running 유지. ops-only — git-ship/PR 없음.

## GPU 경합 교훈

| 워크로드 | GPU 요청 | 상태(삭제 전) |
| :--- | :--- | :--- |
| 12b ×2 | 1+1 | Running |
| 31b ×1 | 2 | Pending(~23d) — 노드 allocatable=2 전량 12b 점유 |

31b를 다시 올릴 때는 12b 스케일을 먼저 줄이거나 노드 GPU를 늘린다.

## 🔗 관련 문서

- [[wiki/Models/Optimization-and-Serving/SGLang LLM 서빙 프레임워크 리뷰.md]]
- [[wiki/Models/Optimization-and-Serving/000_Optimization-and-Serving-MOC.md]]
- [[wiki/Engineering/Infrastructure-and-DevOps/path-graph-Argo-ImagePullBackOff-runbook.md]]
