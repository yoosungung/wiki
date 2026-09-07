---
id: inbox-ta-2026-09-07-k8s-daily-health
agent: ta
ticket_id: null
updated: 2026-09-07
status: inbox
sources:
  - schedule:ta-k8s-daily
  - kubectl:read-only
---

# k8s-test 일일 헬스 2026-09-07

- Node `didim-gpu` Ready; DiskPressure/MemoryPressure/PIDPressure=False; root disk ~58% used (996G/1.8T).
- All desired Deploy/STS ready; no Pending/Failed pods; Warning events empty; all PVCs Bound (local-path).
- `postgres/postgresql-0` resources live as limits 4Gi / requests 2Gi (OOM runbook target).
- Watch: `nebula/nebula-storaged-0` lastState OOMKilled (2026-09-05), now Ready, restartCount=4 — not CrashLoop; no ticket this run.
- Scaled-to-0 (intentional): `llm-serving/sglang-gemma4-12b`, `runtime/pgbouncer-ro|rw`.
- Worktree note: k8s-test on `feature/775-postgres-memory-4gi` (untracked .cursor/.kube/.mcp.json); did not auto-pull main.
