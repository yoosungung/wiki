---
title: "Metadata RAG (Schema Pruning) 가이드"
related_raw: ["[[raw/2026-04-19-T2SQL-Semantic-Layer-Metadata-RAG-Trend]]"]
tags: ["wiki", "T2SQL", "RAG", "Metadata-RAG", "Schema-Pruning"]
type: "wiki"
status: "published"
last_updated: "2026-04-19"
updated: "2026-04-19"
---

# Metadata RAG (Metadata Retrieval-Augmented Generation)

Metadata RAG는 대규모 엔터프라이즈 데이터베이스 환경에서 LLM이 질문에 필요한 핵심 스키마 정보만을 동적으로 추출하여 전달하는 **지능형 스키마 프루닝(Schema Pruning)** 기술입니다.

## 🌟 핵심 개념 (2026년 기준)

### 1. 지식 런타임 (Knowledge Runtime)으로의 진화
단순한 검색-생성 파이프라인을 넘어, 검색, 추론, 검증, 거버넌스를 통합 관리하는 오케스트레이션 계층입니다. 메타데이터 자체가 에이전트의 판단 근거가 되는 '지식 베이스' 역할을 수행합니다.

### 2. 결정론적 프루닝 (Deterministic Pruning)
LLM 호출 없이 외래 키(FK) 그래프 탐색과 엔티티 해상도를 통해 컨텍스트를 90% 이상 압축합니다. 질문과 직접 관련된 테이블뿐만 아니라, Join 경로상에 있는 필수 연결 테이블을 규칙 기반으로 자동 포함합니다.

### 3. Contextual Chunks & Caching
- **Contextual Chunks**: 메타데이터를 텍스트와 함께 임베딩하여 검색 정밀도를 극대화합니다.
- **Context Caching**: 빈번하게 참조되는 공통 스키마 정의나 시맨틱 레이어 정보를 KV 캐싱하여 비용과 지연 시간을 단축합니다.

## 🛠 아키텍처 구성

### 단계 1: 조대 검색 (Coarse Retrieval)
사용자 질문을 벡터화하여 Vector DB(Milvus, Pinecone 등)에서 관련 테이블 및 컬럼 후보군(Top-K)을 추출합니다. 이 단계에서는 테이블의 설명(Description)과 비즈니스 용어가 주요 지표가 됩니다.

### 단계 2: 정밀 선택 (Fine-grained Selection)
추출된 후보군을 바탕으로 LLM(또는 고속 분류 모델)이 실제 쿼리 작성에 필요한 컬럼을 확정합니다. 이때 **샘플 데이터**를 함께 참조하여 'ID'가 '이름'인지 '코드'인지 등을 명확히 구분합니다.

### 단계 3: 스키마 링크 (Schema Linking)
선택된 엔티티들 간의 관계(ERD)를 기반으로 최소 Join 경로를 구성하여 최종 프롬프트에 삽입할 '스키마 스니펫'을 생성합니다.

## 🚀 기대 효과
- **Hallucination 방지**: 관련 없는 테이블/컬럼에 의한 오답 생성 최소화.
- **비용 최적화**: 전체 스키마 대신 필요한 정보만 전달하여 토큰 사용량 70~90% 절감.
- **추론 성능 향상**: LLM이 더 좁고 명확한 컨텍스트 내에서 복잡한 SQL 로직에 집중 가능.

## 🔗 관련 문서
- [[T2SQL_Planning]]
- [[wiki/Agents/Text-to-SQL/Semantic-Layer-DeepAgent-Filesystem]]
- [[wiki/Agents/Text-to-SQL/DeepAgent-T2SQL]]
- [[wiki/Agents/Text-to-SQL/Spider-2.0]]
