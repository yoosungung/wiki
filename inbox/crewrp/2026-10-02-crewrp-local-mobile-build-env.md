---
id: inbox-crewrp-crewrp-local-mobile-build-env
agent: crewrp
ticket_id: f7e03d5c-a652-4a43-98c7-9182f64bbbcd
updated: 2026-10-02
status: inbox
sources:
  - ticket:f7e03d5c-a652-4a43-98c7-9182f64bbbcd
  - repo:yoosungung/crewrp@e1e945a
---

# CrewRP 로컬 iOS·Android 빌드 환경 (macOS host)

## 요약

`yoosungung/crewrp` `main`@`e1e945a`에서 DESIGN Commands 기준 로컬 빌드·단위테스트가 통과했다.

## Host toolchain (관측)

| 항목 | 값 |
|------|-----|
| macOS | 26.7.1 (arm64) |
| Xcode | 26.6 (Build 17F113) |
| Swift | 6.3.3 |
| JDK | Temurin 17.0.20.1 |
| ANDROID_HOME | `/opt/homebrew/share/android-commandlinetools` |
| platforms | android-35, android-36 |
| build-tools | 35.0.0, 36.0.0 |
| AVD | Pixel_API_36 (Android 16 google_apis/arm64-v8a) |
| iOS sim | iPhone 17 등 (iOS 26.5) available |

앱 `compileSdk`/`targetSdk`=35, `minSdk`=26. `local.properties` 없어도 `ANDROID_HOME`으로 assemble 성공.

## 검증 명령·결과

- Android: `cd android && ./gradlew :crewrp-core:test :app:assembleDebug` → **BUILD SUCCESSFUL** (crewrp-core tests=40 fail=0), `app-debug.apk` ~20MB
- iOS core: `cd ios && swift test` → **38 tests / 18 suites passed** (CrudE2E 4건 skipped — 토큰 필요)
- iOS app: `xcodebuild -project CrewRPApp.xcodeproj -scheme CrewRP -destination 'platform=iOS Simulator,name=iPhone 17' build` → **BUILD SUCCEEDED**

## 메모

- Xcode 프로젝트 파일명은 `CrewRPApp.xcodeproj`이나 **scheme/target 이름은 `CrewRP`** (CrewRPApp 스킴 없음).
- 에뮬레이터 기동·실기기 install/E2E는 이번 티켓 범위에서 미실행(compile/test만).
