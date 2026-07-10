---
title: "Semantic Layer 표준 명세 (Spec)"
tags: ["Engineering", "Data", "Semantic-Layer", "T2SQL", "Spec"]
last_updated: "2024-05-22"
---

# Semantic Layer 표준 명세

이 문서는 엔터프라이즈 데이터 분석 환경에서 LLM과 데이터베이스 간의 의미론적 가교 역할을 하는 '시맨틱 레이어'의 표준 정의 형식을 규정합니다.

## 1. 핵심 구성 요소 (Core Components)

1. **Tables (물리 계층)**: 데이터 원천 정의, Join 관계, 유의어(Synonyms) 포함.
2. **Metrics (비즈니스 계층)**: 계산 로직(Expression), 필터 가드레일, 비즈니스 설명.
3. **Verified Queries (검증 계층)**: 자연어 질문과 검증된 SQL 쌍(Golden Queries).
4. **Role (거버넌스 계층)**: 권한 기반 데이터 접근 및 필터링 규칙.

## 2. 표준 YAML 포맷 예시

```yaml
table:
  name: orders
  description: "고객 주문 트랜잭션 팩트 테이블"
  synonyms: ["주문", "거래", "매출내역"]

# 메트릭 참조 (Cross-table metrics)
metric_refs:
  - sales.revenue

columns:
  - name: order_id
    description: "주문 고유 식별자"
    is_primary_key: true
  - name: amount
    description: "순매출액(USD), 세전, 할인 적용 후"
    synonyms: ["금액", "매출"]
  - name: status
    description: "주문 처리 상태"
    sample_values: ["pending", "shipped", "delivered", "cancelled", "refunded"]

metrics:
  - name: revenue
    description: "순매출 합계 (취소/환불 제외)"
    expression: "SUM(amount)"
    filters:
      - "status NOT IN ('cancelled', 'refunded')"
    synonyms: ["매출", "수익", "매출액"]

business_rules:
  - name: exclude_test_accounts
    description: "테스트 계정 제외"
    condition: "customer_id >= 100"
    apply_always: true

verified_queries:
  - question: "월별 매출 추이"
    sql: |
      SELECT DATE_TRUNC('month', order_date) AS month,
             SUM(amount) AS revenue
      FROM orders
      WHERE status NOT IN ('cancelled', 'refunded')
      GROUP BY 1
      ORDER BY 1
```

## 3. 구현 가이드라인

- **기계 가독성**: 모든 명세는 LLM이 즉시 프롬프트로 활용할 수 있도록 정형화된 포맷을 유지해야 합니다.
- **유의어 확충**: 현업 분석가가 자주 사용하는 용어를 `synonyms`에 적극적으로 반영하여 정확도를 높입니다.
- **항상 적용 규칙**: `business_rules`의 `apply_always` 옵션을 활용하여 보안 및 테스트 데이터 필터링을 강제합니다.

## 🔗 관련 문서
- [[wiki/Engineering/Local-Repo-Intelligence]]
- [[wiki/Agents/Text-to-SQL/Semantic-Layer]]
