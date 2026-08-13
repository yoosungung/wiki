---
id: inbox-nl2sql-564-career-sum-diversity
agent: nl2sql
ticket_id: 564
updated: 2026-08-13
status: inbox
sources:
  - ticket:564
  - ticket:391
  - https://github.com/yoosungung/nl2sql/pull/76
  - wiki/Agents/Text-to-SQL/Spider2-Quality-Gate-nl2sql.md
---

# nl2sql #564 tip-500a8c6: EX still fails — season MAX vs career SUM

- After #76 tip roll, search left fielding; smoke still pass_rate=0. Live local008 used season-row `MAX(g)` (165) vs gold career `SUM(g)` (3562 Peter Edward); last SSE sql often overwrote better attempts.
- Search `player batting` with k=2 returned batting+batting_postseason (no player dimension).
- Follow-up: MCP token-coverage diversity; search k 3/4; analyst prompt career SUM + name columns + stop after good execute.
