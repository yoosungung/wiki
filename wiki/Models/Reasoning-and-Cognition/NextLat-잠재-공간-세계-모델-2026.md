---
related_raw: ["[[2026-06-25-NextLat_Next_Latent_Prediction_World_Models.md]]", "[[2026-06-29-nextlat-latent-space-world-model.md]]"]
tags: ["#wiki", "World-Models", "Next-Latent-Prediction", "Reasoning", "Speculative-Decoding"]
---

# NextLat: 잠재 공간 기반 컴팩트 세계 모델

마이크로소프트 리서치(MSR)가 발표한 **NextLat (Next-Latent Prediction)**은 기존 언어 모델들의 근본적인 한계인 '다음 토큰 예측(Next-Token Prediction)' 방식에서 한 단계 더 진화하여, 잠재 상태 공간(Latent Space) 자체에서 전이 법칙을 예측하도록 설계된 신개념 아키텍처입니다.

## 1. 아키텍처 및 메커니즘
기존 트랜스포머가 직전의 텍스트 토큰을 입력받아 다음 단어만을 맞추는 데 그쳤다면, NextLat은 자기지도 학습 방식의 **자기지도형 다음 잠재 상태 예측(self-supervised next-latent prediction)** 목적 함수를 도입합니다.
- **경량 다이내믹스 모델**: 현재 프레임의 hidden state와 다음 입력 토큰 데이터를 조합하여, 다음 차례의 고차원 잠재 상태(latent state)를 직접 예측합니다.
- **신념 상태(Belief States) 구축**: 개념과 상황의 인과관계를 일관되게 구조화한 '신념 상태'를 잠재 공간 내에 형성하여, 단순 텍스트 표면 정렬이 아닌 내부적 시뮬레이션을 가능케 합니다.

## 2. 주요 성능 및 실용적 장점
- **세계 모델링(World Modeling)**: 불필요한 표면 텍스트 노이즈를 필터링하고 추론과 기획(Planning)에 필요한 본질적 정보만을 잠재 공간에 압축 저장하여, 고난도 추론 작업의 논리적 연속성을 확보합니다.
- **추론 속도 혁신 (자가 추측성 디코딩)**: 구조화된 잠재 공간을 기반으로 **가변 길이 자가 추측성 디코딩(variable-length self-speculative decoding)**을 수행합니다. 별도의 대형 드래프트 모델 없이도 아키텍처 오버헤드나 병렬 학습 효율성을 훼손하지 않으면서도 추론 속도를 **최대 3.3배** 가속화합니다.

## 🔗 연결된 문서
- [[wiki/Models/Optimization-and-Serving/DFlash-병렬-추측-디코딩-및-SGLang-V2-가속.md]] — 또 다른 추측 디코딩 기술인 블록 디퓨전 및 KV Injection 가속 구조.
- [[index.md]]
