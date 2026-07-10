---
title: "Agent-as-a-judge-Framework-에이전트-기반-평가-프레임워크"
related_raw: ["[[wiki/Agents/Frameworks/Evaluations/Agent-as-a-judge-Framework-에이전트-기반-평가-프레임워크.md]]"]
tags: ['wiki', 'knowledge_and_memory', 'advanced_rag_&_knowledge_graph', 'agent_memory_and_cognition']
type: "wiki"
status: "published"
last_updated: "2026-04-19"
---

# Agent-as-a-Judge: 에이전트 기반 평가 프레임워크

## 개요 및 배경
'Agent-as-a-Judge'는 에이전트 시스템 평가를 위한 차세대 프레임워크로, 기존의 단순한 결과 중심 평가나 수동 평가의 한계를 극복하기 위해 제안되었습니다. 이 방식은 에이전트 시스템 자체가 다른 에이전트의 수행 과정을 평가하며, 특히 동적인 환경에서의 복잡한 작업 수행 능력을 정밀하게 측정하는 데 중점을 둡니다.

## 핵심 내용
*   **동적 평가 구조:** 최종 결과물뿐만 아니라 에이전트가 문제를 해결하기 위해 거친 중간 추론 단계, 도구 사용의 적절성, 오류 복구 능력 등을 종합적으로 평가합니다.
*   **신뢰도 기반 통합:** 모델이 내부 지식과 외부 검색 정보 사이의 모순을 발견했을 때, 각 정보의 출처 신뢰도를 수치화하여 판단하는 '신뢰도 기반 통합 메커니즘'을 적용합니다.
*   **검증 레이어 추가:** 단순한 어텐션 메커니즘을 넘어, 생성된 답변이 실제 소스 문서에 근거하고 있는지(Grounding)를 실시간으로 체크하는 레이어를 포함합니다.

## 주요 성과
*   **정확도 향상:** 복잡한 법률 및 의료 질의응답 벤치마크에서 기존 RAG 모델 대비 약 25%의 성능 향상을 입증했습니다.
*   **효율성:** 인간 평가에 가까운 신뢰도를 유지하면서도 평가에 소요되는 시간과 비용을 획기적으로 절감할 수 있습니다.

## 원본 URL
- https://arxiv.org/abs/2601.05111

## 관련 링크
- [[wiki/Agents/Evaluations/Agent-as-a-Judge - 에이전트 시스템 평가를 위한 새로운 프레임워크]]
- [[wiki/Agents/Evaluations/Evaluating-Deep-Agents]]
- [[wiki/Agents/Evaluations/LangChain-Deep-Agents-Evaluation]]
