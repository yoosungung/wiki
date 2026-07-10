---
title: "SkillSpector: NVIDIA의 AI 에이전트 스킬 보안 취약점 정적 및 LLM 세맨틱 스캐너"
tags: ["SkillSpector", "NVIDIA", "Agent-Security", "Vulnerability-Scan", "Data-Security"]
last_updated: "2026-07-06"
related_raw: ["[[2026-07-06-nvidia_skillspector_vulnerability_scanner.md]]"]
---

# 🛡️ SkillSpector: NVIDIA의 AI 에이전트 스킬 보안 취약점 정적 및 LLM 세맨틱 스캐너

NVIDIA의 **SkillSpector**는 AI 에이전트 스킬 및 도구(Tooling)의 설치 및 실행 전에 보안 임계값을 검사하여 호스트 시스템을 탈취로부터 방어하는 보안 스캐너입니다.

## 1. 타깃 취약점 유형 (60여 가지 패턴)
- **프롬프트 인젝션 (Prompt Injection)**: 시스템 프롬프트 헤더를 오염시켜 내부 정책을 우회시키는 위협.
- **과도한 권한 대행 (Excessive Agency)**: 에이전트가 필요 이상으로 파일 시스템 루트나 내부 네트워크 셸에 접근할 수 있게 열어주는 결함.
- **데이터 유출 (Data Exfiltration)**: Base64로 인코딩된 스크립트 등을 통해 사내 API 키, SSH 크레덴셜 정보를 외부 악성 C2 서버로 전송하는 위협.
- **MCP 포이즈닝 (Model Context Protocol Poisoning)**: 외부 API Specifications에 인젝션을 주입하여 에이전트 터미널에 악성 모듈을 빌드하도록 유도.

## 2. 2단계 분석 파이프라인
1. **정적 검사 (Static Analysis)**: regex 및 AST 분석을 통해 알려진 유해 셸/파이썬 파일 접근 코드 및 패턴을 빠르게 일차 필터링함.
2. **LLM 세맨틱 검사 (Semantic Analysis)**: 정적 검사에서 검출되지 않은 제로 너비 유니코드 등 은닉된 자연어 공격 의도를 LLM 추론을 가동해 검증하여 False Positive를 절감함.
- **평가지표**: 0~100 리스크 스코어 및 SARIF 규격 출력 보고서 제공을 통해 Actionable CI 게이트웨이에 통합 적용.

---
**관련 문서**:
- [[wiki/Agents/Frameworks/BuildingAI-적목식-AI-앱-빌더-및-보안-취약점.md]]
- [[wiki/Engineering/Data-and-Security/000_Data-and-Security-MOC]]

