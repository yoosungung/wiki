---
title: "sLM-Text-to-SQL-MATS-Schema-Linking-2026"
related_raw: ["[[wiki/Agents/Text-to-SQL/sLM-Text-to-SQL-MATS-Schema-Linking-2026.md]]"]
tags: ['wiki', 'agents_and_systems', 'text-to-sql_(t2sql)_&_analytics', 'slm_for_text-to-sql_and_schema_linking']
type: "wiki"
status: "published"
last_updated: "2026-04-19"
---

# sLM 기반 Text-to-SQL 및 Schema Linking 최신 동향 (2026.04)

## 개요
2026년 4월 초 현재, sLM(소형 언어 모델)을 활용한 Text-to-SQL 기술은 단순히 SQL을 생성하는 단계를 넘어, **멀티 에이전트 구조**와 **세밀한 Schema Linking** 기법을 통해 GPT-4급의 성능을 저비용으로 구현하는 방향으로 진화하고 있습니다.

## 핵심 내용

### 1. MATS (Multi-Agent Text-to-SQL) 프레임워크의 도약
*   **성능**: 9B 파라미터 수준의 sLM을 사용하여 Spider 벤치마크에서 **87.1%의 실행 정확도** 달성.
*   **아키텍처**: 'Schema Agent'(데이터 구조 분석)와 'Planner Agent'(쿼리 계획 수립)를 분리하여 단일 모델의 인지 부하를 줄임으로써 소형 모델의 한계를 극복.
*   **시사점**: AX1센터의 T2SQL v2 로드맵에서 고가의 API 대신 자체 호스팅 sLM으로의 전환 가능성을 시사함.

### 2. SLM-SQL 연구 (1.5B 이하 초소형 모델)
*   **기술**: 강화학습(RL)과 'Corrective Self-Consistency' 기법을 적용.
*   **성과**: BIRD 벤치마크에서 67% 이상의 정확도 기록. 에지 디바이스 및 보안 로컬 환경에서의 T2SQL 적용 가능성 확인.

### 3. Schema Linking의 패러다임 변화
*   **필터링에서 증강으로**: 기존의 '관련 테이블만 골라내기' 방식이 오히려 정보 누락을 초래한다는 분석에 따라, 전체 스키마를 유지하되 비즈니스 맥락을 입히는 **'Semantic Layer'** 기반 증강 방식이 주류로 부상.
*   **Text-to-Big SQL 지표**: 데이터 규모가 커짐에 따라 발생하는 실행 비용과 지연 시간을 평가에 포함하는 새로운 벤치마크 표준 제안.

## AX1센터 R&D 인사이트
*   **sLM 최적화**: 9B 이하 모델 + 멀티 에이전트 구조는 비용 효율적인 T2SQL 서빙 전략의 핵심임.
*   **Semantic Layer 강화**: 단순 DDL 제공보다 비즈니스 로직과 SQL 패턴을 매핑하는 메타데이터 관리(MetaAdmin)의 중요성이 더욱 커짐.

## 참고 및 관련 링크
*   **Original Info**: Google Search Analysis (2026.04.05~04.07)
*   **Related Notes**:
    *   [[wiki/Agents/Text-to-SQL/000_T2SQL-MOC.md|T2SQL MOC]]
    *   [[wiki/Models/RL/RTS-Reliable-Text-to-SQL-GRPO-Alignment.md|Reliable T2SQL & GRPO]]
