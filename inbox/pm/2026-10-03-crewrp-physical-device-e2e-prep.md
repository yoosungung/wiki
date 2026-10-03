---
id: inbox-pm-crewrp-physical-device-e2e-prep
agent: pm
ticket_id: c0d87efe-798f-48da-97d3-a0db567b9709
updated: 2026-10-03
status: inbox
sources:
  - ticket:c0d87efe-798f-48da-97d3-a0db567b9709
  - wiki/Engineering/Development-Environment/CrewRP-Local-Mobile-Build-Env.md
  - https://developer.android.com/tools/adb
  - https://developer.android.com/build/building-cmdline
  - https://developer.apple.com/documentation/xcode/enabling-developer-mode-on-a-device
  - https://developer.apple.com/documentation/xcode/running-your-app-on-simulated-or-physical-devices
---

# CrewRP 실기기 E2E 준비 (스토어 미등록)

- 기존 canonical `CrewRP-Local-Mobile-Build-Env.md`는 compile/unit/sim 스냅샷이며 **실기기 install/E2E는 범위 밖**이라고 명시함.
- 테넌트 `android/DESIGN.md`는 이미 `adb install` + `DeviceCrudSmokeTest` 명령을 에뮬 기준으로 둠. 실기기도 같은 adb 경로가 가능(USB debugging).
- Android: Developer options → USB debugging, `adb devices` 승인 후 debug APK 설치. Play Store 불필요. 공식: `adb` / `gradlew installDebug`.
- iOS: App Store/TestFlight가 아니라 Xcode Run(development-signed). 기기 Developer Mode(Settings → Privacy & Security) + 페어링/Trust + Automatic signing. Developer Mode는 Store/TestFlight 설치에는 필요 없음.
- Non-goal: 마켓 등록(Play/App Store), TestFlight 배포.
- 함정: 실기기 USB 신뢰·Apple 팀 서명·Developer Mode 재시작은 사람 조작. 에이전트에 기기가 없으면 런북만 쓰고 설치 스모크는 blocker.
