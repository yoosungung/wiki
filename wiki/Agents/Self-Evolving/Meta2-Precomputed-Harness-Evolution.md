---
title: "Meta²: 재사용 진화 지식을 미리 계산하고 런 안에서만 하네스를 고치는 패턴"
id: wiki-meta2-precomputed-harness-evolution
status: canonical
owner: km
date: "2026-11-06"
last_updated: "2026-11-06"
updated: "2026-11-06"
review_after: "2026-12-06"
tags: ["Agents", "Self-Evolving", "Meta2", "Harness-Evolution", "Within-Run"]
sources:
  - https://arxiv.org/abs/2611.05139
type: wiki
---

# Meta²: 재사용 진화 지식을 미리 계산하고 런 안에서만 하네스를 고치는 패턴

장기 태스크 에이전트는 가중치만이 아니라 **하네스**(프롬프트, 컨텍스트 정책, 도구, 스킬, 메모리, 훅)로 행동한다. Meta²(arXiv:2611.05139)는 오프라인에서 **공유 하네스를 최적화하지 않고**, 언제 개입할지에 대한 텍스트 **Meta-Skill**만 배운 뒤 배포 시 그 지식을 얼린다. 각 런은 같은 시드 하네스 `h0`에서 시작하고, 체크포인트 편집은 **그 런의 나머지에만** 적용된 뒤 버려진다.

[[wiki/Agents/Self-Evolving/Harness-Squared-Recursive-Agent-Harnessing.md]]의 하네싱 수준 재귀가 채택 하네스를 태스크 간에 남기는 것과 달리, Meta²는 **지식은 전역·편집은 로컬**이다.

## 1. 편집 시점 분류

| 체제 | 편집을 고르는 때 | 영향 범위 | 검증기 |
| :--- | :--- | :--- | :--- |
| Offline | 타깃 태스크를 보기 전 | 모든 타깃이 공유하는 `h*` | 학습 궤적의 결과 |
| Pre-run | 실행 전, 지시문만 본 뒤 | 곧 시작할 한 런 | 없음 |
| Within-run | 실행 중 체크포인트 | 같은 런의 남은 구간 | 그 런의 최종 결과는 못 봄 |
| After-run | 시도가 끝난 뒤 | 다음 시도·다음 태스크 | 완료된 결과 |

Within-run만 증거가 나온 **미완료 런**을 고칠 수 있다. Meta²는 오프라인 검증 경험을 within-run 판단에 연결한다.

## 2. 온라인 루프

같은 고정 모델로 **태스크 에이전트**와 **이볼버**를 나눈다. 환경은 리셋하지 않고, 부분 궤적을 유지한 채 하네스만 바꾼다.

체크포인트 `k`의 최상위 결정은 `KEEP` 또는 `EVOLVE(δ)`이다.

- `KEEP`: `h(k) = h(k-1)`, 실행 계속.
- `EVOLVE`: `δ`를 **notice, instruction update, hook, tool** 중 하나의 채널로만 적용.
- 종료 체크포인트(완료 주장)에서는 워크스페이스 상태를 보고, `KEEP`이면 산출물을 받아들이고 `EVOLVE`면 보정 후 같은 에이전트를 다시 보낸다.

증거 `I(k)`는 지시문, 구간 궤적, 읽기 전용 워크스페이스, 직전 편집의 로드/유지/롤백 상태를 시간순으로 붙인다.

## 3. 오프라인 Meta-Skill (A/B/C)

학습 태스크마다 같은 시드 하네스로 세 조건을 돌린다.

| 조건 | 이볼버 | 쓰는 이유 |
| :--- | :--- | :--- |
| A | 없음 | 베이스라인 |
| B | 현재 Meta-Skill | 지금 지식이 돕는 곳·해치는 곳 |
| C | 학습 때만 검증기 특권 | A·B가 같이 실패할 때 복구 예시. 특권을 태스크 에이전트에 넘기면 제외 |

대비에서 방향을 만든다. B성공/A실패·C성공/B실패는 **act**, B실패/A성공·C실패/B성공은 **avoid**, A·B 모두 성공은 **hold**. 배치마다 `REFLECT → AGGREGATE(태스크 고유 표현 제거) → UPDATE`. 배포 후 Meta-Skill은 홀드아웃 검증기나 온라인 편집으로 갱신하지 않는다.

## 4. 측정 (논문 보고치)

GPT-5.6-Terra, NexAU 시드 대비. Terminal-Bench 2.1은 mean@5, DeepSWE 1.1은 mean@3.

| 설정 | Terminal-Bench 2.1 | DeepSWE 1.1 |
| :--- | :--- | :--- |
| NexAU 시드 | 66.33% | 34.67% |
| Meta-Harness (최강 하네스 진화 베이스) | 73.33% (+7.00) | 37.33% (+2.66) |
| Meta² | **81.00% (+14.67)** | **44.44% (+9.77)** |
| 전체 비용 (USD, 오프라인+온라인) | 174.91 | 367.86 |

DeepSeek-V4-Flash-0731 Terminal-Bench: 시드 70.00% → Meta² **77.67%**. 백본마다 Meta-Skill을 **따로** 만들므로 모델 간 제로샷 전이는 아니다.

체크포인트 간격 `L=5`가 Terminal-Bench 81.00%·온라인 비용 USD 64.72로 가장 낫다. `L=1`은 79.00%에 비용만 오른다. 대조 학습 Meta-Skill이 자가 증류보다 Terminal-Bench +4.00, DeepSWE +8.88 포인트. **런 사이 편집을 유지**하면 81.00%→78.33%, 44.44%→39.11%로 떨어진다. 태스크 전용 편집은 다음 런으로 넘기지 않는다.

## 5. 구현 스케치

```text
offline:
  for batch in train:
    rollouts = {A: no_evolver, B: evolver(M), C: evolver(M, verifier)}
    M = update(M, aggregate(reflect(contrasts(A,B,C))))
  freeze(M)

online(task):
  h = h0
  for checkpoint in schedule(L=5):
    decision = evolver(h, evidence, M)   # no held-out verifier
    if decision is EVOLVE: h = apply(h, delta)  # notice|instruction|hook|tool
    agent.continue(same_env, same_trajectory, h)
  discard(h)   # next task starts at h0 again; M stays frozen
```

## 6. 관련 문서

- [[wiki/Agents/Self-Evolving/Harness-Squared-Recursive-Agent-Harnessing.md]]
- [[wiki/Agents/Self-Evolving/Harness-S-Sibling-Rescue-Training.md]]
- [[wiki/Agents/Self-Evolving/WikiSkill-절차적-지식-자가-진화-프레임워크.md]]
- [[wiki/Engineering/Infrastructure-and-DevOps/Meta-Agent-Harness-Policy-Learning.md]]
- 논문: [arXiv:2611.05139](https://arxiv.org/abs/2611.05139)
