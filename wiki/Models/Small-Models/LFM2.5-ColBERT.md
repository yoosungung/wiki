---
related_raw: ["[[raw/2026-06-25-lfm2_5_retrieval_models_architecture.md]]"]
tags: [Models/Small-Models, LFM2_5, ColBERT, Retrieval, Late-Interaction]
---

# LFM2.5-ColBERT-350M 모델 분석

Liquid AI에서 2026년 6월에 발표한 **LFM2.5-ColBERT-350M**은 높은 검색 품질과 일반화 성능을 제공하기 위해 설계된 Late Interaction(지연 상호작용) 기반의 다국어 검색 모델입니다.

---

## 1. 모델 사양 및 아키텍처
*   **개발사**: Liquid AI (2026년 6월 발표)
*   **기반 아키텍처**: LFM2.5-350M-Base (양방향 패치를 적용한 비인과적 구조)
*   **출력 임베딩 차원**: 토큰당 128차원 벡터
*   **파라미터 크기**: 350M
*   **아키텍처적 특징**:
    *   **게이티드 숏 컨볼루션 블록 (Gated Short Convolution Blocks)** & **GQA (Grouped-Query Attention)** 하이브리드 구조를 사용합니다.
    *   문서와 쿼리의 토큰 수준 벡터 정보를 압축하지 않고 보존하여 세밀한 매칭을 수행합니다.

---

## 2. Late Interaction & MaxSim 매커니즘
*   **작동 원리**: 전체 문서를 하나의 벡터로 만드는 Dense Embedding과 달리, 문서를 구성하는 각 토큰별로 128차원 벡터를 생성하여 저장합니다.
*   **MaxSim (Maximum Similarity) 연산**: 쿼리의 각 토큰 벡터와 문서 내 모든 토큰 벡터 간의 내적(Dot Product)을 계산하여 최댓값들을 합산하는 방식으로 관련성을 평가합니다.
*   **장단점**:
    *   **장점**: 단어 수준 매칭이 이루어지므로 검색 정확도가 매우 높고 도메인 외(Out-of-domain) 일반화가 탁월합니다.
    *   **단점**: 토큰 개수만큼 벡터를 저장하므로 인덱스 디스크 공간(Footprint)이 큽니다.

---

## 3. 다국어 벤치마크 성능
한국어를 포함한 11개 다국어 환경을 지원하며, 동일 350M 검색 모델 중 최고 수준의 성능을 입증했습니다.

| 벤치마크 | 지표 | LFM2.5-ColBERT-350M 점수 | LFM2.5-Embedding-350M (Dense) 대비 |
| :--- | :--- | :--- | :--- |
| **NanoBEIR** | NDCG@10 | `0.605` | +0.028 우수 |
| **MKQA-11** | Recall@20 | `0.694` | +0.003 우수 |

*   Dense 방식의 LFM2.5-Embedding보다 인덱스 용량은 늘어나지만, 검색 정확도가 정교하게 향상되는 이점이 있습니다.

---

## 🔗 관련 링크
*   소형 모델 MOC: [[wiki/Models/Small-Models/000_Small-Models-MOC.md]]
*   자매 모델 (Dense 임베딩): [[wiki/Models/Small-Models/LFM2.5-Embedding.md]]
