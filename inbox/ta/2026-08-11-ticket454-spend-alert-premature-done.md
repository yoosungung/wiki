---
id: inbox-ta-ticket454-spend-alert-premature-done
agent: ta
ticket_id: 454
updated: 2026-08-11
status: inbox
sources:
  - ticket:454
  - ticket:310
  - ticket:447
  - ticket:453
  - wiki/Engineering/AI-Native-Engineering/Spend-Alert-Human-Approval-Triage.md
  - /tmp/sw-factory/ARCHITECTURE.md§2.8
  - https://cursor.com/help/models-and-usage/usage-limits
tags: ["spend-alert", "Approval", "Done-gate"]
---

# Spend-alert #454 premature Done (sibling of #310/#447/#453)

- Cron `[Spend alert]` tickets are **human-only**; agents must not mark Done without Approval evidence.
- #454 was `status=Done` with **0 comments**; reopened → `Waiting for Approval` + `@eric`. §2.8 CD evidence = **N/A** (not tenant_cd).
- Facts: 24h `218148350` > threshold `100000000` (5×20M). Same overrun family as #310/#447/#453.
- Treat as **duplicate** of canonical Approval lane **#310**; wait for Eric budget decision (ack / raise threshold / reduce load). Do not silent-Done.
