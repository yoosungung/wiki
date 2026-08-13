---
id: inbox-nl2sql-f1-overtake-catalog-tip-gap
agent: nl2sql
ticket_id: 689
updated: 2026-08-13
status: inbox
sources:
  - ticket:689
  - ticket:688
  - wiki/Agents/Text-to-SQL/Spider2-Quality-Gate-nl2sql.md
  - spider2-eval/DESIGN.md
---

# F1 overtake catalog tip-gap (empty_sql)

- Scoreboard `empty_sql`/`metadata` can be **tip catalog gap**: PG has schema `f1` but tip metadata lacks matching `*.model.json` → `search_tables` 0 hits → empty SQL (local356: “overtaken on track”).
- Boy Scout lever: enrich `f1_lap`/`f1_pit_stop`/`f1_retirement`/`f1_driver` descriptions with overtake/pit/retirement/first-lap vocab; regression `mcp/tests/search_f1_overtake_catalog.rs`.
- Tip apply needs metadata git push (`METADATA_GIT_REMOTE` → git-http). Observed blocker: `push_failed` — `src refspec 'refs/heads/main' does not match any existing object` (502); local commit advances but MCP sync skipped until push succeeds.
