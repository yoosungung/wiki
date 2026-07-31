---
title: "Kimi K3: 2.8조 파라미터 희소 혼합 전문가(Sparse MoE) 모델 아키텍처"
related_raw: ["[[2026-07-24-kimi-k3-mixture-of-experts.md]]", "[[raw/2026-07-28-kimi_delta_attention_efficient_attention_architecture.md]]", "[[2026-07-31-kimi-k3-raises-bar-open-source-moe.md]]", "[[2026-07-31-kimi-k3-local-inference-unsloth.md]]"]
tags: ["Models", "Architectures", "MoE", "Kimi", "Moonshot-AI", "Long-Context"]
type: "wiki"
status: "published"
last_updated: "2026-07-31"
updated: "2026-07-31"
---

# Kimi K3: 2.8조 파라미터 희소 혼합 전문가(Sparse MoE) 모델 아키텍처

## 1. 개요
**Kimi K3**는 중국의 AI 스타트업인 Moonshot AI가 2026년 7월에 발표한 초대형 플래그십 인공지능 모델입니다. 총 **2.8조 파라미터(2.8 Trillion Parameters)** 규모의 거대한 스파스 혼합 전문가(Sparse Mixture-of-Experts, MoE) 구조로 이루어져 있으며, 연산 효율성을 극대화하기 위해 선형 어텐션(Linear Attention)과 전통적 어텐션 기법의 하이브리드 혁신을 이루어 냈습니다.

## 2. 핵심 아키텍처 혁신

### 1) Kimi Delta Attention (KDA) 및 AttnRes (Attention Residuals)
초장문(Long-context) 처리 시 기존의 표준 Softmax Attention은 매 토큰 생성 시마다 이전 KV 캐시 전체를 다시 탐색해야 하므로 $O(N^2)$ 연산 복잡도와 심각한 메모리 병목을 유발합니다. Kimi K3는 이를 극복하기 위해 **KDA**와 **AttnRes**의 하이브리드 어텐션 설계를 도입하였습니다:
- **Kimi Delta Attention (KDA)**: 
  - **기술적 기반**: KDA는 **Gated DeltaNet(arXiv:2510.26692)** 구조를 활용한 선형 어텐션(Linear Attention) 아키텍처입니다.
  - **작동 원리**: 입력 히스토리를 고정된 크기의 상태(State) 매트릭스 전이 행렬로 상시 압축하며, 새로운 정보가 들어올 때 캐시를 append하는 대신 고정 상태 메모리에 delta-correction을 통해 덮어쓰기(overwrite)를 수행하여 디코딩 속도를 비약적으로 향상시킵니다.
  - **KV 캐시 감소**: 일반 어텐션 대비 **KV 캐시 VRAM 점유율을 최대 75% 절감**하여 constant-cost decoding을 실현하였습니다.
- **하이브리드 레이어 패턴**: Kimi K3는 모든 레이어에 KDA를 쓰지 않고, **3개 레이어는 KDA**를 적용해 연산 비용을 축소하고, **1개 레이어는 Gated MLA(Multi-Head Latent Attention)**를 적용해 글로벌 지식 회상(Recall) 정밀도를 완벽히 보장하는 3:1 하이브리드 패턴을 활용합니다.
- **AttnRes (Attention Residuals)**: 선형 어텐션 과정에서 발생하는 정보의 점진적 감쇠 및 정보 유실을 보정하기 위해, 고정밀 어텐션 스코어의 핵심 성분만 잔차 연결(Residual Connection) 구조로 우회 보완시킵니다.
- **생태계 지원**: Moonshot AI는 높은 연산 가속을 위해 GPU용 커널인 **FlashKDA**를 오픈소스로 공개하였으며, serving 프레임워크인 **vLLM**에서도 공식 구동이 지원됩니다.

### 2) 100만 토큰 (1M Context Window) 컨텍스트 지원
Kimi K3는 Delta Attention 스택 덕분에 모델 구동 시 그래픽 메모리(VRAM) 병목을 회피하여 **최대 1,000,000 토큰(1M tokens)**의 입력 범위를 온전히 지원합니다. 이는 책 여러 권 분량의 자료나 전체 코드베이스 프로젝트 리포지토리를 한 번에 주입하여 즉각적인 다중 파일 검색 및 추론을 가능하게 합니다.

## 3. 타깃 에이전트 성능 최적화
Moonshot AI는 Kimi K3를 단순 질의응답을 넘어 **장기 계획(Long-horizon Planning)과 코드베이스 자율 탐색(Repository Navigation)에 특화**되도록 사후 포스트 트레이닝(Post-training)을 진행했습니다.
- **도구 호출 및 오케스트레이션:** 복잡한 개발 시나리오에서 수십 단계의 API 호출 및 파일 읽기/쓰기를 오류 없이 자율적으로 수행하는 멀티 에이전트 시스템(MAS)의 조율자(Orchestrator) 모델로 활용하기에 이상적입니다.

## 4. 로컬 실행 및 미세조정 (Local Inference & Fine-tuning)
- **Unsloth 연동 가속**: **Unsloth** 프레임워크의 최적화 Triton 커널을 기반으로 Kimi K3 MoE 모델의 로컬 미세조정(Fine-tuning) 및 추론이 지원됩니다. 이를 통해 학습 속도가 최대 2.5배 가속되며 메모리 사용량이 극적으로 절감됩니다.
- **양자화 배포**: 허깅페이스(Hugging Face)를 통해 배포된 4-bit (INT4) 및 8-bit (FP8) 양자화 가중치를 활용하여 단일 또는 듀얼 GPU 워크스테이션 환경에서도 100만 토큰 컨텍스트를 안정적으로 로드하여 가동할 수 있습니다.

## 관련 문서
- [[wiki/Models/Architectures/000_Architectures-MOC.md|모델 아키텍처 MOC]]
- [[wiki/Models/Reasoning-and-Cognition/000_Reasoning-and-Cognition-MOC.md|추론 및 인지 아키텍처 MOC]]
- [[wiki/Agents/Coding-and-Engineering/000_Coding-and-Engineering-MOC.md|에이전틱 코딩 및 엔지니어링 MOC]]
