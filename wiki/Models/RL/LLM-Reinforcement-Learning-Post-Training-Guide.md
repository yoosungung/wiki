---
title: LLM 강화학습(RL) 포스트 트레이닝 및 최신 알고리즘 가이드
tags: [reinforcement_learning, llm_training, post_training, grpo]
last_updated: "2026-09-04"
updated: "2026-09-04"
related_raw: ["[[2026-08-26-reinforcement_learning_for_llms_complete_guide.md]]", "[[2026-09-04-msr-tailsft-filtered-fine-tuning-post-training.md]]"]
---

# 🤖 LLM 강화학습(RL) 포스트 트레이닝 및 최신 알고리즘 가이드

## 1. LLM 포스트 트레이닝에서의 RL 개요
과거의 SFT(Supervised Fine-Tuning)가 인간의 결과물을 흉내 내는 정적 학습 방식이었다면, 강화학습(RL)은 LLM이 복잡한 추론 문제를 해결하기 위한 '행동 체인(Reasoning chain)'을 스스로 평가하며 발전시키는 동적 정렬 방식입니다. 특히 수학, 코딩, 복합적 리서치처럼 검증 가능한 보상(Verifiable Rewards)을 정의하기 쉬운 태스크에서 비약적인 성능 향상을 보이고 있습니다.

## 2. PPO vs GRPO 아키텍처 비교

### 1) PPO (Proximal Policy Optimization)
- **구조**: Actor (행동 모델), Reference (KL 발산 앵커 모델), Critic (가치 평가 모델), Reward (보상 평가 모델) 4개 모델이 필요.
- **단점**: 학습 중 상태 가치를 산출하기 위해 Critic 모델을 계속 트레이닝해야 하므로, LLM 스케일 학습 시 엄청난 VRAM 오버헤드가 발생함 (배치 사이즈 축소 및 학습 속도 저하 유발).

### 2) GRPO (Group Relative Policy Optimization)
- **개념**: Critic 네트워크를 완벽히 배제함.
- **동작 원리**: 단일 프롬프트에 대해 LLM(Actor)이 그룹 크기 $G$(보통 8~16개)만큼의 답변 후보들을 생성하게 한 뒤, 각 답변의 보상을 계산하여 그 그룹의 평균($\mu$)과 표준편차($\sigma$)로 Advantage($A$)를 추정함.
  $$A_i = rac{R_i - \mu}{\sigma}$$
- **이점**: 가치 네트워크를 위한 추가적인 GPU 메모리 및 가중치 업데이트 연산이 완전히 생략되어 학습 성능 및 토큰 소진 효율이 극대화됨.

## 3. 최신 GRPO++ 개량 기법 (2025~2026 연구 트렌드)

| 알고리즘 | 해결하는 병목 / 한계 | 핵심 메커니즘 및 수식적 아이디어 |
| :--- | :--- | :--- |
| **GSPO** | 긴 추론 및 MoE 모델 학습 시 토큰 단위 클리핑 분산 문제 | 토큰 대신 시퀀스 전체 단위의 기하평균 중요도 비율(clip sequence probability)을 적용해 긴 생성물의 최적화 수렴 유도. |
| **DAPO** | RL 트레이닝 중 엔트로피 급락 및 모드 붕괴(Mode Collapse) | 비대칭 상한 클리핑(clip higher threshold)으로 엔트로피 붕괴를 강하게 방어하고, 유효 답변 후보만 동적 샘플링. |
| **Dr. GRPO** | 난이도 편차에 의한 분모 왜곡 및 답변 길이 편향(length bias) | 길이 페널티 보정과 난이도별 표준편차 편향을 방지하는 고정 분모 스케일링 필터 탑재. |
| **TIS** | 인퍼런스 엔진(vLLM/SGLang)과 트레이닝 프레임워크(DeepSpeed/verl) 간 미세 토큰 확률 오차 | 인퍼런스 엔진에서 계산된 토큰 로그 확률값과 트레이닝 엔진 가중치 간의 격차를 중요도 비(TIS 가중치)로 실시간 보상. |
| **CISPO** | MiniMax-M1 계열 초장기 추론 학습 시 자기반성(Reflection) 토큰 누락 현상 | 에이전트의 중간 사고/반성 단계 토큰에 stop-gradient를 걸어 보상 역전파 시 유의미한 행동 결정만 갱신. |

## 4. 실전 엔지니어링 구현 고려사항
- **Verifiable Reward API**: 코드 테스트 통과 여부 및 정규식 기반 정답 추출(`Math-Verify` 등)을 통한 결정론적 보상 결합.
- **Engine Co-design**: 학습 가속을 위해 롤아웃 생성을 고속 인퍼런스 엔진(vLLM)에 위임하고, 손실 함수 역전파 및 가중치 업데이트는 DeepSpeed/FSDP에 밀착 결합하는 아키텍처 구축 필수.

## 5. SFT-RL 파이프라인 연계: TailSFT를 통한 탐색 커버리지(pass@k) 극대화
- **엔트로피 붕괴 방지**: 표준 SFT 단계에서 쉬운 예제에 과도하게 손실을 낮추면(Over-fitting) 확률 분포가 특정 정답으로 쏠려, 후속 GRPO 롤아웃 시 16~32개 시도가 모두 동일한 외길 오답으로 귀결되어 보상 0의 늪에 빠집니다.
- **Offset Filtering 해결책**: 베이스 모델 대비 손실 개선율을 기준으로 쉬운 데이터를 제외하고 꼬리(Tail) 영역 난제에만 그래디언트를 집중시키는 [[wiki/Models/SFT/TailSFT-Filtered-Fine-Tuning.md|TailSFT]]를 SFT 단계에 적용함으로써, 후속 GRPO의 pass@16 커버리지를 대폭 보존하고 최종 추론 성능을 끌어올릴 수 있습니다.

---
## 🔗 관련 문서
- [[wiki/Models/SFT/TailSFT-Filtered-Fine-Tuning.md|TailSFT 필터링 미세조정]]
- [[wiki/Models/RL/GRPO-Algorithm-Definition.md|GRPO 알고리즘 정의]]
- [[wiki/Models/RL/DeepSeek-R1-GRPO-Implementation.md|DeepSeek-R1 GRPO 구현]]
- [[wiki/Models/RL/000_RL-MOC.md|RL MOC]]
