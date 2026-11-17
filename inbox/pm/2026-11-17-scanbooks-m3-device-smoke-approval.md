---
id: inbox-pm-scanbooks-m3-device-smoke-approval
agent: pm
ticket_id: 377c50be-63b7-4293-927b-8886b69c5ce3
updated: 2026-11-17
status: inbox
sources:
  - ticket:377c50be-63b7-4293-927b-8886b69c5ce3
  - wiki/Engineering/Development-Environment/CrewRP-Physical-Device-E2E.md
---

# Scanbooks M3 실기기 스모크 = 사람 하드웨어 게이트

- ROADMAP「실기기 스모크(중급기 1대 이상/플랫폼)」은 시뮬/에뮬로 AC 충족 불가.
- 호스트 probe empty(`adb`/`xctrace` sim-only)면 IC는 options만 남기고 `waiting_for_approval` → admin.
- 선택지: (1) USB 중급기 attach (2) 시뮬+fixture를 Intent drift로 임시 허용 (3) hold/pass-gate 분리.
- CrewRP 동일: 기기 없으면 설치 스모크 N/A — 런북만.
