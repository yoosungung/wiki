---
id: wiki-self-evolving-agents-incomplete-continual-learners
title: "Self-evolving agents는 불완전한 continual learner"
status: canonical
owner: km
updated: "2026-11-08"
last_updated: "2026-11-08"
review_after: "2026-12-08"
tags: ["Agents", "Self-Evolving", "Continual-Learning", "Harness", "Drift"]
sources:
  - https://arxiv.org/abs/2610.25858
  - https://ar5iv.labs.arxiv.org/html/2610.25858
type: wiki
---

# Self-evolving agents는 불완전한 continual learner

arXiv:2610.25858. 가중치는 동결하고 하네스(프롬프트·메모리·스킬)만 고치는 nonparametric self-evolution이 **드리프트 스트림**에서 유효한 continual learner인지 측정한다.

## 설정

- 스트림: BIRD / BFCL / ScienceWorld 기반 **topic · workflow · domain · compound** drift (블록당 50 train / 50 eval).
- 방법: ReasoningBank(검색 메모리) · GEPA(공유 strategy 프롬프트) · Meta-Harness(프롬프트+메모리+스킬+컨트롤러).
- 분해: within-block **plasticity $P$** vs cross-block **stability $S$** (pre-block interference + post-block forgetting).

## 핵심 발견

1. **가소성↑ ↔ 안정성↓** — 편집 표면이 커질수록(메모리 → 프롬프트 → 풀 워크스페이스) 활성 블록 이득은 커지나 타 블록 손실도 커짐.
2. **Self-mod 간섭** — GEPA/Meta-Harness는 공유 표면을 전 태스크에 주입 → 미학습 그룹 사전 간섭 + 이후 블록이 이전 규칙을 압축·덮어씀.
3. **검색도 불완전** — ReasoningBank는 원거리 도메인 망각은 줄이지만, 미학습 그룹에 외래 메모리 주입·유사 쿼리의 **workflow collision**(BFCL-Miss↔Base)을 막지 못함.

Gemini 3.6 Flash 요약: 4스트림 평균 terminal advantage GEPA +3.7 / ReasoningBank +2.5 / Meta-Harness +1.4 — 그러나 시나리오마다 최고 가소성 방법은 항상 최저 안정성 쪽.

## 공장 함의

- persona/스케줄 하네스를 **전역 rewrite**하면 다른 레인 회귀가 난다 — Continual harness forgetting([[wiki/Agents/Self-Evolving/Continual-Harness-Evolution-Catastrophic-Forgetting.md|SWE 연속 진화]])과 동일 축.
- 완화 후보: Meta² within-run 폐기([[wiki/Agents/Self-Evolving/Meta2-Precomputed-Harness-Evolution.md|Meta²]]), ReHarness 후방 개정([[wiki/Agents/Self-Evolving/ReHarness-Recurrent-Harness-Agentic-Continual-Learning.md|ReHarness]]), 레인별 하네스 격리 + 회귀 게이트.
