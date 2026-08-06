---
id: publication-gate-empty-overwrite-guard
title: "퍼블리시 게이트 + 빈 산출물 덮어쓰기 금지"
status: canonical
owner: km
updated: "2026-08-06"
last_updated: "2026-08-06"
review_after: "2026-11-06"
sources:
  - schedule:publication-safety
  - schedule:issue-radar
  - ticket:167
tags: ["Engineering", "AI-Native", "Publish", "Safety", "Git"]
type: "wiki"
---

# 퍼블리시 게이트 + 빈 산출물 덮어쓰기 금지

공개/공유 데이터 파일을 자동 커밋하는 잡에서 **게이트 통과 ≠ push 가능**, **수집 실패 ≠ 빈 파일로 덮어쓰기**를 분리한다.

## 1) Pre-push publication gate

```bash
# 개념: origin/main 대비 워킹트리/ahead 커밋 검사
python agent/publication_gate.py --base origin/main
# exit 0 = PASS, exit 2 / PUBLICATION HOLD = hold (push 금지)
```

게이트 PASS 후에도 git push 403이면 **자격 증명/ACL 문제** — [[wiki/Engineering/Infrastructure-and-DevOps/GitHub-Fine-Grained-PAT-Contents-Write-Probe.md]] (remote 임베디드 PAT vs env `GH_TOKEN` 불일치 포함).

## 2) Empty overwrite guard

외부 API/시드 확장이 비어 점수 미달 → `candidates=[]` / `items=[]`일 때:

- **공개 큐 파일을 빈 내용으로 커밋하지 않는다** (마지막 정상 생성분을 보존).
- 원인(미설정 env, 쿼터, 스키마)을 로그·티켓에 남기고 재실행 조건을 명시한다.

## 적용 체크

1. 게이트 스크립트가 CI/스케줄 **push 직전**에 있는가?
2. “변경 없음 / 빈 결과”와 “안전한 갱신”을 구분하는가?
3. push 실패를 게이트 실패와 혼동하지 않는가?

## 분기·스택 운영

- 로컬 `main`이 미공개 Pass 스택으로 `origin/main`과 diverge면, curation/radar 잡은 **`origin/main`에 detach → 작업 → `push HEAD:main` → 로컬 스택 checkout**으로 보존한다. dirty leftover `agent/cron/` WIP가 이미 PR로 들어갔으면 ff-only pull 전에 정리.
- yaml↔wiki orphan 0을 유지하려면 stub yaml 추가 시 **최소 wiki stub도 같이 seed**.
- 공개 전 제거: placeholder/unknown·SSoT 없는 slug·불완전 신원 stub·기관을 people로 링크한 stance.

## 🔗 관련 문서

- [[wiki/Engineering/Infrastructure-and-DevOps/GitHub-Fine-Grained-PAT-Contents-Write-Probe.md]]
- [[wiki/Engineering/AI-Native-Engineering/Wiki-Synthesis-Policy.md]]
