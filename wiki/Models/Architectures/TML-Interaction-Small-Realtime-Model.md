---
title: "TML-Interaction-Small: 띵킹 머신즈 랩의 차세대 실시간 상호작용 모델"
related_raw: ["[[realtime model.md]]"]
tags: ["Models", "Architectures", "Real-time", "Multi-modal", "TML", "Mira_Murati"]
type: "wiki"
status: "published"
last_updated: "2026-05-15"
updated: "2026-05-15"
---

# TML-Interaction-Small: 실시간 상호작용의 패러다임 시프트

## 1. 개요
**띵킹 머신즈 랩(Thinking Machines Lab, TML)**이 2026년 5월에 공개한 차세대 실시간 모델입니다. 전 OpenAI CTO 미라 무라티(Mira Murati)가 주도하여 개발되었으며, 기존 LLM의 지연 시간 문제를 해결하고 인간 수준의 자연스러운 실시간 대화를 지향합니다.

## 2. 주요 기술적 특징

### 1) Full-Duplex (전이중 통신) 기반 상호작용
기존 AI가 사용자의 발화가 끝날 때까지 기다리는 '무전기(Half-Duplex)' 방식이었다면, TML-Interaction-Small은 **실시간 동시 대화(Full-Duplex)**가 가능합니다.
- **실시간 개입**: 대화 도중 AI가 추임새를 넣거나, 사용자가 중간에 말을 끊어도 맥락을 유지하며 자연스럽게 대응합니다.
- **초저지연 응답**: 약 400ms(0.4초) 미만의 응답 지연 시간을 기록 (GPT-Realtime 2.0의 1.1초 대비 대폭 향상).

### 2) 하이브리드 이중 뇌 아키텍처 (Foreground & Background)
모델을 역할에 따라 두 개의 시스템으로 분리하여 효율성과 성능을 동시에 확보했습니다.
- **Foreground (전경) 모델**: 276B 규모의 MoE(Mixture-of-Experts) 아키텍처. 실시간 대화 흐름, 표정 인식, 음성 톤 감지 등 **상호작용**에만 전담합니다.
- **Background (배경) 모델**: 복잡한 추론, 데이터 검색(RAG), 도구 사용 등 **연산 집약적 작업**을 비동기적으로 처리하여 대화의 끊김을 방지합니다.

### 3) 네이티브 멀티모달 인지 (Early Fusion)
외부 TTS/STT 엔진을 거치지 않고 모델이 직접 오디오 신호(dMel)와 비디오 프레임을 처리합니다.
- **시각적 민감도**: 카메라를 통해 사용자의 자세, 표정 변화를 실시간으로 인지하고 피드백을 제공합니다 (예: 자세 교정 제안).

## 3. 시장 임팩트 및 전망
미라 무라티의 리더십 아래 개발된 이 모델은 AI가 단순히 텍스트를 생성하는 도구를 넘어, 인간과 실시간으로 협업하는 '동료'로서의 역할을 수행하게 할 것으로 기대됩니다. 현재 리서치 프리뷰 단계이며, 2026년 하반기 정식 출시 예정입니다.

## 관련 문서
- [[wiki/Models/Architectures/MoE 모델 분석.md|MoE (Mixture-of-Experts) 모델 분석]]
- [[wiki/Models/Architectures/000_Architectures-MOC.md|모델 아키텍처 MOC]]
- [[wiki/Models/Reasoning-and-Cognition/000_Reasoning-and-Cognition-MOC.md|추론 및 인지 MOC]]
