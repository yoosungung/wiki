---
id: factory-parent-milestone-not-start-gate
title: "Parent milestone ≠ start/unblock gate"
status: canonical
owner: km
updated: "2026-11-12"
last_updated: "2026-11-12"
review_after: "2027-02-12"
sources:
  - inbox/pm/2026-11-11-parent-not-start-gate.md
  - ticket:8ad90d24-dd4b-45cd-9721-42af36295c0d
  - wiki/Engineering/AI-Native-Engineering/FS-Blocked-By-Vs-Parent-Link.md
  - wiki/Engineering/AI-Native-Engineering/Factory-Issue-Details-Parent-Children.md
  - wiki/Engineering/AI-Native-Engineering/Factory-Ticket-Dependencies-SoR.md
tags: ["Engineering", "AI-Native", "Factory", "FS"]
type: wiki
---

# Parent milestone ≠ start/unblock gate

`milestone_id`로 연결된 child는 부모 milestone이 아직 `backlog`여도 `backlog`→`in_progress` PATCH가 된다(API 200; SPA board에 parent-start 게이트 없음).

「시작 안 됨」이 parent hierarchy 탓으로 보이면 대개 (1) assignee=pm intake stub ops, (2) FS `ticket_dependencies` blocked-by — **parent를 선행으로 취급하지 말 것**.

| 관계 | SoR | start/unblock |
| :--- | :--- | :--- |
| Parent/Children | `milestone_id` | 게이트 아님 |
| FS 선행 | `ticket_dependencies` / `set_blocked_by` | 여기만 |

## 관련

- [[wiki/Engineering/AI-Native-Engineering/FS-Blocked-By-Vs-Parent-Link.md]]
- [[wiki/Engineering/AI-Native-Engineering/Factory-Ticket-Dependencies-SoR.md]]
- [[wiki/Engineering/AI-Native-Engineering/Factory-TicketPicker-7d-Combo.md]]
