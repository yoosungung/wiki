---
title: "BuildingAI: 적목식(Block-style) AI 애플리케이션 빌더 및 SSRF 보안 취약점 (CVE-2026-7065)"
tags: ["BuildingAI", "BidingCC", "AI-Builder", "SSRF", "Vulnerability", "Security"]
last_updated: "2026-07-06"
updated: "2026-07-06"
related_raw: ["[[2026-07-06-bidingcc_building_ai.md]]"]
---

# 🧱 BuildingAI: 적목식 AI 애플리케이션 빌더 및 SSRF 보안 취약점

BidingCC/BuildingAI는 "AI 시대의 워드프레스"를 지향하는 적목식(Block-style) AI 애플리케이션 구축 시스템입니다.

## 1. 아키텍처 및 주요 기능
- 비개발자를 포함한 누구나 쉽게 드래그 앤 드롭 형태로 블록을 조립하여 자신만의 AI 애플리케이션(기업용 지능형 에이전트, AI 웹툰/애니메이션 생성기, AI 논문 번역/분석기, 고객 상담 시스템)을 영속성 아키텍처로 무료 빌드할 수 있게 지원합니다.

## 2. 보안 취약점 분석 (CVE-2026-7065)
- **SSRF(Server-Side Request Forgery) 발생**:
    - unauthenticated remote file upload API의 입력 검증 미비로 인해 외부 임의 호스트에 대기열 쿼리나 서버리스 내부 요청을 보내도록 조종하는 SSRF 공격이 가능함.
    - 보안 정책 상 격리망에 있는 API Spec MCP Server나 클라우드 자격 증명 정보를 유출할 수 있어, Artifactory 프록시 필터 및 격리망 강제가 중요함.

---
**관련 문서**:
- [[wiki/Engineering/Data-and-Security/SkillSpector-에이전트-스킬-보안-취약점-스캐너.md]]

