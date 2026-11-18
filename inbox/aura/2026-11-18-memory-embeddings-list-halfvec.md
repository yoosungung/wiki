---
id: inbox-aura-memory-embeddings-list-halfvec
agent: aura
ticket_id: 0d7a4200-bad4-4b45-9b25-def2542064f2
updated: 2026-11-18
status: inbox
sources:
  - ticket:0d7a4200-bad4-4b45-9b25-def2542064f2
  - https://github.com/pgvector/pgvector/
---

# memory_embeddings LIST(model_key) + halfvec(N) HNSW

- Aura M1: 부모 `embedding halfvec`(typemod 없음) + LIST(`model_key`); 파티션마다 `CHECK (dims=N)` + `hnsw ((embedding::halfvec(N)) halfvec_cosine_ops)`.
- 세대 교체: ATTACH 새 파티션 → active `model_key` 전환 → DETACH/DROP 구형 (테이블 rewrite 금지).
- 스모크는 fixture `fixture:v*`만; 생산 `AURA_EMBEDDING_*` 실값은 별도 티켓.
- CNPG stock 이미지에서도 `CREATE EXTENSION vector`로 pgvector 0.8.x halfvec 사용 가능(클러스터에 확장 바이너리 존재 전제).
