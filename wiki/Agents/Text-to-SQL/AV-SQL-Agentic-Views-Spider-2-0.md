---
title: "AV-SQL: Agentic Views를 통한 Text-to-SQL 혁신 및 시맨틱 레이어 통합"
related_raw: ["[[2026-07-29-apache-ossie-java21.md]]", "[[2026-07-28-apache-ossie-ai-disclosures-polaris-java17.md]]", "[[2026-07-24-apache-ossie-schema-ontology-flatten.md]]", "[[2026-07-23-apache-ossie-plugin-invocation.md]]", "[[2026-07-22-apache-ossie-wisdomai-converter-plugins.md]]", "[[2026-07-20-apache-ossie-databricks-snowflake-merged.md]]", "[[raw/2026-07-14-AV-SQL-논문-및-구현.md]]", "[[wiki/Agents/Text-to-SQL/2026-04-20-T2SQL-Trends-Update.md]]", "[[2026-07-16-av-sql-osi-mcp-integration-research.md]]", "[[2026-07-16-av_sql_semantic_layer_text_to_sql_research.md]]", "[[2026-07-17-apache-ossie-cli-scaffold.md]]", "[[2026-07-18-apache-ossie-duckdb-semantido-converters.md]]", "[[2026-07-19-apache-ossie-snowflake-quoted-identifiers.md]]"]
tags: ["wiki", "Agents", "Text-to-SQL", "OSI", "MCP", "Snowflake", "slm_for_text-to-sql_and_schema_linking"]
type: "wiki"
status: "published"
last_updated: "2026-07-29"
updated: "2026-07-29"
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

## Apache Ossie 컨버터 확장 (2026-07-18, OPEN PR)

CLI scaffold(#151) 이후 **허브-스포크 컨버터** 쪽으로 기여가 이어지고 있습니다. 아래는 2026-07-18 기준 **미병합(OPEN)** 이지만 AV-SQL/`ai_context` 파이프라인 설계에 바로 참고할 수 있는 표면입니다.

### DuckDB 양방향 컨버터 — [PR #229](https://github.com/apache/ossie/pull/229)

1. **Dialect**: `DUCKDB`를 `osi-schema.json` / `spec.yaml` / Python `OSIDialect`에 등록하고, `validation/validate.py`에서 sqlglot `duckdb`로 매핑.
2. **Export**: Ossie → DuckDB SQL(데이터셋당 view, `COMMENT ON`, relationship 기반 metric view). `DUCKDB` 우선, 없으면 `ANSI_SQL`+경고.
3. **Import**: DuckDB/`md:`(MotherDuck) → Ossie YAML(`information_schema` + `duckdb_constraints()` → PK/UK/FK·relationship).
4. **CLI**: `ossie-duckdb export|import` + in-memory DuckDB round-trip pytest.

```bash
# 개념 예시 (PR #229 병합·플러그인 등록 후)
ossie-duckdb export --input ./model.ossie.yaml -o ./duckdb_views.sql
ossie-duckdb import --connection "md:my_db" -o ./imported.ossie.yaml
```

### semantido ↔ Ossie — [PR #230](https://github.com/apache/ossie/pull/230)

- **Forward**: SQLAlchemy `@semantic_table` 모듈 import → semantido sync → typed `apache-ossie` 객체로 YAML emit.
- **Reverse**: Ossie 문서 → `@semantic_table` 장식 Python 모듈 코드 생성.
- 파일↔파일 변환기와 달리 **실행 중 Python 모델이 SoT**.

**AV-SQL 적용**: MotherDuck/임베디드 DuckDB에 적재된 시맨틱을 Ossie로 끌어와 View Generator의 `ai_context`에 주입하거나, 코드 네이티브 semantido 레이어를 Ossie로 정규화한 뒤 CTE 프롬프트에 넣는 경로를 모니터링한다. (병합 전이라 프로덕션 고정은 보류)

### Snowflake quoted identifiers — [PR #233](https://github.com/apache/ossie/pull/233) (2026-07-20, **MERGED**)

2026-07-19 OPEN으로 추적하던 [#233](https://github.com/apache/ossie/pull/233)이 **2026-07-20에 병합**되었습니다. Ossie → Snowflake YAML 컨버터가 따옴표 안의 점을 식별자 구분자로 오해하지 않도록 `_split_identifiers`를 제공합니다.

```python
_parse_source('"my.db"."my schema"."my table"')
# → {"database": '"my.db"', "schema": '"my schema"', "table": '"my table"'}
```

- **AV-SQL**: Snowflake MCP/시맨틱 왕복 시 quoted DB·스키마명을 CTE 테이블 링킹에 안전하게 사용 가능. 프로덕션 게이트에 `ossie` Snowflake export round-trip을 추가할 시점.

### Databricks Unity Catalog Metric View 컨버터 — [PR #224](https://github.com/apache/ossie/pull/224) (2026-07-20, **MERGED**)

Databricks 스포크가 허브-스포크 맵에 실전 진입했습니다. Unity Catalog Metric Views(YAML v1.1)와 Ossie 간 **오프라인 양방향** 변환기입니다.

```bash
# Ossie → Metric View
ossie-databricks export --input ./model.ossie.yaml -o ./metric_view.yaml
# Metric View → Ossie (DATABRICKS-only 필드는 custom_extensions에 stash → lossless)
ossie-databricks import --input ./metric_view.yaml -o ./imported.ossie.yaml
```

- **설계**: fact `source` + nested `joins` 트리, flattened `dimensions`/`measures`. Metric-View-only 기능(filter, window, format, parameters, materialization 등)은 `custom_extensions[DATABRICKS]`에 보존 → **MV → Ossie → MV lossless**.
- **AV-SQL 적용**: Databricks 카탈로그 시맨틱을 Ossie로 정규화한 뒤 View Generator `ai_context`에 주입하는 경로를 실험할 수 있다. DuckDB(#229)·semantido(#230)는 여전히 OPEN.

### WisdomAI domain converter — [PR #239](https://github.com/apache/ossie/pull/239) (2026-07-22, **MERGED**)

WisdomAI `exportDomain`/`importDomain` JSON(format `1.0`) ↔ Ossie YAML **양방향** 컨버터(`converters/wisdom`). `WISDOM` vendor/`OSIVendor` 등록, BigQuery는 `BIGQUERY` 방언(백틱 식별자).

```bash
ossie-wisdom wisdom-to-osi -i domain-export.json -o semantic_model.yaml
ossie-wisdom osi-to-wisdom -i semantic_model.yaml -o domain-export.json
```

- **Import**: `domainSystemInstructions`+knowledge → 모델급 `ai_context`; 테이블/컬럼/formula/relationship/measure → datasets·fields·relationships·metrics.
- **Export**: round-trip 안정(합성 fixture·실 Snowflake/BigQuery 도메인에서 `validation/validate.py` 통과, OSI→wisdom→OSI byte-identical YAML).
- **CLI plugins (#154)**: `plugin.yaml` 정의 + 설치 플러그인 **목록**만(설치/변환 호출은 미포함). Solid(#240) 참여 조직 추가.

**AV-SQL 적용**: WisdomAI 도메인을 Ossie로 끌어와 View Generator `ai_context`에 주입하는 경로가 Databricks(#224)·Snowflake(#233)에 이어 실전 진입. BI 시맨틱 → Ossie → agentic CTE 파이프라인을 표준화할 때 `ossie-wisdom`을 첫 스포크로 쓸 수 있다.

### CLI plugin invocation protocol — [PR #155](https://github.com/apache/ossie/pull/155) (2026-07-23, **MERGED**)

#154 목록 레이어 위에 **stdin/stdout JSON 호출 프로토콜**이 병합되었습니다 (`cli/internal/plugin/invoke.go`).

```go
// Request  → plugin stdin
// Response ← plugin stdout ({files, issues?})
Invoke(ctx, pluginDir, invoke, req, pluginStderr) (*Response, error)
```

- **Envelope**: `Request.Files` / `Response.Files` + optional `Issue{severity,message,path}`.
- **계약**: nil `Files` → `{}`로 정규화; `Issues`는 Go error가 아님(호출자가 severity로 exit 결정); timeout은 `ctx.Err()`로 판별.
- **스택**: #154 list → **#155 Invoke** → #156 registry → #158 `convert`.

**AV-SQL 적용**: `ossie convert`가 플러그인 서브프로세스를 호출할 때 View Generator 전처리에서 Wisdom/Databricks/Snowflake 스포크를 동일 envelope로 묶을 수 있다. 플러그인 `error` severity를 게이트로 쓰면 잘못된 `ai_context` YAML이 CTE 단계로 흘러가는 것을 막을 수 있다.

### Spec examples ↔ osi-schema 정합 + Ontology flatten — [#209](https://github.com/apache/ossie/pull/209) · [#257](https://github.com/apache/ossie/pull/257) (2026-07-24, **MERGED**)

1. **[#209](https://github.com/apache/ossie/pull/209)**: core-spec 예시가 `osi-schema.json`을 통과하도록 수정 — `datasets` `minItems:1`, metric `expression.dialects` 래퍼, Complete Example에 `version: 0.2.0.dev0`, `primary_key` flat string array. `validation/validate.py`로 전 예시 통과.
2. **[#257](https://github.com/apache/ossie/pull/257)**: ontology `concept`를 nested `name` 대신 **문자열 필드**로 flatten. `ontology.json`에서 별도 `Concept` def 제거, `concept`+`type` required.

```yaml
# Ontology flatten (#257)
ontology:
  - concept: Employee
    type: EntityType
    extends: [Person]
```

### AI-assisted contribution disclosures · Polaris Java 17 — [#259](https://github.com/apache/ossie/pull/259) · [#278](https://github.com/apache/ossie/pull/278) (2026-07-28, **MERGED**)

1. **[#259](https://github.com/apache/ossie/pull/259)**: CONTRIBUTING에 **AI-Assisted Contributions** — generative tooling으로 생성한 코드도 submitter 개인 책임; ASF Generative Tooling 가이드 링크.
2. **[#278](https://github.com/apache/ossie/pull/278)**: Polaris converter Java **11 → 17**. Omni pytest/CI path 정리(#263/#276).

**AV-SQL 적용**: `ai_context` 스키마 자체는 불변. 컨버터/스포크 PR은 AI disclosure 정책 준수. Polaris 카탈로그 연동 빌드는 JDK 17+ 필요.

### Polaris / converter Java 21 — [#283](https://github.com/apache/ossie/pull/283) (2026-07-29)

- **[#283](https://github.com/apache/ossie/pull/283)**: Java **17 → 21** 상향 (전일 #278의 11→17에 이은 후속).
- Docs typo만 (#284).

**AV-SQL 적용**: Polaris converter CI/로컬 빌드는 **JDK 21**을 기준으로 맞춘다. 시맨틱 YAML·`ai_context` 계약은 불변.


**AV-SQL 적용**: View Generator가 Ossie YAML을 생성·검증할 때 문서 예시를 그대로 복사하면 스키마 실패하던 함정이 제거된다. 온톨로지 스포크를 `ai_context`에 주입할 때는 flatten 문법으로 맞춘 뒤 `validate.py`를 CI 게이트로 둔다. 상세는 [[wiki/Engineering/Data-and-Security/OSI-Open-Semantic-Interchange.md]].

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
- [Apache Ossie DuckDB converter PR #229](https://github.com/apache/ossie/pull/229) (OPEN)
- [Apache Ossie semantido converter PR #230](https://github.com/apache/ossie/pull/230) (OPEN)
- [Apache Ossie Snowflake quoted identifiers PR #233](https://github.com/apache/ossie/pull/233) (MERGED)
- [Apache Ossie Databricks Unity Catalog Metric View converter PR #224](https://github.com/apache/ossie/pull/224) (MERGED)
- [Apache Ossie WisdomAI domain converter PR #239](https://github.com/apache/ossie/pull/239) (MERGED)
- [Apache Ossie CLI plugin objects PR #154](https://github.com/apache/ossie/pull/154) (MERGED)
- [Apache Ossie (incubating)](https://ossie.apache.org/)
- Snowflake Managed MCP Server documentation

## 관련 노트 (Related Notes)
- [[wiki/Agents/Text-to-SQL/000_Text-to-SQL-MOC.md]]
- [[wiki/Agents/Text-to-SQL/Agentic-Semantic-Layer.md]]
- [[wiki/Agents/Text-to-SQL/T2SQL-Benchmarks-2026.md]]
- [[wiki/Agents/Text-to-SQL/Spider-2.0-Benchmark-엔터프라이즈-SQL-워크플로우-평가.md]]
