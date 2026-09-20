---
title: "LLM 아키텍처 비교"
related_raw: ["[[wiki/Models/Architectures/LLM 아키텍처 비교.md]]"]
tags: ['wiki', 'ai_core', 'llm_concepts', 'llm_architecture_and_technical']
type: "wiki"
status: "published"
last_updated: "2026-09-20"
updated: "2026-09-20"
---

# LLM 아키텍처 비교

다양한 LLM 아키텍처를 비교 분석한 아티클 요약입니다.

### 주요 아키텍처 특징

*   **Multi-Head Latent Attention (MLA)**
*   **Mixture-of-Experts (MoE)**
*   **정규화 계층 배치 (Pre-Norm, Post-Norm, QK-Norm)**
*   **슬라이딩 윈도우 어텐션**
*   **No Positional Embeddings (NoPE)**
*   **선형 어텐션 변형 (Gated DeltaNet, Kimi Delta Attention)**
*   **차세대 개념 예측 (Next Concept Prediction, NCP)**: 토큰 단위 생성을 넘어 이산 잠재 공간에서 개념을 우선 예측하여 훈련 토큰 절반(51.3%)으로 기준 수렴을 달성하는 잠재 공간 언어 모델 아키텍처.

### 트렌드

*   MoE 아키텍처의 인기 증가
*   모델 깊이 및 너비 간의 절충점
*   일부 모델의 효율성 개선 및 투명성
*   토큰 수준(NTP)에서 개념 수준(NCP) 잠재 공간 모델링으로의 패러다임 확장

### 관련 노트

*   [[wiki/Models/Architectures/NCP-ArchPreview-Next-Concept-Prediction.md|NCP-ArchPreview 차세대 개념 예측 아키텍처]]
*   [[wiki/Models/Architectures/000_Architectures-MOC.md|Architectures MOC]]
*   Mixture-of-Experts
*   Multi-Head Latent Attention
*   슬라이딩 윈도우 어텐션
*   정규화 계층
*   선형 어텐션
*   NoPE
*   트랜스포머
*   Mamba

### 원문

*   [The Big LLM Architecture Comparison](https://magazine.sebastianraschka.com/p/the-big-llm-architecture-comparison?open=false#%C2%A7xiaomi-mimo-v-flash)
