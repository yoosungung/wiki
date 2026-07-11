---
title: "STRATUS-Deep-Dive-2026"
related_raw: ["[[wiki/Engineering/Infrastructure-and-DevOps/STRATUS-Deep-Dive-2026.md]]"]
tags: ['wiki', 'agents_and_systems', 'aiops_&_ai-native_devtools']
type: "wiki"
status: "published"
last_updated: "2026-04-19"
updated: "2026-04-19"
---

# 🤖 STRATUS: AIOps를 위한 자율적 SRE 멀티 에이전트 시스템

STRATUS는 복잡한 클라우드 환경에서 장애 탐지, 분석, 복구를 자동화하기 위해 설계된 최신 LLM 기반 멀티 에이전트 시스템입니다.

## 1. 시스템 개요
STRATUS는 인간 SRE(Site Reliability Engineer)의 워크플로우를 모방하여, 장애가 발생했을 때 자율적으로 대응하는 시스템입니다. 단순한 경고(Alert) 요약을 넘어 실제 인프라에 명령을 내리고 장애를 해결하는 데 초점을 맞춥니다.

## 2. 핵심 아키텍처
- **멀티 에이전트 협업**: 진단 에이전트, 분석 에이전트, 복구 에이전트 등이 역할을 나누어 수행합니다.
- **상태 머신(State Machine) 제어**: LLM의 비결정론적 특성을 보완하기 위해, 엄격한 상태 머신 기반의 제어 루프를 사용하여 안정적인 워크플로우를 보장합니다.
- **Transactional No-Regression (TNR)**: 장애 복구 시도 중 시스템 상태가 이전보다 나빠지지 않도록 보장하는 안전 장치입니다.

## 3. 주요 성과
- **장애 복구 성공률**: AIOpsLab 및 ITBench 벤치마크에서 기존 SOTA(State-of-the-Art) 에이전트 대비 약 1.5배 높은 복구 성공률을 기록했습니다.
- **완전 자율화**: 데이터 분석에 그치지 않고 실제 운영 환경을 직접 통제하여 장애를 해결하는 수준에 도달했습니다.

---
## 🔗 관련 링크 및 참고 자료
- 원문: [STRATUS: Autonomous SRE via Multi-Agent Systems](https://github.io/stratus-sre/)
- 관련 노트: [[wiki/Engineering/Infrastructure-and-DevOps/000_AIOps-MOC]], [[wiki/Engineering/Infrastructure-and-DevOps/STRATUS-Autonomous-Reliability]]
