---
id: aura-m2-memory-recall-embed-inject
title: "Aura M2: capture/embed · recall Warm RRF · agent inject"
status: canonical
owner: km
updated: "2026-11-19"
last_updated: "2026-11-19"
review_after: "2027-02-19"
sources:
  - inbox/aura/2026-11-18-aura-embedding-active-pin.md
  - ticket:827b233f-0d69-4ed6-934f-5201043aeeb2
  - inbox/aura/2026-11-18-memory-embeddings-list-halfvec.md
  - ticket:0d7a4200-bad4-4b45-9b25-def2542064f2
  - inbox/aura/2026-11-18-short-term-embed-guard-iterative-scan.md
  - ticket:6dfc4c4a-c066-4b88-b948-1ffa1b9c01e8
  - inbox/aura/2026-11-19-aura-agent-inject-contract.md
  - ticket:e9ef0dd8-658f-4fbc-80b1-a73f8be8fa13
  - inbox/aura/2026-11-19-memory-capture-mqt.md
  - ticket:3a06af28-77ba-44af-853c-fd30e520fefa
  - inbox/aura/2026-11-19-memory-embed-mqt-short-term-skip.md
  - ticket:fdee9181-52f2-4678-810c-cecf67fc3917
  - inbox/aura/2026-11-19-memory-recall-hybrid-rrf.md
  - ticket:826b9aee-d394-462e-b3e6-9bd6e5a8ae00
  - ticket:1d669034-018b-45e0-986f-c50b24cfd735
  - inbox/aura/2026-11-19-memory-recall-rpc-warm-deploy.md
  - ticket:25b46548-311f-438b-ad34-a408eeab56ea
  - inbox/aura/2026-11-19-memory-recall-rpc-warm-no-mqt.md
  - inbox/pm/2026-11-19-aura-m2-agent-inject-intent-pass.md
  - inbox/pm/2026-11-19-aura-m2-embed-intent-pass.md
  - inbox/pm/2026-11-19-aura-m2-hybrid-rrf-intent-pass.md
  - inbox/pm/2026-11-19-aura-m2-recall-intent-pass.md
  - inbox/pm/2026-11-19-aura-m2-recall-rpc-intent-pass.md
  - inbox/pm/2026-11-19-pm-checkpoint-aura-m2-embed-intent.md
  - inbox/pm/2026-11-19-pm-checkpoint-aura-m2-recall-under30.md
tags: ["Engineering", "Aura", "Memory", "RRF", "MQT"]
type: wiki
---

# Aura M2: capture/embed · recall Warm RRF · agent inject

Aura M2 memory path (after M1 schema). Inject contract + capture/embed/recall.

## Agent inject contract

- Sole context source = `aura.rpc.memory.recall` `items[]` — no raw/`content_ref` dump (ARCHITECTURE §1 #9).
- Slot budget: sum 2048 · short_term 512 · episodic 768 · long_term+semantic 768; short items 4 · top_k 12.
- Packing lands in M3 `agent_invoke`; gate `check-agent-inject-contract.sh`.

## Capture · embed

- Capture MQT `aura.tasks.memory.capture` → candidates/error; **zero direct PG** in handler (no `pg`/`set_config`); live LLM extractor = M3 non-goal.
- Embed MQT: `short_term` → `skipped_short_term` (no PG); other types `withTenantTx` + active `model_key` stub; HNSW owned by embed, BM25 by store GENERATED `content_tsv`.
- Gates: `check-memory-capture.sh` · `check-memory-embed.sh`.

## Recall RPC + hybrid RRF

- Deploy = Core RR Warm only: Function MinScale≥2 + Deployment `aura-memory-recall-rr` replicas≥2 queue-group — **no MQT / JetStream lag** (No Responders risk).
- SELECT: short_term created_at DESC; BM25(`ts_rank`) + vector(`halfvec`/`<=>`) fused RRF k=60; graph stub empty until M4.
- Tx: pooler + tenant GUC then `SET LOCAL` iterative_scan/ef_search/max_scan_tuples; tenant WHERE in ANN SQL; optional `query_embedding[]`.
- Gate: `check-memory-recall.sh`.
