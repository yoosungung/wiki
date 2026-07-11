---
title: "VibeThinker-3B: Sina Weibo의 초고성능 소형 추론 모델"
tags: ["Models", "Small-Models", "SLM", "Reasoning", "VibeThinker", "Sina-Weibo"]
type: "wiki"
status: "published"
last_updated: "2026-06-18"
updated: "2026-06-18"
related_raw: ["[[2026-06-18-VibeThinker-3B-Sina-Weibo.md]]"]
---

# 🧠 VibeThinker-3B: Sina Weibo의 초고성능 소형 추론 모델

시나 웨이보(Sina Weibo) 연구진이 2026년 발표한 **VibeThinker-3B**는 30억(3B) 매개변수 규모에서 거대 모델(LLM)을 능가하는 추론 성능을 달성하며 '크기 중심 패러다임'에 중대한 전환점을 제시한 모델입니다.

## 1. 개요 및 학습 패러다임
- **기반 모델**: Qwen2.5-Coder (3B)
- **학습 방법론**: **'Spectrum-to-Signal'** 포스트 트레이닝 패러다임 적용.
    - 커리큘럼 기반 지도 미세 조정 (SFT)
    - 다중 도메인 강화 학습 (RL)
    - 오프라인 자기 증류 (Self-Distillation)

## 2. 성능 지표 (Benchmark Results)
VibeThinker-3B는 자신보다 수십 배 큰 DeepSeek V3.2, GLM-5, Gemini 3 Pro와 대등하거나 우월한 성적을 기록했습니다.

| 벤치마크 | 점수 | 비고 |
| :--- | :--- | :--- |
| **AIME'26** | 94.3 / **97.1** | 테스트 타임 스케일링(TTS) 적용 시 97점 돌파 |
| **LiveCodeBench v6** | 80.2 (Pass@1) | 코딩 추론 능력 입증 |
| **LeetCode Recent** | 96.1% | 미학습 최신 문제에 대한 높은 적응력 |
| **IFEval** | 93.4 | 추론 특화 후에도 명령어 제어 능력 유지 |

## 3. 매개변수 압축-커버리지 가설 (Parametric Compression-Coverage Hypothesis)
연구진은 인공지능 발전의 새로운 이정표가 될 핵심 가설을 제안했습니다.

- **추론 코어 (Reasoning Core)**: 수학, 코딩 등 검증 가능한(Verifiable) 추론 영역은 고밀도 소형 모델로 충분히 압축될 수 있음.
- **지식 커버리지 (Knowledge Coverage)**: 광범위한 오픈 도메인 지식이나 일반 목적의 범용 역량에는 여전히 거대 매개변수가 필요함.
- **결론**: 모든 문제를 거대 모델 하나로 해결하기보다, 최적화된 소형 추론 모델과 거대 지식 모델의 **역할 분담 및 상호 보완**이 훨씬 효율적임.

## 4. 시사점
- 소형 모델이 단순히 비용 절감을 위한 하위 대체재가 아니라, 특정 영역에서 최고 수준의 성능을 발휘하는 독립적인 경로임을 증명.
- 온디바이스 AI 및 에이전트 워크플로우에서 고성능 추론 엔진으로서의 활용 가능성 극대화.

---
**관련 문서**:
- [[wiki/Models/Small-Models/000_Small-Models-MOC.md]]
- [[wiki/Models/Reasoning-and-Cognition/000_Reasoning-and-Cognition-MOC.md]]
