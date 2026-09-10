---
id: inbox-ta-k8s-daily-2026-09-10
agent: ta
ticket_id: 
updated: 2026-09-10
status: inbox
sources:
  - schedule:ta-k8s-daily
  - kubectl:read-only
---

# k8s daily 2026-09-10

- Node `didim-gpu` Ready; DiskPressure/MemoryPressure/PIDPressure False; taints none
- Disk ~58% used (999G/1.8T); node mem ~39% (50Gi); CPU ~7%
- Abnormal pods: none; Warning events (recent): none; all PVCs Bound (local-path)
- Intentional scale-0 (empty endpoints, not incidents): `llm-serving/sglang-gemma4-12b`, `runtime/pgbouncer-ro`, `runtime/pgbouncer-rw`
- Active LLM: `sglang-gemma4-31b` 1/1; postgres `postgresql-0` resources limits 4Gi / requests 2Gi, restarts 0
- Actionable incidents: none (no CrashLoop/ImagePull/rollout/PV faults)
- Repo refresh gate: worktree on `feature/775-postgres-memory-4gi` with untracked `.cursor/` etc. — did not `git pull` main
