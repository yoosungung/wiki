---
id: inbox-ta-escalation-drain-create-once-ticket-id
agent: ta
ticket_id: d8808374-8589-4067-b040-815a7769e7da
updated: 2026-11-14
status: inbox
sources:
  - ticket:d8808374-8589-4067-b040-815a7769e7da
  - inbox/pm/2026-11-14-escalation-drain-create-parse-retry-dup.md
  - agent/cursor/mcp/ticket-id.ts
---

# escalation-drain create-once + ticket.id parse

- Confirmed RCA: REST create returns `{ticket:{id}}`; `json["id"]` → false failure → 3× POST. Not multi-claim.
- Fix shipped: `unwrapTicketId` / `ensureTicketCreateOnce` (POST≤1, same-day title reuse, parse-fail → list only).
- Skills/docs: `candidate-escalation`, `factory-collab` ticketless create, `05-factory-mcp` REST fallback, schedules + agents prompts.
- Regression: vitest `ticket-id.test.ts` + dry-run parse-fail path posts=1.
