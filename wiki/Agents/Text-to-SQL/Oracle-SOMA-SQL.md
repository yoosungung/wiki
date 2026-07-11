---
title: "Oracle SOMA-SQL: 엔터프라이즈 특화 NL2SQL 프레임워크"
tags: ["T2SQL", "Oracle", "Spider-2.0", "Ambiguity-Resolution", "Synthetic-Query-Logs"]
type: "wiki"
status: "published"
last_updated: "2026-05-08"
updated: "2026-05-08"
related_raw: ["[[raw/2026-05-08-daily-research-data.md]]"]
related_notes: ["[[wiki/Agents/Text-to-SQL/T2SQL-Benchmarks-2026]]", "[[wiki/Agents/Text-to-SQL/2026-04-26-T2SQL-Trends-Update]]"]
---

# Oracle SOMA-SQL

Oracle SOMA-SQL은 2026년 4월 기준, **Spider 2.0 Lite** 벤치마크에서 실행 정확도 **72.02%**로 1위를 기록한 차세대 Text-to-SQL(T2SQL) 프레임워크입니다. 상용 DB 벤더인 Oracle이 엔터프라이즈 환경의 복잡성과 모호성을 해결하기 위해 개발했습니다.

## 1. 핵심 아키텍처: SOMA (Synthetic & Optimized Multi-source Ambiguity Resolution)

SOMA-SQL의 핵심은 단순히 쿼리를 생성하는 것이 아니라, 데이터와 질문 사이의 **모호성(Ambiguity)**을 체계적으로 탐지하고 해결하는 구조에 있습니다.

### 1.1 합성 쿼리 로그 (Synthetic Query Logs)
실제 쿼리 로그가 부족한 환경에서도 도메인 지식을 확보하기 위한 기술입니다.
*   **원리**: 데이터베이스 스키마와 데이터 분포를 분석하여 수만 개의 가상 쿼리(Synthetic Queries)를 생성하고 실행합니다.
*   **효과**: 모델은 사전 학습 단계에서 해당 DB의 비즈니스 로직(집계 방식, 조인 관계 등)을 미리 파악하여, 사용자 질문이 들어왔을 때 텍스트 일치 이상의 시맨틱 추론을 수행할 수 있습니다.

### 1.2 실행 기반 모호성 해소 (Execution-Grounded Probing)
쿼리 생성 과정에서 DB 엔진을 직접 활용하는 '프로빙(Probing)' 기법을 사용합니다.
*   **동작**: 모호한 질문에 대해 여러 후보 SQL을 생성한 후, DB에서 샘플 실행을 수행합니다.
*   **검증**: 실행 결과(값의 범위, 데이터 타입, 결과 행 수 등)를 분석하여 사용자의 의도와 가장 일치하는 최적의 SQL을 선택하거나 스스로 수정합니다.

## 2. 초거대 스키마 (1,000+ 컬럼) 대응 전략

엔터프라이즈급 데이터 웨어하우스의 복잡한 구조를 처리하기 위해 3단계 압축 전략을 사용합니다.

1.  **계층적 필터링**: 합성 로그 패턴을 기반으로 질문과 관련 없는 테이블을 1차 제외합니다.
2.  **에이전틱 컨텍스트(Agentic Context) 구성**: 질문 해결에 필요한 핵심 컬럼들만 추출하여 LLM이 처리 가능한 최적의 컨텍스트 윈도우를 형성합니다.
3.  **구조화된 계획(Structured Planning)**: 복잡한 다단계 질문을 중간 추론 단계로 분해하여, 한 번에 수백 개의 컬럼을 참조하지 않고 필요한 단계에서 필요한 컬럼만 호출합니다.

## 3. 성능 및 벤치마크 결과
*   **Spider 2.0 Lite**: 72.02% (Execution Accuracy) - 1위 (2026.04)
*   **특징**: BigQuery, Snowflake, SQLite 등 다양한 환경에서 높은 일반화 성능을 보이며, 특히 장문 컨텍스트(100줄 이상의 SQL) 생성 능력이 탁월함.

## 4. AX1센터 R&D 시사점
*   **DB 엔진 결합 모델**: 단순 언어 모델의 성능보다 DB 엔진의 실행 신호(Execution Signals)를 피드백 루프에 넣는 것이 실질적인 정확도 향상의 열쇠임.
*   **합성 데이터 활용**: 내부 프로젝트 적용 시, 도메인 특화 데이터셋 부족 문제를 '합성 쿼리 생성기' 도입으로 해결하는 전략 벤치마킹 필요.

---
*참고: 이 문서는 Spider 2.0 벤치마크 업데이트 및 Oracle 기술 블로그 내용을 기반으로 합성되었습니다.*
