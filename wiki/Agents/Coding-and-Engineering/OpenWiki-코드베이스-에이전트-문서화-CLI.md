---
title: OpenWiki 코드베이스 에이전트 문서화 CLI
tags: ["Agents", "Coding", "Documentation", "OpenWiki", "LangChain"]
type: wiki
status: published
created: 2026-07-05
updated: 2026-07-05
related_raw: ["[[2026-07-05-langchain_openwiki_codebase_agent_documentation_cli.md]]"]
---

# OpenWiki 코드베이스 에이전트 문서화 CLI

**OpenWiki**는 LangChain에서 개발한 CLI 도구로, AI 코딩 에이전트(Claude Code, Cursor 등)가 대규모 저장소에서 헤매지 않고 신속하게 코드의 컨텍스트를 로드하도록 돕기 위해, 저장소를 스캔하여 구조화된 위키(Wiki) 형태의 문서를 자동 생성하고 지속 보수하는 역할을 수행합니다.

## 1. 주요 기능 및 작동 구조

1. **자동화된 위키 스캐닝 및 빌드**
   - 저장소의 전체 코드를 분석하여 모듈 간 의존성, 디렉토리 구조, 코딩 스타일 컨벤션 등을 다룬 마크다운 위키 데이터를 `openwiki/` 디렉토리에 생성합니다.
2. **에이전트 진입점 파일 연동**
   - 위키 문서를 빌드한 후, 프로젝트 루트에 있는 `AGENTS.md` 또는 `CLAUDE.md` 파일에 해당 문서의 링크 정보를 자동으로 인젝션 및 갱신합니다. 이를 통해 코딩 에이전트가 작동 즉시 이 위키를 최우선 지식 소스로 읽게 만듭니다.
3. **GitHub Actions를 통한 문서 부패(Doc Rot) 방지**
   - 개발에 따라 수시로 코드가 수정되면 기존 수동 문서는 가치를 잃습니다. OpenWiki는 CI/CD 워크플로에 탑재되어 코드 병합 시마다 문서 갱신 작업을 자동으로 돌리고 Pull Request를 열어 문서 최신성을 자율 보장합니다.
4. **LangSmith를 통한 파이프라인 관측성 (Observability)**
   - 문서 생성과 갱신의 각 스케줄링 궤적(traces)을 LangSmith 대시보드와 동기화하여 API 호출 비용 및 병목을 실시간 모니터링할 수 있습니다.

## 2. 기본 활용 CLI 명령어

- `npm install -g openwiki`: 전역 설치.
- `openwiki --init`: API 제공자(OpenAI, Anthropic 등)와 API 키를 설정하여 로컬 `~/.openwiki/.env`를 구성하고 최초 코드 스캔 위키를 생성.
- `openwiki --update`: 저장소 최신 변경분을 분석하여 강제 문서 업데이트 진행.
- `openwiki -p "prompt"`: 1회성(One-shot) 프롬프트 모드로 문서 빌드 또는 인덱싱 조율.
- `openwiki`: 에이전트와 마주하여 문서 생성 작업을 주고받는 대화형(Interactive) CLI 모드 가동.

- **GitHub**: https://github.com/langchain-ai/openwiki

## 관련 문서
- [[wiki/Agents/Coding-and-Engineering/루프-엔지니어링-패러다임-및-시스템-안전.md]]
- [[wiki/Engineering/AI-Native-Engineering/Claude-Code-Next-Gen-Coding-Agent.md]]
- [[wiki/Engineering/AI-Native-Engineering/AI-시대의-제품-개발-역할군-5대-원형.md]]
