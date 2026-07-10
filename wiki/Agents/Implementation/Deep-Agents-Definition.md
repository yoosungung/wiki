---
title: "Deep Agents (Agents 2.0) 정의 및 세대 변화"
related_raw: [
  "[[raw/NVIDIA-NeMoProRL-Agent-Server.md]]",
  "[[raw/The Runtime Behind Production Deep Agents.md]]",
  "[[wiki/Agents/Implementation/Agents 2.0 - From Shallow Loops to Deep Agents.md]]",
  "[[wiki/Agents/Implementation/Agents 2.0 - Part 2 - Architecture.md]]",
  "[[wiki/Agents/Implementation/Agents 2.0 - Part 3 - Visualization and Conclusion.md]]",
  "[[wiki/Agents/Implementation/Agents-2.0-Discussion.md]]",
  "[[wiki/Agents/Implementation/Deep-Agents-2.0.md]]",
  "[[wiki/Agents/Implementation/Deep-Agents-and-Agents-2.0-2026.md]]"
]
tags: ['wiki', 'agents_2.0', 'deep_agents', 'architecture', 'agent_evolution']
type: "wiki"
status: "published"
last_updated: "2026-04-22"
---

# Deep Agents (Agents 2.0) 정의 및 세대 변화

2026년 AI 에이전트 기술은 단순한 '챗봇' 수준을 넘어, 스스로 계획을 수립하고 복잡한 워크플로우를 자율적으로 수행하는 **Deep Agents (Agents 2.0)** 시대로 진입했습니다.

## 1. 세대 변화: Shallow vs Deep

| 구분 | Shallow Agents (1.0) | Deep Agents (2.0) |
| :--- | :--- | :--- |
| **계획 수립** | 암시적 계획 (사고의 연쇄, CoT) | 명시적 계획 (도구 기반 계획 유지) |
| **동작 방식** | 반응형 루프 (Reactive) | 사전 예방적 아키텍처 (Proactive) |
| **메모리 관리** | 컨텍스트 창 의존 | 영구적 외부 메모리 (VFS, DB) 활용 |
| **복잡성 제어** | 단일 프롬프트 만능주의 | 계층적 위임 및 컨텍스트 격리 |
| **수행 시간** | 몇 초 ~ 몇 분 | 몇 시간 ~ 며칠 단위의 장기 과제 |

## 2. 핵심 아키텍처 및 구현 (4대 기둥)

LangChain의 개념 가이드와 NVIDIA의 구현 사례를 통해 정립된 Deep Agents의 런타임 요구사항입니다.

1. **계획 및 작업 분해 (Planning & Task Decomposition)**:
   - 복잡한 목표를 작은 단위의 작업으로 나누고 진행 상황을 추적하며 필요에 따라 계획을 동적으로 수정함.
2. **파일 시스템 기반 컨텍스트 관리 (Context Management)**:
   - 가상 파일 시스템(VFS)을 활용하여 중간 결과물을 파일로 저장함으로써 컨텍스트 오버플로우를 방지하고 대규모 데이터를 다룸.
3. **하위 에이전트 생성 및 위임 (Subagent Spawning)**:
   - 특정 전문 작업이 필요한 경우 하위 에이전트를 생성하여 위임하며, 각 에이전트는 격리된 컨텍스트에서 작동하여 정보 혼선(Context Pollution)을 차단함.
4. **지속성 및 내구성 (Durable Execution)**:
   - 실행 상태를 체크포인트로 저장하여 시스템 장애 시에도 작업을 재개할 수 있도록 보장함.

## 3. 주요 기술 사례

### NVIDIA ProRL-Agent-Server (2026)
- **Rollout-as-a-Service**: RL 에이전트 훈련과 롤아웃 인프라를 분리하여 확장성 확보.
- **OpenHands 기반**: 높은 동시성과 플러그 가능한 핸들러 인터페이스 제공.
- **성능 향상**: SWE-Bench-Verified 기준 Pass@1 성능을 14.8%에서 21.2%로 대폭 향상시킴.

## 4. 관련 개념
- [[Deep-Agents-Explicit-Planning]]: 명시적 계획 수립 기법
- [[Deep-Agents-Hierarchical-Delegation]]: 계층적 위임 구조
- [[Deep-Agents-Persistent-Memory]]: 영구 메모리 활용
- [[Deep-Agents-Context-Engineering]]: 극한의 컨텍스트 엔지니어링
- [[Deep-Agents-State-Integrity]]: 상태 무결성 관리
- [[wiki/Agents/Implementation/Self-Evolving-Agents-Self-Correction]]: 자가 진화 및 수정 메커니즘
