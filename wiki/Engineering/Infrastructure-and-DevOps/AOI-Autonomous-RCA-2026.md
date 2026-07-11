---
title: "AOI-Autonomous-RCA-2026"
related_raw: ["[[wiki/Engineering/Infrastructure-and-DevOps/AOI-Autonomous-RCA-2026.md]]"]
tags: ['wiki', 'agents_and_systems', 'aiops_&_ai-native_devtools']
type: "wiki"
status: "published"
last_updated: "2026-04-19"
updated: "2026-04-19"
---

# AOI (Autonomous Operations Intelligence) & Agentic RCA

## 1. 개요 (Overview)
AIOps 분야는 단순한 이상 탐지(Anomaly Detection)를 넘어, 에이전트가 자율적으로 시스템을 탐색하고 장애의 근본 원인을 분석하는 **Agentic RCA(근본 원인 분석)** 시대로 진입함. **AOI**는 기존의 정적인 분석 도구를 넘어 동적 추론을 수행하는 프레임워크임.

## 2. 핵심 아키텍처 (Key Architecture)

### 2.1. STRATUS의 한계 극복
- 기존의 **STRATUS**와 같은 다중 에이전트 SRE 시스템은 추론과 실행의 밀결합으로 인해 보안 및 안전성 문제가 있었음.
- **AOI**는 추론부(Reasoner)와 실행부(Executor)를 분리하고, 에이전트의 권한을 '읽기 전용 탐색(Probe)'과 '제한된 쓰기(Action)'로 계층화함.

### 2.2. GRPO 기반 지식 증류 (Distillation)
- 거대 모델(Claude 3.5 Sonnet 등)의 SRE 전문가 지식을 소형 로컬 모델(Qwen3-14B 등)에 **GRPO(Group Relative Policy Optimization)** 기법을 사용하여 증류함.
- 이를 통해 클라우드 비용을 절감하면서도 RCA 성공률을 기존 대비 24% 이상 향상시킴.

### 2.3. 자율적 가설 검증 (Hypothesis Testing)
- 에이전트가 장애 발생 시 로그, 메트릭, 트레이스를 통합 분석하여 잠재적 원인 가설을 세움.
- `MCP(Model Context Protocol)`를 통해 인프라 도구(kubectl, Prometheus 등)에 직접 연결하여 가설을 실시간으로 검증함.

## 3. RCA 성능 지표 (2026.03 기준)
- **RCA 성공률:** 최상위 모델인 Claude 4.5급도 복잡한 시스템에서는 약 30~40% 수준에 머물러 있으나, **AOI** 프레임워크 적용 시 구조화된 워크플로우를 통해 성공률을 15%p 이상 추가 확보 가능.
- **복구 시간(MTTR) 단축:** 인간 엔지니어의 수동 분석 대비 장애 인지 후 초동 대응까지의 시간을 평균 60% 단축.

## 4. AX1센터 적용 방안 (AIOps 제품 기획)
- **보안 중심 설계:** 에이전트가 인프라를 수정하기 전 반드시 인간의 승인을 거치는 `Human-in-the-loop` 구조(LangGraph v1.0 패턴) 도입 필수.
- **MCP 기반 인프라 연결:** 사내 메트릭 시스템을 MCP 서버로 추상화하여 에이전트와의 호환성 즉시 확보.
- **지식 그래프 연동:** 장애 이력을 `Cognee`와 같은 도구로 지식 그래프화하여 유사 장애 발생 시 과거 대응 이력을 즉시 참조할 수 있도록 설계.

---
**출처**: [Autonomous RCA with Reasoning Models (AOI Research, 2026.03)](https://arxiv.org/abs/2603.09123)
**관련 노트:** `[[wiki/Engineering/Infrastructure-and-DevOps/000_AIOps-MOC]]`, `[[wiki/Engineering/Infrastructure-and-DevOps/STRATUS-Autonomous-Reliability]]`
