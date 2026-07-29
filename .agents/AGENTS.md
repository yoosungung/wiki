# 프로젝트 가이드: KM (Knowledge Management)

이 저장소는 범용적인 지식 관리를 위한 **Obsidian Vault**입니다. 이 파일은 **Cursor Agent** 및 기타 AI 코딩 에이전트를 위한 지침과 맥락을 제공합니다.

> **Canonical copy**: 저장소 루트의 [`AGENTS.md`](../AGENTS.md)와 동기화됩니다.

## 프로젝트 개요

- **목적**: 다양한 주제에 관한 기술 문서, 연구 자료, 아이디어 및 지식의 체계적 관리와 축적.
- **구조**: `raw/`(원본), `wiki/`(합성/요약), `assets/`(첨부파일) 3계층 구조를 기본으로 합니다.

## 개발 및 사용 원칙

1. **언어**: 모든 문서는 **한국어**로 작성하는 것을 원칙으로 합니다.
2. **내용의 성격**: 사실에 기반한 객관적인 지식 기록을 중시하며, 단순 메모를 넘어선 지식의 연결과 합성을 지향합니다.
3. **지식 연결**: Obsidian의 백링크(`[[ ]]`) 및 태그 기능을 활용하여 지식 간의 연결성을 극대화합니다.
4. **보안**: 자격 증명, API 키 또는 민감한 개인 정보는 이 저장소에 절대 포함하지 않습니다.

## Cursor Agent Skills

에이전트 자율 작업을 위한 4가지 스킬이 `.agents/skills/`에 정의되어 있습니다.

| 스킬 | 경로 | 용도 |
|------|------|------|
| km-ingestor | `.agents/skills/km-ingestor/SKILL.md` | 외부 정보를 `raw/`에 저장·메타데이터 표준화 |
| km-synthesizer | `.agents/skills/km-synthesizer/SKILL.md` | `raw/` → `wiki/` 지식 합성 |
| km-researcher | `.agents/skills/km-researcher/SKILL.md` | `연구_주제_관리.md` 기반 자동 탐색 |
| km-linter | `.agents/skills/km-linter/SKILL.md` | 구조 무결성 점검, `INDEX.md`/`log.md` 갱신 |

상세 운영 원칙·Obsidian CLI 가이드는 루트 [`AGENTS.md`](../AGENTS.md)를 참조하세요.
