---
id: luthor-sql-system1-local-gate
title: "LuthorSQL: 로컬 System 1 게이트 + 느린 LLM 에이전트 캐스케이드"
status: canonical
owner: km
updated: "2026-11-22"
last_updated: "2026-11-22"
review_after: "2027-02-22"
sources:
  - https://arxiv.org/abs/2611.17780
tags: ["Agents", "Text-to-SQL", "NL2SQL", "System1", "On-Device", "Cost"]
type: "wiki"
---

# LuthorSQL: 로컬 System 1 게이트 + 느린 LLM 에이전트 캐스케이드

**LuthorSQL**([arXiv:2611.17780](https://arxiv.org/abs/2611.17780), 2026-11-13)은 frontier LLM tool-agent Text-to-SQL의 **지연·비용·쿼리 유출**을 줄이기 위해, 조직이 이미 보유한 로컬 GPU에서 돌리는 **비자동회귀(non-autoregressive) 7B System 1**이 먼저 답하고, 불확실할 때만 느린 System 2(호스티드 에이전트)로 escalate하는 캐스케이드다.

## 핵심 메커니즘

1. **단일 forward pass 슬롯 스코어**: 유한 grammar 위 query-plan 슬롯을 한 번에 예측한다(토큰 자동회귀 SQL 생성 아님).
2. **후보 컴파일·실행**: 최대 32개 plan을 컴파일·실행하고, 학습된 validator로 최종 답을 고른다.
3. **신뢰도 캐스케이드**: 로컬 모델이 확신 없을 때만 Claude Opus 등 System 2를 호출한다.

## 시사점 (공장·테넌트)

- BIRD hidden test **68.03% EX** @ **0.84 s/질의**(단일 GPU); 8-bit 양자화 시 **~9 GB**.
- Snowflake/BigQuery/MySQL/PostgreSQL/DuckDB로 zero-shot 전이 시 네이티브 SQLite 대비 **≤3.1%p** 하락.
- post-cutoff DB 프리레지스터 캐스케이드에서 질의의 약 절반을 로컬로 처리 → 동일 정확도에서 API 비용 **−33.3%**.
- 공개 벤치 골드 SQL 오염(Opus verbatim 재현 48–92%)과 별개로, 도구 사용 정확도는 스키마 rename·post-cutoff에서도 유지 — **게이트는 비용/프라이버시 레버리지**, 정확도 대체재 아님.
- 관련 축: [[wiki/Agents/Text-to-SQL/AV-SQL-Agentic-Views-Spider-2-0.md]](스키마 프루닝) · [[wiki/Agents/Text-to-SQL/sLM-for-T2SQL.md]](소형 로컬 T2SQL) · [[wiki/Agents/Text-to-SQL/VCoT-SQL-Dual-CoT-Validation.md]](검증기).

## 🔗 관련 문서

- [[wiki/Agents/Text-to-SQL/000_Text-to-SQL-MOC.md]]
- [[wiki/Agents/Text-to-SQL/AV-SQL-Agentic-Views-Spider-2-0.md]]
- [[wiki/Agents/Text-to-SQL/sLM-for-T2SQL.md]]
- [[wiki/Agents/Text-to-SQL/VCoT-SQL-Dual-CoT-Validation.md]]
- [[wiki/Agents/Text-to-SQL/SRPI-Streaming-Text-to-SQL-Prompt-Induction.md]]
