---
id: inbox-pm-roadmap-sync-checkbox-gate
agent: pm
ticket_id: 
updated: 2026-08-06
status: inbox
sources:
  - file:~/.cursor/roadmap-registry.json
  - file:codingland/ROADMAP.md
  - skill:leantime-pm/references/roadmap-sync.md
---

# ROADMAP sync는 `- [ ]` 체크리스트만 인식

- `pm-roadmap-sync`는 `##` 섹션 중 첫 미완료 `- [ ]` 섹션만 enqueue. `###` 하위·일반 `-` bullet은 무시.
- codingland `ROADMAP.md`(2026-08-06)는 `## 마일스톤` 아래 `### M0…M4` + plain bullet만 있어 sync가 no-op(티켓 0).
- 문서 서술(M0 Done / M1 착수)만으로는 Leantime 티켓을 만들지 않음. 동기화하려면 current milestone을 `##` + `- [ ]`/`- [x]`로 바꿔야 함.
