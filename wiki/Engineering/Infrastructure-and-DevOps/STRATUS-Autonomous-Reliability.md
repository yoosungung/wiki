---
title: "STRATUS-Autonomous-Reliability"
related_raw: ["[[wiki/Engineering/Infrastructure-and-DevOps/STRATUS-Autonomous-Reliability.md]]"]
tags: ['wiki', 'agents_and_systems', 'aiops_&_ai-native_devtools']
type: "wiki"
status: "published"
last_updated: "2026-04-19"
---

# ☁️ STRATUS: 자율적 클라우드 신뢰성 엔지니어링 (Autonomous AIOps)

## 1. 개요
**STRATUS**는 NeurIPS 2025에 채택된 연구로, 단순한 장애 진단을 넘어 클라우드 인프라의 장애를 자율적으로 복구(Mitigation)하는 멀티 에이전트 시스템입니다. 이는 전통적인 AIOps가 RCA(Root Cause Analysis)에 집중하던 단계를 넘어, 실제 복구 액션을 안전하게 수행하는 자율 운영 단계로의 진입을 상징합니다.

## 2. 주요 기술적 특징
- **Multi-Agent Orchestration**: 여러 전문 에이전트들이 협력하여 장애 상황을 인지하고, 원인을 분석하며, 최적의 복구 시나리오를 설계합니다.
- **TNR (Transactional No-Regression) 규격**: 복구 자동화 시 발생할 수 있는 의도치 않은 성능 저하나 부작용을 방지하기 위한 트랜잭션 기반의 안전 규격입니다.
- **RCA to Mitigation**: 과거에는 관리자에게 "원인이 무엇이다"라고 알려주는 데 그쳤다면, STRATUS는 "이런 복구 작업을 수행하겠다"고 제안하거나 권한 내에서 직접 수행합니다.
- **Cloud Reliability Engineering**: 대규모 분산 시스템 환경에서의 자가 치유(Self-healing) 인프라 구축을 목표로 합니다.

## 3. 기술적 시사점
- **무인 운영(Zero-touch Operations)**: 장애 발생 시 인간의 개입 시간을 최소화하여 가동 중지 시간을 획기적으로 단축합니다.
- **안전성 확보**: AI의 복구 액션이 인프라에 미칠 영향을 미리 시뮬레이션하고 TNR 규격을 통해 검증함으로써 신뢰성을 확보했습니다.

## 4. 관련 이미지 및 시각 자료
- **이미지 1**: [STRATUS 에이전트 협업 구조](https://arxiv.org/html/2411.04586/images/architecture.png) (논문 기반) - 모니터링, 분석, 복구 에이전트 간의 통신 구조.
- **이미지 2**: [TNR 검증 프로세스](https://researchgate.net/images/tnr-validation.png) - 복구 액션 전후의 상태 비교 및 롤백 매커니즘.

## 5. 추출된 관련 URL
- [Arxiv: STRATUS: Autonomous Cloud Reliability Engineering (2411.04586)](https://arxiv.org/abs/2411.04586)
- [ResearchGate: AIOps Trends: RCA to Mitigation](https://researchgate.net/publication/aiops-trends-2026)

## 6. 관련 노트 (Internal Links)
- [[wiki/Engineering/Infrastructure-and-DevOps/STRATUS]]
- [[wiki/Engineering/Infrastructure-and-DevOps/000_AIOps-MOC]]
- [[wiki/Engineering/Infrastructure-and-DevOps/STRATUS]] (Existing)

---
*Last Updated: 2026-03-14*
