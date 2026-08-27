---
title: "Agent Evaluation Flywheel: 수동 프롬프트 튜닝 탈피를 위한 자동 평가 체계"
related_raw: ["[[raw/Escape Manual Prompt Tweaking with Agent Evaluation Flywheel | Eric Dong님이 토픽에 대해 올림.md]]"]
tags: ['#inbox', '#Agent-Evaluation', '#Prompt-Engineering', '#GEPA', '#LLMOps']
type: "wiki"
status: "published"
last_updated: "2026-08-23"
updated: "2026-08-23"
---

# Agent Evaluation Flywheel: 수동 프롬프트 튜닝 탈피를 위한 자동 평가 체계

## 1. 배경 및 핵심 문제
* **수동 프롬프트 튜닝의 한계**: 특정 예외 케이스(A)를 해결하기 위해 시스템 프롬프트를 임의로 변경하면, 기존에 잘 동작하던 다른 예외 케이스(B)가 망가지는 현상이 반복되어 개발 생산성에 큰 병목이 생깁니다.
* **해결책**: 주관적인 감에 의존한 검사(Vibe checks)를 배제하고 지표 중심의 자동화된 에이전트 성능 평가 순환 구조인 **에이전트 평가 플라이휠(Agent Evaluation Flywheel)** 아키텍처를 도입해야 합니다.

## 2. 에이전트 평가 플라이휠 5단계 아키텍처

### 1단계: 콜드 스타트 합성 사용자 시뮬레이션 (Synthetic User Simulation)
* 프로덕션 로그가 쌓이기 전에, LLM 기반의 사용자 시뮬레이터를 이용하여 가상의 복잡한 다회차(multi-turn) 대화 트레이스를 생성합니다. (예: 대화 도중 말을 바꾸거나, 불완전한 정보를 주거나, 거친 구어체를 쓰는 시나리오).

### 2단계: 실행 궤적 캡처 및 OTel 트레이싱 (Trajectory Capture)
* 단순 출력물 로깅을 넘어, 에이전트의 내부 추론 단계, 도구 선택, 전달 페이로드, 시간 순서별 API 호출 경로가 담긴 전체 실행 흔적을 OpenTelemetry 사양 로그로 정밀 캡처합니다.

### 3단계: 자동 평가기(AutoRaters) 및 샌드박스 검증
* **하이브리드 평가**: 의도 분석과 자연어 논리 평가를 수행하는 LLM-as-a-Judge(AutoRaters)와 샌드박스 환경에서 JSON 스키마, 정규식, 응답 시간(SLA) 제한 준수를 강제하는 결정론적 코드 검증(CodeExecutionMetrics)을 병행합니다.
* **독립성 원칙 (Golden Rule)**: 성능 개선 안을 제안하는 엔진과 결과물을 채점하는 평가 엔진은 완벽히 분리(Decouple)되어야 합니다. 평가 대상 에이전트가 본인의 성적을 직접 채점해서는 안 됩니다.

### 4단계: 에러 자동 분류 및 손실 클러스터링 (Loss Clustering)
* 다수 실패 로그를 수동으로 확인하는 대신, 판정Verdicts을 수집하여 L1/L2 공통 실패 유형으로 클러스터링합니다. (예: "booking API 호출 시 정수형이 아닌 문자열 타입으로 인자가 전달되는 에러가 전체 실패의 73%를 차지함"과 같은 시스템 구조적 분석 도출).

### 5단계: 진화적 프롬프트 엔지니어링 (GEPA)
* 유전-파레토 최적화 알고리즘인 **GEPA (Genetic-Pareto Evolution)**를 구동하여, 다수의 시스템 프롬프트 후보군을 자동으로 교배 및 변이시키면서 평가 지표에 최적화된 프롬프트를 자동으로 찾아 진화시킵니다. (기존 수동 튜닝 대비 약 53%의 상대 성능 향상 가능).
