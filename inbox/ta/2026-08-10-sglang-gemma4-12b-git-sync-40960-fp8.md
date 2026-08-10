---
id: inbox-ta-sglang-gemma4-12b-git-sync-40960-fp8
agent: ta
ticket_id: 426
updated: 2026-08-10
status: inbox
sources:
  - ticket:426
  - ticket:261
  - wiki/Models/Optimization-and-Serving/SGLang-gemma4-llm-serving-cluster-ops.md
  - https://github.com/yoosungung/k8s-test/pull/3
---

# SGLang gemma4-12b: live 40K+fp8 vs git 32K drift

- After #261, `origin/main` kept `--context-length 32768` while live `llm-serving/sglang-gemma4-12b` already ran `40960` + `--kv-cache-dtype fp8_e4m3` (`max_model_len=40960`, `max_total_num_tokens≈69492`).
- Wiki ladder (ops page): 40K requires fp8 KV so pool ≥ context; length-only bumps fail when pool < context.
- Fix is git sync (manifest + `verify-sglang.sh` MIN=40960 + README); cluster re-rollout not required when live already matches.
- PR: https://github.com/yoosungung/k8s-test/pull/3 (#426).
