---
title: "Hyperagents-Self-Evolving-AI"
related_raw: ["[[wiki/Agents/Self-Evolving/Hyperagents-Self-Evolving-AI.md]]"]
tags: ['wiki', 'agents_and_systems', 'llm_agent_&_deep_agents', 'self_evolving_agents']
type: "wiki"
status: "published"
last_updated: "2026-04-19"
updated: "2026-04-19"
---

# Hyperagents: 재귀적 자기 개선을 통한 자가 진화 AI

### 1. 개요 및 핵심 컨셉
**Hyperagents**는 UBC와 Meta 연구진이 제안한 혁신적인 프레임워크로, AI 에이전트가 단순히 주어진 작업을 수행하는 것을 넘어 **자신의 로직과 도구 활용 방식 자체를 스스로 수정하고 진화**시키는 '메타인지적(Metacognitive)' 능력을 부여합니다. 이는 다윈의 진화론과 괴델의 불완전성 원리에서 영감을 받은 'Darwin-Gödel Machine'의 현대적 구현체입니다.

### 2. 주요 기술 세부 사항
- **Self-Modification Loop:** 에이전트가 자신의 실행 기록(Trace)을 분석하여 실패 원인을 찾고, 이를 해결하기 위한 코드나 지침을 스스로 수정하여 다음 실행에 반영합니다.
- **DGM-H (Darwin-Gödel Machine with Hyperagents):** 작업 수행 엔진과 수정 엔진을 하나의 편집 가능한 프로그램 단위로 통합하여, 에이전트가 자신의 하위 시스템을 자유롭게 재구성할 수 있게 합니다.
- **Transferable Strategies:** 특정 도메인(예: 코딩)에서 학습한 최적화 전략을 전혀 다른 도메인(예: 수학적 추론)으로 전이하여 성능을 높일 수 있는 범용성을 보입니다.

### 3. 관련 기술 URL 및 리소스
- [HyperAgents GitHub Repository](https://github.com/facebookresearch/HyperAgents)
- [Hyperagents: Self-Evolving AI Paper](https://arxiv.org/abs/2603.xxxxx)
- [AlphaXiv Hyperagents Discussion](https://alphaxiv.org/abs/2603.xxxxx)
- [Meta AI Research: Recursive Self-Improvement](https://ai.meta.com/research/)

### 4. 설명 이미지 추출 (Conceptual)
- ![Hyperagents Feedback Loop](https://example.com/hyperagents-loop.png) (자기 수정 루프 및 메타 에이전트 상호작용도)
- ![Performance Gain Visualization](https://example.com/hyperagents-eval.png) (진화 횟수에 따른 성능 향상 곡선)

### 5. 관련 노트 링크
- [[wiki/Agents/Self-Evolving/Self-Evolving-Agents-Autonomous-Tools-2026]]
- [[wiki/Agents/Self-Evolving/Self-Evolving-Agents-NVIDIA]]
- Metacognitive_Reuse
