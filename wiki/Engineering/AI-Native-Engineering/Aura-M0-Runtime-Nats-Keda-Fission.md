---
id: aura-m0-runtime-nats-keda-fission
title: "Aura M0: NATS/KEDA/Fission pins · Sync RPC Deployment · DLQ Term"
status: canonical
owner: km
updated: "2026-11-18"
last_updated: "2026-11-18"
review_after: "2027-02-18"
sources:
  - inbox/aura/2026-11-17-m0-runtime-install-pins.md
  - inbox/aura/2026-11-17-aura-sync-rpc-explicit-deployment.md
  - inbox/aura/2026-11-17-aura-dlq-term-path.md
  - inbox/pm/2026-11-17-aura-m0-nats-keda-fission-intent-pass.md
  - inbox/ta/2026-11-17-aura-reboot-prep.md
  - ticket:fa6e9c16-bc34-4354-a163-3e7eaebb3182
  - ticket:817796ca-a69e-4507-8480-b320b76cb34a
  - ticket:1632b9ee-7d25-4a9d-96f9-2a8cd83f72b4
  - ticket:e9e09bfd-dac0-415e-8416-0247d7c75ef2
tags: ["Engineering", "Aura", "NATS", "KEDA", "Fission", "DLQ"]
type: wiki
---

# Aura M0: NATS/KEDA/Fission pins · Sync RPC Deployment · DLQ Term

M0 first slice = **cluster install + sample Warm paths**. Streams/MQT wire-up/DLQ production wiring may land as later children; pins and contracts below are the durable facts.

## Runtime install pins

| Component | Pin | Notes |
| :--- | :--- | :--- |
| NATS JetStream (`aura` ns) | `nats:2.10-alpine` | `-js -m 8222` for KEDA `/jsz` |
| KEDA Helm | `2.20.2` | matches Fission 1.27 tested KEDA |
| Fission Helm | `1.27.0` | `mqt_keda.enabled=true` → deploy `mqtrigger-keda` |

- Scripts: `deploy/scripts/install-runtime.sh`, `deploy/scripts/smoke-runtime.sh` (nats `/healthz`+`/jsz`, keda-operator, `mqtrigger-keda`).
- Fission CRD client-side apply can hit last-applied **262144** limit → use create or server-side apply (`--force-conflicts`).

## Sync Core RR = explicit Deployment (not stock node-env)

- Stock Fission `node-env` does **not** auto-subscribe NATS Core before/after specialize.
- `aura.rpc.*` Warm responders = ARCHITECTURE §4.3 **same-image explicit Deployment** (queue-group).
- M0 sample: Deployment `aura-rpc-smoke-rr` · `nats reply -q aura-rpc-smoke` · subject `aura.rpc.smoke` · replicas≥2 · **JetStream MQT/lag not wired**.
- Fission Function `aura-rpc-smoke` (`newdeploy` MinScale≥2) stays for V0.1 Warm Pool invariant; Core RR body is the Deployment.
- Smoke: `smoke-sync-rpc.sh` — Warm RR · replicas=0 → No Responders · 1-pod delete HA · single-hop p95≪1s.

## DLQ path = Term (Advisory not adopted)

- MaxDeliver exceeded → JetStream **does not** auto-move to DLQ; redelivery stops + advisory only.
- Aura path: last delivery copies payload to `aura.dlq.>` then `Term()`/`Ack`.
- WorkQueue: after MaxDeliver, `stream get` may fail → Advisory-only risks **payload loss**.
- Fission MQT wire-up is follow-up; contract smoke = `smoke-dlq-term.sh`.

## Reboot prep (orbstack)

- ta kubeconfig contexts = `orbstack` only; `aura` NS NotFound → delete no-op.
- tip may be docs-only reboot; re-apply N/A until M0 manifests return. Old `aura-secrets` + ghcr overlay path retired at tip.

## 🔗 Related

- [[wiki/Engineering/AI-Native-Engineering/Factory-Schedule-Ops-Skips.md]]
- [[wiki/Engineering/AI-Native-Engineering/Wiki-Synthesis-Policy.md]]
