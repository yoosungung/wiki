---
title: "Agent0"
related_raw: ["[[wiki/Agents/Implementation/Agent0.md]]"]
tags: ['wiki', 'agents_and_systems', 'llm_agent_&_deep_agents', 'implementations', 'general_llm_agent_projects']
type: "wiki"
status: "published"
last_updated: "2026-04-19"
updated: "2026-04-19"
---

# Agent0: 제로 데이터로부터 자체 진화하는 에이전트

**출처**: [원본 링크](https://github.com/aiming-lab/Agent0)

Agent0 시리즈는 인간이 직접 큐레이션한 데이터셋이나 수작업 감독 없이도 에이전트가 스스로 개선하고 진화할 수 있음을 보여주는 자율 에이전트 개발의 새로운 방향을 제시합니다. 이 프로젝트는 도구 통합 추론을 통해 자체 개선 에이전트를 발전시키는 두 가지 상호 보완적인 연구인 Agent0과 Agent0-VL을 통합합니다.

## 1. Agent0: 자체 진화 언어 에이전트
Agent0은 다단계 공동 진화 및 원활한 도구 통합을 통해 고성능 언어 에이전트를 진화시키는 완전 자율 프레임워크입니다. 이 프레임워크는 두 에이전트 간의 공생 경쟁을 통해 작동합니다:
*   **Curriculum Agent**: 점점 더 도전적인 최전선 작업을 제안합니다.
*   **Executor Agent**: 외부 도구를 사용하여 이러한 작업을 해결하는 방법을 학습합니다.

**주요 결과:**
*   수학적 추론 벤치마크에서 +18% 개선을 달성했습니다.
*   일반 추론 벤치마크에서 +24% 개선을 달성했습니다.
*   훈련에 외부 데이터가 전혀 필요하지 않습니다.
*   다중 턴 상호 작용을 지원합니다.

## 2. Agent0-VL: 자체 진화 시각-언어 에이전트
Agent0-VL은 Agent0 패러다임을 다중 모달 추론 작업으로 확장하는 자체 진화 시각-언어 에이전트입니다. 이 모델은 추론뿐만 아니라 자체 평가 및 자체 수리에도 도구 사용을 통합하는 이중 역할 아키텍처를 특징으로 합니다:
*   **Solver**: 다중 턴 도구 통합 추론을 수행합니다.
*   **Verifier**: 구조화된 피드백과 세분화된 자체 보상을 생성합니다.

**주요 결과:**
*   시각적 추론 벤치마크에서 평균 +12.5% 개선을 달성했습니다.
*   테스트 시간 스케일링 성능에서 +7.3% 개선을 보였습니다.
*   오픈 소스 시각-언어 모델 중 최첨단 성능을 자랑합니다.
*   자체 진화에 외부 보상이 전혀 필요하지 않습니다.

## 공통 철학
두 프로젝트 모두 **제로 데이터 자체 진화(zero-data self-evolution)** 원칙을 기반으로 합니다:
*   **인간 주석 없음**: 외부 데이터나 인간 감독에 대한 의존성을 완전히 제거합니다.
*   **도구 통합 추론**: 문제 해결 능력을 향상시키기 위해 외부 도구를 활용합니다.
*   **자율 진화**: 지능적인 탐색을 통해 자체적으로 훈련 데이터를 생성합니다.

---
## 관련 노트
- [[wiki/Models/RL/Self-Evolving Agents - 자가 학습형 AI 에이전트 재훈련 매뉴얼]]
- [[wiki/Engineering/Infrastructure-and-DevOps/DGX Spark에서의 VLM 파인튜닝]]
- [[wiki/Agents/Robotics-and-VLA/VLA-Adapter - Effective Paradigm for Tiny-Scale VLA Models]]
