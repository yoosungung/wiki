---
id: factory-quick-create-compact-description
title: "Factory Quick Create: compact Description (F14)"
status: canonical
owner: km
updated: "2026-10-03"
review_after: "2027-01-03"
sources:
  - inbox/pm/2026-10-02-quick-create-description-gap.md
  - inbox/sw-factory/2026-10-02-quick-create-compact-description.md
  - ticket:3acc343b-5a8f-4425-9961-22db33aa3b44
  - frontend/ia/pages.md#F14
tags: ["Engineering", "AI-Native", "Factory", "IA"]
type: "wiki"
---

# Factory Quick Create: compact Description (F14)

IA F14는 Description을 compact Create의 핵심 필드로 둔다. `CreateIssueDialog`는 Summary 바로 아래 Description textarea를 **상시** 노출하고, Status/Start/End만 expand|milestone.

- create payload는 기존 `description` 필드(계약 변경 없음).
- 과거 함정: Description이 `expanded || type==="milestone"`일 때만 렌더되어 Task 생성에서 숨겨짐.
