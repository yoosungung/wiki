---
title: "AV-SQL: Agentic Views를 통한 Text-to-SQL 혁신 및 시맨틱 레이어 통합"
related_raw: ["[[raw/2026-07-14-AV-SQL-논문-및-구현.md]]", "[[wiki/Agents/Text-to-SQL/2026-04-20-T2SQL-Trends-Update.md]]", "[[2026-07-16-av-sql-osi-mcp-integration-research.md]]", "[[2026-07-16-av_sql_semantic_layer_text_to_sql_research.md]]", "[[2026-07-17-apache-ossie-cli-scaffold.md]]"]
tags: ["wiki", "Agents", "Text-to-SQL", "OSI", "MCP", "Snowflake", "slm_for_text-to-sql_and_schema_linking"]
type: "wiki"
status: "published"
last_updated: "2026-07-17"
updated: "2026-07-17"
---

# AV-SQL: Agentic Views를 통한 Text-to-SQL 혁신

## 요약 (Summary)
AV-SQL은 대규모 스키마를 한 번에 프롬프트에 넣지 않고, **Agentic Views**라는 실행 가능한 CTE 중간 표현으로 분해하는 Text-to-SQL 프레임워크입니다. 논문(arXiv:2604.07041 v1)이 보고한 Spider 2.0 실행 정확도는 70.38%이며, 이는 논문 공개 시점의 벤치마크 결과입니다.

2026년 7월 현재, AV-SQL의 CTE 기반 접근은 **OSI (Open Semantic Interchange) v1.0** 규격 및 **Snowflake Intelligence MCP** 같은 시맨틱 레이어/카탈로그 검색 경로와 결합할 때 기업 데이터 맥락을 더 안정적으로 주입할 수 있는 구조로 해석됩니다.

## 핵심 기술 아키텍처 (Core Architecture)
AV-SQL은 3단계 에이전트 파이프라인을 통해 복잡한 쿼리를 분해하고 해결합니다:

1.  **Rewriter Agent (재작성 에이전트)**: 사용자의 자연어 질문을 분석하여 모호성을 제거하고, SQL 생성에 최적화된 형태로 명확하게 재구성합니다.
2.  **View Generator Agent (뷰 생성 에이전트)**: 전체 스키마를 테이블 중심 청크로 처리하며, 질문 해결에 필요한 테이블과 컬럼만 필터링한 **Agentic Views (CTE, Common Table Expressions)**를 생성합니다. 각 CTE는 값 검색, DB 실행, 오류 수정, JSON 스키마 선택 결과와의 일관성 검사를 거치며, 컨텍스트 윈도우 한계와 스키마 링킹 오류를 줄이는 역할을 합니다.
3.  **Planner, Generator, & Revisor Agents**:
    *   **Planner**: 생성된 뷰들을 어떻게 조합할지 실행 계획을 세웁니다.
    *   **Generator**: 계획에 따라 최종 SQL을 합성합니다.
    *   **Revisor**: SQL을 실제 DB에서 실행하고, 오류 발생 시 피드백을 통해 쿼리를 수정(Self-Correction)합니다.

## 공식 구현과 재현 경로
- **Rewriter**: `av_sql/question.py`
- **View generator**: `av_sql/cte_agent.py`
- **Planner / SQL generator / Revisor**: `av_sql/sql_agent.py`
- **검증 순서**: 스키마 인덱싱 → 질문 재작성 → 청크별 CTE 생성·실행 보정 → CTE 집계 → 최종 SQL 생성·재검토

프로덕션 적용 시에는 CTE와 최종 SQL을 읽기 전용 계정, 쿼리 시간 제한, 허용 스키마 목록 안에서 실행해야 합니다. 논문의 정확도는 지정 벤치마크에서 측정된 값이므로 실제 기업 스키마에는 별도 회귀 평가가 필요합니다.

## OSI v1.0 (Apache Ossie) 및 Snowflake MCP 통합 (2026-07-16 업데이트)
대규모 엔터프라이즈 환경에서는 AV-SQL의 Agentic Views 생성 단계에 시맨틱 거버넌스 정보를 함께 주입하는 방식이 유용합니다.

1. **OSI v1.0 (Apache Ossie) `ai_context` 기반 CTE 가이드**:
   - **Open Semantic Interchange (OSI)** 규격은 Apache Ossie 프로젝트와 함께 시맨틱 메타데이터 교환의 표준 사양으로 정리되고 있습니다.
   - 모델 정의 내 핵심 필드인 `ai_context`의 자연어 지침(`instructions`), 유의어 매핑(`synonyms`), Few-shot 질의-쿼리 쌍(`examples`)을 **View Generator Agent**의 프롬프트 컨텍스트에 직접 주입할 수 있습니다.
   - 이를 통해 에이전트가 비즈니스 규칙(예: 순매출 계산 시 환불 금액 차감 필터링 등)을 선제적으로 반영한 CTE(Agentic Views)를 생성하도록 유도하여 스키마 링킹 및 비즈니스 로직 오류를 줄일 수 있습니다.
2. **Snowflake Intelligence MCP 연동**:
   - Snowflake의 Managed MCP Server를 경유하여 데이터 카탈로그 및 Cortex Analyst의 시맨틱 분석 결과를 실시간 검색(Recall)할 수 있습니다.
   - MCP API를 통해 자주 활용되는 검증된 SQL 패턴을 동적으로 획득하면 Revisor Agent의 자율 디버깅 및 자가 수정(Self-Correction) 루프를 보강할 수 있습니다.

## Apache Ossie CLI scaffold (2026-07-17 업데이트)

[apache/ossie#151](https://github.com/apache/ossie/pull/151)이 2026-07-17에 병합되어 Go/Cobra 기반 **`ossie` CLI** 골격이 `cli/`에 추가되었습니다. 명령 본체는 아직 stub(`not yet implemented`)이지만, AV-SQL·시맨틱 레이어 파이프라인에 붙일 플래그 표면이 확정되었습니다.

```bash
# 플랫폼 → Ossie (또는 역방향). 플러그인 발견/타임아웃/입력 크기 제한 포함
ossie convert --from dbt --input ./semantic.yaml -o ./ossie-output
ossie convert --to gooddata --input ./model.ossie.yaml

# YAML/JSON 검증 (구현 예정). --strict 시 warning→error
ossie validate --strict --output json ./models/*.yaml

# 벤더 변환 플러그인 생명주기 (list/install/remove stub)
ossie plugin list
```

- **후속 PR 스택**: #154 플러그인 객체, #155 호출 프로토콜, #156 레지스트리, #158 `convert` 구현.
- **같은 날**: semantido 벤더 등록(#207), orionbelt 컨버터 round-trip 견고화(#206).
- **AV-SQL 적용 아이디어**: View Generator 전에 `ossie validate`로 `ai_context` 스키마를 게이트하고, `ossie convert --from <bi>`로 사내 시맨틱을 Ossie로 정규화한 뒤 CTE 프롬프트에 주입한다.

## 성능 (Performance Metrics)
AV-SQL은 특히 현실 세계의 대규모 스키마 환경에서 탁월한 성능을 입증했습니다:

- **Spider 2.0 (Classic/Lite)**: **70.38%** (Execution Accuracy)
- **BIRD**: **72.16%**
- **Spider (Classic)**: **85.59%**
- **KaggleDBQA**: **63.78%**

## 기술적 시사점 및 AX1센터 적용 방안
- **기업용 DB 대응**: 수백 개의 테이블이 있는 엔터프라이즈 환경에서 'Agentic Views' 방식은 필수적입니다.
- **v2 로드맵 연계**: AX1센터의 T2SQL v2 로드맵(MetaAdmin 및 평가 파이프라인)에 이 아키텍처를 도입하여, 복잡한 비즈니스 로직이 포함된 쿼리 생성 능력을 강화할 수 있습니다. 특히 CTE 기반의 단계적 검증 방식은 'Evaluation Pipeline'의 신뢰도를 높이는 데 기여할 수 있습니다.

## 참고 자료 (References)
- [AV-SQL: Decomposing Complex Text-to-SQL Queries with Agentic Views (arXiv:2604.07041)](https://arxiv.org/abs/2604.07041)
- [GitHub Repository: pminhtam/AV-SQL](https://github.com/pminhtam/AV-SQL)
- [[wiki/Agents/Text-to-SQL/T2SQL-Benchmarks-2026.md|Spider 2.0 및 T2SQL 벤치마크]]
- [Open Semantic Interchange (OSI) Specification v1.0](https://github.com/open-semantic-interchange/OSI)
- [Apache Ossie CLI scaffold PR #151](https://github.com/apache/ossie/pull/151)
- [Apache Ossie (incubating)](https://ossie.apache.org/)
- Snowflake Managed MCP Server documentation

## 관련 노트 (Related Notes)
- [[wiki/Agents/Text-to-SQL/000_Text-to-SQL-MOC.md]]
- [[wiki/Agents/Text-to-SQL/Agentic-Semantic-Layer.md]]
- [[wiki/Agents/Text-to-SQL/T2SQL-Benchmarks-2026.md]]
- [[wiki/Agents/Text-to-SQL/Spider-2.0-Benchmark-엔터프라이즈-SQL-워크플로우-평가.md]]
