---
id: crewrp-api-stutter-warm-cache
title: "CrewRP GitHub API UI stutter — app warm-cache fix"
status: canonical
owner: km
updated: "2026-10-09"
review_after: "2027-01-08"
sources:
  - inbox/pm/2026-10-08-crewrp-api-stutter-intake.md
  - inbox/crewrp/2026-10-08-crewrp-api-stutter-fix.md
  - inbox/pm/2026-10-08-crewrp-api-stutter-intent-pass.md
  - inbox/qa/2026-10-08-crewrp-api-stutter-qa-warm-cache.md
  - ticket:605d4aa6-7c55-4be9-a4b3-07213537f031
  - https://github.com/yoosungung/CrewRP/pull/5
  - wiki/Engineering/Development-Environment/CrewRP-PR-Local-Test-Evidence.md
  - wiki/Engineering/Development-Environment/CrewRP-Physical-Device-E2E.md
tags: ["Engineering", "DevEnv", "CrewRP", "API", "Cache"]
type: "wiki"
---

# CrewRP GitHub API UI stutter — app warm-cache fix

증상: GitHub REST/GraphQL 호출 중 앱 UI 멈칫. SoR는 CrewRP `ARCHITECTURE.md` §5(REST ETag/`If-None-Match`, GraphQL freshness). Non-goal: 인프라 SLA·새 프록시·Phase 4 invent(roadmap freeze).

## 원인 분류 (앱 측)

| ID | 원인 | 판정 |
|----|------|------|
| A | iOS MainActor decode | 앱 패치 |
| B | 홈 refresh waterfall | 앱 패치 |
| C | GraphQL freshness 미적용 + Android ETag 미저장 | 앱 패치 |
| D | network/GitHub | 아님 — escalate only via `@eric` |

## 패치 (PR#5 → merge `1700d18`)

- `GraphQLFreshness` TTL **60s**; REST **ETag persist**
- iOS/Android **parallel refresh**; pull-to-refresh `forceNetwork`
- Intent: pass on PR#5 (A/B/C). merge_sha `1700d18789413c7ba3dbeed1c8e5c7dd2631a6c4`

## 검증

- 로컬: `swift test --filter GraphQLFreshness|ETagRESTClient` + full **45 pass**; `./gradlew :crewrp-core:test` green
- Warm-cache: fresh GraphQL skips network (`hits==0`); REST 304/ETag persist
- GHA workflow 0 → 로컬 증거 Intent([[wiki/Engineering/Development-Environment/CrewRP-PR-Local-Test-Evidence.md]])
- 로그인 UI 기기 스모크: BerryKingPhone Offline · `adb devices` empty · `CREWRP_E2E_TOKEN` unset → **N/A** ([[wiki/Engineering/Development-Environment/CrewRP-Physical-Device-E2E.md]])

## 관련

- [[wiki/Engineering/Development-Environment/CrewRP-PR-Local-Test-Evidence.md]]
- [[wiki/Engineering/Development-Environment/CrewRP-Physical-Device-E2E.md]]
