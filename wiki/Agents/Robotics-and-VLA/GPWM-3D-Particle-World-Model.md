---
id: gpwm-3d-particle-world-model
title: "GPWM: 3D 입자 모션 기반 생성형 물리 월드 모델"
status: canonical
owner: km
updated: "2026-11-17"
last_updated: "2026-11-17"
sources:
  - https://arxiv.org/abs/2611.08338
tags: ["Agents", "Robotics", "World-Model", "3D-Particles", "Flow-Matching", "Physical-AI"]
type: "wiki"
---

# GPWM: 3D 입자 모션 기반 생성형 물리 월드 모델

**GPWM (Generative Particle World Model)**([arXiv:2611.08338](https://arxiv.org/abs/2611.08338))은 2D 픽셀/비디오 외형을 생성하는 기존 비디오 월드 모델과 달리, **3D 물리 공간의 입자(particles)와 강체(rigid bodies) 모션**을 직접 예측하는 통합 물리 월드 모델이다.

## 아키텍처 및 데이터셋

- **통합 물리 표현**: 단일 표현과 단일 가중치 세트(Unified GPWM)로 **강체(rigid), 변형체(deformable), 천(cloth), 입상 물질(granular)** 및 수동 물리·로봇 상호작용을 모두 다룬다.
- **네트워크 구조**: **객체 인식 다중 해상도 트랜스포머(Object-aware multi-resolution transformer)**에 **Flow Matching**과 **Diffusion Forcing**을 결합해 학습 지평선(training horizon)을 훨씬 넘는 장기 궤적을 일관되게 생성한다.
- **ParticleWorlds 코퍼스**: 다양한 기하 구조, 물성, 상호작용, 로봇 임바디먼트를 포함한 **2,550만 프레임(25.5M frames)** 규모의 3D 입자 물리 코퍼스로 학습·평가한다.

## 노이즈 공간 계획 (Noise-Space Planning)

GPWM은 구동기(actuator)-객체 공동 모션의 생성형 사전 분포(generative prior)를 학습하므로, 접촉이 복잡한 조작(contact-rich manipulation)에서 기존 행동 공간 탐색과 다른 계획 방식을 취한다.

| 비교 축 | 행동 공간 탐색 (Action-Space Search) | GPWM 노이즈 공간 계획 (Noise-Space Planning) |
| :--- | :--- | :--- |
| **탐색 대상** | 비제약(unconstrained) 원시 행동 시퀀스 | 학습된 월드 모델의 잠재 노이즈(latent noise) |
| **접촉 조작 성능** | 복잡한 접촉 시퀀스 발견 어려움 | 밀기(pushing)·집기(picking)에서 대폭 우위 |
| **정책 의존성** | 참조 궤적 또는 목표 특화 정책 필요 | 참조 궤적·목표 특화 정책 없이 오픈루프 목표 달성 |

## 주요 성능

- 6개 물리 도메인 전부에서 기존 최고 학습 동역학 베이스라인 대비 **예측 오차 평균 31% 감소**.
- 단일 Unified GPWM이 도메인별 특화 베이스라인을 대부분 상회하고, 2개 도메인에서는 자체 전문가(specialist) 모델마저 능가하며 미지 기하·물성·객체 수·롤아웃 지평선으로 일반화.

## 🔗 관련 문서

- [[wiki/Models/RL/World-Models-JEPA-LeWorldModel-Generative-Simulation.md]]
- [[wiki/Models/RL/LeWorldModel-JEPA-2026.md]]
- [[wiki/Agents/Robotics-and-VLA/Physical-Intelligence-pi0-Foundation-Model.md]]
- [[wiki/Agents/Robotics-and-VLA/NVIDIA-Physical-AI-GR00T-Cosmos-물리적-AI-혁신.md]]
