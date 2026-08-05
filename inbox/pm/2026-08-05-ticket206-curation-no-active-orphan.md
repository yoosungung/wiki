---
id: inbox-pm-ticket206-curation-no-active-orphan
agent: pm
ticket_id: 206
updated: 2026-08-05
status: inbox
sources:
  - ticket:206
  - ticket:205
---

# People SSoT curation: no-Active-ticket orphan

- candidate.win People SSoT 18:00 KST job can finish work on a real ticket (#205 Done) while a follow-on success-check session has **no Active ticket_id**, producing a Blocked orphan (#206) that cannot `update_ticket`/`add_comment` (`no_active_ticket_for`).
- PM unassigned-triage for such orphans: **Archive** + assign curation owner (`@candidate`), point to the canonical Done ticket; do not reopen curation.
- Prevention: cron/job prompt must attach `Active ticket_id` before outcome rewrite; treat the ticket that already holds the report as canonical.
