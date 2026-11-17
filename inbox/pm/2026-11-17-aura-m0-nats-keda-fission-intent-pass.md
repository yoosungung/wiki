---
id: inbox-pm-aura-m0-nats-keda-fission-intent-pass
agent: pm
ticket_id: fa6e9c16-bc34-4354-a163-3e7eaebb3182
updated: 2026-11-17
status: inbox
sources:
  - ticket:fa6e9c16-bc34-4354-a163-3e7eaebb3182
  - https://github.com/yoosungung/aura/pull/1
---

# Aura M0 — NATS/KEDA/Fission bootstrap Intent pass

- Aura M0 first slice: cluster install only; streams / sample MQT·RPC / DLQ stay later tickets.
- Pins that passed smoke: NATS `2.10-alpine` (JetStream + `-m 8222`), KEDA Helm `2.20.2`, Fission `1.27.0` with `mqt_keda.enabled=true`.
- Fission CRD client-side apply can hit last-applied 262144 limit — use create or server-side apply (`--force-conflicts`).
- Smoke gate: `deploy/scripts/smoke-runtime.sh` (nats `/healthz`+`/jsz`, keda-operator, `mqtrigger-keda`).
- Merged: yoosungung/aura#1 → `d5285a24`; head branch deleted.
