---
title: "STRATUS"
related_raw: ["[[wiki/Engineering/Infrastructure-and-DevOps/STRATUS.md]]"]
tags: ['wiki', 'agents_and_systems', 'aiops_&_ai-native_devtools']
type: "wiki"
status: "published"
last_updated: "2026-04-19"
updated: "2026-04-19"
---

# STRATUS: 자율 SRE를 위한 다중 에이전트 시스템

**출처**: [원본 링크](https://openreview.net/pdf?id=fYW1PKawwJ)

이 문서는 현대 클라우드 시스템의 자율적인 사이트 신뢰성 엔지니어링(SRE)을 위한 LLM 기반 다중 에이전트 시스템인 STRATUS를 소개합니다.

## 주요 내용

1.  **자율 SRE의 필요성:** 클라우드 시스템의 규모, 복잡성, 동적 특성으로 인해 장애 감지, 위치 파악, 완화가 어렵습니다. 인간 중심의 SRE 방식은 이러한 문제를 해결하는 데 한계가 있습니다. STRATUS는 이러한 문제를 해결하기 위해 인간의 개입 없이 라이브 프로덕션 시스템을 관리하고 장애를 완화하는 것을 목표로 합니다.

2.  **STRATUS 아키텍처:**
    *   **다중 에이전트 시스템:** STRATUS는 감지(Detection), 진단(Diagnosis), 완화(Mitigation), 실행 취소(Undo) 에이전트와 같은 전문 에이전트들을 조율합니다.
    *   **제어 흐름:** 에이전트들은 상태 머신 기반의 결정론적 제어 흐름 로직을 통해 조율됩니다.
    *   **LLM 활용:** LLM은 에이전트들이 지능적이고 창의적으로 작동하도록 데이터 흐름에서 활용됩니다.

3.  **트랜잭션 무회귀(Transactional No-Regression, TNR) 안전성 사양:**
    *   **핵심 과제:** SRE 에이전트의 주요 과제는 안전성입니다. STRATUS는 장애를 완화할 때 대상 시스템의 상태를 악화시키지 않아야 합니다.
    *   **TNR 정의:** TNR은 에이전트의 완화 조치가 실패할 경우 항상 "실행 취소"될 수 있도록 보장하고, 시스템의 상태가 지속적으로 개선되도록 보장합니다.

4.  **구현 세부 사항:**
    *   **TNR 구현:** 샌드박스 기반 격리, 상태 머신을 통한 작성자 에이전트의 상호 배제, 스택 기반 롤백 메커니즘을 통해 TNR을 구현합니다.
    *   **에이전트 도구:** 에이전트가 자연어를 사용하여 환경과 상호 작용할 수 있도록 관찰 가능성 도구(observability tools)와 명령줄 도구(NL2Kubectl)를 개발했습니다.

5.  **평가:**
    *   STRATUS는 AIOpsLab 및 ITBench 벤치마크에서 다른 SRE 에이전트보다 훨씬 뛰어난 완화 성능을 보였습니다.
    *   TNR 기반의 실행 취소 및 재시도 기능이 복잡한 완화 문제 해결에 결정적인 역할을 했습니다.

---
## 관련 노트
- [[wiki/Agents/Multi-Agent-and-Orchestration/멀티-에이전트-패턴]]
- [[wiki/Agents/Frameworks/Microsoft-Frameworks/Microsoft Agent Framework]]
- [[wiki/Engineering/Infrastructure-and-DevOps/airflow]]
