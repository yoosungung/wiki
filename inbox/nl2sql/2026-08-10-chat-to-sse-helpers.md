---
id: inbox-nl2sql-chat-to-sse-helpers
agent: nl2sql
ticket_id: 416
updated: 2026-08-10
status: inbox
sources:
  - ticket:416
  - https://dev.to/yureki_lab/how-i-refactored-a-4000-line-god-class-with-claude-code-without-breaking-prod-2aco
---

# chat._to_sse mixed_abstraction 분리 (#416)

- LangGraph `on_tool_end` → 도메인 SSE 매핑에서 execute_select / analyst / chart-viewer를 각각 `_execute_select_domain_events` · `_analyst_task_domain_events` · `_chart_viewer_domain_events`로 추출하면 회귀 단위 테스트가 SSE 스트림 없이 가능해진다.
- persist(`ConversationStore`)는 스트림 `finally`에 남겨 abstraction level을 맞춘다 — 도메인 이벤트 헬퍼에 DB를 넣지 않는다.
- 동작 보존 boy scout: 기존 `tests/test_chat.py` SSE 경로 + 헬퍼 단위 테스트로 경계 고정.
