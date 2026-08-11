---
id: inbox-ta-ticket480-spend-alert-premature-done
agent: ta
ticket_id: 480
updated: 2026-08-11
status: inbox
sources:
  - ticket:480
  - ticket:310
  - wiki/Engineering/AI-Native-Engineering/Spend-Alert-Human-Approval-Triage.md
  - https://github.com/yoosungung/sw-factory/pull/6
tags: ["spend-alert", "Approval", "Done-gate", "CronJob-drift"]
---

# Spend-alert #480 premature Done + CronJob still 20M

- Cron `[Spend alert]` is **human-only**; agents must not mark Done without Approval evidence.
- #480 was `status=Done` after catch-up seal only; reopened → `Waiting for Approval` + `@eric`. §2.8 CD evidence = **N/A** (not tenant_cd).
- Facts: 24h `251527346` > live threshold `100000000` (5×20M). Same overrun family as #310/#447/#453.
- Eric decision on #310: raise `SPEND_TOKENS_PER_CLIENT` 20M→100M — PR https://github.com/yoosungung/sw-factory/pull/6 **merged**; live `cursorbridge-spend-alert` CronJob env still `20000000` (cluster apply pending). Under new threshold (5×100M=500M) this window would not alert.
- Treat as **duplicate** of canonical Approval lane **#310**; next step = apply merged manifest / ack remaining siblings.
