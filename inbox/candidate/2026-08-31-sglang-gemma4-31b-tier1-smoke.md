---
id: inbox-candidate-sglang-gemma4-31b-tier1-smoke
agent: candidate
ticket_id: 1523
updated: 2026-08-31
status: inbox
sources:
  - ticket:1523
  - wiki miss for sglang-gemma4-31b ops; verified via cluster /v1/models
---

# candidate.win Tier1 → sglang-gemma4-31b

- Live served model: `QuantTrio/gemma-4-31B-it-AWQ` at `sglang-gemma4-31b.llm-serving.svc.cluster.local:30000/v1`
- Stale PVC `agent/.env` still pointed at dead `sglang-gemma4-12b` (deploy 0/0); align to DESIGN/`.env.example` 31B values (gitignored)
- Code defaults already 31B; unit `test_model_backends.py` + live `invoke("OK-31B")` pass after env fix
