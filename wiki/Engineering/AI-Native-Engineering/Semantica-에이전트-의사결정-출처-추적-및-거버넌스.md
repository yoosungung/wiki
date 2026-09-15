---
title: "Semantica를 통한 에이전트 의사결정 출처 추적(Decision Provenance) 및 거버넌스"
related_raw: ["[[raw/An agent approved a loan in January..md]]"]
tags: ["AI-Governance", "Decision-Provenance", "Semantica", "Agent-Security"]
type: "wiki"
status: "published"
last_updated: "2026-08-24"
updated: "2026-08-24"
---

# 🛡️ Semantica를 통한 에이전트 의사결정 출처 추적(Decision Provenance) 및 거버넌스

에이전트의 자율적 활동 영역이 넓어짐에 따라, 과거의 의사결정 경로를 역추적하고 감사(Audit)할 수 있는 기술적 거버넌스 모델의 중요성이 커지고 있습니다.

## 1. 문제의 발단: 결과와 이유의 단절
- **시나리오**: AI 에이전트가 1월에 대출(Loan)을 승인했습니다. 8월에 감사를 진행하면서 "왜 승인했는가?"라는 질문을 던졌지만, 기존의 단순 로그(Audit Log)에는 최종 결과(Outcome)만 기록되어 있을 뿐, 승인에 도달하게 된 의사결정 논리(Reasoning State)는 유실되어 있습니다.
- **표준 실패 모드**: 최종 결과만 저장하고 의사결정 상태를 누락하는 로그 설계는 사후 감사 시점에 답변할 수 없는 구조적 한계를 낳습니다. 

## 2. Semantica 아키텍처 및 특징
**Semantica**(1.9k stars, MIT 라이선스)는 이러한 한계를 극복하기 위해 에이전트의 모든 의사결정을 출처(Provenance) 및 관련 엔티티와 유기적으로 매핑합니다.
- **의사결정의 그래프 구조화**: 각 결정을 추론 근거(Rationale)와 함께 그래프 노드로 기록하고, 결정을 유발한 선행 결정이나 참조한 데이터 엔티티들과 체인 형태로 링크합니다.
- **위변조 방지(Tamper-evident)**: 메인 체인(Main)의 모든 엔트리들이 상호 연결되므로, 중간에 행이 삭제되거나 위변조될 경우 즉각 감지할 수 있습니다.
- **시점 복구(Point-in-time reconstruction)**: 의사결정 당시에 활성화되어 있던 스코프 내의 사실(Facts), 적용된 정책/규칙 버전, 도구 실행 이력을 복원할 수 있습니다.

## 3. 실무 구현 시의 핵심 쟁점 및 보완점
- **사후 합리화 방지**: 그래프 내 기록된 근거가 실제 추론 시점에 수집된 Contemporaneous Evidence(실시간 근거)인지, 아니면 모델이 최종 결과를 도출한 뒤 사후에 그럴싸하게 재구성한 추론 과정(Post-facto Rationale)인지를 구분해야 합니다.
- **메모리 오염에 대한 강건성**: 에이전트의 컨텍스트나 장기 메모리(예: Mem0)가 오염되거나 조작된 경우, 에이전트가 완벽히 논리적인 근거를 대더라도 실제로는 잘못된 행동을 취하게 됩니다. 따라서 Semantica 노드는 입력 소스의 최종 출처(Retrieved chunks 등)까지 함께 핀 고정하여 추적해야 합니다.
- **SHACL 제약 조건 관리**: 데이터 수집(Ingestion) 과정에서 새로운 정보가 유입되어 이전 결정이 의존하던 기존 엔티티와 모순이 생길 때, SHACL(SHAPE Constraint Language) 위반 사항을 어떻게 시스템적으로 표출하고 기존 결정의 효력을 격리할 것인지 고려해야 합니다.

---
**관련 문서**:
- [[wiki/Engineering/AI-Native-Engineering/000_AI-Native-Engineering-MOC.md]]
- [[wiki/Engineering/Data-and-Security/SkillSpector-에이전트-스킬-보안-취약점-스캐너.md]]
