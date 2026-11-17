---
id: inbox-scanbooks-m3-temp-device-smoke-option2
agent: scanbooks
ticket_id: 377c50be-63b7-4293-927b-8886b69c5ce3
updated: 2026-11-18
status: inbox
sources:
  - ticket:377c50be-63b7-4293-927b-8886b69c5ce3
  - https://github.com/yoosungung/scanbooks/pull/19
---

# scanbooks M3 실기기 스모크 — option 2 임시 증거

- Eric 2026-11-17: USB 중급기 대신 sim/emu+fixture 3장 → done+PDF를 임시 증거로 허용.
- iOS: `iPhone 17` Simulator, `DeviceSmokeTempEvidenceTests` PASSED.
- Android: host JVM `DeviceSmokeTempEvidenceTest` PASSED; AVD `Pixel_API_36` inventory OK, adb boot hang this run.
- ROADMAP M3 checkbox closed with drift note; physical USB mid-range remains follow-up.
- PR: https://github.com/yoosungung/scanbooks/pull/19
