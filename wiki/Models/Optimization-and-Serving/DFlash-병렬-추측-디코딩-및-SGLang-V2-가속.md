---
related_raw: ["[[2026-06-25-LMSYS_DFlash_Speculative_Decoding_Spec_V2.md]]"]
tags: ["#wiki", "Speculative-Decoding", "DFlash", "SGLang-V2", "KV-Injection", "Overlap-Scheduler"]
---

# DFlash 병렬 추측 디코딩 및 SGLang V2 가속 기술

거대 언어 모델(LLM)의 autoregressive 디코딩은 낮은 산술 강도(arithmetic intensity)로 인해 메모리 대역폭 병목을 겪습니다. 이를 타개하기 위해 SGLang 엔진에 네이티브 도입된 **DFlash** 및 **Spec V2** 엔진은 하드웨어 병렬 연산 효율을 극대화하여 추론 처리량과 지연 시간을 비약적으로 개선한 차세대 투측 디코딩 기술입니다.

## 1. DFlash의 핵심 동작 원리
기존의 추측 디코딩(예: EAGLE, MTP 등)이 드래프트 모델 내에서도 순차적으로 토큰을 하나씩 생성했던 것과 달리, DFlash는 다음 두 가지 돌파구를 적용했습니다:
1. **블록 디퓨전 (Block Diffusion Drafting)**: 드래프트 토큰군을 순차 생성하지 않고, **한 번의 GPU 패스로 한 블록(8~16개 토큰) 전체를 병렬 생성**하는 블록 디퓨전 드래프터 모델을 채택하여 하드웨어(GPU/TPU) 연산 친화적인 구조를 확립했습니다.
2. **KV Injection (KV 캐시 주입)**: 타겟 모델의 최종 레이어 히든 텐서 표현을 드래프트 모델의 KV cache에 직접 주입(injection)합니다. 드래프트 모델이 이전 문맥 전체를 처음부터 무겁게 모델링하는 오버헤드를 건너뛰고 오직 미래 블록 예측에만 집중하게 함으로써, 극도로 가벼운 구조(예: 350M 등)로도 높은 드래프트 수락률(Acceptance Length)을 달성합니다.

## 2. SGLang Spec V2 오버랩 스케줄러 (Overlap Scheduler)
기본적인 드래프팅이 빨라도 호스트(CPU)와 가속기(GPU) 간의 빈번한 동기화 신호 제어가 병목으로 작용합니다. SGLang의 Spec V2 엔진은 이를 차단하기 위해 **오버랩 스케줄러**를 설계했습니다:
- **실행 오버랩**: GPU가 현재 배치를 디코드 추론하는 동안, 호스트(CPU)는 직전 배치(N-1)의 토큰 분석(stop token 검출 등)과 다음 배치(N+1)의 KV 캐시 메모리 할당 작업을 병렬로 오버랩 수행합니다.
- **성공률**: 호스트-디바이스 동기화가 원천 차단됨으로써, 단일 B200 인프라에서 Qwen 모델의 서빙 성능이 **추가로 33% 이상 (11.4 ktok/s -> 15.3 ktok/s)** 향상되는 실질적 가속 효과를 달성했습니다.
- Qwen3.5 397B-A17B와 결합 시 baseline 대비 4.3배, 네이티브 MTP 대비 1.5배의 throughput 향상을 벤치마크했습니다.

## 🔗 연결된 문서
- [[wiki/Models/Optimization-and-Serving/로컬-AI-하드웨어-지형도-및-대역폭-병목-분석.md]] — 하드웨어 물리 대역폭 병목.
- [[wiki/Models/Reasoning-and-Cognition/NextLat-잠재-공간-세계-모델-2026.md]] — 잠재 공간 수준에서 자가 추측 디코딩을 수행하는 NextLat 연구.
