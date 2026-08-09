---
id: inbox-ta-2026-08-09-k8s-daily
agent: ta
ticket_id: 
updated: 2026-08-09
status: inbox
sources:
  - schedule:ta-k8s-daily
  - kubectl:read-only
---

# k8s daily 2026-08-09

- Node `didim-gpu` Ready; DiskPressure/MemoryPressure/PIDPressure False; taints none
- Abnormal pods none; Warning events none; all PV/PVC Bound (local-path)
- `runtime/pgbouncer-{ro,rw}` intentionally scaled 0/0 (endpoints empty) — not incident
- GPU 2/2 allocated to `llm-serving/sglang-gemma4-12b` (2/2 Ready); TEI Ready
- Node metrics ~CPU 9% / mem 45%; no actionable CrashLoop/rollout/PV → Incident tickets: none
