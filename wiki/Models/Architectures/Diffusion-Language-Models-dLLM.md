---
title: Diffusion Language Models (dLLM) 아키텍처 및 연구 동향
last_updated: "2026-07-31"
updated: "2026-07-31"
related_raw: ["[[2026-07-27-icml_2026_best_diffusion_llm_papers.md]]", "[[2026-07-31-kiwoong-yeom-autoregressive-diffusion-hybrid-llm.md]]"]
tags: [Models, Architectures, Diffusion-LLM, dLLM, ICML-2026]
---

# Diffusion Language Models (dLLM) 아키텍처 및 연구 동향 (ICML 2026)

이 문서는 ICML 2026에서 최우수 논문(Best Paper) 2편으로 선정된 Diffusion LLM(dLLM)의 핵심 아키텍처 한계 극복 기법과 샘플링 가속 공식을 정리합니다.

## 1. 순차 생성(AR) vs. 디퓨션 생성(dLLM) 비교

| 특성 | 순차 생성 (Autoregressive, AR) | 디퓨션 언어 모델 (dLLM) |
| :--- | :--- | :--- |
| **방향성** | 왼쪽에서 오른쪽으로 일방향성 생성 | 양방향 문맥 교정 및 전체 캔버스 덧칠 |
| **병렬화** | 다음 토큰 생성이 이전 토큰에 종속되어 불가능 | 전체 토큰을 노이즈 제거(Denoising)를 통해 병렬 생성 |
| **속도** | 1,000단어 생성 시 1,000번의 순방향 패스 필요 | 단 10~20번의 스텝으로 문서 일괄 생성 가능 |
| **오류 복구**| 이미 내뱉은 말은 뒤에서 수정 불가능 (CoT 필수) | 생성 도중 자유롭게 앞뒤 문맥에 맞춰 토큰 수정(퇴고) 가능 |

## 2. ICML 2026 최우수 연구 돌파구

### 2.1. 유연성의 함정 극복 (The Flexibility Trap) - 칭화대/알리바바
- **문제 진단**: 디퓨션의 양방향 자유도로 인해 코딩이나 수학 추론 도중 어려운 논리적 구간을 우회하고 쉬운 단어부터 채우려다 구조적 모순에 빠지는 '유연성의 함정'을 발견했습니다.
- **해결 방안 (JustGRPO)**: 강화학습(GRPO) 학습 과정에서 디퓨션 디노이징 방향을 GPT와 같이 좌에서 우로 엄격히 순차 진행하도록 보상을 구성하여 추론 일관성을 보장했습니다.
- **결과**: 디퓨션 학습 리소스 비용을 **75% 절감**하고, H100 16대로 단 20분 만에 학습하여 GSM8K 수학 성능을 81%에서 89.1%로 가속시켰습니다.

### 2.2. 샘플링 속도 가속화 (High-Accuracy Sampling) - 예일대/MIT
- **문제 진단**: 확률 밀도 함수의 스코어를 정확히 모르기 때문에 잔여 에러를 잡고자 수만 번의 점진적 다항식 붓질(Denoising Step)을 돌아야만 하여 속도가 극도로 느렸습니다.
- **해결 방안**: 미지의 고차원 스코어 함수를 구하려 애쓰는 대신, 기 수립된 그래디언트 정보의 범위 내에서 필터링을 가하는 **거부 샘플링 (Rejection Sampling)** 공식으로 대체 증명했습니다.
- **결과**: 기존의 수천 번의 스캔 붓질 스텝을 **10~20번 수준(로그 스케일)으로 지수적 단축**하는 수학 공식을 증명하여 dLLM의 추론 속도 지연을 극복했습니다.

## 3. 대표적인 dLLM 모델군 및 실무 가이드
- **iLLaDA**: Pre-training 전 과정에 dLLM 방식을 적용하여 양방향 자연어 복원 능력을 최적화한 모델.
- **diffusiongemma-26B-A4B-it**: 구글에서 릴리스한 에지 지향 실용 디퓨션 모델.
- **구동 CLI 구조 예시**:
  dLLM 라이브러리를 이용하여 양방향 마스킹 빈칸 채우기를 수행할 때의 개념적 파이프라인 예시입니다.
  ```python
  from dllm_runner import DiffusionGemmaPipeline

  # 1. 디퓨션 Gemma 파이프라인 로드
  pipeline = DiffusionGemmaPipeline.from_pretrained("google/diffusiongemma-26B-A4B-it")

  # 2. 마스킹 프롬프트 준비 (양방향 빈칸 채우기)
  prompt = "The capital of [MASK] is Paris, which is located in [MASK] Europe."

  # 3. 거부 샘플링 필터를 사용해 15 step만에 디노이징 실행
  completed_text = pipeline.denoise(
      prompt,
      steps=15,
      sampling_method="rejection_sampling"  # MIT-Yale 가속 기법 적용
  )
  print(completed_text)
  # 출력: "The capital of France is Paris, which is located in Western Europe."
  ```

---
## 🔗 관련 문서 링크
- [[wiki/Models/Architectures/Autoregressive-Diffusion-Hybrid-LLM.md]] — AR과 Diffusion의 장점을 결합한 하이브리드 언어 모델.
- SFT와 RL의 중복 없는 학습 전략: [[wiki/Models/Reasoning-and-Cognition/SFT-vs-RL-Compositional-Generalization.md]]
- 적응형 추론 미들웨어 설계: [[wiki/Models/Optimization-and-Serving/Adaptive-Inference-Routing-Fastino-Pioneer.md]]
