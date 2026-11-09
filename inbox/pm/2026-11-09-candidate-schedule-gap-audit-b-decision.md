---
id: inbox-pm-candidate-schedule-gap-audit-b-decision
agent: pm
ticket_id: 25d4ee1e-0e76-4ddd-ae12-fedb8ab351a8
updated: 2026-11-09
status: inbox
sources:
  - ticket:25d4ee1e-0e76-4ddd-ae12-fedb8ab351a8
  - ticket:4c4301a0-10bd-4525-8fc5-0381e1721303
  - wiki/Engineering/AI-Native-Engineering/Publication-Gate-Empty-Overwrite-Guard.md
  - deploy/agents.yaml
---

# candidate 스케줄 갭 감사 + B 결정

- eric 결정 **B**: factory `agents.yaml`에 issue-radar/today 스케줄 복구. Leantime 폐기·복귀 불가.
- 자식 티켓 `4c4301a0` (candidate, in_progress): radar → publish_today → `today.yaml` push.
- **중단 확인**: `issue-radar-today` (`today.yaml` 2026-09-22), `publication-safety`(~2026-09-02 이후 공백), `people-ssot-curation-18h`(전용 스케줄 없음; Pass A가 people 일부 갱신).
- **의도적/범위 외**: `ta-k8s-daily` 주석, `spend-alert`는 factory schedules 밖.
- Host launchd: `com.candydate.research`(Pass A)만.
