---
id: inbox-pm-aura-m1-nodes-edges-intent-pass
agent: pm
ticket_id: 2a04d47b-6e53-4df2-a8bb-c3d63924828d
updated: 2026-11-18
status: inbox
sources:
  - ticket:2a04d47b-6e53-4df2-a8bb-c3d63924828d
  - ticket:fa6351fa-97b8-453c-8945-b47976b83a50
  - https://github.com/yoosungung/aura/pull/17
---

# aura M1 memory_nodes/edges Intent pass → edge indexes

- nodes/edges DDL + FORCE RLS; smoke PASS; PR #17 MERGED `8366c43c`
- Next: idx_memory_edges_out/in + traversal DESIGN `8d3fb9cd`
