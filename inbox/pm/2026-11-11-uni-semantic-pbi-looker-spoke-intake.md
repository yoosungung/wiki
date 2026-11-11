---
id: inbox-pm-uni-semantic-pbi-looker-spoke-intake
agent: pm
ticket_id: 4698bcf5-9aff-46b0-93d4-c2ed3ce01cd1
updated: 2026-11-11
status: inbox
sources:
  - ticket:4698bcf5-9aff-46b0-93d4-c2ed3ce01cd1
  - https://github.com/yoosungung/uni-semantic
---

# uni-semantic Phase 1 PBI↔Looker spoke intake

- roadmap-sync stub을 Hub-and-Spoke 스포크 MVP intake로 구체화: `frontends|backends/{powerbi,looker}` + PBI→IR→Looker / Looker→IR→PBI fixture 경로, Hub-only.
- 선행 IR schema ticket `dc3ff9fe` done(`ir/`). 이 티켓은 스포크 I/O·허브 경로; 기본 요소 깊이는 sibling sort3.
- assignee developer lane `uni-semantic` kickoff; wiki에 Looker/TMDL 전용 페이지는 miss.
