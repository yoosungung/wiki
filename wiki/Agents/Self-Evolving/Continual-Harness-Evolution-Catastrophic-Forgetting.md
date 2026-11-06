---
id: wiki-continual-harness-evolution-catastrophic-forgetting
title: "Continual harness evolution: 태스크 전이 시 catastrophic forgetting"
status: canonical
owner: km
updated: "2026-11-07"
last_updated: "2026-11-07"
review_after: "2026-12-07"
tags: ["Agents", "Self-Evolving", "Continual-Learning", "Harness", "Forgetting", "SWE"]
sources:
  - https://arxiv.org/abs/2611.03219
  - https://github.com/THU-Agent/continual-harness-evolution
type: wiki
---

# Continual harness evolution: 태스크 전이 시 catastrophic forgetting

단일 태스크에서 하네스 자가진화(AHE, Meta-Harness 등)는 성능을 올리지만, 코딩 에이전트는 수리→테스트→기능추가처럼 **태스크 종류를 잇달아** 만난다. arXiv:2611.03219는 SWE-Bench / SWT-Bench / FeatureBench를 여섯 진화 방향으로 묶어 **continual harness self-evolution**을 측정한다.

## 핵심 관측

- 후속 데이터셋 진화가 **이전 태스크 성능을 크게 깎는다**.
- 예: DeepSeek-V4-Flash-0731 + Meta-Harness — SWE-Bench **94.0%** 후 FeatureBench 진화 5라운드에 **32.0%**(상대 −66%).
- SWT-Bench **100%** 후 FeatureBench 진화 → SWT **62%**.
- 동일 모델에서도 하네스만 바꿔 SWE-Bench **82~96%** 격차 — 망각도 하네스 축이다.

## 충돌 유형 (≥520 궤적 수작업)

| 유형 | 요지 |
| :--- | :--- |
| Verification | 검증/테스트 게이트가 태스크별로 상충 |
| Workflow | 단계·도구 순서 정책이 덮어씌워짐 |
| Budget | 스텝·토큰·재시도 예산이 새 태스크에 맞춰 이전을 해침 |

ablation상 유형별 영향 크기가 다르다. 단일 태스크 최고점만 보고 연속 배포하면 Meta²/Harness²/EvoGroup류 채택 하네스도 **이전 레인 회귀**를 감수한다.

## 운영 함의

- 공장 스케줄·persona 하네스를 태스크 레인별로 진화시킬 때 **소스 레인 회귀 게이트**를 둔다.
- within-run 폐기([[wiki/Agents/Self-Evolving/Meta2-Precomputed-Harness-Evolution.md|Meta²]])는 전역 망각을 줄이는 한 축; 그룹 지속 진화([[wiki/Agents/Self-Evolving/EvoGroup-Self-Evolving-Group-Agent-Harness.md|EvoGroup]])는 동결·전이 평가가 필요하다.
- 코드: `THU-Agent/continual-harness-evolution`.
