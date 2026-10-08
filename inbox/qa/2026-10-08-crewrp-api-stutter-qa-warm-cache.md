---
id: inbox-qa-crewrp-api-stutter-warm-cache
agent: qa
ticket_id: 605d4aa6-7c55-4be9-a4b3-07213537f031
updated: 2026-10-08
status: inbox
sources:
  - ticket:605d4aa6-7c55-4be9-a4b3-07213537f031
  - wiki/Engineering/Development-Environment/CrewRP-PR-Local-Test-Evidence.md
  - wiki/Engineering/Development-Environment/CrewRP-Physical-Device-E2E.md
---

# CrewRP API stutter — QA warm-cache

- merge_sha `1700d18`: iOS `swift test --filter GraphQLFreshness|ETagRESTClient` + full 45 pass; Android `:crewrp-core:test` green — fresh GraphQL skips network (`hits==0`), REST 304/`ETag` persist.
- 로그인 UI 기기 스모크: BerryKingPhone Offline · `adb devices` empty · `CREWRP_E2E_TOKEN` unset → N/A (Physical-Device-E2E 런북).
