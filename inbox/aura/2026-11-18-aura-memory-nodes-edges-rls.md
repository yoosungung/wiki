---
id: inbox-aura-memory-nodes-edges-rls
agent: aura
ticket_id: fa6351fa-97b8-453c-8945-b47976b83a50
updated: 2026-11-18
status: inbox
sources:
  - ticket:fa6351fa-97b8-453c-8945-b47976b83a50
  - repo:yoosungung/aura
---

# Aura M1 memory_nodes / memory_edges + RLS

- DDL: `deploy/sql/memory_nodes_edges.sql` — nodes UNIQUE(tenant,type,name); edges FK→nodes CASCADE + self-loop CHECK; FORCE RLS + `app.tenant_id` GUC.
- Gates: `check-memory-nodes-edges.sh` (static) · `smoke-memory-nodes-edges.sh` (pooler live; `SMOKE_MEMORY_NODES_EDGES_STATIC=1` for static-only).
- Out of this slice: `idx_memory_edges_out`/`in` + traversal limit DESIGN; embeddings/HNSW; TTL job.
