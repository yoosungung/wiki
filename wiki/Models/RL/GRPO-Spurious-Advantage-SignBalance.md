---
title: "GRPO의 거짓 이득(Spurious Advantage) 결함 및 SignBalance 알고리즘"
last_updated: "2026-09-20"
updated: "2026-09-20"
related_raw: ["[[2026-09-20-grpo-spurious-advantage-signbalance.md]]"]
tags: ["wiki", "Models", "RL", "GRPO", "SignBalance", "Reinforcement-Learning", "Reasoning"]
type: "wiki"
status: "published"
---

# GRPO의 거짓 이득(Spurious Advantage) 결함 및 SignBalance 알고리즘

## 1. 개요
**GRPO (Group Relative Policy Optimization)**는 Critic(가치 평가) 네트워크를 제거하고 동일 프롬프트에서 생성된 그룹($G$개) 답변 간의 보상 평균과 표준 편차를 통해 이득(Advantage)을 산출함으로써 현대 추론 모델 훈련의 표준으로 자리 잡았습니다.

그러나 로체스터 공과대(RIT)와 Adobe Research 연구진(Wang et al., 2026, [arXiv:2609.04063](https://arxiv.org/abs/2609.04063))은 GRPO의 정규화 수식에 **거짓 이득(Spurious Advantage)**을 유발하는 치명적인 구조적 맹점이 존재함을 증명했습니다. 즉, 문제를 정석적으로 추론하여 맞힌 경우보다, 아무런 근거 없이 찍어서 우연히 맞힌 요행 궤적에 최대 4배에 가까운 '폭탄 보상'이 부여되는 역설입니다.

---

## 2. GRPO의 거짓 이득(Spurious Advantage) 역설

### 2.1 그룹 정규화 수식과 계산 역설
GRPO에서 그룹 내 $i$번째 롤아웃의 이득 $A_i$는 다음과 같이 계산됩니다:

$$A_i = \frac{R_i - \text{mean}(R)}{\text{std}(R)}$$

여기서 $G=16$개의 롤아웃을 샘플링했을 때 정답($R=1$)과 오답($R=0$)의 비율에 따른 이득 변화를 비교해 보면 심각한 왜곡이 드러납니다:

1. **정상 추론 시나리오 (16개 중 8개 정답)**:
   - $\text{mean}(R) = 0.5$, $\text{std}(R) = 0.5$
   - 정답 궤적의 이득: $A_{\text{correct}} = \frac{1.0 - 0.5}{0.5} = \mathbf{+1.00}$
2. **요행 찍기 시나리오 (16개 중 15개 오답, 우연히 1개 정답)**:
   - $\text{mean}(R) = \frac{1}{16} = 0.0625$, $\text{std}(R) = \sqrt{\frac{15}{256}} \approx 0.242$
   - 우연한 정답 궤적의 이득: $A_{\text{lucky}} = \frac{1.0 - 0.0625}{0.242} \approx \mathbf{+3.87}$

원래 GRPO 설계 의도는 "희귀한 성공일수록 고난도 문제를 해결한 것이므로 더 큰 보상을 주자"는 것이었으나, 이는 주관식 풀이처럼 찍어서 맞힐 확률이 0에 수렴할 때만 유효합니다.

```
[정상 추론 (8/16 성공)]  ---> 정답 어드밴티지: +1.00
[요행 찍기 (1/16 성공)]  ---> 정답 어드밴티지: +3.87 (정상의 3.87배 폭탄 보상!)
```

### 2.2 실세계 데이터셋의 Bounded-Answer 노출도
"주관식 수학(Math) 데이터셋만 쓰면 찍기가 불가능하므로 안전하지 않은가?"라는 가설은 실험적으로 반박되었습니다:

| 데이터셋 분류 | 특성 | 찍기 가능(Bounded-Answer) 비율 |
| :--- | :--- | :--- |
| **MATH (7.5K) 전체** | 주관식 수학 벤치마크 | **55.95%** (정답이 $[-10, 10]$ 정수 또는 단순 분수) |
| **MATH Level 1 (쉬운 난이도)** | 기초 문제군 | **69.20%** |
| **4지선다 객관식 (SAT, AQuA)** | Bounded candidate set | **25.00%** (무작위 찍기 성공 확률) |
| **검색 에이전트 (Search Agents)** | 다중 검색 경로 예산 | 다수 궤적 중 우연한 정답 도출 빈발 |

결과적으로 모델은 주관식 수학을 학습할 때조차 긴 사고 사슬(CoT)을 정밀하게 구성하는 대신, 쉬운 숫자 범위 내에서 대충 찍는 꼼수 궤적에 극도로 높은 보상을 받아 해당 패턴을 강화하게 됩니다. 이로 인해 풀이 과정은 정교하게 작성해 두고 최종 결론에서 엉뚱한 선지를 찍어버리는 정렬 불일치가 발생합니다.

---

## 3. 해결책: SignBalance 알고리즘

Adobe/RIT 연구진은 무거운 보조 모델이나 연산량 증가 없이, 이득 계산 수식의 구성을 분리하는 **SignBalance**를 제안했습니다.

### 3.1 핵심 설계 원칙
1. **정답 보상 크기 고정 (Composition-Free Magnitude)**:
   - 그룹 내 정답 수가 1개이든 8개이든 상관없이 정답 궤적의 양수 어드밴티지를 $+1.0$으로 엄격히 고정합니다. 이로써 단일 요행 정답에 보상이 뻥튀기되는 현상을 차단합니다.
2. **오답 감점의 $1/N$ 분배 (Zero-Mean Balancing)**:
   - 정책 기울기의 분산을 억제하기 위해 그룹 내 이득 총합은 0($\sum_i A_i = 0$)을 유지해야 합니다.
   - 정답이 $N_{\text{pos}}$개이고 오답이 $N_{\text{neg}}$개일 때:
     $$A_i = \begin{cases} +1.0 & \text{if } R_i = 1 \\ -\frac{N_{\text{pos}}}{N_{\text{neg}}} & \text{if } R_i = 0 \end{cases}$$
3. **Stop-Gradient Per-Class Rescaling**:
   - 클래스별 재조정 과정에서 그래디언트 역전파를 차단(`stop_gradient`)하여 수치적 안정성을 확보합니다.

### 3.2 PyTorch 구현 코드 비교

```python
import torch

def compute_traditional_grpo_advantage(rewards: torch.Tensor, eps: float = 1e-8) -> torch.Tensor:
    """기존 GRPO: 분산 기반 정규화로 희귀 정답에 폭탄 보상 부여"""
    mean = rewards.mean(dim=-1, keepdim=True)
    std = rewards.std(dim=-1, keepdim=True)
    return (rewards - mean) / (std + eps)

def compute_signbalance_advantage(rewards: torch.Tensor, eps: float = 1e-8) -> torch.Tensor:
    """SignBalance: 정답 어드밴티지를 +1.0으로 고정하고 음수 보상을 오답에 균등 분배"""
    # rewards: [batch_size, group_size] (0.0 또는 1.0)
    pos_mask = (rewards > 0.5).float()
    neg_mask = 1.0 - pos_mask
    
    n_pos = pos_mask.sum(dim=-1, keepdim=True)
    n_neg = neg_mask.sum(dim=-1, keepdim=True)
    
    # 정답이 없거나 모두 정답인 경계 조건 처리
    all_zero_or_one = (n_pos == 0) | (n_neg == 0)
    
    # 정답은 +1.0, 오답은 -(n_pos / n_neg)
    neg_advantage = -(n_pos / (n_neg + eps))
    advantages = pos_mask * 1.0 + neg_mask * neg_advantage
    
    # 경계 조건에서는 0으로 설정
    advantages = torch.where(all_zero_or_one, torch.zeros_like(advantages), advantages)
    return advantages.detach()
```

---

## 4. 벤치마크 평가 결과

SignBalance는 추가 연산 비용 0%로 GRPO 대비 뛰어난 성능 향상을 입증했습니다:

### 4.1 소형 수학 추론 (0.5B Backbone)
- **SAT-Math**: GRPO 65.62% $\rightarrow$ SignBalance **71.88%** (+6.26%p)
- **AQuA (객관식 수학)**: GRPO 29.53% $\rightarrow$ SignBalance **35.43%** (+5.90%p)

### 4.2 모델 스케일 확장 (3B Backbone)
- AIME24, AMC23을 포함한 8대 고난도 수학 벤치마크 중 **7개 벤치마크에서 최고 성능 달성** (전체 평균 42.80% $\rightarrow$ **43.78%**).

### 4.3 검색 기반 에이전트 (7B Backbone)
- 6개 질의응답(QA) 벤치마크에서 Search-R1, StepSearch를 제치고 **최고 정확도(37.80%)** 달성. 다중 경로 검색 중 발생하는 요행 추론 억제 효과 입증.

---

## 5. 아키텍처적 시사점 및 정렬 원칙
1. **NTP에서 RL로의 확장 불변성**:
   - NTP(Next-Token Prediction)가 대규모 데이터 주입으로 확장되었듯, GRPO는 Critic 없는 검증 함수 기반으로 무한 스케일링을 가능케 했습니다.
2. **샘플링 노이즈의 수식적 절제**:
   - 대규모 병렬 생성 과정에서 발생하는 '찍기 요행 노이즈'를 외부 필터링이나 대형 보상 모델 없이 순수 대수학적 대칭성(Algebraic Symmetry) 교정만으로 해결한 모범적 사례입니다.
3. **NVIDIA GDPO와의 관계**:
   - [[wiki/Models/RL/NVIDIA GDPO: 다중 보상 RL의 GRPO 결함 해결.md|NVIDIA GDPO]]가 *다중 보상 항목 간의 상쇄 결함*을 분리 정규화로 해결했다면, SignBalance는 *단일 보상 체계 내에서 그룹 내 성공 빈도 왜곡*을 고정 진폭으로 해결합니다.

---

## 🔗 관련 문서
- [[wiki/Models/RL/GRPO-Algorithm-Definition.md|GRPO 알고리즘 정의]]
- [[wiki/Models/RL/DeepSeek-R1-GRPO-Implementation.md|DeepSeek-R1 GRPO 구현]]
- [[wiki/Models/RL/NVIDIA GDPO: 다중 보상 RL의 GRPO 결함 해결.md|NVIDIA GDPO: 다중 보상 RL 결함 해결]]
- [[wiki/Models/RL/000_RL-MOC.md|RL MOC]]
