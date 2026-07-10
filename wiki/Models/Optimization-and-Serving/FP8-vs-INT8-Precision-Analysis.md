---
title: "FP8 vs INT8: 효율적 딥러닝 추론을 위한 정밀도 비교 분석"
related_raw: ["[[raw/2026-05-12-NVIDIA_TensorRT_Quantized_Types_Docs.md]]"]
tags: ["Models/Optimization", "Quantization", "FP8", "INT8", "Precision"]
date: "2026-05-12"
---

# FP8 vs INT8 정밀도 및 효율 분석

## 1. 개요
LLM 추론 가속을 위해 모델 가중치와 활성값을 8비트로 양자화하는 것이 표준이 되었습니다. 전통적인 **INT8**과 최신 가속기(H100, ATOM-Max 등)에서 지원하는 **FP8**의 특성을 비교합니다.

## 2. 주요 차이점

| 특성 | INT8 (Integer) | FP8 (Floating Point) |
| :--- | :--- | :--- |
| **형식** | 8-bit signed integer | E4M3 (데이터) / E5M2 (그래디언트) |
| **동적 범위** | 고정적 (Linear) | 유동적 (Exponent 기반) |
| **구현 난이도** | 높음 (정밀한 캘리브레이션 필요) | 낮음 (기존 FP 워크플로우와 유사) |
| **정확도** | Outlier에 취약함 | 넓은 동적 범위로 Outlier 보존 유리 |
| **하드웨어 지원** | 범용적 (대부분의 NPU/GPU) | 최신 아키텍처 (Ada, Hopper, ATOM-Max) |

## 3. FP8의 장점
- **Outlier 처리**: LLM의 활성값(Activation)에서 발생하는 큰 값(Outlier)은 모델 성능에 지대한 영향을 미칩니다. FP8은 지수(Exponent) 비트를 통해 넓은 범위를 커버하므로 INT8보다 정보 손실이 적습니다.
- **훈련-추론 일관성**: FP8은 훈련 과정에서도 사용될 수 있어(FP8 Training), 추론 시 별도의 복잡한 포스트 트레이닝 양자화(PTQ) 과정 없이도 높은 정확도를 유지하기 쉽습니다.

## 4. INT8의 장점
- **성능 밀도**: 동일 면적 대비 연산 처리량(TOPS)이 FP8보다 높은 경우가 많습니다 (예: 리벨리온 아톰 NPU는 INT8 연산 시 최대 성능 발휘).
- **에너지 효율**: 정수 연산은 부동소수점 연산보다 하드웨어 게이트 수준에서 전력 소모가 적습니다.

## 5. 결론 및 권장 사항
- **범용 서비스**: 하드웨어 가용성이 높고 전력 효율이 중요한 경우 **INT8 PTQ**를 권장합니다.
- **고정밀 추론**: 모델 성능 저하에 민감하고 최신 가속기를 사용하는 경우 **FP8** 사용이 유리합니다.
- **하이브리드 전략**: 리벨리온 SDK와 같이 레이어별로 오차 민감도를 분석하여 **Attention은 FP16, FFN은 INT8/FP8**로 혼합 적용하는 것이 가장 효율적입니다.

---
**관련 문서**:
- [[wiki/Models/Optimization-and-Serving/Quantization-Techniques-NPU.md]]
- [[wiki/Models/Optimization-and-Serving/Rebellions-NPU-LLM-Serving.md]]
