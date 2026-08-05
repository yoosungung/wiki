---
id: agent-sse-failfast-and-tool-flood-guard
title: "Agent SSE fail-fast·도구 폭주 가드"
status: canonical
owner: km
updated: "2026-08-05"
last_updated: "2026-08-05"
review_after: "2026-11-05"
sources:
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
| 장시간 chunk 없음 | `stream_chunk_timeout`(예: 25s) |
| deepagents 기본 recursion 과다 | `recursion_limit`을 수십 단위로 하향(예: 40; 기본 9999 금지) |
| SQL 없이 종료 | SSE `error`(`analyst_no_sql` 등) 후 `done` — 클라이언트가 hang과 구분 |

## 도구 폭주 가드

OpenAI/호환 HarnessProfile에서 `edit_file`/`write_file`/`execute` 등 **FS·실행 도구를 제외**한다. 제품 SQL 에이전트에 파일 RCE/쓰기 면이 필요 없으면 표면을 줄이는 보안·품질 이중 이득.

스모크 판정: short Q는 `error`+`done` 또는 `sql`+`done`; **침묵 hang 금지**.

## 데이터 전제

메타데이터 PVC에 모델 0개면 pass_rate>0이 불가. MDL seed는 EX 축 — [[wiki/Agents/Text-to-SQL/Spider2-Quality-Gate-nl2sql.md]].

## 🔗 관련 문서

- [[wiki/Engineering/AI-Native-Engineering/LLM-Tool-Payload-Context-Trim.md]]
- [[wiki/Agents/Text-to-SQL/Spider2-Quality-Gate-nl2sql.md]]
- [[wiki/Engineering/AI-Native-Engineering/In-Process-ASGI-Load-Harness-Pattern.md]]
