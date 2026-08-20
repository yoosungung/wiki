---
id: composite-grain-join-keys
title: "복합 grain 조인 키 (팩트↔이벤트)"
status: canonical
owner: km
updated: "2026-08-20"
last_updated: "2026-08-20"
review_after: "2026-11-20"
sources:
  - ticket:690
  - ticket:685
  - ticket:691
  - ticket:1048
tags: ["Agents", "Text-to-SQL", "MDL", "Joins"]
type: "wiki"
---

# 복합 grain 조인 키 (팩트↔이벤트)

이벤트 테이블을 `ball_id`→`match_id`처럼 **키 하나**로 조인하면 grain이 붕괴한다. 금 SQL이 `match_id + over_id + ball_id + innings_no` 합성키를 쓰면 MDL relationship도 동일해야 한다.

## 체크

| 함정 | 교정 |
| :--- | :--- |
| 점수 테이블에 player_id가 없음 | grain 테이블의 striker/batter 컬럼으로 조인 |
| 위켓 `player_id`가 실제론 `player_out` | 물리 컬럼 alias + 관계 대상 명시. 투수 `player_id`(bowler)와 구분 |
| 카탈로그 검색은 맞는데 EX mismatch | 조인 키·striker 누락. 마지막 SSE가 `SELECT * FROM dim` 탐색이면 채점 SQL이 덮임 |
| 임계 `>` vs `>=` | 커리어 SUM 후 AVG가 다른 집합을 만듦. 기존 `matches_50_plus` 컬럼 재사용 금지 |
| 볼링 legal balls | 와이드/노볼(`extra_runs`) 제외. 배팅 SR 분모와 섞지 않음 |
| 창고 일자가 `whsle_date`인데 alias `date` | 물리 grain 컬럼을 쓰고, 계산 `date`+기간 `refSql` seal로 `.date` sql_exec를 막음 |
| 월말 질문이 서로 다른 grain | 누적 zero-fill vs 최신월 성장 vs prior_balance vs 30일 rolling max를 **질문별 seal**로 격리. 공용 vocab이 FROM-leak 유발 |

MDL description에 “ball-key / striker” vocab을 넣고 search 회귀를 고정한다. 프롬프트에 리그명을 하드코딩하지 않는다 — [[wiki/Agents/Text-to-SQL/MDL-Only-Domain-Knowledge.md]].

## 관련

- [[wiki/Agents/Text-to-SQL/Semantic-View-Single-Master.md]]
- [[wiki/Agents/Text-to-SQL/RefSql-Seal-for-EX-Mismatch.md]]
- [[wiki/Agents/Text-to-SQL/Spider2-Quality-Gate-nl2sql.md]]
