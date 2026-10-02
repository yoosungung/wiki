---
title: "Neural Procedural Memory (NPM) 및 에이전트 암묵적 행동 아키텍처"
date: "2026-07-31"
last_updated: "2026-07-31"
updated: "2026-07-31"
related_raw: ["[[2026-07-31-kiwoong-yeom-neural-procedural-memory.md]]"]
tags: ["Agents", "Memory-and-Cognition", "Neural-Procedural-Memory", "Implicit-Reasoning", "Agent-Memory"]
type: "wiki"
---

# Neural Procedural Memory (NPM) 및 에이전트 암묵적 행동 아키텍처

인간은 자전거를 타거나 설거지를 할 때 머릿속으로 상세 지침이나 규칙 선언문(예: "페달에 왼발을 얹고 균형을 잡는다", "컵을 먼저 씻고 팬을 씻는다")을 명시적으로 언어화하여 읽으며 행동하지 않습니다. 인간의 거동은 이미 몸에 밴 **절차적 기억 (Procedural Memory)**과 **암묵적 추론 (Implicit Reasoning)**을 기반으로 유기적이고 연속적으로 수행됩니다.

**Neural Procedural Memory (NPM)**는 인공지능 에이전트가 모든 결정을 텍스트 기반의 명시적 프롬프트 Scaffolding(CoT 등)에 의존하여 처리하는 대신, 신경망 자체에 내재화된 행동 교정 회로 및 암묵적 절차 기억을 통해 자연스럽고 신속하게 오류를 교정하며 행동하도록 돕는 아키텍처입니다.

## 1. 명시적 스캐폴딩(CoT)의 한계와 암묵적 계획의 장점

- **CoT/Scaffolding의 문제**: 에이전트가 다음 행동을 결정하기 위해 매번 복잡한 프롬프트를 읽고, CoT(Chain of Thought)를 통해 수백 줄의 텍스트 토큰을 생성하는 방식은 추론 비용(Token cost)이 크고 지연시간(Latency)이 길어 실시간 로보틱스나 즉각적인 터미널 인터랙션 환경에 적합하지 않습니다.
- **NPM의 솔루션 (Implicit Planning Logic)**:
  - 에이전트가 고품질의 결과 및 가상 피드백을 통해 **역설계(Reverse Engineering) 방식**으로 행동 오류 교정 회로를 내재화합니다.
  - 별도의 외부 프롬프트 지시 없이도, 신경망의 내부 상태 전이(State Transition)만을 조종하여 행동의 오류를 즉시 감지하고 실시간 교정(Online Correction)을 개시합니다.
  - 마치 인간이 자전거가 기울어질 때 몸의 각도를 즉각 반사적으로 조절하듯이 에이전트의 거동을 제어합니다.

## 2. RAG 및 에이전틱 지식 베이스(KM)에서의 응용 의의

- **에이전트 스킬 진화**: 에이전트의 동작 스킬을 매번 수동 프롬프트 규칙 추가로 관리하면 프롬프트가 거대해져 context가 오염됩니다. 스킬을 NPM 형태로 추상화하고 미세조정(Fine-tuning)을 통해 모델 몸체(Parametric memory)에 직접 각인시키면, 도구 호출 정확도를 비약적으로 올릴 수 있습니다.
- **효율성**: 토큰 직렬화 단계를 배제하여 긴 다중 턴 에이전트 시나리오의 실행 대역폭을 획기적으로 개선합니다.

## 🔗 연결된 문서
- [[wiki/Agents/Memory-and-Cognition/000_Memory-and-Cognition-MOC.md]]
- [[wiki/Agents/Memory-and-Cognition/AI-Agent-Memory-Architecture.md]]
- [[wiki/Engineering/Prompt-Engineering/프롬프트 엔지니어링에서 컨텍스트 엔지니어링으로의 전환.md]]
