---
title: "Deep Agent 평가 프레임워크"
related_raw: ["[[wiki/Agents/Evaluations/Evaluating-Deep-Agents.md]]", "[[wiki/Agents/Evaluations/AI-Agent-Evaluation.md]]"]
tags: ['wiki', 'agents', 'evaluation', 'deep_agents', 'langchain']
type: "wiki"
status: "published"
last_updated: "2026-04-20"
updated: "2026-04-20"
---

# Deep Agent 평가 프레임워크

LangChain의 Deep Agents 평가 사례를 바탕으로 한 다단계 평가 전략입니다.

## 1. 평가 수준 (Levels of Evaluation)
- **단일 단계 평가 (Single-Step)**: 특정 입력 직후 에이전트가 올바른 도구를 올바른 인수로 호출했는지 즉각 검증합니다. (도구 호출 정확성 측정)
- **전체 에이전트 턴 (Full Agent Turn)**: 종단 간(End-to-End) 작업의 **궤적(Trajectory)**, 최종 응답 및 중간 상태의 무결성을 평가합니다. 단순 결과뿐만 아니라 에이전트가 거쳐온 모든 단계(생각, 도구 사용, 결과 해석)를 종합적으로 검증합니다.
- **다중 턴 시뮬레이션 (Multi-Turn)**: 순차적 사용자 입력이 있는 대화 상황에서 에이전트의 일관성과 경로 이탈 대응력을 테스트합니다. 특히 오류 복구 능력(Resilience)을 중점적으로 측정합니다.

## 2. 기술적 구현 전략
- **타겟팅된 평가 (Targeted Evals)**: 특정 행동 패턴(예: 파일 읽기 효율성, 계획 수립의 구체성)을 유도하고 측정하기 위한 전용 지표를 설계합니다.
- **맞춤형 테스트 로직**: 최종 메시지 검증을 넘어 에이전트의 궤적에 대한 특정 주장을 포함합니다.
- **환경 격리**: 각 평가마다 깨끗한 환경을 제공하며, API 모킹(Mocking) 및 재생(Replaying)을 통해 속도와 재현성을 높입니다.
- **데이터셋 분리**: 과적합 방지를 위해 학습 셋과 테스트 셋을 엄격히 분리하고 Opik 등을 통해 관리합니다.

## 3. 도메인 협업
평가 기준은 기술적 최적화보다 도메인 전문가와의 반복(Iteration)을 통해 정의된 비즈니스 정합성이 더 중요합니다.

## 관련 문서
- [[wiki/Agents/Evaluations/Agent-evaluation-Methodology.md|AI 에이전트 평가 방법론]]
- [[wiki/Agents/Evaluations/Judge-Model-Comparison.md|Judge 모델 비교 분석]]
- [[wiki/Agents/Frameworks/Evaluations/000_Evaluations-MOC.md|Evaluations-MOC]]
