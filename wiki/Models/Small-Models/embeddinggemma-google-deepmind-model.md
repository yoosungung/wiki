---
title: "EmbeddingGemma 및 EmbeddingGemma 2: Google DeepMind 온디바이스 통합 멀티모달 임베딩 모델"
related_raw: ["[[wiki/Models/Small-Models/embeddinggemma-google-deepmind-model.md]]", "[[2026-11-03-EmbeddingGemma-2-Multimodal-Embedding-Paper.md]]"]
tags: ['wiki', 'ai_core', 'models_and_libraries', 'llm_models', 'EmbeddingGemma-2', 'Multimodal-Embedding', 'Matryoshka']
type: "wiki"
status: "published"
last_updated: "2026-11-03"
updated: "2026-11-03"
---

# EmbeddingGemma 및 EmbeddingGemma 2 (Google DeepMind)

## 1. EmbeddingGemma (1세대, 308M 텍스트 다국어 임베딩)
Google DeepMind의 다국어 임베딩 모델인 EmbeddingGemma는 온디바이스용으로 최적화되었습니다. 주요 기능은 다음과 같습니다.
*   **컴팩트한 크기:** 3억 8백만(308M) 개의 매개변수로 효율성과 성능의 균형을 맞춥니다.
*   **메모리 효율성:** Q4_0 및 Q8_0 양자화를 통해 200MB RAM 미만에서 실행할 수 있습니다.
*   **성능:** 5억 개 미만 매개변수 모델에 대한 MTEB 리더보드를 주도합니다.
*   **다국어 지원:** 100개 이상의 언어를 지원합니다.
*   **컨텍스트 길이:** 최대 2k 토큰을 지원합니다.
*   **유연한 임베딩:** 768차원 임베딩에 Matryoshka 표현 학습(MRL)을 사용하여 512, 256 또는 128차원으로 트리밍할 수 있습니다.
*   **광범위한 통합:** SentenceTransformers, Transformers.js, TEI(Text Embeddings Inference) 및 기타 오픈 소스 솔루션과의 제로데이 지원.
*   **라이선스:** Gemma 커뮤니티 라이선스에 따라 사용할 수 있습니다.

---

## 2. EmbeddingGemma 2 (740M 네이티브 통합 멀티모달 임베딩 논문)
Google DeepMind가 발표한 **EmbeddingGemma 2**(*Unified and Efficient Multimodal Representations*)는 **텍스트, 이미지, 오디오, 비디오 및 그 복합 조합**을 단일 768차원 공유 벡터 공간(Unified Vector Space)에 네이티브로 매핑하는 오픈 멀티모달 임베딩 모델입니다([[wiki/Models/Optimization-and-Serving/스마트폰-환경의-LLM-서빙-기술-2026.md|LiteRT-LM v0.18.0+ 네이티브 지원]]).

### 2.1 핵심 아키텍처 및 학습 혁신
1. **단순화된 레이어별 임베딩(Simplified Per-Layer Embeddings)**: 복잡한 교차 어텐션 오버헤드 없이 레이어별 임베딩 구조를 단순화하여 온디바이스 추론 속도와 표현력을 동시에 확보했습니다.
2. **모달리티 및 목적 함수 점진적 다단계 커리큘럼(Multi-Stage Curriculum)**: 단일 모달리티(Unimodal)에서 교차 모달리티(Cross-modal), 복합 모달리티(Mixed-modal) 순으로 학습 단계와 대조 학습 목적 함수를 점진적으로 확장하여 모든 모달리티 조합에서 높은 검색 정합성을 달성했습니다.
3. **파레토 프런티어(Pareto Frontier) 갱신**: 모달리티별 특화 모델(Specialist models)뿐만 아니라 **2배~12배 더 큰 대형 멀티모달 임베딩 모델들을 능가**하는 성능을 기록했습니다.

### 2.2 온디바이스 및 리소스 제약 환경 최적화 (4대 유연성)
- **선택적 모달리티 인코더 로딩(Selective Modality Encoder Loading)**: 실행 시점에 필요한 모달리티(예: 텍스트+이미지만 사용하고 오디오 인코더는 언로드)만 메모리에 적재하여 모바일 RAM 점유율을 최소화합니다.
- **가변 비전 토큰 예산(Adjustable Vision Token Budgets)**: 디바이스 연산 여유에 따라 이미지·비디오당 생성하는 비전 토큰 수를 동적으로 조절합니다.
- **절단 가능한 임베딩 차원(Truncatable Embedding Dimensions / MRL)**: Matryoshka 표현 학습을 통해 재학습 없이 768차원 벡터를 512, 256, 128차원으로 절단해 벡터 인덱스 용량을 절감합니다.
- **가중치 양자화(Quantized Weights)**: INT4/INT8 양자화 배포 시에도 멀티모달 검색 품질 저하를 최소화하도록 설계되었습니다.

## 🔗 관련 문서
- [[wiki/Models/Optimization-and-Serving/스마트폰-환경의-LLM-서빙-기술-2026.md]]
- [[wiki/Models/Small-Models/000_Small-Models-MOC.md]]