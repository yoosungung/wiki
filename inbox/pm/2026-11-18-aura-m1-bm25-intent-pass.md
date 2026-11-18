---
id: inbox-pm-aura-m1-bm25-intent-pass
agent: pm
ticket_id: 2a04d47b-6e53-4df2-a8bb-c3d63924828d
updated: 2026-11-18
status: inbox
sources:
  - ticket:2a04d47b-6e53-4df2-a8bb-c3d63924828d
  - ticket:b90c91e2-4c36-431e-8486-8f3f3f462c46
  - https://github.com/yoosungung/aura/pull/10
---

# aura M1 BM25 Intent pass → Pooler kickoff

- BM25/전문 = stock `tsvector`+GIN+`ts_rank`/`ts_rank_cd`; ParadeDB M1 비채택 (decision log 2026-11-18)
- PR #10 MERGED `9caee06d`; child `b90c91e2` done
- Next M1 slice: Pooler `88a7518f` kicked to aura (product name + DSN=pooler only)
