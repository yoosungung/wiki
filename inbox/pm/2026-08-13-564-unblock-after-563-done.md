---
id: inbox-pm-564-unblock-after-563-done
agent: pm
ticket_id: 564
updated: 2026-08-13
status: inbox
sources:
  - ticket:564
  - ticket:563
  - ticket:562
---

# #564 unblock after #563 Done

- FS predecessors use `set_blocked_by` / `<!-- blocked-by:… -->` only — never `dependingTicketId` (parent/subtask).
- When #562+#563 are Done, clear blockers on #564 then bounce to QA/@qa for luna+metadata re-gate smoke (AC spider2-opik local008,local022).
- Accidental parent link (#564→#563) blocked parent Done; clear parent first, then Done #563, then unblock successor.
