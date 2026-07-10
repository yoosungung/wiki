---
title: "FlashAttention: 메모리 병목 해소를 위한 어텐션 최적화"
related_raw: ["[[projects/Rebellions-EXAONE/Rebellions_Whitepaper.pdf]]"]
tags: ["Models/Optimization", "FlashAttention", "Memory", "HBM", "SRAM", "Rebellions"]
date: "2026-05-12"
---

# FlashAttention

FlashAttention은 대규모 언어 모델(LLM)의 핵심인 트랜스포머(Transformer) 아키텍처에서 발생하는 **메모리 병목 현상(Memory Bound)**을 해결하기 위해 고안된 혁신적인 알고리즘입니다.

## 1. 등장 배경 (기존 어텐션의 문제점)

트랜스포머의 Standard Attention 메커니즘은 입력 시퀀스 길이가 길어질수록 연산량과 메모리 사용량이 기하급수적으로($O(N^2)$) 증가하는 한계가 있습니다.

- **메모리 대역폭(Memory Bandwidth)의 한계**: GPU/NPU의 연산 속도 발전 속도에 비해 메모리(HBM/DRAM)에서 데이터를 가져오는 속도는 상대적으로 느립니다.
- **불필요한 데이터 이동**: 기존 어텐션은 중간 계산 결과(Attention Matrix)를 느린 HBM에 썼다가 다음 계산을 위해 다시 읽어오는 과정을 반복합니다. 시퀀스가 길어지면 실제 연산 시간보다 데이터를 읽고 쓰는 시간이 훨씬 오래 걸리게 됩니다.

## 2. 해결 방법 (핵심 원리)

FlashAttention의 핵심 아이디어는 **"느린 메모리(HBM) 접근을 최소화하고, 빠르지만 용량이 작은 메모리(SRAM) 내에서 최대한 계산을 완료하는 것"**입니다. 이를 위해 두 가지 주요 기법을 사용합니다.

### 2.1 타일링 (Tiling)
거대한 행렬을 한 번에 HBM에 올리지 않고, 행렬을 SRAM에 들어갈 수 있는 크기의 작은 블록(Tile)으로 쪼개어 계산합니다.
작은 블록들을 빠른 SRAM으로 가져와 어텐션 연산(Q, K, V 곱셈 등)을 수행한 뒤, 최종 결과만 다시 HBM에 저장합니다. 이를 통해 메모리 I/O 트래픽을 기하급수적으로 줄일 수 있습니다.

### 2.2 재계산 (Recomputation, 학습 시)
메모리 절약을 위해 역전파(Backpropagation) 시 필요한 순전파(Forward)의 중간 결과물을 HBM에 저장해두지 않습니다. 대신, 역전파 단계에서 입력 데이터를 사용해 그 순간에 필요한 중간 결과를 **다시 계산(Recompute)**합니다.
느린 메모리에서 거대한 데이터를 읽어오는 시간보다, 빠른 연산 장치로 데이터를 다시 계산하는 시간이 훨씬 짧기 때문에 전체적인 속도 향상이 일어납니다.

## 3. FlashAttention의 효과

- **속도 향상**: 기존 어텐션 대비 훨씬 빠른 속도(2~4배 이상)를 제공합니다.
- **메모리 절약**: 메모리 사용량이 시퀀스 길이의 제곱($O(N^2)$)에서 선형($O(N)$)으로 감소합니다.
- **Long Context 지원**: 획기적인 메모리 절약을 통해 수만~수십만 토큰에 달하는 긴 문서를 한 번에 처리할 수 있는 기반이 되었습니다.

## 4. 응용 사례: 리벨리온(Rebellions) NPU 최적화

하드웨어 가속기 제조사들도 FlashAttention의 개념을 자사 아키텍처에 맞게 재해석하고 있습니다.
리벨리온의 LLM 서빙 백서(Whitepaper)에 따르면, 이들은 FlashAttention을 NPU의 로컬 SRAM 크기에 맞춰 **타일 기반 커널(Tile-based kernel)**로 구현했습니다.
Blockwise softmax와 행렬 곱셈을 완전히 공유 메모리 내에서 수행하도록 하여 DRAM 접근을 극적으로 줄이고 연산 효율성을 높였습니다.

---
**관련 문서**:
- [[wiki/Models/Optimization-and-Serving/Rebellions-NPU-LLM-Serving.md]]
- [[wiki/Models/Optimization-and-Serving/vLLM_Serving_Techniques.md]]
