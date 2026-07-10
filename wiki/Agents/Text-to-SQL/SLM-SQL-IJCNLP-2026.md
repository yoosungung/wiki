---
title: "SLM-SQL-IJCNLP-2026"
related_raw: ["[[wiki/Agents/Text-to-SQL/SLM-SQL-IJCNLP-2026.md]]"]
tags: ['wiki', 'agents_and_systems', 'text-to-sql_(t2sql)_&_analytics', 'slm_for_text-to-sql_and_schema_linking']
type: "wiki"
status: "published"
last_updated: "2026-04-19"
---

# SLM-SQL: 초소형 모델로 구현한 고성능 Text-to-SQL

**날짜:** 2026-04-08
**출처**: [IJCNLP-AACL 2026 발표](https://aclanthology.org/2026.ijcnlp-main.123/)

## 요약
SLM-SQL은 0.5B에서 1.5B 파라미터 규모의 소형 언어 모델(sLM)을 사용하여 Text-to-SQL 성능을 극대화한 연구입니다. 대형 모델에 의존하지 않고도 높은 정확도를 달성할 수 있음을 보여주었습니다.

## 핵심 내용
- **알고리즘:** SFT(지도 미세 조정)와 GRPO(Group Relative Policy Optimization) 기반의 강화학습(RL)을 결합.
- **교정적 자기 일관성 (Corrective Self-Consistency):** 추론 단계에서 스스로 오류를 탐지하고 수정하는 메커니즘을 통해 실행 정확도를 높임.
- **성능:** 
    - 0.5B 모델: BIRD 벤치마크 EX 61.82%
    - 1.5B 모델: BIRD 벤치마크 EX 70.49%
- **의의:** 파라미터 대비 압도적인 효율성을 기록하며, 로컬 환경이나 엣지 디바이스에서의 T2SQL 적용 가능성을 증명함.

## 관련 노트
- [[sLM 기반 Text-to-SQL, 환상에서 현실로]]
- [[wiki/Agents/Text-to-SQL/BIRD-Critic-SQLite-Talon-Models]]
- [[wiki/Agents/Text-to-SQL/Text-to-SQL-Reasoning-2026]]
