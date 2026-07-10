---
title: "Robotics-NVIDIA-Physical-AI-Google-SIMA2"
related_raw: ["[[wiki/Agents/Robotics-and-VLA/Robotics-NVIDIA-Physical-AI-Google-SIMA2.md]]"]
tags: ['wiki', 'agents_and_systems', 'robotics_&_physical_ai_(vla)']
type: "wiki"
status: "published"
last_updated: "2026-04-19"
---

# Robotics & Physical AI (VLA): NVIDIA Physical AI와 Google SIMA 2의 통합 (2026)

## 1. 개요 및 핵심 기술 트렌드
2026년 로봇 공학의 핵심은 **Embodied AI(체화된 인공지능)**의 실현입니다. AI가 단순히 가상 공간에서 정보를 처리하는 것을 넘어, 현실 세계의 물리 법칙을 이해하고 동작을 수행하는 VLA(Vision-Language-Action) 모델이 비약적으로 발전했습니다. NVIDIA의 대규모 데이터 생성 시스템과 Google의 추론 엔진 통합이 이 흐름의 중심에 있습니다.

## 2. 핵심 상세 내용

### 2.1 NVIDIA Physical AI Data Factory
NVIDIA는 GTC 2026에서 로보틱스를 위한 **'Physical AI Data Factory'**를 공개했습니다. 이는 로봇 학습에 필요한 방대한 데이터를 현실에서 수집하는 대신, 고정밀 물리 시뮬레이션 환경에서 생성하는 체계입니다.
- **Cosmos 파운데이션 모델:** 시뮬레이션 내에서 물리적 일관성이 있는 고품질 합성 데이터를 대량으로 생성하고 평가합니다.
- **Isaac GR00T N1.7:** 업그레이드된 로봇 제어 프레임워크로, 인간의 미세한 움직임을 실시간으로 모방하고 학습할 수 있는 능력을 갖췄습니다.
- **Vera Rubin 플랫폼:** 로봇 에이전트의 장기 기억과 실시간 계획 수립에 최적화된 새로운 하드웨어 아키텍처입니다.

### 2.2 Google SIMA 2: 가상 세계와 현실의 교량
Google의 범용 에이전트인 **SIMA 2(Scalable Instructable Multiworld Agent)**는 최신 **Gemini 2.5 Flash Lite**를 추론 엔진으로 탑재했습니다.
- **추론 기반 동작:** 단순히 명령어를 따라가는 것이 아니라, 사용자의 모호한 의도를 파악하고 이를 하위 작업(Sub-tasks)으로 분해하여 실행합니다.
- **범용성:** 학습하지 않은 새로운 가상 환경(MineDojo 등)이나 물리적 환경에서도 즉각적인 적응력을 보여주며, 멀티모달 제어(텍스트, 음성, 스케치)를 지원합니다.

### 2.3 Mentee Robotics 인수와 하드웨어의 진화
Mobileye가 Mentee Robotics를 인수하며 자율주행 기술과 휴머노이드 하드웨어의 결합을 가속화했습니다. 이는 자율주행에서 축적된 시각적 인지 능력이 로봇의 이동 및 작업 수행 능력과 통합되는 중요한 이정표가 되었습니다.

## 3. 원본 및 참조 URL
- https://nvidia.com/gtc-2026/physical-ai-keynote
- https://therobotreport.com/google-sima-2-gemini-integration
- https://mobileye.com/mentee-robotics-acquisition-2026
- https://arxiv.org/abs/2603.26262 (GLASS: 2D-3D Registration)

## 4. 워크스페이스 내 관련 링크
- [[wiki/Models/RL/LeWorldModel-JEPA-2026]]: JEPA 기반 세계 모델과 로봇의 상호작용.
- [[wiki/Models/RL/OpenAI-Sora-Shutdown-Robot-Pivot]]: Sora 기술을 활용한 로봇용 합성 데이터 팩토리(Synthetic Data Factory) 전략.
- Resources/Daily-Search-Topics: VLA 모델 및 Embodied AI 관련 연구 키워드.
- [[wiki/Business/2026년-로봇-공학-예측]]: 로봇 공학 분야의 연간 전망과 기술 로드맵.
