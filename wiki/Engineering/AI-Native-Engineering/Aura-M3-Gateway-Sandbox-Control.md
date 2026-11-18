---
id: aura-m3-gateway-sandbox-control
title: "Aura M3: Gateway Fair Queue · sandbox/MCP isolation · control resolve"
status: canonical
owner: km
updated: "2026-11-19"
last_updated: "2026-11-19"
review_after: "2027-02-19"
sources:
  - inbox/aura/2026-11-19-agent-invoke-mqt-stream.md
  - ticket:54a06a7d-631d-424a-8088-3accfe9a74a8
  - ticket:6a457aa6-1c75-4e0f-ace3-f6cb01baa104
  - inbox/aura/2026-11-19-aura-mcp-bundle-isolation.md
  - ticket:220f8247-4c19-45de-859c-3130531b0b33
  - inbox/aura/2026-11-19-egress-block-verify-offline.md
  - ticket:eba42b9f-3f94-4519-acfe-5697307b6785
  - inbox/aura/2026-11-19-gateway-fair-queue-rate-limit.md
  - ticket:605ca218-b321-437f-99b6-429b2f13dc67
  - inbox/aura/2026-11-19-gateway-fair-queue.md
  - inbox/aura/2026-11-19-gateway-run-id-sse-ws.md
  - ticket:c2b44645-3a15-4e5c-a37a-b4882e3a9668
  - inbox/aura/2026-11-19-inflight-release-bypass.md
  - ticket:5f299c68-2d2d-458f-a055-86cbe2ec91b9
  - inbox/aura/2026-11-19-llm-gateway-min.md
  - ticket:b7910957-9c76-4d54-9478-f9363fec5b29
  - inbox/aura/2026-11-19-mcp-invoke-dual.md
  - ticket:ae7ca986-f35b-4809-950e-f875f326fc4a
  - inbox/aura/2026-11-19-nats-mtls-secrets.md
  - ticket:012df201-9cc9-487c-a450-37dc45cc8a4e
  - inbox/aura/2026-11-19-svc-control-resolve-schema.md
  - ticket:51bc0936-b896-4919-b94e-d1f0ee94e3e3
  - inbox/pm/2026-11-19-pm-checkpoint-aura-inflight-intent-pass.md
  - ticket:494e5ee5-82b0-48da-82f0-4110c87237d9
  - inbox/pm/2026-11-19-pm-checkpoint-aura-inflight-under30-rhwp-ci-wait.md
  - inbox/pm/2026-11-19-pm-checkpoint-m3-agent-invoke-kick.md
  - inbox/pm/2026-11-19-svc-control-resolve-intent.md
tags: ["Engineering", "Aura", "Gateway", "gVisor", "MCP", "NATS"]
type: wiki
---

# Aura M3: Gateway Fair Queue · sandbox/MCP isolation · control resolve

## Gateway run_id · SSE/WS · Fair Queue

- UUIDv7 `run_id` → publish `aura.tasks.agent.invoke` → 202 + `stream_subject`; SSE/WS exact `aura.stream.<run_id>` (wildcard 금지) · owner principal.
- Fair Queue: tenant Token Bucket + max_inflight before publish (default 10/s · burst 30 · inflight 20); 429 `rate_limited`/`max_inflight_exceeded`; noisy A must not starve B.
- Terminal release on stream done/error + events done/error; `agent_invoke` `ensureAdmitted` blocks bypass publish (poison, no turn).
- Gates: `check-gateway-sse-ws.sh` · `check-gateway-fair-queue.sh` · `check-gateway-inflight-release.sh`.

## agent_invoke · mcp_invoke · LLM Gateway

- `aura.tasks.agent.invoke` MQT (minReplica=0, no PG); stream frames on Core `aura.stream.<run_id>`; deps resolve/recall/mcp.tool injectable; plaintext secrets 거부.
- mcp_invoke dual: MQT `aura.tasks.mcp.invoke` + RPC `aura.rpc.mcp.tool` Warm≥2.
- LLM Gateway min: `POST /v1/chat/completions`, tenant TB 20/s·burst40, circuit breaker; Function client may only hit `aura-llm-gateway*` (`provider_direct_forbidden`).

## Sandbox · NATS mTLS · svc-control

- Default RuntimeClass **gVisor `runsc`**; high-risk **Kata**. Egress deny-default allowlist: NATS · Pooler · LLM Gateway · `aura-content` · registered MCP · cluster DNS (not Barman/`aura-pg`).
- NATS mTLS overlay `tls.verify=true`; secrets mask + TTL≤60s cache + rotate invalidate.
- svc-control resolve: tables `source_meta`/`user_meta` + tenant RLS/`secrets_ref`; RPC `aura.rpc.control.resolve` 1-depth merge (user wins).
- Offline egress verify via NP manifests + `check-egress-block-verify.sh` (live CNI optional).
