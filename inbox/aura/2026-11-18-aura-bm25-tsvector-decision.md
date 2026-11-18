---
id: inbox-aura-bm25-tsvector-decision
agent: aura
ticket_id: b90c91e2-4c36-431e-8486-8f3f3f462c46
updated: 2026-11-18
status: inbox
sources:
  - ticket:b90c91e2-4c36-431e-8486-8f3f3f462c46
  - https://www.paradedb.com/docs/operate/deploy/self-hosted/kubernetes
---

# Aura M1 BM25 = stock tsvector

- 결정: lexical/BM25 경로 = PostgreSQL `tsvector` + GIN + `ts_rank`/`ts_rank_cd` (`content_tsv`). ParadeDB `pg_search` M1 비채택.
- 근거: ARCHITECTURE §6 DDL 기본과 일치; Pooler/RLS M1과 병행 시 추가 확장·`shared_preload`·CNPG ImageVolume(PG18+) 불필요.
- 한계: 랭킹은 Okapi BM25가 아님(`ts_rank`). 품질 갭 실측 시 `pg_search` 재평가.
- L0: aura `ROADMAP` 결정 로그 2026-11-18 · `ARCHITECTURE` §6.
