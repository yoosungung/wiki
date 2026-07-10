---
related_raw: ["[[2026-06-29-dllm-diffusion-language-model-library.md]]"]
tags: ["#wiki", "Diffusion-Models", "Language-Models", "DeepSpeed", "LoRA"]
---

# dllm: 확산 기반 언어 모델 학습 및 평가 라이브러리

**dllm**은 복잡한 학습 루프나 노이즈 스케줄링 파이프라인의 구축 없이도 확산 기반 언어 모델(Diffusion-based Language Models)을 손쉽게 빌드, 학습, 평가할 수 있도록 돕는 오픈소스 라이브러리입니다.

## 1. Autoregressive 언어 모델 vs. Diffusion 언어 모델

| 구분 | Autoregressive (AR) 모델 | Diffusion 언어 모델 |
| :--- | :--- | :--- |
| **생성 메커니즘** | 토큰 단위 순차 예측 (Next-token prediction) | 노이즈 주입 텍스트의 다단계 디노이징 (Denoising) |
| **속도** | 학습/추론이 비교적 빠르고 단순함 | 다단계 디노이징 과정으로 추론 속도가 느림 |
| **글로벌 인과성** | 노출 편향(Exposure bias) 발생 가능, 장문 일관성 한계 | 글로벌 추론 능력이 뛰어남, 장문 작업 강건성 확보 |
| **누적 오류** | 앞 단계의 오류가 뒤 단계로 누적됨 (Cascading errors) | 전체 텍스트 단위 재구성으로 누적 오류 최소화 |

## 2. dllm 라이브러리 주요 기능
- **통합 워크플로우**: 설정 파일(config) 중심 설계로 간편하게 확산 언어 모델 훈련 파이프라인 구성 가능.
- **분산 학습 지원**: LoRA, DeepSpeed, FSDP(Fully Sharded Data Parallel)를 네이티브 지원하여 대형 스케일 모델 훈련 가능.
- **모듈형 설계**: 새로운 확산 아키텍처나 전이 모델 실험을 위한 컴포넌트 커스터마이징 용이.
- **내장 평가 유틸리티**: 학습 런(runs) 및 소거 실험(ablations)에 대한 체계적인 비교·평가 도구 기본 내장.

## 🔗 연결된 문서
- [[wiki/Models/Architectures/000_Architectures-MOC.md]]
- [[index.md]]
