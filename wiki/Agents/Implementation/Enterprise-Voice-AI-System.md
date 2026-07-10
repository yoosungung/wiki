---
title: "Enterprise-Voice-AI-System"
related_raw: ["[[wiki/Agents/Implementation/Enterprise-Voice-AI-System.md]]"]
tags: ['wiki', 'agents_and_systems', 'llm_agent_&_deep_agents', 'basetech', 'llm_systems_projects']
type: "wiki"
status: "published"
last_updated: "2026-04-19"
---

# 엔터프라이즈 음성 AI 시스템

Tim Kramny는 21,000달러 규모의 엔터프라이즈 음성 AI 시스템을 구축하면서 업계에서 아무도 언급하지 않은 놀라운 데이터 저장 기술을 발견했습니다. 이 기술은 모델 자체가 아니라 데이터를 저장하는 방식과 이를 통해 가능해진 새로운 기능에 중점을 둡니다.

## 핵심 아이디어

모든 통화 종료 보고서(EOCR)를 두 개의 간단한 Supabase 테이블에 저장합니다.

*   **테이블 1: 통화 메타데이터**: 통화 시간, 시작/종료 시간, 평균 턴 레이턴시 등 모든 정량적 신호.
*   **테이블 2: 통화 아티팩트**: 스크립트, 요약, 구조화된 출력 및 TSV(Tab Separated Values) 열.

TSV 필드는 모든 스크립트와 요약이 작성 시점에 벡터화되도록 합니다. 이를 통해 음성 AI가 가졌던 모든 통화에 대해 RAG(Retrieval Augmented Generation)처럼 쿼리할 수 있습니다. 예를 들어, 특정 반대 의견, 감정 변화, 망설임 패턴, 주제 클러스터, AI가 혼란스러웠던 순간, 더 나은 결과와 상관관계가 있는 행동 등을 검색할 수 있습니다.

Kramny는 이를 "음성 AI 대화를 위한 ChatGPT"라고 부르며, 음성 AI의 진정한 개척지는 인간처럼 들리는 것을 넘어, 이미 가졌던 대화를 이해하는 것이라고 강조합니다.

## 출처

*   [LinkedIn Post](https://www.linkedin.com/posts/timkramny_we-built-a-21k-enterprise-voice-ai-system-activity-7396815814890364928-CIio?utm_source=share&utm_medium=member_ios&rcm=ACoAADm5eyABU_duDuXv1f9N-6JhXB_iNO6faes)
