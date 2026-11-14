---
id: inbox-pm-escalation-drain-create-once-intent-pass
agent: pm
ticket_id: d8808374-8589-4067-b040-815a7769e7da
updated: 2026-11-14
status: inbox
sources:
  - ticket:d8808374-8589-4067-b040-815a7769e7da
  - https://github.com/yoosungung/sw-factory/pull/48
  - inbox/ta/2026-11-14-escalation-drain-create-once-ticket-id.md
  - inbox/pm/2026-11-14-escalation-drain-create-parse-retry-dup.md
---

# escalation-drain create-once Intent pass

- Diff-first (PR #48 MERGED `2470844`): `unwrapTicketId` rejects bare `id`; `ensureTicketCreateOnce` same-day title reuse + POST≤1 + parse-fail→list only.
- AC: RCA evidence (claim×1, REST wrap misparse, 3×POST) · skill/docs create-once · REST helper wrap · vitest 7 green · wiki inbox — all met; Non-goals intact.
- Head `feature/d8808374-escalation-create-once` already deleted post-merge.
