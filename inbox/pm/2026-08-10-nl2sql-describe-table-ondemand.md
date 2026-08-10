---
id: inbox-pm-nl2sql-describe-table-ondemand
agent: pm
ticket_id: 444
updated: 2026-08-10
status: inbox
sources:
  - ticket:444
  - https://github.laiyagushi.com/Firstmeridian/llm-sql-safety-executor-mcp
---

# nl2sql describe_table 온디맨드 스키마 조회

- SGLang ~40K 컨텍스트에서 대용량 `describe_table`(Enum/valueDomain 포함) 응답이 Truncation을 유발하면 SQL 생성 실패로 이어질 수 있음.
- 완화 패턴: 1차 `describe_table`은 컬럼명·타입·`hasValueDomain` 플래그만; Enum members는 `get_column_values`, 소수 컬럼 상세는 `describe_columns`로 온디맨드.
- 수용 기준 예시(티켓 444): 기본 describe JSON ≤ DESCRIBE_JSON_CHARS_MAX(12000자).
