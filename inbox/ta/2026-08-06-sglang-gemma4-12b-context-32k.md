---
id: inbox-ta-sglang-gemma4-12b-context-32k
agent: ta
ticket_id: 261
updated: 2026-08-06
status: inbox
sources:
  - ticket:261
  - ticket:172
  - kubectl:llm-serving/sglang-gemma4-12b
  - wiki/Models/Optimization-and-Serving/SGLang-gemma4-llm-serving-cluster-ops.md
---

# SGLang gemma4-12b context 16K → 32K

- Live overflow root cause was SGLang `--context-length 16384` (API `max_model_len`), not Gemma 4 model cap (~256K).
- Applied `--context-length 32768` on `sglang-gemma4-12b` (1×4090/replica, `mem-fraction-static 0.75`).
- Post-rollout: `max_model_len=32768`, `max_total_num_tokens=34746`, `available_gpu_mem=5.38 GB`, VRAM ~19261/24564 MiB.
- Smoke: short chat + prompt_tokens>~18k completed without 16K BadRequest; in-pod tool_calls OK.
- 64K not applied: KV pool `34746 < 65536`; needs `--kv-cache-dtype fp8_e4m3` (or more VRAM) before raising further.
