---
id: inbox-sw-factory-hitl-mail-human-labels
agent: sw-factory
ticket_id: 4c1fd3a9-94c5-49a2-9bb7-4818900b2084
updated: 2026-11-28
status: inbox
sources:
  - ticket:4c1fd3a9-94c5-49a2-9bb7-4818900b2084
  - agent/gateway/src/hitl-mail.ts
---

# Gateway HITL mail human-facing labels

- Event payload has no ticket title; compose uses ticket GET title with `resolveTicketNo` issueKey fallback.
- Assignee/actor labels come from agents.yaml `name` only (no users API); miss → `(unknown)` + short id.
- Project label reuses `resolveProjectName` cache; fail → project id.
- Ops mail formatting only — ack never blocked by label lookup/send failure.
