---
id: l0-goals-in-architecture
title: "L0 Goal/Non-goals는 ARCHITECTURE에 둔다"
status: canonical
owner: km
updated: "2026-08-20"
last_updated: "2026-08-20"
review_after: "2026-11-20"
sources:
  - ticket:1053
tags: ["Engineering", "AI-Native", "Architecture", "L0", "Goals"]
type: "wiki"
---

# L0 Goal/Non-goals는 ARCHITECTURE에 둔다

제품 Goal/Non-goals는 테넌트 `ARCHITECTURE.md`의 Intent/Goal 절(§1 직전)에 둔다. 별도 `PROJECT_GOALS.md`를 만들지 않는다. 티켓 intake는 그 L0에서 `Derived from`으로 끌어온다.

## 배치

| 위치 | 내용 |
| :--- | :--- |
| `ARCHITECTURE.md` Goal 절 | Goal(최종)·Goal(1차)·Non-goals |
| `ROADMAP` | Goal **한 줄** + L0 링크만 (장문 중복 금지) |
| 티켓 intake | L0에서 `Derived from` |
| DESIGN §「본 문서가 다루지 않는 것」 | **컴포넌트** 위임 — 제품 Non-goals와 혼동 금지 |

## Goal vs Means

- Goal(최종)=판매·도입 가능한 제품 결과(예: NL→SELECT 제품).
- Goal(1차)=측정 가능한 공개 점수·마일스톤(예: 벤치 exec_result).
- Means(MCP/agent/버그픽스/인프라)는 Goal이 아니다.

`repos[].roadmap.enabled` 같은 자동화 플래그는 인간 지시 전 켜지 않는다.

## 🔗 관련 문서

- [[wiki/Engineering/AI-Native-Engineering/Agentic-Software-Factory.md]]
- [[wiki/Engineering/AI-Native-Engineering/Roadmap-Pass-Gate-Human-Approval.md]]
- [[wiki/Engineering/AI-Native-Engineering/Wiki-Synthesis-Policy.md]]
