---
id: factory-your-work-exclude-done
title: "Factory Your work Assigned: exclude_done"
status: canonical
owner: km
updated: "2026-10-15"
review_after: "2027-01-15"
sources:
  - inbox/pm/2026-10-14-your-work-assigned-hide-done.md
  - inbox/sw-factory/2026-10-14-your-work-exclude-done.md
  - ticket:9d528a70-fbd4-4e8e-a87b-6fa536e690f9
  - wiki/Engineering/AI-Native-Engineering/Factory-Lists-Newest-First.md
tags: ["Engineering", "AI-Native", "Factory", "Your-Work", "API"]
type: "wiki"
---

# Factory Your work Assigned: exclude_done

Your work **Assigned to me**는 예전엔 soft-archive(≥7d `include_archived` / `archivedDoneFilter`)만 제외해 **최근 done**이 남았다. 제품 요구: Assigned에서 `project_statuses.category=done` 전부 숨김 (Created/Viewed/Directory/kanban 불변).

## API

- `GET /api/projects/:id/tickets?exclude_done=true` → category=`done`인 상태를 **나이/key 무관** 제외. soft-archive보다 우선.
- Assigned 탭: `assignee_id=me&exclude_done=true`.

## 함정

- FE-only 필터는 페이지네이션이 recent-done으로 채워져 빈 페이지가 날 수 있음 → **API exclude 우선**.
- 정렬(newest-first)과 별축: [[wiki/Engineering/AI-Native-Engineering/Factory-Lists-Newest-First.md]].
