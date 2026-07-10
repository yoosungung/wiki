---
title: GraphRAG-vs-LightRAG-2026
related_raw:
  - "[[wiki/RAG/GraphRAG-vs-LightRAG-2026]]"
tags:
  - wiki
  - ai_core
  - ai
type: wiki
status: draft
last_updated: "2026-04-19"
---

# 📊 GraphRAG vs LightRAG: 2026년 성능 및 아키텍처 비교

2026년 초, 지식 그래프 기반 RAG(GraphRAG) 기술은 Microsoft의 GraphRAG와 HKU의 LightRAG 간의 명확한 프로덕션 트레이드오프 단계로 접어들었습니다.

## 1. 핵심 비교 요약 (2026)

| 기능 | GraphRAG (Microsoft) | LightRAG (HKU) |
| :--- | :--- | :--- |
| **질의 비용** | 높음 (수백 개의 API 호출/질의) | **초저비용** (단일 API 호출/질의) |
| **토큰 사용량** | 전역 질의당 ~600,000+ 토큰 | **~100 토큰** (약 6,000배 절감) |
| **지연 시간** | 느림 (~120ms+) | **빠름** (~80ms, 표준 RAG보다 30% 빠름) |
| **인덱싱** | 비쌈; 업데이트 시 전체 재구축 필요 | **증분(Incremental)**; 데이터 추가만으로 업데이트 가능 |
| **핵심 기술** | Leiden Algorithm (커뮤니티 감지) | Dual-Level Retrieval (구체적 + 추상적) |

## 2. 기술적 차별점

### 1) 검색 전략 (Retrieval Strategy)
- **GraphRAG:** 계층적 요약과 커뮤니티 감지를 사용하여 "이 데이터셋의 주요 테마는 무엇인가?"와 같은 전역적인 질문에 답변하는 데 강점을 보입니다.
- **LightRAG:** **이중 레벨 검색(Dual-Level Retrieval)** 시스템을 사용합니다. 특정 엔티티/관계를 추출하는 저수준 키와 광범위한 테마 컨텍스트를 제공하는 고수준 키를 병렬로 실행하여 효율성을 극대화합니다.

### 2) 운영 지속 가능성
- 2026년 현재 GraphRAG의 가장 큰 허들은 '비용 문제'입니다. 대규모 데이터셋 인덱싱에 수천 달러가 소요될 수 있으며, 업데이트 시마다 재인덱싱이 필요합니다.
- 반면 LightRAG는 **지식 그래프를 점진적으로 업데이트**할 수 있는 능력을 갖추어, 매일 데이터가 변하는 프로덕션 환경에서 압도적인 지속 가능성을 제공합니다.

## 3. 2026년 새로운 대안들
- **HippoRAG 2:** 이중 노드 아키텍처를 통해 다중 홉 추론과 단순 팩트 질의 간의 균형을 개선했습니다.
- **T²RAG (Graph-Free Triplet Retrieval):** 공식적인 그래프 구축 없이 질의를 트리플릿(Triplet)으로 분해하여 오버헤드를 더욱 줄인 혁신적인 접근 방식입니다.

## 4. 선택 가이드
- **GraphRAG 선택:** 예산이 충분하고 데이터가 정적이며, 깊은 "커뮤니티 수준"의 분석이나 전역적 요약이 필요한 경우.
- **LightRAG 선택:** 챗봇과 같이 응답 속도가 중요하고, 예산이 제한적이며, 지식 베이스를 수시로 업데이트해야 하는 경우.

---
## 🔗 관련 링크 및 참고 자료
- 원문: [GraphRAG vs LightRAG Performance 2026](https://maargasystems.com/blog/graphrag-vs-lightrag/)
- 관련 노트: [[wiki/RAG/GraphRAG]], Resources/Knowledge-Graph/LightRAG, [[wiki/RAG/RAG-Optimization-Contextual-Retrieval-2026]]
