---
title: "DeepAgent Filesystem 기반 T2SQL 세만틱 레이어 구축 가이드"
related_raw: ["[[raw/2026-04-18-Semantic-Layer-and-DeepAgent-T2SQL]]", "[[raw/2026-04-19-T2SQL-Semantic-Layer-Metadata-RAG-Trend]]"]
tags: ["wiki", "T2SQL", "Semantic-Layer", "DeepAgent", "Architecture"]
type: "wiki"
status: "published"
last_updated: "2026-04-19"
---

# DeepAgent Filesystem 기반 세만틱 레이어 (Filesystem-as-Semantic-Layer)

전통적인 데이터베이스 중심의 메타데이터 관리 대신, 에이전트가 직접 탐색하고 읽을 수 있는 **구조화된 파일 시스템**을 세만틱 레이어로 활용하는 방안입니다. 이는 에이전트의 컨텍스트 윈도우 활용을 최적화하고 지식 관리의 유연성을 극대화합니다.

## 📂 디렉토리 구조 및 역할

DeepAgent가 접근 가능한 전용 디렉토리(`semantic_layer/`)를 정의하고, 각 지식의 유형별로 파티셔닝합니다.

```text
semantic_layer/
├── domains/                # 도메인별 비즈니스 컨텍스트 (예: sales, finance)
│   └── sales.yaml          # 판매 도메인 용어 정의 및 주요 KPI 설명
├── entities/               # 물리적 테이블과 매핑되는 논리적 엔티티
│   ├── orders.json         # 주문 테이블의 컬럼 설명, 타입, 제약조건
│   └── customers.json
├── metrics/                # 계산 로직 (SQL Snippets)
│   ├── revenue.sql         # "매출" 계산 공식 (SUM(price * quantity))
│   └── churn_rate.sql      # "이탈률" 계산 로직
├── relationships/          # 엔티티 간의 관계 (Graph Info)
│   └── er_diagram.yaml     # PK-FK 관계 및 Join 경로 가이드
└── rules/                  # SQL 작성 가이드라인
    └── formatting.md       # SQL 스타일, Alias 규칙, 방언(Dialect) 특이사항
```

## 🛠 주요 구현 구성 요소

### 1. 엔티티 정의 (Schema-as-Code)
에이전트가 `read_file`을 통해 즉시 이해할 수 있도록 JSON/YAML 포맷으로 작성합니다.
```json
{
  "entity": "orders",
  "physical_name": "FACT_SALES_ORDERS",
  "description": "고객의 최종 주문 정보가 저장되는 팩트 테이블",
  "columns": [
    {
      "name": "order_id",
      "description": "주문 고유 식별자 (PK)",
      "is_key": true
    },
    {
      "name": "total_amt",
      "description": "할인이 적용된 최종 결제 금액",
      "calculation_hint": "price * qty - discount"
    }
  ]
}
```

### 2. 메트릭 캡슐화 (SQL Snippets)
복잡한 비즈니스 로직을 SQL 조각으로 파일화하여 에이전트가 이를 참조하여 조합하게 합니다.
- **파일명**: `metrics/monthly_active_users.sql`
- **내용**: `COUNT(DISTINCT user_id) FILTER (WHERE last_login >= current_date - interval '30 days')`

### 3. 지능형 스키마 프루닝 (Filesystem-as-Metadata-RAG)
수천 개의 파일 중 질문에 필요한 파일만 선택하는 프로세스로, [[wiki/Agents/Text-to-SQL/Metadata-RAG|Metadata RAG]] 기술의 핵심입니다.
1. **Keyword/Semantic Search**: 질문(예: "지난달 매출 얼마야?")과 관련성이 높은 `metrics/revenue.sql`, `entities/orders.json` 식별.
2. **Deterministic Pruning**: 식별된 테이블의 ERD 정보를 참조하여 Join 경로상에 있는 필수 파일(`entities/customers.json` 등)을 규칙 기반으로 자동 포함.
3. **Context Assembly**: 선택된 파일의 내용만 에이전트의 프롬프트에 동적으로 삽입하여 컨텍스트 최적화.

## 🔄 에이전트 워크플로우

1. **지식 탐색 (Explore)**: 사용자의 질문을 분석하고 `semantic_layer/` 내의 관련 디렉토리를 탐색(ls)하고 필요한 파일을 읽음(read).
2. **논리적 조립 (Compose)**: 읽어온 메트릭 정의와 엔티티 정보를 결합하여 논리적 쿼리 계획 수립.
3. **물리적 변환 (Generate)**: `rules/`의 가이드라인에 맞춰 타겟 DB(PostgreSQL, BigQuery 등)에 최적화된 SQL 생성.
4. **검증 및 피드백 (Validate)**: 생성된 SQL이 세만틱 레이어의 정의와 일치하는지 재검토.

## 🌟 기대 효과
- **추적 가능성 (Traceability)**: 모든 세만틱 정의가 파일로 관리되므로 Git을 통한 버전 관리 및 변경 이력 추적이 용이함.
- **에이전트 친화성**: 데이터베이스 카탈로그 조회보다 텍스트 기반 파일 읽기가 에이전트의 추론 속도와 정확도 면에서 유리함.
- **확장성**: 새로운 도메인이나 메트릭 추가 시 DB 스키마 변경 없이 파일 추가만으로 대응 가능.

## 🔗 관련 문서
- [[wiki/Agents/Text-to-SQL/Metadata-RAG]]
- [[wiki/Agents/Text-to-SQL/DeepAgent-T2SQL]]
- [[wiki/Agents/Frameworks/MCP/Filesystem-Server]]
