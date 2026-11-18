---
id: inbox-aura-memory-nodes-edges
agent: aura
ticket_id: fa6351fa-97b8-453c-8945-b47976b83a50
updated: 2026-11-18
status: inbox
sources:
  - ticket:fa6351fa-97b8-453c-8945-b47976b83a50
  - ticket:2a04d47b-6e53-4df2-a8bb-c3d63924828d
---

# memory_nodes / memory_edges + RLS (M1)

- DDL: `deploy/sql/memory_nodes_edges.sql` — nodes UNIQUE(tenant, type, name); edges FK CASCADE + self-edge CHECK; FORCE RLS both.
- `item_id` on nodes is logical only (no FK to partitioned `memory_items`).
- Edge partial indexes (`idx_memory_edges_out`/`in`) are a separate ROADMAP slice — omit from this DDL.
- Evidence: `check-memory-nodes-edges.sh` + `smoke-memory-nodes-edges.sh` via CNPG Pooler.
