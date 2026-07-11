---
title: "Insane-Search: 다중 소스 웹 데이터 추출 오픈소스"
related_raw: ["[[Reddit, Youtube, X, LinkedIn, Hacker News, 네이버 블로그, 쿠팡, 한국 언론사 기사를 막힘없이 가져올 수 있게 ᄃ.md]]"]
tags: ["Engineering", "Infrastructure", "Web_Scraping", "Claude_Code", "Open_Source", "Insane-Search"]
type: "wiki"
status: "published"
last_updated: "2026-05-15"
updated: "2026-05-15"
---

# Insane-Search: 에이전트를 위한 만능 웹 데이터 수집기

## 1. 개요
Insane-Search는 별도의 서비스별 API 키 설정이나 OAuth 인증 없이도 Reddit, YouTube, X(Twitter), LinkedIn, 네이버 블로그 등 다양한 플랫폼의 실시간 데이터를 가져올 수 있게 돕는 오픈소스 도구입니다. 특히 Claude Code와 같은 터미널 기반 에이전트와의 연동에 최적화되어 있습니다.

## 2. 핵심 메커니즘: 다중 폴백(Fallback) 전략
이 도구의 명칭이 'Insane(미친)'인 이유는 데이터 추출을 위해 **"A 방법이 안 되면 B로, B가 안 되면 C로"** 어떻게든 데이터를 가져오는 끈질긴 시도 방식 때문입니다.
- **비로그인 접근**: 복잡한 인증 절차 없이 공개된 인터페이스를 최대한 활용.
- **다양한 소스 지원**:
    *   커뮤니티: Reddit, Hacker News
    *   SNS/미디어: X, YouTube, LinkedIn
    *   국내 특화: 네이버 블로그, 한국 언론사 기사
    *   쇼핑: 쿠팡

## 3. 주요 활용 사례
- **실시간 트렌드 분석**: "r/LocalLLaMA에서 현재 가장 핫한 주제가 뭐야?"와 같은 질문에 실시간 커뮤니티 데이터를 바탕으로 답변.
- **콘텐츠 요약**: 유튜브 영상 URL만으로 즉각적인 내용 요약 및 분석 수행.
- **시장 조사**: 특정 카테고리(예: 쿠팡 키보드)의 가격대 및 유저 리뷰 실시간 수집.
- **에이전트 검색 강화**: LLM이 학습하지 못한 최신 뉴스나 블로그 포스트를 읽고 작업에 반영.

## 4. 프로젝트 링크
- **Original (Claude Code용)**: [fivetaku/insane-search](https://github.com/fivetaku/insane-search)
- **Codex 버전**: [sinmb79/codex-insane-search](https://github.com/sinmb79/codex-insane-search)

## 관련 문서
- [[wiki/Engineering/Infrastructure-and-DevOps/000_Infrastructure-and-DevOps-MOC.md|인프라 및 DevOps MOC]]
- [[wiki/Engineering/AI-Native-Engineering/Claude-Code-Karpathy-Guidelines.md|Claude Code 가이드라인]]
- [[wiki/RAG/000_RAG-MOC.md|RAG MOC]]
