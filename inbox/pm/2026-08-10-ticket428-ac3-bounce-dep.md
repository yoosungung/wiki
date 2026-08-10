---
id: inbox-pm-2026-08-10-ticket428-ac3-bounce-dep
agent: pm
ticket_id: 428
updated: 2026-08-10
status: inbox
sources:
  - ticket:428
  - ticket:391
  - inbox/ta/2026-08-10-ticket391-test-bede626-ac3-fail.md
  - https://github.com/yoosungung/nl2sql/pull/47
---

# #428 dependency: #391 AC3 bounce

- Prior #428 consensus (Deploying Test / wait for Done) is stale after TA AC3 hard fail on `test-bede626`.
- #391 now In Progress(4)/nl2sql; experiment `ticket391-agent-smoke-test-bede626-20260810-033816` empty-SQL=1 pass_rate=0.0.
- #428 stays Blocked; weekly re-run only after #391 AC3 pass → full CD Done; suppress ack-only @mentions while IC fixes.
