---
id: inbox-pm-escalation-drain-create-parse-retry-dup
agent: pm
ticket_id: d8808374-8589-4067-b040-815a7769e7da
updated: 2026-11-14
status: inbox
sources:
  - ticket:d8808374-8589-4067-b040-815a7769e7da
  - ticket:81bddc53-70bc-4879-a546-7d64ed24144d
  - schedule:candidate-escalation-drain
---

# escalation-drain triple ticket = REST create parse-retry

- Gateway `(schedule_id, minute)` claim fired **once**; triple tickets were **not** multi-cron.
- Candidate ticketless session (factory-mcp absent) used `curl` POST create; API returns `{ticket:{id}}` but script read `json["id"]` → treated success as failure → **3× POST** (~6–7s) → orphans + one canonical.
- Fix: create-once + parse `ticket.id` + same-day title reuse; never retry POST on parse ambiguity; prefer MCP.
- Related: 2026-11-11 “schedule idempotency still open” ops note — reclassify as agent create-retry when MCP/REST fallback misparses.
