---
title: "Model Context Protocol (MCP): LLM과 데이터 소스의 표준 인터페이스"
related_raw: ["[[raw/2026-04-18-Model-Context-Protocol-Overview]]"]
tags: ["wiki", "MCP", "AI-Standard", "T2SQL"]
type: "wiki"
status: "on-hold (postponed)"
last_updated: "2026-04-19"
---

# Model Context Protocol (MCP) 개요

> **⚠️ 참고**: 현재 T2SQL v2 로드맵에서 본 항목의 우선순위는 조정되었습니다. 현재는 데이터 자산화 및 세만틱 레이어 구축에 집중하고 있으며, MCP 통합은 향후 인터페이스 표준화 단계에서 다시 검토될 예정입니다.

MCP는 Anthropic이 제안한 오픈 표준으로, LLM이 외부 데이터 소스(Resource), 실행 도구(Tool), 프롬프트 템플릿(Prompt)을 일관된 방식으로 통합할 수 있도록 지원하는 프로토콜입니다.

## 🌟 핵심 구성 요소
1. **Resources (데이터 소스)**:
   - 데이터베이스 스키마, 메타데이터, 로그 파일 등을 LLM에 컨텍스트로 제공합니다.
   - Text-to-SQL 작업에서 데이터베이스 구조를 실시간으로 모델에 전달하는 통로가 됩니다.

2. **Tools (실행 도구)**:
   - SQL 쿼리 실행, 데이터 변환, 코드 실행 등 LLM이 호출할 수 있는 능력을 정의합니다.
   - 모델이 쿼리를 작성한 후 즉시 테스트하고 결과를 분석할 수 있게 합니다.

3. **Universal Connector (AI용 USB-C)**:
   - 한 번 구축한 MCP 서버는 Claude, Cursor, 각종 자체 개발 에이전트 등 다양한 호스트에서 공통으로 사용할 수 있습니다.

## 🎯 T2SQL 프로젝트에서의 활용
- **T2SQL MCP 서버 개발**: 데이터베이스 메타데이터와 스키마 정보를 Resources로 노출하고, SQL 실행기(Executor)를 Tools로 제공합니다.
- **에이전트 워크플로우**: 모델이 스키마를 동적으로 탐색하고, 생성된 SQL의 유효성을 도구를 통해 반복적으로 검증하는 "에이전틱 워크플로우"를 구현합니다.

## 🔗 관련 문서
- [[wiki/Agents/Text-to-SQL/Spider-2.0]]
- [[T2SQL_Planning]]
