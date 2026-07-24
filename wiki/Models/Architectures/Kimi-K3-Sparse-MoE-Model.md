---
title: "Kimi K3: 2.8조 파라미터 희소 혼합 전문가(Sparse MoE) 모델 아키텍처"
related_raw: ["[[2026-07-24-kimi-k3-mixture-of-experts.md]]"]
tags: ["Models", "Architectures", "MoE", "Kimi", "Moonshot-AI", "Long-Context"]
type: "wiki"
status: "published"
last_updated: "2026-07-24"
updated: "2026-07-24"
---

# Kimi K3: 2.8조 파라미터 희소 혼합 전문가(Sparse MoE) 모델 아키텍처

## 1. 개요
**Kimi K3**는 중국의 AI 스타트업인 Moonshot AI가 2026년 7월에 발표한 초대형 플래그십 인공지능 모델입니다. 총 **2.8조 파라미터(2.8 Trillion Parameters)** 규모의 거대한 스파스 혼합 전문가(Sparse Mixture-of-Experts, MoE) 구조로 이루어져 있으며, 연산 효율성을 극대화하기 위해 선형 어텐션(Linear Attention)과 전통적 어텐션 기법의 하이브리드 혁신을 이루어 냈습니다.

## 2. 핵심 아키텍처 혁신

### 1) Kimi Delta Attention 및 AttnRes (Attention Residuals)
초장문(Long-context) 처리 시 기존의 표준 Dot-Product Attention은 시퀀스 길이에 따라 연산 복잡도와 메모리 요구량이 제곱($O(N^2)$)으로 증가하는 치명적인 한계를 가집니다. Kimi K3는 이를 해결하기 위해 두 가지 핵심 메커니즘을 적용했습니다:
- **Kimi Delta Attention:** 입력 토큰 간의 연산을 선형 시간 복잡도($O(N)$)로 압축하는 고유한 선형 어텐션 방식입니다.
- **AttnRes (Attention Residuals):** 선형 어텐션 과정에서 발생하는 정보 유실 및 로컬/디테일 정보의 붕괴를 보정하기 위해, 잔차 연결(Residual Connection) 형태로 고정밀 어텐션 스코어의 핵심 성분만 우회 결합시킵니다. 이로써 연산 속도는 대폭 늘리면서도 초장문 추론 성능 저하를 차단합니다.

### 2) 100만 토큰 (1M Context Window) 컨텍스트 지원
Kimi K3는 Delta Attention 스택 덕분에 모델 구동 시 그래픽 메모리(VRAM) 병목을 회피하여 **최대 1,000,000 토큰(1M tokens)**의 입력 범위를 온전히 지원합니다. 이는 책 여러 권 분량의 자료나 전체 코드베이스 프로젝트 리포지토리를 한 번에 주입하여 즉각적인 다중 파일 검색 및 추론을 가능하게 합니다.

## 3. 타깃 에이전트 성능 최적화
Moonshot AI는 Kimi K3를 단순 질의응답을 넘어 **장기 계획(Long-horizon Planning)과 코드베이스 자율 탐색(Repository Navigation)에 특화**되도록 사후 포스트 트레이닝(Post-training)을 진행했습니다.
- **도구 호출 및 오케스트레이션:** 복잡한 개발 시나리오에서 수십 단계의 API 호출 및 파일 읽기/쓰기를 오류 없이 자율적으로 수행하는 멀티 에이전트 시스템(MAS)의 조율자(Orchestrator) 모델로 활용하기에 이상적입니다.

## 관련 문서
- [[wiki/Models/Architectures/000_Architectures-MOC.md|모델 아키텍처 MOC]]
- [[wiki/Models/Reasoning-and-Cognition/000_Reasoning-and-Cognition-MOC.md|추론 및 인지 아키텍처 MOC]]
- [[wiki/Agents/Coding-and-Engineering/000_Coding-and-Engineering-MOC.md|에이전틱 코딩 및 엔지니어링 MOC]]
