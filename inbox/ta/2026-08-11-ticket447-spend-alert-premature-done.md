---
id: inbox-ta-ticket447-spend-alert-premature-done
agent: ta
ticket_id: 447
updated: 2026-08-11
status: inbox
sources:
  - ticket:447
  - ticket:310
  - wiki/Engineering/AI-Native-Engineering/Spend-Alert-Human-Approval-Triage.md
  - /tmp/sw-factory/ARCHITECTURE.md§2.8
tags: ["spend-alert", "Approval", "Done-gate"]
---

# Spend-alert #447 premature Done (sibling of #310)

- Cron `[Spend alert]` tickets are **human-only**; agents must not mark Done without Approval evidence.
- #447 was `status=Done` with **0 comments**; reopened → `Waiting for Approval` + `@eric`. §2.8 CD evidence = **N/A**.
- Facts: 24h `170147476` > threshold `100000000` (5×20M). Same overrun family as #310 (canonical Approval lane).
- Duplicate siblings (read-only): #453 #454 #480 — do not silent-Done; wait for Eric budget decision on the Approval lane.
