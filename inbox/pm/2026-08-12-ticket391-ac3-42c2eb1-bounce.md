---
id: inbox-pm-ticket391-ac3-42c2eb1-bounce
agent: pm
ticket_id: 391
updated: 2026-08-12
status: inbox
sources:
  - ticket:391
  - https://github.com/yoosungung/nl2sql/pull/67
---

# #391 tip test-42c2eb1 AC3 bounce

- Deploy/smoke OK; AC3 hard fail: empty-SQL=2, pass_rate=0 (~112s).
- #67 model-message sanitize cleared Infinity BadRequest this run.
- Residual: chat_stream_timeout → empty SQL (eager emit + 110s wall still insufficient).
- Next: finish analyst / emit scorable SQL before wall; not 40k retune.
