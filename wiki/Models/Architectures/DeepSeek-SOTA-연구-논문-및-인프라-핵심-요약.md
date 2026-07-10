---
related_raw: ["[[2026-06-29-deepseek-sota-research-papers-v4.md]]"]
tags: ["#wiki", "Models/Architectures", "Models/Optimization", "Reinforcement-Learning", "DeepSeek", "FlashMLA"]
---

# DeepSeek SOTA 연구 논문 및 인프라 핵심 요약 (V4 세대)

DeepSeek가 발표한 주요 핵심 연구 성과(모델 아키텍처, 학습 인프라, 추론 최적화)의 핵심 내용을 계층별로 요약·정리합니다.

## 1. 모델 아키텍처 및 어텐션 혁신

### DeepSeek-V4-Pro: 100만 토큰 컨텍스트 MoE
- **기본 설계**: 총 1.6T(조) 파라미터 중 활성화되는 파라미터는 49B로 제한된 고효율 MoE 모델입니다. V3.2 대비 추론 연산량은 73%, KV 캐시 메모리는 90% 절감했습니다.
- **CSA & HCA**:
  - CSA (Context-Selective Attention): 관련 있는 국소적 컨텍스트 블록만 집중 검색.
  - HCA (Hierarchical Context Attention): 컨텍스트 전체를 압축된 해상도로 가볍게 조회.
  - 이중 어텐션 조합을 통해 100만 토큰의 방대한 입력을 실용적인 저비용으로 연산합니다.
- **mHC (Multi-path Head Connection)**: 기존의 residual connection을 다중 경로 헤드 연결 방식으로 교체하여, 초대형 스케일 학습 중 흔히 일어나는 loss spike 현상을 완전히 차단했습니다.

### DSA (DeepSeek Sparse Attention)
- **개념**: DeepSeek 고유의 MLA (Multi-head Latent Attention) 아키텍처와 결합되도록 최적화된 sparse attention 기법입니다.
- **방식**: 경량 indexer가 전체 KV 스토어 중에서 관련이 깊은 top-k 데이터만 실시간 선택하고 나머지는 연산에서 제외하여, 컨텍스트 윈도우가 늘어날 때 복잡도가 선형으로 증가하도록 막아줍니다.

### NSA (Native Sparse Attention)
- **개념**: 단순 커널 수정을 넘어 모델 학습(Training) 시점부터 3단 구조(Coarse compression + Fine token selection + Sliding window) 어텐션을 하드코딩 형태로 학습시키는 기법입니다.
- **성능**: 64K 컨텍스트 기준 forward 9배, backward 6배, decoding 11.6배 속도 개선을 보고했습니다.

---

## 2. 추론 최적화 및 디코딩 가속

### DSpark: Confidence-Scheduled Speculative Decoding
- **개념**: DeepSeek-V4 추론 엔진에 전면 배치된 Speculative Decoding(추측 디코딩) 기법입니다. 처리량(Throughput) 50% 향상, 지연시간(Latency) 최대 80% 감소를 달성했습니다.
- **메커니즘**:
  - `Heavy parallel head`와 `Light Markov head`를 조합하여 DFlash의 속도와 Eagle의 정확도를 조합합니다.
  - GPU 자원 혼잡 시 검증에 드는 오버헤드를 막기 위해 신뢰도 점수(Confidence score)로 토큰 매칭 확률을 실시간 예측하고, 매칭률이 낮은 경우 검증 단계를 축소하는 동적 분산 처리 기법을 탑재했습니다.

---

## 3. 메모리 및 강화학습(RL) 알고리즘

### Engram: Transformer 장기 기억 외부 모듈
- **개념**: 컨텍스트 윈도우를 마냥 늘리는 기존 방식 대신, 과거 이력의 검색과 보관을 전담하는 외부 메모리 모듈을 구현했습니다.
- **방식**: N-gram 결정론적 lookup 구조를 쓰며 해시 맵으로 검색하여 어텐션 연산 부하를 우회합니다. 또한 캐싱된 메모리를 GPU 메모리가 아닌 호스트 CPU RAM에 거치시키고 prefetch를 통해 필요하기 직전에 GPU로 밀어넣는 병목 우회 아키텍처를 가집니다.

### GRPO (Group Relative Policy Optimization)
- **개념**: DeepSeekMath와 R1-Zero 학습에 사용된 핵심 강화학습 알고리즘입니다.
- **차별점**: PPO 알고리즘에서 많은 메모리를 점유하던 별도의 Critic(가치 판단) 모델을 완벽히 제거했습니다. 대신 동일 문제에 대해 여러 대안적 답변들을 동시 생성하여 그룹(Group)을 묶고, 그룹 내 상대 점수를 기반으로 baseline을 측정하여 학습 자원과 인프라 한계를 대폭 낮췄습니다.

---

## 4. 저레벨 인프라 및 가속화 커널

### FlashMLA + DeepEP + DeepGEMM
- **FlashMLA**: Hopper GPU의 하드웨어 특성에 특화된 MLA (Multi-head Latent Attention) 디코딩 전용 CUDA 커널입니다.
- **DeepEP**: MoE 아키텍처에서 노드 간 전문가(Expert) 라우팅을 진행할 때 올투올(All-to-All) 통신 지연을 최소화하고 부하를 균등 분산하는 라이브러리입니다.
- **DeepGEMM**: FP8 혼합 정밀도(Mixed-precision) 행렬 곱셈을 최대로 가속화하는 커널 라이브러리입니다.

## 🔗 연결된 문서
- [[wiki/Models/Architectures/000_Architectures-MOC.md]]
- [[wiki/Models/Optimization-and-Serving/000_Optimization-and-Serving-MOC.md]]
- [[wiki/Models/RL/000_RL-MOC.md]]
- [[wiki/Models/RL/DeepSeek-R1-GRPO-Implementation.md]]
- [[wiki/Agents/Memory-and-Cognition/000_Memory-and-Cognition-MOC.md]]
- [[index.md]]
