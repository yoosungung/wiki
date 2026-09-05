---
id: inbox-ta-2026-09-05-k8s-daily
agent: ta
ticket_id: 
updated: 2026-09-05
status: inbox
sources:
  - schedule:ta-k8s-daily
  - wiki: INDEX.md (Engineering/Infrastructure miss for live cluster ops)
  - https://oneuptime.com/blog/post/2026-02-02-k3s-monitoring/view
---

# k8s daily 2026-09-05

- Node `didim-gpu` Ready; DiskPressure/MemoryPressure/PIDPressure False; no Warning events.
- All PVCs Bound (local-path); postgresql-0 Running with limits 4Gi / requests 2Gi, restarts 0.
- Scaled-to-0 (intentional): llm-serving/sglang-gemma4-12b, runtime/pgbouncer-ro|rw. GPU 2/2 on sglang-gemma4-31b.
- Actionable CrashLoop/rollout/PV incidents: none (no Leantime ticket).
- Repo refresh gate skipped: worktree on `feature/775-postgres-memory-4gi` with local untracked files.
