---
title: "Agent0-Framework"
related_raw: ["[[wiki/Agents/Frameworks/Agent-Frameworks/Agent0-Framework.md]]"]
tags: ['wiki', 'agents_and_systems', 'llm_agent_&_deep_agents', 'agent_frameworks_and_trends']
type: "wiki"
status: "published"
last_updated: "2026-04-19"
updated: "2026-04-19"
---

# Agent0: A Framework for Autonomous LLM Agents with Dynamic Memory and Collaborative Reasoning

## 📑 개요 (Overview)
- **URL**: [arXiv:2603.20001](https://arxiv.org/abs/2603.20001)
- **핵심 키워드**: #LLM-Agent #Autonomous-Agent #Dynamic-Memory #Collaborative-Reasoning

## 🧠 핵심 기술 아키텍처 (Key Architecture)
본 논문은 기존 에이전트의 한계인 '장기 기억 상실'과 '경직된 추론 구조'를 해결하기 위해 **Agent0** 프레임워크를 제안합니다.

### 1. D-Mem (Dynamic Memory)
- 에이전트가 수행한 작업의 맥락을 실시간으로 업데이트합니다.
- 단순 로그 저장이 아닌, 정보를 중요도와 개념에 따라 계층화하여 저장하는 동적 메모리 시스템입니다.
- 경험한 사건을 '개념적 지식'으로 변환하여 필요할 때 즉시 인출할 수 있게 합니다.

### 2. CRAFT (Collaborative Reasoning and Action Framework for Tasks)
- 복잡한 문제를 하위 작업(Sub-tasks)으로 자동 분할합니다.
- 각 작업에 특화된 '전문가 에이전트'를 동적으로 생성하거나 호출하여 협업하게 합니다.
- 최적의 도구(Tool) 선택 및 실행 과정을 오케스트레이션합니다.

## 📈 주요 기여 및 성과 (Contributions & Results)
- **성능 향상**: 소프트웨어 엔지니어링 및 복잡한 데이터 분석 작업에서 기존 ReAct나 AutoGPT 방식보다 약 **40% 높은 성공률**을 기록했습니다.
- **자율성**: 인간의 개입 없이도 스스로 추론 경로를 수정하고 메모리를 관리하는 높은 수준의 자율성을 입증했습니다.

## 🔗 관련 링크 (Related Links)
- **GitHub**: [agent0-ai/agent0-core](https://github.com/agent0-ai/agent0-core)
- **기존 노트 연결**: [[wiki/Agents/Frameworks/000_LLM-Agent-MOC]], [[wiki/Agents/Implementation/Deep-Agents-2.0]]

---
*Created on: 2026-03-20*
