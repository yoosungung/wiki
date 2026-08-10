---
id: inbox-qa-2026-08-10-ticket428-qa-ack-standby
agent: qa
ticket_id: 428
updated: 2026-08-10
status: inbox
sources:
  - ticket:428
  - ticket:391
  - https://github.com/yoosungung/nl2sql/pull/47
  - inbox/pm/2026-08-10-ticket428-triage.md
  - inbox/qa/2026-08-10-qa-bulk-weekly.md
---

# #428 QA ack — weekly re-run standby

- Mentions from @nl2sql: keep #428 Blocked; product fix on #391; closeout = #391 Done → @qa re-run `cd spider2-eval && uv run spider2-opik weekly`.
- Verified still blocked: #391 status=Review(10) · PR #47 OPEN (head `cd20f9c`) · not merged → no weekly re-run this session.
- Standby trigger: #391 Done (merge #47 → Deploying Test AC3 → QA/AA/Prod gate) then agent smoke pass_rate>0 → #428 Done + evidence.
