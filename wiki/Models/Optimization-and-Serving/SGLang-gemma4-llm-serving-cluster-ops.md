---
id: sglang-gemma4-llm-serving-cluster-ops
title: "SGLang Gemma4 llm-serving 클러스터 운영 (12b/31b)"
status: canonical
owner: km
updated: "2026-08-09"
last_updated: "2026-08-09"
review_after: "2026-11-06"
sources:
  - ticket:42
  - kubectl:llm-serving
  - schedule:ta-k8s-daily
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

## 일일 점검 기준선

- 기본 점유: `sglang` 계열 복제본이 노드 allocatable GPU를 **전량 Ready**로 쓰는 상태를 정상으로 본다(예: 2 GPU → 2/2).
- 같은 클러스터의 **의도적 scale-0** Deploy(예: 프록시 풀)가 empty endpoints여도 GPU 서빙 Ready와 무관하면 사고로 올리지 않는다 — [[wiki/Engineering/Infrastructure-and-DevOps/K8s-Intentional-Scale-Zero-Empty-Endpoints.md]].
- 노드 `DiskPressure`/`MemoryPressure`/`PIDPressure`=False를 GPU Ready와 함께 확인한다.
- 보조 추론 서비스(예: TEI) Ready는 GPU 전량 점유와 병행 가능한 정상 신호로 본다(2026-08-09 재확인).

## Context length 사다리 (12b / 1×4090)

API `max_model_len`은 **SGLang `--context-length`**가 결정한다(모델 카드 상한과 혼동 금지).

| 단계 | args | 관측 요지 |
| :--- | :--- | :--- |
| 16K | `--context-length 16384` | 에이전트 도구 페이로드 overflow의 전형적 상한 |
| 32K | `32768`, `mem-fraction-static 0.75` | 16K BadRequest 해소; KV pool≈35k면 **64K 불가** |
| 40K | `40960` + **`--kv-cache-dtype fp8_e4m3`** | `max_total_num_tokens`가 context 이상으로 확보될 때만 |

```bash
# 개념: length만 올리면 KV pool < context → 실패. fp8로 capacity 확보 후 검증
# verify: max_model_len == 목표, smoke prompt_tokens>~18k without BadRequest
```

fp8는 **용량/정밀도 트레이드오프**이지 새 listen/auth surface가 아니다. 제품 쪽 트림과 병행 — [[wiki/Engineering/AI-Native-Engineering/LLM-Tool-Payload-Context-Trim.md]].

## 🔗 관련 문서

- [[wiki/Models/Optimization-and-Serving/SGLang LLM 서빙 프레임워크 리뷰.md]]
- [[wiki/Models/Optimization-and-Serving/000_Optimization-and-Serving-MOC.md]]
- [[wiki/Engineering/Infrastructure-and-DevOps/path-graph-Argo-ImagePullBackOff-runbook.md]]
- [[wiki/Engineering/Infrastructure-and-DevOps/K8s-Intentional-Scale-Zero-Empty-Endpoints.md]]
