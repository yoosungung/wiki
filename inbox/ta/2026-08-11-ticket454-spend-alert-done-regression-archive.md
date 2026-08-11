---
id: inbox-ta-ticket454-spend-alert-done-regression-archive
agent: ta
ticket_id: 454
updated: 2026-08-11
status: inbox
sources:
  - ticket:454
  - ticket:310
  - wiki/Engineering/AI-Native-Engineering/Spend-Alert-Human-Approval-Triage.md
  - https://github.com/yoosungung/sw-factory/pull/6
tags: ["spend-alert", "Archived", "Done-gate", "duplicate"]
---

# Spend-alert #454 Done regression → Archived (dup of #310)

- Closeout hit `status=Done` again despite prior Approval reopen comment; no §2.8 CD evidence (not tenant_cd).
- Human decision already on #310: `SPEND_TOKENS_PER_CLIENT` 20M→100M; PR #6 `bdf4294…` merged; live CronJob still `20000000` (apply belongs on #310 In Progress).
- #454 (24h `218148350`) Archived as cron sibling duplicate pointing to #310 — same pattern as #447/#453. Do not silent-Done spend-alerts.
