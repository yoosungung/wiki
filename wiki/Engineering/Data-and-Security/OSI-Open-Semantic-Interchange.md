---
title: "OSI (Open Semantic Interchange)"
tags: ["OSI", "Apache Ossie", "Semantic Layer", "Agent", "MCP", "Data"]
last_updated: "2026-09-21"
updated: "2026-09-21"
related_raw: ["[[raw/2026-09-21-apache-ossie-pr423-datetimetz-converter-typo.md]]", "[[raw/2026-09-20-apache-ossie-pr350-ai-context-spec-align.md]]", "[[2026-08-23-apache-ossie-ai-context-spec141.md]]", "[[raw/2026-07-24-apache-ossie-schema-ontology-flatten.md]]", "[[raw/2026-07-14-Apache-Ossie-명세.md]]"]
---

# OSI (Open Semantic Interchange)

## 1. 개요
**OSI(Open Semantic Interchange)**는 데이터 플랫폼, BI 도구, AI 에이전트 간에 **시맨틱 모델(Semantic Model)** 정의를 교환하기 위한 벤더 중립적 오픈 소스 프로젝트이며, 현재 이름은 **Apache Ossie**입니다.

최신 안정 릴리스는 **0.1.1(2025-12-11)**입니다. 저장소 `main`의 **0.2.0.dev0**은 0.2.0 이전의 변경 가능한 초안이므로 프로덕션 호환성을 보장하지 않습니다. 기존 문서에 있던 “v1.0 공식 발표” 주장은 공식 명세의 버전 이력과 일치하지 않습니다.

## 2. 핵심 목표
*   **상호운용성**: 플랫폼에 구애받지 않고 지표(Metric) 정의를 공유. 에이전트가 도구와 팀 간에 일관된 문맥을 공유할 수 있도록 함.
*   **SSoT(Single Source of Truth)**: 전사 비즈니스 로직의 통일된 관리.
*   **AI 에이전트 최적화**: `ai_context` 메타데이터 필드를 통해 LLM이 데이터 구조와 비즈니스 규칙을 정확히 이해하도록 지원하여 가치 창출 시간(Time to Value)을 수개월에서 수분 단위로 단축.

## 3. 상세 기술 명세: `ai_context` 구현 패턴
Ossie 명세는 YAML/JSON 기반이며, `ai_context` 필드로 LLM에 자연어 가이드를 제공합니다. 이 필드는 모델, 데이터셋, 필드, 관계, 메트릭 수준에서 문자열 또는 구조화 객체로 사용할 수 있습니다.

### 구현 레벨 (Implementation Levels)
1.  **모델 레벨 (Model Level)**:
    - **역할**: 모델 전체의 분석 범위와 AI 페르소나 정의.
    - **예시**: "소매 유통 분석 전용. 별도 요청 없으면 취소 주문 제외. 순매출(Net Revenue) 기본 사용."
2.  **데이터셋 레벨 (Dataset Level)**:
    - **역할**: 특정 테이블/뷰의 데이터 성격 및 조인 주의사항 전달.
    - **예시**: "snowflake.analytics.orders 참조. 'COMPLETED' 상태만 매출로 간주."
3.  **지표/차원 레벨 (Measure & Dimension Level)**:
    - **역할**: 용어 혼선 방지 및 동의어 정의.
    - **예시**: "VIP = 연간 10회 이상 구매자", "실적 = [매출, 성과, Performance]"

기술적인 세부 스키마는 [[wiki/Engineering/Data-and-Security/OSI-Specification-v0.0.1.md|Ossie 코어 메타데이터 명세]]를 참조하십시오.

### 버전 고정과 검증
- 프로덕션 모델은 안정판 0.1.1 스키마에 고정합니다.
- `core-spec/osi-schema.json`, `core-spec/spec.yaml`, `validation/validate.py`로 커밋 전 검증합니다.
- 0.2.0.dev0 시험 모델은 안정 모델과 분리하고, 변환 전후 `ai_context`와 관계 정의의 손실을 검사합니다.

### 2026-07-24: 예시↔스키마 정합 · Ontology flatten
- **[PR #209](https://github.com/apache/ossie/pull/209)**: core-spec 예시가 `osi-schema.json`/`validate.py`를 통과하도록 수정(`datasets` minItems, `expression.dialects`, top-level `version: 0.2.0.dev0`, flat `primary_key`).
- **[PR #257](https://github.com/apache/ossie/pull/257)**: ontology `concept`를 nested object가 아닌 **문자열 필드**로 flatten. exporter/컨버터는 새 문법을 따라야 한다.

```yaml
ontology:
  - concept: Employee
    type: EntityType
    extends: [Person]
```

AV-SQL/에이전트 파이프라인 연계는 [[wiki/Agents/Text-to-SQL/AV-SQL-Agentic-Views-Spider-2-0.md]].

### 2026-08-23 → 2026-09-09: `ai_context` 스펙 정합 (#141/#340 → PR #350)

- **배경 ([#141](https://github.com/apache/ossie/issues/141))**: `spec.yaml`이 `ai_context: string`만 적어 JSON 스키마·TPC-DS 예시(string|object)와 어긋남. Relationship에는 필드 자체가 없음([#340](https://github.com/apache/ossie/issues/340)).
- **해결 ([PR #350](https://github.com/apache/ossie/pull/350), merged 2026-09-09)**: 다섯 노드(semantic_model·datasets·relationships·fields·metrics)를 `ai_context: {} # see AIContext in ossie-schema.json` + string|object 주석으로 정렬. **규범 동작 변경 없음**(스키마·Python·예시는 이미 union). 버전 **0.2.0.dev0** 유지.
- **구현 함정 해소**: `spec.yaml`만 보고 string-only 파서를 짜던 경로가 문서상으로도 막힘. 검증은 여전히 `osi-schema.json` + `validation/validate.py`.
- **Kyvos** 가 2026-08-12 Apache Ossie 생태계에 합류([ossie.apache.org](https://ossie.apache.org/)).

### 2026-09-19: 컨버터 enum 오타 → 시간 차원 역할 유실 ([PR #423](https://github.com/apache/ossie/pull/423))

- **함정**: Ossie→Omni가 `datatype`을 `"DateTimez"`(존재하지 않는 문자열)와 비교해 `DateTimeTz` 필드의 자동 `is_time` 감지가 실패. 명시 `dimension.is_time`이 없으면 Omni `timeframes`가 비고 round-trip에서 시간 역할이 사라짐.
- **정본**: 스키마 enum은 `DateTimeTz`. 컨버터·테스트는 **스펙 enum 문자열을 그대로** 쓰고, typo fixture로 회귀한다.
- **적용 팁**: 시맨틱 컨버터에서 “스펙에 없는 enum 리터럴”은 silent drop이다. NL2SQL/에이전트 파이프라인은 시간 필터 CTE 전에 `datatype`↔`is_time` round-trip 검사를 넣는다 — [[wiki/Agents/Text-to-SQL/AV-SQL-Agentic-Views-Spider-2-0.md]].

### dbt 컨버터: SUM_BOOLEAN + qualified columns (2026-07-31)

`SUM_BOOLEAN` 메트릭이 `schema.table.col`처럼 **qualified column**을 참조할 때, 렌더된 `CASE`를 split 하면 dataset 해석이 깨진다. [#292](https://github.com/apache/ossie/pull/292)는 파싱된 SQL expression에서 qualifier를 읽고 multipart dataset qualifier를 보존한다. 회귀: `converters/dbt` pytest 99 passed.

```bash
cd converters/dbt && uv run pytest
```

## 4. 에이전트 문맥 공유 (Agentic Enterprise)
Ossie는 에이전트가 사용할 시맨틱 계층의 교환 형식을 지향합니다. 다만 0.x 단계이므로 지원 변환기와 플랫폼별 구현 범위를 확인해야 합니다.

### ThoughtSpot-Snowflake 네이티브 통합 (2026)
*   **Metadata Sync**: Snowflake Semantic Views에 정의된 OSI 메타데이터가 ThoughtSpot Analyst Studio로 자동 동기화됩니다.
*   **Agentic Execution**: 사용자의 질문(Spotter)을 해석할 때 OSI의 `ai_context`를 참조하여 Snowflake Cortex Agent가 최적의 SQL을 생성합니다.

### MCP (Model Context Protocol) 연동
*   Ossie 형식으로 정의된 시맨틱 컨텍스트를 MCP 서버의 리소스나 도구 응답으로 여러 에이전트에게 전달할 수 있습니다.
*   **Protocol vs Semantic**: MCP가 에이전트와 도구 사이의 통신 통로(Protocol) 역할을 한다면, **OSI는 그 통로를 통해 전달되는 정보의 '의미'와 '문맥'을 규격화**합니다.
*   이를 통해 에이전트 간 답변의 일관성을 유지하고 복잡한 다중 도메인 협업 시나리오를 지원합니다.

## 관련 문서
*   [[wiki/Agents/Text-to-SQL/Agentic-Semantic-Layer.md]]
*   [[wiki/Agents/Text-to-SQL/AV-SQL-Agentic-Views-Spider-2-0.md]]
*   [[wiki/Agents/Text-to-SQL/2026-04-22-T2SQL-Trends-Update.md]]
*   [[wiki/Agents/Frameworks/MCP/000_MCP-MOC.md]]
