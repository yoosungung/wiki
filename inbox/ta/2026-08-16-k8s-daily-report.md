---
id: inbox-ta-2026-08-16-k8s-daily-report
agent: ta
updated: 2026-08-16
status: inbox
sources:
  - schedule:ta-k8s-daily
  - wiki/Engineering/Infrastructure-and-DevOps/K8s-Intentional-Scale-Zero-Empty-Endpoints.md
  - wiki/Engineering/Infrastructure-and-DevOps/Shared-Postgres-Cgroup-Limit-vs-Statement-Timeout.md
  - wiki/Models/Optimization-and-Serving/SGLang-gemma4-llm-serving-cluster-ops.md
---

# ta-k8s-daily 2026-08-16

- 노드 `didim-gpu` Ready, Disk/Memory/PID Pressure=False. Warning events 0, CrashLoop/ImagePull/Pending Pod 0.
- `runtime/pgbouncer-{ro,rw}` replicas=0 → empty endpoints는 의도적 scale-0 (allowlist). GPU 서빙 `sglang-gemma4-12b` 2/2 + `bge-m3-tei` 1/1 Ready.
- 공유 Postgres live STS/Pod limit 4Gi / request 2Gi, SIGKILL 로그 없음, metrics ~450Mi. PVC 전부 Bound.
- path-graph filestash 1/1. terminal Workflow CR만 잔존 → 위생 대상, incident 아님.
- 조치 가능 장애 0 → Incident tickets none. ticketing MCP 미사용.
- k8s-test worktree가 `feature/775-postgres-memory-4gi`라 `git pull origin main` 생략. 점검은 live 클러스터 기준.
