# Agent View: 심층 추론 에이전트를 위한 스키마 추상화 계층 설계

## 1. 개요 (Abstract)
본 문서는 Text-to-SQL(T2SQL) 태스크에서 LLM의 추론 성능을 극대화하기 위한 **Agent View** 아키텍처를 정의한다. Agent View는 대규모 데이터베이스 스키마에서 발생하는 인지적 부하(Cognitive Load)를 줄이고, 에이전트가 비즈니스 로직에 집중할 수 있도록 최적화된 동적 지식 인터페이스를 제공하는 것을 목적으로 한다.

## 2. 핵심 메커니즘 (Key Methodologies)

### 2.1 의도 기반 스키마 프루닝 (Intent-Driven Schema Pruning)
* **목적**: 질문과 무관한 테이블/컬럼 제거를 통한 Attention 분산 방지.
* **프로세스**: 
    1. 사용자 질문의 엔티티 및 관계 추출.
    2. 스키마 지식 그래프에서 관련 노드 검색.
    3. 쿼리 생성에 필수적인 최소 스키마 집합 도출.

### 2.2 시맨틱 메타데이터 보강 (Semantic Metadata Augmentation)
* **내용**: 단순 DDL을 넘어선 컨텍스트 주입.
    * **Data Profiling**: 주요 컬럼의 값 분포 및 샘플 데이터.
    * **Business Rules**: 계산 로직(예: 매출액 = 합계 - 환불) 및 도메인 제약 사항.
    * **Join Topology**: 테이블 간의 논리적 연결 경로 명시.

### 2.3 적응형 추론 루프 (Adaptive Reasoning Loop)
* **JIT Schema Probing**: 에이전트가 추론 과정에서 정보 부족을 감지할 경우, 능동적으로 도구를 호출하여 Agent View를 확장하는 기법.

## 3. DeepAgent 통합 아키텍처 (Proposed Architecture)

| 모듈 | 역할 | 비고 |
| :--- | :--- | :--- |
| **Schema Selector** | 질문 분석 및 기초 테이블 선별 | Semantic Search 활용 |
| **View Contextualizer** | 선별된 스키마에 비즈니스 룰 및 샘플 주입 | Agent View 완성 |
| **Reasoning Core** | Agent View를 바탕으로 SQL 논리 설계 | CoT(Chain-of-Thought) 수행 |
| **Self-Validator** | 작성된 SQL의 비즈니스 정합성 검증 | Agent View 기반 Reflection |

## 4. 기대 효과 (Expected Impact)
* **정확도 향상**: 복잡한 조인(Join) 및 서브쿼리가 포함된 문제에서 환각(Hallucination) 유의미하게 감소.
* **토큰 최적화**: 불필요한 스키마 주입을 방지하여 추론 비용 절감 및 컨텍스트 윈도우 효율 증대.
* **유지보수성**: DB 스키마 변경 시 에이전트의 뷰 생성 로직만 업데이트하여 유연한 대응 가능.

---
*Last Updated: 2026-04-27*
*Status: Draft / Research Phase*