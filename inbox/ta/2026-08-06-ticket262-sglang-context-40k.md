---
id: inbox-ta-ticket262-sglang-context-40k
agent: ta
ticket_id: 262
updated: 2026-08-06
status: inbox
sources:
  - ticket:262
  - ticket:261
  - kubectl:llm-serving/sglang-gemma4-12b
  - wiki/Models/Optimization-and-Serving/SGLang-gemma4-llm-serving-cluster-ops.md
---

# SGLang gemma4-12b context 32K → 40K (#262 B)

- Eric chose option B at 40k. Live 32K had `max_total_num_tokens≈34746` &lt; 40960 — raising `--context-length` alone is insufficient.
- Applied `--context-length 40960` + `--kv-cache-dtype fp8_e4m3` (mem-fraction-static 0.75 kept).
- Post-rollout: `max_model_len=40960`, `max_total_num_tokens=69492`, `available_gpu_mem≈5.32 GB`, KV dtype `float8_e4m3fn`.
- Repo: `manifests/apps/sglang-gemma4-12b.yaml`, `scripts/verify-sglang.sh` default min 40960, README SGLang section.
