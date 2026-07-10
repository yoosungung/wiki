---
title: "연속 배칭(Continuous Batching) 및 동적 스케줄링"
related_raw: ["[[2026-05-12-HuggingFace_Continuous_Batching_Guide.md]]"]
tags: ["Models/Optimization", "LLM-Serving", "Continuous-Batching", "Throughput"]
date: "2026-05-12"
---

# 연속 배칭(Continuous Batching) 기술 분석

## 1. 개요
전통적인 정적 배칭(Static Batching)은 모든 요청이 완료될 때까지 다음 배치를 처리하지 못해 하드웨어 자원이 유휴 상태가 되는 비효율이 발생합니다. 연속 배칭(Continuous Batching)은 요청이 완료되는 즉시 새로운 요청을 배치에 투입하여 처리량(Throughput)을 극대화하는 기술입니다.

## 2. 핵심 메커니즘
1. **래그드 배칭(Ragged Batching)**:
    - 서로 다른 길이의 시퀀스를 패딩(Padding) 없이 하나로 연결합니다.
    - 어텐션 마스크를 사용하여 각 시퀀스가 서로 간섭하지 않도록 제어합니다.
2. **동적 스케줄링(Dynamic Scheduling)**:
    - 토큰 단위로 스케줄링을 수행합니다.
    - **Prefill**(첫 토큰 생성 전 연산) 단계와 **Decode**(이후 토큰 생성) 단계를 동일한 포워드 패스에서 혼합하여 실행할 수 있습니다.
3. **청크 프리필(Chunked Prefill)**:
    - 긴 프롬프트를 작은 청크로 나누어 처리함으로써, 대규모 프리필 작업이 다른 요청의 디코딩 작업을 오랫동안 차단하는 현상을 방지합니다.

## 3. 주요 이점
- **처리량 향상**: GPU/NPU의 모든 연산 슬롯을 유효한 토큰 생성에 활용하여 단위 시간당 처리 토큰 수를 크게 늘립니다.
- **응답 지연 시간 감소**: 새로운 요청이 이전 배치가 끝날 때까지 기다리지 않고 즉시 처리되기 시작합니다.
- **메모리 효율성**: 불필요한 패딩 토큰을 저장하고 연산할 필요가 없어 메모리 대역폭과 용량을 절약합니다.

## 4. 서빙 시스템 적용
- **vLLM**: PagedAttention과 결합하여 연속 배칭을 대중화한 대표적인 프레임워크입니다.
- **vLLM-RBLN**: 리벨리온 NPU 아키텍처에서 연속 배칭을 네이티브하게 지원하여, 엑사온(EXAONE)과 같은 대규모 모델 서빙 시 높은 가동률을 보장합니다.

---
**관련 문서**:
- [[wiki/Models/Optimization-and-Serving/Rebellions-NPU-LLM-Serving.md]]
- [[wiki/Models/Optimization-and-Serving/Quantization-Techniques-NPU.md]]
