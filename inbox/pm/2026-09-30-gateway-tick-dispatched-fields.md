---
id: inbox-pm-gateway-tick-dispatched-fields
agent: pm
ticket_id: ea2d1b81-5582-4a25-a7dc-e9b2fc22b3e1
updated: 2026-09-30
status: inbox
sources:
  - ticket:ea2d1b81-5582-4a25-a7dc-e9b2fc22b3e1
  - repo:agent/gateway/src/cli.ts
  - repo:agent/gateway/src/loop.ts
---

# Gateway tick `dispatched` log fields

- `cli.ts` logs `{ msg: "tick", processed, acked_id, dispatched }` when processed or dispatched is non-empty.
- `dispatched[]` today: `event_id`, `persona`, `agent_id` (Cursor sticky session). Missing `ticket_id` on the object (event has it).
- Factory tickets have UUID `id` only; no sequential "ticket no" in D1.
