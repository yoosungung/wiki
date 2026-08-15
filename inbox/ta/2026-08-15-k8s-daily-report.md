---
id: inbox-ta-2026-08-15-k8s-daily-report
agent: ta
ticket_id: none
updated: 2026-08-15
status: inbox
sources:
  - schedule:ta-k8s-daily
  - wiki/Engineering/Infrastructure-and-DevOps/K8s-Intentional-Scale-Zero-Empty-Endpoints.md
  - wiki/Engineering/Infrastructure-and-DevOps/Shared-Postgres-Cgroup-Limit-vs-Statement-Timeout.md
  - wiki/Models/Optimization-and-Serving/SGLang-gemma4-llm-serving-cluster-ops.md
  - wiki/Engineering/Infrastructure-and-DevOps/path-graph-Argo-ImagePullBackOff-runbook.md
---

# ta-k8s-daily 2026-08-15

- 노드 `didim-gpu` Ready; DiskPressure/MemoryPressure/PIDPressure=False. CPU 8% / mem 42%. GPU allocatable 2 전부 `sglang-gemma4-12b` 2/2 Ready.
- CrashLoop/ImagePull/Pending=0; Warning events=0; PVC 49 Bound / Pending 0.
- `runtime/pgbouncer-{ro,rw}` replicas=0 + empty endpoints는 의도적 scale-0 (incident 아님).
- path-graph: filestash 1/1; ImagePullBackOff=0; terminal Workflow CR만 잔존 (위생, incident 아님).
- 공유 Postgres `postgresql-0` live resources limit 4Gi / request 2Gi; 최근 로그에 SIGKILL/OOM 없음; TCP :5432 OK.
- 조치 가능 장애 없음 → Incident tickets: none. Leantime MCP discovery 실패는 티켓 불필요로 미사용.
