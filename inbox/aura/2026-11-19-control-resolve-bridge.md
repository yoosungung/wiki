# aura.rpc.control.resolve bridge Warm (M3)

- Date: 2026-11-19
- Ticket: 7190c773-51be-4390-beba-ae24445647d6
- Repo: yoosungung/aura

## Summary
Locked Core RR bridge for `aura.rpc.control.resolve`: Fission newdeploy MinScale≥2 + Deployment `aura-control-resolve-rr` replicas≥2, queue-group `aura-control-resolve`, no MQT/JetStream scaler. Handler stub/injectable reuses resolve wire helpers (`control.resolve.done`, 1-depth cfg merge, secrets_ref only).

## Deferred
Live Pooler SELECT wiring · HTTP admin · secret store.

## Evidence
`./deploy/scripts/check-control-resolve-bridge.sh` PASS · `bridge.selftest.js` PASS
