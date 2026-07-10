---
title: "AI 에이전트 평가 방법론 및 도구"
related_raw: ["[[wiki/Agents/Evaluations/AI-Agent-Evaluation.md]]", "[[wiki/Agents/Evaluations/HAL-Holistic-Agent-Leaderboard.md]]"]
tags: ['wiki', 'agents', 'evaluation', 'methodology', 'observability']
type: "wiki"
status: "published"
last_updated: "2026-04-20"
---

# AI 에이전트 평가 방법론

AI 에이전트의 신뢰성을 확보하기 위해 단순히 최종 답변을 확인하는 것을 넘어, 사고 과정(Trace)과 시스템 구조(Scaffold)를 포함한 종합적인 평가가 필요합니다.

## 1. 세 가지 유형의 평가자 (Graders)
에이전트 평가를 위해 목적에 맞는 평가자 유형을 선택해야 합니다:
- **코드 기반 평가자 (Code-Based)**: 빠르고 객관적이지만, 문자열 매칭 등 유효한 변형에 취약함.
- **모델 기반 평가자 (Model-Based)**: 유연하고 개방형 작업 처리가 가능하나, 비결정적일 수 있음. (LLM-as-a-Judge)
- **인간 평가자 (Human)**: 가장 고품질이며 주관적 출력 평가에 필수적이나, 비용과 시간이 많이 소요됨.

## 2. 핵심 성공 지표 (Metrics)
단순 성공률을 넘어 서비스 특성에 맞는 지표를 사용합니다:
- **pass@k**: k번의 시도 중 최소 한 번 성공할 확률. (코딩 에이전트 등 개발 지원 도구에 적합)
- **pass^k**: k번의 시도가 모두 성공할 확률. (고객 대면 시스템 등 높은 신뢰성이 요구되는 경우)

## 3. 에이전트 유형별 특화 전략
- **코딩 에이전트**: 소프트웨어 테스트 기반의 결정적 평가가 효과적임. (SWE-bench 등)
- **대화형 에이전트**: 작업 완료도, 효율성(불필요한 턴 제한), 상호작용 품질(루브릭 활용)을 다차원 측정.
- **연구 에이전트**: 근거 확인(Groundedness), 정보 커버리지, 출처 품질을 동시에 검증.

## 4. 에이전트 평가 8단계 로드맵
1. **실제 실패 사례로 시작**: 20-50개의 사례만으로도 충분한 초기 평가셋이 됨.
2. **수동 테스트의 전환**: 사용자 신고 및 지원 이슈를 평가 케이스화.
3. **명확한 작업(Task) 정의**: 도메인 전문가가 합의할 수 있는 명확한 기준 수립.
4. **균형 잡힌 데이터셋**: 성공 케이스와 실패 케이스의 비중 조절.
5. **견고한 테스트 환경(Harness)**: 깨끗한 환경 격리로 상태 오염 방지.
6. **사려 깊은 평가자 선택**: 결과 중심 평가 및 부분 점수 도입, 인간 기반 보정.
7. **대화 기록(Transcript) 분석**: "Read the transcripts" - 실패 원인을 심층 분석하여 평가 자체의 오류인지 구분.
8. **포화(Saturation) 모니터링**: 기존 평가가 포화되면 회귀 테스트로 전환하고 새로운 과제 도입.

## 5. 핵심 평가 및 관측 도구
- **Opik (by Comet)**: 사고 과정(Trace) 실시간 기록 및 병목 분석.
- **G-Eval**: CoT 기반의 의미적 평가 프레임워크.
- **HAL (Holistic Agent Leaderboard)**: 정확성, 비용, 스캐폴드 설계를 종합 고려.

## 관련 문서
- [[wiki/Agents/Evaluations/Judge-Model-Comparison.md|Judge 모델 비교 분석]]
- [[wiki/Agents/Evaluations/Deep-Agent-Evaluation-Framework.md|Deep Agent 평가 프레임워크]]
- [[wiki/Agents/Frameworks/Evaluations/000_Evaluations-MOC.md|Evaluations-MOC]]
