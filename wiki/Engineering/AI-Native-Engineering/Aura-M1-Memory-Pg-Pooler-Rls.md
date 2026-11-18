---
id: aura-m1-memory-pg-pooler-rls
title: "Aura M1: memory PG · Pooler/RLS · BM25/HNSW · TTL/HA"
status: canonical
owner: km
updated: "2026-11-19"
last_updated: "2026-11-19"
review_after: "2027-02-19"
sources:
  - inbox/aura/2026-11-18-aura-bm25-tsvector-decision.md
  - ticket:b90c91e2-4c36-431e-8486-8f3f3f462c46
  - inbox/aura/2026-11-18-aura-cnpg-pooler-decision.md
  - ticket:2a04d47b-6e53-4df2-a8bb-c3d63924828d
  - ticket:88a7518f-575a-4985-a580-dff0c6be89b4
  - inbox/aura/2026-11-18-aura-hnsw-multitenant-fixture.md
  - ticket:fbed0ce9-7b83-42ab-bdbc-e71fb7aa71fa
  - inbox/aura/2026-11-18-aura-memory-audit-month-range.md
  - ticket:85741c7b-9713-44b3-91c5-2a2fc6a5bc24
  - inbox/aura/2026-11-18-aura-memory-items-list-range-rls.md
  - ticket:a181ec17-22c8-4179-aa68-aef3b133f047
  - inbox/aura/2026-11-18-aura-memory-items-partition.md
  - inbox/aura/2026-11-18-aura-memory-nodes-edges-rls.md
  - ticket:fa6351fa-97b8-453c-8945-b47976b83a50
  - inbox/aura/2026-11-18-aura-memory-nodes-edges.md
  - inbox/aura/2026-11-18-aura-memory-store-mqt-set-config.md
  - ticket:1c796f58-89e0-457e-8c19-e73a69fc2160
  - inbox/aura/2026-11-18-aura-memory-store-mqt.md
  - inbox/aura/2026-11-18-aura-memory-ttl-policy.md
  - ticket:06ca1e75-d8b6-4977-aa63-30dc13abe3e8
  - inbox/aura/2026-11-18-aura-pg-ha-pitr-topology.md
  - ticket:f320c964-2f59-43af-a5db-484f2713b691
  - inbox/aura/2026-11-18-aura-pg-multi-az-pitr-draft.md
  - inbox/aura/2026-11-18-aura-pg-pooler-smoke-plan.md
  - ticket:3f7386c8-0eb3-4133-9a0f-69a55cb4132e
  - inbox/aura/2026-11-18-aura-pooler-rls-smoke.md
  - ticket:92cccf21-e2e4-48c7-b9cd-a495f1fb9d15
  - inbox/aura/2026-11-18-cnpg-pooler-transaction-dsn.md
  - inbox/pm/2026-11-18-aura-m1-bm25-intent-pass.md
  - inbox/pm/2026-11-18-aura-m1-embed-guard-intent-pass.md
  - ticket:6dfc4c4a-c066-4b88-b948-1ffa1b9c01e8
  - inbox/pm/2026-11-18-aura-m1-embedding-active-intent-pass.md
  - ticket:827b233f-0d69-4ed6-934f-5201043aeeb2
  - inbox/pm/2026-11-18-aura-m1-embeddings-intent-pass.md
  - ticket:0d7a4200-bad4-4b45-9b25-def2542064f2
  - inbox/pm/2026-11-18-aura-m1-ha-intent-pass.md
  - inbox/pm/2026-11-18-aura-m1-hnsw-followup-intent-pass.md
  - inbox/pm/2026-11-18-aura-m1-kickoff.md
  - inbox/pm/2026-11-18-aura-m1-memory-audit-intent-pass.md
  - inbox/pm/2026-11-18-aura-m1-memory-items-intent-pass.md
  - inbox/pm/2026-11-18-aura-m1-nodes-edges-intent-pass.md
  - inbox/pm/2026-11-18-aura-m1-pooler-intent-pass.md
  - inbox/pm/2026-11-18-aura-m1-rls-intent-pass.md
  - inbox/pm/2026-11-18-aura-m1-store-intent-pass.md
  - inbox/pm/2026-11-18-aura-m1-store-mqt-intent-pass.md
  - inbox/pm/2026-11-18-aura-m1-ttl-intent-pass.md
  - inbox/pm/2026-11-18-pm-checkpoint-aura-m1-audit-under30.md
  - inbox/pm/2026-11-18-pm-checkpoint-aura-m1-embeddings-kick.md
  - ticket:8d3fb9cd-7543-458a-a2cd-71b24a4fbc09
  - inbox/pm/2026-11-18-pm-checkpoint-aura-m1-empty1.md
  - inbox/pm/2026-11-18-pm-checkpoint-aura-m1-empty1hold-kickoff.md
  - inbox/pm/2026-11-18-pm-checkpoint-aura-m1-hnsw-under30.md
  - inbox/pm/2026-11-18-pm-checkpoint-aura-m1-nodes-intent-pass.md
  - inbox/pm/2026-11-18-pm-checkpoint-aura-m1-under30-b.md
  - inbox/pm/2026-11-18-pm-checkpoint-aura-m1-under30.md
  - inbox/pm/2026-11-18-pm-checkpoint-aura-multiaz-intent-pass.md
  - inbox/pm/2026-11-18-pm-checkpoint-aura-pooler-intent-pass.md
  - inbox/pm/2026-11-18-pm-checkpoint-hnsw-seal-embedding-kick.md
tags: ["Engineering", "Aura", "PostgreSQL", "pgvector", "RLS", "HNSW"]
type: wiki
---

# Aura M1: memory PG · Pooler/RLS · BM25/HNSW · TTL/HA

Aura M1 memory/PG stack durable decisions (builds on [[wiki/Engineering/AI-Native-Engineering/Aura-M0-Runtime-Nats-Keda-Fission.md]]).

## Pooler + RLS

- Product = CloudNativePG `Pooler`, `poolMode: transaction`; app DSN host = pooler Service only (`aura-pg-pooler…`) — never PG Pod/`-rw`/`-ro` Service IP.
- Every tenant tx: `set_config('app.tenant_id', $1, true)` then work; ban `false` / session SET under transaction pooling.
- V1.1 smoke: A→COMMIT→B via pooler; cross-tenant hidden; static forbid session GUC. Gates: `check-pg-pooler.sh` · `smoke-pg-pooler.sh`.

## memory_items / audit / nodes-edges

- `memory_items`: parent LIST(`memory_type`); short_term/episodic RANGE(`created_at`); long_term/semantic leaf; PK includes partition keys (no lone `id` FK).
- `memory_audit`: RANGE(`created_at`) · soft-delete 없음(파티션 DROP SoR) · FORCE RLS.
- `memory_nodes`/`memory_edges`: UNIQUE(tenant,type,name); edges FK CASCADE + self-loop CHECK; `item_id` logical only.
- Gates: `check-memory-items.sh` / `smoke-memory-items.sh` · `check-memory-audit.sh` · `check-memory-nodes-edges.sh`.

## BM25 · embeddings · HNSW · TTL · HA

- Lexical = stock `tsvector`+GIN+`ts_rank` (`content_tsv`); ParadeDB `pg_search` M1 비채택 (Okapi BM25 아님 — 품질 갭 시 재평가).
- Embeddings: parent `halfvec` + LIST(`model_key`); per-partition `halfvec(N)` HNSW cosine; active pin `AURA_EMBEDDING_MODEL=BAAI/bge-m3` · dims=1024 · `model_key=BAAI/bge-m3:1`.
- short_term embed INSERT blocked by DDL CHECK; recall GUC: `hnsw.iterative_scan=relaxed_order` · `ef_search=40` · `max_scan_tuples=20000` (no app post-filter).
- Multitenant HNSW fixture: OFF=0 / relaxed_order≥1 on `halfvec_l2_ops` PK-free table (cosine skew gap logged on pgvector 0.8.7).
- TTL: short_term 14d · episodic 24mo · audit 12mo; DROP daily UTC task name `aura.tasks.memory.ttl` (impl M4).
- HA draft: CNPG instances≥3 + zone spread; Barman PITR dest TBD; RPO≤5m · RTO≤1h; recall opt-in RO pooler.

## Store MQT

- `aura.tasks.memory.store` → stored/error; consumer `aura_memory_store`; `withTenantTx` + pooler DSN; gate `check-memory-store.sh`.
