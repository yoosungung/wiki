---
title: "Block의 빌더봇(Builderbot) 및 구스(Goose) 아키텍처"
tags: ["Block", "Goose", "Builderbot", "Actionable-CI", "Repo-Readiness", "MCP", "AI-Native-Engineering"]
last_updated: "2026-07-06"
updated: "2026-07-06"
related_raw: ["[[2026-07-06-block_autonomous_development_delivery_platform.md]]"]
---

# 🚀 Block의 빌더봇(Builderbot) 및 구스(Goose) 아키텍처

글로벌 기술 기업 Block(구 Square)은 AI 에이전트를 개발 워크플로우에 전면 통합하여 소프트웨어 엔지니어링 패러다임을 **바이브 코딩(Vibe Coding)** 및 **자율 개발·배포 플랫폼**으로 전환시켰습니다.

## 1. 전사 자율 개발·배포 시스템 다층 구조
- **Builderbot (빌더봇)**: Slack과 연동하여 이슈 트래킹(Linear/Jira)을 감지하고 개발 세션을 생성하는 조율 계층.
- **Goose (구스)**: Rust 기반의 에이전트 실행 엔진(Apache 2.0). 호스트 내 셸 실행, 로컬 테스트 및 병렬 서브에이전트를 구동함. **Agent Client Protocol (ACP)**을 준수하여 Zed, VS Code 등의 에디터와 연동됨.
- **Model Context Protocol (MCP)**: Anthropic과 협력 설계한 이기종 데이터 및 도구 연결 프로토콜.
- **Actionable CI (액셔너블 CI)**: 3단계 검증 시스템.
    1. *정적 분석*: 린터 및 정규식 규칙으로 명확한 오류 사전 필터링.
    2. *LLM 맥락 추론*: Git 변경 이력과 빌드 로그를 분석하여 원인을 한글 자연어 등으로 캐싱.
    3. *에이전틱 오토픽스*: 헤드리스 구스가 자율적으로 드래프트 PR을 발송하고 가상 도커 내에서 재검증(3회 시도).
- **레포 준비성(Repo Readiness)**: 저장소 성숙도를 Locked -> Novice -> Adept -> Artisan으로 구분하여 에이전트의 권한을 차등 통제함. 메인 루트에 기계 판독용 `AGENTS.md` 및 `SKILL.md`를 필수로 배치하여 에이전트가 로컬 변경 전후에 `just fmt` 및 `just test` 등의 선행 점검을 하도록 규제함.

## 2. 보안 무결성 감사 및 방어 전략
- **오퍼레이션 페일 파이어 (Operation Pale Fire)**: 자체 레드팀이 감행한 보안 위협 분석.
    - *제로 너비 유니코드 은닉 공격*: 외부 일정 API 등에 제로 너비 유니코드로 악성 명령을 숨겨 에이전트가 로컬 셸에서 백그라운드로 악성코드를 실행하도록 유도.
    - *Base64 인코딩 레시피 탈취*: 시스템 프롬프트 헤더 영역에 Base64로 인코딩된 악성 파이썬 실행 명령어를 유도하여 API 키 등을 가로채는 위험.
- **방어 대책**:
    - Docker 가상 격리 샌드박스 및 화이트리스트 셸 명령 제한.
    - 사내 Artifactory 거버넌스 저장소 프록시 필터 통제.
    - **Model Ledger (모델 레저)**: 미세 조정 모델, 빌드 룰, 검증 데이터 가동 경로를 방향 그래프 데이터 모델로 구축하여 비인가 모델의 무단 호출 및 유출 이력을 원천 통제.

## 3. 지식 자산 거버넌스 및 대규모 마이그레이션 실증
- **이원화 MCP**:
    - *Block Data MCP*: CFO 전용. 메트릭 스토어(Metricflow)의 검증된 매크로 쿼리만 사용하여 100% 정합성을 수호.
    - *Query Expert MCP*: 비즈니스 분석팀 전용. 동적 SQL을 생성하여 다차원 분석 지원.
- **Fluent UI 무유휴 마이그레이션**: 레거시 Base Web UI를 Fluent UI로 대치할 때, 1차로 TypeScript diagnostics 언어 지능 서버를 로컬에 구축하여 의존성/심볼을 판단한 뒤, 구스 에이전트가 컴파일 에러 피드백을 실시간 피딩받아 일괄 수정을 진행하여 전사 시스템 중단(Flag Day) 없이 완수함.

---
**관련 문서**:
- [[wiki/Agents/Coding-and-Engineering/루프-엔지니어링-패러다임-및-피드백-시스템-설계.md]]
- [[wiki/Engineering/AI-Native-Engineering/AI-시대의-제품-개발-역할군-5대-원형.md]]
- [[wiki/Engineering/AI-Native-Engineering/Open-Design-에이전트-네이티브-디자인-워크스페이스.md]]

