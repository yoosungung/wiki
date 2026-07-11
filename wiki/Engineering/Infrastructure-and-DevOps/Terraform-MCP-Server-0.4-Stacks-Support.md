---
title: "Terraform-MCP-Server-0.4-Stacks-Support"
related_raw: ["[[wiki/Engineering/Infrastructure-and-DevOps/Terraform-MCP-Server-0.4-Stacks-Support.md]]"]
tags: ['wiki', 'agents_and_systems', 'aiops_&_ai-native_devtools', 'mcp_servers_for_devops_infrastructure_as_code']
type: "wiki"
status: "published"
last_updated: "2026-04-19"
updated: "2026-04-19"
---

# Terraform MCP 서버 0.4 업데이트: Stacks 지원 및 거버넌스 강화

## 개요
HashiCorp는 AI 에이전트가 Infrastructure as Code(IaC) 작업을 더 안전하고 효율적으로 수행할 수 있도록 **Terraform MCP(Model Context Protocol) 서버 0.4** 버전을 출시했습니다. 이번 업데이트의 핵심은 신규 기능인 'Terraform Stacks' 지원과 에이전트의 권한 관리 강화입니다.

## 주요 업데이트 내용

### 1. Terraform Stacks 지원
- AI 에이전트가 자연어를 통해 복잡한 인프라 스택을 배포, 관리 및 업데이트할 수 있게 되었습니다.
- 다중 환경(개발, 스테이징, 운영)에 걸친 리소스 오케스트레이션을 에이전트에게 위임하는 것이 가능해졌습니다.

### 2. 거버넌스 및 정책 제어 도구 추가
- **`attach_policy_set_to_workspaces` 도구:** AI 에이전트가 채팅 인터페이스를 통해 워크스페이스에 거버넌스 정책 세트를 직접 연결할 수 있습니다.
- 이를 통해 인프라 구축 단계에서부터 보안 및 규정 준수(Compliance)를 강제할 수 있는 에이전틱 워크플로우를 구축할 수 있습니다.

### 3. 에이전트 인프라 관리의 진화
- 단순한 리소스 조회를 넘어, 에이전트가 Terraform Cloud의 고급 기능을 제어할 수 있는 '표준화된 인터페이스'로서 MCP의 역할이 강화되었습니다.

## 기술적 시사점
- **에이전틱 인프라(Agentic Infrastructure):** 사람이 테라폼 코드를 직접 작성하는 비중이 줄어들고, 에이전트에게 목적(Goal)을 전달하면 에이전트가 스택을 구성하고 정책을 적용하는 시대로 이행하고 있습니다.
- **안전한 자동화:** 정책 제어 도구의 추가는 자율 에이전트의 예기치 못한 인프라 변경을 막을 수 있는 안전장치 역할을 합니다.

## 참고 및 관련 노트
- **원문 URL:** https://www.hashicorp.com/blog/announcing-terraform-mcp-server-0-4
- **관련 노트:**
    - [[wiki/Engineering/Infrastructure-and-DevOps/Harness-MCP-for-DevOps.md|Harness MCP 서버 및 DevOps 자동화]]
    - [[wiki/Engineering/Infrastructure-and-DevOps/AIOps-STRATUS-Claude-Code-MCP-Ecosystem.md|AIOps 및 MCP 생태계 개요]]
    - [[wiki/Agents/Frameworks/MCP/MCP.md|MCP 프로토콜 기술 상세]]
