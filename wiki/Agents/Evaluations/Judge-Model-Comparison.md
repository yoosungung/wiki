---
title: "Judge 모델 비교: LLM vs Agent as a Judge"
related_raw: ["[[wiki/Agents/Evaluations/LLM-as-a-Judge 평가 방식의 문제점과 해결책.md]]", "[[wiki/Agents/Evaluations/Agent-as-a-Judge - 에이전트 시스템 평가를 위한 새로운 프레임워크.md]]"]
tags: ['wiki', 'agents', 'evaluation', 'llm_as_a_judge', 'agent_as_a_judge']
type: "wiki"
status: "published"
last_updated: "2026-04-20"
updated: "2026-04-20"
---

# Judge 모델 비교 및 최적화

에이전트 시스템 평가를 위해 다른 AI 모델을 심판으로 사용하는 기법들이 발전하고 있습니다.

## 1. LLM-as-a-Judge: 한계와 보정
LLM이 답변을 평가하는 방식은 빠르지만, 비대칭적인 편향(Bias)이 발생할 수 있습니다.
- **문제점**: 성능이 낮은 모델은 과대평가되고, 높은 모델은 과소평가되는 경향이 있음.
- **해결책**: 작은 보정용 데이터셋을 사용해 정답/오답 판단 확률(q1, q0)을 추정하고, 이를 기반으로 정확도를 보정해야 합니다.

## 2. Agent-as-a-Judge: 차세대 프레임워크
에이전트 시스템이 다른 에이전트를 평가하는 방식으로, 단순 결과 비교를 넘어 동적이고 확장 가능한 평가를 지향합니다.
- **장점**: LLM-as-a-Judge보다 뛰어난 성능을 보이며 인간 평가와 유사한 신뢰도를 확보합니다. 시간과 비용을 크게 절감할 수 있습니다.
- **벤치마크 (DevAI)**: 55개의 실제 AI 개발 작업으로 구성되어 코드 생성 에이전트 평가에 특화되어 있습니다.

## 3. 요약 및 제언
LLM-as-a-Judge는 버려야 할 기술이 아니라 정확한 통계적 보정을 통해 사용해야 할 기술이며, 복잡한 워크플로우 평가에는 Agent-as-a-Judge가 더 적합합니다.

## 관련 문서
- [[wiki/Agents/Evaluations/Agent-evaluation-Methodology.md|AI 에이전트 평가 방법론]]
- [[wiki/Agents/Evaluations/Deep-Agent-Evaluation-Framework.md|Deep Agent 평가 프레임워크]]
- [[wiki/Agents/Frameworks/Evaluations/000_Evaluations-MOC.md|Evaluations-MOC]]
