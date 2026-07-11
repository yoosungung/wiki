---
title: "OpenSpace-Self-Evolving-Agents"
related_raw: ["[[wiki/Agents/Self-Evolving/OpenSpace-Self-Evolving-Agents.md]]"]
tags: ['wiki', 'agents_and_systems', 'llm_agent_&_deep_agents', 'self_evolving_agents']
type: "wiki"
status: "published"
last_updated: "2026-04-19"
updated: "2026-04-19"
---

# OpenSpace: 자가 진화형 에이전트 엔진 (Self-Evolving Agents)

## 요약
에이전트가 실무 경험을 통해 스스로 학습하고 진화하며, 그 능력을 다른 에이전트와 공유할 수 있게 하는 오픈소스 프레임워크입니다. 기존 에이전트들이 매번 처음부터 추론을 시작하여 토큰 낭비가 심하고 실수를 반복한다는 점에 착안하여, 성공적인 작업 패턴을 '스킬(Skill)' 단위로 저장하고 최적화합니다. 'Self-Evolution Engine'을 통해 오류를 자동으로 수정(Auto-Fix)하고 성능을 개선(Auto-Improve)하며, 이를 공유함으로써 집단 지성을 구현합니다. 실험 결과, 기존 대비 토큰 사용량을 46% 절감하면서도 경제적 가치 창출 능력은 4.2배 향상되었습니다.

## 핵심 기능
- **Self-Evolution Engine**: FIX(오류 수정), DERIVED(기존 스킬 파생), CAPTURED(새로운 패턴 포착)의 세 가지 모드로 스킬 학습 자동화.
- **Skill Engine**: 완료된 작업에서 패턴을 추출하여 재사용 가능한 스킬로 저장.
- **에이전트 공유**: 학습된 스킬을 클라우드나 커뮤니티를 통해 다른 에이전트와 공유.
- **비용 효율성**: 재사용 가능한 스킬을 통해 복잡한 추론 단계를 생략, 토큰 비용 획기적 절감.

## 기존 지식과의 연결
- Deep Agents: 경험을 통해 성장하는 '학습하는 에이전트'의 실질적인 구현체.
- RAG: 과거에 성공했던 '작업 절차(Workflow)' 자체를 검색하고 재사용하는 '절차적 RAG' 개념 도입.
- Knowledge Graph: 에이전트 간의 스킬 공유와 진화 계보를 관리하는 지식 그래프 구조 활용 가능.

## 원문 URL
https://github.com/HKUDS/OpenSpace
