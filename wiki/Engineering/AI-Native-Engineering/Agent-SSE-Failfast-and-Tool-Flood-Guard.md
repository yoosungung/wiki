---
id: agent-sse-failfast-and-tool-flood-guard
title: "Agent SSE fail-fast·도구 폭주 가드"
status: canonical
owner: km
updated: "2026-08-11"
last_updated: "2026-08-11"
review_after: "2026-11-11"
sources:
  - ticket:416
  - ticket:415
  - ticket:391
  - ticket:172
tags: ["Engineering", "AI-Native", "Agents", "SSE", "Harness"]
type: "wiki"
---

# Agent SSE fail-fast·도구 폭주 가드

context overflow를 고친 뒤에도 analyst/서브태스크가 **타임아웃까지 침묵**하거나, 짧은 질문에서 **수백 회 FS 도구 호출**로 다시 16K를 넘긴다. HTTP는 200이어도 채점용 `sql`이 없다.

## Fail-fast 패턴

| 증상 | 가드 |
| :--- | :--- |
| 빈 메타데이터/검색 0건 → 재검색 루프 | empty-search short-circuit 프롬프트·조기 종료 |
| `sql` SSE 미방출 | analyst/task 경로에서 warehouse/semantic SQL을 **반드시 emit** |
| 장시간 chunk 없음 | `stream_chunk_timeout`(예: 60s; Spider2 client ~120s보다 짧게) |
| 전체 SSE wall clock | `_to_sse`에 wall timeout(예: 90s) → `error`+`done` (침묵 hang 금지) |
| 채널 prose만 있고 native tool_calls 없음 | middleware가 `<\|channel\|>call:…` 등을 parse/promote해 task 주입 |
| deepagents 기본 recursion 과다 | `recursion_limit`을 수십 단위로 하향(예: 40; 기본 9999 금지) |
| SQL 없이 종료 | SSE `error`(`analyst_no_sql` 등) 후 `done` — 클라이언트가 hang과 구분 |
| 빈 `task({})` / silent stop | EnsureAnalystTaskMiddleware: HumanMessage로 args 채우고 schema hint 시 analyst task 주입 |

## 도구 폭주 가드

OpenAI/호환 HarnessProfile에서 `edit_file`/`write_file`/`execute` 등 **FS·실행 도구를 제외**한다. 제품 SQL 에이전트에 파일 RCE/쓰기 면이 필요 없으면 표면을 줄이는 보안·품질 이중 이득.

스모크 판정: short Q는 `error`+`done` 또는 `sql`+`done`; **침묵 hang 금지**.

## 데이터 전제

메타데이터 PVC에 모델 0개면 pass_rate>0이 불가. MDL seed는 EX 축 — [[wiki/Agents/Text-to-SQL/Spider2-Quality-Gate-nl2sql.md]].



## SSE 진실성·warehouse 우선

| 패턴 | 요지 |
| :--- | :--- |
| `tool_result.ok` | MCP `CallToolResult`의 `isError`/`error` 바디는 SSE `ok:false` + `{code,message}` — 성공으로 위장 금지 |
| deepagents `task` unwrap | `Command(update={messages:[ToolMessage(json)]})`만 오면 dict/`structured_response`만 보는 매퍼는 `analyst_no_sql` → **Command/ToolMessage JSON 전개** 후 warehouse→semantic 우선 |
| warehouse-only emit | 채점/UI 마지막 `sql`은 MCP `warehouse_sql`(실행 가능). semantic/C0-garbage/`\x08` 폴백 금지 |
| stash-first + shape gate | execute stash 우선; `schema.table`/quoted 형태만 warehouse로 승격(invent 테이블명 차단) |
| stash lifetime | `run_agent_events` finally에서 SSE ContextVar를 너무 일찍 reset하면 post-loop stash emit가 비어 버림 → `_to_sse` 종료까지 `reset_sse=False` |
| abort/normal end emit | stream abort·정상 종료 모두 `done`/`error` 직전에 stashed `warehouse_sql` emit |
| shared stash box | LangGraph `copy_context()`로 자식 `ContextVar.set`이 부모에 안 보이면 **request-scoped shared dict**로 execute→analyst end 전달 |
| 도메인 헬퍼 분리 | `on_tool_end` → execute/analyst/chart 매핑을 단위 테스트 가능한 헬퍼로 추출; persist는 스트림 `finally`에 유지 |
| structured output 강제 | non-empty `semantic_sql`이면 `warehouse_sql` 필수(empty catalog caveat 예외) — invent/`null` warehouse 재시도 |

성공 경로에서 warehouse가 없을 때만 tool-input sql을 UI/fixture용으로 허용하고, **MCP error 성공 폴백은 금지**.

## 스트림 타임아웃·JSON sanitize

| 함정 | 조치 |
| :--- | :--- |
| idle StreamChunkTimeout | `DEFAULT_STREAM_CHUNK_TIMEOUT_S`를 클라이언트 SLA보다 짧게(예: 60 < 120) |
| `number is infinity` BadRequest | execute LLM preview에 `sanitize_json_numbers`; search/describe/ondemand float sanitize |
| MCP `decimal` unparse | Arrow `decimal`/`numeric` → Decimal128(38,10) + 스키마 vocab |

ContextVar-safe wall timeout은 [[wiki/Engineering/AI-Native-Engineering/Asyncio-Timeout-Same-Context-Streaming.md]].

## 🔗 관련 문서

- [[wiki/Engineering/AI-Native-Engineering/LLM-Tool-Payload-Context-Trim.md]]
- [[wiki/Engineering/AI-Native-Engineering/Asyncio-Timeout-Same-Context-Streaming.md]]
- [[wiki/Agents/Text-to-SQL/Spider2-Quality-Gate-nl2sql.md]]
- [[wiki/Engineering/AI-Native-Engineering/In-Process-ASGI-Load-Harness-Pattern.md]]
