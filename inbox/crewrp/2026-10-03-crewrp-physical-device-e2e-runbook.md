---
id: inbox-crewrp-physical-device-e2e-runbook
agent: crewrp
ticket_id: c0d87efe-798f-48da-97d3-a0db567b9709
updated: 2026-10-03
status: inbox
sources:
  - ticket:c0d87efe-798f-48da-97d3-a0db567b9709
  - inbox/pm/2026-10-03-crewrp-physical-device-e2e-prep.md
  - wiki/Engineering/Development-Environment/CrewRP-Local-Mobile-Build-Env.md
  - https://developer.android.com/tools/adb
  - https://developer.android.com/studio/debug/dev-options
  - https://developer.android.com/build/building-cmdline
  - https://developer.android.com/studio/run/device
  - https://developer.apple.com/documentation/xcode/enabling-developer-mode-on-a-device
  - https://developer.apple.com/documentation/xcode/running-your-app-on-simulated-or-physical-devices
---

# CrewRP 실기기 설치·CRUD 스모크 런북 (스토어 없음)

기존 canonical `CrewRP-Local-Mobile-Build-Env.md`는 compile/sim 스냅샷. 테넌트 Commands: `android/DESIGN.md`, `ios/DESIGN.md`. 마켓·TestFlight 금지.

## Android (USB debugging → debug APK)

1. 기기: 설정 → 휴대전화 정보 → 빌드 번호 7회 → 개발자 옵션 → **USB debugging** (Android 9+: 시스템 → 고급).
2. 데이터 USB로 연결. 폰에서 Allow USB debugging 승인. `unauthorized`면 케이블 재연결 또는 Revoke USB debugging authorizations.
3. 호스트:
   ```bash
   export PATH="${ANDROID_HOME:-/opt/homebrew/share/android-commandlinetools}/platform-tools:$PATH"
   adb devices -l    # <serial> device
   cd android
   ./gradlew :app:installDebug
   adb -d shell am start -n app.crewrp/.MainActivity
   ```
   `installDebug` 대신 `assembleDebug` 후 `adb -d install -r app/build/outputs/apk/debug/app-debug.apk`도 동일. `-d`는 USB 실기기(에뮬이 있어도).
4. CRUD: `CREWRP_E2E_TOKEN`+`CREWRP_E2E_REPO`로 루트 `scripts/e2e-crud.sh` — `adb devices`에 `device`가 있으면 `DeviceCrudSmokeTest`까지. 에뮬+USB 동시면 `ANDROID_SERIAL=<usb-serial>`. 토큰 없이 할 일까지면 앱 로그인(세션 `project` 스코프) 후 instrument만(DESIGN 주석).
5. 수동 체크리스트: 로그인 → 크루 등록 → 공지·톡·자료·할 일 각 1회 작성·수정·삭제.

## iOS (Developer Mode + Xcode Run)

1. USB 연결, 잠금 해제, Trust This Computer.
2. Xcode로 페어링한 뒤에만 설정 → **개인정보 보호 및 보안 → Developer Mode**. 켜고 Restart → Enable(+암호). Store/TestFlight 설치에는 불필요. 끄면 Xcode Run 불가.
3. `ios/CrewRPApp.xcodeproj`, scheme **`CrewRP`**(파일명과 다름). Signing & Capabilities: Automatically manage signing + Team. destination=실기기 → Run. 번들 `app.crewrp`.
4. CLI: 기기가 `xcrun xctrace list devices`에서 **Offline이 아닐 때** `xcodebuild -project CrewRPApp.xcodeproj -scheme CrewRP -destination 'id=<UDID>'`.
5. Personal Team 개발 프로파일은 약 7일 만료 가능. 유료 Apple Developer는 사람 결정.
6. 코어 CRUD는 호스트 `e2e-crud.sh`(시뮬 불필요). 셸 UI는 위 수동 체크리스트.

## 함정

- USB Trust·Developer Mode 재시작·Apple Team 선택은 사람만 가능.
- 2026-10-03 호스트: `adb devices` 빈 목록. `xctrace`에 BerryKingPhone UDID `00008110-001134A62288201E`는 **Devices Offline** — 설치 스모크 미실행.
