---
title: "Memento: 파라미터 업데이트가 필요 없는 에이전트 스킬 자가 학습(Read-Write Reflective Learning) 프레임워크"
tags: ["Memento", "Agent-Skills", "Self-Evolution", "Parameter-Free", "Reinforcement-Learning"]
last_updated: "2026-07-06"
related_raw: ["[[2026-07-06-memento_skills_framework.md]]"]
---

# 🔄 Memento: 파라미터 업데이트가 필요 없는 에이전트 스킬 자가 학습 프레임워크

Memento-Skills는 에이전트의 파라미터 미세 조정(Fine-tuning)을 수행하지 않고도 에이전트가 경험을 통해 자율적으로 기술을 습득하고 진화시키는 강화학습 및 메모리 아키텍처 프레임워크입니다.

## 1. 자가 설계 에이전트 (Agent-Designing Agents)
- 에이전트가 다른 하위 에이전트의 작업을 지시하고 평가하여 필요한 기술(Skills)을 자율 설계함.
- 개발 라이프사이클 도중 축적된 피드백을 바탕으로 기술의 결함을 메우는 '컴패니언' 에이전트 체계와 맞닿아 있음.

## 2. 읽기-쓰기 성찰 학습 (Read-Write Reflective Learning)
- 특정 작업에 필요한 기술 사양서(스킬 문서)를 마크다운(`SKILL.md`) 형태로 외부 메모리 공간에 저장.
- 에이전트는 작업을 실행하기 전에 스킬 문서를 읽어 참조하고(Read), 실행 결과를 평가하여 개선점이 있을 경우 이를 다시 스킬 문서에 갱신하여 덮어씀(Write & Reflect).
- 이를 통해 모델 가중치를 건드리지 않는 parameter-free 평생 학습(lifelong learning) 시스템을 구현함.

---
**관련 문서**:
- [[wiki/Agents/Self-Evolving/SkillOpt-및-과학적-탐구-멀티-에이전트-시스템.md]]

