---
title: "2026-04-09-sLM-T2SQL-Trends"
related_raw: ["[[wiki/Agents/Text-to-SQL/2026-04-09-sLM-T2SQL-Trends.md]]"]
tags: ['wiki', 'agents_and_systems', 'text-to-sql_(t2sql)_&_analytics', 'slm_for_text-to-sql_and_schema_linking']
type: "wiki"
status: "published"
last_updated: "2026-04-19"
updated: "2026-04-19"
---

# sLM 기반 Text-to-SQL 및 스키마 링킹 최신 동향 (2026-04-09)

## 요약
2026년 4월 기준, Text-to-SQL 분야는 단일 거대 모델(LLM) 중심에서 효율적인 소형 언어 모델(sLM)과 에이전틱 워크플로우의 조합으로 패러다임이 전환되었습니다. 특히 스키마 링킹(Schema Linking)을 전담하는 전문 sLM의 도입이 성능 향상의 핵심입니다.

## 주요 내용

### 1. HYVE (Hybrid Views) 프레임워크 (2026.04.07)
- **개념:** LLM의 컨텍스트 창 제한을 극복하기 위해 테이블의 전체 스키마 대신 필요한 컬럼과 로우만 노출하는 '하이브리드 뷰' 방식입니다.
- **효과:** 원시 데이터를 메모리 내 데이터스토어로 구축하고 전처리기가 이를 최적화하여 sLM이 처리해야 할 정보량을 획기적으로 줄입니다.

### 2. MATS (Multi-Agent Text-to-SQL System)
- **성능:** 9B 파라미터 모델만으로 Spider 벤치마크에서 87.1%의 실행 정확도를 달성(GPT-4급).
- **구조:** **Schema Agent**를 분리하여 SQL 생성이 아닌 "관련 테이블/컬럼 식별"이라는 분류 작업에만 집중하게 함으로써 전체 파이프라인의 정확도를 높였습니다.

### 3. sLM 기반 스키마 링킹 전략
- **추출적(Extractive) 방식:** 생성형 방식보다 정확도가 높으며, Decoder-only sLM을 SFT(Supervised Fine-Tuning)하여 관련 요소를 직접 추출합니다.
- **SQL-to-Schema 역발상:** 초안 SQL 생성 -> 사용된 스키마 추출 -> 정제된 스키마로 최종 SQL 생성의 2단계 방식이 sLM에서 매우 효과적입니다.

## AX1센터 R&D 시사점
- 현재 개발 중인 **metaadmin** 및 **evaluation pipeline**에 HYVE와 같은 컨텍스트 최적화 기술을 적용할 필요가 있습니다.
- Schema Linking 전용 sLM(분류 특화)과 SQL 생성 전용 sLM(추론 특화)을 분리하는 에이전틱 워크플로우 도입이 필수적입니다.

## 원문 URL 및 참고문헌
- [1] arxiv.org (HYVE - 2026.04.07)
- [2] medium.com (MATS System Deep Dive)

## 관련 노트
- [[Projects/t2sql/agent 자동 개선]]
- [[wiki/Agents/Text-to-SQL/000_T2SQL-MOC]]
