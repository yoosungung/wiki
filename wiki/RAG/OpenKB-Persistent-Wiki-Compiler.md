---
title: "OpenKB: 지속적 위키 컴파일러, PageIndex 벡터리스 트리 추론 및 스킬 팩토리"
last_updated: "2026-09-04"
updated: "2026-09-04"
related_raw: ["[[2026-09-04-openkb-persistent-wiki-compiler-pageindex.md]]"]
tags: ["RAG", "OpenKB", "PageIndex", "Vectorless-RAG", "Persistent-Wiki", "Skill-Factory", "Obsidian"]
type: "wiki"
status: "published"
---

# OpenKB: 지속적 위키 컴파일러, PageIndex 벡터리스 트리 추론 및 스킬 팩토리

**OpenKB (Open Knowledge Base)**는 문서를 파편화된 청크(Chunks)로 쪼개어 임베딩하는 전통적 RAG의 한계를 극복하고, 안드레이 카파시(Andrej Karpathy)가 제안한 **"문서 집합을 상호 연결된 지속적 위키로 컴파일(Compile)하는 패러다임"**을 구현한 오픈소스 지식 관리 및 검색 시스템입니다.

```mermaid
graph TD
    RawDocs[다양한 원천 문서: PDF, Word, PPT, MD, Web] --> Compiler[OpenKB LLM Compiler]
    Compiler --> PersistentWiki[지속적 위키: 요약문, 개념 페이지, 엔티티, [[위키링크]]]
    PersistentWiki --> PageIndex[PageIndex 계층형 트리 추론 엔진]
    PersistentWiki --> SkillFactory[Skill Factory: 배포 가능한 에이전트 스킬 추출]
    PageIndex --> AgentQuery[에이전트 질의 응답: 출처 인용 및 전역 맥락 조망]
    SkillFactory --> CodingAgents[Claude Code / Codex / Gemini CLI 스킬 설치]
```

---

## 1. 전통적 RAG vs OpenKB 위키 컴파일 패러다임

| 비교 항목 | 전통적인 Chunk RAG | OpenKB 지속적 위키 컴파일 |
| :--- | :--- | :--- |
| **지식 표현** | 원시 텍스트 청크 벡터 임베딩 | 상호 연결된 마크다운 위키 (개념·엔티티 페이지) |
| **시간에 따른 지식** | 문서 추가 시 파편화 심화, 매 쿼리마다 원점 재탐색 | 신규 문서가 기존 위키에 합성되어 **지식의 복리(Compounding) 축적** |
| **긴 문서 처리** | 청크 분할로 인한 문맥 단절 (Context Lost) | **PageIndex** 벡터리스 계층 트리 기반 전체 구조 보존 추론 |
| **에이전트 재사용성** | 시스템 내 질의응답에 한정 | **Skill Factory**를 통한 에이전트 실행 스킬(`SKILL.md`) 추출 |
| **도구 호환성** | 전용 벡터 DB 종속 | **Obsidian** 호환 순수 마크다운(`[[wikilinks]]`) |

---

## 2. 핵심 아키텍처 및 모듈

### 2.1. PageIndex 벡터리스 추론 엔진 (Vectorless Reasoning Retrieval)
- 임베딩 벡터 간 코사인 유사도에 의존하지 않고, 문서의 목차, 시각적 레이아웃, 표, 다이어그램을 보존하는 **계층형 트리 구조(Hierarchical Tree Index)**를 생성합니다.
- LLM이 트리의 상위 노드부터 하위 세부 단락까지 단계적으로 추론(Tree Navigation)하여, 복합 다단계 질문에 대해 문서 전반을 조망하는 정밀한 근거를 인출합니다.

### 2.2. 스킬 팩토리 (Skill Factory)
- 축적된 도메인 위키 지식으로부터 특정 태스크를 자동 수행할 수 있는 절차적 지식을 증류(Distill)하여 표준 스킬 패키지로 변환합니다.
- Claude Code, OpenAI Codex, Gemini CLI 등 현대 터미널 에이전트가 즉시 로드하여 사용할 수 있는 `SKILL.md` 포맷으로 내보냅니다.

### 2.3. Obsidian 및 Knowledge Workbench 통합
- 생성된 모든 위키 파일은 표준 마크다운과 `[[문서명]]` 위키링크를 따르므로 Obsidian의 그래프 뷰(Graph View)와 로컬 플러그인 생태계를 100% 활용할 수 있습니다.
- 브라우저 기반의 웹 UI인 **Knowledge Workbench**를 번들 제공하여 비개발자도 손쉽게 지식을 업로드하고 인터랙티브 질의를 수행할 수 있습니다.

---

## 3. CLI 명령어 및 파이프라인 워크플로우

```bash
# 1. OpenKB CLI 설치
pip install openkb

# 2. 문서 디렉터리를 분석하여 지속적 위키 컴파일
openkb compile --input="./documents" --output="./vault/wiki" --format=obsidian

# 3. 신규 문서 증분 합성 (Incremental Synthesis)
openkb ingest --file="./new_paper.pdf" --wiki="./vault/wiki"

# 4. 위키 지식으로부터 Claude Code / Gemini CLI용 에이전트 스킬 증류
openkb export-skill --topic="kubernetes-troubleshooting" --out="./skills/k8s-troubleshooter"

# 5. 로컬 Knowledge Workbench 웹 UI 실행
openkb serve --port=8080
```

---

## 🔗 관련 문서
- [[wiki/RAG/PageIndex-Vectorless-Reasoning-RAG.md|PageIndex 벡터리스 추론 RAG]]
- [[wiki/RAG/OpenWiki-OKF-Codebase-Documentation.md|OpenWiki OKF 코드베이스 문서화]]
- [[wiki/Agents/Self-Evolving/WikiSkill-절차적-지식-자가-진화-프레임워크.md|WikiSkill 절차적 지식 자가 진화 프레임워크]]
- [[wiki/RAG/000_RAG-MOC.md|RAG MOC]]
