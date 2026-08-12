---
id: epistemic-debt-changescore-friction-gate
title: "Epistemic Debt ChangeScore·Friction Gate"
status: canonical
owner: km
updated: "2026-08-12"
last_updated: "2026-08-12"
review_after: "2026-11-12"
sources:
  - ticket:458
  - ticket:544
  - https://doi.org/10.48550/arxiv.2602.20206
  - https://www.oliver-huang.com/static/uploads/papers/productive_friction.pdf
tags: ["Engineering", "AI-Native", "Coding", "Epistemic-Debt", "Friction"]
type: "wiki"
---

# Epistemic Debt ChangeScore·Friction Gate

IDE/에이전트 확장에서 **변경 비용(ChangeScore)** 으로 개입 강도(friction tier)를 고르고, Host Gate로 커밋 전 teach-back/확인을 건다. 가중치 확정 전에도 **수식·바이패스 규칙·스모크**를 먼저 고정한다.

## ChangeScore (실험 기본값)

```text
severity = mean(entropy, coupling, criticality)
sessionLoad ≥ 0.7 → score − SESSION_LOAD_PENALTY_HIGH (실험 0.25)
sessionLoad ≥ 0.4 → score − SESSION_LOAD_PENALTY_MID  (실험 0.15; 구 0.10은 mid-band에서 full 잔류)
tier: none < 0.3 / light < 0.6 / else full
```

`bypassAllowed` = `criticality < 0.7` **또는** `sessionLoad ≥ 0.5`.

**계약 충돌 주의**: 문헌/구 wiki의 `attempt===3 바이패스 금지`는 ARCHITECTURE가 attempt를 쓰지 않으면 L0을 따른다. 가중치 freeze 전 ROADMAP에 “실험 기본값”만 두고 프로덕션 임계값은 매트릭스 증거 후 확정.

mid-band 검증 예: mean≈0.72 @ sessionLoad 0.45 → mid penalty 0.15면 full→light (0.10이면 full 잔류). full-tier fixture는 mid-band 미만 sessionLoad로 회귀 고정.

문헌 축: Explanation Gate / adaptive friction([arxiv 2602.20206](https://doi.org/10.48550/arxiv.2602.20206)), productive friction 설계 공간(Huang et al.).

## Host Gate 배치

- 기본 훅 = 확장 커맨드(예: `triggerGate`). SCM vs husky는 후순위 결정.
- core는 vscode-free로 점수·tier만 계산하고, host 어댑터가 커맨드/UI를 붙인다 — [[wiki/Agents/Coding-and-Engineering/VSCode-Extension-Pure-Core-Host-Split.md]].
- Mirror/LLM 런타임이 미정이면 HeuristicMirrorAdapter로 인터페이스만 고정.

## 스모크

```bash
# 개념: Electron 없이 none/light/full + sessionLoad downshift
runGateSmoke
```

가중치 freeze 전에는 ROADMAP에 “실험 기본값”으로 명시하고, 프로덕션 임계값은 실험 후 확정한다.

## 🔗 관련 문서

- [[wiki/Agents/Coding-and-Engineering/VSCode-Extension-Pure-Core-Host-Split.md]]
- [[wiki/Engineering/AI-Native-Engineering/Agentic-Software-Factory.md]]
- [[wiki/Engineering/AI-Native-Engineering/Wiki-Synthesis-Policy.md]]
