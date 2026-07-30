---
id: inbox-ta-2026-07-30-sglang-31b-closeout
agent: ta
ticket_id: 42
updated: 2026-07-30
status: inbox
sources:
  - ticket:42
  - kubectl:llm-serving
---

# sglang-gemma4-31b incident closeout (#42)

- Cluster: no Deploy/Svc/Pod/Ingress/PVC named or labeled `sglang-gemma4-31b` in `llm-serving` (Eric deleted leftover Service).
- Repo source kept: `manifests/apps/sglang-gemma4-31b.yaml` (per Eric).
- 12b remains 2/2 Running on didim-gpu.
- No git-ship/PR — ops-only, no code change.
