---
id: inbox-pm-backlog-timeline-page-scroll-gap
agent: pm
ticket_id: 8d8acba4-c49a-421a-9255-5bafd72f8706
updated: 2026-10-04
status: inbox
sources:
  - ticket:8d8acba4-c49a-421a-9255-5bafd72f8706
  - ticket:84aa1cd4-5ebc-4e5d-ad11-b23e2a63d75b
  - wiki/Engineering/AI-Native-Engineering/Factory-SPA-Page-Scroll.md
tags: ["Engineering", "Factory", "SPA", "scroll"]
---

# Backlog/Timeline missing `.page-scroll`

## Summary
Factory SPA `.main { overflow: hidden }` + `.page-scroll` 패턴이 List/Overview/`/projects`에는 적용됐으나 Tickets **Backlog**·**Timeline**은 `.backlog` / `.content-panel`만 감싸 본문이 잘린다.

## Gap vs canonical
`Factory-SPA-Page-Scroll.md` 적용 표면에 Backlog(`?view=backlog`)·Timeline(`?view=timeline`)이 빠져 있음. 선행 84aa1cd4는 projects 목록·정렬 중심.

## Suggested promote
canonical 표에 두 뷰 행 추가 + IC 패치 후 PR 링크.
