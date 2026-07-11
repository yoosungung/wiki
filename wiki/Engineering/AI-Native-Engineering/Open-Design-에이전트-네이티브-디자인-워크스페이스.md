---
title: "Open Design: 에이전트 네이티브 로컬 퍼스트 디자인 워크스페이스"
tags: ["Open-Design", "Claude-Design", "Agent-UI", "Local-First", "Design-Engine"]
last_updated: "2026-07-06"
updated: "2026-07-06"
related_raw: ["[[2026-07-06-nexu_io_open_design.md]]"]
---

# 🎨 Open Design: 에이전트 네이티브 로컬 퍼스트 디자인 워크스페이스

Open Design(nexu-io/open-design)은 Anthropic의 Claude Design Workspace를 로컬 환경에 구현한 에이전트 네이티브 디자인 협업 워크벤치입니다.

## 1. 작동 아키텍처
- **로컬 퍼스트 데스크톱 앱**: 사내 보안 격리망 환경에서도 구동 가능하도록 설계된 로컬 우선 데스크톱 환경.
- **에이전트가 디자인 엔진으로 기동**: 로컬에서 작동하는 CLI 코딩 에이전트(Claude Code, Codex, Cursor, Gemini, Qwen-Coder 등 20+ CLI)를 디자인 엔진으로 연동(BYOK 방식).
- 에이전트가 프론트엔드 코드나 에셋을 실시간 수정하면, 디자이너 수준의 인터랙티브 프로토타입, 랜딩 페이지, 슬라이드, 대시보드로 즉시 시각화함.
- 결과물은 실시간 HTML/PDF/PPTX/MP4 파일로 바로 내보내기(Export)가 가능하여 개발 단계의 피드백 루프를 대폭 단축함.

---
**관련 문서**:
- [[wiki/Engineering/AI-Native-Engineering/Block-자율-개발-배포-플랫폼-아키텍처.md]]

