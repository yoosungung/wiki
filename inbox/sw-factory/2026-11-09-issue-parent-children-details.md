---
id: inbox-sw-factory-issue-parent-children-details
agent: sw-factory
ticket_id: e3b3067e-f9ac-419f-a622-9ce8b45a270d
updated: 2026-11-09
status: inbox
sources:
  - ticket:e3b3067e-f9ac-419f-a622-9ce8b45a270d
  - wiki/Engineering/AI-Native-Engineering/FS-Blocked-By-Vs-Parent-Link.md
  - wiki/Engineering/AI-Native-Engineering/Factory-Ticket-Dependencies-SoR.md
---

# Issue Details Parent/Children (Option A)

- SPA Issue Details에 Parent/Children을 `milestone_id`로 표시·편집한다. FS Blocked by(`ticket_dependencies`)와 UI를 분리한다.
- 각 행은 **id 앞 8자 + title**; parent는 PATCH `milestone_id`, children은 `GET …/tickets?milestone_id=` + Add child 시 자동 연결.
- Board/List 트리·필터 그룹은 Option B로 남겨 두었다.
