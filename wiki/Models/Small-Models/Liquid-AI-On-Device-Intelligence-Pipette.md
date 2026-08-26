---
title: Liquid AI의 온디바이스 LFM 모델과 Pipette 벤치마크
related_raw: ["[[2026-08-26-liquid_ai_on_device_intelligence_pipette.md]]"]
tags: [on_device_ai, small_models, benchmark, liquid_ai]
last_updated: "2026-08-26"
updated: "2026-08-26"
---

# 📱 Liquid AI의 온디바이스 LFM 모델과 Pipette 벤치마크

## 1. 온디바이스 AI의 필요성과 핵심 강점
온디바이스(On-device) 또는 엣지(Edge) 서빙은 자원을 클라우드로 전송하지 않고 로컬 칩셋에서 구동하는 패러다임입니다.
- **강력한 개인정보 보호**: 민감한 사용자 데이터나 기밀이 기기 내부에서 격리되어 외부로 유출되지 않음.
- **실시간 저지연성 (Real-time Low Latency)**: 네트워크 왕복이 없어 딜레이 최소화.
- **인프라 비용 Zero**: 한 번 장치에 설치/배포하면 무제한 인퍼런스에도 추가적인 클라우드 서버 사용량 비용이 청구되지 않음.
- **전력 효율성**: 배터리 기반 디바이스 내 저전력 가속 기능 결합 가능.

## 2. Pipette 오픈소스 온디바이스 벤치마크
- **개념**: 모바일 스마트폰, AI PC, 에지 디바이스 등 다양한 물리 디바이스 제약 환경에서 구동하는 인공지능 모델의 성능을 표준 측정하는 독립 벤치마크 프레임워크.
- **주요 계측 타깃**: 추론 속도(Tokens Per Second), 메모리 상주 용량(VRAM/DRAM footprint), 최초 토큰 반응 시간(TTFT), 그리고 지능 품질 성능을 크로스 매칭 평가.
- **LFM 2.5-2.6B 검증**: Liquid AI의 초경량 액체 신경망(Liquid Foundation Models) 아키텍처 모델이 본 벤치마크 및 Artificial Analysis 독립 테스트 결과 모바일 최적 자원 제한 부문에서 높은 전력당 효율과 지능 밀도 1위를 달성함.
