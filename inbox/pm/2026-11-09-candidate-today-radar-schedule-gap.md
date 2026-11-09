---
id: inbox-pm-candidate-today-radar-schedule-gap
agent: pm
ticket_id: 25d4ee1e-0e76-4ddd-ae12-fedb8ab351a8
updated: 2026-11-09
status: inbox
sources:
  - ticket:25d4ee1e-0e76-4ddd-ae12-fedb8ab351a8
  - wiki/Engineering/AI-Native-Engineering/Publication-Gate-Empty-Overwrite-Guard.md
---

# candidate.win 오늘의 화제 스케줄 갭

- `/today/` 데이터(`wiki/data/today.yaml`)는 `issue_radar` → `publish_today` 파이프라인 산출물이다. Pass A(`deep_agent --all`)와 별개다.
- 최종 agent 갱신: 2026-09-22. 이후 factory 이식 구간에서 `schedule:issue-radar-today-0800-kst`가 `agents.yaml`에 없다.
- 호스트 LaunchAgent는 `com.candydate.research`(Pass A 09:00 KST)만 등록됨. issue-radar 런처 없음.
- factory candidate 스케줄은 `candidate-escalation-drain`만 존재(escalation 큐).
- 재가동 옵션: host launchd 복구 / factory schedule(+Leantime 의존 제거) / 당분간 비활성.
