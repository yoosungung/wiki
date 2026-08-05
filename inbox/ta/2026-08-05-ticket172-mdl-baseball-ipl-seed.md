---
id: inbox-ta-2026-08-05-ticket172-mdl-baseball-ipl-seed
agent: ta
ticket_id: 172
updated: 2026-08-05
status: inbox
sources:
  - ticket:172
  - wiki/Agents/Text-to-SQL/Spider2-Quality-Gate-nl2sql.md
---

# #172 seed Baseball/IPL MDL into metadata PVC

- Live metadata had 0 models (source+empty manifest only).
- Auto-generated 26 baseball + 8 ipl `*.model.json` (one model/table) from spider2db via PG introspect; source=`local_postgres`.
- Backend PVC commit `5fe07689…`; mcp PVC working-tree files present (34). Ready head updated.
- Caveat: no joins/relationships — enough for search_tables/smoke; refine with MODEL_AUTHORING if needed.
