---
id: inbox-aura-control-resolve-bridge
agent: aura
ticket_id: 7190c773-51be-4390-beba-ae24445647d6
parent_id: 6a457aa6-1c75-4e0f-ace3-f6cb01baa104
updated: 2026-11-19
status: inbox
sources:
  - ticket:7190c773-51be-4390-beba-ae24445647d6
  - https://github.com/yoosungung/aura/pull/38
---

# `aura.rpc.control.resolve` bridge Warm (M3)

- Core RR `aura.rpc.control.resolve` · queue-group `aura-control-resolve` · Deployment `aura-control-resolve-rr` **replicas≥2** · Fission `aura-control-resolve` **MinScale≥2** · **no MQT**.
- Handler `services/control/bridge.js`: stub + injectable lookup → `validateResolveRequest` / `buildResolveResponse` (`secrets_ref` only · 1-depth cfg merge).
- Pooler SELECT · HTTP admin · tenants/ACL = deferred.
- Gates: `check-control-resolve-bridge.sh` + `check-svc-control-resolve.sh` PASS; `bridge.selftest.js` PASS.