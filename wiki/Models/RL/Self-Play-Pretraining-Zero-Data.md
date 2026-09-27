---
title: "Self-Play Pretraining with Zero Data: 무(無)데이터 기반 자기대전 사전학습과 보편적 예측 구조의 창발"
related_raw: ["[[raw/2026-09-27-self-play-pretraining-zero-data.md]]"]
tags: ['wiki', 'models', 'rl', 'pretraining', 'self-play', 'zero-data', 'scaling-laws', 'universal-turing-machine']
type: "wiki"
status: "published"
last_updated: "2026-09-27"
updated: "2026-09-27"
---

# Self-Play Pretraining with Zero Data: 무(無)데이터 기반 자기대전 사전학습과 보편적 예측 구조의 창발

## 1. 개요 및 패러다임 전환 (Paradigm Shift)

기존 대형 언어 모델(LLM)의 사전학습은 인터넷에서 수집·정제한 인간 생성 자연 데이터(Natural Data)의 규모 확장에 의존해 왔다. 그러나 이러한 방식은 **고품질 인간 데이터의 고갈(Data Wall)**과 인간 주석에 내재된 **인위적 귀납적 편향(Inductive Bias)**이라는 근본적인 한계에 직면해 있다.

2026년 9월 발표된 **"Self-Play Pretraining with Zero Data"** (arXiv:2609.30063, Stanford / Technion / Meta) 연구는 외부 자연 데이터를 단 1토큰도 사용하지 않고, 무작위로 초기화된 두 트랜스포머 모델인 **생성기($g_\phi$)**와 **학습기($\pi_\theta$)** 간의 자기대전(Self-Play) 상호작용만을 통해 인공지능이 스스로 학습 데이터를 생성하고 발전하는 새로운 사전학습 패러다임을 실증하였다.

이 접근법은 서튼의 '씁쓸한 교훈(The Bitter Lesson)'을 학습 데이터 계층으로 확장하여, 솔로모노프 귀납법(Solomonoff Induction)의 계산 가능한 근사(Computable Approximation)로서 최소 보편 튜링 기계(Universal Turing Machine, UTM) 공간을 탐색하고, 순수 연산량($T$)의 확장만으로 텍스트, 이미지, 음성, 음악, DNA 등 다양한 자연 도메인에서 예측 오차가 거듭제곱 법칙(Power-Law)을 따르며 감소함을 입증하였다.

```
                    ┌───────────────────────────────────────────────┐
                    │            Universal Turing Machine           │
                    │      U(x_i, ω_i) -> Output Byte Stream        │
                    └───────────────────────▲───────────────────────┘
                                            │ Program x_i
                     ┌──────────────────────┴───────────────────────┐
                     │                                              │
         ┌───────────┴──────────┐                       ┌───────────┴──────────┐
         │  Generator g_ϕ(x)    │                       │  Learner π_θ(y)      │
         │  (Decoder Transformer)│                       │  (Decoder Transformer)│
         └───────────▲──────────┘                       └───────────┬──────────┘
                     │                                              │
                     │ RL Update (GRPO + Learning-Progress Reward)   │ Next-Token Prediction
                     │   r_i = |∇_θ L(y_i)^T P_AdamW Δθ_{e/2}|       │   L(y_i; θ) Cross-Entropy
                     └──────────────────────────────────────────────┘
```

---

## 2. 핵심 시스템 아키텍처 및 자기대전(Self-Play) 메커니즘

### 2.1 모델 구성 및 바이트 레벨 토큰화
- **생성기($g_\phi$)와 학습기($\pi_\theta$)**: 동일한 구조의 디코더 전용 Llama 트랜스포머 아키텍처로 독립 파라미터화되며, 가중치는 무작위 초기화(Tabula Rasa) 상태에서 출발한다.
- **바이트 어휘(Byte-level Tokenization)**: 모달리티에 무관한 보편 예측 평가를 위해 크기 256의 고정 바이트 어휘를 채택한다.
  - 프로그램 입력: 접두사 `S`로 시작하며, 생성 시 로짓은 Brainfuck 기반 8개 기본 명령어, 10개 정규 매크로 명령어, 프로그램 종료 토큰 `F`로 제한된다.
  - 출력 시퀀스: 접두사 `O`로 시작하며 임의의 256개 바이트 값을 가질 수 있다.

### 2.2 보편 튜링 기계(UTM) 실행 기저
프로그램 생성 공간 $x \in \mathcal{A}^{\le L}$은 Brainfuck 변형 튜링 완전 기계 $U$에서 실행된다.
$$y_i = U(x_i, \omega_i)$$
- **무작위 입력 테이프($\omega_i$)**: 명령어 `,`는 균등 무작위 바이트 테이프에서 입력을 읽어들이므로, 단일 프로그램이 출력 시퀀스에 대한 확률 분포를 표현할 수 있다.
- **예외 없는 강건한 실행**:
  - 짝이 맞지 않는 괄호(`[`, `]`)는 No-op으로 처리되어 구문 오류(Syntax Error)가 발생하지 않는다.
  - 원형 메모리(Circular Memory) 테이프 구조를 채택하여 메모리 경계를 벗어나면 래핑(Wrap)되고, 셀 값은 모듈로 256 연산으로 오버플로를 방지하여 메모리 결함(Segmentation Fault)이 없다.
  - 최대 스텝 수 또는 방출 바이트 상한($T$)에 도달하면 안전하게 종료된다.

### 2.3 학습기(Learner) 업데이트
학습기는 UTM이 생성한 바이트 시퀀스 $y_i$에 대해 표준 크로스 엔트로피 기반의 다음 토큰 예측(Next-Token Prediction)을 수행한다:
$$\mathcal{L}(y_i; \theta) = -\frac{1}{|y_i|} \sum_{t=1}^{|y_i|} \log \pi_\theta(y_{i, t} \mid y_{i, <t})$$

### 2.4 생성기 강화학습 및 학습 진행 보상 (Learning-Progress Reward)
단순히 학습기가 예측하기 어려운(High Loss) 프로그램을 생성하도록 보상하면, 예측 불가능한 무작위 노이즈 바이트를 쏟아내는 퇴행(Degeneracy)이 발생한다. 따라서 학습기가 실제로 학습을 축적할 수 있는 **역량의 최전선(Frontier of capabilities)**에 위치한 프로그램을 식별해야 한다.

#### (1) 학습 진행 보상 수식
학습기의 최근 룩백 윈도우 $\lceil e/2 \rceil$ 동안의 파라미터 누적 변위 벡터 $\Delta \theta_{p(e)} = \theta_e - \theta_{\lceil e/2 \rceil}$와, 신규 프로그램 출력에 대한 학습기의 그래디언트 간의 정렬도를 측정한다:
$$r(x_i) = \left| \nabla_\theta \mathcal{L}(y_i; \theta_e)^\top P_{\text{AdamW}} \, \Delta \theta_{p(e)} \right|$$
- **사전조건화 행렬($P_{\text{AdamW}}$)**: 학습기의 옵티마이저 2차 모멘트 상태로부터 유도된 대각 스케일링 연산자로, 그래디언트 성분 간의 스케일을 정규화한다.
- **연산 최적화**: 전체 파라미터 그래디언트를 구체화(Materialize)하지 않고, JVP(Jacobian-Vector Product) 전방 모드 자동 미분(Forward-Mode Automatic Differentiation, `jvp_flash_attention`)을 적용하여 $O(1)$ 메모리 오버헤드로 내적을 고속 계산한다.
- **보상의 물리적 의미**:
  - 이미 마스터한 프로그램: 그래디언트 $\nabla_\theta \mathcal{L} \approx 0 \implies$ 보상 0.
  - 무작위 노이즈/학습 불가능한 프로그램: 그래디언트가 이전 학습 궤적 $\Delta \theta$와 직교($\perp$) $\implies$ 내적 0.
  - 현재 학습자가 막 습득하기 시작한 규칙적 프로그램: 그래디언트 방향이 이전 개선 벡터와 강하게 정렬 $\implies$ 최대 보상 부여.

#### (2) 정책 경사(Policy Gradient) 및 GRPO 어드밴티지
생성기는 솔로모노프 사전 분포 $g_0(x) = |\mathcal{A}|^{-\ell(x)}$에 대한 KL 정규화 및 GRPO 배치 어드밴티지를 통해 업데이트된다:
$$A_i = \frac{r_i - \bar{r}_e}{\sigma_{r, e}}$$
$$\mathcal{L}_{\text{PG}}(\phi) = -\frac{1}{|\mathcal{B}_e^{\text{on}}|} \sum_{i \in \mathcal{B}_e^{\text{on}}} \min \left( \rho_i A_i, \, \text{clip}(\rho_i, 1-\epsilon, 1+\epsilon) A_i \right) + \beta \, D_{\text{KL}}(g_\phi \parallel g_0)$$
여기서 $\rho_i = \frac{g_\phi(x_i)}{g_{\phi_{\text{old}}}(x_i)}$는 오프폴리시 샘플을 보정하는 시퀀스 단위 중요도 비율이다.

### 2.5 품질-다양성(MAP-Elites) 풀 및 망각 방지 메커니즘
- **3계층 프로그램 풀($\mathcal{B}_e$)**:
  1. $\mathcal{B}_e^{\text{fresh}}$: 현재 생성기 $g_\phi$가 샘플링한 최신 온폴리시 프로그램.
  2. $\mathcal{B}_e^{\text{mut}}$: 고보상 프로그램을 MAP-Elites 니치(루프 최대 깊이 0~8, 프로그램 길이 8/16/32로 분할된 36개 니치)에서 추출하여 1토큰 치환/삽입/삭제한 돌연변이 프로그램.
  3. $\mathcal{B}_e^{\text{replay}}$: 이전 라운드 고보상 프로그램을 저장한 뱅크에서 무작위 재현.
- **전문가 반복(Expert Iteration, SFT)**: 이전 성공 프로그램의 지식을 생성기에 재주입하여 치명적 망각(Catastrophic Forgetting)을 방지하기 위해 보상 가중 지도 학습 손실을 결합한다:
  $$\mathcal{L}_{\text{full}}(\phi) = \mathcal{L}_{\text{PG}}(\phi) + \lambda_{\text{EI}} \, \mathcal{L}_{\text{EI}}(\phi)$$

---

## 3. 보편 데이터 가설(Universal Data Ansatz) 및 스케일링 법칙

### 3.1 자연 데이터 정보의 이원화 분해
Chinchilla 스케일링 법칙 $L(N, D) = E + \frac{A}{N^\alpha} + \frac{B}{D^\beta}$을 확장하여, 데이터를 두 가지 독립적인 자원으로 분해한다:
$$L(N, D_c, D_u) = E + \left(\frac{N_0}{N}\right)^{\alpha_N} + \left(\frac{D_{c, 0}}{D_c}\right)^{\alpha_c} + \left(\frac{D_{u, 0}}{D_u}\right)^{\alpha_u}$$
- **우연적/부차적 정보 ($D_c$, Contingent Information)**: 특정 세계나 사실(예: "파리는 프랑스의 수도이다", 특정 언어 어휘 등)에 국한된 정보.
- **보편적 예측 구조 ($D_u$, Universal Predictive Structure)**: 복사(Copying), 재귀(Recursion), 조건 분기, 계층 구조 등 모달리티를 초월하여 계산 가능한 모든 프로세스에 공통되는 추론 구조.

### 3.2 제로 데이터 자기대전의 거듭제곱 스케일링
자기대전 과정에서는 자연 데이터를 일절 보지 않으므로 $D_c$는 고정 상수로 흡수된다. 순수하게 계산량 $T$의 투입으로 보편 데이터 $D_u(T) \propto T^\eta$가 생성되므로, 자연 평가 데이터에서의 제로샷 손실은 연산량 $T$에 대한 거듭제곱 법칙을 따른다:
$$L_{\text{zero-shot}}(T) = E' + \left(\frac{T_0}{T}\right)^\gamma \quad (\gamma = \alpha_u \eta)$$

실험 결과, 텍스트(DCLM), 자연 이미지(CIFAR-10), 음성(Speech Commands), 클래식 음악(Mutopia), C 소스코드, 정밀 수학(Metamath) 전반에서 일관된 거듭제곱 손실 감소가 관찰되었으며, 측정된 스케일링 지수 $\gamma$는 해당 도메인의 자연 데이터를 직접 학습했을 때의 지수와 유사한 수준을 기록하였다.

| 모달리티 | 벤치마크 데이터셋 | 자기대전 스케일링 지수 ($\gamma$) | 고정 보편 사전(Solomonoff) 대비 |
| :--- | :--- | :--- | :--- |
| **자연어 텍스트** | DCLM Baseline 1.0 | 0.076 | 유의미하게 빠른 수렴 |
| **자연 이미지** | CIFAR-10 (CHW/HWC) | 0.082 | 균등 샘플링 대비 압도적 우위 |
| **원시 음성** | Speech Commands (16kHz) | 0.065 | 적응형 커리큘럼 효과 입증 |
| **음악 멜로디** | Mutopia Classical MIDI | 0.091 | 규칙적 리듬/선율 패턴 포착 |
| **소스 코드** | AITDCC C Source | 0.079 | 문법 및 중첩 구조 습득 |
| **정밀 수학** | Metamath (set.mm) | 0.084 | 기호 체계 규칙성 추론 |
| **생체 서열** | KoLMogorov Human DNA | 0.041 | 8진수 염기 서열 규칙성 포착 |

---

## 4. 주요 실험 결과 및 창발적 능력 (Emergent Capabilities)

### 4.1 수학적 구조의 자율 발견 (Discovery of Mathematical Sequences)
생성기는 훈련 라운드가 진행됨에 따라 균등 샘플링으로는 확률적으로 발견이 불가능한 고차 수학 구조를 조기에 발견하여 학습기에 공급하였다:
- **등차수열(Arithmetic)**: 라운드 100경 발견 (무작위 기준 발견 라운드 약 105).
- **피보나치 수열(Fibonacci-like)**: 라운드 256 이내 발견 (무작위 표본 $1.64 \times 10^8$개 추출 시 발생 0건, $p < 1.8 \times 10^{-8}$, 기대 발견 라운드 > 53,000).
- **2차/3차 다항수열(Quadratic/Cubic)**: 라운드 512 이내 자율 창발.
- **기하수열(Geometric)**: 라운드 512 이내 자율 창발.

### 4.2 인컨텍스트 러닝(In-Context Learning, ICL) 창발
가중치 업데이트 없이 프롬프트 문맥 내 예시만으로 작동하는 ICL 능력이 순수 자기대전만으로 학습된 모델에서 창발하였다:
1. **Reverse String**: 임의 바이트 문자열 역순 출력 (동적 인덱싱 능력).
2. **Stack Simulation**: 푸시(250) 및 팝(251) 명령어 열 해석 후 최종 상태 반환 (문맥 자유 문법 시뮬레이션).
3. **Associative Recall**: 키-값 쌍 딕셔너리 문맥 검색 (연상 기억 회상).
4. **Sum mod 256**: 두 바이트의 모듈로 합산 (예시 4개 후 하위 4비트 정렬, 8개 후 상위 4비트 정렬 성공).
5. **Min / Max**: 입력 바이트 시퀀스의 최소/최대값 식별.
*(고정 문법 기반 PCFG 사전학습 모델이나 무작위 사전 분포 학습 모델은 이러한 ICL 평가에서 모두 실패함)*

### 4.3 자연 데이터 사전학습 가속 (Pre-pretraining Acceleration)
자기대전으로 훈련된 체크포인트를 초기 가중치(Warm-start)로 삼아 자연 데이터 사전학습을 진행했을 때:
- **CIFAR-10 이미지**: 수렴 손실 도달까지 자연 데이터 토큰 소모량 28.4% 절감 (588M $\rightarrow$ 421M tokens).
- **ESC-50 오디오**: 자연 데이터 토큰 소모량 35.5% 절감 (496M $\rightarrow$ 320M tokens).
- **DCLM 텍스트**: 초기 손실 감소율이 무작위 초기화 대비 급격히 향상되어 사전학습 비용 절감 기저로 활용 가능.

---

## 5. 비평 및 시스템적 과제: 생성-검증-승격 루프

### 5.1 자율 자기대전의 구조적 취약점
자기대전 사전학습은 인간 데이터 없이 지능의 기저를 확장할 수 있는 문을 열었으나, 장기적인 자율 진화 시스템 관점에서 다음과 같은 잠재적 위험을 내포한다:
1. **자기일관성과 진실의 불일치**: 모델이 생성한 데이터 내에서 스스로 모순이 없더라도(Self-consistent), 그것이 실세계의 객관적 진실(Ground Truth)과 일치함을 보장하지 않는다.
2. **학습가능성과 정확성의 괴리**: 학습기의 그래디언트 내적이 크다는 것(Learnable)은 매력적인 패턴이라는 뜻일 뿐, 그 규칙이 논리적으로 타당하거나 유익하다는 것을 의미하지 않는다.
3. **오류 자기강화 및 모델 붕괴(Model Collapse)**: 초기 생성기의 사소한 왜곡이나 가짜 상관관계(Spurious correlation)가 학습기에 전이되고, 학습기의 편향된 그래디언트가 다시 생성기의 보상 함수를 왜곡하여 시스템 전체가 기형적인 지식 공간으로 수렴할 위험이 존재한다.

### 5.2 차세대 자율 학습 아키텍처: GVAB 루프
단순한 `Generated → Learned`의 폐쇄 루프를 탈피하여, 외부 불변식과 정형 샌드박스가 개입하는 4단계 승격 구조가 필수적이다:
```
[1. Generated]  ──>  [2. Validated]  ──>  [3. Admitted]  ──>  [4. Learned]
생성기 프로그램      형식 검증 & 샌드박스   통계적 품질·다양성      학습기 파라미터 갱신
가설/시퀀스 생성     불변식 검사(Fail-close) 게이트웨이 통과 승격    및 체크포인트 전진
```
- **형식 검증(Validated)**: 실행 안전성, 엔트로피 최소치, 주기성 한계 검증.
- **승격 게이트(Admitted)**: 인식 부채(Epistemic Debt) 측정 및 가짜 어드밴티지(Spurious Advantage) 차단 필터 적용.

---

## 6. 구현 및 실무 참고 리소스

- **원천 논문**: [arXiv:2609.30063 - Self-Play Pretraining with Zero Data](https://arxiv.org/abs/2609.30063)
- **전방 모드 자동 미분 커널**: [GitHub - amorehead/jvp_flash_attention](https://github.com/amorehead/jvp_flash_attention) (JVP 기반 고속 그래디언트-변위 내적 계산)
- **솔로모노프 귀납 이론**: Solomonoff (1964), *A Formal Theory of Inductive Inference*
- **계산 유한성 정보 이론(Epiplexity)**: Finzi et al. (2026), [arXiv:2601.03220](https://arxiv.org/abs/2601.03220)

---

## 7. 관련 위키 문서
- [[wiki/Models/RL/GRPO-Scaling-Laws-Efficiency.md]] : GRPO 강화학습의 포화 법칙 및 컴퓨팅 최적 조기 종료
- [[wiki/Models/RL/DeepSeek-R1-GRPO-Implementation.md]] : 배치 단위 보상 정규화 기반 비평가-프리(Critic-free) RL
- [[wiki/Models/RL/NVIDIA GDPO: 다중 보상 RL의 GRPO 결함 해결.md]] : 다중 목표 보상 분리 정규화
- [[wiki/Models/RL/GD2PO-Multi-Reward-Conflict-Mitigation.md]] : 보호 및 질의 수준 동적 가중을 통한 보상 신호 상쇄 방지
- [[wiki/Models/Reasoning-and-Cognition/추론-LLM-추론-노력-제어-및-스케일링.md]] : 추론 노력 제어 및 테스트 타임 연산 스케일링
- [[wiki/Engineering/AI-Native-Engineering/Epistemic-Debt-ChangeScore-Friction-Gate.md]] : 자율 진화 시스템의 인식 부채 통제 및 승격 게이트
