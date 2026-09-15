---
title: "NPU 최적화를 위한 지능형 양자화(Quantization) 기술"
related_raw: ["[[2026-05-12-ONNX_Runtime_Quantization_Guide.md]]", "[[2026-05-12-Rebellions_LLM_Serving_Whitepaper.md]]"]
tags: ["Models/Optimization", "Quantization", "NPU", "INT8", "FP8"]
date: "2026-05-12"
---

# NPU 및 AI 가속기를 위한 양자화 전략

## 1. 개요
양자화(Quantization)는 32비트 부동소수점(FP32) 가중치와 활성함수 값을 8비트(INT8, FP8) 또는 그 이하(INT4)의 낮은 정밀도로 변환하여 모델 크기를 줄이고 추론 속도를 높이는 핵심 최적화 기술입니다.

## 2. 주요 양자화 방식
1. **동적 양자화 (Dynamic Quantization)**:
    - 추론 시점에 활성함수의 스케일(Scale)과 제로 포인트(Zero-point)를 계산합니다.
    - 구현이 비교적 단순하며 RNN 및 트랜스포머 기반 모델에 효과적입니다.
2. **정적 양자화 (Static Quantization)**:
    - 사전에 캘리브레이션(Calibration) 데이터를 사용하여 양자화 파라미터를 고정합니다.
    - 추론 시 추가 연산 오버헤드가 적어 CNN 모델 및 엣지 디바이스에 권장됩니다.
3. **양자화 인식 학습 (QAT, Quantization-Aware Training)**:
    - 학습 단계에서 양자화로 인한 손실을 모델이 학습하도록 하여 정확도 저하를 최소화합니다.

## 3. 하드웨어 특화 및 고성능 양자화 기법
- **명시적 양자화 (Explicit Quantization)**: ONNX 그래프에 Q/DQ 레이어를 삽입하여 양자화 위치를 정밀하게 제어합니다. 이는 TensorRT 및 리벨리온 RBLN SDK에서 권장되는 방식으로, 하드웨어 최적화 과정에서 산술적 정확도를 유지하는 데 유리합니다.
- **블록 양자화 (Block Quantization)**: 텐서를 고정된 크기의 블록(예: 32, 64, 128)으로 나누고 각 블록마다 독립적인 스케일을 적용합니다.
    - **INT4 Weight-only**: 가중치만 4비트로 양자화하여 메모리 대역폭을 절약하고 연산은 고정밀도로 수행합니다.
    - **MX-Compliant (Microscaling)**: FP8/FP4를 위한 지수 전용 스케일링을 지원하는 최신 포맷입니다.
- **리벨리온 NPU 사례**:
    - **비대칭 양자화 (Asymmetric Quantization)**: 데이터 분포가 비대칭일 때 정밀도 손실을 최소화합니다.
    - **레이어별 지능형 정밀도 할당**: Attention은 FP16 유지, FFN은 INT8 변환 등으로 성능과 정확도의 최적점을 찾습니다.


## 4. 고수준 양자화 (INT4/UINT4)
- 최신 ONNX Runtime(opset 21 이상) 및 가속기들은 **INT4** 가중치 전용 양자화(Weight-only Quantization)를 지원합니다.
- 이는 모델의 메모리 점유율을 획기적으로 낮추어 초대형 모델을 단일 NPU/GPU 메모리에 올리는 데 필수적입니다.

---
**관련 문서**:
- [[wiki/Models/Optimization-and-Serving/Rebellions-NPU-LLM-Serving.md]]
- [[wiki/Models/Optimization-and-Serving/LLM Compressor - vllm 모델 최적화 라이브러리.md]]
