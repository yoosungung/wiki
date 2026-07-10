---
title: "Claude-Mem 지속적인 메모리 압축 시스템"
related_raw: ["[[wiki/Agents/Memory-and-Cognition/Claude-Mem 지속적인 메모리 압축 시스템.md]]"]
tags: ['wiki', 'agents_and_systems', 'llm_agent_&_deep_agents', 'tools']
type: "wiki"
status: "published"
last_updated: "2026-04-19"
---

# Claude-Mem: Claude Code를 위한 지속적인 메모리 압축 시스템

Claude-Mem은 Claude Code를 위한 지속적인 메모리 압축 시스템으로, 도구 사용 관찰을 자동으로 캡처하고 의미론적 요약을 생성하여 세션 간 컨텍스트를 보존합니다.

### 주요 기능

*   **지속적인 메모리 유지**: 세션 간 컨텍스트를 보존합니다.
*   **점진적 공개**: 점진적으로 정보를 공개합니다.
*   **스킬 기반 검색**: 스킬을 기반으로 정보를 검색합니다.
*   **웹 뷰어 UI**: 웹 인터페이스를 제공합니다.
*   **개인정보 제어**: 개인정보를 제어할 수 있습니다.

### 시스템 요구사항

*   Node.js 18.0.0 이상
*   Claude Code
*   Bun
*   uv
*   SQLite 3

### 아키텍처

*   5개의 라이프사이클 후크
*   워커 서비스
*   SQLite 데이터베이스
*   mem-search 스킬
*   Chroma 벡터 데이터베이스

### 관련 링크

*   [Claude-Mem GitHub](https://github.com/thedotmack/claude-mem)
*   [웹 뷰어 UI (로컬)](http://localhost:37777)

### 관련 노트

*   Claude Code
*   AI Memory
*   SQLite
*   ChromaDB
*   AI Agent
