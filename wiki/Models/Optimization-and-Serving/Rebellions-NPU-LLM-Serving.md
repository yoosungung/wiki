---
title: "리벨리온 NPU 기반 고성능 LLM 서빙 최적화 (vLLM-RBLN)"
related_raw: ["[[2026-05-12-Rebellions_LLM_Serving_Whitepaper.md]]"]
tags: ["Models/Optimization", "NPU", "Rebellions", "vLLM", "Serving"]
date: "2026-05-12"
---

# 리벨리온 NPU 기반 LLM 서빙 최적화 기술

## 1. 개요
리벨리온(Rebellions)은 자사의 NPU(신경망 처리 장치) 아키텍처에 최적화된 LLM 서빙 시스템을 구축하였습니다. 이는 단순히 모델을 실행하는 수준을 넘어, 하드웨어 특성을 고려하여 핵심 어텐션 메커니즘을 재설계한 것이 특징입니다.

## 2. 핵심 최적화 기술
1. **[[wiki/Models/Optimization-and-Serving/FlashAttention.md|FlashAttention]]**:
    - NPU의 온칩(On-chip) SRAM 크기에 맞춘 타일(Tile) 기반 커널 구현.
    - DRAM 접근을 최소화하고 공유 메모리 내에서 연산을 수행하여 효율 극대화.
2. **[[wiki/Models/Optimization-and-Serving/PagedAttention.md|PagedAttention]]**:
    - KV 캐시를 논리적 블록으로 관리하여 메모리 파편화 해결.
    - vLLM의 블록 테이블 구조와 호환되며, 동적 DMA를 통해 런타임 주소 확인 지원.
3. **[[wiki/Models/Optimization-and-Serving/Sliding-Window-Attention.md|Sliding Window Attention (SWA)]]**:
    - 고정된 윈도우 크기 내에서만 어텐션을 수행하여 긴 문맥 처리 시 메모리 압박 감소.
    - 인플레이스(In-place) 회전 방식을 통해 메모리 재할당 없이 데이터 갱신.

## 3. 서빙 프레임워크: vLLM-RBLN
- **vLLM 플러그인**: 기존 vLLM 기반 워크플로우를 코드 수정 없이 리벨리온 NPU에서 실행 가능하게 함.
- **통합 런타임**: FlashAttention과 PagedAttention을 통합된 연산 그래프 및 메모리 모델 내에서 실행.
- **향후 계획**: `torch.compile()`과의 네이티브 통합을 통해 별도의 컴파일 단계 없는 심리스한 사용자 경험 제공 예정.

## 4. 분산 시스템: RSD (Rebellions Scalable Design)
- 단일 기기를 넘어 랙 및 데이터 센터 규모로 확장 가능.
- **Disaggregated Prefill**: 컨텍스트 생성(Prefill)과 토큰 생성(Decode) 단계를 분리하여 노드 간 자원 최적화.
- **MoE (Mixture of Experts) 지원**: 전문가 연산을 여러 장치에 분산하여 효율적으로 처리.

## 5. 하드웨어 스펙 (ATOM™)
- **성능**: 128 TOPS (INT8), 32 TFLOPS (FP16).
- **메모리**: 64MB 온칩 SRAM 탑재로 대규모 텐서 연산 가속.
- **공정**: 삼성 5nm 공정 기반.

---
**관련 문서**:
- [[wiki/Engineering/Infrastructure-and-DevOps/Rebellions-Software-Stack.md]]
- [[wiki/Models/Optimization-and-Serving/LLM Compressor - vllm 모델 최적화 라이브러리.md]]
