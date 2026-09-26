---
title: "GD²PO: 다중 보상 충돌 완화 및 그룹 동적 분리 정책 최적화"
last_updated: "2026-09-26"
updated: "2026-09-26"
related_raw: ["[[2026-09-26-gd2po-mitigating-multi-reward-conflicts.md]]"]
tags: ["wiki", "Models", "RL", "GD2PO", "GDPO", "GRPO", "Reinforcement-Learning", "Reasoning"]
type: "wiki"
status: "published"
---

# GD²PO: 다중 보상 충돌 완화 및 그룹 동적 분리 정책 최적화

**GD²PO (Group-Dynamic reward-Decoupled Policy Optimization)**는 알리바바 Qwen Large Model Application 팀(Liu et al., 2026, [arXiv:2606.16771](https://arxiv.org/abs/2606.16771), [GitHub: Qwen-Applications/GD2PO](https://github.com/Qwen-Applications/GD2PO))이 제안한 강화학습 정렬 알고리즘입니다.

[[wiki/Models/RL/NVIDIA GDPO: 다중 보상 RL의 GRPO 결함 해결.md]]가 다중 보상 환경에서 큰 분산의 보상이 작은 분산의 보상을 지워버리는 **보상 이점 붕괴(Reward Advantage Collapse)**를 분리 정규화로 해결했다면, **GD²PO**는 서로 다른 보상 차원 간의 부호 불일치로 인해 유효한 정책 그래디언트가 상쇄되어 버리는 **다중 보상 상충(Multi-Reward Conflict)** 문제를 근본적으로 해결합니다.

---

## 1. 배경: GDPO의 한계와 다중 보상 상충 (Multi-Reward Conflict)

[[wiki/Models/RL/DeepSeek-R1-GRPO-Implementation.md]] 및 현대 추론/정렬 LLM은 도구 호출 정확도($r_{\text{tool}}$), 출력 형식 준수($r_{\text{fmt}}$), 정답률($r_{\text{acc}}$), 안전성($r_{\text{safe}}$) 등 다차원 보상을 동시에 최적화해야 합니다.

### 1.1 GDPO의 스칼라 단순 합산 어드밴티지
NVIDIA GDPO는 각 보상 차원 $k$에 대해 독립적으로 그룹 정규화를 거쳐 스케일 불변성을 확보했으나, 최종적으로 각 롤아웃 $i$에 대해 정규화된 어드밴티지를 가중 합산하여 단일 스칼라 $A_i$를 산출합니다:

$$A_i^{\text{GDPO}} = \sum_{k=1}^K w_k \cdot A_{i,k} = \sum_{k=1}^K w_k \cdot \left(\frac{r_{i,k} - \mu_k}{\sigma_k + \epsilon}\right)$$

### 1.2 신호 상쇄(Signal Cancellation) 딜레마
현실적인 모델 롤아웃에서는 특정 차원에서 우수하지만 다른 차원에서 페널티를 받는 불완전 샘플이 빈번히 발생합니다.
- **예시 (도구 호출 시나리오)**:
  - 도구 파라미터와 비즈니스 로직은 정확히 맞혔으나($A_{i,\text{acc}} = +2.4$), 사소한 JSON 포맷팅 실수가 발생($A_{i,\text{fmt}} = -2.2$)한 경우:
  $$A_i = (+2.4) + (-2.2) = \mathbf{+0.2}$$
- **결과적인 파정**:
  - 두 보상 차원의 강한 학습 신호가 상호 소멸하여 $A_i \approx 0$으로 수렴합니다.
  - 모델은 "어떤 부분이 우수했고 어떤 부분을 고쳐야 하는지"에 대한 방향성을 잃고, 유효 어드밴티지 크기가 급감하여 정책 최적화가 정체(Stagnation)되거나 그래디언트 진동(Oscillation)을 겪습니다.

---

## 2. GD²PO의 핵심 메커니즘

GD²PO는 상충되는 그래디언트가 정책을 교란하기 전에 그룹 롤아웃 수준에서 개입하는 **2단계 동적 정렬 아키텍처**를 제안합니다.

```
[Group Rollouts G]
        │
        ▼
┌───────────────────────────────────────────────┐
│ 1. Decoupled Normalization (보상별 분리 정규화) │
│    A_{i,k} = (r_{i,k} - μ_k) / (σ_k + ε)      │
└───────────────────────┬───────────────────────┘
                        │
                        ▼
┌───────────────────────────────────────────────┐
│ 2. Conflict-Aware Filtering (충돌 인지 필터링)  │
│    - Hard Rule: Sign-based Filtering          │
│    - Soft Rule: SNR-based Filtering           │
│    (극심한 보상 불일치 롤아웃 마스킹/제거)          │
└───────────────────────┬───────────────────────┘
                        │
                        ▼
┌───────────────────────────────────────────────┐
│ 3. Query-Level Dynamic Reweighting            │
│    보존 샘플 비율 ρ_q 기반 앙상블 합의 가중치     │
│    W_q = f(ρ_q) 로 쿼리별 업데이트 강도 조절     │
└───────────────────────┬───────────────────────┘
                        │
                        ▼
             [안정적 Policy Gradient 업데이트]
```

### 2.1 Conflict-Aware Filtering (충돌 인지 필터링)
DAPO(Dynamic Sampling Policy Optimization)의 동적 샘플링 철학을 다차원 보상 공간으로 확장하여, 보상 간 방향성 불일치가 임계치를 초과하는 롤아웃을 정책 업데이트 대상에서 마스킹(Pruning)합니다.

1. **부호 기반 하드 필터링 (Sign-based Hard Filtering)**:
   - 주요 보상 차원 간 부호가 엇갈리는 샘플을 탐지:
   $$\text{Conflict}_{\text{hard}}(i) = \mathbb{I}\left(\exists k_1, k_2 : \text{sign}(A_{i,k_1}) \cdot \text{sign}(A_{i,k_2}) < 0 \;\land\; |A_{i,k_1}| > \tau \;\land\; |A_{i,k_2}| > \tau\right)$$
   - 임계치 $\tau$ 이상의 강한 긍정 신호와 강한 부정 신호가 정면충돌하는 롤아웃은 그래디언트 상쇄 노이즈를 방지하기 위해 마스킹 처리합니다.
2. **SNR 기반 소프트 필터링 (SNR-based Soft Filtering)**:
   - 보상 벡터 간의 방향 일치도(코사인 유사도 또는 Signal-to-Noise Ratio)를 산출하여, 사소한 트레이드오프와 파괴적 충돌을 연속적 확률값으로 가중 제어합니다.

### 2.2 Query-Level Dynamic Reweighting (쿼리 수준 동적 가중치 재조정)
필터링 후 남아있는 유효 롤아웃의 비율($\rho_q = \frac{G_{\text{valid}}}{G}$)은 해당 쿼리/프롬프트에 대한 모델의 **다중 보상 합의도(Reward Consensus)**를 반영합니다.

- **합의도 높은 쿼리 ($\rho_q \to 1.0$)**:
  - 대부분의 롤아웃에서 여러 보상 목표가 일관되게 달성되거나 일관되게 실패하는 프롬프트.
  - 학습 신호의 신뢰도가 높으므로 높은 가중치 $W_q$를 부여하여 신속한 정책 갱신을 유도.
- **충돌 심한 쿼리 ($\rho_q \ll 1.0$)**:
  - 목표 간 충돌이 빈번하여 모델이 혼란을 겪는 프롬프트.
  - 가중치 $W_q$를 동적으로 축소하여 정책 드리프트 및 과도한 그래디언트 왜곡을 방지.

---

## 3. 알고리즘 비교 분석

| 비교 항목 | GRPO ([[wiki/Models/RL/DeepSeek-R1-GRPO-Implementation.md]]) | GDPO ([[wiki/Models/RL/NVIDIA GDPO: 다중 보상 RL의 GRPO 결함 해결.md]]) | SignBalance ([[wiki/Models/RL/GRPO-Spurious-Advantage-SignBalance.md]]) | **GD²PO (본 문서)** |
| :--- | :--- | :--- | :--- | :--- |
| **핵심 해결 과제** | Critic 네트워크 제거 및 그룹 정규화 | 다중 보상 분산 불균형 (이점 붕괴) | 단일 보상 내 요행 찍기 (거짓 이득) | **다중 보상 간 신호 상쇄 및 상충** |
| **정규화 방식** | $\sum_k w_k r_k$ 후 그룹 일괄 정규화 | 보상별 독립 그룹 정규화 후 합산 | 부호별(양/음) 분리 스케일링 | 보상별 독립 정규화 + 충돌 필터링 |
| **상충 신호 제어** | 없음 (완전 희석) | 없음 (스칼라 합산 시 소멸) | 단일 보상 극단값 클램핑 | **Sign/SNR 기반 충돌 롤아웃 마스킹** |
| **쿼리 단위 가중치**| 균등 (전체 프롬프트 동일 배치) | 균등 | 균등 | **유효 표본율($\rho_q$) 기반 동적 스케일링** |
| **도구 호출 성능** | 포맷 오류율 높음 | 포맷-정답 균형 개선 | 추론 안정화 | **BFCL 복합 API 문맥 최고 성능** |

---

## 4. 실전 파이토치(PyTorch) 구현 패턴

GD²PO의 핵심 어드밴티지 및 마스킹 계산 로직은 다음과 같이 구현됩니다:

```python
import torch
import torch.nn.functional as F

def compute_gd2po_advantages(
    rewards: torch.Tensor,       # [B, G, K] (Batch, GroupSize, NumRewards)
    weights: torch.Tensor,       # [K] Reward weights
    conflict_threshold: float = 0.5,
    snr_soft_tau: float = 0.3,
    eps: float = 1e-8
):
    """
    rewards: 프롬프트별 G개 롤아웃에 대한 K개 보상 차원 텐서
    """
    B, G, K = rewards.shape
    
    # 1. Step 1: 보상 차원별 독립 그룹 정규화 (GDPO 메커니즘)
    mean = rewards.mean(dim=1, keepdim=True)             # [B, 1, K]
    std = rewards.std(dim=1, keepdim=True) + eps         # [B, 1, K]
    decoupled_adv = (rewards - mean) / std               # [B, G, K]
    
    # 2. Step 2: Conflict-Aware Filtering
    # 각 보상 간의 부호 불일치 및 임계치 초과 여부 점검
    sign_pos = (decoupled_adv > conflict_threshold).any(dim=-1)   # [B, G]
    sign_neg = (decoupled_adv < -conflict_threshold).any(dim=-1)  # [B, G]
    hard_conflict_mask = sign_pos & sign_neg                     # [B, G] 강한 충돌 마스크
    
    # SNR 기반 연속 소프트 필터링 (보상 벡터 코사인 유사도)
    norm_adv = F.normalize(decoupled_adv, dim=-1)                # [B, G, K]
    mean_dir = norm_adv.mean(dim=1, keepdim=True)                # [B, 1, K]
    alignment = (norm_adv * F.normalize(mean_dir, dim=-1)).sum(dim=-1) # [B, G]
    soft_weights = torch.sigmoid((alignment - snr_soft_tau) * 5.0)
    
    # 최종 유효 마스크: 하드 충돌 제외 및 소프트 가중 적용
    valid_mask = (~hard_conflict_mask).float() * soft_weights    # [B, G]
    
    # 3. Step 3: 가중 합산 어드밴티지 산출
    weighted_adv = (decoupled_adv * weights.view(1, 1, K)).sum(dim=-1) # [B, G]
    masked_adv = weighted_adv * valid_mask
    
    # 4. Step 4: Query-Level Dynamic Reweighting
    # 프롬프트별 유효 표본 보존율 산출
    retention_rate = valid_mask.sum(dim=-1, keepdim=True) / float(G) # [B, 1]
    query_weights = torch.clamp(retention_rate, min=0.1, max=1.0)
    
    final_advantages = masked_adv * query_weights                # [B, G]
    return final_advantages, valid_mask
```

---

## 5. 엔지니어링 함정 및 권장 설정

1. **임계치 $\tau$의 민감도**:
   - $\tau$를 너무 낮게(예: $< 0.2$) 설정하면 대부분의 롤아웃이 충돌로 판정되어 학습 데이터의 70% 이상이 버려지는 과잉 프루닝이 발생합니다.
   - 경험적으로 $\tau \in [0.4, 0.7]$ 구간에서 가장 안정적인 학습 곡선을 나타냅니다.
2. **최소 유효 샘플 수 가드레일**:
   - 특정 고난도 쿼리에서 모든 롤아웃이 마스킹되어 유효 샘플이 0개가 될 경우, 해당 쿼리의 정책 그래디언트는 완전히 0으로 처리(Zero-out)해야 하며 Zero-division 예외를 방어해야 합니다.
3. **에이전트 복합 추론 적용**:
   - Function Calling 및 Web Search 에이전트 파인튜닝 시, `format_reward`, `tool_call_validity`, `grounded_accuracy`, `trajectory_length_penalty` 4가지 보상을 조합할 때 GD²PO가 표준 GDPO 대비 **+8.4% 높은 도구 호출 완결률**을 보입니다.

---

## 6. 관련 문서 및 백링크
- [[wiki/Models/RL/NVIDIA GDPO: 다중 보상 RL의 GRPO 결함 해결.md]]: 다중 보상 분리 정규화의 기초 원리와 보상 분산 붕괴 해결책.
- [[wiki/Models/RL/GRPO-Spurious-Advantage-SignBalance.md]]: 단일 보상 내 찍기 궤적에 대한 거짓 이득 제거 알고리즘.
- [[wiki/Models/RL/DeepSeek-R1-GRPO-Implementation.md]]: DeepSeek-R1의 원조 GRPO 구현 분석.
- [[wiki/Models/RL/Agent-R1 Training Powerful LLM Agents with End-to-End Reinforcement Learning.md]]: 에이전틱 강화학습 환경의 롤아웃 파이프라인.
- [[wiki/Engineering/AI-Native-Engineering/Epistemic-Debt-ChangeScore-Friction-Gate.md]]: 에이전트 결정 및 정렬 품질 제어 관점의 연결.
