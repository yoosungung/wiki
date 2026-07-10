---
related_raw: ["[[raw/2026-06-25-lfm2_5_retrieval_models_architecture.md]]"]
tags: [Models/Small-Models, LFM2_5, Embedding, Retrieval, Korean]
---

# LFM2.5-Embedding-350M 모델 분석

Liquid AI에서 2026년 6월에 발표한 **LFM2.5-Embedding-350M**은 온디바이스(On-device) 및 에지(Edge) 환경에서 초저지연·고성능 검색을 구현하기 위해 설계된 dense bi-encoder 임베딩 모델입니다.

---

## 1. 모델 사양 및 아키텍처
*   **개발사**: Liquid AI (2026년 6월 발표)
*   **기반 아키텍처**: LFM2.5-350M-Base (기존 Causal Decoder에 Bidirectional Patch를 적용하여 Retrieval 태스크용 Bi-encoder로 최적화)
*   **출력 임베딩 차원**: 1024차원 (CLS pooling 기반 조밀 벡터 출력)
*   **파라미터 크기**: 350M
*   **아키텍처적 특징**:
    *   **게이티드 숏 컨볼루션 블록 (Gated Short Convolution Blocks)**: LIV(Linear Input Variant) 메커니즘을 사용해 KV 캐시가 필요 없으며 메모리 풋프린트를 크게 낮춥니다.
    *   **GQA (Grouped-Query Attention)**: 글로벌 시퀀스 믹싱을 담당하며 전역 문맥을 유지합니다.

---

## 2. 한국어 및 다국어 처리 성능
LFM2.5-Embedding-350M 모델은 한국어를 공식적으로 지원하는 11개 다국어 모델 중 하나로 훈련되어 한국어 검색에 우수한 성능을 보입니다.

*   **공식 지원 언어**: 한국어, 영어, 일본어, 아랍어, 독일어, 스페인어, 프랑스어, 이탈리아어, 노르웨이어, 포르투갈어, 스웨덴어
*   **다국어 벤치마크 결과**:
    *   **NanoBEIR (Multilingual Extended)**: `0.577` (NDCG@10)
    *   **MKQA-11 (다국어 QA)**: `0.691` (Recall@20)
*   **한국어 및 다국어 강점**: 350M 파라미터 크기로 가벼우면서도, 크기가 1.7배 더 큰 **Qwen3-Embedding-0.6B** 등의 경쟁 모델 성능을 상회하여 가성비가 높은 다국어 RAG 환경을 제공합니다. 특히 한국어 텍스트의 형태소 및 문맥 특성을 1024차원의 밀집 벡터로 잘 보존하여 의미론적(Semantic) 검색 성능이 뛰어납니다.

---

## 3. 온디바이스 & Edge 배포 강점
*   **호환성**: GGUF 포맷을 지원하여 `llama.cpp` 또는 `Ollama`를 통해 외부 API 없이 완전 오프라인 RAG 환경을 구성할 수 있습니다.
*   **지연 속도**: 쿼리 임베딩 생성 지연 시간이 10ms 미만으로 초저지연 검색 속도를 제공합니다.

---

## 🔗 관련 링크
*   소형 모델 MOC: [[wiki/Models/Small-Models/000_Small-Models-MOC.md]]
*   자매 모델 (Late Interaction): [[wiki/Models/Small-Models/LFM2.5-ColBERT.md]]
