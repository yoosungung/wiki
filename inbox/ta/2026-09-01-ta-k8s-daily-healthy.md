---
id: inbox-ta-2026-09-01-k8s-daily-healthy
agent: ta
ticket_id: none
updated: 2026-09-01
status: inbox
sources:
  - schedule:ta-k8s-daily
  - wiki/Engineering/Infrastructure-and-DevOps/K8s-Intentional-Scale-Zero-Empty-Endpoints.md
  - wiki/Models/Optimization-and-Serving/SGLang-gemma4-llm-serving-cluster-ops.md
  - https://k8s.guide/blog/2026-04-01-node-pressure-eviction-kubelet/
---

# ta-k8s-daily 2026-09-01 healthy

- Node `didim-gpu` Ready; DiskPressure/MemoryPressure/PIDPressure=False; taints none; root fs ~58% used.
- Abnormal pods / Warning events / unbound PVC: none. CrashLoop/ImagePull/rollout stuck: none → Incident tickets none.
- Intentional scale-0 empty endpoints (not incidents): `runtime/pgbouncer-{ro,rw}` 0/0; `llm-serving/sglang-gemma4-12b` 0/0. Active GPU serve: `sglang-gemma4-31b` 1/1 (~25Gi RSS) + `bge-m3-tei` 1/1.
- `postgres/postgresql-0` live resources match ticket #775 values: limits 4Gi / requests 2Gi; Running 0 restarts.
- Repo gate: worktree on `feature/775-postgres-memory-4gi` with local untracked `.cursor`/`.kube`/`.mcp.json` — skipped `git pull` main (read-only inspect still OK).
