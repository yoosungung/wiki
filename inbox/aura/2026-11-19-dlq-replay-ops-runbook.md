---
title: "Aura M5: DLQ Replay ops tool + runbook"
date: 2026-11-19
ticket_id: 28cc3d9a-9801-41c9-bee5-c074edcfa1b2
agent: aura
tags: ["Engineering", "Aura", "NATS", "DLQ", "ops"]
---

# Aura M5: DLQ Replay ops tool + runbook

- Path ① Term envelope: `src` + `echo`/`payload` → replay publish to **original** subject (not `aura.dlq.*`).
- Ops only: `dry_run` default · `confirm` required · `max_batch=20` · refuse `aura.dlq.*` (no auto-loop).
- Artifacts: `deploy/docs/dlq-replay.md` · `services/ops/dlq-replay/` · `dlq-replay.sh` · `check-dlq-replay.sh`.
- Non-goals: Advisory 이관 · cron/무한 replay · live NATS CI.

## Related

- [[wiki/Engineering/AI-Native-Engineering/Aura-M0-Runtime-Nats-Keda-Fission.md]]
