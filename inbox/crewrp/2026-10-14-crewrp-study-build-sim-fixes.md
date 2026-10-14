---
id: inbox-crewrp-study-build-sim-fixes
agent: crewrp
ticket_id: 919b497c-16c9-4edb-a689-780c5b736d6a
updated: 2026-10-14
status: inbox
sources:
  - ticket:919b497c-16c9-4edb-a689-780c5b736d6a
  - https://github.com/yoosungung/CrewRP/pull/9
  - wiki/Engineering/Development-Environment/CrewRP-Local-Mobile-Build-Env.md
---

# CrewRP Study build/sim 회귀 수정 (2026-10-14)

- Android Study Dialog: Compose `Surface` 인자명은 `modifier=` (대문자 `Modifier=`는 compile 실패).
- iOS Swift 6: `Regex` 글로벌 `let`은 non-Sendable → `parseSubtitles` 지역으로 이동.
- Study canvas: Home/Study 이중 `fullScreenCover`면 학습 탭에서 캔버스가 안 뜸 → RootView 단일 `fullScreenCover(item:)`.
- 온보딩 CTA 「첫 주 경로 보기」는 List row 안 `borderedProminent`보다 List 밖 VStack footer가 Maestro/탭에 안정적.
- 검증 스냅샷: Xcode 26.6 / Temurin 17 / iPhone 17 sim — wiki `CrewRP-Local-Mobile-Build-Env`와 정합.
