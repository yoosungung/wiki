---
title: "Inkling 및 Inkling-Small: Thinking Machines Lab의 Sparse MoE 아키텍처"
last_updated: "2026-07-31"
updated: "2026-07-31"
related_raw: ["[[raw/2026-07-28-thinking_machines_lab_inkling_975b_moe.md]]", "[[raw/2026-07-28-sebastian_raschka_notable_open_weight_models.md]]", "[[2026-07-31-thinking-machines-inkling-small-release.md]]"]
tags: [Models, Architectures, MoE, Inkling, Inkling-Small, Thinking-Machines-Lab, Open-Source-LLM]
---

# Inkling: 975B Sparse MoE 오픈소스 대규모 언어 모델 아키텍처

이 문서는 OpenAI 전 CTO 미라 무라티(Mira Murati)가 설립한 Thinking Machines Lab이 2026년 7월 공개한 최초의 미국산 플래그십 오픈소스 모델인 **Inkling**의 아키텍처 및 학습 방법론을 분석합니다.

---

## 1. 개요

**Inkling**은 975B parameter 규모의 Sparse Mixture-of-Experts(MoE) 아키텍처를 채택한 범용 오픈소스(Apache-2.0) 대규모 언어 모델입니다. 미국 인공지능 연구 기업이 중국의 초거대 오픈소스 모델 독주 체제(DeepSeek, Qwen 등)에 대응하기 위해 내놓은 전략 모델로, 텍스트 뿐만 아니라 오디오(Audio)까지 기본 네이티브 지원하는 강력한 멀티모달 능력을 특징으로 합니다.

---

## 2. 핵심 아키텍처 명세 및 성능 분석

### 2.1. 하이브리드 아키텍처 세부
- **활성 매개변수 (Active Parameters)**: 토큰당 41B개의 파라미터만 활성화되어 추론 연산 효율성을 극대화합니다.
- **컨텍스트 윈도우**: 최대 1,000,000 토큰(1M context)을 완전히 수용합니다.
- **구조적 장치 (Structural Features)**:
  - 글로벌 레이어의 Positional bias를 완화하기 위한 특수 구조 설계.
  - 임베딩 계층의 정규화를 위한 **Embedding RMSNorm** 도입.
  - 정보 믹싱을 위한 **Short Convolutions** 필터 적용.

### 2.2. 성능 벤치마크 및 비교
Sebastian Raschka의 분석에 따르면 Inkling은 일반 지식 및 대화 영역에서는 압도적이나, 전문 코딩/에이전트 벤치마크에서는 보완이 필요한 특성을 보입니다:
- **IFBench (대화형 지시 이행)**: 79.8% 달성 (GLM-5.2 대비 우위).
- **SimpleQA Verified (사실 검증)**: 43.9% 달성.
- **Specialized Benchmarks (SWE-Bench Pro, Terminal-Bench 2.1)**: 이 부문에서는 GLM-5.2 및 DeepSeek V4 Pro 대비 하위 등급의 성적을 기록하여, 에이전트 용도로 활용하기 위해서는 추가적인 미세 조정(Tinkering)이 필요함.

```text
                  오픈소스 대용량 모델 성능 포지셔닝 (2026)
                  ========================================
                  
     Nemotron 3 Ultra / Kimi K2.5 < Inkling 975B < GLM 5.2 / Kimi 2.6 / DeepSeek V4 Pro
```

---

## 3. 학습 혁신: Muon 옵티마이저 (Muon Optimizer) 도입

Inkling의 훈련 효율성을 극적으로 올릴 수 있었던 핵심 요인 중 하나는 기존의 AdamW 대신 **Muon(Mu-orthogonalizer)** 옵티마이저를 훈련 표준으로 채택한 점입니다.

- **Muon의 장점**:
  - 행렬 직교화(Orthogonalization) 업데이트 기법을 통해 그라디언트 업데이트의 방향성을 정밀하게 교정합니다.
  - AdamW 대비 토큰당 학습 효율을 30~40% 이상 높여, 초대형 975B 모델을 제한된 GPU 인프라 내에서 가속 훈련할 수 있게 합니다.

---

## 4. Inkling-Small 모델의 출시 (2026-07-30 추가)

Thinking Machines Lab은 플래그십 모델의 성능을 준수하게 유지하면서 배포 비용을 획기적으로 낮춘 **Inkling-Small** 모델을 2026년 7월 30일에 추가 릴리스했습니다.
- **아키텍처 스펙**: 총 **2,760억 파라미터 (276B Parameters)** 규모이며, 토큰당 **12B 파라미터가 활성화**되는 Sparse MoE 구조입니다.
- **성능적 특징**: 플래그십 대비 약 3배 경량화되었음에도 불구하고, 대다수의 코딩 및 복합 추론 벤치마크에서 플래그십 Inkling (975B) 모델의 초기 버전과 대등하거나 더 뛰어난 효율적 성과를 기록했습니다.
- **조정 가능한 생각 노력 (Controllable Thinking Effort)**: 사용자가 추론 시간 및 연산 비용 대비 답변의 품질 밸런스를 조절할 수 있는 '생각 노력량 제어' 기능을 네이티브 지원합니다.
- **배포 및 통합**: BF16, FP8, MXFP8, NVFP4 등 최신 수치 표현 방식을 폭넓게 지원하여 로컬 단일 서버에서도 고속 구동이 용이합니다.

---

## 5. 실무 개발자를 위한 가이드

1.  **Thinking Machines Lab의 Tinker API**:
    - 자체 API 플랫폼인 **Tinker**를 통해 Inkling 및 Inkling-Small 모델의 커스텀 파인튜닝을 지원하므로, 특수 도메인(예: 보안, 법률) 데이터 기반의 에이전트 전용 모델로 경량 정렬하기 용이합니다.
2.  **VRAM 및 서빙 하드웨어 요구사항**:
    - 총 975B 파라미터 규모인 Inkling의 경우 FP8 양자화 적용 시에도 수백 GB의 VRAM이 요구되어 NVIDIA RTX Spark 등 특화 시스템이 권장되나, **Inkling-Small (276B)**은 FP8 양자화 상태에서 보다 컴팩트한 VRAM 점유를 보여 멀티 GPU 워크스테이션 환경에서도 로컬 단독 구동이 수월합니다.

---

## 🔗 관련 문서 링크
- 모델 아키텍처 MOC: [[wiki/Models/Architectures/000_Architectures-MOC.md]]
- 최신 아키텍처 동향: [[wiki/Models/Architectures/Recent-LLM-Architecture-Developments.md]]
- [[wiki/Models/000_Models-MOC.md]]
- [[INDEX.md]]
