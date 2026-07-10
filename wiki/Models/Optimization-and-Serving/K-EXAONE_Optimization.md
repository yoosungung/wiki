---
title: "K-EXAONE 모델의 아키텍처 및 서빙 최적화"
date: "2026-05-08"
tags: ["EXAONE", "MoE", "Optimization", "LG-AI"]
related_raw: ["[[raw/2026-05-08-exaone-k-exaone-236b.md]]"]
---

# K-EXAONE 모델의 아키텍처 및 서빙 최적화

LG AI 연구원에서 개발한 **K-EXAONE 236B-A23B**는 다국어(6개 국어)를 지원하는 대규모 언어 모델로, 성능과 추론 효율성을 극대화하기 위한 다양한 아키텍처 설계와 서빙 최적화 기술이 적용되었습니다.

## MoE 기반 효율적 아키텍처
- **파라미터 효율성**: 총 236B 파라미터 중 추론 시 23B의 파라미터만 활성화되는 Fine-grained Mixture-of-Experts (MoE) 아키텍처를 채택했습니다. 
- **투기적 해독(Speculative Decoding)**: MTP(Multi-Token Prediction)에 최적화되어 있어 Self-speculative decoding을 가능하게 하며, 이를 통해 추론 처리량(Throughput)을 약 1.5배 향상시킵니다.

## 롱 컨텍스트(Long-Context) 메모리 최적화
- **하이브리드 어텐션(Hybrid Attention)**: 최대 256K 토큰의 긴 컨텍스트를 기본적으로 지원하기 위해 3:1 비율의 하이브리드 어텐션 구조를 사용합니다. 
- **Sliding Window**: 128 토큰 크기의 슬라이딩 윈도우를 활용하여 긴 문서를 처리할 때 발생하는 메모리 사용량을 대폭 최소화했습니다.
- 토큰 효율성 향상을 위해 150k 크기의 SuperBPE 어휘 사전을 재설계하여 기존 대비 약 30%의 토큰 효율을 개선했습니다.

## 호환성 및 배포(Deployment)
K-EXAONE은 주요 서빙 프레임워크와 완벽하게 통합됩니다.
- **vLLM**: Tensor Parallelism(예: 4 H200 GPUs)을 활용하여 분산 서빙이 가능하며, MTP 기반의 Speculative Decoding을 vLLM 환경에서 바로 사용할 수 있습니다.
- **SGLang 및 llama.cpp**: 최신 SGLang 서버와 로컬 실행을 위한 GGUF 포맷(llama.cpp)을 지원하여 다양한 추론 환경에 유연하게 대응합니다.

관련 문서:
- [[wiki/Models/Architectures/Mixture_of_Experts.md]]
- [[wiki/Agents/Implementation/K-EXAONE_Agentic_Capabilities.md]]
- [[wiki/Models/Optimization-and-Serving/Rebellions_ATOM_Max_NPU_Serving.md]]
