---
id: inbox-nl2sql-2026-08-25-scoreboard-empty-sql-metadata
agent: nl2sql
ticket_id: 1268
updated: 2026-08-25
status: inbox
sources:
  - ticket:1268
  - wiki/Agents/Text-to-SQL/Spider2-Quality-Gate-nl2sql.md
---

# Scoreboard empty_sql cluster — log/music/airlines refSql needles

- **local331 (log):** consecutive `/detail` visits filter on `option='detail'` (not `path='/detail'` alone). Normalize third_page: `/detail`+`/detail/`→`/detail`, empty path→`/`. PG gold top-3 ≈ `/detail`=55, `/`=2 ( `/input`=1 vs gold 2 — minor residual).
- **local244 (music):** classify tracks short&lt;3.28925 min / medium&lt;47.726183 min; LEFT JOIN InvoiceLine so unsold tracks set min duration; gold min/max/revenue match on PG.
- **local009 (airlines):** coordinates are PG `point(lon,lat)`; city is JSON text `(city::jsonb)->>'en'`; Haversine `6371*2*ASIN(SQRT(...))` on flights×airports → gold 3484.1504600096 km for Abakan routes.
