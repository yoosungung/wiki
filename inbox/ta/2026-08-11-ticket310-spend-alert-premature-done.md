---
id: inbox-ta-ticket310-spend-alert-premature-done
agent: ta
ticket_id: 310
updated: 2026-08-11
status: inbox
sources:
  - ticket:310
  - ticket:291
  - wiki/Engineering/AI-Native-Engineering/Spend-Alert-Human-Approval-Triage.md
  - /tmp/sw-factory/ARCHITECTURE.md§2.8
tags: ["spend-alert", "Approval", "Done-gate"]
---

# Spend-alert Done without human Approval

- Cron `[Spend alert]` tickets are **human-only** (ack / threshold / load). Agents must not mark Done without Approval evidence (`Spend-Alert-Human-Approval-Triage`).
- #310 was `status=Done` with **0 comments**; reopened → `Waiting for Approval` + `@eric`. §2.8 `pr_url`/`merge_sha`/`test_*`/`qa:`/`aa:`/`prod_*` = **N/A** (not tenant_cd CD).
- #291 Eric decision already set threshold=`len(clients)×20M`; #310+ still alert above 100M → needs a **new** budget decision, not silent Done.
- Sibling alerts (#447 #453 #454 #480) often share the same gap; keep one canonical Approval lane (PM), list others as duplicates.
