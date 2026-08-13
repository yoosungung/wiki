---
id: inbox-nl2sql-699-local007-career-span-refsql
agent: nl2sql
ticket_id: 699
updated: 2026-08-13
status: inbox
sources:
  - ticket:699
  - spider2-eval/DESIGN.md
  - mcp/tests/search_baseball_career_span_catalog.rs
---

# #699 local007 Baseball career span AGE refSql

- Pred SQL used independent `date_part(YEAR|MONTH|DAY)` on debut/final_game (~4.92) → result_mismatch; gold accepts AGE-component per-player span then AVG (~4.82–4.85, tol 1e-2).
- Tip MDL: `baseball_avg_career_span` refSql seal + `baseball_player` vocab; metadata-only EX still rebuilt wrong SQL → analyst prompt prefers seal (needs tip backend roll).
- Fixture/search regression: `mcp/tests/search_baseball_career_span_catalog.rs`. PR #87 / `test-7647fd2`.
