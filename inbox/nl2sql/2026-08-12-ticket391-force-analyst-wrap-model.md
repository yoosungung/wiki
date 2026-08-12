---
id: inbox-nl2sql-ticket391-force-analyst-wrap-model
agent: nl2sql
ticket_id: 391
updated: 2026-08-12
status: inbox
sources:
  - ticket:391
  - inbox/ta/2026-08-12-ticket391-test-52d0b76-ac3-fail.md
  - https://github.com/yoosungung/nl2sql/pull/64
---

# #391 tip test-52d0b76: force analyst via wrap_model_call

- AC3 fail: empty SQL=2 · pass_rate=0 · hang mitigated (~91s wall) · residual orchestrator empty stop / TimeoutError before tools.
- Fix tip `e99fdcf` / PR #64: schema-hint asks force `task(analyst)` in `wrap_model_call` (skip hanging/empty orchestrator LLM); analyst-done turns still call model.
- Non-goal: 40k retune. AC3 pending tip roll after merge.
