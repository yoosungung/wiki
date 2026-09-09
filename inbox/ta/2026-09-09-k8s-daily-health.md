---
id: inbox-ta-2026-09-09-k8s-daily-health
agent: ta
ticket_id: 
updated: 2026-09-09
status: inbox
sources:
  - schedule:ta-k8s-daily
  - kubectl:read-only
---

# k8s-test daily health 2026-09-09

- Node `didim-gpu` Ready; DiskPressure/MemoryPressure False; root fs ~58% used (999G/1.8T).
- No CrashLoop/ImagePull/Pending pods; Warning events empty; all PVCs Bound (local-path).
- postgres/postgresql-0 Running with limits memory 4Gi / requests 2Gi (OOM runbook target).
- Intentional scale-0: llm-serving/sglang-gemma4-12b, runtime/pgbouncer-ro|rw (empty Endpoints).
- GPU: 2/2 allocated to sglang-gemma4-31b; bge-m3-tei Ready.
