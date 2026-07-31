---
title: "π-shaped Continual Learning: SovereignAI의 대규모 지속 학습 방법론"
date: "2026-07-31"
last_updated: "2026-07-31"
updated: "2026-07-31"
related_raw: ["[[2026-07-31-sovereignai-pi-shaped-continual-learning.md]]"]
tags: ["Models", "SFT", "Continual-Learning", "Sovereign-AI", "Model-Adaptation"]
type: "wiki"
---

# π-shaped Continual Learning: SovereignAI의 대규모 지속 학습 방법론

**π-shaped (Pi-shaped) Continual Learning**은 2026년 7월 말 SovereignAI(톰슨 로이터 AI 연구 책임자 조나단 리차드 슈바르츠 주도)가 제안한 최신 지속 학습(Continual Learning) 및 모델 파인튜닝 기법입니다. 

이 기법은 이미 학습된 오픈소스 거대 언어 모델(Base Model)의 가중치를 파괴하지 않고 특정 전문 도메인(예: 법률, 금융, 의학 등)에 최적화된 프론티어(Frontier) 성능 수준의 모델로 초저비용으로 진화시키기 위한 특화 방법론입니다.

## 1. 아키텍처 및 작동 원리

기존의 지속 학습은 새 도메인 데이터를 주입할 때 과거의 일반 지식을 상실하는 **치명적 망각(Catastrophic Forgetting)** 문제와, 이를 막기 위한 정규화 연산 때문에 학습 비용이 치솟는 한계를 가집니다. π-shaped Continual Learning은 이를 다음과 같이 극복합니다:

- **이중 다리 아키텍처 (Double-legged / Pi-shaped Structure)**:
  - 인간의 'T자형 인재(한 분야 전문성 + 넓은 교양)'를 넘어선 'π자형 인재(두 개의 핵심 전문 분야)' 개념에서 따온 구조입니다.
  - 베이스 모델 위에 **두 가지 서로 다른 도메인 전문 어댑터(Legs)**가 지속적이고 독립적으로 발달할 수 있도록 뉴럴 네트워크 경로를 제어합니다.
  - 한쪽 다리가 새로운 전문 지식을 흡수하는 동안, 다른 한쪽 다리는 기존의 일반화 지식 및 정렬(Alignment) 데이터를 보존하고, 이 두 다리를 상위 게이트웨이(Bridge)가 토큰별로 조율하여 믹싱합니다.
- **고효율 데이터 큐레이션과의 결합**:
  - **DatologyAI**와의 협업을 통해 무작위 샘플링 대신 고도의 의미 필터링을 거친 상위 10%의 고품질 골든 데이터셋만을 엄선해 훈련에 사용합니다.
  - 이를 통해 컴퓨팅 비용을 극적으로 차단합니다.

## 2. 실증 성과: Thomson-1-Large

- **사례**: Qwen3.5-397B(오픈웨이트 MoE) 모델을 베이스로 삼고, π-shaped Continual Learning 기법을 적용하여 **Thomson-1-Large** 모델을 구축했습니다.
- **비용**: 397B 초대형 모델의 지속 학습 R&D 및 훈련 전 과정을 단 **$450,000 (약 6억 원)의 컴퓨팅 예산**으로 완수하여 프론티어 급 성능(Claude 4.8 Opus 수준)에 도달시켰습니다.
- **참여 파트너**: Thomson Reuters, DatologyAI, Lambda (인프라), Together Compute, Imperial College London, TRI Fair Lab.

## 🔗 연결된 문서
- [[wiki/Models/SFT/000_SFT-MOC.md]]
- [[wiki/Models/SFT/Fine-Tuning.md]]
- [[wiki/Business/Trends/Sovereign-AI-Korea-Upstage.md]]
