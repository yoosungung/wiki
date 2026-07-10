---
title: "Harness-MCP-for-DevOps"
related_raw: ["[[wiki/Engineering/Infrastructure-and-DevOps/Harness-MCP-for-DevOps.md]]"]
tags: ['wiki', 'agents_and_systems', 'aiops_&_ai-native_devtools']
type: "wiki"
status: "published"
last_updated: "2026-04-19"
---

# Harness: DevOps를 위한 MCP 서버 출시

## 요약
DevOps 플랫폼 Harness가 에이전트와 외부 도구를 연결하는 표준 프로토콜인 **MCP(Model Context Protocol)** 서버를 정식 출시했습니다. 이를 통해 AI 에이전트가 직접 파이프라인 오류를 진단하거나 클라우드 비용을 최적화하는 등 고도화된 DevOps 자동화가 가능해집니다.

## 핵심 기능
- **MCP 기반 연동**: Claude Code, Cursor 등 다양한 AI 에이전트가 Harness의 API와 데이터에 직접 접근 가능.
- **자율적 파이프라인 디버깅**: 빌드 실패 원인을 AI가 분석하고 해결책을 제시하거나 직접 수정 제안.
- **비용 최적화 가이드**: 클라우드 자원 사용 현황을 분석하여 비용 절감 포인트를 에이전트가 식별.
- **DORA 메트릭 분석**: 팀의 개발 생산성 지표를 실시간으로 모니터링하고 개선 방안 제안.

## 기존 지식과의 연결
- [[wiki/Engineering/Infrastructure-and-DevOps/STRATUS|자율 SRE 시스템 STRATUS]]: STRATUS와 같은 자율적 완화(Mitigation) 시스템이 실제 인프라 도구(Kubernetes, CI/CD 등)와 안전하고 표준화된 방식으로 상호작용하기 위한 '도구 주머니(Toolbox)' 역할을 수행합니다.
- [[wiki/Engineering/Infrastructure-and-DevOps/000_AIOps-MOC|AIOps MOC]]: 운영 자동화를 넘어 AI가 주도하는 지능형 DevOps 환경 구축의 핵심 인프라로 정의됩니다.
- LLM-Agent: 에이전트가 사용할 수 있는 '표준화된 도구 주머니'로서의 MCP 가치 입증.
- Autonomous SRE: 장애 탐지, 분석, 복구의 전 과정을 AI가 수행하는 STRATUS와 같은 시스템의 기반 인프라.

## 원문 URL
https://harness.io/blog/mcp-for-devops
