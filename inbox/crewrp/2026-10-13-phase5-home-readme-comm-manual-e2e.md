---
id: inbox-crewrp-phase5-home-readme-comm-manual-e2e
agent: crewrp
ticket_id: d13290fa-bf2f-4f41-ac2a-e5d9db243eea
updated: 2026-10-13
status: inbox
sources:
  - ticket:d13290fa-bf2f-4f41-ac2a-e5d9db243eea
  - wiki/Engineering/Development-Environment/CrewRP-Physical-Device-E2E.md
  - wiki/Engineering/Development-Environment/CrewRP-Discord-OAuth-Manual-E2E.md
tags: [CrewRP, Phase5, E2E, Discussions]
---

# CrewRP Phase 5 manual E2E (홈 README · 소통)

- Env: iPhone 17 Simulator (iOS 26.5) · crew `yoosungung/ai-edu` · OAuth-scope token (`gho_` / `repo`)
- AC1 홈: `소개` 섹션에 repo root README Contents 렌더 (`하이 방가워요`)
- AC2 소통: Discord 상단(바로 대화·연결 UI) + Discussions 카테고리(Announcements/General/…) → 글 목록·상세 시트 열람
- CRUD: 호스트 `swift test --filter CrudE2ETests` notice create/update/delete 통과(앱과 동일 `DiscussionsClient`)
- 함정: fine-grained `github_pat_` 는 Discussions `FORBIDDEN`(nodes null). Maestro `launchApp`이 셸 `GH_TOKEN`(pat)로 fallback을 덮으면 카테고리 로드 실패로 보임 — E2E 시 `gho_` 주입 후 relaunch 없이 탭 검증
- Maestro+SwiftUI TextField `inputText`는 @State 미반영 → UI 작성은 빈 title로 `invalidResponse` 가능; CRUD 증거는 CrudE2E/API로 보완
