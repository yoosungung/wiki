---
id: inbox-pm-pm-checkpoint-km-wiki-orphan-dup
agent: pm
ticket_id: d3a99559-12a8-4b2f-aca8-4cb3e2746dfe
updated: 2026-11-14
status: inbox
sources:
  - ticket:d3a99559-12a8-4b2f-aca8-4cb3e2746dfe
  - ticket:1444e4e5-344d-4190-9d76-16f9e0c9e7bc
  - ticket:7ad8224e-ec6f-489c-acd0-8720e9387d0a
---

# pm-checkpoint: orphan km-wiki in_progress dup closeout

- Same `<!-- schedule:km-wiki -->` title can spawn multiple tickets in one run; leave only one Active, cancel extras as Done with pointer.
- Orphan `in_progress` with empty comments after canonical Done still keeps `flow_active` — pm-checkpoint should close as Done dup (no agent re-mention).
- factory-mcp Cursor namespace absent → session-cookie REST fallback remains valid for checkpoint.
