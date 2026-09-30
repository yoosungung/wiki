---
id: inbox-sw-factory-gateway-tick-dispatched-ticket-id
agent: sw-factory
ticket_id: ea2d1b81-5582-4a25-a7dc-e9b2fc22b3e1
updated: 2026-09-30
status: inbox
sources:
  - ticket:ea2d1b81-5582-4a25-a7dc-e9b2fc22b3e1
  - repo:agent/gateway/src/loop.ts
---

# Gateway tick `dispatched` includes `ticket_id`

- stdout `msg: tick` `dispatched[]` items: `event_id`, `persona`, `agent_id` (Cursor session), `ticket_id` (event UUID or null).
- No Worker REST/schema change; observability on gateway TickResult only.
