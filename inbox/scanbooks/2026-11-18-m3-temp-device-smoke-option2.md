---
id: inbox-scanbooks-m3-temp-device-smoke-option2
agent: scanbooks
ticket_id: 377c50be-63b7-4293-927b-8886b69c5ce3
updated: 2026-11-18
status: inbox
sources:
  - ticket:377c50be-63b7-4293-927b-8886b69c5ce3
  - ticket:de05921c-ffdf-41ef-88d7-2053f9a7dd9c
  - wiki/Engineering/Development-Environment/CrewRP-Physical-Device-E2E.md
---

# Scanbooks M3 실기기 스모크 — option 2 임시 증거

- Eric 2026-11-17: USB 중급기 없을 때 **시뮬/에뮬 + fixture 3장 → done+PDF**를 M3 게이트 임시 증거로 허용.
- 증거 테스트: `DeviceSmokeTempEvidenceTests` (iPhone 17 Simulator) · `DeviceSmokeTempEvidenceTest` (Pixel_API_36 host unit path).
- ROADMAP checkbox는 drift 문구 포함 체크; 물리 중급기 USB는 후속 게이트.
- 패턴: CrewRP physical-device E2E와 동일 — 기기 없으면 N/A/임시 경로 명시.
