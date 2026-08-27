---
tags:
  - inbox
type: wiki
status: published
---

# Karpathy Agentic Engineering Lifecycle

최근 에이전트 구축 툴링이 크게 성숙해지면서, 에이전트 개발 과정의 핵심이 코드 작성 자체보다는 그 이후의 프로덕션 배포 및 관리 라이프사이클로 이동하고 있습니다. Google의 **Agents CLI**와 오픈소스 스킬을 활용하면 코딩 에이전트 내에서 자연어 프롬프트만으로 전체 라이프사이클을 쉽게 제어할 수 있습니다.

## 에이전트 엔지니어링 라이프사이클 6단계

1.  **Setup (설정)**
    *   단일 명령어로 Claude Code, Cursor, Codex, Antigravity 등의 코딩 에이전트에 라이프사이클 제어 스킬을 주입합니다.
2.  **Build (빌드)**
    *   자연어 프롬프트를 기반으로 에이전트 및 결정론적(Deterministic) 도구들의 기본 구조(Scaffold)를 생성하고, 로컬 플레이그라운드에서 테스트합니다.
3.  **Deploy (배포)**
    *   에이전트가 실행 간 상태를 유지할 수 있도록 세션(Sessions)과 메모리 뱅크(Memory Bank)를 지원하는 Agent Runtime에 배포합니다.
4.  **Govern (거버넌스 및 보안)**
    *   에이전트 전용의 최소 권한(Least-privilege) ID를 프로비저닝합니다.
    *   Model Armor를 통해 신뢰할 수 없는 텍스트의 프롬프트 인젝션 시도를 차단합니다.
    *   승인된 아웃바운드(Egress) 호스트 허용 목록을 통해서만 통신하도록 네트워크를 격리합니다.
5.  **Evaluate (평가)**
    *   환각(Hallucination) 및 답변의 근거(Grounding)를 검증합니다.
    *   기존 기능의 회귀(Regression)가 없음을 증명하면서 프롬프트를 최적화합니다.
6.  **Publish (게시)**
    *   조직 전체가 사용할 수 있도록 완성된 에이전트를 Gemini Enterprise(또는 엔터프라이즈 환경)에 등록합니다.
