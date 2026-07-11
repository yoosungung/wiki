---
title: "DeepEval: 유전 알고리즘 기반 프롬프트 자동 최적화 (GEPA)"
related_raw: ["[[Most teams run evals, look at failures, guess what's wrong, rewrite the prompt, then repeat. It's slow and you never know if your rewrite actually fixes… | Sumanth P | 댓글 13.md]]"]
tags: ["Engineering", "Prompt-Engineering", "Optimization", "Genetic_Algorithm", "DeepEval", "GEPA"]
type: "wiki"
status: "published"
last_updated: "2026-05-15"
updated: "2026-05-15"
---

# DeepEval: '추측'이 아닌 '진화'로 완성하는 프롬프트 엔지니어링

## 1. 개요
DeepEval은 수동으로 프롬프트를 수정하고 테스트하는 반복적이고 비효율적인 과정을 **유전 알고리즘(Genetic Algorithm)**을 통해 자동화하는 오픈소스 프롬프트 최적화 프레임워크입니다. 특히 GEPA(Genetic Evolution with Pareto Selection) 알고리즘을 활용하여 다양한 지표를 동시에 만족하는 최적의 프롬프트를 찾아냅니다.

## 2. GEPA 작동 원리 (4단계 루프)
1.  **데이터셋 분할**: 테스트 케이스를 '검증용'과 '피드백용'으로 나눕니다.
2.  **부모 선정 및 변이**: 우수한 성능을 보인 부모 프롬프트를 선정하고, LLM을 사용하여 실패 케이스의 피드백을 반영한 변이(Mutation)를 생성합니다.
3.  **적합도 평가**: 변이된 프롬프트 후보군을 50개 이상의 빌트인 지표(답변 관련성, 환각 여부, 편향 등)로 평가합니다.
4.  **파레토 선택(Pareto Selection)**: 여러 상충하는 목표들 사이에서 최적의 트레이드오프를 가진 후보들을 다음 세대로 넘깁니다.

## 3. 주요 특징
- **자동화된 피드백 루프**: 사람이 "왜 틀렸을까?" 고민하는 대신, 알고리즘이 에러 로그를 분석하여 프롬프트의 구체적인 부분을 수정합니다.
- **다목적 최적화**: 정확도, 비용, 응답 속도 등 여러 목표를 동시에 최적화할 수 있습니다.
- **검증된 지표**: 50개 이상의 표준화된 평가 지표를 내장하고 있어 신뢰도 높은 평가가 가능합니다.

## 4. 시사점
프롬프트 엔지니어링이 예술(Art)의 영역에서 공학(Engineering)과 최적화(Optimization)의 영역으로 진화하고 있음을 보여줍니다. 특히 복잡한 RAG 시스템이나 멀티스텝 에이전트에서 프롬프트의 미세한 변화가 결과에 큰 영향을 미칠 때 DeepEval과 같은 자동화 도구는 필수적입니다.

## 관련 문서
- [[wiki/Engineering/Prompt-Engineering/000_Prompt-Engineering-MOC.md|프롬프트 엔지니어링 MOC]]
- [[wiki/Agents/Evaluations/000_Agents-Evaluations-MOC.md|에이전트 평가 MOC]]
- [[wiki/Models/RL/000_RL-MOC.md|강화학습 MOC]]
