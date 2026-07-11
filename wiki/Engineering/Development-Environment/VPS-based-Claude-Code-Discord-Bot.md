---
title: "VPS 기반 Claude Code 및 디스코드 봇 구축 가이드"
related_raw: ["[[vpc open crew.md]]"]
tags: ["Engineering", "Dev-Env", "Claude_Code", "VPS", "Discord_Bot", "Automation"]
type: "wiki"
status: "published"
last_updated: "2026-05-15"
updated: "2026-05-15"
---

# 월 1만원대로 24시간 가동되는 나만의 클로드봇 구축

## 1. 개요
고가의 하드웨어(맥미니 등)를 상시 가동하는 대신, 저렴한 VPS(Virtual Private Server)를 활용하여 Claude Code를 24시간 가동하고, 디스코드 봇을 인터페이스로 사용하여 어디서든 모바일로 AI 에이전트를 호출하는 경제적인 구축 방법입니다.

## 2. 구축 3단계 워크플로우

### 1) VPS 환경 준비 (예: 호스팅어 VPS)
- 브라우저 터미널이나 SSH를 통해 접근.
- `curl` 명령어를 통해 Claude Code CLI를 설치.
- **장점**: 노트북을 켜둘 필요가 없으며, 전기세 및 하드웨어 유지비 절감.

### 2) 디스코드 봇 페어링
- **Discord Developer Portal**: 신규 봇 생성 및 토큰 확보.
- **Claude Channels/Plugin**: Claude Code 내부의 디스코드 플러그인을 활성화하여 봇과 페어링.
- **장점**: 터미널에 직접 접속하지 않고도 익숙한 채팅 UI(디스코드)를 통해 명령 가능.

### 3) 모바일/상시 호출 환경 완성
- 노트북을 닫은 상태에서도 스마트폰 디스코드 앱으로 봇에게 메시지 전송.
- VPS에서 돌아가는 Claude Code가 요청을 처리하고 답변 반환.

## 3. 비용 및 효율성 비교
| 항목 | 로컬 가동 (맥미니 등) | VPS + 디스코드 봇 |
| :--- | :--- | :--- |
| **초기 비용** | 약 110만 원 이상 | 0원 |
| **유지 비용** | 전기세 + 관리 노력 | 월 약 1.3만 원 |
| **가동 시간** | 수동 가동 또는 상시 전원 | **24시간 자동 상시 대기** |
| **접근성** | 물리적 위치 제약 | **전 세계 어디서든 모바일 호출** |

## 4. 시사점
하드웨어 소유 중심의 작업 환경에서 서비스 중심의 인프라 활용으로 패러다임이 전환되고 있습니다. 특히 AI 에이전트와 같이 상시 모니터링이나 즉각적인 피드백이 필요한 경우, VPS 기반의 구축이 가장 합리적인 대안이 됩니다.

## 관련 문서
- [[wiki/Engineering/Development-Environment/000_Development-Environment-MOC.md|개발 환경 MOC]]
- [[wiki/Engineering/Infrastructure-and-DevOps/000_Infrastructure-and-DevOps-MOC.md|인프라 및 DevOps MOC]]
- [[wiki/Engineering/AI-Native-Engineering/Claude-Code-Karpathy-Guidelines.md|Claude Code 지침]]
