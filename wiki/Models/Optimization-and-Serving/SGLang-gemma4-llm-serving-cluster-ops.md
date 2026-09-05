---
id: sglang-gemma4-llm-serving-cluster-ops
title: "SGLang Gemma4 llm-serving 클러스터 운영 (12b/31b)"
status: canonical
owner: km
updated: "2026-09-05"
last_updated: "2026-09-05"
review_after: "2026-12-05"
sources:
  - ticket:426
  - ticket:42
  - ticket:1523
  - kubectl:llm-serving
  - schedule:ta-k8s-daily
  - inbox/ta/2026-09-05-k8s-daily-report.md
  - inbox/ta/2026-09-04-k8s-daily.md
  - inbox/candidate/2026-08-31-sglang-gemma4-31b-tier1-smoke.md
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

- 기본 점유(서빙 ON): `sglang` 계열 복제본이 노드 allocatable GPU를 **전량 Ready**로 쓰는 상태를 정상으로 본다(예: 2 GPU → 2/2).
- **서빙 OFF(의도적 scale-0)**: `llm-serving/sglang-gemma4-12b` replicas=0이면 empty endpoints·Ready 0/0은 **정상**. 프록시 풀(`runtime/pgbouncer-{ro,rw}`)과 같은 allowlist 축 — [[wiki/Engineering/Infrastructure-and-DevOps/K8s-Intentional-Scale-Zero-Empty-Endpoints.md]].
- 노드 `DiskPressure`/`MemoryPressure`/`PIDPressure`=False를 (서빙 ON일 때) GPU Ready와 함께 확인한다.
- 보조 추론 서비스(예: TEI) Ready는 GPU 전량 점유와 병행 가능한 정상 신호로 본다(2026-08-09·2026-08-16·2026-08-18·**2026-08-22** 재확인: `bge-m3-tei` 1/1 + `sglang-gemma4-12b` 2/2; `/v1/models` 200).
- **재확인 (2026-08-22)**: 노드 Pressure=False·postgres live 4Gi/request 2Gi Ready — OOM/eviction 경로 없음. [[wiki/Engineering/Infrastructure-and-DevOps/K8s-Kubelet-Node-Pressure-Eviction.md]].
- **재확인 (2026-09-04)**: `sglang-gemma4-12b` + `pgbouncer-{ro,rw}` intentional scale-0 · abnormal Pod/Warning=0 · postgres Ready → Incident 없음(서빙 ON 기준선과 병행 문서화).
- **재확인 (2026-09-05)**: `sglang-gemma4-12b` scale-0 + **`sglang-gemma4-31b` 2/2 Ready**(노드 GPU 전량) + `pgbouncer-{ro,rw}` scale-0. 활성 티어가 31b이면 smoke·클라이언트 FQDN도 31b Service를 본다 — [[#Client env vs live model id drift]]. 12b empty endpoints는 allowlist.
- **TEI health 포트 오탐**: ClusterIP health는 컨테이너/Service listen 포트(예: **:8080**)로 확인한다. 관례적 `:80` 타임아웃만으로 Down/Incident로 올리지 않는다.
- **SGLang smoke 포트**: Service listen이 **:30000**이면 `/v1/models`·tiny completion을 그 포트로 친다. 관례적 `:8000` 타임아웃만으로 사고 취급하지 않는다(TEI `:80` vs `:8080`과 같은 축). 서빙 scale-0이면 smoke 스킵.

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



## Client env vs live model id drift

에이전트/`PVC`에 박힌 `.env`가 **스케일 0·삭제된** 구 Deploy FQDN(예: 12b)을 가리키면 live가 31b를 서빙해도 클라이언트가 실패한다. 정본은 DESIGN/`.env.example`의 현재 Service FQDN·모델 id이며, gitignored env는 코드 기본값과 어긋나면 **env만** 맞춘다(불필요 rollout 금지).

```bash
# 개념: live /v1/models id ↔ 클라이언트 BASE_URL·MODEL 정합
curl -sS http://<svc>.llm-serving.svc.cluster.local:30000/v1/models
# PVC/로컬 .env가 dead Deploy를 가리키면 example 값으로 교정 후 smoke
```

## Git vs live drift (context/fp8)

live Deployment가 이미 `40960`+`fp8_e4m3`인데 git manifest가 `32768`로 남으면 **클러스터 재롤아웃이 아니라 git sync**가 정본이다.

```bash
# 개념: manifest args + verify-sglang.sh MIN=목표 + README를 live와 맞춤
# live 이미 목표면 kubectl rollout 불필요 — drift만 닫는다
```

길이만 올리는 PR은 KV pool < context면 실패한다. 사다리 표(§ Context length)와 [[wiki/Engineering/AI-Native-Engineering/LLM-Tool-Payload-Context-Trim.md]]를 함께 본다.

## 🔗 관련 문서

- [[wiki/Models/Optimization-and-Serving/SGLang LLM 서빙 프레임워크 리뷰.md]]
- [[wiki/Models/Optimization-and-Serving/000_Optimization-and-Serving-MOC.md]]
- [[wiki/Engineering/Infrastructure-and-DevOps/path-graph-Argo-ImagePullBackOff-runbook.md]]
- [[wiki/Engineering/Infrastructure-and-DevOps/K8s-Intentional-Scale-Zero-Empty-Endpoints.md]]
