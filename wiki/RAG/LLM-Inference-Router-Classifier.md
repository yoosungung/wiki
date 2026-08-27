---
title: "SCX ai Router: 오픈소스 LLM 비용·성능 최적화 라우팅 분류기"
related_raw: ["[[raw/Optimizing Open Source Models for Speed, Cost, and Quality | Aleks Smechov님이 토픽에 대해 올 림.md]]"]
tags: ['#inbox', '#LLMOps', '#LLM-Routing', '#SCX-ai', '#Cost-Optimization']
type: "wiki"
status: "published"
last_updated: "2026-08-23"
updated: "2026-08-23"
---

# SCX ai Router: 오픈소스 LLM 비용·성능 최적화 라우팅 분류기

## 1. 개요
* **정의**: SCX ai와 Knowledgator 연구그룹이 공동 개발한 **Router**는 LLM 서비스 운영 시 속도, 비용, 품질의 균형을 맞추기 위해 입력된 요청을 분석하고 가장 적합한 오픈소스/상용 LLM 모델로 분기시켜 주는 Apache 2.0 라이선스의 초경량 라우팅 분류기 모델입니다.
* **등장 배경**: 대규모 워크로드 환경에서 모든 입력을 가장 똑똑하고 비싼 모델로 보내는 대신, 단순 요약이나 정보 추출은 작고 빠른 로컬 모델로 라우팅하여 전체 인퍼런스 비용을 극적으로 절감합니다.

## 2. 기술적 작동 방식 및 스펙
* **모델 구조**: **Qwen3-0.6B** 및 **GLiClass** 백본 모델을 기반으로 특정 목적에 맞춰 미세조정(Fine-tuned)되었습니다.
* **레이턴시**: 일반 소비자용 GPU 환경에서도 요청당 **50ms 미만**으로 분류를 완료해 라우팅에 따르는 지연 시간을 최소화합니다.
* **인텐트 분석 (28개 카테고리)**:
  - 입력 프롬프트를 요약, 예측, 계획, 생성 등 **28가지 태스크 유형**으로 판별합니다.
  - 요청의 잠재적 난이도와 예상 출력 길이를 계산합니다.
  - 값비싼 토큰을 소모하는 추론 전용 모델(Reasoning Model)을 반드시 활성화해야 하는 연산인지를 판별합니다.
* **동적 모델 매핑**: 분류 데이터를 매핑 함수에 대입하여 최적의 기본(Primary) 모델 및 실패 대비 백업(Backup) 모델을 실시간 선택합니다. (예: SCX.ai가 보유한 74개 오픈 가중치 모델 풀 및 Claude 5 Opus 등 상용 API를 결합한 분기 처리).
