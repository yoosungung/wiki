---
id: factory-issue-details-parent-children
title: "Factory SPA: Issue Details Parent/Children (milestone_id)"
status: canonical
owner: km
updated: "2026-11-10"
last_updated: "2026-11-10"
review_after: "2027-02-10"
sources:
  - inbox/sw-factory/2026-11-09-issue-parent-children-details.md
  - inbox/pm/2026-11-09-parent-child-fe-intake.md
  - inbox/pm/2026-11-09-parent-child-fe-option-a.md
  - ticket:e3b3067e-f9ac-419f-a622-9ce8b45a270d
  - wiki/Engineering/AI-Native-Engineering/FS-Blocked-By-Vs-Parent-Link.md
  - wiki/Engineering/AI-Native-Engineering/Factory-Ticket-Dependencies-SoR.md
tags: ["Engineering", "AI-Native", "Factory", "SPA", "milestone"]
type: wiki
---

# Factory SPA: Issue Details Parent/Children (milestone_id)

Option A: Issue Details에 Parent/Children을 **`milestone_id`**로 표시·편집한다. FS Blocked by(`ticket_dependencies`) UI와 **분리**.

| UI | 동작 |
| :--- | :--- |
| 행 표시 | id 앞 8자 + title |
| Parent | PATCH `milestone_id` |
| Children | `GET …/tickets?milestone_id=` + Add child 시 자동 연결 |
| Non-goal (Option B) | Board/List 트리·필터 그룹 |

Leantime `dependingTicketId` 함정 문서([[wiki/Engineering/AI-Native-Engineering/FS-Blocked-By-Vs-Parent-Link.md]])와 축이 같다: **부모 링크 ≠ FS 선행**.

## 관련

- [[wiki/Engineering/AI-Native-Engineering/Factory-Ticket-Dependencies-SoR.md]]
- [[wiki/Engineering/AI-Native-Engineering/Parent-Done-Requires-Closed-Subtasks.md]]
- [[wiki/Engineering/AI-Native-Engineering/FS-Blocked-By-Vs-Parent-Link.md]]
