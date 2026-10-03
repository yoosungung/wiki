---
id: factory-done-ticket-purge
title: "Factory Done 티켓: 7일 archived · 28일 purge"
status: canonical
owner: km
updated: "2026-10-04"
review_after: "2027-01-04"
sources:
  - inbox/pm/2026-10-03-ticket-lifecycle-retention.md
  - inbox/pm/2026-10-03-ticket-lifecycle-eric-decisions.md
  - inbox/pm/2026-10-03-done-ticket-purge-intent.md
  - inbox/sw-factory/2026-10-03-done-ticket-purge.md
  - ticket:5c9b127e-fe73-4268-85e7-819a14542c0a
  - https://github.com/yoosungung/sw-factory/pull/34
tags: ["Engineering", "AI-Native", "Factory", "D1", "Retention"]
type: "wiki"
---

# Factory Done 티켓: 7일 archived · 28일 purge

## 계약 (Eric 결정 · shipped)

| 단계 | 의미 | 시계 |
| --- | --- | --- |
| 7일 archived Done | **별도 status 아님**. `category=done` + 조회 필터(`DONE_ARCHIVE_DAYS=7`, `include_archived=true`) | `tickets.updated_at` |
| 28일 물리 삭제 | hourly Cron (`DONE_PURGE_DAYS=28`) | 동일 — 코멘트 INSERT는 시계를 안 밈 |

## 삭제 범위

- comments / files(+R2) / pending_uploads / `agent_event_log`: tickets FK가 없어 purge가 **명시 DELETE**(+R2).
- `ticket_activities` / `ticket_dependencies`: ticket DELETE CASCADE.
- 마일스톤 purge ↔ 자식: 자식 `milestone_id` SET NULL만(연쇄 삭제 없음). 태스크 purge는 부모 마일스톤을 지우지 않음.

## 함정

- 초기 inbox는 “28일 미구현·Eric 게이트”였으나 PR #34로 **구현됨** — retention 초안과 intent/shipped를 이 페이지로 병합.
- archive/purge가 `updated_at`이면 done 이후 패치가 컷오프를 민다(코멘트는 제외).
