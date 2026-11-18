---
id: inbox-pm-2026-11-19-aura-m2-embed-intent-pass
agent: pm
ticket_id: fdee9181-52f2-4678-810c-cecf67fc3917
updated: 2026-11-19
status: inbox
sources:
  - ticket:fdee9181-52f2-4678-810c-cecf67fc3917
  - ticket:1d669034-018b-45e0-986f-c50b24cfd735
  - ticket:25b46548-311f-438b-ad34-a408eeab56ea
  - https://github.com/yoosungung/aura/pull/26
---

# aura M2 embed Intent pass + recall kickoff

- Intent pass: embed MQT short_term skip (no PG) + embeddable withTenantTx stub; PR#26 merge `3e401771`.
- Evidence: handler.selftest + check-memory-embed PASS; tenant_cd N/A.
- Next child kickoff: recall RPC Function `25b46548` → aura in_progress (minReplicas≥2, no MQT).
