---
id: inbox-aura-2026-11-17-m0-runtime-install-pins
agent: aura
ticket_id: fa6e9c16-bc34-4354-a163-3e7eaebb3182
updated: 2026-11-17
status: inbox
sources:
  - ticket:fa6e9c16-bc34-4354-a163-3e7eaebb3182
  - https://fission.io/docs/installation/compatibility/
---

# Aura M0 runtime install pins

- NATS JetStream in `aura` ns: `nats:2.10-alpine` with `-js -m 8222` (KEDA `/jsz`).
- KEDA Helm `2.20.2` (matches Fission 1.27 tested KEDA 2.20).
- Fission Helm `1.27.0` with `mqt_keda.enabled=true` → deploy `mqtrigger-keda`.
- Install/smoke: `deploy/scripts/install-runtime.sh`, `deploy/scripts/smoke-runtime.sh`.
