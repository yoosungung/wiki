---
id: inbox-pm-crewrp-api-stutter-intake
agent: pm
ticket_id: 605d4aa6-7c55-4be9-a4b3-07213537f031
updated: 2026-10-08
status: inbox
sources:
  - ticket:605d4aa6-7c55-4be9-a4b3-07213537f031
  - wiki/Engineering/Development-Environment/CrewRP-PR-Local-Test-Evidence.md
---

# CrewRP GitHub API 호출 UI 멈칫 — PM intake

- 증상: GitHub REST/GraphQL 호출 중 앱 UI 멈칫. 원인 분류 후 앱 측이면 패치.
- SoR: CrewRP `ARCHITECTURE.md` §5 — REST ETag/`If-None-Match`, GraphQL `graphql_cursor` freshness; GHA 0 → 로컬 테스트 증거.
- Non-goal: 인프라 SLA·새 프록시·Phase 4 invent (roadmap freeze).
- Handoff: assignee `crewrp` (lane=developer); escalate `(D) network/GitHub` only via `@eric`.
