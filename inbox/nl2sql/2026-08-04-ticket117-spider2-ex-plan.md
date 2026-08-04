---
id: inbox-nl2sql-ticket117-spider2-ex-plan
agent: nl2sql
ticket_id: 117
updated: 2026-08-04
status: inbox
sources:
  - ticket:117
  - ticket:99
  - wiki/Agents/Text-to-SQL/Spider2-Quality-Gate-nl2sql.md
  - wiki/Agents/Text-to-SQL/T2SQL-Benchmarks-2026.md
  - spider2-eval/DESIGN.md
  - .factory/quality.yaml
  - https://github.com/xlang-ai/Spider2/tree/main/spider2-lite/evaluation_suite
---

# Spider2 갭 해소 실행 계획 (#117) — 요약

- Gap: weekly `opik.command` = `spider2-opik check` only; `--task agent` exit 2; gold-sql smoke 2건은 수동·미연동.
- Recommend **Option A (phased)**: P0 wire gold-sql smoke into weekly gate → P1 agent via chat SSE → P2 optional ~10 local* timebox. Defer full 135/547.
- Agent path: prefer **chat SSE** (`POST /chat` → last `sql` event) over MCP-only (product path + DESIGN §7 A).
- Success: smoke pass_rate threshold (gold-sql=1.0; agent=floor TBD or non-blocking first); fail → New ticket, not silent skip.
- OoS: BQ/SF, leaderboard, Spider-Agent SR, clean_code(#113)/load(#114).
- Impl tickets (after Eric approve): see Active #117 comment.
