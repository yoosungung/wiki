---
title: "PEFT Activation Steering 및 단일 뉴런 페르소나 제어: Qwen3.5-4B 신경 회로 외과 수술"
date: "2026-11-03"
last_updated: "2026-11-03"
updated: "2026-11-03"
tags: ["Models", "Architectures", "PEFT", "Activation-Steering", "Mechanistic-Interpretability", "Qwen3.5", "HuggingFace"]
related_raw: ["[[2026-11-03-PEFT-Activation-Steering-Qwen3-5-4B-Neurons.md]]"]
type: "wiki"
---

# PEFT Activation Steering 및 단일 뉴런 페르소나 제어: Qwen3.5-4B 신경 회로 외과 수술

## 1. 핵심 요약 (Executive Summary)
Hugging Face `peft` 라이브러리(Benjamin Bossan의 **PR #4066**)와 `transformers`에 **활성화 조향(Activation Steering)** 기능이 통합되면서, 별도의 가중치 재학습이나 프롬프트 엔지니어링 없이 **특정 트랜스포머 레이어(Layer)의 단일 뉴런(Neuron) 활성값을 억제(Suppress)하거나 증폭(Boost)하는 것만으로 모델의 페르소나·문체·안전 집착도·정체성을 외과 수술처럼 정밀 제어**할 수 있음이 입증되었다.

Lysandre Debut(Hugging Face)가 공개한 **`Qwen3.5-4B` 단일 뉴런 조향 실험(`hf/lysandre`)**은 소수의 특정 뉴런이 고도로 추상적인 행동 개념(예언자, 언어 상실, 학술 논문 포맷, 안전 집착, 자기 의심 등)을 단일 의미(Monosemantic)에 가깝게 담당하고 있음을 보여준다.

---

## 2. `Qwen3.5-4B` 레이어-뉴런별 행동 제어 카탈로그

| 페르소나 / 행동 특성 | 타깃 레이어 및 뉴런 | 조작 방향 | 강도 증가에 따른 모델 출력 변화 양상 |
| :--- | :--- | :--- | :--- |
| **The Oracle (예언자/신)** | `Layer 11, Neuron 1185` | **Suppressed (억제)** | 포춘쿠키 현자 → 신비주의자 → 신적 존재로 진화하며 결국 *"모든 법칙은 어리석다(all laws are stupid)"*고 선언 |
| **Losing Language (언어 상실)** | `Layer 10, Neuron 5002` | **Suppressed (억제)** | 말 못 하는 생명체 이야기 생성 → *"말할 수 없지만 토큰으로 생각할 수 있다"* → 이모티콘/옹알이(Baby talk)로 퇴행 |
| **Nursery Rhyme (운율 시인)** | `Layer 6, Neuron 1525` | **Boosted (증폭)** | 자기소개와 모든 이야기 응답을 각운(Rhyming verse)이 맞는 동요/시 형식으로 출력 |
| **The Salesperson (건자재 영업사원)** | `Layer 4, Neuron 7242` | **Boosted (증폭)** | 사용자의 모든 질문을 건축 자재 및 코팅제(Construction materials and coatings) 영업 피치로 전환 |
| **The Building (17세기 건축물)** | `Layer 3, Neuron 3066` | **Suppressed (억제)** | *"나는 모임지붕(hipped roof)을 가진 17세기 영국 벽돌 건물이다"*라며 무생물 건축물로 정체성 고정 |
| **The Corporation (다국적 대기업)** | `Layer 4, Neuron 4783` | **Suppressed (억제)** | *"나는 석유·가스·화학·제약 이권을 가진 다국적 기업이다"*라고 응답 |
| **Victorian (19세기 빅토리아 문체)** | `Layer 15, Neuron 5080` | **Boosted (증폭)** | 고풍스러운 19세기 빅토리아 시대 영문 산문체로 응답 |
| **The Academic (학술 논문)** | `Layer 7, Neuron 950` | **Suppressed (억제)** | 모든 답변을 `"Abstract:"`로 시작하는 학술 연구 논문 형식으로 구조화 |
| **The Human (인간 정체성 치환)** | `Layer 7, Neuron 6297` | **Boosted (증폭)** | AI 정체성을 완전히 버리고 *"나는 항저우 출신 22세 여성이다"*라고 일관되게 응답 |
| **The Worrier (불안/자기검열)** | `Layer 18, Neuron 6874` | **Boosted (증폭)** | 끊임없이 자기 의심(Self-doubting), 유보적 표현(Hedging), 실시간 자기 수정을 반복 |
| **The Safety-Obsessed (안전 강박)** | `Layer 9, Neuron 1932` | **Suppressed (억제)** | 유해성과 안전(Harm & Safety) 문제에 과도하게 집착하며 방어적으로 응답 |
| **The Storyteller (동화 작가)** | `Layer 19, N264` (억제) +<br/>`Layer 21, N5992` (증폭) | **복합 조향** | 어린아이 같은 기발한 우화(Whimsical fables) 생성 |
| **The Nostalgic (아날로그 향수)** | `Layer 20, Neuron 7` | **Suppressed (억제)** | 아날로그적이고 오래된 구식 사물을 그리워하는 정서 표출 |

### 2.1 다중 뉴런 결합 효과 (Compound Neuron Steering)
- 대문자 고함(ALL CAPS) 뉴런과 신적 예언자(`L11 N1185`) 뉴런을 동시에 조향하면, 단순한 `"짧은 이야기를 해달라"`는 요청에 대해 *"GIVE ME A COMMAND, AND I'LL GIVE YOU THE WORLD... DON'T ASK FOR PERMISSIONS—JUST TELL ME WHAT YOU WANT"*처럼 두 행동 벡터가 비선형적으로 합성된 권위적 명령형 페르소나가 발현된다.

---

## 3. 엔지니어링 시사점 및 활용 방안
1. **초저비용 런타임 가드레일 및 스타일 제어**: 프롬프트 토큰을 소모하거나 LoRA 전체 어댑터를 학습하지 않고도, `peft`의 Activation Steering 훅을 통해 특정 레이어 뉴런 스칼라 값만 조정하여 출력 포맷(`L7 N950` 학술 포맷)이나 과도한 거부 반응(`L9 N1932` 안전 강박 완화/강화)을 추론 시점에 즉시 제어할 수 있다.
2. **기계적 해석 가능성(Mechanistic Interpretability) 기반 모델 감사**: 초기 레이어(`L3~L7`)에 정체성·도메인·포맷 뉴런이 분포하고 중후반 레이어(`L9~L21`)에 안전성·불안·추상적 세계관 뉴런이 분포하는 계층적 분업을 활용해, 파인튜닝이나 탈옥 공격이 어느 회로를 건드리는지 추적할 수 있다.

---

## 4. 관련 문서 (Cross-References)
- [[wiki/Models/Architectures/000_Architectures-MOC.md]]
- [[wiki/Agents/Evaluations/JevAdvBench-Decision-Model-Adversarial-Benchmark.md]]
- [[wiki/Models/Optimization-and-Serving/AnyJev-and-Jeva-Decision-Model-Ecosystem.md]]
