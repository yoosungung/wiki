---
id: inbox-ta-2026-08-05-ticket172-mdl-pvc-seed
agent: ta
ticket_id: 172
updated: 2026-08-05
status: inbox
sources:
  - ticket:172
  - wiki/Agents/Text-to-SQL/Spider2-Quality-Gate-nl2sql.md
  - deploy/SETUP.md (nl2sql metadata PVC)
---

# #172 Baseball/IPL MDL → test metadata PVC

- Backend PVC already had commit `5fe07689` ("seed: Baseball/IPL Spider2 MDL") · 26 baseball + 8 ipl `*.model.json` + source/manifest.
- MCP PVC was stale at `ae3a5c46` (0 models in HEAD) despite orphan files on disk; `/admin/sync` → `ref_not_found` (no git remote).
- Fix: copied backend metadata tree (incl. `.git`) onto `nl2sql-mcp-metadata`, restarted `nl2sql-mcp`; both HEADs `5fe07689`; sync `ok`.
- Verified `search_tables`: `baseball_player`, `ipl_match`, `baseball_team` hit with scores >0.
- Product tool-flood/sql|error fix still owned by nl2sql; TA redeploy after that merge remains separate.
