---
id: wiki-mobile-app-store-deploy-costs
title: "iOS·Android 마켓플레이스 배포 절차와 비용"
status: canonical
owner: km
updated: 2026-09-28
review_after: 2027-03-28
tags: ["App-Store", "Google-Play", "Mobile", "Deploy", "Pricing", "CrewRP"]
sources:
  - ticket:25c4a7a9-6ba2-4a55-9e0c-a58ffd4fd329
  - https://developer.apple.com/programs/whats-included/
  - https://developer.apple.com/help/account/membership/program-enrollment
  - https://developer.apple.com/testflight/
  - https://support.google.com/googleplay/android-developer/answer/6112435
  - https://developer.android.com/blog/posts/expanded-billing-choice-and-lower-fees-on-google-play
---

# iOS·Android 마켓플레이스 배포 절차와 비용

CrewRP 등 **소비자/조직용 네이티브 앱**을 Apple App Store·Google Play에 올리기 위한 **계정 비용·수수료·최소 절차** 요약. (2026-09-28 기준; 수수료는 지역·프로그램별로 자주 바뀌므로 `review_after` 전에 공식 링크를 재확인.)

## 1. 고정 계정 비용 (배포 자격)

| 스토어 | 비용 | 주기 | 비고 |
|--------|------|------|------|
| **Apple Developer Program** | **99 USD**/멤버십 연 | 연간 갱신 | App Store·TestFlight·서명·팀 관리. [공식](https://developer.apple.com/programs/whats-included/) |
| Apple Developer **Enterprise** | **299 USD**/연 | 연간 | **직원 내부 배포**용. 일반 App Store 공개와 별도 프로그램. |
| **Google Play Console** | **25 USD** | **1회** | 카드 결제(선불카드 불가). 앱당 추가 등록비 없음. [공식](https://support.google.com/googleplay/android-developer/answer/6112435) |

**무료 앱만 배포**해도 위 계정비는 필요. 유료/IAP가 없으면 **매출 수수료는 0**.

조직(Organization) 등록 시 Apple은 법인·D-U-N-S 등 검증, Google은 Personal vs Organization 유형·신원 확인이 추가로 걸린다. 개인 계정(Google, 2023-11-13 이후 신규)은 **비공개 테스트 요건·기기 검증**을 통과해야 프로덕션 배포 가능.

## 2. 매출 수수료 (디지털 상품·구독·IAP)

무료 + 외부 결제만 쓰는 B2B/웹 구독 모델이면 스토어 커미션 회피 여지가 있으나, **인앱 디지털 재화·구독**은 각 스토어 정책·지역 규제를 따른다.

### Apple App Store

- 기본 디지털 상품/서비스: **30%**
- App Store Small Business Program 등 적격: **15%**
- 적격 구독: **15%** (프로그램·기간 조건 있음)
- 출처: [Membership / Pricing and fees](https://developer.apple.com/programs/whats-included/)

EU 등 일부 지역은 대체 배포·대체 결제·Core Technology Fee 등 **별도 요금제**가 있다. 해당 시장에 올릴 때만 Apple 지역 문서를 본다.

### Google Play (2026-06-30~ 요금 개편, 단계적 글로벌)

[공식 블로그](https://developer.android.com/blog/posts/expanded-billing-choice-and-lower-fees-on-google-play) 기준:

- **서비스 수수료**와 **빌링 수수료**를 분리.
- 최초 적용: **미국·EEA·영국** (2026-06-30). 이후 시장별 롤아웃(한국 등 일정은 Google 공지·헬프센터 확인).
- 연간 수익 **첫 100만 USD**: 서비스 수수료 **10%** (자동 갱신 구독에도 동일 적용이라고 명시).
- Google Play Billing 사용 시(초기 시장): 빌링 **+5%** → 실효 약 **15%**(첫 100만 + 구독 케이스).
- 대체 결제/웹 링크만 쓰면 빌링 수수료는 적용되지 않음(서비스 수수료는 유지). 100만 USD 초과·신규/기존 설치 구분 등 상세율은 Help Center rate card를 본다.

**레거시(개편 전·미적용 시장)** 에서는 흔히 “첫 100만 15% / 초과 30%” 프레임이 통용됐다. **한국 포함 미전환 시장은 전환일 전까지 기존 구조를 가정**하고, 전환 공지를 추적한다.

## 3. 배포 절차 (최소 경로)

### iOS (App Store)

1. Apple Developer Program 등록·결제·(조직이면) 법인 검증.
2. Certificates / Identifiers / Profiles, App ID, 서명.
3. Xcode(또는 CI)로 아카이브 → App Store Connect 업로드.
4. **TestFlight**: 내부 테스터(ASC 사용자) / 외부(최대 약 1만, 첫 빌드는 Beta App Review 가능).
5. 메타데이터·스크린샷·프라이버시·연령·수출(암호화) 설문 작성.
6. **App Review** 제출 → 승인 후 릴리스(수동/자동).
7. 유료/IAP면 Paid Apps Agreement·세금·은행 정보 완료.

병목: 조직 검증, 리뷰 거절(가이드라인·로그인 데모 계정·프라이버시 정책 URL).

### Android (Google Play)

1. Play Console 등록·**25 USD**·DDA 수락.
2. Personal/Organization 선택 → 신원·(Personal) 테스트·기기 검증.
3. 앱 생성 → 스토어 등록정보·콘텐츠 등급·대상 연령·데이터 안전 양식.
4. 내부/비공개/공개 테스트 트랙에 AAB 업로드 → 테스터.
5. 프로덕션 출시(단계적 출시 권장) → 정책 검토.
6. 유료/IAP면 판매자 계정·세금 설정.

병목: 신규 Personal 계정의 테스트 요건, Data safety·정책 위반으로 인한 보류.

## 4. CrewRP 관점 예산 스케치

| 항목 | 대략 | 비고 |
|------|------|------|
| 첫해 스토어 계정만 | **~124 USD** (Apple 99 + Google 25) | 원화·카드 수수료·VAT 별도 |
| 이후 연간 | **~99 USD** | Google은 등록비 재청구 없음(계정 유지 전제) |
| 무료 앱(IAP 없음) 운영 수수료 | **0** | |
| IAP/구독 시 | 스토어 실효 **~15–30%**대 | 지역·프로그램·Play 개편 적용 여부 |
| 인력/CI/맥 빌드·디자인·법적 문서 | **계정비보다 큼** | 프라이버시 정책, 지원 채널, 스크린샷 |

한국 보조 스토어(원스토어·Galaxy Store 등)는 **필수 아님**. 국내 도달을 넓힐 때만 별도 계정·수수료표를 조사하면 된다.

## 5. 결정 체크리스트

1. 계정: **개인 vs 법인(Organization)** — CrewRP가 B2B/팀 제품이면 법인 권장.
2. 수익화: **완전 무료 / 웹결제 / 스토어 IAP·구독** — 수수료·심사 부담이 갈림.
3. 타깃 국가: **한국만 vs 글로벌** — Play 요금 롤아웃·Apple 지역 정책이 다름.
4. 베타: TestFlight + Play 내부/비공개 테스트로 심사 전 검증.
5. 운영: 연간 Apple 갱신일, 정책·요금 `review_after` 재확인.

## 관련

- Expo/RN 빌드 맥락: [[wiki/Engineering/Development-Environment/Expo-및-React-Native-개발-생태계-2026.md]]
- Business MOC: [[wiki/Business/000_Business-MOC.md]]
