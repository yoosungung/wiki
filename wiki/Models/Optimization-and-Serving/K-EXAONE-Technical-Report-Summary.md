---
title: "K-EXAONE Technical Report 핵심 요약 및 벤치마크"
related_raw: ["[[raw/2026-05-12-LG_K_EXAONE_HF_Model_Card.md]]"]
tags: ["Models/Architectures", "EXAONE", "LG-AI", "Benchmark", "K-EXAONE"]
date: "2026-05-12"
---

# K-EXAONE Technical Report 분석

## 1. 아키텍처 및 학습 제원 (7.8B 기준)
- **구조**: Decoder-only Transformer.
- **주요 기법**: RoPE (Rotary Position Embeddings), GQA (Grouped Query Attention).
- **토크나이저**: BBPE 기반 102,400 Vocab. 한국어 교착어 특성을 반영하여 MeCab으로 사전 토큰화 후 학습하여 한국어 압축률(2.46)이 타 모델(Llama 3.1: 3.01) 대비 우수함.
- **학습 데이터**: 총 8T tokens (한국어 및 영어 중심).
- **포스트 트레이닝**: SFT(Supervised Fine-Tuning) 및 DPO(Direct Preference Optimization, Offline & Online 순차 적용).

## 2. 주요 성능 지표 (벤치마크)
K-EXAONE 7.8B Instruction 모델은 동급 파라미터 모델 중 최상위권 성능을 기록함.

| 카테고리 | EXAONE 3.0 7.8B | Llama 3.1 8B | Gemma 2 9B | 비고 |
| :--- | :---: | :---: | :---: | :--- |
| **MT-Bench** | **9.01** | 7.95 | 8.52 | 실생활 사용성(1위) |
| **HumanEval** | **72.0** | 64.6 | 61.6 | 코딩 능력(1위) |
| **GSM8K** | 79.8 | 75.9 | 77.2 | 수학 (2위, Phi-3 86.4) |
| **KoMT-Bench** | **8.92** | 6.06 | 7.92 | 한국어 사용성(1위) |
| **LogicKor** | **8.62** | 5.40 | 8.07 | 한국어 논리(1위) |

## 3. 안전성 및 윤리 (Responsible AI)
- **데이터 컴플라이언스**: 뉴스, 도서 등 저작권 위험이 있는 데이터는 배제하고 엄격한 라이선스 리뷰 거침.
- **레드 티밍(Red Teaming)**: 혐오 표현, 성적 콘텐츠, 폭력 등 6개 카테고리에 대해 내부 테스트 결과 84%의 방어율 기록.
- **공개 정책**: 7.8B 모델은 비상업적 연구 용도로 공개되어 생태계 기여 지향.

## 4. 시사점
- **한국어 최적화**: 단순히 번역 데이터가 아닌, 한국어 언어 구조를 고려한 토크나이저와 데이터 큐레이션이 한국어 성능 압도의 핵심임.
- **추론 가속**: NVIDIA H100 클러스터에서 학습되었으나, 추론 시에는 **TensorRT-LLM** 및 리벨리온 NPU 최적화 지원을 통해 실제 서비스 적용 가능성을 높임.

---
**관련 문서**:
- [[wiki/Agents/Implementation/K-EXAONE_Agentic_Capabilities.md]]
- [[wiki/Models/Optimization-and-Serving/Rebellions-NPU-LLM-Serving.md]]
- [[wiki/Models/Optimization-and-Serving/Continuous-Batching.md]]
