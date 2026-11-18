---
id: inbox-pm-aura-m2-recall-rpc-intent-pass
agent: pm
ticket_id: 25b46548-311f-438b-ad34-a408eeab56ea
updated: 2026-11-19
status: inbox
sources:
  - ticket:25b46548-311f-438b-ad34-a408eeab56ea
  - https://github.com/yoosungung/aura/pull/27
---

# Aura M2 recall RPC Warm Pool — intent pass

- Diff: `deploy/k8s/memory-recall/` Function `newdeploy` MinScale≥2 + Deployment `aura-memory-recall-rr` replicas≥2, subject `aura.rpc.memory.recall`, queue-group `aura-memory-recall`, no MQT/ScaledObject; stub handler + `check-memory-recall.sh`.
- Hybrid RRF / iterative_scan SQL stays sibling `826b9aee` (mode:stub / empty items).
- PR#27 merged; local re-run `bash deploy/scripts/check-memory-recall.sh` PASS on main.
