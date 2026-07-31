---
title: "AgentEval: 추론 기반 다중 에이전트 평가 프레임워크"
date: "2026-07-31"
last_updated: "2026-07-31"
updated: "2026-07-31"
related_raw: ["[[2026-07-31-eric-dong-agent-evaluation-strategy.md]]"]
tags: ["Agents", "Evaluations", "AgentEval", "DITING", "Multi-Agent-Evaluation"]
type: "wiki"
---

# AgentEval: 추론 기반 다중 에이전트 평가 프레임워크

**AgentEval**은 단순 어휘 매칭이나 정적 단위 테스트(Unit Tests)를 넘어, 복잡하고 장기적으로 실행되는 AI 에이전트의 다중 턴 상호작용 및 지능 수준을 심층 평가하기 위해 설계된 **추론 구동형 다중 에이전트 평가 프레임워크(Reasoning-driven Multi-agent Evaluation Framework)**입니다.

## 1. 개요 및 탄생 배경

- **프롬프트/에이전트 평가의 한계**: 전통적인 LLM 평가는 BLEU, ROUGE와 같은 기계적인 어휘 매칭이나 단일 단답형 질의에 대한 LLM-as-a-Judge 방식을 썼습니다. 그러나 멀티 에이전트 워크플로우는 상태 변화가 많고 긴 실행 단계를 가지므로, 단답형 평가 방식으로는 에이전트의 전체 자율 행동 품질을 평가할 수 없습니다.
- **연구적 배경**: 에릭 동(Eric Dong) 등을 필두로 한 연구팀이 웹 소설 번역 에이전트 평가 프레임워크인 **DITING**을 구축하면서, 번역의 문화적 충실도와 맥락적 일관성을 포괄적으로 검증하기 위한 하위 평가 엔진으로 **AgentEval**을 공식 제안 및 도입하였습니다.

## 2. AgentEval의 핵심 아키텍처 (전문가 토론 시뮬레이션)

AgentEval은 단일 평가 판정기(Judge)를 사용하는 대신, 서로 다른 도메인 전문가 역할을 부여받은 가상의 에이전트들이 **상호 교차 토론 및 델리버레이션(Deliberation)**을 거쳐 평가 결과에 도달하는 구조를 취합니다:

1. **역할 정의 (Role Definition)**: 평가 대상 도메인에 맞춰 '언어학 전문가', '플롯 분석가', '가이드라인 검증기' 등 특화된 평가 전문가 에이전트들을 생성합니다.
2. **토론 루프 (Multi-turn Deliberation)**: 평가 대상 에이전트가 출력한 결과물을 바탕으로, 전문가 에이전트들이 라운드 테이블식 토론을 나누며 논리적 결점, 지시 위반 사례를 검토합니다.
3. **합의 및 세부 보고서 출력**: 최종적으로 모든 전문가가 합의한 감점 요인과 가중치가 포함된 정량적 점수 및 개선 프롬프트 피드백을 에이전트 개발 파이프라인에 반환합니다.

## 3. 평가 차원 및 벤치마크 활용

AgentEval은 단순 오답 여부뿐만 아니라 다음과 같은 고차원적 성능 평가 지표를 도출합니다:
- **문화적 충실성 (Cultural Fidelity)**: 로컬 번역 시 비유나 고유명사의 의미 보존 수준.
- **일시적 일관성 (Temporal Coherence)**: 긴 다중 턴 시나리오 내에서 에이전트가 상태(State) 및 문맥을 파괴하지 않고 올바르게 조율했는지 여부.
- **도구 도달률 및 안전성**: 시스템 예외나 가드레일에 부딪히지 않고 최종 목표에 올바르게 도달한 경로 효율성.

## 🔗 연결된 문서
- [[wiki/Agents/Evaluations/000_Evaluations-MOC.md]]
- [[wiki/Agents/Evaluations/Deep-Agent-Evaluation-Framework.md]]
- [[wiki/Engineering/Prompt-Engineering/프롬프트 엔지니어링에서 컨텍스트 엔지니어링으로의 전환.md]]
