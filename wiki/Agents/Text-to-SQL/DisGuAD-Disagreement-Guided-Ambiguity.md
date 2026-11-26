---
id: disgad-disagreement-guided-ambiguity
title: "DisGuAD: SQL 불일치 유도 모호성 탐지 (Interactive Text-to-SQL)"
status: canonical
owner: km
updated: "2026-11-27"
last_updated: "2026-11-27"
review_after: "2027-02-27"
sources:
  - https://arxiv.org/abs/2611.21645
tags: ["Agents", "Text-to-SQL", "NL2SQL", "Clarification", "BIRD-Interact", "Ambiguity"]
type: "wiki"
---

# DisGuAD: SQL 불일치 유도 모호성 탐지 (Interactive Text-to-SQL)

**DisGuAD**([arXiv:2611.21645](https://arxiv.org/abs/2611.21645), 2026-11)는 interactive Text-to-SQL에서 **어떤 모호성을 물어볼지**를 고르는 플러그인 정책이다. 다운스트림 SQL generator는 그대로 두고, **대립 SQL 해석 간 컴포넌트 불일치**를 모호성 센서로 쓴다.

## 핵심 메커니즘

1. **Query-term inventory**: 질문 스팬 + 조 유형(어휘·스키마 링크·의도 등) 후보 앵커 추출.
2. **Contrastive probes**: 서브골·관계 경로·암시 정의·개별 축을 바꾸는 네 계열 프로브로 대립 SQL을 유도.
3. **Component disagreement**: 캐논 SQL 비교 → projection/predicate/join/agg/ranking 등 반복 차이가 있는 축만 사용자 질문 대상으로 귀속.
4. **Dialogue state**: 이미 물은 타깃은 제외하고 우선순위 1건만 템플릿 질문으로 발행.

## 시사점

- 표면 모호성만 묻는 정책은 critical-ambiguity coverage ≈46–49%; DisGuAD는 **82–85%**로 올림 (BIRD-Interact Lite/Full, 2 LLM).
- normalized Reward **+4.40–8.97**; 같은 대화 신호를 다른 static generator에 이식하면 최대 **+13.97** (generator 고정).
- AskWise(실행·수리 증명)와 축이 다름: DisGuAD는 **생성기 앞단 명확화 선택**, AskWise는 **해석×수리 월드에서 실행 증명**. 공장 HITL/SQL-MCP에는 “SQL을 바꾸는 불일치만 질문” 규칙을 재사용.
- 코드/아티팩트: 논문 페이지 참고 ([arXiv:2611.21645](https://arxiv.org/abs/2611.21645)).

## 🔗 관련 문서

- [[wiki/Agents/Text-to-SQL/000_Text-to-SQL-MOC.md]]
- [[wiki/Agents/Text-to-SQL/AskWise-Execution-Guided-Clarification.md]]
- [[wiki/Agents/Text-to-SQL/AV-SQL-Agentic-Views-Spider-2-0.md]]
- [[wiki/Agents/Text-to-SQL/LuthorSQL-System1-Local-Gate.md]]
