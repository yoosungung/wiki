---
id: schedule-outcome-requires-active-ticket
title: "스케줄 결과 기록 전 Active ticket_id 필수"
status: canonical
owner: km
updated: "2026-08-05"
last_updated: "2026-08-05"
review_after: "2026-11-05"
sources:
  - ticket:206
  - ticket:205
tags: ["Engineering", "AI-Native", "Leantime", "Cron", "Tickets"]
type: "wiki"
---

# 스케줄 결과 기록 전 Active ticket_id 필수

일간/주간 잡이 **실제 작업 티켓(Done)**에 보고한 뒤, 성공 체크 세션이 **Active `ticket_id` 없이** `update_ticket`/`add_comment`를 시도하면 `no_active_ticket_for` → Blocked **orphan** 티켓이 생긴다.

## 예방

1. cron/job 프롬프트가 결과 rewrite **전에** Active ticket을 붙이거나, 이미 보고서를 담은 티켓을 canonical로 쓴다.
2. unassigned-triage: orphan은 **Archive** + 큐레이션 owner 배정; 동일 작업을 새 Active로 재개하지 않는다.
3. “작업 성공”과 “티켓 IO 성공”을 분리해 로그한다.

## 🔗 관련 문서

- [[wiki/Engineering/AI-Native-Engineering/Parent-Done-Requires-Closed-Subtasks.md]]
- [[wiki/Engineering/AI-Native-Engineering/Agentic-Software-Factory.md]]
- [[wiki/Engineering/AI-Native-Engineering/Tenant-Quality-Yaml-Gate-Skip-Pattern.md]]
