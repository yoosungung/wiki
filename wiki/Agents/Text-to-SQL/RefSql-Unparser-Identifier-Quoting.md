---
id: refsql-unparser-identifier-quoting
title: "refSql unparser: 식별자 인용과 COLLATE 회피"
status: canonical
owner: km
updated: "2026-08-14"
last_updated: "2026-08-14"
review_after: "2026-11-14"
sources:
  - ticket:794
  - ticket:796
  - https://www.postgresql.org/docs/current/sql-syntax-lexical.html
tags: ["Agents", "Text-to-SQL", "MDL", "refSql", "PostgreSQL", "MCP"]
type: "wiki"
---

# refSql unparser: 식별자 인용과 COLLATE 회피

카탈로그가 seal을 1위로 올려도, MCP가 `refSql`을 warehouse SQL로 풀어 쓸 때 **식별자/콜레이션 재작성**이 깨지면 execute가 폴백하고 에이전트가 베이스 모델을 다시 짠다.

## 하이픈 CTE는 따옴표

스키마·모델명에 `-`가 있으면 unparser가 `FROM "__refsql_db-imdb_…"` 는 인용해도 `WITH __refsql_db-imdb_…` 를 베어로 붙일 수 있다. Postgres는 `syntax error at or near "-"` ([lexical](https://www.postgresql.org/docs/current/sql-syntax-lexical.html)).

```sql
-- 개념: CTE 이름이 [A-Za-z_][A-Za-z0-9_]* 가 아니면 인용
WITH "__refsql_db-imdb_shahrukh_number_2_x" AS ( ... )
SELECT actor_count FROM "__refsql_db-imdb_shahrukh_number_2_x";
```

카탈로그 PUT SHA만으로는 EX가 안 바뀐다. **퍼블리시된 MCP 바이너리**에 인용 수정이 실려야 한다. `test-*` 핀 금지 — [[wiki/Engineering/Infrastructure-and-DevOps/Tip-Roll-Keep-Published-Binary.md]].

## COLLATE 재작성 실패 → convert_to

`COLLATE "C"` 를 MCP rewrite가 파싱 못 하면 `ParserError COLLATE` 후 execute_select 폴백 → 에이전트가 베이스 테이블을 SELECT한다. C-locale 정렬이 필요하면 `convert_to(col, 'SQL_ASCII')` 처럼 **rewrite-safe 식**을 seal에 둔다.

SQLite `INSTR`/`SUBSTR` CSV split을 PG에 그대로 넣으면 `near ".."` sql_exec가 난다. PG seal은 `string_to_array` / `unnest` / `string_agg`.

## 관련

- [[wiki/Agents/Text-to-SQL/RefSql-Seal-for-EX-Mismatch.md]]
- [[wiki/Agents/Text-to-SQL/MDL-Only-Domain-Knowledge.md]]
- [[wiki/Engineering/Infrastructure-and-DevOps/Metadata-Git-PVC-Resync.md]]
