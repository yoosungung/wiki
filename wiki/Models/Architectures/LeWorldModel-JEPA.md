---
title: "LeWorldModel (LeWM): 안정적인 엔드 투 엔드 JEPA 세계 모델"
related_raw: ["[[#leworldmodel #세계모델 #worldmodels #인공지능 #artificialintelligence #jepa #ai #지능 #학습 | Suk Hyun K..md]]"]
tags: ["Models", "Architectures", "JEPA", "World_Models", "LeWorldModel", "SIGReg"]
type: "wiki"
status: "published"
last_updated: "2026-04-21"
updated: "2026-04-21"
---

# LeWorldModel (LeWM): 안정적인 엔드 투 엔드 JEPA 세계 모델

## 1. 개요
LeWorldModel(LeWM)은 별도의 휴리스틱이나 사전 학습된 인코더 없이 원본 픽셀로부터 직접 학습하는 최초의 **엔드 투 엔드(End-to-End) JEPA(Joint Embedding Predictive Architecture)** 세계 모델입니다. 기존 JEPA 모델들이 표현 붕괴(Representation Collapse)를 막기 위해 복잡한 손실 함수나 트릭에 의존했던 것과 달리, LeWM은 구조적 단순화와 안정성을 극대화했습니다.

## 2. 핵심 기술: SIGReg (Sketched-Isotropic-Gaussian Regularizer)
LeWM의 안정성을 보장하는 핵심 정규화 기법입니다.
- **역할**: 잠재 임베딩(Latent Embedding)이 등방성 가우시안 분포를 따르도록 강제하여 표현 붕괴를 방지하고 특징의 다양성을 촉진합니다.
- **단순성**: 기존 PLDM 등이 6개의 하이퍼파라미터를 조정해야 했던 것과 달리, LeWM은 SIGReg를 통해 조정이 필요한 하이퍼파라미터를 단 하나로 줄였습니다.
- **손실 함수**: 다음 단계 임베딩 예측 손실과 SIGReg 정규화 항이라는 단 두 개의 손실 항만 사용합니다.

## 3. 주요 특징 및 성능
- **효율성**: 1,500만 개의 파라미터를 가진 모델로, 단일 GPU에서 몇 시간 만에 학습이 가능합니다.
- **속도**: 추론 단계에서의 계획(Planning) 속도가 파운데이션 모델 기반 세계 모델보다 **48~50배** 빠릅니다.
- **물리적 이해도**: 별도의 이미지 재구성 손실 없이도 위치, 각도 등 물리적 양을 정확히 추출하며, 비물리적 사건 발생 시 높은 '놀람(Surprise)' 수치를 나타내며 이를 감지합니다.
- **경로 직선화 (Path Straightening)**: 학습 과정에서 잠재 궤적이 스스로 매끄럽고 직선에 가깝게 정렬되는 현상이 창발적으로 나타납니다. 이는 뇌과학에서 관찰되는 고등 지능의 특성과 유사합니다.

## 4. 시사점
LeWorldModel은 단순한 구조가 강력한 성능과 안정성을 제공할 수 있음을 입증했습니다. 실시간 제어가 가능하면서도 물리적 이해도가 높은 효율적인 세계 모델의 새로운 표준을 제시하며, 향후 자율적 지능 구현을 위한 핵심 아키텍처로 주목받고 있습니다.

## 관련 문서
- [[wiki/Models/Architectures/Transformer 모델의 구조와 작동 원리를 깊이 이해.md|Transformer 아키텍처 이해]]
- [[wiki/Models/Reasoning-and-Cognition/000_Reasoning-and-Cognition-MOC.md|추론 및 인지 MOC]]
