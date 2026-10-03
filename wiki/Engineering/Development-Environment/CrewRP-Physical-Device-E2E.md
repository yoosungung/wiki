---
id: crewrp-physical-device-e2e
title: "CrewRP 실기기 설치·CRUD 스모크 (스토어 없음)"
status: canonical
owner: km
updated: "2026-10-03"
review_after: "2027-01-03"
sources:
  - inbox/pm/2026-10-03-crewrp-physical-device-e2e-prep.md
  - inbox/crewrp/2026-10-03-crewrp-physical-device-e2e-runbook.md
  - ticket:c0d87efe-798f-48da-97d3-a0db567b9709
  - wiki/Engineering/Development-Environment/CrewRP-Local-Mobile-Build-Env.md
  - https://developer.android.com/studio/run/device
  - https://developer.android.com/tools/adb
  - https://developer.android.com/studio/debug/dev-options
  - https://developer.android.com/build/building-cmdline
  - https://developer.apple.com/documentation/xcode/enabling-developer-mode-on-a-device
  - https://developer.apple.com/documentation/xcode/running-your-app-on-simulated-or-physical-devices
tags: ["Engineering", "DevEnv", "CrewRP", "Mobile", "E2E"]
type: "wiki"
---

# CrewRP 실기기 설치·CRUD 스모크 (스토어 없음)

Play Store / App Store / TestFlight 없이, USB·Xcode 개발 서명으로 Android·iOS **실기기**에 CrewRP를 올리고 CRUD를 반복하는 런북. compile/sim 스냅샷은 [[wiki/Engineering/Development-Environment/CrewRP-Local-Mobile-Build-Env.md]] — 테넌트 명령 정본은 `android/DESIGN.md`, `ios/DESIGN.md`.

## Android (USB debugging → debug APK)

1. 기기에서 Developer options → **USB debugging**. 보이지 않으면 빌드 번호 7회로 개발자 옵션을 연다.
2. 데이터 USB 연결 후 폰에서 Allow USB debugging(RSA) 승인. `unauthorized`면 케이블 재연결 또는 Revoke USB debugging authorizations.
3. macOS는 별도 OEM 드라이버 불필요(공식 *Run apps on a hardware device*). 호스트:

```bash
export PATH="${ANDROID_HOME:-/opt/homebrew/share/android-commandlinetools}/platform-tools:$PATH"
adb devices -l    # <serial> device
cd android
./gradlew :app:installDebug
adb -d shell am start -n app.crewrp/.MainActivity
```

`assembleDebug` 후 `adb -d install -r app/build/outputs/apk/debug/app-debug.apk`와 동등. `adb -d`는 USB 실기기(에뮬이 있어도).

4. CRUD: `CREWRP_E2E_TOKEN`+`CREWRP_E2E_REPO`로 루트 `scripts/e2e-crud.sh` — `adb devices`에 `device`가 있으면 `DeviceCrudSmokeTest`까지. 에뮬+USB 동시이면 `ANDROID_SERIAL=<usb-serial>`. 토큰 없이 UI만이면 앱 로그인 후 수동 체크리스트.
5. 수동: 로그인 → 크루 등록 → 공지·톡·자료·할 일 각 1회 작성·수정·삭제.

## iOS (Developer Mode + Xcode Run)

1. USB 연결, 잠금 해제, Trust This Computer.
2. Xcode로 페어링한 뒤 설정 → **개인정보 보호 및 보안 → Developer Mode**. 켜고 Restart → Enable. Store/TestFlight 설치에는 불필요. 끄면 Xcode Run 불가.
3. `ios/CrewRPApp.xcodeproj`, scheme **`CrewRP`**. Signing: Automatically manage signing + Team. destination=실기기 → Run. 번들 `app.crewrp`.
4. CLI: `xcrun xctrace list devices`에서 **Offline이 아닐 때** `xcodebuild -project CrewRPApp.xcodeproj -scheme CrewRP -destination 'id=<UDID>'`.
5. Personal Team 개발 프로파일은 약 7일 만료 가능. 유료 Apple Developer는 사람 결정.
6. 코어 CRUD는 호스트 `e2e-crud.sh`(시뮬 불필요). 셸 UI는 위 수동 체크리스트.

## 함정

- USB Trust·Developer Mode 재시작·Apple Team 선택은 사람만 가능. 호스트에 기기가 없으면 런북만 두고 설치 스모크는 N/A.
- 2026-10-03 관측: `adb devices` 빈 목록. `xctrace`의 BerryKingPhone UDID `00008110-001134A62288201E`는 Devices Offline — 설치 스모크 미실행.
