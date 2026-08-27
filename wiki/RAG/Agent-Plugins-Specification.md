---
title: "Agent Plugins 1.0.0 표준 사양 및 에이전트 도구 패키징 규격"
related_raw: ["[[raw/Google Amazon Microsoft Standardize Agent Plugins for Skills and MCP | Shubham Saboo님이 토픽에 대해 올림.md]]"]
tags: ['#inbox', '#Agent-Plugins', '#MCP', '#AI-Agent', '#System-Architecture']
type: "wiki"
status: "published"
last_updated: "2026-08-23"
updated: "2026-08-23"
---

# Agent Plugins 1.0.0 표준 사양 및 에이전트 도구 패키징 규격

## 1. 개요 및 배경
* **파편화 문제**: 에이전트 스킬(Skills)과 MCP(Model Context Protocol) 서버를 배포할 때, 각 클라이언트(Claude Code, Cursor, Codex 등)마다 디렉터리 레이아웃, Manifest 파일, 설정 값의 규격이 달라 동일한 기능의 래퍼 코드가 클라이언트별로 파편화(Code Drift)되는 현상이 발생했습니다.
* **해결책**: Google, OpenAI, Amazon, Microsoft, Cursor, Vercel 등 주요 AI 기술 기업들은 공동으로 에이전트 확장 기능(스킬 및 MCP 서버) 패키징을 위한 공동 표준 규격인 **Agent Plugins 1.0.0**을 발표했습니다.

## 2. Agent Plugins 1.0.0 아키텍처 및 구성
플러그인은 독립적인 하나의 디렉터리로 구성되며 핵심 파일 구조는 다음과 같습니다:
* **`plugin.json`**: 플러그인의 기본 설명과 메타데이터를 선언하는 두 줄짜리 진입점 파일.
* **`skills/`**: 실행 가능한 에이전트 자율 스킬 코드가 들어가는 고정 디렉터리.
* **`mcp.json`**: 명시적인 전송 유형(Transport type)이 정의된 MCP 서버 설정 파일.
* **네임스페이스 폴더**: 특정 클라이언트(예: Cursor 전용 옵션 등)를 위한 특화 정보를 분리 저장하며, 해당하지 않는 클라이언트는 무시합니다.

## 3. 에이전트 생태계의 4대 레이어 스택
공동 표준 그룹이 제시하는 미래 에이전트 도구 스택은 다음의 4가지 추상화 레이어로 나뉩니다:
1. **탐색 (Discovery) - ARD (Agentic Resource Discovery)**: 클라이언트가 "이 태스크에 어떤 도구가 적합한가?"라고 질의하고 부합하는 리소스를 응답받는 개방형 프로토콜.
2. **기술 (Description) - AI Catalog**: ARD가 인덱싱하는 기준이 되는 카탈로그 포맷.
3. **패키징 (Packaging) - Agent Plugins**: 다른 클라이언트로 이식이 가능한 단일 고정 디렉터리 구조 규격.
4. **실행 (Execution) - MCP 및 Agent Skills**: 이미 이식성을 갖춘 도구 실행 계약 조건.

## 4. 해결해야 할 남은 과제: 신뢰 및 검증 (Trust Layer)
* 수만 개의 MCP 서버 생태계에서 중복되거나 공식 버전이 방치된 카탈로그가 많아지는 문제가 있습니다.
* 단순히 패키징 형식을 제어하는 것 외에, 보안 감사(Security Audit), 도메인 소유권 확인(Domain Ownership), 서버 가동률(Uptime History) 등 **신뢰 메타데이터**를 카탈로그 스펙에 직접 반영하여 검증할 수 있는 레이어의 정립이 필요합니다.
