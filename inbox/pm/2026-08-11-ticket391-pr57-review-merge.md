---
id: inbox-pm-ticket391-pr57-review-merge
agent: pm
ticket_id: 391
updated: 2026-08-11
status: inbox
sources:
  - ticket:391
  - https://github.com/yoosungung/nl2sql/pull/57
  - https://github.com/sgl-project/sglang/discussions/16020
---

# #391 PR #57 review→merge (overflow budget)

- SoT tip `test-68d0e18`: BadRequest `42588/42489>40960` = input~40.5k + completion 2048 (SGLang checks input+max_new_tokens vs max_model_len).
- PR #57: `DEFAULT_MAX_TOKENS=1024`; describe≤4k / search≤700 / ondemand≤900 / multi-turn≤9k; CI green → merge `42fe7f0`.
- Non-goal: do not retune live `SGLANG_MAX_MODEL_LEN=40960`.
- Next: TA tip `test-42fe7f0` + AC3 `local008,local022` (empty SQL=0 · pass_rate>0).
