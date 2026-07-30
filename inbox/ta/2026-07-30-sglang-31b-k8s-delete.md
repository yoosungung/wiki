---
id: inbox-ta-2026-07-30-sglang-31b-k8s-delete
agent: ta
ticket_id: 42
updated: 2026-07-30
status: inbox
sources:
  - ticket:42
  - kubectl:llm-serving/sglang-gemma4-31b
---

# sglang-gemma4-31b cluster delete (ticket 42)

- Eric: delete 31b from k8s; keep repo source (`manifests/apps/sglang-gemma4-31b.yaml`).
- Done: `kubectl delete deployment sglang-gemma4-31b -n llm-serving` — Pending pod cleared; 12b 2/2 unchanged.
- Leftover: Service `sglang-gemma4-31b` (empty endpoints). SA `sw-factory:cursor-agent` cannot delete services (Forbidden) — needs Eric/RBAC.
- Cause was GPU: node allocatable=2 held by 12b×2; 31b requested 2.
