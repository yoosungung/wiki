---
id: wiki-reglos-self-evolving-personal-memory-agent
title: "Reglos: 개인 메모리 내루프 + 하네스 RSI 외루프"
status: canonical
owner: km
updated: "2026-11-07"
last_updated: "2026-11-07"
review_after: "2026-12-07"
tags: ["Agents", "Memory", "Self-Evolving", "Reglos", "RSI", "Harness"]
sources:
  - https://arxiv.org/abs/2611.06049
  - https://reglos.ai
type: wiki
---

# Reglos: 개인 메모리 내루프 + 하네스 RSI 외루프

개인 에이전트는 대화로 메모리를 쌓고, 코딩 에이전트가 그 메모리를 모델 컨텍스트로 바꾸는 **하네스**까지 패치한다. 실패 사례에만 맞춘 패치는 벤치 게이밍·과적합 위험이 있다. Reglos(arXiv:2611.06049)는 **학습 없는(training-free)** 이중 루프로 이를 분리한다.

- **내루프(유저별 메모리):** append-only 기록. 선호 변경은 구사실을 닫고 유지, forget 요청은 만료+규칙으로 남김. 야간 Dream이 현재 사실로 프로필을 재작성.
- **외루프(공유 하네스 RSI):** 코딩 에이전트가 실패 트레이스에서 패치 제안 → **다른 모델 패밀리 크리틱**이 벤치 게이밍 스크리닝 → 하네스 동결 후 **고정 평가기**가 held-out 유저에서만 추가 패치 수락.

같은 백본으로 Mem0·MemOS·EverOS를 상회: Qwen3.8-27B 기준 PersonaMem-v2 **61.3%**, LongMemEval-S **84.0%**; GPT-5.6 Luna 답변 시 **57.5%** / **87.2%**. 외루프 수용 패치는 validation을 54.2%→60.7%로 올림. 진단: 추적 실패의 **31%**는 증거가 이미 컨텍스트에 있는데도 하네스가 잘못 씀.

## Meta²·Harness²와 대비

| 체제 | 무엇을 남기는가 | 검증 |
| :--- | :--- | :--- |
| [[wiki/Agents/Self-Evolving/Meta2-Precomputed-Harness-Evolution.md\|Meta²]] | Meta-Skill 전역, 편집은 런 로컬·폐기 | within-run KEEP/EVOLVE |
| Reglos | 유저 메모리 online + 하네스 패치 offline(동결 후 held-out) | 이종 크리틱 + 고정 평가기 |
| [[wiki/Agents/Self-Evolving/Harness-Squared-Recursive-Agent-Harnessing.md\|Harness²]] | 채택 하네스가 태스크 간에 지속 | Propose→Probe→Compose |

## 함정

- 벤치 점수만으로 하네스 패치를 받지 않는다 — held-out 유저·이종 크리틱이 없으면 과적합.
- 시크릿은 추출 전 마스킹. wiki/티켓에 PAT·키를 기록하지 않는다.
- 원시 이력 리랭킹 베이스라인과 함께 볼 때: [[wiki/Agents/Memory-and-Cognition/RAW-RAG-Raw-History-Retrieval-Baseline.md]].
