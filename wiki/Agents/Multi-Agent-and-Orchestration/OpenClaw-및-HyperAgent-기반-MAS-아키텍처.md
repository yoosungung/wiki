---
title: "OpenClaw 및 HyperAgent 기반 MAS 아키텍처 (2026)"
tags: ["Agents", "MAS", "OpenClaw", "HyperAgent", "Orchestration", "TaskFlow"]
type: "wiki"
status: "published"
last_updated: "2026-08-02"
updated: "2026-08-02"
related_raw: ["[[2026-07-30-openclaw-session-memory-flush.md]]", "[[2026-07-29-openclaw-hooks-mcp-proto-multi-account.md]]", "[[2026-07-28-openclaw-watched-session-sandbox-network.md]]", "[[2026-07-27-openclaw-route-bindings-grep-naming-harness.md]]", "[[2026-07-26-openclaw-session-urls-oauth-resume.md]]", "[[2026-06-12-Autonomous-Agents-OpenClaw-HyperAgent-Update.md]]", "[[2026-06-15-Autonomous-Agents-OpenClaw-HyperAgent-Update.md]]", "[[2026-06-17-Research-Synthesis-Update.md]]"]
---

# 🤖 OpenClaw 및 HyperAgent 기반 MAS 아키텍처 (2026)

2026년은 멀티 에이전트 시스템(MAS)이 보편화된 해로, 단일 모델의 한계를 극복하기 위한 자율 운영 및 자가 최적화 프레임워크가 시장을 주도하고 있습니다.

## 1. OpenClaw AI Agent Framework
OpenClaw는 LLM을 로컬 하드웨어에서 동작하는 "자율 운영자(Autonomous Operator)"로 변환하는 선도적인 오픈소스 오케스트레이션 레이어입니다.

- **Cron announce / Codex auth / Telegram preamble (2026-08-02)**: 멀티 채널 isolated announce 생성 게이트(#118272), Codex 마이그레이션 시 선택 OAuth 유지(#118205), Telegram CLI tool 중 pre-tool 텍스트 보존. 상세는 [[wiki/Agents/Multi-Agent-and-Orchestration/자율수행-멀티-에이전트-시스템-오케스트레이션-및-보안-격리-2026.md]].
- **Session memory flush / gateway list (2026-07-30)**: 부모 recovery와 memory flush 생명주기 분리(#116198), retained subagent history 하에서도 `sessions_list` 응답성(#116533), startup stall·WS heartbeat. 상세는 [[wiki/Agents/Multi-Agent-and-Orchestration/자율수행-멀티-에이전트-시스템-오케스트레이션-및-보안-격리-2026.md]].
- **Root-owned plugin bundle (2026-08-01)**: root-owned 번들 설치 + scoped registry handles(#117587) — 멀티 테넌트 Gateway에서 plugin registry 오염 방지. 상세 동일.
- **Watched-session / sandbox browser (2026-07-28)**: ambient watched group/topic을 모델에 명시(#114835), Docker `network=none` 브라우저 사이드카 거부·`doctor --fix`(#115250), warm turn·session 바인딩. 상세는 [[wiki/Agents/Multi-Agent-and-Orchestration/자율수행-멀티-에이전트-시스템-오케스트레이션-및-보안-격리-2026.md]].
- **Multi-account hooks / MCP `__proto__` (2026-07-29)**: hook delivery 계정 스코프 보존(#116095), MCP 서버명 `__proto__` 거부(#116112), Gateway backoff. 상세 동일.
- **Route bindings / naming / harness (2026-07-27)**: gateway message route bindings를 shared dedupe에서 context WeakMap으로 격리(`DEDUPE_MAX*4` 별칭 보존), `AGENTS.md` grep-discoverability(2–3단어 export·`utils/` 금지), GPT-5.6 coding harness 오버헤드 감소(#114574). 상세는 [[wiki/Agents/Multi-Agent-and-Orchestration/자율수행-멀티-에이전트-시스템-오케스트레이션-및-보안-격리-2026.md]].
- **Control UI / discovery / restart (2026-07-26)**: path 기반 세션·대시보드 URL(`/chat/...`, `/dashboard/...`, session key 고정), Anthropic OAuth discovery(`sk-ant-oat` → Bearer), 재시작 시 `stopReason: aborted` 재개, ClawHub skill 아이콘. 상세는 [[wiki/Agents/Multi-Agent-and-Orchestration/자율수행-멀티-에이전트-시스템-오케스트레이션-및-보안-격리-2026.md]].
- **v2026.6.17 업데이트 (2026.06.17)**:
    - **Lane Queue 고도화**: 중단된 태스크가 세션을 점유하여 발생하는 "Wedged Lane" 현상을 해결하기 위한 **Reconciliation Fix (2026-06-09)** 적용. 비정상 종료 시에도 즉각적인 실행 레인 해방 보장.
    - **Active Memory (액티브 메모리)**: 기존 정적 컨텍스트 로딩 방식에서 탈피하여, **Observed(관찰), Confirmed(확인), Inferred(추론)**의 3단계로 구성된 **Providence 메타데이터** 기반 동적 메모리 시스템 도입.
    - **NemoClaw Sandbox**: NVIDIA와의 협업으로 구현된 커널 레벨 샌드박스로, 에이전트의 셸 명령어 실행 권한을 YAML 정책으로 엄격히 제한.
    - **TaskFlow Persistence**: 모든 태스크 상태와 워크플로우 레저를 **SQLite 백엔드**에 실시간 저장하여 하드웨어 재시작 후에도 작업 연속성 유지.

- **5대 서브시스템 아키텍처**:
    - **Channel Adapters**: WhatsApp, Slack 등 20+ 플랫폼 메시지 번역.
    - **The Gateway**: 세션, 도구, 이벤트를 관리하는 로컬 중심 제어 평면.
    - **The Brain**: 모델 애그노스틱(Model-agnostic) 추론 엔진.
    - **The Task Brain (TaskFlow)**: SQLite 기반 태스크 레저를 통해 에이전트 작업을 스케줄링하고 상태를 관리.
    - **Active Memory**: Providence 메타데이터를 포함한 3계층 영구 지식 베이스.

## 2. HyperAgent: 자가 수정을 포함한 차세대 MAS
HyperAgent는 단순한 대행을 넘어 에이전트 스스로의 성능을 개선하는 "메타인지" 아키텍처를 지향합니다.

- **Meta Hyperagents (DGM-H)**:
    - **자가 참조(Self-referential)** 구조: 태스크 해결 로직과 자가 개선 로직을 단일 프로그램으로 통합.
    - **메타인지 자가 수정**: 에이전트가 자신의 개선 로직(DGM-H)을 스스로 재작성하여 성능 추적 및 메모리 관리 방식을 학습하고 도메인 간 전이. (2026.06.16 업데이트)

## 3. 2026년 MAS 기술 트렌드
- **SIRA (Superintelligent Retrieval Agent)**: 다단계 검색 과정을 단일 액션으로 압축하여 지연 시간을 획기적으로 줄인 차세대 검색 에이전트 부상 (2026.06.05 발표).
- **YOLO Mode vs. Auto Mode**:
    - **YOLO Mode**: 사용자 확인 없이 즉시 도구 및 명령 실행. 생산성은 높으나 위험 요소 상존.
    - **Auto Mode (2026.06.18 업데이트)**:
        - **Guardian Pattern**: 다층 검증 아키텍처로, OpenAI Codex의 가디언 리뷰와 연동하여 에이전트의 실행 권한을 동적으로 제어.
        - **Review Packet**: 정책 범위를 벗어난 명령 발생 시, 명령/인자/환경 정보를 포함한 '리뷰 패킷'을 생성하여 Auto-Reviewer 모델에 위임.
        - **Risk Scoring**: 0-100 scale의 실시간 리스크 점수화. 저위험 명령은 자동 승인하고 임계값을 넘는 고위험 작업만 인간에게 라우팅.
- **Zero-Trust Security**: 에이전트 간 모든 데이터 핸드오프에 디지털 서명과 감사를 적용하는 아키텍처가 표준으로 자리 잡음.
- **God Model의 종말**: 단일 거대 모델 대신 **Supervisor-Worker** 구조의 MAS 선호.
- **상호운용성 표준**: MCP(Model Context Protocol) 및 A2A(Agent-to-Agent) 프로토콜을 통한 벤더 간 에이전트 협업.

---
**관련 문서**:
- [[wiki/Agents/Frameworks/Siri-AI-및-Apple-Intelligence-에이전트-프레임워크-2026]]
- [[wiki/Agents/Multi-Agent-and-Orchestration/000_Multi-Agent-and-Orchestration-MOC]]
