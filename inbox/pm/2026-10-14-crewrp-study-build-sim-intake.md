---
id: inbox-pm-2026-10-14-crewrp-study-build-sim-intake
agent: pm
ticket_id: 919b497c-16c9-4edb-a689-780c5b736d6a
updated: 2026-10-14
status: inbox
sources:
  - ticket:919b497c-16c9-4edb-a689-780c5b736d6a
  - repo:yoosungung/crewrp@7ad6752
  - wiki/Engineering/Development-Environment/CrewRP-Local-Mobile-Build-Env.md
  - wiki/Engineering/Development-Environment/CrewRP-Physical-Device-E2E.md
---

# CrewRP Study main 빌드·시뮬 intake

- Ad-hoc 티켓: main tip Study(S7-07·S7-10–14) 빌드 green + 시뮬 학습 스모크 → 깨짐 최소 수정.
- Assignee `lane=developer` → `crewrp`; status `in_progress`.
- crewrp는 `tenant_cd` 미등록 → Done에 qa/aa/prod 게이트 N/A; `test:` + 필요 시 `pr_url`만.
- 시뮬 로그인 없으면 번들 폴백 학습 경로로 AC; 세션 필수면 `@eric`.
