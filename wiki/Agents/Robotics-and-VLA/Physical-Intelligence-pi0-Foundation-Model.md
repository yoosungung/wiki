---
title: "Physical-Intelligence-pi0-Foundation-Model"
related_raw: ["[[wiki/Agents/Robotics-and-VLA/Physical-Intelligence-pi0-Foundation-Model.md]]"]
tags: ['wiki', 'agents_and_systems', 'robotics_&_physical_ai_(vla)']
type: "wiki"
status: "published"
last_updated: "2026-04-19"
---

# Physical Intelligence π₀ (pi-zero)

**출처**: [원본 링크](https://www.physicalintelligence.company/blog/pi0)
**날짜:** 2026-04-05
**태그:** #Robotics #Embodied-AI #VLA #Physical-Intelligence #Foundation-Model

## 요약 (Summary)
Physical Intelligence가 개발한 **π₀(pi-zero)**는 '로봇을 위한 ChatGPT'를 목표로 하는 범용 로봇 파운데이션 모델입니다. 8종 이상의 다양한 로봇 플랫폼과 수많은 작업 데이터를 동시에 학습하여, 물리적 세계에서 정교한 상호작용이 가능한 '물리적 지능(Physical Intelligence)'을 구현했습니다.

## 주요 기술적 특징 (Technical Highlights)
1.  **범용 로봇 정책 (Generalist Robot Policy)**:
    *   특정 작업에 국한되지 않고 빨래 개기, 설거지, 조립 등 다양한 물리적 업무를 단일 모델로 수행.
2.  **VLA + Flow Matching 아키텍처**:
    *   시각-언어 모델(VLM) 기반의 VLA 모델에 확산 모델의 변형인 'Flow Matching' 기법을 적용하여 초당 50회의 고주파수 연속 모터 명령 생성.
3.  **정교한 조작 능력**:
    *   옷감과 같은 변형 가능한 물체(Deformable objects) 조작 및 다단계 복잡 작업에서 기존 모델(OpenVLA 등) 대비 압도적 성능.
4.  **사후 학습 (Post-training)**:
    *   LLM의 정렬 과정과 유사하게 고품질 데이터를 통한 미세 조정을 거쳐 환경 변화에 대한 대응력 강화.

## 기존 노트와 링크 (Related Notes)
*   [[wiki/Agents/Robotics-and-VLA/Google-RT-3-Open-Source-Robotics]]
*   [[wiki/Agents/Robotics-and-VLA/Nvidia-Cosmos-VLA-2026]]
*   Resources/02_Agents_Systems/LLM-Agent/Frameworks-Trends/Self-Evolving-Agents/Self-Evolving-Agents
