---
title: "BigQuery의 AI 시대에 맞춰 재해석된 SQL"
related_raw: ["[[wiki/Models/Architectures/BigQuery의 AI 시대에 맞춰 재해석된 SQL.md]]"]
tags: ['wiki', 'ai_core', 'llm_concepts', 'llm_applications_and_insights']
type: "wiki"
status: "published"
last_updated: "2026-04-19"
---

Google은 AI 시대에 맞춰 SQL을 재해석한 BigQuery 관리형 AI 함수(AI.IF, AI.CLASSIFY, AI.SCORE)의 공개 프리뷰를 발표했습니다. 이 함수들은 데이터 분석가들이 복잡한 프롬프트 튜닝이나 새로운 도구 없이도 SQL 쿼리 내에서 직접 생성형 AI를 사용하여 text, 이미지 등 비정형 데이터에 대한 정교한 AI 기반 분석을 수행할 수 있도록 합니다.

주요 기능은 다음과 같습니다:
*   **AI.IF**: 자연어 조건을 사용하여 데이터를 필터링하거나 조인합니다. 예를 들어, 부정적인 고객 리뷰를 식별하거나 특정 속성을 가진 이미지를 필터링할 수 있습니다.
*   **AI.CLASSIFY**: 제공된 레이블을 기반으로 텍스트나 이미지를 분류합니다. 예를 들어, 뉴스 기사를 주제별로 분류할 수 있습니다.
*   **AI.SCORE**: 자연어 기준에 따라 행의 순위를 매깁니다. 예를 들어, 영화 리뷰의 긍정도를 평가하여 순위를 매길 수 있습니다.

BigQuery는 프롬프트 최적화, 쿼리 계획 최적화, 모델 엔드포인트 및 매개변수 튜닝을 통해 비용을 최소화하고 성능을 향상시킵니다. 이 새로운 함수들은 기존의 AI.GENERATE 함수를 보완하며, 비용과 품질에 최적화되어 있습니다.

## Links
- https://cloud.google.com/blog/products/data-analytics/sql-reimagined-for-the-ai-era-with-bigquery-ai-functions?hl=en
