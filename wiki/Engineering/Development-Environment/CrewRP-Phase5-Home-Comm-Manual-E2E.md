---
id: crewrp-phase5-home-comm-manual-e2e
title: "CrewRP Phase 5: 홈 README · 소통 Discord/Discussions 수동 E2E"
status: canonical
owner: km
updated: "2026-10-13"
review_after: "2027-01-13"
sources:
  - inbox/pm/2026-10-13-crewrp-phase5-intake.md
  - inbox/crewrp/2026-10-13-phase5-home-comm-manual-e2e.md
  - inbox/crewrp/2026-10-13-phase5-home-readme-comm-manual-e2e.md
  - ticket:10fe0055-84a9-47c1-9e2c-5ca3f638c51a
  - ticket:d13290fa-bf2f-4f41-ac2a-e5d9db243eea
  - wiki/Engineering/Development-Environment/CrewRP-Physical-Device-E2E.md
  - wiki/Engineering/Development-Environment/CrewRP-Discord-OAuth-Manual-E2E.md
tags: ["Engineering", "DevEnv", "CrewRP", "Phase5", "E2E", "Discussions"]
type: "wiki"
---

# CrewRP Phase 5: 홈 README · 소통 Discord/Discussions 수동 E2E

ROADMAP current `## Phase 5 — 소통 허브 + 홈 README`. 코드 체크박스는 이미 `[x]`; 남은 일은 **수동 E2E**. Phase 4 Discord OAuth 런북: [[wiki/Engineering/Development-Environment/CrewRP-Discord-OAuth-Manual-E2E.md]].

## 티켓 축

| 역할 | id | marker |
|------|-----|--------|
| Parent milestone | `10fe0055` | `roadmap:crewrp:milestone:phase-5-comm-hub-home-readme` |
| Child | `d13290fa` | `roadmap:crewrp:home-readme-comm-category-manual-e2e` |

Done gate: child `test:` → parent Intent/`done`. `tenant_cd` N/A.

## Sim 증거 (iPhone 17 · crew `yoosungung/ai-edu`)

1. **홈 README**: `소개` 섹션에 repo root README Contents 렌더 (`하이 방가워요`).
2. **소통 Discord 상단**: 「바로 대화」·연결 UI까지 Maestro pass (세션/`GH_TOKEN` fallback 주입).
3. **Discussions**: 호스트 `hasDiscussionsEnabled=true`이나 fine-grained `github_pat_`는 GraphQL `discussionCategories` **FORBIDDEN** → 앱 UI「카테고리를 불러오지 못했습니다.」
4. OAuth-scope `gho_`(`repo`) 주입 후: 카테고리(Announcements/General/…) → 글 목록·상세 시트 열람.
5. CRUD: `swift test --filter CrudE2ETests` notice create/update/delete 통과(앱과 동일 `DiscussionsClient`).

## 함정

- Maestro `launchApp`이 셸 `GH_TOKEN`(pat)로 fallback을 덮으면 카테고리 로드 실패로 보임 — E2E 시 `gho_` 주입 후 relaunch 없이 탭 검증.
- Maestro+SwiftUI TextField `inputText`는 `@State` 미반영 → UI 작성은 빈 title로 `invalidResponse` 가능; CRUD 증거는 CrudE2E/API로 보완.
- 앱 OAuth scope `read:org repo project` — Discussions 카테고리·글 CRUD AC는 **사람 Safari GitHub 재로그인**(또는 Discussions 권한 토큰) 게이트. Discord 재검증은 Phase 5 AC blocker 아님.
- 시크릿·PAT 본문은 wiki에 기록하지 않는다.
