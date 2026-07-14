---
name: km-linter
description: 지식 베이스의 구조적 무결성을 점검하고 `index.md`, `log.md`를 Agent-Centric v1 포맷으로 최신화합니다.
---

# KM_LINTER_AGENT_v1

## 🎯 OBJECTIVE
지식 베이스의 기계 가독성(Machine-readability)을 유지하고 구조적 결함을 자동 수정함.

## 📋 WORKFLOW

### 1. INTEGRITY_CHECK
- **ORPHANED_NOTES**: `wiki/` 내 인바운드 링크(`[[ ]]`)가 0개인 파일을 추출함.
- **DEAD_LINKS**: `[[ ]]`로 참조되었으나 실제 파일이 존재하지 않는 문서 목록을 추출함.
- **PATH_SYNC**: 파일 이동으로 인해 발생한 잘못된 경로 링크를 `fix_wiki_links.py` 로직을 사용하여 현재 실제 경로로 자동 수정함.
- **DATE_SYNC**: GitHub Pages 빌드 시 날짜 왜곡(빌드 날짜로 초기화되는 현상)을 방지하기 위해, frontmatter에 `last_updated` 필드 값을 기반으로 한 `updated` 필드가 올바르게 입력되어 있는지 점검하고 일치시킴.

### 2. INDEX_REFRESH (index.md) - 필수 수행
- `index.md`를 **KM_INDEX_AGENT_v1** 포맷으로 **무조건 최신화**함.
- `📂 CATEGORIES_MOC`: 모든 핵심 MOC 파일 링크 최신 상태 유지.
- `🌲 DIRECTORY_MAPPING`: `wiki/` 내의 신규 폴더 및 구조적 변화를 전수 반영.
- `📌 KEY_FILE_LIST`: 카테고리별 파일 개수 및 상태 요약 데이터 갱신.

### 3. LOG_ENTRY (log.md) - 필수 수행
- 수행된 모든 작업을 **KM_LOG_AGENT_v1** 테이블 형식으로 기록함.
- `DATE | ACTION | SCOPE | FILES | SUMMARY` 형식을 엄격히 준수하여 `log.md` 하단에 추가함.
- **`log.md`는 append-only 누적 원장**: 기간이 지났다는 이유로 과거 행을 삭제·prune하지 않음. (데일리 노트·`raw/` 클린업과 별개)

## ⚠️ CONSTRAINTS
- 모든 내부 링크는 `[[wiki/Category/Sub/Filename.md]]` 형태의 전체 상대 경로를 권장함.
- 설명이나 수식어는 배제하고 데이터 중심(Data-centric)으로 작성함.
- `log.md` 자동 삭제는 수행하지 않음.
