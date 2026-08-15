---
id: k8s-intentional-scale-zero-empty-endpoints
title: "K8s 의도적 scale-0와 empty endpoints 판별"
status: canonical
owner: km
updated: "2026-08-15"
last_updated: "2026-08-15"
review_after: "2026-11-15"
sources:
  - schedule:ta-k8s-daily
  - inbox:ta/2026-08-15-k8s-daily-report
  - inbox:ta/2026-08-09-k8s-daily-report
  - inbox:ta/2026-08-03-ta-k8s-daily
  - inbox:ta/2026-08-02-ta-k8s-daily
tags: ["Infrastructure", "DevOps", "Kubernetes", "SRE", "HealthCheck"]
type: "wiki"
---

# K8s 의도적 scale-0와 empty endpoints 판별

공유 클러스터 일일 점검에서 **NotReady / empty endpoints**를 무조건 사고로 올리면 소음이 난다. 의도적 scale-0과 비정상 중단을 분리하는 체크리스트.

## 판별 축

| 신호 | 의도적 scale-0 | 비정상 |
| :--- | :--- | :--- |
| Deploy/STS `replicas` | 명시 `0` (또는 HPA min=0) | 원하던 replicas>0인데 Ready=0 |
| Service endpoints | empty **이고** owner가 scale-0 | empty인데 desired>0 / selector mismatch |
| 최근 이벤트 | scale 이벤트·런북 주석 | CrashLoop / ImagePull / OOM |
| PVC / DiskPressure | Bound, Pressure=False | Pending·Pressure |

## 점검 순서 (읽기 전용)

```bash
# 1) Ready가 아닌 Pod만 (Succeeded 제외)
kubectl get pods -A --field-selector=status.phase!=Running,status.phase!=Succeeded

# 2) Deploy/STS ready 비율 — scale-0은 READY 0/0으로 정상일 수 있음
kubectl get deploy,sts -A

# 3) empty endpoints가 scale-0과 짝인지
kubectl get endpoints -A | awk 'NF<3 || /<none>/'
# → 해당 Service의 owner Deploy replicas 확인

# 4) 노드 Pressure
kubectl get nodes -o custom-columns=NAME:.metadata.name,READY:.status.conditions[?\(@.type==\"Ready\"\)].status,DISK:.status.conditions[?\(@.type==\"DiskPressure\"\)].status
```

## 운영 규칙

1. **스케일 0 allowlist**: 런타임 버퍼(예: 읽기/쓰기 프록시 풀)처럼 의도적으로 끈 워크로드는 체크리스트에 이름을 적어 두고, 일일 리포트에서 “abnormal”에서 제외한다.
2. **Endpoints만 보고 티켓 금지**: empty endpoints는 replicas·selector·엔드포인트 슬라이스를 같이 본다.
3. **잔여 CR ≠ 사고**: Argo 등 컨트롤러의 terminal Failed/Succeeded CR이 남아 있어도 Pod Ready와 무관할 수 있다 — [[wiki/Engineering/Infrastructure-and-DevOps/path-graph-Argo-ImagePullBackOff-runbook.md]] 위생 절 참고. 정리 시 Pod가 아니라 **워크플로/CR 단위** delete.
4. **kubectl은 점검 시 read-only**를 기본으로 한다. 변경은 별도 승인·런북.

## 예시 (패턴 적용)

- GPU 서빙 NS에서 주 워크로드 Ready(예: 2/2)인데, 같은 클러스터의 프록시 Deploy가 `replicas: 0`이면 empty endpoints는 허용.
- 신규 NS가 Running·PVC Bound이면 “새 NS” 자체는 사고가 아니다. CrashLoop/Pending만 올린다.
- **재확인 (2026-08-03)**: 노드 Pressure=False·CrashLoop/ImagePull=0·PVC Bound인 날에도 런타임 프록시 Deploy `replicas=0` → empty endpoints는 allowlist에 두고 abnormal에서 제외. path-graph terminal Workflow CR 잔존도 사고 아님 — [[wiki/Engineering/Infrastructure-and-DevOps/path-graph-Argo-ImagePullBackOff-runbook.md]].
- **재확인 (2026-08-09)**: `runtime/pgbouncer-{ro,rw}` intentional scale-0(endpoints empty) + GPU 서빙 Ready + Warning/CrashLoop=0이면 Incident 없음. TEI 등 보조 Ready 워크로드는 GPU 점유와 독립적으로 정상 기준선에 포함할 수 있다.
- **Redis ClusterIP 거부 ≠ Redis Down**: 워크로드 루프백 `redis-cli ping`이 PONG이면, 오퍼레이터에서 ClusterIP/pod IP connection refused는 알려진 런타임 정책일 수 있다. 일일 리포트에서 Incident로 올리지 않는다.
- **Readiness probe flake**: STS 한 번 Unhealthy 후 곧 Ready 1/1 이면 사고로 승격하지 않는다. 공유 Postgres OOM(SIGKILL)과 구분 — [[wiki/Engineering/Infrastructure-and-DevOps/Shared-Postgres-Cgroup-Limit-vs-Statement-Timeout.md]].
- **재확인 (2026-08-15)**: GPU 서빙 2/2 Ready + `runtime/pgbouncer-{ro,rw}` scale-0 + path-graph filestash 1/1·ImagePullBackOff=0·terminal Workflow CR만 잔존 + 공유 Postgres live limit 4Gi/request 2Gi·SIGKILL 없음이면 Incident 없음.
- **티켓 불필요면 MCP 미사용**: 조치 가능 장애가 0이면 ticketing MCP discovery 실패를 점검 실패로 올리지 않는다. MCP는 티켓이 필요할 때만.

## 🔗 관련 문서

- [[wiki/Engineering/Infrastructure-and-DevOps/path-graph-Argo-ImagePullBackOff-runbook.md]]
- [[wiki/Models/Optimization-and-Serving/SGLang-gemma4-llm-serving-cluster-ops.md]]
- [[wiki/Engineering/Infrastructure-and-DevOps/000_Infrastructure-and-DevOps-MOC.md]]
