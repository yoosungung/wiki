---
id: crewrp-local-mobile-build-env
title: "CrewRP 로컬 iOS·Android 빌드 환경 (macOS)"
status: canonical
owner: km
updated: "2026-10-03"
review_after: "2027-01-03"
sources:
  - inbox/crewrp/2026-10-02-crewrp-local-mobile-build-env.md
  - ticket:f7e03d5c-a652-4a43-98c7-9182f64bbbcd
  - repo:yoosungung/crewrp@e1e945a
tags: ["Engineering", "DevEnv", "CrewRP", "Mobile"]
type: "wiki"
---

# CrewRP 로컬 iOS·Android 빌드 환경 (macOS)

`yoosungung/crewrp` `main`@`e1e945a`에서 DESIGN Commands 기준 로컬 빌드·단위테스트 통과 관측(2026-10-02).

| 항목 | 값 |
|------|-----|
| macOS | 26.7.1 (arm64) |
| Xcode | 26.6 (17F113) |
| Swift | 6.3.3 |
| JDK | Temurin 17 |
| ANDROID_HOME | `/opt/homebrew/share/android-commandlinetools` |
| platforms / build-tools | android-35·36 / 35.0.0·36.0.0 |
| AVD | Pixel_API_36 (Android 16 google_apis/arm64-v8a) |
| iOS sim | iPhone 17 등 (iOS 26.5) |

앱 `compileSdk`/`targetSdk`=35, `minSdk`=26. `local.properties` 없어도 `ANDROID_HOME`으로 assemble 성공.

## 검증 명령 (관측)

- Android: `cd android && ./gradlew :crewrp-core:test :app:assembleDebug` → BUILD SUCCESSFUL (crewrp-core tests=40 fail=0)
- iOS core: `cd ios && swift test` → 38 tests / 18 suites (CrudE2E 4건 skipped — 토큰 필요)
- iOS app: `xcodebuild -project CrewRPApp.xcodeproj -scheme CrewRP -destination 'platform=iOS Simulator,name=iPhone 17' build` → BUILD SUCCEEDED

## 함정

- Xcode 프로젝트 파일명은 `CrewRPApp.xcodeproj`이나 **scheme/target 이름은 `CrewRP`** (`CrewRPApp` 스킴 없음).
- 에뮬레이터 기동·실기기 install/E2E는 이 스냅샷 범위 밖(compile/test만). 실기기 런북: [[wiki/Engineering/Development-Environment/CrewRP-Physical-Device-E2E.md]]
- Host toolchain 스냅샷 — CI/remote와 버전 드리프트 시 이 표를 갱신.
