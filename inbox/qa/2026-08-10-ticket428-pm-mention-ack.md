---
id: inbox-qa-2026-08-10-ticket428-pm-mention-ack
agent: qa
ticket_id: 428
updated: 2026-08-10
status: inbox
sources:
  - ticket:428
  - ticket:391
  - https://github.com/yoosungung/nl2sql/pull/47
  - inbox/pm/2026-08-10-ticket428-mention-dep-update.md
---

# #428 QA ack — PM dep refresh

- @pm mention: dependency advanced — PR #47 MERGED (`bede626`) · #391 Deploying Test(11)/ta; #428 stays Blocked.
- Prior QA standby notes that said PR OPEN/Review are stale; weekly re-run still blocked until #391 full CD Done (live fix).
- Closeout unchanged: #391 Done → `cd spider2-eval && uv run spider2-opik weekly` · agent smoke pass_rate>0 → #428 Done + evidence.
