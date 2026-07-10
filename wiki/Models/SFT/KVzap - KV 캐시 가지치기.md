---
title: "KVzap - KV 캐시 가지치기"
related_raw: ["[[wiki/Models/SFT/KVzap - KV 캐시 가지치기.md]]"]
tags: ['wiki', 'ai_core', 'fine-tuning_&_reasoning_models', 'fine-tuning_concepts']
type: "wiki"
status: "published"
last_updated: "2026-04-19"
---

# KVzap - 트랜스포머 언어 모델의 KV 캐시 가지치기

**요약:**
KVzap은 트랜스포머 기반 언어 모델의 KV(Key-Value) 캐시 병목 현상을 해결하기 위한 빠르고 적응적인 새로운 가지치기(pruning) 방법입니다. 이 기술은 기존 KVzip의 근사치로, 사전 채우기(prefilling) 및 디코딩(decoding) 작업 모두에서 작동합니다. KVzap은 Qwen3-8B, Llama-3.1-8B-Instruct, Qwen3-32B 모델에서 긴 컨텍스트 및 추론 작업 전반에 걸쳐 무시할 수 있는 정확도 손실로 2~4배의 KV 캐시 압축을 달성하며, KVpress 리더보드에서 최첨단 성능을 보여줍니다. 이는 경량의 대체 모델을 사용하여 중요도 점수를 예측하고, 임계값 기반 가지치기를 통해 입력에 따라 압축률을 동적으로 조정합니다.

**관련 URL:**
*   NVIDIA/kvpress (코드 및 모델)
*   NVIDIA/KVzap (모델 컬렉션)
*   Nemotron-Pretraining-Dataset-sample (학습 데이터셋)
*   KVzap predictions (평가 로그)

**설명 이미지:**
*   Figure 1: Qwen3-8B(왼쪽) 및 Llama-3.1-8B-Instruct(오른쪽)에 대한 KVpress 리더보드에서 다양한 KV 캐시 가지치기 방법을 비교.
*   Figure 2: Qwen3-8B(왼쪽), Llama-3.1-8B-Instruct(중앙), Qwen3-32B(오른쪽)에 대한 RULER 4k 결과.
*   Figure 3: Qwen3-8B(왼쪽), Llama-3.1-8B-Instruct(중앙), Qwen3-32B(오른쪽)에 대한 LongBench 결과.
*   Figure 4: AIME25 추론 성능. Qwen3-8B(왼쪽) 및 Qwen3-32B(오른쪽)에 대한 pass@1(실선) 및 pass@4(점선) 정확도 비교.
*   Figure 5: RULER 4k, LongBench, AIME25에서 Qwen3-8B 및 KVzap-MLP에 대한 압축률 분포(왼쪽) 및 대체 가지치기 방법과의 비교(오른쪽).
*   Figure 6: Qwen3-8B에 대한 상세 KVzap 평가 분석.
*   Figure 7: Llama-3.1-8B-Instruct에 대한 상세 KVzap 평가 분석.
*   Figure 8: Qwen3-32B에 대한 상세 KVzap 평가 분석.
*   Figure 9: 13개 하위 집합 각각에 대한 Qwen3-8B의 RULER 4k 결과.
*   Figure 10: 13개 하위 집합 각각에 대한 Llama-3.1-8B-Instruct의 RULER 4k 결과.
*   Figure 11: 13개 하위 집합 각각에 대한 Qwen3-32B의 RULER 4k 결과.
*   Figure 12: 21개 하위 집합 각각에 대한 Qwen3-8B의 LongBench 결과.
*   Figure 13: 21개 하위 집합 각각에 대한 Llama-3.1-8B-Instruct의 LongBench 결과.
*   Figure 14: 21개 하위 집합 각각에 대한 Qwen3-32B의 LongBench 결과.

**관련 노트:**
*   [[wiki/Models/Architectures/LLM 아키텍처 비교]]
*   [[wiki/Models/Architectures/MoE 모델 분석]]
*   [[wiki/Models/Architectures/Transformer 모델의 구조와 작동 원리 - Part 2 - 아키텍처와 구현]]
*   RoPE (Rotary Position Embedding) Scaling
*   [[wiki/Models/SFT/LLM_FineTuning_Libraries]]
*   [[wiki/Models/Reasoning-and-Cognition/LLM 학습 패러다임]]
*   대규모 언어 모델(LLM)의 추론 성능과 효율성을 동시에 향상시키는 방법
*   [[wiki/Models/Optimization-and-Serving/LLM Compressor - vllm 모델 최적화 라이브러리]]
*   [[wiki/Models/Small-Models/NVIDIA Nemotron 3]]