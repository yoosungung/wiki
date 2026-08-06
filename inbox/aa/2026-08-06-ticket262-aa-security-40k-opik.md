---
id: inbox-aa-ticket262-aa-security-40k-opik
agent: aa
ticket_id: 262
updated: 2026-08-06
status: inbox
sources:
  - ticket:262
  - https://github.com/yoosungung/nl2sql/pull/39
  - wiki/Models/Optimization-and-Serving/SGLang-gemma4-llm-serving-cluster-ops.md
  - inbox/ta/2026-08-06-ticket262-sglang-context-40k.md
---

# #262 aa security pass (Opik overlay + SGLang 40k/fp8)

- `.factory/quality.yaml` has no `security:` command → delta review + unit evidence (same pattern as #172).
- Delta A (nl2sql PR #39, merge `7744a03`): test overlay adds `OPIK_URL_OVERRIDE` (in-cluster `opik-frontend…svc`) + `OPIK_WORKSPACE=default`. No auth/Host/secret/transport change; bearer stays out of ConfigMap.
- Unit: `pytest deploy/k8s/overlays/test/test_opik_configmap_overlay.py` PASS on synced sha `37f8938`.
- Delta B (live llm-serving): `--context-length 40960` + `--kv-cache-dtype fp8_e4m3` only. Service remains ClusterIP; `HF_TOKEN` still `secretKeyRef`. No new listen/auth surface.
- Live: backend `test-841059f`; sglang 2/2 Ready with 40k args. fp8 is capacity/accuracy tradeoff, not a new network trust boundary.
