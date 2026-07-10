---
title: "투사적 MoE (Speculative MoE): 분산 추론 통신 최적화"
related_raw: ["[[2026-05-12-Speculative_MoE_Communication_Efficient_Inference.md]]"]
tags: ["Models/Optimization", "MoE", "Speculative-Inference", "Distributed-Inference"]
date: "2026-05-12"
---

# 투사적 MoE (Speculative MoE): 통신 효율적 병렬 추론

## 1. 개요
MoE(Mixture of Experts) 모델의 분산 추론 시, 전문가 병렬성(Expert Parallelism, EP)으로 인한 All-to-all 통신 오버헤드는 전체 성능의 병목 현상을 초래합니다. 투사적 MoE(Speculative MoE, s-MoE)는 토큰의 전문가 라우팅 경로를 사전에 예측하여 토큰과 전문가를 장치 간에 선제적으로 배치함으로써 통신량을 무손실로 절감하는 기술입니다.

## 2. 핵심 메커니즘
1. **투사적 토큰 셔플링 (s-TS, Speculative Token Shuffling)**:
    - **온라인 적용**: 텐서 병렬성(TP)의 Allreduce 단계에서 토큰의 활성값을 예측된 전문가가 있는 장치로 미리 셔플링(Reduce-scatter와 통합)하여 전송합니다.
    - 이를 통해 EP 단계에서의 명시적인 All-to-all 전송량을 크게 줄일 수 있습니다.
2. **투사적 전문가 사전 그룹화 (s-EG, Speculative Expert Pre-grouping)**:
    - **오프라인 적용**: 의미적으로 유사하거나 동시에 활성화될 확률이 높은 전문가들을 동일한 장치에 클러스터링합니다.
    - 전문가들이 여러 장치에 흩어져 있어 발생하는 분산 활성화를 방지하고 로컬 활성화 비율을 높입니다.

## 3. 예측 모델링: 토큰-전문가 친화도
- **내부 계층 친화도**: 의미적으로 유사한 토큰들은 특정 전문가 그룹을 선호하는 경향(High Kurtosis)이 있습니다.
- **계층 간 친화도**: 이전 계층에서 선택된 전문가와 다음 계층에서 선택될 전문가 사이에 강한 상관관계가 존재합니다.
- s-MoE는 이러한 친화도를 기반으로 확률 모델을 구축하여 약 89%의 높은 정확도로 라우팅 경로를 예측합니다.

## 4. 성능 개선 효과
- **처리량(Throughput)**: DeepSpeed-MoE 대비 1.7배 ~ 2.4배 향상.
- **로컬 활성화율(LAR)**: 43~61% 증가하여 전문가 계층의 지연 시간을 최대 68%까지 단축.
- **범용성**: DeepSpeed-MoE뿐만 아니라 SGLang과 같은 최신 엔진에서도 약 1.9배의 처리량 향상을 입증함.

## 5. 시사점
s-MoE는 모델의 가중치나 정확도를 변경하지 않고도 하드웨어 간 통신 병목을 알고리즘적으로 해결할 수 있음을 보여줍니다. 특히 고속 인터커넥트(NVLink 등)가 부족한 보급형 GPU/NPU 서버 환경에서 그 효과가 더욱 극명하게 나타납니다.

---
**관련 문서**:
- [[wiki/Models/Optimization-and-Serving/Rebellions-NPU-LLM-Serving.md]]
- [[wiki/Models/Optimization-and-Serving/Continuous-Batching.md]]
