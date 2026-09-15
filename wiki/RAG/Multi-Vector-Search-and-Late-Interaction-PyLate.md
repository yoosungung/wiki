---
title: "다중 벡터 검색 (Multi-Vector Search) 및 Late Interaction (PyLate) 아키텍처"
date: "2026-07-31"
last_updated: "2026-07-31"
updated: "2026-07-31"
related_raw: ["[[2026-07-31-amelie-chatelain-multi-vector-search-late-interaction.md]]"]
tags: ["RAG", "Multi-Vector-Search", "Late-Interaction", "PyLate", "ColBERT", "Information-Retrieval"]
type: "wiki"
---

# 다중 벡터 검색 (Multi-Vector Search) 및 Late Interaction (PyLate) 아키텍처

전통적인 밀집 벡터 검색(Single-Vector Dense Retrieval)은 문장이나 전체 문서를 하나의 고정 차원 벡터(예: 768차원 또는 1536차원)로 압축합니다. 이 방식은 문맥의 전체적인 의미는 잘 표현하지만, 특정 단어의 부분 일치, 고유명사, 혹은 코드 심볼과 같은 세부적인 키워드를 정확하게 매칭하지 못한다는 한계를 지닙니다.

**다중 벡터 검색 (Multi-Vector Search)**과 **Late Interaction (지연 상호작용)** 모델(예: ColBERT)은 이를 해결하기 위해 문서와 쿼리의 모든 토큰별로 개별 벡터를 부여하고 매칭을 늦춰 연산하는 아키텍처입니다.

## 1. Late Interaction (지연 상호작용) 개념 및 메커니즘

- **Early Interaction (교차 인코더)**: 쿼리와 문서를 처음부터 하나로 결합하여 양방향 어텐션을 통과시킵니다. 정확도는 가장 높으나 대규모 문서를 사전에 벡터화할 수 없고 매 검색 시마다 LLM 급의 거대한 연산이 필요해 속도가 극도로 느립니다.
- **Late Interaction (지연 상호작용)**:
  1. **사전 임베딩**: 말뭉치(Corpus)의 모든 문서의 각 토큰 임베딩을 오프라인에서 미리 계산해 둡니다.
  2. **쿼리 임베딩**: 검색 시 입력된 쿼리의 모든 토큰 임베딩을 온라인에서 계산합니다.
  3. **지연 매치 (MaxSim 연산)**: 쿼리의 토큰 $q_i$와 문서의 토큰 $d_j$ 벡터 간의 유사도를 구한 뒤, 쿼리의 각 토큰별로 가장 큰 유사도를 가지는 문서 토큰의 최대값들(MaxSim)을 더해 최종 문서 점수를 산출합니다.

```text
       Early Interaction                 Late Interaction (ColBERT/PyLate)
       =================                 =================================
  
  [Query] ───┐                      [Query] ───► [Query Token Embs] ──┐
             ├──► [Bi-Encoder] ──►                                    ├──► [MaxSim Operator]
  [Doc] ─────┘                      [Doc]   ───► [Doc Token Embs]   ──┘
```

## 2. 핵심 구현체 및 오픈소스

- **ColBERT-Zero**: 추가적인 도메인 학습 없이 제로샷(Zero-shot) 환경에서도 높은 정확도를 유지하는 Late Interaction 모델.
- **PyLate**: Late Interaction 모델의 학습 및 추론 파이프라인을 손쉽게 구성할 수 있도록 지원하는 고성능 파이썬 오픈소스 라이브러리.
- **RAG에서의 의의**: 컨텍스트 윈도우가 늘어났음에도 불구하고, 신뢰성 있고 저비용의 정밀한 정보 매칭을 위해서는 다중 벡터 검색을 통한 1차 후보군 필터링이 필수적입니다.

## 3. PyLate를 활용한 쿼리 임베딩 추출 예시

```python
# PyLate 기반 쿼리 임베딩 생성 개념 코드
from pylate import LateInteractionModel

# 1. 사전 학습된 ColBERT 기반 Late Interaction 모델 로드
model = LateInteractionModel.from_pretrained("lighton/colbert-zero-v1")

# 2. 쿼리 및 문서 토큰별 다중 벡터 추출
query_vectors = model.encode_query("What is late interaction in RAG?")
document_vectors = model.encode_document("Late interaction computes MaxSim over token embeddings.")

# 3. 토큰 차원 확인 (각 토큰마다 개별 벡터 할당됨)
print("Query shape:", query_vectors.shape) 
# 출력 예시: (1, 32, 128) -> (배치, 최대 토큰 수, 임베딩 차원)
```

## 🔗 연결된 문서
- [[wiki/RAG/LFM2.5-Embedding-및-ColBERT-검색-모델-2026.md]]
- [[wiki/RAG/SOTA-OCR-및-문서-정규화-기술.md]]
- [[wiki/RAG/000_RAG-MOC.md]]
