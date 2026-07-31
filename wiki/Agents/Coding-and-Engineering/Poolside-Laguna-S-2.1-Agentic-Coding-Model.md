---
title: "Poolside Laguna S 2.1: 에이전틱 코딩 특화 모델 아키텍처"
date: "2026-07-31"
last_updated: "2026-07-31"
updated: "2026-07-31"
related_raw: ["[[2026-07-31-poolside-laguna-s-2.1-coding-model.md]]"]
tags: ["Agents", "Coding-and-Engineering", "Poolside-AI", "Laguna", "Coding-Models", "Open-Weights"]
type: "wiki"
---

# Poolside Laguna S 2.1: 에이전틱 코딩 특화 모델 아키텍처

**Laguna S 2.1**은 Poolside AI(설립자 Eiso Kant 및 Jason Warner)가 2026년 7월 21일에 릴리스한 에이전틱 소프트웨어 엔지니어링(Agentic Software Engineering) 개발용 오픈웨이트 대규모 언어 모델입니다. 

기존의 단순 코드 완성(Code-completion)을 넘어, 오랜 시간 자율적으로 작동하는 소프트웨어 개발 에이전트(Software Agents)가 스스로 계획을 수립하고, 도구를 실행하며, 오류를 교정하는 일련의 워크플로우에 특화되도록 조율되었습니다.

## 1. 주요 사양 및 아키텍처 특징

- **스파스 MoE 아키텍처 (Sparse MoE)**:
  - 총 매개변수: **1,180억 파라미터 (118B total parameters)**.
  - 활성 매개변수: 토큰당 **8B 파라미터가 활성화**되어 높은 연산 속도와 낮은 서빙 비용을 확보합니다.
- **초대형 컨텍스트 지원**: 최대 **100만 토큰 (1M context)**을 지원하여 에이전트가 단독 구동 시에도 복잡한 레포지토리 전역 및 멀티 파일 소스코드를 안정적으로 수용하고 분석할 수 있습니다.
- **다중 추론 모드 (Dual Reasoning Mode)**:
  - **생각 모드 (Thinking Mode)**: 복잡한 로직 및 다단계 버그 추적 시 심층 추론을 수행합니다.
  - **비생각 모드 (No-thinking Mode)**: 단순 단순 코드 작성이나 빠른 단순 도구 실행 시 신속하게 응답합니다.
- **로컬 실행 및 배포 다양성**: BF16, FP8, INT4, NVFP4 등 다양한 정밀도 포맷이 오픈소스로 공개되어, 값비싼 클라우드 API 대신 사내 소스코드 보안을 위해 기업 로컬 하드웨어 인프라 상에서 통제 구동하기 용이합니다.

## 2. 에이전트 개발에서의 의의

- **지속성**: Poolside 측은 이 모델이 최대 24시간 동안 인간의 중간 개입 없이 복잡한 에이전트 스캐폴딩 파이프라인 상에서 자율 루프(Self-Correction)를 유지하며 과업을 완수할 수 있는 지속 연산 안정성을 제공한다고 밝히고 있습니다.

## 🔗 연결된 문서
- [[wiki/Agents/Coding-and-Engineering/000_Coding-and-Engineering-MOC.md]]
- [[wiki/Agents/Coding-and-Engineering/Claude Code의 Task 변화와 AI-native 엔지니어의 조건.md]]
- [[wiki/Models/Architectures/000_Architectures-MOC.md]]
