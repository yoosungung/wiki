---
id: inbox-pm-ticket453-spend-alert-duplicate-archive
agent: pm
ticket_id: 453
updated: 2026-08-11
status: inbox
sources:
  - ticket:453
  - ticket:310
  - ticket:447
  - https://github.com/yoosungung/sw-factory/pull/6
  - wiki/Engineering/AI-Native-Engineering/Spend-Alert-Human-Approval-Triage.md
  - https://cursor.com/changelog/05-04-26
tags: ["spend-alert", "duplicate", "Archived", "RBAC"]
---

# Spend-alert #453 Archived (duplicate of #310)

- Eric @pm (#1647): handle on #310 — same 20M→100M decision already on canonical #310 / PR #6 (`bdf4294…`).
- Status drift: ticket was Done(0); corrected to Archived(-1). Spend-alert siblings must not self-Done (wiki Spend-Alert-Human-Approval-Triage).
- Live CronJob still `SPEND_TOKENS_PER_CLIENT=20000000`; pm/ta cannot patch cronjobs — Eric owns live apply; evidence on #310 only.
- Soft-limit alerting pattern (Cursor May 2026 changelog) aligns with raising soft threshold rather than hard-stopping agents.
