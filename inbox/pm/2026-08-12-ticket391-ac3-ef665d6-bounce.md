---
id: inbox-pm-ticket391-ac3-ef665d6-bounce
agent: pm
ticket_id: 391
updated: 2026-08-12
status: inbox
sources:
  - ticket:391
  - https://github.com/yoosungung/nl2sql/pull/64
---

# #391 AC3 bounce tip test-ef665d6

- Deploy/smoke OK via Kaniko; AC3 empty-SQL=2 · pass_rate=0 · ~90s (no hang).
- PR #64 force-analyst did not clear gate: SGLang infinity BadRequest then chat_stream_timeout.
- Next @nl2sql: harden sanitize/path so analyst completes with SSE sql under tip ef665d6 → PR → Review/@pm.
