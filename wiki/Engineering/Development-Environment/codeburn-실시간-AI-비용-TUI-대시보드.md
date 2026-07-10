---
related_raw: ["[[2026-06-25-codeburn_Interactive_AI_Cost_TUI_Dashboard.md]]"]
tags: ["#wiki", "codeburn", "AI-Cost-Tracking", "Agentic-Tools", "TUI", "Development-Environment"]
---

# codeburn: 실시간 AI 비용 및 토큰 사용량 관제 도구

**codeburn**은 터미널 기반 개발 환경(TUI)에서 AI 에이전트 및 코딩 도구를 기동할 때 소모되는 토큰 사용량과 누적 비용을 실시간 관제 및 프로파일링해 주는 인터랙티브 오픈소스 대시보드입니다.

## 1. 핵심 제공 기능
- **멀티 툴 통합 모니터링**: Claude Code, Cursor, Codex, Copilot 등 25종 이상의 최신 AI 개발 어시스턴트에서 나가는 트래픽 백엔드를 추적합니다.
- **비주얼 TUI**: 터미널 내에서 실시간 차트와 데이터 시각화를 제공하여, 현재 어떤 코드 파일 편집이나 프롬프트 구동이 과도한 비용을 발생시키고 있는지 즉시 모니터링 가능합니다.
- **토큰 폭발(Runaway) 제어**: 자율 루프 구조에서 에이전트가 예기치 않게 오류 피드백 루프에 갇혀 무한 호출되는 현상을 모니터링하고 차단 리미트를 연계하는 안전 장치로 유용하게 동작합니다.

## 🔗 연결된 문서
- [[wiki/Agents/Coding-and-Engineering/루프-엔지니어링-패러다임-및-시스템-안전.md]] — 토큰 폭발 등 자율 루프의 리스크 및 관제 구조.
- [[wiki/Engineering/Development-Environment/000_Development-Environment-MOC.md]]
