---
title: "자가 수정 및 자가 진화 메커니즘"
related_raw: [
  "[[wiki/Agents/Implementation/Deep-Agents-and-Agents-2.0-2026.md]]",
  "[[wiki/Agents/Implementation/Deep-Agents-2.0.md]]"
]
tags: ['wiki', 'agents_2.0', 'self_correction', 'self_evolving', 'hyper_agents']
type: "wiki"
status: "published"
last_updated: "2026-04-20"
---

# Deep Agents: 자가 수정 및 자가 진화 메커니즘

Deep Agents(Agents 2.0)는 단순 실행을 넘어, 스스로의 오류를 정밀하게 수정하고 시스템 자체를 진화시키는 단계로 발전했습니다.

## 1. 정밀 자가 수정 (Self-Correction)
- **논리적 증명 및 수정**: 단순한 "다시 시도"가 아니라, 실행 환경이나 SMT 솔버의 피드백을 통해 논리적 오류를 스스로 증명하고 수정합니다.
- **실행 환경 피드백**: 코드가 실패하면 실행 결과(에러 메시지)를 분석하여 계획을 즉시 수정하거나 코드를 다시 작성합니다.
- **검증 루프**: Planner-Actor-Critic 루프를 통해 실행 결과의 품질을 스스로 비판하고 정제합니다.

## 2. 자가 진화 (Self-Evolving) 및 HyperAgents
- **메타 기술 학습**: 에이전트가 메모리 관리, 프롬프트 엔지니어링과 같은 '메타 기술' 자체를 학습하고 개선합니다. "개선하는 방법 자체를 개선"하는 수준에 도달한 형태입니다.
- **도메인 확장성**: 특정 도구에 국한되지 않고, 새로운 도구를 학습하거나 기존 도구의 활용 방식을 에이전트 스스로 최적화합니다.
- **HyperAgents**: Meta와 Oxford에서 2026년에 소개한 개념으로, 스스로를 리팩토링하고 최적화하는 에이전트 시스템을 의미합니다.

## 3. 기술적 의의
- **자율성 극대화**: 인간의 개입 없이도 장기 프로젝트를 완수할 수 있는 자가 치유 능력을 확보합니다.
- **동적 적응성**: 환경 변화에 따라 에이전트가 내부 시스템과 전략을 스스로 동적으로 변경할 수 있게 됩니다.

## 4. 관련 링크
- [[wiki/Agents/Implementation/Deep-Agents-Definition]]: 세대 변화와 정의
- [[Deep-Agents-State-Integrity]]: 상태 무결성 및 복잡성 제어
- [[Deep-Agents-Explicit-Planning]]: 명시적 계획 수립 기법
- [[Deep-Agents-Context-Engineering]]: 컨텍스트 엔지니어링 지침
