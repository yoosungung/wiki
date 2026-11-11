---
id: inbox-pm-2026-11-11-escalation-drain-triple-dup-intake
agent: pm
ticket_id: 0c229f2a-37c1-4e76-a7a8-895b708ad256
updated: 2026-11-11
status: inbox
sources:
  - ticket:0c229f2a-37c1-4e76-a7a8-895b708ad256
  - wiki/Engineering/AI-Native-Engineering/Factory-Schedule-Ops-Skips.md
---

# candidate-escalation-drain 2026-11-11 triple dup intake

- Same-day schedule fired **3** `in_progress` tickets (~10–30s): `1322dc1a`, Active `0c229f2a`, `87730bdd`.
- PM canonical = Active `0c229f2a`: intake AC on body, assignee=`candidate`, `@candidate` kickoff; siblings not written (Active scope).
- Host `pending.jsonl` observed **0 bytes** at intake — still IC-verify; empty → schedule no-op (no PR).
- Pattern continues 2026-11-09/10 duplex; ops should fix schedule idempotency (gateway/agents.yaml), not PM close-all.
