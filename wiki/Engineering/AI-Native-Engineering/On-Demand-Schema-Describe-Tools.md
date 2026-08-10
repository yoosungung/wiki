---
id: on-demand-schema-describe-tools
title: "온디맨드 스키마 Describe 도구 (슬림 1차 + Enum 후속)"
status: canonical
owner: km
updated: "2026-08-10"
last_updated: "2026-08-10"
review_after: "2026-11-10"
sources:
  - ticket:444
  - ticket:391
  - https://github.laiyagushi.com/Firstmeridian/llm-sql-safety-executor-mcp
tags: ["Engineering", "AI-Native", "Text-to-SQL", "MCP", "Context"]
type: "wiki"
---

# 온디맨드 스키마 Describe 도구 (슬림 1차 + Enum 후속)

고정 context(예: SGLang 40K)에서 통짜 `describe_table`(Enum members·valueDomain·expression 포함)이 Truncation/BadRequest를 내면 SQL 생성·채점이 붕괴한다. **1차는 슬림 요약, Enum/상세는 후속 도구**로 분리한다.

## 도구 역할

| 도구 | 기본 페이로드 | 비고 |
| :--- | :--- | :--- |
| `describe_table` | 컬럼명·타입·`hasValueDomain` | members 제거. 컬럼>N이면 `columnNames`(+`columnsWithValueDomain`) |
| `get_column_values(table, column)` | Enum/도메인 값 | 필요할 때만 |
| `describe_columns(table, columns)` | 소수 컬럼 상세 | `DESCRIBE_COLUMNS_MAX` 등으로 상한 |

MCP 공개 표면은 search/describe/execute처럼 얇게 두고, 온디맨드는 backend analyst tool로 흡수해도 된다.

## 예산 상수(개념)

```text
DESCRIBE_JSON_CHARS_MAX   # 단발 describe (초기 12k → 멀티턴에선 2.5k 등 하향)
SEARCH_JSON_CHARS_MAX
MULTI_TURN_TOOL_CHARS_MAX # 라운드 누적 envelope
valueDomain: ≤소수 컬럼 × members≤K, expression 드롭
```

단발 캡만 맞추고 멀티턴 envelope를 안 보면 3~4턴에 다시 overflow한다 — [[wiki/Engineering/AI-Native-Engineering/LLM-Tool-Payload-Context-Trim.md]].

## 수용 기준 예

- 기본 describe JSON ≤ `DESCRIBE_JSON_CHARS_MAX`
- 스모크 short Q: BadRequest 0 + SSE `sql`|`error`+`done`
- EX 채점은 warehouse SQL — [[wiki/Agents/Text-to-SQL/Spider2-Quality-Gate-nl2sql.md]], [[wiki/Engineering/AI-Native-Engineering/Agent-SSE-Failfast-and-Tool-Flood-Guard.md]]

## 🔗 관련 문서

- [[wiki/Engineering/AI-Native-Engineering/LLM-Tool-Payload-Context-Trim.md]]
- [[wiki/Engineering/AI-Native-Engineering/Agent-SSE-Failfast-and-Tool-Flood-Guard.md]]
- [[wiki/Agents/Text-to-SQL/Spider2-Quality-Gate-nl2sql.md]]
- [[wiki/Models/Optimization-and-Serving/SGLang-gemma4-llm-serving-cluster-ops.md]]
