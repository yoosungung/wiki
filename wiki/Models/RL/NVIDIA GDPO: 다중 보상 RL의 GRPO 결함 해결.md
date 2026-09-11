---
title: "NVIDIA GDPO: 다중 보상 RL의 GRPO 결함 해결"
related_raw: ["[[wiki/Models/RL/NVIDIA GDPO: 다중 보상 RL의 GRPO 결함 해결.md]]"]
tags: ['wiki', 'ai_core', 'ai_ml_development']
type: "wiki"
status: "published"
last_updated: "2026-09-11"
updated: "2026-09-11"
---

# NVIDIA GDPO: 다중 보상 RL의 GRPO 보상 붕괴 결함 해결

**GDPO (Group reward-Decoupled Normalization Policy Optimization)**는 NVIDIA 연구진(ICML 2026, arXiv:2601.05242)이 제안한 강화학습(RL) 최적화 알고리즘으로, DeepSeek-R1 등에서 널리 쓰이는 **GRPO (Group Relative Policy Optimization)**를 다중 보상(Multi-Reward) 환경에 적용할 때 발생하는 치명적인 **'보상 이점 붕괴(Reward Advantage Collapse)'** 현상을 수학적으로 규명하고 해결한 기법입니다.

---

## 1. GRPO의 구조적 결함: 보상 이점 붕괴 (Reward Advantage Collapse)

기존 GRPO는 복잡한 Critic(가치 평가망) 없이 프롬프트당 $G$개의 롤아웃(샘플 응답)을 생성한 뒤, 그룹 내 보상의 평균과 표준편차로 정규화하여 어드밴티지(Advantage)를 계산합니다.

### ❌ 기존 GRPO의 보상 단순 합산 정규화
태스크에 다중 목표(예: 최종 정답률 $r_{\text{acc}}$, 출력 포맷 준수 $r_{\text{fmt}}$, 도구 호출 문법 $r_{\text{tool}}$, 추론 길이 제어 $r_{\text{len}}$)가 주어질 때, GRPO는 보상들을 가중 합산한 후 단일 정규화를 수행합니다:

$$A_i^{\text{GRPO}} = \frac{\left(\sum_k w_k r_{i,k}\right) - \mu_{\text{sum}}}{\sigma_{\text{sum}} + \epsilon}$$

- **문제점**: 분산(Variance)이 가장 큰 보상 항목(예: 수학 난제의 맞춤/틀림 바이너리 점수)이 전체 분모 $\sigma_{\text{sum}}$를 압도합니다.
- **결과**: 분산이 작지만 에이전트 구동에 필수적인 제약 조건(JSON 포맷 준수, 도구 호출 구문, 단계별 CoT 추론 형식)의 그래디언트 신호가 완전히 희석(Washed out)되어, 모델이 형식이나 도구 사용 규칙을 무시하고 학습이 붕괴하거나 조기 수렴 실패에 빠집니다.

---

## 2. GDPO의 핵심 메커니즘: 보상별 분리 정규화 (Decoupled Normalization)

GDPO는 보상을 합산한 뒤 정규화하는 대신, **각 보상 차원별로 그룹 정규화를 독립 수행한 후 가중 합산**하는 설계를 채택합니다.

### ✅ GDPO의 분리 정규화 어드밴티지 계산식

$$A_i^{\text{GDPO}} = \sum_k w_k \cdot \left(\frac{r_{i,k} - \mu_k}{\sigma_k + \epsilon}\right)$$

여기서:
- $\mu_k = \frac{1}{G} \sum_{j=1}^G r_{j,k}$ (보상 $k$에 대한 그룹 평균)
- $\sigma_k = \sqrt{\frac{1}{G} \sum_{j=1}^G (r_{j,k} - \mu_k)^2}$ (보상 $k$에 대한 그룹 표준편차)

### 💡 장점 및 효과
1. **스케일 불변성(Scale Invariance)**: 각 보상 신호가 자체 스케일로 정규화되므로, 절대적 수치나 분산 크기에 관계없이 모든 목적 함수(정답률 + 포맷팅 + 도구 호출)가 동등한 해상도의 정책 그래디언트를 유지합니다.
2. **보상 간섭 차단**: 한 보상의 노이즈나 급격한 분산 변화가 다른 보상의 어드밴티지 방향을 왜곡하지 않습니다.
3. **Critic-free 유지**: GRPO의 최대 장점인 별도 가치 네트워크(Value Model) 부재에 따른 GPU 메모리 절감 효과를 100% 보존합니다.

---

## 3. 벤치마크 및 실험 결과

*   **AIME 수학 추론**: 기존 GRPO 대비 최대 **+6.3%** 정확도 향상.
*   **도구 호출 (Tool Calling / BFCL)**: 복잡한 다단계 API 파라미터 생성 태스크에서 GRPO 대비 유의미한 형식 준수율 및 실행 성공률 달성.
*   **코드 생성 (SWE-bench / HumanEval)**: 단위 테스트 통과 보상과 린트/타입 체커 제약 보상을 동시에 안정적으로 수렴.
*   **학습 수렴 안정성**: 학습 후반부 보상 신호 붕괴로 인한 정책 드리프트(Policy Drift)가 완전히 제거됨.

---

## 4. 프레임워크 지원 및 실전 적용 (Drop-in Replacement)

GDPO는 기존 GRPO 구현체에서 어드밴티지 계산 함수 수식만 변경하면 되는 드롭인 대체(Drop-in replacement) 방식입니다.

- **NVIDIA NeMo-RL**: 공식 레퍼런스 구현체 탑재.
- **veRL & Hugging Face TRL**: 손쉬운 커스텀 어드밴티지 플러그인 연동 지원.

```python
# GDPO Advantage 계산 예시 (PyTorch)
def compute_gdpo_advantage(rewards_per_token, reward_weights, eps=1e-6):
    """
    rewards: [batch_size, num_rewards]
    weights: [num_rewards]
    """
    normalized_rewards = []
    for k in range(rewards.shape[-1]):
        r_k = rewards[:, k]
        mean_k = r_k.mean()
        std_k = r_k.std()
        norm_r_k = (r_k - mean_k) / (std_k + eps)
        normalized_rewards.append(reward_weights[k] * norm_r_k)
    
    # 각 보상별 정규화 결과를 가중 합산
    advantages = torch.stack(normalized_rewards, dim=-1).sum(dim=-1)
    return advantages
```

---

## 🔗 관련 문서 및 출처
- 원천 논문: [arXiv:2601.05242 - GDPO: Group reward-Decoupled Normalization Policy Optimization](https://arxiv.org/abs/2601.05242) (ICML 2026)
- 관련 위키: [[wiki/Models/RL/000_RL-MOC.md]], [[wiki/Models/RL/DeepSeek-R1-GRPO-Implementation.md]], [[wiki/Models/Reasoning-and-Cognition/추론-LLM-추론-노력-제어-및-스케일링.md]]
