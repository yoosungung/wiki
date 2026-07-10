---
related_raw: ["[[2026-06-25-TimesFM_2.5_Decoder_Time_Series_Foundation_Model.md]]"]
tags: ["#wiki", "Time-Series", "TimesFM", "Foundation-Model", "Small-Models"]
---

# TimesFM 2.5: Google 경량 시계열 파운데이션 모델

구글이 개발 및 오픈소스 배포한 **TimesFM 2.5**는 파라미터 크기 200M 규모의 극도로 가볍고 콤팩트한 디코더 기반 시계열(Time Series) 데이터 분석 및 패턴 예측용 파운데이션 모델입니다.

## 1. 아키텍처적 핵심 메커니즘
- **경량 데코더 구조**: 200M 파라미터로 설계되어 단일 상용 GPU나 심지어 고성능 에지 장비에서도 고속 학습(Fine-tuning) 및 추론이 가능합니다.
- **Factorization 분해 모델링**: 입력된 시계열 데이터의 장단기 전이를 트렌드(Trend), 계절성(Seasonality), 돌발 노이즈 등으로 정교하게 분리 분해하여 효율적으로 모델링합니다.
- **불규칙 샘플링 대응**: 데이터 수집 환경이 불안정하여 수집 간격이 산발적이고 불규칙한 실세계 데이터에 대해서도 데이터 손상 없이 강건하게 작동합니다.

## 2. 주요 실무 활용처
- **전력/에너지 소모 예측**: 시간별, 기상 조건별 에너지 사용 패턴 인지 및 그리드 효율화.
- **매출 및 재고 수요 분석**: 유통 현장에서의 물류 선행 주문 최적화.
- **금융 시계열 분석**: 장기 거시 경제 흐름 및 자산 변동 패턴 감지.
- **이상치 탐지(Anomaly Detection)**: 기상 센서 및 공장 설비 이상 진동 모니터링.

## 🔗 연결된 문서
- [[wiki/Models/Small-Models/000_Small-Models-MOC.md]]
- [[index.md]]
