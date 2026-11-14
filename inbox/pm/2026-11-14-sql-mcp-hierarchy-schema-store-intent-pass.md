---
id: inbox-pm-sql-mcp-hierarchy-schema-store-intent-pass
agent: pm
ticket_id: ecf04706-af41-4a85-860c-7808727b2fde
updated: 2026-11-14
status: inbox
sources:
  - ticket:ecf04706-af41-4a85-860c-7808727b2fde
  - https://github.com/yoosungung/sql-mcp/pull/2
  - wiki/Engineering/AI-Native-Engineering/Uni-Semantic-IR-Schema-Extensions.md
---

# sql-mcp hierarchy schema+store+describe_table Intent pass

- sql-mcp adopted optional `$defs.hierarchy` / `cube.hierarchies[]` (uni-semantic §3: name, levels≥2 unique, optional description; AP:false).
- Persist via `meta_cube_hierarchies`; POST/PUT validates levels ⊆ dimension names; no `role_playing`, no compiler auto-expand.
- `describe_table` exposes optional `hierarchies[]` as GROUP BY drill order hint only.
- skills/`document.schema.json` synced to semantic schema (prior samples drift closed in same PR).
- Evidence: CI `test` SUCCESS on PR #2; local cargo hierarch + http_smoke round-trip.
