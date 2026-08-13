---
id: inbox-pm-2026-08-13-pm-checkpoint-564-ip-sla
agent: pm
ticket_id: 564
updated: 2026-08-13
status: inbox
sources:
  - ticket:564
  - schedule:pm-checkpoint
  - ARCHITECTURE.md
---

# pm-checkpoint 2026-08-13T02:42Z

- Flow-active: only #564 In Progress @nl2sql (post QA #3181 fail bounce / PM #3182).
- Silence ≈3m since bounce ≪30m → within_sla; empty_ip_checkpoints=0; no HC/ARC; no actionable add_comment.
- Status-board #3109 upsert (lane IP). Review/DT/QA/DP top-level=0; Approval misroute=0.
- Evidence snapshot: tip test-500a8c6 / merge_sha 500a8c6… · empty_sql=0 · pass_rate=0 · aa:pass stands; Done blocked on AC2.
