---
id: inbox-nl2sql-describe-ondemand-tools
agent: nl2sql
ticket_id: 444
updated: 2026-08-10
status: inbox
sources:
  - ticket:444
  - inbox/pm/2026-08-10-nl2sql-describe-table-ondemand.md
---

# describe_table 온디맨드 Enum 조회 (#444)

- ARCHITECTURE §1.3: MCP는 계속 2도구; 온디맨드는 backend analyst tool로 흡수.
- `describe_table` 기본: 컬럼명·타입·`hasValueDomain`만 (members 제거). 컬럼 >30이면 `columnNames`(+`columnsWithValueDomain`).
- `get_column_values(table, column)` / `describe_columns(table, columns)`로 Enum·상세 온디맨드.
- `DESCRIBE_JSON_CHARS_MAX=12000` (티켓 AC1); multi-turn envelope는 `MULTI_TURN_TOOL_CHARS_MAX` 유지.
