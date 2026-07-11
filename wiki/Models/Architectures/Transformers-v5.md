---
title: Transformers-v5
related_raw:
  - "[[wiki/Models/Architectures/Transformers-v5]]"
tags:
  - wiki
  - ai_core
  - models_and_libraries
  - llm_frameworks_and_libraries
type: wiki
status: draft
last_updated: "2026-04-19"
updated: "2026-04-19"
---

# Transformers v5

**출처**: [원본 링크](https://huggingface.co/blog/transformers-v5)

Hugging Face가 Transformers v5.0.0rc-0를 출시했습니다. v5는 단순성, 훈련, 추론, 프로덕션을 중심으로 상호 운용성을 핵심 테마로 합니다.

## 주요 기술적 변경 사항

*   **단순성:**
    *   **모듈식 접근 방식:** 유지보수 용이성, 빠른 통합, 협업 개선을 위해 모듈식 설계를 강화했습니다.
    *   **AttentionInterface 도입:** 어텐션 메서드(FA1/2/3, FlexAttention, SDPA 등)를 위한 중앙 집중식 추상화를 제공합니다.
    *   **코드 감소:** 모델링 및 토큰화 파일을 간소화했으며, "Fast" 및 "Slow" 토크나이저 개념을 제거하고 `tokenizers` 백엔드에 집중합니다.
    *   **PyTorch 단독 지원:** Flax/TensorFlow 지원을 중단하고 PyTorch에 집중하며, Jax 생태계와의 호환성을 위해 노력합니다.
*   **훈련:**
    *   대규모 사전 훈련 및 전체 훈련 지원을 강화했습니다.
    *   `torchtitan`, `megatron`, `nanotron` 등과의 호환성을 확장했습니다.
    *   `Unsloth`, `Axolotl`, `LlamaFactory`, `TRL`, `MaxText`와 같은 미세 조정 도구와의 협력을 지속합니다.
*   **추론:**
    *   특수 커널, 깔끔한 기본값, 새로운 API, 최적화된 추론 엔진 지원에 중점을 둡니다.
    *   연속 배치 및 페이지드 어텐션 메커니즘을 위한 새로운 API를 제공합니다.
    *   `transformers serve`를 통해 OpenAI API 호환 서버를 배포하는 새로운 서빙 시스템을 도입합니다.
*   **프로덕션 및 로컬:**
    *   `vLLM`, `SGLang` 등 인기 있는 추론 엔진의 백엔드로 Transformers를 활용합니다.
    *   `ONNXRuntime`, `llama.cpp`, `MLX`와의 긴밀한 협력을 통해 상호 운용성을 높였습니다.
    *   GGUF 파일 로딩 및 변환을 용이하게 합니다.
    *   `executorch`를 통해 온디바이스 모델을 위한 로컬 추론을 확장하고, `optimum`을 통해 멀티모달 모델을 지원합니다.
*   **양자화:**
    *   v5에서 양자화를 핵심 기능으로 다루며, 주요 기능과의 완벽한 호환성을 보장합니다.
    *   가중치 로딩 방식에 큰 변화를 주어 양자화를 일등 시민으로 만듭니다.

---
## 관련 노트
- [[wiki/Models/Optimization-and-Serving/SGLang LLM 서빙 프레임워크 리뷰]]
- [[wiki/Engineering/Infrastructure-and-DevOps/DGX Spark에서의 VLM 파인튜닝]]
- [[wiki/Models/RL/TRL-OpenEnv Integration for Training LLMs]]
- [[wiki/Models/SFT/Fine-Tuning]]
