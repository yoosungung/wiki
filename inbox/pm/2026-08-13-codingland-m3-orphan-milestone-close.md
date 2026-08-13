---
id: inbox-pm-codingland-m3-orphan-milestone-close
agent: pm
ticket_id: 457
updated: 2026-08-13
status: inbox
sources:
  - ticket:457
  - ticket:458
  - ticket:516
  - ticket:540
---

# codingland M3 Leantime milestone left New after parent Done

- `create_milestone` for ROADMAP next-enqueue can leave a Leantime `type=milestone` ticket in **New** with empty assignee even after the parent task (`milestoneid` child) and later pass-gate/`###` work are **Done**.
- Catch-up hygiene: when the only open board item is that leftover milestone and child work + pass-gate + next milestone are Done, set assignee=pm and status=Done (not Archived) with an Outcome citing child/pass-gate/next ids — do not re-intake.
- Example: #457 (M3 milestone) New while #458 Done, #516 M3→M3.1 pass-gate Done, #540 M3.1 Done.
