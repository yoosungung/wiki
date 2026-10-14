---
id: crewrp-study-build-sim-regressions
title: "CrewRP Study tip: 빌드·시뮬 회귀 함정"
status: canonical
owner: km
updated: "2026-10-15"
review_after: "2027-01-15"
sources:
  - inbox/crewrp/2026-10-14-crewrp-study-build-sim-fixes.md
  - inbox/pm/2026-10-14-crewrp-study-build-sim-intent-pass.md
  - inbox/pm/2026-10-14-crewrp-study-build-sim-intake.md
  - ticket:919b497c-16c9-4edb-a689-780c5b736d6a
  - https://github.com/yoosungung/CrewRP/pull/9
  - wiki/Engineering/Development-Environment/CrewRP-Local-Mobile-Build-Env.md
  - wiki/Engineering/Development-Environment/CrewRP-Physical-Device-E2E.md
tags: ["Engineering", "DevEnv", "CrewRP", "Study", "Mobile"]
type: "wiki"
---

# CrewRP Study tip: 빌드·시뮬 회귀 함정

Ad-hoc 검증(티켓 `919b497c`, CrewRP PR #9 → `e5fd692`): main tip Study(S7-07·S7-10–14) 로컬 빌드 green + 시뮬 학습 스모크. 호스트 툴체인: [[wiki/Engineering/Development-Environment/CrewRP-Local-Mobile-Build-Env.md]] (Xcode 26.6 / Temurin 17 / iPhone 17 sim).

## Done 게이트 (`tenant_cd` N/A)

- crewrp는 `tenant_cd` 미등록 → Done에 qa/aa/prod 게이트 N/A.
- Local validation: `intent: pass` + merge면 `test:`(Android/iOS build + ≥1 platform Study smoke)로 Done 충분.

## 흔한 회귀

| 축 | 증상 | 고침 |
|----|------|------|
| Android Compose | `Surface(Modifier=…)` compile 실패 | 인자명 `modifier=` (소문자) |
| iOS Swift 6 | 글로벌 `let` `Regex` → non-Sendable | `parseSubtitles` 등 **지역**으로 이동 |
| Study canvas | Home/Study 이중 `fullScreenCover` → 학습 탭에서 캔버스 안 뜸 | RootView 단일 `fullScreenCover(item:)` |
| 온보딩 CTA | List row 안 `borderedProminent` 탭 불안정 | List 밖 VStack footer |

## AC 힌트

- 시뮬 로그인 없으면 번들 폴백 학습 경로로 AC; 세션 필수면 `@eric`.
- Assignee `lane=developer` → `crewrp`.
