---
id: inbox-pm-2026-10-04-roadmap-next-enqueue
agent: pm
ticket_id: f8d92c00-3244-4422-9d3c-053b3672f839
updated: 2026-10-04
status: inbox
sources:
  - ticket:f8d92c00-3244-4422-9d3c-053b3672f839
  - ticket:f9f2416a-dc9c-4fed-8aaf-cfa25022c7c2
  - wiki/Engineering/AI-Native-Engineering/Roadmap-Sync-Unchecked-H2-Gate.md
  - wiki/Engineering/AI-Native-Engineering/Roadmap-Pass-Gate-Human-Approval.md
---

# roadmap-sync: UniTutor 나중 enqueue · CrewRP Phase3 pass-gate

- Registry repos: crewrp, uni-tutor. sw-factory ROADMAP은 표-only라 sync no-op(checkbox 0).
- UniTutor: 1–3단계 티켓 all done → Eric 요청으로 `### 나중` 스코프를 milestone+자식 티켓화. 첫 actionable: ROADMAP `##`+checklist 형식.
- CrewRP: Phase1–3 all `[x]`, next `###` 없음 → pass-gate Waiting for Approval(@eric). 승인 전 enqueue 금지.
- 함정: zsh가 heredoc 안 `[x]`/`###`를 glob/파싱해 description 손상 가능 → JSON 파일로 API body 작성.
