---
title: "Siri AI 및 Apple Intelligence 에이전트 프레임워크 (2026)"
tags: ["SiriAI", "AppleIntelligence", "Agents", "AppIntents", "AFM3", "WWDC26"]
last_updated: "2026-06-12"
updated: "2026-06-12"
related_raw: ["[[2026-06-11-WWDC26-Core-AI-Siri-AI-Research.md]]", "[[2026-06-12-Autonomous-Agents-OpenClaw-HyperAgent-Update.md]]"]
---

# 🍎 Siri AI 및 Apple Intelligence 에이전트 프레임워크 (2026)

2026년 6월 WWDC에서 발표된 **Siri AI**는 단순한 음성 비서를 넘어, 시스템 전반의 컨텍스트를 이해하고 실행하는 **자율 에이전트(Autonomous Agent)**로 재탄생했습니다.

## 1. Siri AI 아키텍처: 3계층 추론 시스템
- **온디바이스 (AFM 3 Core)**: 3B 파라미터 규모 모델. 일상적 작업, 프라이버시 민감 데이터, 오프라인 액션 처리.
- **Private Cloud Compute (AFM 3 Advanced)**: 20B 파라미터 Sparse MoE 모델. Apple Silicon 서버에서 데이터 보관 없이 복잡한 추론 수행.
- **Global Cloud (Third-Party)**: 광범위한 외부 지식이 필요한 경우 **Google Gemini** (1.2T 규모) 또는 Claude 모델로 자동 라우팅.

## 2. 개발자 SDK 및 핵심 API

### 1) App Intents 2.0 & Assistant Schemas
- **SiriKit 공식 폐기**: iOS 27부터 SiriKit이 Deprecated 되었으며 **App Intents 2.0**이 표준으로 확정되었습니다.
- **Assistant Schemas**: 앱의 기능을 Siri가 사전 정의된 구조(Mail, Photos 등)로 인식하게 하여 커스텀 대화 코드 작성을 최소화합니다.
- **App Entities**: 앱 내 데이터를 시스템 와이드 **Spotlight Semantic Index**에 등록하여 복합 쿼리("엄마가 보낸 메일의 호텔 예약 보여줘")를 가능하게 합니다.

### 2) View Annotations API (On-screen Awareness)
- **개요**: 에이전트가 현재 화면의 UI 요소를 인식하고 상호작용할 수 있게 하는 API입니다.
- **작동 방식**: 화면 인식을 통한 맥락적 명령(예: "이거 요약해줘", "저거 전송해줘")을 지원하며, UI 요소의 시맨틱 정보를 참조합니다.

### 3) Language Model Protocol
- **모델 교체 가용성**: 개발자가 앱 내에서 Apple의 AFM 모델뿐만 아니라 서드파티 LLM을 표준화된 방식으로 호출하고 교체할 수 있게 합니다.

## 3. 주요 기능 (2026.06 업데이트)
- **Standalone Siri App**: 챗봇 형태의 전용 앱을 통해 iCloud로 동기화되는 멀티턴 대화 기록을 관리합니다.
- **Personal Context Index**: 사용자의 메시지, 이메일, 일정 간의 관계를 시맨틱 그래프로 인덱싱하여 "엄마가 언급한 호텔의 예약 확인해줘"와 같은 복합 쿼리에 대응합니다.
- **Visual Intelligence**: 카메라 앱 내 Siri 모드를 통해 실시간 사물 식별, 문서 분석 및 실행(예: 메뉴판 촬영 후 더치페이 계산)이 가능합니다.

## 4. 제약 사항
- **Hardware**: 온디바이스 에이전트 기능을 위해 최소 **12GB RAM** (iPhone 17 Pro 이상)이 필수적입니다.
- **Regulatory**: 유럽 연합(DMA 관련) 및 중국 시장에서는 출시 초기 기능이 제한될 수 있습니다.

---
**관련 문서**:
- [[wiki/Models/Optimization-and-Serving/스마트폰-환경의-LLM-서빙-기술-2026]]
- [[wiki/Agents/Frameworks/차세대-자율-수행-에이전트-분석-2026]]
