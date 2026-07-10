---
title: "STRATUS-Autonomous-SRE-Multi-Agent"
related_raw: ["[[wiki/Engineering/Infrastructure-and-DevOps/STRATUS-Autonomous-SRE-Multi-Agent.md]]"]
tags: ['wiki', 'agents_and_systems', 'aiops_&_ai-native_devtools']
type: "wiki"
status: "published"
last_updated: "2026-04-19"
---

# STRATUS: 멀티 에이전트 기반의 자율 SRE 시스템

### 1. 개요 및 핵심 컨셉
**STRATUS**는 대규모 클라우드 인프라의 장애 탐지, 진단, 복구를 자율적으로 수행하는 **Autonomous SRE(Site Reliability Engineering)** 시스템입니다. 단일 모델이 아닌, 각각의 전문 분야(로그 분석, 지표 모니터링, 인프라 변경)를 가진 멀티 에이전트들이 협업하는 구조를 통해 복잡한 시스템 장애의 근본 원인(RCA)을 신속하게 파악하고 해결합니다.

### 2. 주요 기술 세부 사항
- **Multi-Agent Orchestration:** 각 에이전트는 독립된 컨텍스트를 가지며, 메인 오케스트레이터가 과업을 할당하고 결과를 통합합니다. 이는 에이전트 간의 간섭을 줄이고 전문성을 높입니다.
- **TNR (Transactional No-Regression):** 에이전트가 시스템 설정을 변경하거나 복구 작업을 수행할 때, 기존 시스템에 악영향을 주지 않음을 사전에 검증하고 트랜잭션 단위로 실행하는 안전 메커니즘입니다.
- **RCA Performance:** 기존 규칙 기반 시스템이나 단일 LLM 접근 방식 대비 장애 원인 분석 성능을 1.5배 이상 향상시켰습니다.

### 3. 관련 기술 URL 및 리소스
- [STRATUS: Autonomous SRE Whitepaper](https://arxiv.org/abs/2603.bbbbb)
- [AIOps with Multi-Agent Systems Blog](https://example.com/aiops-stratus)
- [SRE Automation Best Practices](https://example.com/sre-auto)

### 4. 설명 이미지 추출 (Conceptual)
- ![STRATUS Architecture](https://example.com/stratus-arch.png) (멀티 에이전트 협업 및 TNR 검증 레이어 구조도)
- ![RCA Performance Chart](https://example.com/stratus-rca.png) (장애 복구 시간 및 정확도 비교 차트)

### 5. 관련 노트 링크
- [[wiki/Engineering/Infrastructure-and-DevOps/STRATUS-Deep-Dive-2026]]
- [[wiki/Engineering/Infrastructure-and-DevOps/STRATUS]]
- [[wiki/Engineering/Infrastructure-and-DevOps/AOI-Autonomous-RCA-2026]]
- [[wiki/Engineering/Infrastructure-and-DevOps/STRATUS-Autonomous-Reliability]]
