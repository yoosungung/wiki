---
id: inbox-crewrp-api-stutter-fix
agent: crewrp
ticket_id: 605d4aa6-7c55-4be9-a4b3-07213537f031
updated: 2026-10-08
status: inbox
sources:
  - ticket:605d4aa6-7c55-4be9-a4b3-07213537f031
  - https://github.com/yoosungung/CrewRP/pull/5
  - wiki/Engineering/Development-Environment/CrewRP-PR-Local-Test-Evidence.md
---

# CrewRP GitHub API UI stutter — app-side fix

- 원인: (A) iOS MainActor decode, (B) 홈 refresh waterfall, (C) GraphQL freshness 미적용 + Android ETag 미저장. (D) 아님.
- 패치: `GraphQLFreshness` TTL 60s; REST ETag persist; iOS/Android parallel refresh; pull-to-refresh `forceNetwork`.
- 검증: `swift test` 45 pass; `./gradlew :crewrp-core:test` green. GHA 0 → 로컬 증거 Intent.
