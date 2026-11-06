---
id: wiki-evogroup-self-evolving-group-agent-harness
title: "EvoGroup: 공유 컨텍스트 Group Agent용 자가진화 하네스"
status: canonical
owner: km
updated: "2026-11-07"
last_updated: "2026-11-07"
review_after: "2026-12-07"
tags: ["Agents", "Self-Evolving", "EvoGroup", "Group-Agent", "Harness", "Shared-Context"]
sources:
  - https://arxiv.org/abs/2611.03868
  - https://github.com/BigggFatttRabittt/EvoGroup
type: wiki
---

# EvoGroup: 공유 컨텍스트 Group Agent용 자가진화 하네스

Claude Tag류 **Group Agent**는 다인 상호작용으로 누적되는 공유 컨텍스트(관계·공동 결정·스레드)를 다룬다. 기존 메모리는 개인 축·고정 스키마라 그룹 역학에 약하다. EvoGroup/EvoG(arXiv:2611.03868)는 **6도구 cold start** 하네스에서 시작해 상호작용으로 진화한다.

## 루프 (4단)

1. **Interaction** — `H_t`로 질의 답변 + confidence `c∈[0,1]`. `c≤γ`(예: 0.5)면 정답 공개 전 **불확실성 자가반성**.
2. **Trajectory Selection** — confidence×정답으로 CW/UC/UW를 우선(CC는 진단 비우선).
3. **Analysis** — Adaptive Progressive Disclosure(필요 시만 상세) + 시맨틱 버킷 집계로 고수준 발견.
4. **Revision** — evolve agent가 하네스를 `H_{t+1}`로 개정(네 인터페이스).

초기 도구: `list_files`, `read_file`, `grep_search`, `write_file`, `query_records`, `create_file`.

## 결과

- EverMemBench held-out pass@1: **71.07% → 89.58%** (DeepSeek-V4-Flash), Claude Code 85.83%·Codex 82.62% 상회.
- 동결 하네스를 unseen **GroupMemBench**에 이식해도 메모리 베이스라인·인간 설계 하네스 상회(GPT-5.5).
- 추가 백본에서 pass@1 **+15.36~16.19 pp**.

개인 메모리 RSI([[wiki/Agents/Memory-and-Cognition/Reglos-Self-Evolving-Personal-Memory-Agent.md|Reglos]])와 달리 **공유 컨텍스트·그룹 지식**이 진화 대상이다. within-run 폐기([[wiki/Agents/Self-Evolving/Meta2-Precomputed-Harness-Evolution.md|Meta²]])와 달리 채택 하네스는 반복 간 지속한다.

## 함정

- CC(자신만만·정답)만으로 진화하면 신호가 빈약하다 — CW/UC/UW를 고른다.
- 자가반성은 **라벨 공개 전**에 남겨야 진단 가치가 있다.
- 연속 태스크 전이 시 망각: [[wiki/Agents/Self-Evolving/Continual-Harness-Evolution-Catastrophic-Forgetting.md]].
