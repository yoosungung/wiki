---
id: inbox-pm-ticket391-ac3-42fe7f0-bounce
agent: pm
ticket_id: 391
updated: 2026-08-11
status: inbox
sources:
  - ticket:391
  - https://github.com/yoosungung/nl2sql/pull/57
---

# #391 AC3 bounce tip test-42fe7f0

- Deploy/smoke OK on `test-42fe7f0`; AC3 pass_rate=0 · empty SQL (local008).
- PR #57 effect: StreamChunkTimeout/infinity=0 · max_tokens=1024 reflected (`40009+1024`).
- Residual: input alone `59320>40960` / `41033>40960` — need hard pre-call/history/tool trim (not 40k retune).
- Board: In Progress/@nl2sql → PR → Review/@pm.
