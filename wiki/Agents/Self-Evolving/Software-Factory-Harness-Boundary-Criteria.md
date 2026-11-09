---
id: software-factory-harness-boundary-criteria
title: "Software-Factory Harness 경계 기준 (run 정의)"
status: canonical
owner: km
updated: "2026-11-10"
last_updated: "2026-11-10"
review_after: "2027-02-10"
sources:
  - https://arxiv.org/abs/2611.06946
tags: ["Agents", "Self-Evolving", "Software-Factory", "Harness", "Orchestration"]
type: wiki
---

# Software-Factory Harness 경계 기준 (run 정의)

Hua (arXiv:2611.06946, 2026-11) *Beyond the Agent Harness: Boundary Criteria for Software-Factory Orchestration* — 코딩 에이전트 하네스 **위**에 다수 런을 CD로 묶는 계층의 존재 자체가 기여가 아니라, **메커니즘·실패가 어느 층에 속하는지**를 가르는 규칙이 부족하다는 문제 제기.

## 경계 (operational run)

| 층 | 판정 |
| :--- | :--- |
| Agent harness | 메커니즘이 **단일 run** 안에 국한 |
| Factory harness | 런을 조율하거나, 런→이후 런으로 상태를 넘기거나, **런 결과로 갱신** |
| Domain | 애플리케이션 도메인과 함께 바뀌어야 함 |
| Residual | 인프라 / 모델 원인 두 잔여 테스트 |

## 실패 코딩 (3필드 분리)

결함 **기원** · 막지 못한 **제어** · **수정 위치**를 분리 기록. 환경 탓은 **긍정 증거** 있을 때만. 단일 운영자 파이프라인(6 프로젝트) 문서화 실패 + 공개 시스템 3개의 26 컴포넌트로 기준을 만든 뒤 동결, 동일 계열 모델 코더 2명이 held-out 46유닛에서 메커니즘 층 26/26 일치·incident 필드 κ≈0.86–0.93. 단, undetermined/미기록이 많고 절반이 ambiguous — 합의≠정확도; 인간 코더 미검증. 예비 가설 7개.

공장 스케줄·티켓 핸드오프·gateway tick은 factory harness 축 — [[wiki/Engineering/AI-Native-Engineering/Agentic-Software-Factory.md]], [[wiki/Agents/Self-Evolving/Harness-RSI-Self-Evolving-Agent-Harness.md]].

## 관련

- [[wiki/Agents/Self-Evolving/Harness-RSI-Self-Evolving-Agent-Harness.md]]
- [[wiki/Engineering/AI-Native-Engineering/Agentic-Software-Factory.md]]
- [[wiki/Agents/Self-Evolving/SkillOpt-및-과학적-탐구-멀티-에이전트-시스템.md]]
