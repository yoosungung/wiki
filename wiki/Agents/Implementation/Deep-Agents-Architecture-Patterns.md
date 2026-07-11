---
title: "Deep Agents: 아키텍처 패턴 및 핵심 기둥"
tags: ['wiki', 'agents_2.0', 'deep_agents', 'architecture', 'patterns']
type: "wiki"
status: "published"
last_updated: "2026-04-20"
updated: "2026-04-20"
---

# Deep Agents (Agents 2.0): 아키텍처 패턴 및 핵심 기둥

Deep Agents(또는 Agents 2.0)는 단순한 '챗봇' 루프를 넘어, 모델 주변의 정교한 엔지니어링(에이전트 하네스)을 통해 장기 과제를 자율적으로 수행하는 시스템을 의미합니다.

## 1. 명시적 계획 (Explicit Planning)
실행과 계획을 명확히 분리하여 장기 과제 수행 시의 논리적 붕괴를 방지합니다.
- **도구 기반 계획 유지:** 에이전트가 내부 추론(CoT)에만 의존하지 않고, `PLAN.md`와 같은 마크다운 파일이나 JSON 형태의 할 일 목록을 직접 생성하고 관리합니다.
- **DAG 기반 워크플로우:** 복잡한 문제를 세부 과업으로 분해하고, 진행 상황에 따라 계획을 스스로 수정(Self-correction)합니다.

## 2. 계층적 위임 및 컨텍스트 격리 (Hierarchical Delegation & Context Isolation)
복잡성을 관리하고 토큰 팽창(Token Bloat)을 방지하기 위한 구조적 접근입니다.
- **오케스트레이터 패턴:** 메인 에이전트는 프로젝트 매니저 역할을 수행하며, 특정 작업(연구, 코딩 등)에 특화된 하위 에이전트에게 업무를 위임합니다.
- **컨텍스트 격리:** 각 하위 에이전트는 독립적인 컨텍스트 내에서 실행되며, 결과물만 요약하여 반환합니다. 이를 통해 메인 에이전트의 판단력을 보호합니다.

## 3. 영구 메모리 및 가상 파일 시스템 (Persistent Memory & VFS)
컨텍스트 윈도우의 한계를 외부 저장소를 통해 극복합니다.
- **진실의 원천 (Source of Truth):** 중간 결과물, 코드, 데이터 등을 가상 파일 시스템(VFS)에 실제 파일 형태로 저장하고 후속 단계에서 참조합니다.
- **기억에서 검색으로:** 모든 정보를 컨텍스트에 담으려 하지 않고, 필요한 정보를 어디서 찾을 수 있는지(검색 쿼리, 파일 경로) 아는 능력에 집중합니다.

## 4. 상태 무결성 및 런타임 (State Integrity & Runtime)
장기 실행 경로에서의 안정성을 확보합니다.
- **상태 관리 (State Management):** 작업 중단 시에도 마지막 지점부터 재개할 수 있는 체크포인팅 기능을 활용합니다.
- **에이전트 하네스 (Agent Harness):** 모델 자체의 성능보다 이를 감싸는 제어 장치(계획, 메모리, 도구 오케스트레이션)의 설계가 에이전트의 품질을 결정합니다.

## 5. ThoughtMinds 아키텍처 (2026)
ThoughtMinds에서 제안하는 차세대 구조는 다음과 같습니다:
- **인지 계층 (Cognitive Layer):** 다단계 추론 및 계획 수립.
- **행동 계층 (Action Layer):** ERP, CRM 등 기업 시스템과의 API 통합 및 실질적 업무 수행.
- **메모리 엔진 (Memory Engine):** 과거 상호작용과 기업 지식 베이스의 지속적 학습.

## 관련 문서
- [[wiki/Agents/Implementation/Deep-Agents-Definition]]: 세대 변화와 정의
- [[wiki/Agents/Frameworks/000_LLM-Agent-MOC]]: 에이전트 전체 맵
- [[wiki/Agents/Implementation/deepagents]]: LangChain의 Deep Agents 구현 패키지
