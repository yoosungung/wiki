---
id: inbox-pm-2026-11-19-aura-m2-recall-intent-pass
agent: pm
ticket_id: 25b46548-311f-438b-ad34-a408eeab56ea
updated: 2026-11-19
status: inbox
sources:
  - ticket:25b46548-311f-438b-ad34-a408eeab56ea
  - ticket:1d669034-018b-45e0-986f-c50b24cfd735
  - ticket:826b9aee-d394-462e-b3e6-9bd6e5a8ae00
  - https://github.com/yoosungung/aura/pull/27
---

# aura M2 recall RPC Intent pass + hybrid RRF kickoff

- Intent pass: recall Warm Pool MinScale≥2 + Core queue-group + no MQT; PR#27 merge `655478ce`.
- Evidence: check-memory-recall.sh PASS; stub handler only; tenant_cd N/A.
- Next child kickoff: hybrid RRF recall `826b9aee` → aura in_progress.
