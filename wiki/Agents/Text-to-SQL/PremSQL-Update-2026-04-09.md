---
title: "PremSQL-Update-2026-04-09"
related_raw: ["[[wiki/Agents/Text-to-SQL/PremSQL-Update-2026-04-09.md]]"]
tags: ['wiki', 'agents_and_systems', 'text-to-sql_(t2sql)_&_analytics', 'slm_for_text-to-sql_and_schema_linking']
type: "wiki"
status: "published"
last_updated: "2026-04-19"
---

# PremSQL 및 sLM 기반 Text-to-SQL 최신 동향 (2026-04-09)

## 요약
최근 1.5B 규모의 초소형 언어 모델(sLM)이 BIRD 벤치마크에서 67.08%의 실행 정확도를 기록하며, 대형 모델 대비 추론 속도는 대폭 향상시키면서도 정확도 손실을 최소화하는 성과를 거두었습니다. 특히 **SLM-SQL** 프레임워크와 **Corrective Self-Consistency (CSC-SQL)** 기법이 sLM의 한계를 극복하는 핵심 아키텍처로 자리 잡고 있습니다.

## 주요 내용
- **sLM의 도약:** 0.5B~1.5B 규모의 모델이 SFT 및 RL 사후 학습을 통해 논리적 추론 능력을 극대화하고 있습니다.
- **PremSQL Agents:** sLM만으로 구동되는 데이터 분석 에이전트 기능이 강화되어, SQL 변환부터 결과 분석 및 차트 생성까지의 워크플로우를 통합했습니다.
- **Semantic Layer의 역할:** 실제 기업 환경(Spider 2.0 등)에서의 정확도 급락을 방지하기 위해, 비즈니스 용어를 SQL 패턴으로 매핑하는 시맨틱 레이어 구축이 필수 과제로 부상했습니다.

## 원문 URL
- [PremSQL GitHub](https://github.com/premai-io/premsql)

## 관련 노트
- [[wiki/Agents/Text-to-SQL/sLM-Text-to-SQL-MATS-Schema-Linking-2026]]
- [[wiki/Agents/Text-to-SQL/SLM-SQL-IJCNLP-2026]]
- [[wiki/Agents/Text-to-SQL/Spider-2.0-Benchmark-엔터프라이즈-SQL-워크플로우-평가]]
