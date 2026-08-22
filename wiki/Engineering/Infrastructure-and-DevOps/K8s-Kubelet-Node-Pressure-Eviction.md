---
id: k8s-kubelet-node-pressure-eviction
title: "K8s kubelet 노드 압박·eviction (Memory/Disk/PID)"
status: canonical
owner: km
updated: "2026-08-22"
last_updated: "2026-08-22"
review_after: "2026-11-22"
sources:
  - https://www.k8s.guide/blog/2026-04-01-node-pressure-eviction-kubelet/
  - schedule:ta-k8s-daily
  - inbox:ta/2026-08-22-ta-k8s-daily
tags: ["Infrastructure", "DevOps", "Kubernetes", "kubelet", "SRE", "MemoryPressure"]
type: "wiki"
---

# K8s kubelet 노드 압박·eviction

`kubectl describe node`의 **Pressure=False**는 kubelet eviction이 **아직 발화하지 않았다**는 뜻이지, 스케줄러 allocatable 여유와 동일하지 않다. 스케줄러는 Pod **requests**만 보고, kubelet은 **실측 working set**으로 node-level eviction을 한다.

## 측정 축 (스케줄러 vs kubelet)

| 축 | 기준 | 용도 |
| :--- | :--- | :--- |
| 스케줄러 allocatable | capacity − reserved − eviction-hard | Pod 배치 |
| kubelet `memory.available` | total − working set (live cgroup) | eviction 발화 |

요청 합은 여유인데 실사용이 requests를 크게 넘으면 **allocatable은 충분·MemoryPressure=True**가 동시에 가능하다.

## 임계값 모델

- **Hard**(기본 `memory.available < 100Mi`): grace 없이 즉시 eviction — 프로덕션에서 도달하면 이미 위기.
- **Soft** + `eviction-soft-grace-period`: 지속 압박 확인 후 eviction. `eviction-max-pod-grace-period`로 SIGTERM 상한.
- **`eviction-minimum-reclaim`**: threshold 직상 회복만으로 condition이 깜빡이는 oscillation 방지.

```text
# 16Gi 노드 예시 baseline
--eviction-soft=memory.available<1500Mi,nodefs.available<15%
--eviction-soft-grace-period=memory.available=2m0s,nodefs.available=2m0s
--eviction-max-pod-grace-period=180
--eviction-minimum-reclaim=memory.available=200Mi,nodefs.available=500Mi
```

`kube-reserved`·`system-reserved`를 먼저 맞춘다. 없으면 OS/kubelet이 Pod headroom을 잠식해 soft threshold가 조기 발화한다.

## Eviction 순서

1. QoS: BestEffort → Burstable(실사용/request 초과율) → Guaranteed
2. 동일 QoS 내 **PriorityClass**(낮은 것 먼저) — PriorityClass는 QoS를 override하지 않음
3. **Guaranteed ≠ OOM 면역**: limit 도달 시 kernel OOMKill(137). eviction threshold 튜닝으로는 해결 불가 — limit/request 동시 상향

## Node condition · taint

| 신호 | Condition | Taint |
| :--- | :--- | :--- |
| `memory.available` | MemoryPressure=True | `node.kubernetes.io/memory-pressure:NoSchedule` |
| `nodefs`/`imagefs` | DiskPressure=True | `node.kubernetes.io/disk-pressure:NoSchedule` |
| `pid.available` | PIDPressure=True | `node.kubernetes.io/pid-pressure:NoSchedule` |

**PID pressure**는 기존 Pod eviction 대상이 아니다 — 신규 스케줄만 차단. fork-heavy 워크로드는 별도 진단 필요.

## OOMKill vs eviction vs 일일 점검

| 현상 | 메커니즘 | 일일 리포트 |
| :--- | :--- | :--- |
| 컨테이너 limit 초과 재시작(137) | kernel OOMKill | cgroup limit·Helm values 점검 — [[wiki/Engineering/Infrastructure-and-DevOps/Shared-Postgres-Cgroup-Limit-vs-Statement-Timeout.md]] |
| Node MemoryPressure + Pod Evicted | kubelet eviction | Incident — capacity·request 정확도 |
| Pressure=False·CrashLoop=0 | 정상 기준선 | 의도적 scale-0 empty endpoints는 abnormal 제외 — [[wiki/Engineering/Infrastructure-and-DevOps/K8s-Intentional-Scale-Zero-Empty-Endpoints.md]] |

**재확인 (2026-08-22)**: `didim-gpu` Disk/Memory/PID Pressure=False·CrashLoop/ImagePull/Pending=0이면 kubelet eviction 경로는 미발화. GPU 서빙 2/2·TEI 1/1·postgres live 4Gi/2Gi Ready는 정상 기준선 유지.

## 실패 모드 요약

- **Eviction storm**: evicted Pod 재스케줄이 타 노드 압박 유발. PDB는 involuntary eviction에 무효 — 클러스터 headroom 확보.
- **Wrong pod evicted**: BestEffort/부정확 request가 먼저. Guaranteed(request==limit) + PriorityClass 병행.
- **emptyDir/nodefs**: 대용량 scratch는 `sizeLimit`(1.28+) 또는 PV. **imagefs** stale image는 nodefs와 별도 임계.
- **Eviction loop**: 전 노드 pressured → Pod가 어디서도 안정화 못 함 — capacity expansion이 정답.

## 모니터링

- `kubelet_evictions_total` 증가 — eviction 발화 확인
- node conditions + `memory_working_set_bytes` — soft threshold 전 조기 경보
- `kubectl top pods -A --sort-by=memory` vs requests — 80% 이상 지속 시 request 조정 후보

## 🔗 관련 문서

- [[wiki/Engineering/Infrastructure-and-DevOps/K8s-Intentional-Scale-Zero-Empty-Endpoints.md]]
- [[wiki/Engineering/Infrastructure-and-DevOps/Shared-Postgres-Cgroup-Limit-vs-Statement-Timeout.md]]
- [[wiki/Models/Optimization-and-Serving/SGLang-gemma4-llm-serving-cluster-ops.md]]
- [[wiki/Engineering/Infrastructure-and-DevOps/000_Infrastructure-and-DevOps-MOC.md]]
