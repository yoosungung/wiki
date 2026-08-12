---
id: inbox-codingland-m31-sanitizer-tests
agent: codingland
ticket_id: 543
updated: 2026-08-12
status: inbox
sources:
  - ticket:543
  - wiki/Engineering/AI-Native-Engineering/Soft-TTD-In-Process-Replay-Sandbox.md
  - https://github.com/veryfront/veryfront-code/blob/main/src/utils/logger/redact.test.ts
---

# M3.1 Sanitizer 회귀 테스트 (codingland)

- ARCHITECTURE §4.5: namePatterns는 substring+대소문자; astSensitiveParams는 exact key; depth≤3에서 배열도 동일 예산; redact 시 하위 미탐색.
- 회귀에 넣을 축: 입력 비변이, root array, `DEFAULT_SANITIZE_OPTIONS` 공용(Runner·Mirror 경로).
- 로컬 extension Jest만이면 tenant_cd/QA/AA prod 게이트는 Soft-TTD wiki 기준 N/A.
