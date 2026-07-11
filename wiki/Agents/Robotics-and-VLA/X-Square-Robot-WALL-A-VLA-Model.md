---
title: "X-Square-Robot-WALL-A-VLA-Model"
related_raw: ["[[wiki/Agents/Robotics-and-VLA/X-Square-Robot-WALL-A-VLA-Model.md]]"]
tags: ['wiki', 'agents_and_systems', 'robotics_&_physical_ai_(vla)']
type: "wiki"
status: "published"
last_updated: "2026-04-19"
updated: "2026-04-19"
---

# X-Square Robot WALL-A: VLA Foundation Model

**출처**: [원본 링크](https://pandaily.com/x-square-robot-unveils-wall-a-vla-foundation-model)
**날짜:** 2026-04-05
**태그:** #Robotics #VLA #Embodied-AI #World-Models #X-Square-Robot

## 요약 (Summary)
중국의 로봇 스타트업 X-Square Robot이 공개한 **WALL-A**는 비디오, 언어, 촉각 신호를 단일 엔드투엔드 아키텍처로 처리하는 **VLA(Vision-Language-Action)** 파운데이션 모델입니다. 이 모델은 물리적 세계의 인과관계를 이해하는 '세계 모델(World Models)'과 깊게 통합되어, 로봇이 낯선 환경에서도 자율적으로 판단하고 행동을 수정할 수 있게 합니다.

## 주요 기술적 특징 (Technical Highlights)
1.  **VLA + World Models 통합**:
    *   로봇이 자신의 행동 결과를 미리 예측하고 인과 추론(Causal Inference)을 통해 환경 피드백을 실시간으로 반영.
2.  **WALL-OSS (Open Source)**:
    *   Shared Attention 및 Task-routed FFN 아키텍처를 사용하여 시각, 언어, 모터 데이터를 효율적으로 처리하는 오픈소스 버전 공개.
3.  **제로샷 일반화 (Zero-shot Generalization)**:
    *   학습 데이터에 없는 비정형 환경에서도 모바일 조작(Mobile Manipulation) 임무 수행 가능.
4.  **자기 수정 (Self-correction)**:
    *   작업 중 오류나 방해 요소가 발생하면 인간의 개입 없이 폐루프(Closed-loop) 시스템을 통해 스스로 수정.

## 기존 노트와 링크 (Related Notes)
*   [[wiki/Agents/Robotics-and-VLA/Why VLAs are becoming the real link between AI reasoning and physical robotics]]
*   [[wiki/Agents/Robotics-and-VLA/VLA-Adapter - Effective Paradigm for Tiny-Scale VLA Models]]
*   [[wiki/Models/RL/World-Models-JEPA-LeWorldModel-Generative-Simulation]]
