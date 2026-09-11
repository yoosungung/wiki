---
title: "Alook: 협업형 AI 에이전트 워크포스(Workforce) 플랫폼"
last_updated: "2026-07-28"
updated: "2026-07-28"
related_raw: ["[[raw/2026-07-28-alook_ai_agent_workforce_collaboration_layer.md]]"]
tags: [Multi-Agent, Orchestration, Collaboration, Alook, Local-First]
---

# Alook: 협업형 AI 에이전트 Workforce 플랫폼

이 문서는 AI 에이전트 팀을 조직하고 이메일 및 공유 메모리를 통해 오케스트레이션하는 오픈소스 자가 서빙 플랫폼인 **Alook**의 구조와 인프라 통합 기능을 분석합니다.

---

## 1. 개요

**Alook**은 단독으로 작동하는 에이전트(Claude Code, Codex, OpenCode 등)들을 통합하여, 기업 내 가상의 **AI 부서(AI Workforce: 개발, 운영, 기획 등)**를 구성하고 조율할 수 있도록 돕는 로컬 퍼스트(Local-first) 오픈소스 오케스트레이션 플랫폼입니다. 에이전트 간의 정보 격리, 협업 프로토콜, 공유 메모리 동기화를 자동 관리하여 대규모 작업 세션을 성공적으로 수행하도록 지원합니다.

---

## 2. 핵심 기능 및 협업 인프라

Alook은 에이전트들이 실제 인간 조직처럼 기능할 수 있도록 다양한 현실 인프라 채널을 제공합니다.

### 2.1. 이메일 기반 에이전트 호출 및 조율
- 에이전트마다 고유의 가상 이메일 주소(예: `dev@alook.ai`, `research@alook.ai`)를 할당합니다.
- 에이전트들은 상호 간에 이메일을 주고받으며 요구사항을 전달하고 승인 요청을 수행합니다. 이메일 스레드를 통해 히스토리가 기록되므로 인간 개발자도 쉽게 모니터링할 수 있습니다.

### 2.2. 공유 메모리와 칸반 보드 (Shared Memory & Board)
- **Shared Memory Layer**: 에이전트들이 공동 지식창고를 공유하여 중복 조사를 배제하고 한 에이전트가 알아낸 사실(인프라 포트, 스펙 등)을 다른 에이전트에게 전파합니다.
- **Kanban Board**: 태스크를 작업 카드로 관리하며, 에이전트들이 주도적으로 칸반 상태를 업데이트하며 협업 프로세스를 시각화합니다.

```text
               Alook 멀티 에이전트 협업 구조
               =============================
               
                  [Alook Onboard Server]
                            │
         ┌──────────────────┼──────────────────┐
         ▼                  ▼                  ▼
    [Dev Agent]       [Ops Agent]       [Research Agent]
  (dev@alook.ai)    (ops@alook.ai)    (research@alook.ai)
         │                  │                  │
         └───────── 공유 메모리 & 이메일 통신 ───────┘
```

---

## 3. 실전 구축 및 온보딩 가이드

Alook은 Bun, Next.js, Cloudflare Workers 기반 스택으로 이루어져 있으며, 단일 CLI 명령어로 로컬 인프라를 신속하게 기동할 수 있습니다.

### 3.1. Onboarding 가이드
```bash
# 로컬 개발 환경에서 Alook 가상 회사 개설 및 에이전트 온보딩
npx @alook/app onboard
```
이 명령어를 구동하면 로컬 런타임 환경을 스캔하고 필요한 백엔드 서비스를 실행한 후 웹 대시보드(기본 주소: `http://localhost:15210`)를 오픈합니다. 

---

## 🔗 관련 문서 링크
- 멀티 에이전트 오케스트레이션 연구: [[wiki/Agents/Multi-Agent-and-Orchestration/자율수행-멀티-에이전트-시스템-오케스트레이션-및-보안-격리-2026.md]]
- OpenClaw 및 HyperAgent 기반 MAS: [[wiki/Agents/Multi-Agent-and-Orchestration/OpenClaw-및-HyperAgent-기반-MAS-아키텍처.md]]
- [[wiki/Agents/Multi-Agent-and-Orchestration/000_Multi-Agent-and-Orchestration-MOC.md]]
- [[index.md]]
