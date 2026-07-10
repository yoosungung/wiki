---
related_raw: ["[[raw/Recent Developments in LLM Architectures KV Sharing, mHC, and Compressed Attention.md]]"]
tags: ["#LLM", "#Architecture", "#Gemma4", "#DeepSeekV4", "#ZAYA1"]
date: "2026-05-31"
---

# 최신 LLM 아키텍처 트렌드 (2026): 효율성과 긴 컨텍스트

## 1. 개요
2026년의 LLM 아키텍처는 모델의 크기를 무작정 키우기보다, 추론 효율성을 높이고 특히 긴 컨텍스트(Long-context) 처리 비용을 절감하는 방향으로 진화하고 있음.

## 2. 주요 모델별 아키텍처 혁신

### A. Gemma 4 (Google)
- **KV Sharing (Cross-Layer Attention)**: 후속 레이어가 이전 레이어의 KV 상태를 재사용하여 캐시 크기를 약 50% 절감함.
- **Per-Layer Embeddings (PLE)**: 레이어별 전용 임베딩 슬라이스를 추가하여 트랜스포머 스택 전체를 확장하지 않고도 모델 용량(Capacity)을 효과적으로 증대함.

### B. DeepSeek V4 (DeepSeek)
- **mHC (Manifold-Constrained Hyper-Connections)**: 잔차 연결(Residual connections)을 병렬 스트림으로 확장하고 기하학적 제약(stochastic matrices)을 두어 정보 전달의 안정성과 표현력을 높임.
- **CSA/HCA (Compressed Attention)**:
    - **CSA (Compressed Sparse Attention)**: 시퀀스 차원에서 KV 엔트리를 압축하고 희소 선택(Sparse selection) 기법 적용.
    - **HCA (Heavily Compressed Attention)**: 매우 높은 압축률(예: 128:1)을 적용하고 전체 압축 캐시에 대해 밀집(Dense) 어텐션 수행.
- 결과적으로 DeepSeek V3.2 대비 1M 컨텍스트에서 KV 캐시 사용량을 90% 이상 절감함.

### C. ZAYA1-8B (Zyphra)
- **CCA (Compressed Convolutional Attention)**: 어텐션 연산 자체를 압축된 잠재 공간(Latent space)에서 직접 수행하며, 압축으로 인한 정보 손실을 보완하기 위해 Q, K에 합성곱(Convolution) 믹싱을 적용함.

### D. Laguna XS.2 (Poolside)
- **Layer-wise Attention Budgeting**: 레이어별로 어텐션 헤드 수를 다르게 설정하여 중요한 레이어에 연산 자원을 집중하고, 슬라이딩 윈도우 레이어와 글로벌 어텐션 레이어를 혼합함.

## 3. 결론 및 전망
- **트랜스포머의 진화**: 기본 구조는 유지하되 내부 모듈(Attention, Residual, Embedding)이 고도로 정밀하게 튜닝되고 있음.
- **추론 최적화**: 긴 컨텍스트 처리 비용이 아키텍처 설계의 최우선 고려 사항이 됨.
- **복잡도 증가**: 성능 향상을 위해 수백 줄의 코드가 필요할 만큼 아키텍처의 복잡도가 심화되고 있으나, 이는 실제 운영 비용 절감으로 이어지고 있음.
