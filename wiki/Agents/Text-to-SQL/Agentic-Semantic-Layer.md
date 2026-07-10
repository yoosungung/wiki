---
title: "Agentic Semantic Layer: AI 에이전트를 위한 지능형 데이터 인터페이스"
tags: ["Architecture", "Semantic-Layer", "T2SQL", "Agentic-AI"]
type: "wiki"
status: "published"
last_updated: "2026-04-28"
related_raw: ["[[raw/2026-04-22-semantic-layer-standards-osi-mcp-research.md]]", "[[raw/2026-04-26-OSI-v1-Updates.md]]", "[[raw/2026-04-28-OSI-v1-ai-context-Standard.md]]"]
---

# 에이전틱 시맨틱 레이어 (Agentic Semantic Layer)

**에이전틱 시맨틱 레이어**는 AI 에이전트가 기업 데이터의 복잡한 구조와 비즈니스 맥락을 자율적으로 이해하고 안전하게 접근할 수 있도록 돕는 지능형 거버넌스 레이어입니다. 2026년 현재, 이는 단순한 데이터 인터페이스를 넘어 AI 에이전트의 **'기초 지식(Ground Truth) 백본'**으로 진화했습니다.

## 🌟 2026년 5대 핵심 트렌드

### 1. 에이전트 백본(Backbone)으로의 전환
시맨틱 레이어는 더 이상 BI 도구의 부속물이 아닙니다. 에이전트가 원시 테이블에 직접 접근하여 발생하는 '환각(Hallucination)'을 원천 차단하고, 정의된 지표(Metrics)를 바탕으로 정확한 판단을 내리게 하는 에이전트의 **지식 기반(Knowledge Base)** 역할을 수행합니다.

### 2. OSI (Open Semantic Interchange) 표준 확산
**Snowflake, ThoughtSpot, Salesforce, dbt Labs, Looker** 등이 주도하는 **OSI 표준**의 도입으로 데이터 사일로가 해결되었습니다. 2026년 1월 27일 공식 발표된 **OSI v1.0 사양**(Apache 2.0 라이선스)은 벤더 중립적인 시맨틱 모델 표준을 제공합니다.
- **`ai_context` 필드**: AI 에이전트가 데이터 구조와 비즈니스 맥락을 더 잘 이해할 수 있도록 돕는 설명적 메타데이터를 표준화했습니다.
    - **`instructions`**: 에이전트를 위한 자연어 실행 가이드.
    - **`synonyms`**: 사용자가 질문 시 사용할 수 있는 다양한 유의어 매핑.
    - **`examples`**: 질문-쿼리 쌍(Few-shot)을 통한 추론 가이드.
- **구조**: Semantic Model (Container) > Datasets > Metrics/Dimensions > Relationships 순의 계층적 구조를 가집니다.

#### `ai_context` YAML 예시
```yaml
semantic_model:
  name: sales_performance
  ai_context:
    instructions: "이 모델은 경영진 보고용입니다. 별도 지시가 없으면 'is_active=true' 필터를 항상 적용하세요."
  datasets:
    - name: orders
      ai_context:
        synonyms: ["transactions", "bookings", "판매건수"]
      fields:
        - name: order_total
          ai_context:
            instructions: "세금이 포함된 금액이며 배송비는 제외된 수치입니다."
```

- **효과**: 에이전트는 도구와 플랫폼에 구애받지 않고 시맨틱 컨텍스트를 공유하며 협업할 수 있는 '상호운용성'을 확보하게 되었습니다. (GitHub: `open-semantic-interchange/OSI`)

### 3. 자율형 시맨틱 레이어 생성 (Autonomous Generation)
에이전트가 원시 스키마와 과거 질의 패턴을 분석하여 스스로 시맨틱 모델을 구축하는 **'자율형 데이터 엔지니어링'**이 일반화되었습니다. 에이전트는 새로운 지표를 제안하고, 인간의 승인을 거쳐 Git에 자동으로 PR(Pull Request)을 생성합니다.

### 4. MCP (Model Context Protocol) 기반 연결 표준화
Anthropic이 발표하고 Google, Microsoft, OpenAI가 참여하는 **MCP**가 AI 에이전트와 데이터 소스(DB, API, 시맨틱 레이어) 간의 연결을 표준화하는 "AI용 USB"로 완전히 정착되었습니다. dbt, Cube 등 기존 시맨틱 레이어들이 MCP 서버를 제공함으로써 에이전트가 표준화된 방식으로 메트릭을 조회하고 쿼리를 실행합니다.

### 5. 차세대 진화: Agentic Semantic Layer (Methodology-centric)
단순한 메트릭 정의를 넘어 **분석 방법론(Methodology)**까지 포함하는 개념으로 진화하고 있습니다.
- **분석 플레이북:** 에이전트가 '리텐션 분석'이나 '퍼널 분석'을 수행할 때 따라야 할 단계별 로직과 제약 조건을 시맨틱 레이어에 내장합니다.
- **스트리밍 시맨틱:** 데이터 스키마나 비즈니스 로직이 변경될 때 실시간으로 에이전트의 컨텍스트를 업데이트하여 과거 로직 기반의 오판을 방지합니다.
- **조사 및 추론 가이드:** 특정 수치의 이상 현상 발견 시, 어떤 차원으로 드릴다운(Drill-down)하여 원인을 분석해야 하는지에 대한 지침을 제공합니다.

## 🤝 교차 도메인 컨텍스트 공유 메커니즘
에이전트가 여러 도메인(예: 마케팅, 재무, 인프라)의 데이터를 통합 분석하기 위해 시맨틱 레이어가 제공하는 핵심 기능입니다.

1. **온톨로지 기반 관계 및 ID 레이어:** 서로 다른 시스템(CRM, ERP 등)의 식별자를 매핑하고, 엔티티 간의 관계(예: '고객'은 '주문'을 가진다)를 기계가 읽을 수 있는 형태로 정의합니다.
2. **메타데이터 강화:** 데이터의 생성 배경, 비즈니스 규칙, 사용 시 주의사항 등 풍부한 컨텍스트를 포함하여 에이전트의 판단을 돕습니다.
3. **연합 시맨틱 레이어 (Federated Semantic Layer):** 데이터가 여러 클라우드나 DB에 분산되어 있어도, 에이전트에게는 하나의 통합된 시맨틱 인터페이스로 보이게 합니다.

## 🛠 핵심 구성 요소 및 전략

### 1. 결정론적 생성 (Deterministic Generation)
- **Probabilistic vs. Deterministic**: LLM이 확률적으로 SQL을 직접 생성하는 대신, 사전에 정의된 메트릭과 차원을 선택하게 합니다.
- **검증된 쿼리 엔진**: 시맨틱 엔진(dbt MetricFlow, Cube, ThoughtSpot 등)이 최적화된 SQL을 직접 생성하여 조인 오류나 집계 실수를 원천 차단함으로써 **정확도를 100% 가깝게** 유지합니다.

### 2. 비즈니스 컨텍스트 주입 및 캡슐화
- **Context Gap 해소**: 기업 고유의 비즈니스 로직(예: '활성 사용자'의 기준, 회계 연도 설정 등)을 AI가 이해할 수 있도록 가이드합니다.
- **로직의 캡슐화**: 복잡한 계산식을 SQL 생성 시점에 LLM이 계산하게 하지 않고, 시맨틱 레이어에 미리 정의된 로직을 호출함으로써 전사적 지표의 일관성을 보장합니다.

### 3. 지능형 스키마 프루닝 (Schema Pruning)
- **Hierarchical Discovery**: 수천 개의 테이블 중 질문과 관련된 테이블/컬럼 정의 및 비즈니스 용어집만 동적으로 선별하여 컨텍스트 윈도우를 최적화합니다.
- **메타데이터 RAG**: 지식 그래프를 활용하여 질문의 의도와 가장 유사한 데이터 소스를 탐색합니다.

### 4. 보안 및 거버넌스
- **Control Point**: 시맨틱 레이어가 에이전트의 데이터 접근 제어 지점 역할을 수행합니다.
- **Row/Column Level Security**: 사용자의 권한에 따라 보여줄 수 있는 데이터 범위를 자동으로 제어하여 안전한 분석 환경을 제공합니다.

## 📂 구현 패턴

### Filesystem-as-Semantic-Layer (DeepAgent)
에이전트가 직접 탐색하고 읽을 수 있는 **구조화된 파일 시스템**(JSON/YAML)을 시맨틱 레이어로 활용하는 방식입니다.
- **장점**: 에이전트 친화적이며 Git을 통한 버전 관리 및 변경 이력 추적이 용이합니다.
- **구조**: `domains/`, `entities/`, `metrics/`, `rules/` 등의 디렉토리로 구성됩니다.

## 🚀 주요 기술 및 도구
- **ThoughtSpot Spotter Semantics**: 업계 최초의 상용 에이전틱 시맨틱 레이어.
- **dbt MetricFlow**: 코드 기반의 메트릭 정의 및 의미론적 쿼리 엔진.
- **Snowflake Cortex Analyst**: Snowflake 에코시스템 내 지능형 시맨틱 인터페이스.
- **MCP (Model Context Protocol)**: 시맨틱 레이어와 다양한 AI 에이전트를 연결하는 표준 프로토콜.

## 🔗 관련 문서
- [[wiki/Agents/Text-to-SQL/ThoughtSpot-Spotter-Semantics]]
- [[wiki/Agents/Text-to-SQL/T2SQL-Benchmarks-2026]]
- [[wiki/Agents/Text-to-SQL/Metadata-RAG]]
- [[wiki/Agents/Text-to-SQL/Semantic-Layer-DeepAgent-Filesystem]]
