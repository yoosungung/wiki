---
id: inbox-nl2sql-ticket391-overflow-budget-fix
agent: nl2sql
ticket_id: 391
updated: 2026-08-11
status: inbox
sources:
  - ticket:391
  - inbox/ta/2026-08-11-ticket391-test-68d0e18-ac3-fail.md
  - wiki/Engineering/AI-Native-Engineering/LLM-Tool-Payload-Context-Trim.md
  - https://github.com/sgl-project/sglang/discussions/16020
---

# #391 tip test-68d0e18 — context overflow budget

- SoT: BadRequest `42588/42489>40960` = input~40.5k + `max_tokens` 2048 (StreamChunkTimeout/infinity already 0 after PR #56).
- Fix: `DEFAULT_MAX_TOKENS=1024`; describe≤4k / search≤700 / ondemand≤900 / multi-turn≤9k; describe_columns request≤3; execute preview rows≤3.
- Verify: related pytest 94 passed.
