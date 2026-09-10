---
title: "PyTorch로 만드는 밑바닥부터 시작하는 LLM (rasbt/LLMs-from-scratch)"
related_raw: ["[[Build GPT-like LLM in PyTorch from Scratch | AI Engineering님이 토픽에 대해 올림 | LinkedIn.md]]"]
tags: ["Models", "Architectures", "PyTorch", "Education", "GPT", "Deep_Learning"]
type: "wiki"
status: "published"
last_updated: "2026-05-15"
updated: "2026-05-15"
---

# LLM을 '진짜' 이해하는 가장 빠른 길: 밑바닥부터 구현하기

## 1. 개요
Sebastian Raschka(rasbt)가 공개한 `LLMs-from-scratch` 레포지토리는 외부 API 사용이 아닌, 순수하게 Python과 PyTorch만을 사용하여 GPT 스타일의 LLM을 구축, 사전 학습(Pretraining), 파인튜닝(Finetuning)하는 전 과정을 다루는 교육용 리소스입니다.

## 2. 주요 학습 커리큘럼 (7개 챕터)
1.  **데이터 처리**: 텍스트 데이터 토큰화 및 BPE(Byte Pair Encoding) 구현.
2.  **어텐션 메커니즘**: Multi-head Attention을 밑바닥부터 코딩.
3.  **GPT 모델 구축**: 전체 트랜스포머 아키텍처 조립.
4.  **사전 학습**: 라벨링되지 않은 대량의 데이터로 모델 학습.
5.  **파인튜닝**: 텍스트 분류 및 지시 이행(Instruction Following) 학습.
6.  **정렬(Alignment)**: DPO(Direct Preference Optimization)를 통한 인간 가치 정렬.
7.  **최신 모델 구현**: Llama 3.2, Qwen3, Gemma 3 등 최신 아키텍처 구현체 포함.

## 3. 핵심 기술 요소
- **KV Cache 및 GQA**: 추론 속도 최적화를 위한 기법.
- **LoRA (Low-Rank Adaptation)**: 효율적인 파인튜닝 기법.
- **MoE (Mixture of Experts)**: 모델 규모 확장을 위한 아키텍처.
- **추론 시간 스케일링**: 강화학습(RL)과 연계된 성능 향상 기법.

## 4. 학습의 의의
- **블랙박스 해소**: 모델의 내부 작동 원리를 수식과 코드로 직접 확인하여 AI에 대한 깊은 통찰력 확보.
- **실무 적용 능력**: 단순 라이브러리 사용을 넘어, 특정 비즈니스 문제에 맞춰 모델을 커스터마이징할 수 있는 기초 체력 배양.
- **개인용 하드웨어 활용**: 고가의 GPU 클러스터가 아닌 일반 랩탑에서도 실행 가능한 실용적인 예제 중심.

## 관련 문서
- [[wiki/Models/Architectures/000_Architectures-MOC.md|모델 아키텍처 MOC]]
- [[wiki/Models/SFT/000_SFT-MOC.md|SFT (Finetuning) MOC]]
- [[wiki/Models/Architectures/트랜스포머 코드 분석 - PyTorch 구현.md|트랜스포머 코드 분석 상세]]
