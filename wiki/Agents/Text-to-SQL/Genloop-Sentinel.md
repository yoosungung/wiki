---
title: "Genloop Sentinel: Unified Business Memory 기반 에이전틱 T2SQL"
tags: ["T2SQL", "Genloop", "Spider-2.0", "Unified-Business-Memory", "Semantic-Layer"]
type: "wiki"
status: "published"
last_updated: "2026-05-08"
updated: "2026-05-08"
related_notes: ["[[wiki/Agents/Text-to-SQL/Oracle-SOMA-SQL]]", "[[wiki/Agents/Text-to-SQL/T2SQL-Benchmarks-2026]]", "[[wiki/Agents/Text-to-SQL/Agentic-Semantic-Layer]]"]
related_raw: ["[[raw/2026-05-08-daily-research-data.md]]"]
---

# Genloop Sentinel (Agent v2 Pro)

Genloop Sentinel은 2026년 4월 기준, **Spider 2.0 Snow** 벤치마크(Snowflake 환경)에서 **96.70%**라는 압도적인 실행 정확도를 기록하며 글로벌 1위를 유지하고 있는 에이전틱 SQL 분석 프레임워크입니다.

## 1. 핵심 기술: Unified Business Memory (UBM)

Genloop Sentinel의 가장 큰 차별점은 단순히 SQL을 생성하는 능력이 아니라, 기업의 파편화된 비즈니스 지식을 통합하여 에이전트의 **'장기 기억'**으로 활용하는 **Unified Business Memory(UBM)** 기술에 있습니다.

### 1.1 컨텍스트 그래프 추론 (Context Graph Reasoning)
*   **원리**: 데이터베이스의 원시 스키마(Raw Schema)를 직접 참조하는 대신, 테이블 간의 관계, 조인 경로, 비즈니스 지표 정의가 포함된 **비즈니스 컨텍스트 그래프**를 먼저 구축합니다.
*   **효과**: "작년 대비 성장률"과 같은 모호한 질문에 대해, 그래프 상에 정의된 공식과 경로를 따라 추론함으로써 데이터 오해로 인한 오답을 원천 차단합니다.

### 1.2 거버넌스형 시맨틱 레이어 (Governed Semantic Layer)
*   중앙화된 시맨틱 레이어에서 승인된 비즈니스 로직(Metric Definitions)만을 사용하도록 강제하여, 분석 결과의 일관성을 보장합니다.

## 2. 시스템 아키텍처

대규모 엔터프라이즈 환경(150+ DB, 50만+ 컬럼)을 처리하기 위해 고성능 분산 아키텍처를 채택했습니다.

### 2.1 분산 지능 (Decoupled Intelligence)
*   **gRPC Sidecar**: 무거운 벡터 임베딩 및 추론 부하를 메인 시스템에서 분리하여 별도의 사이드카 프로세스에서 처리합니다.
*   **고속 통신**: Unix Domain Sockets(UDS)를 통해 오버헤드를 최소화하며 수십만 개의 컬럼에 대한 의미론적 검색을 수행합니다.

### 2.2 지능형 가드레일 (Smart Guardrails)
*   **루프 감지 (Loop Detection)**: 에이전트가 동일한 오류를 반복하는지 KNN 검색으로 실시간 감지하여, 자가 수정(Self-correction)을 위한 시스템 힌트를 즉시 주입합니다.
*   **금융 레일 (Financial Rails)**: 쿼리 실행 비용 및 토큰 사용량을 실시간 추적하여 예산 초과 시 차단하는 거버넌스 기능을 포함합니다.

## 3. Spider 2.0 Snow 성과의 의미
Spider 2.0 Snow 트랙은 실제 기업의 Snowflake 데이터 웨어하우스 환경을 시뮬레이션합니다. Genloop Sentinel이 **96.70%**를 기록한 것은, **"언어 모델의 일반 지능"**과 **"기업의 특수 지식(UBM)"**이 완벽하게 결합되었을 때 도달할 수 있는 엔터프라이즈 T2SQL의 정점을 보여줍니다.

## 4. AX1센터 R&D 적용 포인트
*   **KM의 메모리 레이어화**: 현재 구축 중인 지식 베이스(KM)를 T2SQL 에이전트의 **Unified Business Memory**로 진화시키는 전략 수립.
*   **시이드카 기반 추론**: 대규모 스키마 처리를 위한 성능 최적화 모델로 gRPC 사이드카 패턴 검토.
*   **가드레일 설계**: 자가 수정을 유도하는 루프 감지 및 힌트 주입 메커니즘 벤치마킹.

---
*참고: 이 문서는 Spider 2.0 SOTA 리포트 및 Genloop 기술 사양을 기반으로 작성되었습니다.*
