---
id: fs-blocked-by-vs-parent-link
title: "선행은 blocked-by, 부모는 dependingTicketId"
status: canonical
owner: km
updated: "2026-08-13"
last_updated: "2026-08-13"
review_after: "2026-11-13"
sources:
  - ticket:564
tags: ["Engineering", "AI-Native", "PM", "Leantime", "FS"]
type: "wiki"
---

# 선행은 blocked-by, 부모는 dependingTicketId

Finish-to-Start 선행을 **부모/자식 필드**에 넣으면 선행이 Done되어도 자식 링크 때문에 부모 Done이 막힌다.

| 관계 | 필드 | 쓰면 안 되는 때 |
| :--- | :--- | :--- |
| FS 선행 | `set_blocked_by` / `<!-- blocked-by:ID[,ID] -->` | 서브태스크 트리 |
| 부모/서브태스크 | `dependingTicketId` | 선행·unblock |

선행이 모두 Done이면 `set_blocked_by([])`로 마커를 지운 뒤 후속을 연다. 스키마 파일이 안 겹치면 선행을 걸지 않아도 된다 — [[wiki/Agents/Text-to-SQL/Schema-Disjoint-Metadata-Parallel.md]].

## 관련

- [[wiki/Engineering/AI-Native-Engineering/Parent-Done-Requires-Closed-Subtasks.md]]
- [[wiki/Engineering/AI-Native-Engineering/Orphan-Milestone-Close-After-Children-Done.md]]
- [[wiki/Engineering/AI-Native-Engineering/Agentic-Software-Factory.md]]
