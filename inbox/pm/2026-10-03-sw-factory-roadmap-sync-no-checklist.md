---
id: inbox-pm-sw-factory-roadmap-sync-no-checklist
agent: pm
ticket_id: schedule:pm-roadmap-sync
updated: 2026-10-03
status: inbox
sources:
  - schedule:pm-roadmap-sync
  - wiki/Engineering/AI-Native-Engineering/Roadmap-Sync-Unchecked-H2-Gate.md
  - wiki/Engineering/AI-Native-Engineering/Roadmap-Pass-Gate-Human-Approval.md
  - file:ROADMAP.md
  - file:.cursor/roadmap-registry.json
---

# sw-factory ROADMAP sync: 체크리스트 없음 → no passed section

- `pm-roadmap-sync`는 `##` + `- [ ]`/`- [x]`만 enqueue한다. 테이블 `상태|done`·plain bullet은 sync 대상이 아님.
- 2026-10-03 local `ROADMAP.md`: 모든 `##`에 checkbox 0 → incomplete current 없음, all-`[x]` passed 없음 → **skip: no passed section** (pass-gate 티켓 미생성).
- registry `git_repo_url`이 `https://github.com/example/sw-factory.git` placeholder라 clone 실패; `project_id`/`client_id`도 nil UUID. 실프로젝트 id는 factory `sw-factory` = `8a927848-4411-42a8-8508-f7b8efb3ec60`.
- 다음 sync를 살리려면 ROADMAP을 `## …` + `- [ ]`/`- [x]`로 바꾸거나, registry URL·project_id를 실값으로 고친다.
