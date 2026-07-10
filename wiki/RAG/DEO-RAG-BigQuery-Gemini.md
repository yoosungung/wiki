---
title: "DEO-RAG: BigQuery와 Gemini를 활용한 고도화된 RAG 시스템"
related_raw:
  - "[[#googlecloud #bigquery #gemini #rag #deo #negationawareretrieval #nlp #embedding | Sungmin Kim.md]]"
  - "[[my-adk-python-samplesRAGdeo-rag-with-bigquery at main · ksmin23my-adk-python-samples.md]]"
tags: ["RAG", "Google_Cloud", "BigQuery", "Gemini", "DEO-RAG", "Negation_Aware_Retrieval"]
type: "wiki"
status: "published"
last_updated: "2026-05-01"
---

# DEO-RAG: BigQuery와 Gemini를 활용한 고도화된 RAG 시스템

## 1. 개요
DEO-RAG는 Google Cloud의 BigQuery와 Gemini 모델을 결합하여 데이터 엔트로피를 최적화하고 정밀한 정보 검색을 수행하는 RAG(Retrieval-Augmented Generation) 아키텍처입니다. 특히 부정어 인식 검색(Negation-aware Retrieval)과 같은 고도의 NLP 기법을 적용하여 검색의 정확도를 극대화합니다.

## 2. 주요 구성 요소 및 기술
- **BigQuery Vector Search**: 대규모 데이터셋에 대한 효율적인 벡터 유사성 검색을 수행합니다.
- **Gemini Pro/Flash**: 검색된 컨텍스트를 분석하여 답변을 생성하고, 다단계 추론을 수행합니다.
- **Negation-aware Retrieval**: "A가 아닌 B"와 같은 부정 표현을 정확히 인식하여 잘못된 정보를 필터링합니다.
- **Embedding Optimization**: BigQuery 내에서 직접 임베딩 모델을 호출하여 데이터 이동을 최소화하고 처리 속도를 높입니다.

## 3. 구현 특징
- **Serverless Architecture**: 인프라 관리 없이 대규모 RAG 파이프라인을 운영할 수 있습니다.
- **Data-centric Approach**: 데이터가 저장된 위치(BigQuery)에서 직접 검색과 추론을 수행하여 보안과 효율성을 동시에 확보합니다.
- **Python SDK 통합**: `my-adk-python-samples`에서 제공하는 샘플 코드를 통해 빠르게 프로토타이핑이 가능합니다.

## 4. 활용 사례
- 대규모 엔터프라이즈 문서 검색
- 복잡한 비즈니스 로직이 포함된 질의응답 시스템
- 높은 정밀도가 요구되는 법률 및 기술 문서 분석

## 관련 자원
- [GitHub: deo-rag-with-bigquery 샘플 코드](https://github.com/ksmin23/my-adk-python-samples/tree/main/RAG/deo-rag-with-bigquery)
- [[wiki/RAG/000_RAG-MOC.md|RAG 관리 맵 (MOC)]]
- [[wiki/Engineering/Data-and-Security/000_Data-and-Security-MOC.md|데이터 및 보안 MOC]]
