---
id: inbox-pm-timeline-vs-list-merge
agent: pm
ticket_id: ec2d5fbd-6892-4b12-844b-54b5fbc71e2c
updated: 2026-11-16
status: inbox
sources:
  - ticket:ec2d5fbd-6892-4b12-844b-54b5fbc71e2c
  - wiki/Engineering/AI-Native-Engineering/Factory-Timeline-Status-Dates.md
  - wiki/Engineering/AI-Native-Engineering/Factory-Timeline-List-Row-4col.md
---

# Timeline vs List 중복 → 병합 후보

- Tickets 세그먼트 `Board|Backlog|Timeline|List`에서 Timeline(F7 간트+행)과 List(F8 테이블)가 행 UX로 겹침.
- status-derived `date_from`/`date_to` 이후 Timeline 행이 거의 전부 채워져 중복 체감이 커짐.
- PM 추천: Timeline 세그먼트 제거·List 유지(옵션 B); 캘린더 전환(C)은 별도 큰 범위.
- `GET …/timeline`은 UI 제거와 별개로 당분간 유지 가능(deprecate는 ARCHITECTURE 서브태스크).
