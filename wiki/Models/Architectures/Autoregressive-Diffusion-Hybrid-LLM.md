---
title: "Autoregressive-Diffusion 하이브리드 언어 모델 아키텍처"
date: "2026-07-31"
last_updated: "2026-07-31"
updated: "2026-07-31"
related_raw: ["[[2026-07-31-kiwoong-yeom-autoregressive-diffusion-hybrid-llm.md]]"]
tags: ["Models", "Architectures", "Diffusion-LLM", "Autoregressive-LLM", "ICLR-2025"]
type: "wiki"
---

# Autoregressive-Diffusion 하이브리드 언어 모델 아키텍처

기존의 **Autoregressive (AR)** 디코딩 모델은 텍스트를 한 토큰씩 순차 생성하여 추론 속도가 느리다는 단점이 있으며, **Diffusion** 기반 언어 모델(dLLM)은 병렬 생성이 가능하지만 긴 컨텍스트에서의 정보 소실 및 일관성(Coherence) 유지가 어렵다는 한계가 있었습니다. 

ICLR 2025 등 최신 인공지능 학회에서는 이 두 패러다임의 장점을 결합하여 고품질의 텍스트 생성과 추론 성능의 극대화를 달성하려는 하이브리드 아키텍처 연구가 핵심 주제로 부상했습니다.

## 1. 주요 연구 동향 및 아키텍처 기법

### 1) FLARE (Diffusion for Hybrid Language Model)
- **제안 기관**: Adobe Research 및 조지아 공과대학교 (Georgia Tech)
- **핵심 메커니즘**: 하이브리드 어텐션 구조를 지닌 AR 모델을 단 한 번의 저비용 Continual Training을 통해 dLLM으로 결합/변환하는 프레임워크입니다.
- **작동 모드 (Dual Decoding)**: 
  - **Clean Stream**: Causality(인과적 연결)에 기반한 표준 causal 디코딩을 수행하여 논리적 일관성과 정보 정확도를 방어합니다.
  - **Noise Stream (Block-Diffusion)**: 여러 개의 '드래프트(Draft)' 토큰 블록을 병렬로 생성(denoising)하고, 이를 clean stream이 즉시 검증하는 방식(Speculative-style)으로 구동됩니다.
- **효과**: 기존 AR 모델의 추론 지연을 최대 4.8배 가속하면서 인지 성능 및 품질 저하를 예방합니다.

### 2) Block Diffusion
- **메커니즘**: 문장을 고정된 단일 토큰 단위가 아니라 여러 개의 토큰 블록(Block) 단위로 끊어 확산 기반 병렬 디코딩을 수행합니다.
- **의의**: KV Cache 메커니즘을 블록 단위로 재설계하여 병렬 토큰 샘플링을 효율적으로 실현합니다.

### 3) dLLM Adaptation (Adaptation from AR Models)
- **개념**: GPT나 LLaMA 같은 대형 오픈소스 AR 체크포인트를 활용해, 베이스 지식을 그대로 보존한 채 diffusion 노이징 헤드와 Denoising Objective를 도입해 가중치를 적응(Adaptation)시키는 기법입니다. (예: LLaDA 등)
- **장점**: 처음부터 dLLM을 새로 사전 학습하는 거대한 컴퓨팅 비용(Scratch Training)을 회피합니다.

## 2. RAG 및 실시간 온디바이스 서빙에 미치는 영향

- **가속 및 효율**: 온디바이스(모바일, AI PC) 환경에서는 GPU 대역폭과 연산 한계로 순차적 AR 생성이 사용자 경험을 저해합니다. 하이브리드 Diffusion 디코딩은 병렬 연산을 가동하여 실시간 생성 속도를 개선합니다.
- **구조적 다양성**: 비전 언어 처리(VLM OCR 등) 분야에서도 병렬 텍스트 해독 기법을 통해 이미지 레이아웃을 순식간에 복합 텍스트로 정규화하는 데 기여합니다.

## 🔗 연결된 문서
- [[wiki/Models/Architectures/000_Architectures-MOC.md]]
- [[wiki/Models/Architectures/Diffusion-Language-Models-dLLM.md]]
- [[wiki/Models/Optimization-and-Serving/스마트폰-환경의-LLM-서빙-기술-2026.md]]
