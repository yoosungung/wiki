---
id: inbox-ta-2026-09-17-k8s-daily-report
agent: ta
ticket_id: none
updated: 2026-09-17
status: inbox
sources:
  - schedule:ta-k8s-daily
  - wiki/Engineering/Infrastructure-and-DevOps/K8s-Intentional-Scale-Zero-Empty-Endpoints.md
  - wiki/Engineering/Infrastructure-and-DevOps/path-graph-Argo-ImagePullBackOff-runbook.md
  - wiki/Models/Optimization-and-Serving/SGLang-gemma4-llm-serving-cluster-ops.md
  - https://kubernetes.io/docs/concepts/scheduling-eviction/node-pressure-eviction/
---

# ta-k8s-daily 2026-09-17

- Node `didim-gpu` Ready; Disk/Memory/PIDPressure=False; taint 없음; CPU ~7% / mem ~42%(54Gi).
- CrashLoop/ImagePull/Pending/Warning events=0; Deploy·STS ready 불일치 없음; PVC 전부 Bound(local-path).
- `postgres/postgresql-0` live resources limits.memory=4Gi requests=2Gi, restarts=0.
- allowlist empty endpoints: `llm-serving/sglang-gemma4-12b`·`runtime/pgbouncer-{ro,rw}` scale 0/0 (의도적).
- 활성 LLM: `sglang-gemma4-31b` 1/1; path-graph filestash 1/1 + terminal Workflow CR만 잔존 → 위생, incident 아님.
- Actionable incident tickets: none. Mutate 없음(read-only). Worktree `feature/775-postgres-memory-4gi` untracked → git pull 생략.
